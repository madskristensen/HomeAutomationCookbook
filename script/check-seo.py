#!/usr/bin/env python3
"""Fail the build if a built page has an img without alt text or a title over 70 characters."""
import html, pathlib, re, sys

site = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs/_site")
img_re = re.compile(r"<img\b[^>]*>", re.I)
alt_re = re.compile(r'\balt\s*=\s*"[^"]*\S[^"]*"', re.I)
title_re = re.compile(r"<title>(.*?)</title>", re.I | re.S)
errors = []
for page in sorted(site.rglob("*.html")):
    text = page.read_text(encoding="utf-8", errors="ignore")
    rel = page.relative_to(site)
    for img in img_re.findall(text):
        if not alt_re.search(img):
            errors.append(f"{rel}: img without alt text: {img[:120]}")
    m = title_re.search(text)
    if m:
        title = html.unescape(m.group(1).strip())
        if len(title) > 70:
            errors.append(f"{rel}: title is {len(title)} chars: {title}")
for e in errors:
    print(f"::error::{e}")
print(f"SEO check: {len(errors)} problem(s).")
sys.exit(1 if errors else 0)
