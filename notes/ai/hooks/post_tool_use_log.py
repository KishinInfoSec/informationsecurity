#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///
"""
PostToolUse hook - the observer.

Fires AFTER every tool call. It cannot block (the tool already ran), so its job
is to *see*: append one line per event to logs/agent-actions.jsonl. The result is
a complete audit trail of exactly what the agent did - every command, every edit -
that you can read back, grep, or pipe into a dashboard.

    Pre = gate. Post = log.

Why JSONL and not JSON: the course version rewrote a single JSON array on every
tool call, which is O(n^2) writes and corrupts if two hooks fire at once. One
append-only line per event is cheap, concurrent-safe enough, and greppable:

    grep '"tool_name":"Bash"' logs/agent-actions.jsonl | tail -20
    python -c "import json,sys;[print(json.loads(l)['summary']) for l in open('logs/agent-actions.jsonl')]"

Fails OPEN: any error exits 0, so logging can never break your session.

MAKE IT YOURS: the common upgrades are auto-formatting a file the moment it is
edited, or notifying you on a specific tool. Both are PostToolUse. Change
`summarize()` if you want different fields, or set FULL_PAYLOAD = True to keep
everything.
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

if os.name == "nt":
    import msvcrt
else:
    import fcntl

# The one line most people edit.
LOG_PATH = Path("logs") / "agent-actions.jsonl"

# True keeps the entire hook payload per line (verbose, but complete).
FULL_PAYLOAD = False

# Long tool inputs are truncated to keep the log readable.
MAX_FIELD = 300


def _clip(value: object) -> object:
    text = str(value)
    return text if len(text) <= MAX_FIELD else text[:MAX_FIELD] + f"... [+{len(text) - MAX_FIELD} chars]"


def summarize(data: dict) -> dict:
    """One readable line per tool call: what ran, on what, and when."""
    tool_input = data.get("tool_input", {}) or {}
    tool_name = data.get("tool_name", "")

    # The field that actually says what happened differs per tool.
    target = (
        tool_input.get("command")
        or tool_input.get("file_path")
        or tool_input.get("pattern")
        or tool_input.get("url")
        or ""
    )

    return {
        "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
        "session": data.get("session_id", ""),
        # PostToolUse fires on success; PostToolUseFailure on failure. Both are
        # wired to this hook, so record which one so the trail distinguishes a
        # command that ran from one that blew up.
        "event": data.get("hook_event_name", "PostToolUse"),
        "tool_name": tool_name,
        "summary": _clip(target),
        "cwd": data.get("cwd", ""),
    }


def _lock(handle) -> None:
    if os.name == "nt":
        msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
    else:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)


def _unlock(handle) -> None:
    if os.name == "nt":
        handle.seek(0)
        msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
    else:
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def append_line(log_path: Path, line: str) -> None:
    """Append one line under an exclusive cross-process lock.

    Plain append mode is NOT atomic across processes. Claude Code fires tool
    calls in parallel and this hook is wired to every one of them, so several
    copies race on the same file. Measured before the lock: 128 concurrent
    invocations produced 124 lines. Four entries vanished and every process
    still exited 0, so nothing anywhere reported a problem.

    An audit trail that silently drops entries is worse than no audit trail,
    because you trust it.

    The lock is taken on a SEPARATE lock file, not on the log itself. On
    Windows msvcrt locks a byte range starting at the current file position,
    and in append mode every process sits at a different offset, so locking the
    log would lock a different region per process and exclude nobody. Byte 0 of
    a dedicated file is the same region for everyone. OS-level locks are also
    released automatically if a process dies, which a lock file created with
    O_EXCL would not be.
    """
    lock_path = log_path.with_name(log_path.name + ".lock")
    with lock_path.open("a+b") as guard:
        held = False
        # msvcrt's LK_LOCK already blocks and retries for ~10s before raising.
        # Retry around it: under heavy contention a single 10s window can lapse,
        # and writing unlocked is what loses the line in the first place.
        for _ in range(3):
            try:
                guard.seek(0)
                _lock(guard)
                held = True
                break
            except OSError:
                time.sleep(0.05)
        try:
            with log_path.open("a", encoding="utf-8") as handle:
                handle.write(line)
                handle.flush()
                os.fsync(handle.fileno())
        finally:
            if held:
                try:
                    _unlock(guard)
                except OSError:
                    pass


def main() -> None:
    try:
        data = json.load(sys.stdin)

        log_path = Path(data.get("cwd") or ".") / LOG_PATH
        log_path.parent.mkdir(parents=True, exist_ok=True)

        entry = data if FULL_PAYLOAD else summarize(data)

        # One line per tool call, appended under a lock. See append_line: plain
        # append mode alone loses entries when tool calls run in parallel.
        append_line(log_path, json.dumps(entry, ensure_ascii=False) + "\n")

        sys.exit(0)

    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
