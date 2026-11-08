#!/usr/bin/env python3
"""Build database-ready metadata from a download manifest.

Outputs (into ../metadata by default):
  all_manuals.csv / .json           - every downloaded edition
  <collection>.csv / .json          - split by collection

Columns: id, designation, title, branch, pub_type, edition_year, collection,
format, filename, relative_path, bytes, slug, source_file_url, source_pdf_url,
source_epub_url, source_page_url

Run: python3 4_metadata.py [--manifest manifest_all.json] [--out-dir ../metadata]
"""
import json, os, csv, sys
from collections import defaultdict

WORKDIR = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.abspath(os.path.join(WORKDIR, ".."))
MAN = os.path.join(WORKDIR, "manifest_all.json")
OUT_DIR = os.path.join(DEST, "metadata")

args = sys.argv[1:]
i = 0
while i < len(args):
    if args[i] == "--manifest":
        MAN = args[i + 1]; i += 2
    elif args[i] == "--out-dir":
        OUT_DIR = os.path.abspath(args[i + 1]); i += 2
    else:
        i += 1

slugs = json.load(open(os.path.join(WORKDIR, "slugs.json")))
urls = json.load(open(os.path.join(WORKDIR, "urls.json")))
man = json.load(open(MAN))
os.makedirs(OUT_DIR, exist_ok=True)

rows = []
for sid, v in man.items():
    if v.get("status") not in ("ok", "exists"):
        continue
    s = slugs[sid]
    rel = os.path.relpath(v["path"], DEST)
    fmt = v.get("format")
    rows.append({
        "id": sid,
        "designation": s["designation"],
        "title": s["title"],
        "branch": s["branch"],
        "pub_type": s["pub_type"],
        "edition_year": s["year"],
        "collection": s["collection"],
        "format": fmt,
        "filename": os.path.basename(v["path"]),
        "relative_path": rel,
        "bytes": v.get("bytes", 0),
        "slug": s["slug"],
        "source_file_url": v.get("url") or urls[sid].get(fmt),
        "source_pdf_url": urls[sid].get("pdf"),
        "source_epub_url": urls[sid].get("epub"),
        "source_page_url": "https://www.trex-arms.com/field-manual-vault/" + s["slug"],
    })

rows.sort(key=lambda r: (r["branch"], r["pub_type"], r["id"]))
cols = list(rows[0].keys())


def write(path, rs):
    with open(path + ".csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rs)
    json.dump(rs, open(path + ".json", "w"), indent=1)


write(os.path.join(OUT_DIR, "all_manuals"), rows)
by = defaultdict(list)
for r in rows:
    by[r["collection"]].append(r)
for coll, rs in by.items():
    write(os.path.join(OUT_DIR, coll), rs)

print("rows", len(rows), "->", OUT_DIR)
for coll, rs in sorted(by.items()):
    print(f"  {coll}: {len(rs)} ({sum(x['bytes'] for x in rs) / 1e9:.2f} GB)")
print("total: %.2f GB" % (sum(r["bytes"] for r in rows) / 1e9))
