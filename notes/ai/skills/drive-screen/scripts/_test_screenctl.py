#!/usr/bin/env python3
"""Tests that need no screen, no focus, and no permission grants.

These cover the parts that were wrong or unproven after the first end-to-end run:
image introspection, the coordinate arithmetic that turns a screenshot pixel into
a click, transcript interpretation, and whether all three platform backends
actually expose the same API. The last one matters most, because two of those
three backends have never executed a line on this machine and a missing function
is the failure that looks like a crash on someone else's laptop.

  python _test_screenctl.py
"""

from __future__ import annotations

import ast
import pathlib
import struct
import sys
import tempfile
import zlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import screenctl as sc          # noqa: E402
import session_watch as sw      # noqa: E402

FAILURES: list[str] = []
CHECKS = 0


def check(name: str, got, want) -> None:
    global CHECKS
    CHECKS += 1
    if got != want:
        FAILURES.append(f"{name}: got {got!r}, wanted {want!r}")


def truthy(name: str, got) -> None:
    global CHECKS
    CHECKS += 1
    if not got:
        FAILURES.append(f"{name}: expected truthy, got {got!r}")


# --------------------------------------------------------------------------
# PNG introspection
# --------------------------------------------------------------------------

def make_png(path: str, w: int, h: int, solid: bool) -> None:
    """Write a real PNG: one flat colour, or noisy rows."""
    rows = bytearray()
    for y in range(h):
        rows.append(0)                                   # filter byte
        for x in range(w):
            v = 128 if solid else (x * 7 + y * 13) % 251
            rows += bytes((v, (v * 3) % 256, (v * 5) % 256))

    def chunk(kind: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + kind + data
                + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF))

    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", ihdr))
        f.write(chunk(b"IDAT", zlib.compress(bytes(rows), 6)))
        f.write(chunk(b"IEND", b""))


tmp = tempfile.mkdtemp()
solid, noisy = f"{tmp}/solid.png", f"{tmp}/noisy.png"
make_png(solid, 200, 120, solid=True)
make_png(noisy, 200, 120, solid=False)

check("png_size reads IHDR", sc.png_size(solid), (200, 120))
check("png_size on a non-PNG", sc.png_size(__file__), (0, 0))

# The whole reason this exists: on macOS a missing Screen Recording grant returns
# a black image with a zero exit code. It has to fire on a flat image and must not
# fire on a real screen, or it either misses the failure or cries wolf every shot.
check("blank detector fires on a flat image", sc.looks_blank(solid), True)
check("blank detector ignores real content", sc.looks_blank(noisy), False)
check("blank detector survives a non-PNG", sc.looks_blank(__file__), False)


# --------------------------------------------------------------------------
# Coordinate arithmetic: the mapping a caller performs from `shot` output
# --------------------------------------------------------------------------

def to_screen(origin: int, px: float, scale: float) -> int:
    return round(origin + px / scale)


# A window on the primary monitor, captured at native size.
check("native scale, primary monitor", to_screen(0, 640, 1.0), 640)
# The real case from the live run: second monitor, downscaled capture.
check("downscaled, second monitor", to_screen(1922, 70, 0.6674), 2027)
# A monitor to the LEFT of primary has negative coordinates. Untested live, and
# the arithmetic has to keep working through zero rather than clamping.
check("negative-origin monitor", to_screen(-1920, 100, 1.0), -1820)
check("negative origin, downscaled", to_screen(-1920, 640, 0.5), -640)
check("negative origin, crossing zero", to_screen(-100, 400, 1.0), 300)
# Retina: an 800-point window yields a 1600px image, so scale is 2.0 and a click
# at image pixel 1000 is point 500.
check("retina 2x maps back to points", to_screen(0, 1000, 2.0), 500)

# Minimized windows park at -32000 on Windows and must be flagged, not treated as
# a real target, or a click computed from that geometry goes nowhere.
truthy("minimized flagged", sc.Win("1", "t", -32000, -32000, 160, 28).minimized)
check("negative-monitor window is not 'minimized'",
      sc.Win("1", "t", -1920, -8, 1936, 1048).minimized, False)


# --------------------------------------------------------------------------
# Transcript interpretation, replayed over every real transcript on this machine
# --------------------------------------------------------------------------

def rec(t, blocks=None, sub=None):
    d = {"type": t}
    if sub:
        d["subtype"] = sub
    if blocks is not None:
        d["message"] = {"content": blocks}
    return d


done = [rec("user", [{"type": "text", "text": "hi"}]),
        rec("assistant", [{"type": "text", "text": "ok"}]),
        rec("system", sub="turn_duration")]
open_turn = done + [rec("user", [{"type": "text", "text": "do a thing"}])]
tool_round = done + [
    rec("assistant", [{"type": "tool_use", "id": "x", "name": "Bash",
                       "input": {"command": "ls"}}]),
    rec("user", [{"type": "tool_result", "tool_use_id": "x"}]),
    rec("system", sub="turn_duration")]

check("closed turn is not in flight", sw.turn_in_flight(done), False)
check("new prompt opens the turn", sw.turn_in_flight(open_turn), True)
check("a tool_result is not a new prompt", sw.turn_in_flight(tool_round), False)
check("empty transcript is not in flight", sw.turn_in_flight([]), False)
check("junk records do not crash it",
      sw.turn_in_flight([{"nope": 1}, rec("assistant")]), False)

# Path mangling: every non-alphanumeric becomes a hyphen. Getting this wrong means
# the directory is never found and the error blames the wrong thing.
check("drive letter and separators", sw.mangle(r"C:\Users\me\proj"), "C--Users-me-proj")
truthy("spaces and parens survive", "-" in sw.mangle(r"C:\Users\me\my proj (v2)"))
check("no non-alphanumerics remain",
      any(not (c.isalnum() or c == "-") for c in sw.mangle(r"C:\a b.c(d)\e")), False)

# Replay against real transcripts: the point is that nothing crashes on shapes I
# did not anticipate, and that a transcript ending in a completed turn is never
# reported as open.
root = pathlib.Path.home() / ".claude" / "projects"
files = (sorted(root.glob("*/*.jsonl"), key=lambda q: q.stat().st_mtime)[-40:]
         if root.is_dir() else [])
replayed = closed_ok = 0
for f in files:
    try:
        recs = sw.records(f)
    except Exception as e:                                  # pragma: no cover
        FAILURES.append(f"records() crashed on {f.name}: {e}")
        continue
    if not recs:
        continue
    replayed += 1
    try:
        in_flight = sw.turn_in_flight(recs)
        sw.pending_tool_details(recs)
        sw.assistant_texts(recs)
        sw.tool_reads(recs, 0)
    except Exception as e:                                  # pragma: no cover
        FAILURES.append(f"parsing crashed on {f.name}: {e}")
        continue
    # The invariant that matters: if a turn completed AFTER the newest user
    # prompt, the turn is closed. This is the exact judgement that was wrong
    # before, when a quiet transcript was read as finished while a permission
    # prompt sat on screen.
    ends = sw.turn_ends(recs)
    last_prompt = max(
        (i for i, d in enumerate(recs)
         if d.get("type") == "user"
         and not any(isinstance(c, dict) and c.get("type") == "tool_result"
                     for c in sw._content(d))),
        default=-1)
    if ends and last_prompt >= 0 and ends[-1] > last_prompt:
        CHECKS += 1
        if in_flight:
            FAILURES.append(f"{f.name}: a turn completed after the last prompt "
                            f"but it reads as in flight")
        else:
            closed_ok += 1

print(f"replayed {replayed} real transcripts "
      f"({closed_ok} with a completed final turn, all read as closed)")


# --------------------------------------------------------------------------
# Key tables
# --------------------------------------------------------------------------

if sc.OS == "Windows":
    for name in ("enter", "esc", "tab", "backtick", "pagedown", "f5", "ctrl", "shift"):
        truthy(f"key name {name!r} is mapped", name in sc.VK)
    # Letters and digits map through ord(); punctuation must be named instead,
    # because a bare '`' has no virtual key code and a backtick inside double
    # quotes is command substitution in most shells.
    check("backtick is VK_OEM_3", sc.VK["backtick"], 0xC0)

    # wScan is 16 bits and carries a UTF-16 code unit. Passing a code point
    # straight in truncates every astral character: a rocket (U+1F680) arrived
    # as U+F680, a private-use glyph, with no error. BMP characters have one
    # unit and always worked, which is why it went unnoticed.
    check("BMP character is one unit", sc._utf16_units("é"), [0xE9])
    check("CJK is one unit", sc._utf16_units("日"), [0x65E5])
    check("astral character is a surrogate PAIR", sc._utf16_units("🚀"),
          [0xD83D, 0xDE80])
    for u in sc._utf16_units("🚀") + sc._utf16_units("★"):
        CHECKS += 1
        if not 0 <= u <= 0xFFFF:
            FAILURES.append(f"code unit {u:#x} does not fit in a 16-bit wScan")


# --------------------------------------------------------------------------
# All three backends must expose the same API
# --------------------------------------------------------------------------
# Only one platform branch executes at import, so the other two are invisible to
# every test above. This reads the source instead and asserts each branch defines
# the same names. It cannot prove macOS or Linux behave correctly, but it does
# catch the failure that would otherwise surface as a crash on a stranger's
# laptop: a function that simply is not there.

REQUIRED = {"list_windows", "foreground_id", "same_window", "raise_window",
            "unlock_foreground", "type_text", "send_chord", "move_click",
            "scroll", "get_clipboard", "set_clipboard", "capture"}

src = pathlib.Path(sc.__file__).read_text(encoding="utf-8")
tree = ast.parse(src)

branches: dict[str, set[str]] = {}
for node in ast.walk(tree):
    if not isinstance(node, ast.If):
        continue
    for label, body in (("primary", node.body), ("else", node.orelse)):
        names = {n.name for n in body if isinstance(n, ast.FunctionDef)}
        if REQUIRED & names:
            branches[f"{label}:{id(node)}"] = names

truthy("found the platform branches", len(branches) >= 3)
for label, names in branches.items():
    missing = REQUIRED - names
    check(f"backend {label.split(':')[0]} defines the full API", sorted(missing), [])

truthy("every backend defines PASTE_CHORD", src.count("PASTE_CHORD = ") >= 3)


# --------------------------------------------------------------------------

if FAILURES:
    print(f"\nFAILED {len(FAILURES)} of {CHECKS}:")
    for f in FAILURES:
        print("  " + f)
    sys.exit(1)
print(f"all {CHECKS} checks passed")
