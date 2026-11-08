#!/usr/bin/env python3
"""Download editions: EPUB preferred, PDF fallback. Resumable + live logging.

Usage:
  python3 3_download.py                                  # all collections
  python3 3_download.py current                          # current doctrine only
  python3 3_download.py recent-archive lessons-learned historic
  python3 3_download.py --dest /mnt/books --workers 6 --rate 8 all
  python3 3_download.py current --limit 5 --rate 2     # smoke test

Global request rate is capped by --rate (requests/sec across all workers);
429/5xx responses honor Retry-After with jittered exponential backoff.
Reads slugs.json + urls.json (run 1_enumerate.py and 2_resolve_urls.py first).
Writes <workdir>/manifest_all.json and files under
  <dest>/<branch>/<type>/<file_id>.<epub|pdf>
Re-running skips files already on disk.
"""
import json, concurrent.futures, os, re, threading, time, sys
from collections import Counter
from _http import RateLimiter, stream_to

WORKDIR = os.path.dirname(os.path.abspath(__file__))
COLLECTIONS = ["current", "recent-archive", "lessons-learned", "historic"]

args = sys.argv[1:]
DEST = os.path.join(WORKDIR, "..", "manuals")
WORKERS = 6
RATE = 8.0
LIMIT = 0
MAN = os.path.join(WORKDIR, "manifest_all.json")
wanted = []

i = 0
while i < len(args):
    a = args[i]
    if a == "--dest":
        DEST = args[i + 1]; i += 2
    elif a == "--workers":
        WORKERS = int(args[i + 1]); i += 2
    elif a == "--rate":
        RATE = float(args[i + 1]); i += 2
    elif a == "--limit":
        LIMIT = int(args[i + 1]); i += 2
    elif a == "--manifest":
        MAN = args[i + 1]; i += 2
    else:
        wanted.append(a); i += 1

if not wanted or "all" in wanted:
    wanted = list(COLLECTIONS)
DEST = os.path.abspath(DEST)

slugs = json.load(open(os.path.join(WORKDIR, "slugs.json")))
urls = json.load(open(os.path.join(WORKDIR, "urls.json")))
manifest = json.load(open(MAN)) if os.path.exists(MAN) else {}
lock = threading.Lock()
last_activity = {"t": time.time(), "file": ""}
LIMITER = RateLimiter(RATE)


def safe(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", s.strip().lower()).strip("-") or "misc"


def fetch_to(url, dest):
    try:
        return True, stream_to(
            url, dest, limiter=LIMITER, timeout=60,
            on_chunk=lambda n: last_activity.__setitem__("t", time.time()),
        )
    except Exception as e:
        return False, str(e)[:160]


def job(item):
    sid = item
    info = slugs[sid]
    u = urls[sid]
    branch, typ = safe(info["branch"]), safe(info["pub_type"])
    detail = "no url"
    for fmt, url in (("epub", u.get("epub")), ("pdf", u.get("pdf"))):
        if not url:
            continue
        d = os.path.join(DEST, branch, typ, os.path.basename(url))
        if os.path.exists(d) and os.path.getsize(d) > 1000:
            return sid, {"status": "exists", "format": fmt, "path": d, "bytes": os.path.getsize(d)}
        last_activity["file"] = sid
        ok, detail = fetch_to(url, d)
        if ok:
            last_activity["t"] = time.time()
            return sid, {"status": "ok", "format": fmt, "path": d, "bytes": detail}
    return sid, {"status": "failed", "error": detail}


todo = [
    k for k, v in urls.items()
    if slugs[k]["collection"] in wanted and manifest.get(k, {}).get("status") not in ("ok", "exists")
]
if LIMIT:
    todo = todo[:LIMIT]
print("collections", wanted, "| to download", len(todo), "| already", len(manifest), flush=True)


def watchdog():
    while True:
        time.sleep(15)
        with lock:
            done = sum(1 for v in manifest.values() if v["status"] in ("ok", "exists"))
        print(f"[watch] done={done}/{len(todo)} idle={time.time() - last_activity['t']:.0f}s "
              f"last={last_activity['file']}", flush=True)


threading.Thread(target=watchdog, daemon=True).start()

n = b = 0
t0 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
    futs = {ex.submit(job, sid): sid for sid in todo}
    for f in concurrent.futures.as_completed(futs):
        sid, val = f.result()
        with lock:
            manifest[sid] = val
            n += 1
            b += val.get("bytes", 0)
            if n % 25 == 0 or val["status"] != "ok":
                json.dump(manifest, open(MAN, "w"))
                print(f"[{n}/{len(todo)}] {val['status']:6} {val.get('format','')} {sid} "
                      f"{b / 1e9:.2f}GB {time.time() - t0:.0f}s", flush=True)

json.dump(manifest, open(MAN, "w"))
print("DONE", dict(Counter(v["status"] for v in manifest.values())),
      dict(Counter(v.get("format") for v in manifest.values())), flush=True)
