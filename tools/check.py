#!/usr/bin/env python3
"""Check the week's work with rules. Run from the folder: python3 tools/check.py"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
read = lambda p: open(os.path.join(ROOT, p), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, p)) else ""

me = read("me.md")
sources = [f for f in glob.glob(os.path.join(ROOT, "raw", "*")) if not os.path.basename(f).startswith(".")]
pages = [f for f in glob.glob(os.path.join(ROOT, "wiki", "*.md")) if os.path.basename(f) != "told.md"]
wiki = "".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(ROOT, "wiki", "*.md")))
told = [l for l in read("wiki/told.md").split("\n") if re.search(r"\d{4}-\d\d-\d\d", l)]
days = set(re.findall(r"^\W*(\d{4}-\d\d-\d\d)", read("log.md"), re.M))
rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in read("eval/questions.md").split("\n") if re.match(r"\|\s*[123]\s*\|", l)]
mark = lambda c: c.lower() in ("right", "wrong")

checks = [
    ("me.md has my North Star", "North Star" in me and "[month and year]" not in me),
    ("one source in raw/", len(sources) >= 1),
    ("one page in wiki/ written from it", len(pages) >= 1),
    ("one fact told to it, with a date", len(told) >= 1),
    ("three questions written, with their answers", len(rows) == 3 and all(len(r) > 2 and r[1] and not r[1].startswith("(") and r[2] for r in rows)),
    ("three questions marked before and after", len(rows) == 3 and all(len(r) > 4 and mark(r[3]) and mark(r[4]) for r in rows)),
    ("log.md has lines on five different days", len(days) >= 5),
    ("one line replaced, with the old one kept", bool(re.search(r"Replaced on \d{4}-\d\d-\d\d", wiki))),
    ("three questions marked again after Lecture 16", len(rows) == 3 and all(len(r) > 5 and mark(r[5]) for r in rows)),
]
for name, ok in checks:
    print(("[x] " if ok else "[ ] ") + name)
print("%d of %d done" % (sum(ok for _, ok in checks), len(checks)))
