#!/usr/bin/env python3
"""Verify notes/ refactor invariants. Run from the repo root.

Unit mode (during the notes refactor; a unit owns a disjoint set of folders):
    python3 -I scripts/verify_notes.py --base <ref> --owned <notes-relative prefix> [--owned ...]
    --base <ref> is the git ref the unit forked from, used for content-preservation checks.

Repo-wide mode (final sweep; no --base/--owned):
    python3 -I scripts/verify_notes.py --all

Failures (exit 1) are scope leaks, leftover ethical-hacking-and-pen-testing-notes/
paths, broken/badly-tagged frontmatter, tag-vocabulary violations, known junk, and
unresolved [[wikilinks]] (junk/links in --all). Stub, kebab-case, and
content-preservation findings print as warnings only.
"""
import argparse, os, re, subprocess, sys

EH = "ethical-hacking-and-pen-testing-notes"
VOCAB = {
    "type": {"cheatsheet", "lab", "walkthrough", "reference", "tool", "methodology", "index"},
    "phase": {"recon", "enumeration", "initial-access", "exploitation", "privesc", "persistence",
              "credential-access", "lateral-movement", "evasion", "c2", "exfiltration", "impact",
              "forensics", "detection", "hardening"},
    "platform": {"windows", "linux", "macos", "android", "ios", "active-directory", "aws", "azure",
                 "gcp", "m365", "web", "api", "network", "wireless", "container", "blockchain", "iot"},
    "source": {"bhis", "cis"},
}
LIMITS = {"type": (1, 1), "phase": (0, 3), "platform": (0, 3), "source": (0, 1)}
JUNK = {"Untitled.md", "Awesome-Hacking/README 1.md"}


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout


def owned(path, prefixes):
    for p in prefixes:
        p = p.strip("/")
        if p in ("", ".") or path == p or path.startswith(p + "/"):
            return True
    return False


def split_fm(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, text


KEYCAP = re.compile(r"[0-9#*]?️?⃣|️")


def norm(line):
    line = KEYCAP.sub("", line)
    line = re.sub(r"^\s*#+\s*", "", line)
    return " ".join(line.split())


def body_lines(text):
    _, body = split_fm(text)
    out = []
    for l in body.split("\n"):
        n = norm(l)
        if n and n not in ("---", "```") and not re.fullmatch(r"[-*_=`~|: ]+", n):
            out.append(n)
    return out


def lint_file(root, rel, allnotes, fails, warns, link_fail):
    """rel is notes-relative (no "notes/" prefix). allnotes = set of stems w/o .md."""
    if rel in JUNK:
        fails.append(f"JUNK: known-junk file still present: notes/{rel}")
        return
    path = os.path.join(root, "notes", rel)
    text = open(path, encoding="utf-8", errors="replace").read()
    if rel.startswith(EH + "/"):
        fails.append(f"DUPTREE: duplicate EH tree still present: notes/{rel}")
        return
    fm, body = split_fm(text)
    if fm is None:
        fails.append(f"FM: no frontmatter: {rel}")
        return
    stem = os.path.splitext(os.path.basename(rel))[0]
    title = next((l.split(":", 1)[1].strip() for l in fm if l.startswith("title:")), None)
    if title is None or title.strip("'\"") != stem:
        fails.append(f"FM: title {title!r} != stem {stem!r}: {rel}")
    tl = next((l for l in fm if l.startswith("tags:")), None)
    m = re.fullmatch(r"tags:\s*\[(.*)\]\s*", tl or "")
    if not m:
        fails.append(f"FM: tags missing or not inline [..]: {rel}")
        return
    tags = [t.strip().strip("'\"") for t in m.group(1).split(",") if t.strip()]
    segs = [s.lower() for s in os.path.dirname(rel).split("/") if s]
    if tags[:len(segs)] != segs:
        fails.append(f"FM: folder tags {tags[:len(segs)]} != path {segs}: {rel}")
    counts = {k: 0 for k in VOCAB}
    for t in tags[len(segs):]:
        ns, _, val = t.partition("/")
        if ns not in VOCAB or val not in VOCAB[ns]:
            fails.append(f"FM: tag not in vocabulary: {t!r}: {rel}")
        else:
            counts[ns] += 1
    for ns, (lo, hi) in LIMITS.items():
        if not lo <= counts[ns] <= hi:
            fails.append(f"FM: {counts[ns]} {ns}/ tags (want {lo}-{hi}): {rel}")
    if not any(not l.lstrip().startswith("#") and l.strip() for l in body.split("\n")):
        warns.append(f"STUB: heading-only note: {rel}")
    if re.search(r"[A-Z _]", os.path.basename(rel)):
        warns.append(f"NAME: not lowercase kebab-case: {rel}")
    if allnotes is not None:
        for tgt in links_outside_code(body):
            if not tgt:
                continue
            # Attachments / vault-local assets (images, asm, etc.) are not
            # tracked; report but never fail on them.
            if os.path.splitext(tgt)[1].lower():
                warns.append(f"LINK: attachment [[{tgt}]] (not tracked) in {rel}")
                continue
            if tgt not in allnotes:
                (fails if link_fail else warns).append(f"LINK: unresolved [[{tgt}]] in {rel}")


def links_outside_code(body):
    """Extract [[wikilink]] targets outside fenced code blocks, HTML <pre>
    blocks and inline `code spans` — links inside code are import artifacts,
    not Obsidian links."""
    targets = []
    body = re.sub(r"<pre>.*?</pre>", "", body, flags=re.S)
    in_fence = False
    for l in body.split("\n"):
        if l.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        rest = re.sub(r"`[^`\n]*`", "", l)
        targets.extend(t.strip() for t in re.findall(r"\[\[([^\]|#]+)", rest))
    return targets


def walk(notes):
    out = []
    for r, ds, fs in os.walk(notes):
        ds[:] = [d for d in ds if d != ".obsidian"]
        for f in fs:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(r, f), notes))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    ap.add_argument("--owned", action="append")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    root = git("rev-parse", "--show-toplevel").strip()
    os.chdir(root)
    notes = os.path.join(root, "notes")
    fails, warns = [], []

    rels = walk(notes)
    allnotes = set(os.path.splitext(r)[0].replace("\\", "/") for r in rels)

    if a.all:
        for rel in rels:
            lint_file(root, rel, allnotes, fails, warns, link_fail=True)
        print(f"checked {len(rels)} notes; {len(fails)} failures, {len(warns)} warnings")
        for f in fails:
            print("FAIL ", f)
        for w in warns:
            print("WARN ", w)
        sys.exit(1 if fails else 0)

    if not a.base or not a.owned:
        ap.error("--all, or --base with at least one --owned, is required")

    changed = set()
    for line in git("diff", "--name-status", "-M", a.base).splitlines():
        parts = line.split("\t")
        changed.update(parts[1:])
    changed.update(git("ls-files", "--others", "--exclude-standard").splitlines())
    for p in sorted(changed):
        if not p.startswith("notes/") or not owned(p[len("notes/"):], a.owned):
            fails.append(f"SCOPE: changed path outside owned prefixes: {p}")

    owned_rels = [r for r in rels if owned(r, a.owned)]
    for rel in owned_rels:
        lint_file(root, rel, allnotes, fails, warns, link_fail=False)

    pool_lines = set()
    for rel in owned_rels:
        pool_lines.update(body_lines(open(os.path.join(notes, rel), encoding="utf-8", errors="replace").read()))
    pool = "\n".join(pool_lines)
    base_files = [p for p in git("ls-tree", "-r", "--name-only", a.base, "--", "notes/").splitlines()
                  if p.endswith(".md") and owned(p[len("notes/"):], a.owned)]
    missing = 0
    for p in base_files:
        try:
            text = git("show", f"{a.base}:{p}")
        except subprocess.CalledProcessError:
            continue
        for n in body_lines(text):
            if n not in pool_lines and n not in pool:
                missing += 1
                warns.append(f"LOST: {p}: {n[:160]}")

    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print(f"\nchecked {len(owned_rels)} current notes, {len(base_files)} base notes; "
          f"{len(fails)} failures, {missing} possibly-lost lines, {len(warns) - missing} other warnings")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()