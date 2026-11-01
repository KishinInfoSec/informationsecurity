#!/usr/bin/env python3
"""
Read a driven Claude Code session's own transcript instead of guessing from pixels.

A session started in <repo> writes JSONL to
  ~/.claude/projects/<mangled-repo-path>/<session-uuid>.jsonl

That file is ground truth for what the driven agent did. It answers three questions
a screenshot cannot answer reliably:

  is it finished?   see "How completion is detected" below. This is the subtle part.
  what did it say?  the last assistant text block, verbatim, no OCR.
  what did it read? every file-touching tool call, so "did it cheat by re-reading
                    the file it was supposed to recall" is a fact, not a hope.

A caveat to take seriously: Anthropic's own docs say the transcript format "is
internal to Claude Code and changes between versions, so scripts that parse these
files directly can break on any release." Everything here is therefore written
defensively: unknown record types are ignored rather than assumed away, and no
single field is load-bearing on its own.

How completion is detected
--------------------------
Claude Code appends {"type":"system","subtype":"turn_duration"} when a turn ends.
That record is real but undocumented, and it is emitted INCONSISTENTLY. Measured
across 17 local transcripts on one machine: a 126-prompt session had 134 of them,
a 128-prompt session had 20, and two sessions had none at all.

Waiting only on it has a nasty failure shape. When it never arrives, a watcher
reports a stall, and a caller that treats "stalled" as "waiting for permission"
will send an approval keystroke into a session that already finished.

So completion is decided by two independent signals:

  FAST   a new turn_duration record appears.
  QUIET  the transcript stops growing for --idle seconds AND the last assistant
         message has no tool_use left without a matching tool_result.

The second condition separates "finished" from "blocked". A session waiting at a
permission prompt has an unanswered tool_use as its last act; a finished one does
not. Every exit says which signal fired.

Usage
  session_watch.py dir      --repo <path>
  session_watch.py sessions --repo <path>
  session_watch.py mark     --repo <path>
  session_watch.py wait     --repo <path> [--timeout 900] [--idle 45]
  session_watch.py last     --repo <path>
  session_watch.py reads    --repo <path> [--since N] [--match CLAUDE.md]

Exit codes
  0  done (for `wait`: a turn completed)
  1  not found, or timed out
  2  BLOCKED: idle with an unanswered tool call, i.e. a prompt is waiting
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"

FILE_TOOLS = ("Read", "Grep", "Glob", "Edit", "Write", "NotebookEdit")
CMD_TOOLS = ("Bash", "PowerShell")


def mangle(repo: str) -> str:
    r"""C:\Users\me\my project  ->  C--Users-me-my-project

    The documented rule is EVERY non-alphanumeric character becomes a hyphen, not
    just the path separators. A folder with a space, a dot or a parenthesis in it
    is common enough that getting this wrong means the directory is simply never
    found, with a "the session never started" message pointing at the wrong cause.
    """
    return re.sub(r"[^A-Za-z0-9]", "-", str(Path(repo).resolve()))


def session_dir(repo: str) -> Path:
    """Resolve the project directory, tolerating drive-letter case on Windows.

    Claude Code has been observed writing this folder with an upper-case drive
    letter while looking it up with a lower-case one. Deriving the name and
    trusting it therefore fails intermittently on Windows for no visible reason,
    so the derived name is only a candidate: what is actually on disk wins.
    """
    want = mangle(repo)
    exact = PROJECTS / want
    if exact.is_dir():
        return exact
    if PROJECTS.is_dir():
        for d in PROJECTS.iterdir():
            if d.is_dir() and d.name.lower() == want.lower():
                return d
    print(f"NO_SESSION_DIR: {exact}")
    print("The driven session has not started, or it started in a different cwd.")
    print("Check the terminal's working directory before assuming anything else.")
    sys.exit(1)


PIN: str | None = None  # set from --session; pins one session out of many


def transcripts(repo: str) -> list[Path]:
    """Every transcript for this project, including subagent transcripts.

    A driven session that dispatches subagents writes their turns to
    <sessionId>/subagents/agent-<id>.jsonl, not inline in the parent file. Reading
    only the parent misses everything a subagent did, which for an audit question
    ("what files did it actually touch") is exactly the part you wanted.
    """
    d = session_dir(repo)
    return sorted(d.glob("*.jsonl")) + sorted(d.glob("*/subagents/*.jsonl"))


def latest(repo: str) -> Path:
    # With several sessions open in one repo, "newest by mtime" is whichever wrote
    # last, not necessarily the one being driven. Pin it with --session.
    d = session_dir(repo)
    if PIN:
        hits = sorted(d.glob(f"{PIN}*.jsonl"))
        if not hits:
            print(f"NO_SUCH_SESSION: {PIN} in {d}")
            sys.exit(1)
        return hits[0]
    files = sorted(d.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not files:
        print(f"NO_TRANSCRIPTS in {d}")
        sys.exit(1)
    return files[-1]


def records(p: Path) -> list[dict]:
    out = []
    # errors="replace" plus a per-line try: the file is appended to while we read,
    # so the last line is routinely a half-written fragment.
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    for line in text.splitlines():
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def turn_ends(recs: list[dict]) -> list[int]:
    return [i for i, d in enumerate(recs)
            if d.get("type") == "system" and d.get("subtype") == "turn_duration"]


def _content(d: dict) -> list:
    c = (d.get("message") or {}).get("content")
    return c if isinstance(c, list) else []


def assistant_texts(recs: list[dict]) -> list[str]:
    out = []
    for d in recs:
        if d.get("type") != "assistant":
            continue
        for c in _content(d):
            if isinstance(c, dict) and c.get("type") == "text" and c.get("text", "").strip():
                out.append(c["text"])
    return out


def turn_in_flight(recs: list[dict]) -> bool:
    """True if the newest user prompt has not been answered by a completed turn.

    This is the honest replacement for a wrong assumption. It is tempting to
    detect a waiting permission prompt as "a tool_use with no tool_result", and
    that is simply not how Claude Code writes its transcript. Verified against
    v2.1.266 by watching a live prompt: the user record is written, then the
    prompt appears on screen with NOTHING written, and only when it is approved
    do the tool_use and its tool_result get appended together.

    So a waiting permission prompt is invisible here. What this function can say
    is whether the turn is still open, which combined with a quiet transcript
    means "either thinking or waiting at a prompt" - and only a screenshot can
    tell those apart.
    """
    last_prompt = -1
    for i, d in enumerate(recs):
        if d.get("type") != "user":
            continue
        # A tool_result also arrives as a "user" record. Only a real prompt counts.
        if any(isinstance(c, dict) and c.get("type") == "tool_result"
               for c in _content(d)):
            continue
        last_prompt = i
    if last_prompt < 0:
        return False
    ends = turn_ends(recs)
    return not ends or ends[-1] < last_prompt


def pending_tool_calls(recs: list[dict]) -> list[str]:
    """Tool calls with no matching tool_result: a tool that is RUNNING.

    Not a permission prompt. See turn_in_flight above for why: the tool_use is
    only written once the call has been approved, so an unanswered one means the
    command is executing (or the process died mid-call), never that something is
    waiting to be allowed.
    """
    issued: dict[str, str] = {}
    answered: set[str] = set()
    for d in recs:
        for c in _content(d):
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use" and c.get("id"):
                issued[c["id"]] = c.get("name", "?")
            elif c.get("type") == "tool_result" and c.get("tool_use_id"):
                answered.add(c["tool_use_id"])
    return [name for tid, name in issued.items() if tid not in answered]


def pending_tool_details(recs: list[dict]) -> list[tuple[str, str]]:
    """(tool, what it actually wants to do) for every unanswered tool call.

    `pending_tool_calls` answers "is it blocked". This answers "on what", which
    is the part a human needs before approving anything. Reading the real command
    out of the transcript is the difference between an audit trail and a
    click-through: the old loop printed the last thing in the transcript and
    called it the pending call, which is not the same thing at all.
    """
    issued: dict[str, tuple[str, str]] = {}
    answered: set[str] = set()
    for d in recs:
        for c in _content(d):
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use" and c.get("id"):
                inp = c.get("input", {}) or {}
                detail = (inp.get("command") or inp.get("file_path")
                          or inp.get("path") or inp.get("pattern")
                          or inp.get("url") or "")
                issued[c["id"]] = (c.get("name", "?"), str(detail))
            elif c.get("type") == "tool_result" and c.get("tool_use_id"):
                answered.add(c["tool_use_id"])
    return [v for k, v in issued.items() if k not in answered]


def tool_reads(recs: list[dict], start: int) -> list[tuple[str, str]]:
    hits = []
    for d in recs[start:]:
        for c in _content(d):
            if not isinstance(c, dict) or c.get("type") != "tool_use":
                continue
            name = c.get("name", "")
            inp = c.get("input", {}) or {}
            path = inp.get("file_path") or inp.get("path") or inp.get("pattern") or ""
            if name in FILE_TOOLS and path:
                hits.append((name, str(path)))
            elif name in CMD_TOOLS and (cmd := str(inp.get("command", ""))):
                hits.append((name, cmd[:200]))
    return hits


def _print_final(recs: list[dict], how: str) -> None:
    print(f"TURN_COMPLETE ({how})")
    print(f"RECORDS: {len(recs)}")
    if texts := assistant_texts(recs):
        print("\n--- final assistant message ---")
        print(texts[-1][:4000])


def cmd_wait(a) -> int:
    p = latest(a.repo)
    base = len(turn_ends(records(p)))
    deadline = time.time() + a.timeout
    print(f"Waiting for a turn to complete in {p.name} (baseline {base} turns)...")

    last_count = len(records(p))
    last_change = time.time()

    while time.time() < deadline:
        # Re-resolve every poll. /compact keeps the same file, but /branch and
        # --fork-session start a new one, and a cached path would then follow a
        # session nobody is driving.
        p = latest(a.repo)
        recs = records(p)

        if len(turn_ends(recs)) > base:
            _print_final(recs, "turn_duration record")
            return 0

        if len(recs) != last_count:
            last_count = len(recs)
            last_change = time.time()
            time.sleep(a.poll)
            continue

        idle = time.time() - last_change
        if idle < a.idle:
            time.sleep(a.poll)
            continue

        if not turn_in_flight(recs):
            _print_final(recs, f"quiet {int(idle)}s, turn closed")
            return 0

        pending = pending_tool_calls(recs)
        if pending:
            print(f"RUNNING: quiet for {int(idle)}s with a tool still executing: "
                  f"{', '.join(sorted(set(pending)))}")
            print(f"RECORDS: {len(recs)}")
            print("Long-running command, or the process died mid-call. Screenshot")
            print("before deciding which.")
            return 2

        print(f"BLOCKED: quiet for {int(idle)}s with the turn still open and")
        print("nothing executing. That is what a permission prompt looks like from")
        print("here, because Claude Code writes nothing to the transcript while one")
        print("is waiting.")
        print(f"RECORDS: {len(recs)}")
        print("The transcript cannot tell you what it is asking. Screenshot the")
        print("window, read the command, and answer it deliberately.")
        return 2

    print(f"TIMEOUT after {a.timeout}s.")
    print("Neither a completion record nor a quiet period appeared, so the agent")
    print("is probably still working. Screenshot before concluding anything.")
    return 1


def main() -> int:
    # Windows defaults stdout to cp1252 when redirected, and agent output is full
    # of characters it cannot encode. Without this, piping a transcript to a file
    # dies mid-write and leaves an empty file behind. newline="\n" matters as much:
    # Python emits CRLF on Windows and the stray CR breaks shell comparisons.
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", newline="\n")
        except Exception:
            pass

    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["dir", "sessions", "mark", "wait", "last", "reads"])
    ap.add_argument("--repo", required=True)
    ap.add_argument("--since", type=int, default=0, help="baseline index from `mark`")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--idle", type=int, default=45,
                    help="seconds of silence before deciding done-or-blocked")
    ap.add_argument("--poll", type=float, default=3.0)
    ap.add_argument("--match", default=None, help="only show reads containing this")
    ap.add_argument("--session", default=None, help="pin one session uuid (prefix ok)")
    ap.add_argument("--all", action="store_true",
                    help="for `reads`: include subagent transcripts too")
    a = ap.parse_args()

    global PIN
    PIN = a.session

    if a.cmd == "sessions":
        for p in sorted(session_dir(a.repo).glob("*.jsonl")):
            print(p.stem)
        return 0

    if a.cmd == "dir":
        print(session_dir(a.repo))
        print(latest(a.repo))
        subs = [p for p in transcripts(a.repo) if "subagents" in p.parts]
        if subs:
            print(f"({len(subs)} subagent transcript(s) also present)")
        return 0

    if a.cmd == "mark":
        p = latest(a.repo)
        recs = records(p)
        print(f"TRANSCRIPT: {p}")
        print(f"MARK: {len(recs)}")
        print(f"TURNS_COMPLETE: {len(turn_ends(recs))}")
        return 0

    if a.cmd == "wait":
        return cmd_wait(a)

    if a.cmd == "last":
        texts = assistant_texts(records(latest(a.repo)))
        if not texts:
            print("NO_ASSISTANT_TEXT")
            return 1
        print(texts[-1])
        return 0

    if a.cmd == "reads":
        files = transcripts(a.repo) if a.all else [latest(a.repo)]
        hits = []
        for f in files:
            sub = "subagents" in f.parts
            tag = "  (subagent)" if sub else ""
            # --since is a record INDEX into the parent transcript. A subagent
            # writes its own file with its own index space, where that number
            # means nothing: applying it there skips most of a short transcript
            # and reports NONE. Measured live, a subagent that had just run a
            # find across the repo audited as having touched nothing, which is
            # the most misleading answer this command can give. A subagent file
            # is one dispatched task, so it is read whole and labelled.
            start = 0 if sub else a.since
            hits += [(t, p + tag) for t, p in tool_reads(records(f), start)]
        if a.match:
            hits = [h for h in hits if a.match.lower() in h[1].lower()]
        if not hits:
            print("NONE" + (f" matching {a.match!r}" if a.match else ""))
            return 0
        for tool, path in hits:
            print(f"{tool:8} {path}")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
