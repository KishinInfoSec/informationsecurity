#!/usr/bin/env python3
"""Enumerate every manual edition in the T.REX Field Manual Vault.

Pulls the site's SvelteKit `__data.json` listing (paginated by collection) and
expands each work's editions. Writes:
  works.json  - one row per work (collapsed editions)
  slugs.json  - one row per edition: {id, slug, branch, pub_type, title,
                designation, year, collection}

Run: python3 1_enumerate.py [--collections current,historic] [--rate 4] [--max-pages N]
"""
import json, math, os, sys
from _http import RateLimiter, fetch_bytes

WORKDIR = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.trex-arms.com/field-manual-vault/__data.json?"
COLLECTIONS = ["current", "recent-archive", "lessons-learned", "historic"]

args = sys.argv[1:]
if "--collections" in args:
    COLLECTIONS = args[args.index("--collections") + 1].split(",")
RATE = float(args[args.index("--rate") + 1]) if "--rate" in args else 4.0
MAX_PAGES = int(args[args.index("--max-pages") + 1]) if "--max-pages" in args else 0
LIMITER = RateLimiter(RATE)


def fetch(params):
    raw = fetch_bytes(BASE + params, limiter=LIMITER, timeout=90)
    return json.loads(raw.decode().splitlines()[0])


def parse_list(d):
    node = d["nodes"][2]["data"]

    def deref(p):
        if isinstance(p, dict):
            return {k: res(v) for k, v in p.items()}
        if isinstance(p, list):
            return [res(x) for x in p]
        return p

    def res(v):
        if isinstance(v, bool) or v is None or isinstance(v, str):
            return v
        if isinstance(v, int):
            return deref(node[v])
        if isinstance(v, (dict, list)):
            return deref(v)
        return v

    for v in node:
        if isinstance(v, dict) and "results" in v and "searched" in v and "size" in v:
            return res(v)
    return None


def collect(param):
    works = {}
    page = 1
    while True:
        d = fetch(param + f"&page={page}")
        lst = parse_list(d)
        if not lst:
            break
        for r in lst["results"]:
            works[r["id"]] = {
                "id": r["id"], "slug": r["slug"], "title": r["title"],
                "designation": r["designation"], "pub_type": r["pub_type"],
                "branch": r["branch"], "collection": r["collection"],
                "edition_year": r.get("edition_year"),
                "file_size": r.get("file_size"),
                "editions": [
                    {"id": e.get("id"), "slug": e["slug"], "year": e.get("edition_year")}
                    for e in r.get("editions", [])
                ],
            }
        total = lst["total"]
        size = lst["size"] or 30
        pages = math.ceil(total / size)
        if page == 1:
            print(f"   total={total} size={size} pages={pages}", flush=True)
        if page >= pages or not lst["results"] or (MAX_PAGES and page >= MAX_PAGES):
            break
        page += 1
    return works


def main():
    all_works = {}
    for coll in COLLECTIONS:
        print("COLL", coll, flush=True)
        w = collect("coll=" + coll)
        print("   works:", len(w), flush=True)
        all_works.update(w)

    slugs = {}
    for wid, w in all_works.items():
        editions = w["editions"] or [{"id": wid, "slug": w["slug"], "year": w["edition_year"]}]
        for e in editions:
            sid = e["id"] or wid
            slugs[sid] = {
                "id": sid, "slug": e["slug"], "branch": w["branch"],
                "pub_type": w["pub_type"], "title": w["title"],
                "designation": w["designation"], "year": e["year"],
                "collection": w["collection"],
            }

    print("unique works:", len(all_works))
    print("unique editions:", len(slugs))
    json.dump(all_works, open(os.path.join(WORKDIR, "works.json"), "w"), indent=1)
    json.dump(slugs, open(os.path.join(WORKDIR, "slugs.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
