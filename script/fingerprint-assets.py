#!/usr/bin/env python3
"""Minify and fingerprint shared CSS/JS for Home Automation Cookbook.

Reads docs/_css and docs/_js. Writes assets/css/<name>.<hash>.css and
assets/js/<name>.<hash>.js, plus _data/css.yml and _data/js.yml so layouts
can link the hashed files. Run before Jekyll reads static files (the
fingerprint_assets plugin does this on after_init). Sources stay under
underscore dirs so Jekyll does not also publish the unhashed copies.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

try:
    import rcssmin
except ImportError:
    sys.exit("rcssmin is required: python3 -m pip install rcssmin")

# Repo root when this file lives at script/fingerprint-assets.py
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CSS_SRC = DOCS / "_css"
JS_SRC = DOCS / "_js"
CSS_DEST = DOCS / "assets" / "css"
JS_DEST = DOCS / "assets" / "js"
CSS_DATA = DOCS / "_data" / "css.yml"
JS_DATA = DOCS / "_data" / "js.yml"

LINKED_CSS = ("site", "print")
LINKED_JS = (
    ("page.js", "page"),
    ("navigation.js", "navigation"),
    ("share.js", "share"),
    ("recipe-search.js", "recipe_search"),
)


def minify_css(name: str) -> str:
    source = CSS_SRC / f"{name}.css"
    if not source.is_file():
        sys.exit(f"missing stylesheet {source}")
    raw = source.read_text(encoding="utf-8")
    mini = rcssmin.cssmin(raw)
    if not mini.endswith("\n"):
        mini += "\n"
    if "</style" in mini.lower():
        sys.exit(f"{name}.css cannot be linked after minify")
    return mini


def write_css() -> list[str]:
    CSS_DEST.mkdir(parents=True, exist_ok=True)
    for old in CSS_DEST.glob("*.css"):
        old.unlink()
    lines: list[str] = []
    for name in LINKED_CSS:
        mini = minify_css(name)
        digest = hashlib.sha256(mini.encode("utf-8")).hexdigest()[:10]
        filename = f"{name}.{digest}.css"
        (CSS_DEST / filename).write_text(mini, encoding="utf-8")
        public = f"/assets/css/{filename}"
        lines.append(f"{name}: {public}")
        print(f"{name}\t{public}\t{len(mini)}")
    CSS_DATA.parent.mkdir(parents=True, exist_ok=True)
    CSS_DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return lines


def write_js() -> list[str]:
    JS_DEST.mkdir(parents=True, exist_ok=True)
    # Remove prior fingerprinted copies only; leave other assets alone.
    for old in JS_DEST.glob("*.*.js"):
        old.unlink()
    for stem, _key in ((f[:-3], k) for f, k in LINKED_JS):
        for old in JS_DEST.glob(f"{stem}.*.js"):
            old.unlink()
    lines: list[str] = []
    for filename, key in LINKED_JS:
        source = JS_SRC / filename
        if not source.is_file():
            sys.exit(f"missing script {source}")
        raw = source.read_text(encoding="utf-8")
        if not raw.endswith("\n"):
            raw += "\n"
        digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:10]
        stem = filename[:-3]
        hashed = f"{stem}.{digest}.js"
        (JS_DEST / hashed).write_text(raw, encoding="utf-8")
        public = f"/assets/js/{hashed}"
        lines.append(f"{key}: {public}")
        print(f"{stem}\t{public}\t{len(raw)}")
    JS_DATA.parent.mkdir(parents=True, exist_ok=True)
    JS_DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return lines


def main() -> None:
    if not CSS_SRC.is_dir() or not JS_SRC.is_dir():
        sys.exit(f"expected {CSS_SRC} and {JS_SRC}")
    write_css()
    write_js()


if __name__ == "__main__":
    main()
