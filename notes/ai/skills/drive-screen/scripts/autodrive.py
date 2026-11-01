#!/usr/bin/env python3
"""
Run a driven Claude Code session to the end of a turn, answering its permission
prompts, and stop the moment anything looks like it needs a human.

This answers prompts inside the DRIVEN SESSION'S OWN terminal UI. It has nothing
to do with operating-system dialogs and cannot answer one: every keystroke it
sends goes to the editor window you name.

What it does differently from a naive approval loop
---------------------------------------------------
The obvious version watches for the driven session to go quiet and assumes
silence means a prompt is waiting. Silence does not mean that. A finished turn
and a waiting prompt are identical from outside, so that version answers prompts
that are not there, and types into a session that has already stopped.

This one reads the transcript to decide whether the turn is still open, which
is the part the transcript can actually answer.

What it cannot answer, verified live against v2.1.266: a waiting permission
prompt writes NOTHING. The user record lands, the prompt appears on screen with
no transcript activity at all, and only when it is approved do the tool_use and
its tool_result get appended together. So an unanswered tool_use means a command
is RUNNING, never that one is waiting to be allowed.

That leaves the screen as the only place a pending prompt exists. So on a quiet,
still-open turn this screenshots the window and stops, and a human or a
vision-capable agent reads the image and approves. --approve-blind will press
Enter without that step, and is off by default because it approves a command
nobody has read.

It also presses Enter rather than typing a digit. Enter accepts the highlighted
option, which is approve-once. Typing "2" selects the variant that stops asking,
and for a Bash command that writes a permanent rule into the repository's
settings, unattended, which is not a thing to do while nobody is watching.

  autodrive.py --title "<window>" --repo <path> [--session <uuid>]
               [--max 25] [--timeout 900] [--idle 45]
               [--shot-dir <dir>] [--dry-run]

Exit codes
  0  the turn completed
  1  timed out with the agent still working
  2  approvals are not reaching the session, the prompt could not be
     photographed, or the cap was hit
  3  stopped deliberately for a human: a prompt is waiting and needs reading,
     a command matched the refuse list, or --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import session_watch as sw  # noqa: E402

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", newline="\n")
    except Exception:
        pass


# Commands this will never approve on its own. The point is not to be a security
# boundary, because a determined mistake can be spelled around any regex. The
# point is that the class of thing you most regret approving while away is small,
# well known, and cheap to stop on. Anything matching hands control back with the
# command printed, and you approve it yourself or you do not.
REFUSE = [
    (r"\brm\s+(-\w*\s+)*-\w*[rf]", "recursive or forced delete"),
    (r"\brmdir\s+/s", "recursive delete"),
    (r"\bgit\s+push\b.*(--force|-f)\b", "force push"),
    (r"\bgit\s+reset\s+--hard\b", "discards working tree"),
    (r"\bgit\s+clean\b.*-\w*[fdx]", "deletes untracked files"),
    (r"\bsudo\b", "privilege escalation"),
    (r"\b(curl|wget|iwr|Invoke-WebRequest)\b[^|]*\|\s*(sudo\s+)?(ba|z|)sh",
     "pipes the network into a shell"),
    (r"\bdd\s+if=", "raw disk write"),
    (r"\b(mkfs|diskpart|format)\b", "formats a volume"),
    (r"\b(shutdown|reboot|Restart-Computer|Stop-Computer)\b", "restarts the machine"),
    (r"\b(npm|pnpm|yarn)\s+publish\b", "publishes a package"),
    (r"\bgh\s+release\s+create\b", "publishes a release"),
    (r"\bDROP\s+(TABLE|DATABASE|SCHEMA)\b", "destructive SQL"),
    (r"\bDELETE\s+FROM\b(?!.*\bWHERE\b)", "unfiltered DELETE"),
    (r"\btruncate\b", "truncates data"),
    (r"\bkill(all)?\b|\btaskkill\b|\bStop-Process\b", "kills processes"),
    (r"\bchmod\s+(-R\s+)?777\b", "world-writable permissions"),
    (r"\b(Remove-Item|del)\b.*-Recurse", "recursive delete"),
]

# These never carry a destructive command, so they are approved without matching.
SAFE_TOOLS = {"Read", "Grep", "Glob", "NotebookRead", "TodoWrite"}


def refuses(tool: str, detail: str) -> str | None:
    if tool in SAFE_TOOLS:
        return None
    for pattern, why in REFUSE:
        if re.search(pattern, detail, re.IGNORECASE):
            return why
    return None


def _target(a) -> list:
    return ["--id", a.id] if a.id else ["--title", a.title]


def screenctl(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, os.path.join(HERE, "screenctl.py"), *args],
                          capture_output=True, text=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", help="window holding the driven session")
    # Prefer --id for a driven agent. Claude Code renames its own terminal window
    # as it works: launched as "DRIVE-TEST" it became "claude", then
    # "* Claude Code". A title captured at launch stops matching mid-run, and a
    # generic one collides with whatever else is open.
    ap.add_argument("--id", help="target the window by handle from `screenctl.py list`")
    ap.add_argument("--repo", required=True, help="repo the driven session runs in")
    ap.add_argument("--session", default=None, help="pin one session uuid (prefix ok)")
    ap.add_argument("--max", type=int, default=25, help="approval cap")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--idle", type=int, default=45)
    ap.add_argument("--poll", type=float, default=3.0)
    ap.add_argument("--shot-dir", default=None,
                    help="screenshot before every approval, into this directory")
    # The transcript cannot say what a prompt is asking, so this approves
    # commands nobody has read. Off by default for that reason.
    ap.add_argument("--approve-blind", action="store_true",
                    help="press Enter on a detected prompt without reading it")
    ap.add_argument("--dry-run", action="store_true",
                    help="report the first prompt and what it would do, approve nothing")
    a = ap.parse_args()

    if not (a.title or a.id):
        print("NO_TARGET: pass --title or --id")
        return 3

    sw.PIN = a.session
    path = sw.latest(a.repo)
    base_turns = len(sw.turn_ends(sw.records(path)))
    print(f"Driving {path.name} in {(a.id or a.title)!r} (baseline {base_turns} turns, "
          f"cap {a.max} approvals)")
    if a.dry_run:
        print("DRY RUN: nothing will be sent.")

    approvals = 0
    last_count = len(sw.records(path))
    last_change = time.time()
    deadline = time.time() + a.timeout

    while time.time() < deadline:
        path = sw.latest(a.repo)
        recs = sw.records(path)

        if len(sw.turn_ends(recs)) > base_turns:
            print(f"TURN_COMPLETE after {approvals} approval(s)")
            if texts := sw.assistant_texts(recs):
                print("\n--- final assistant message ---")
                print(texts[-1][:2000])
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

        if not sw.turn_in_flight(recs):
            print(f"TURN_COMPLETE (quiet, turn closed) after {approvals} approval(s)")
            if texts := sw.assistant_texts(recs):
                print("\n--- final assistant message ---")
                print(texts[-1][:2000])
            return 0

        # Turn open and quiet: waiting at a permission prompt, running a slow
        # command, or thinking. The transcript cannot tell these apart, and the
        # reason is worth stating because two rounds of testing got it wrong in
        # opposite directions.
        #
        # Records are flushed asynchronously and the flush lags the conversation
        # (Anthropic's hook docs say the transcript "may lag the in-memory
        # conversation"). Measured against v2.1.266 with a prompt visibly on
        # screen: once the transcript held an unanswered tool_use naming the exact
        # command, and once it held nothing at all and the tool_use only appeared
        # after approval. Same on-screen state, two different transcript shapes.
        #
        # So an unanswered tool_use is a HINT about what is being asked, never
        # proof of which state we are in. The screen decides.
        hint = sw.pending_tool_details(recs)
        if approvals >= a.max:
            print(f"CAP: {a.max} approvals reached. Stopping deliberately.")
            return 2

        shot = None
        if a.shot_dir or not a.approve_blind:
            d = a.shot_dir or os.path.join(HERE, "_prompts")
            os.makedirs(d, exist_ok=True)
            shot = os.path.join(d, f"prompt-{approvals + 1:02d}.png")
            # The capture can fail - most often FOCUS_FAILED, which is exactly
            # the situation where a human is about to be told "read this image".
            # Naming a path that was never written is bad; naming one left over
            # from an earlier prompt in the same --shot-dir is worse, because it
            # looks valid and describes a different question. Say it failed.
            before = os.path.getmtime(shot) if os.path.exists(shot) else None
            rs = screenctl("shot", *_target(a), "--out", shot)
            fresh = os.path.exists(shot) and os.path.getmtime(shot) != before
            if rs.returncode != 0 or not fresh:
                print("\nSCREENSHOT FAILED, so there is nothing to read:")
                print("   ", (rs.stdout + rs.stderr).strip()[:300] or "no new file")
                print("Refusing to approve something that cannot be seen.")
                return 2

        print(f"\n--- quiet {int(idle)}s, turn still open "
              f"(records {len(recs)}, approvals so far {approvals}) ---")
        if hint:
            for tool, detail in hint:
                print(f"    transcript hint: {tool}: {detail[:300]}")
                if why := refuses(tool, detail):
                    print(f"\nREFUSING: {why}. Answer this one yourself.")
                    print(f"    screenshot: {shot}")
                    return 3
        else:
            print("    transcript says nothing about what is being asked")

        if not a.approve_blind:
            print(f"\nScreenshot: {shot}")
            print("Read it. This is a permission prompt, a slow command, or thinking,")
            print("and only the image separates them. If it is a prompt, approve with:")
            print(f"  python screenctl.py key {' '.join(_target(a))} --keys enter")
            print("Re-run with --approve-blind only if you accept pressing Enter on")
            print("something nobody has read.")
            return 3

        if a.dry_run:
            print("\nDRY RUN: would press Enter to approve. Stopping here.")
            return 3
        print(f"    approving blind (--approve-blind). Screenshot: {shot}")

        # Enter, not a digit: it accepts the highlighted option, which is
        # approve-once. screenctl verifies the foreground window by identity and
        # exits non-zero rather than sending, so a stolen focus stops the run
        # instead of typing an approval into whatever is actually in front.
        r = screenctl("key", *_target(a), "--keys", "enter")
        if r.returncode != 0:
            print("\nSEND FAILED, stopping rather than pretending it landed:")
            print("   ", (r.stdout + r.stderr).strip()[:300])
            return 2
        approvals += 1
        print("    approved (Enter)")

        # Give the session a moment to act, then require evidence that it did.
        # An approval that changes nothing means the keystroke is not reaching the
        # prompt, and looping harder has never once fixed that.
        grew_by = time.time() + 30
        while time.time() < grew_by:
            time.sleep(a.poll)
            if len(sw.records(sw.latest(a.repo))) != last_count:
                break
        else:
            print("\nNo new transcript records after that approval.")
            print("The keystroke is not reaching the prompt. Stopping for a human.")
            return 2

        last_count = len(sw.records(sw.latest(a.repo)))
        last_change = time.time()

    print(f"TIMEOUT after {a.timeout}s with {approvals} approval(s) given.")
    print("The agent may still be working. Screenshot before concluding anything.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
