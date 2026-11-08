#!/usr/bin/env python3
"""Resolve real PDF/EPUB URLs for every edition.

Fetches each manual's public detail page (HTML) and extracts the exact
files.trex-arms.com links. This handles the vault's varying path layouts
(`/<branch>/<type>/`, `/<branch>/legacy/<type>/`, `/<branch>/recovered/...`,
`/<branch>/lessons/...`). Resumable -> writes urls.json.

Run: python3 2_resolve_urls.py [--workers 6] [--rate 10] [--limit N]
"""
import json, re, concurrent.futures, os, threading, sys
from _http import RateLimiter, fetch_bytes

WORKDIR = os.path.dirname(os.path.abspath(__file__))
SLUGS = os.path.join(WORKDIR, "slugs.json")
OUT = os.path.join(WORKDIR, "urls.json")
PAT = re.compile(r"https://files\.trex-arms\.com/[^\"'<> ]+\.(?:pdf|epub)")

args = sys.argv[1:]
WORKERS = int(args[args.index("--workers") + 1]) if "--workers" in args else 6
RATE = float(args[args.index("--rate") + 1]) if "--rate" in args else 10.0
LIMIT = int(args[args.index("--limit") + 1]) if "--limit" in args else 0
LIMITER = RateLimiter(RATE)

lock = threading.Lock()


def get(item):
    sid, it = item
    slug = it["slug"]
    url = "https://www.trex-arms.com/field-manual-vault/" + slug
    try:
        html = fetch_bytes(url, limiter=LIMITER, timeout=45).decode("utf-8", "replace")
        urls = sorted(set(PAT.findall(html)))
        epub = next((u for u in urls if u.endswith(".epub")), None)
        pdf = next((u for u in urls if u.endswith(".pdf")), None)
        return sid, {"slug": slug, "epub": epub, "pdf": pdf, "all": urls}
    except Exception as e:
        return sid, {"slug": slug, "epub": None, "pdf": None, "all": [], "error": str(e)[:120]}


def main():
    slugs = json.load(open(SLUGS))
    done = json.load(open(OUT)) if os.path.exists(OUT) else {}
    todo = [(k, v) for k, v in slugs.items() if k not in done]
    if LIMIT:
        todo = todo[:LIMIT]
    print("to resolve", len(todo), "already", len(done), flush=True)

    n = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(get, it): it[0] for it in todo}
        for f in concurrent.futures.as_completed(futs):
            sid, val = f.result()
            with lock:
                done[sid] = val
                n += 1
                if n % 100 == 0:
                    json.dump(done, open(OUT, "w"), indent=0)
                    print("resolved", n, "/", len(todo), flush=True)

    json.dump(done, open(OUT, "w"), indent=0)
    missing = [k for k, v in done.items() if not v.get("epub") and not v.get("pdf")]
    pdf_only = [k for k, v in done.items() if not v.get("epub") and v.get("pdf")]
    print("DONE total", len(done), "no-file", len(missing), "pdf-only", len(pdf_only))
    if missing:
        print("missing sample", missing[:20])


if __name__ == "__main__":
    main()
