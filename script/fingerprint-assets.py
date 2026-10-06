#!/usr/bin/env python3
"""Minify and fingerprint shared CSS/JS for Home Automation Cookbook.

Reads docs/_css and docs/_js. Writes assets/css/<name>.<hash>.css and
assets/js/<name>.<hash>.js, plus unhashed fallbacks (site.css, page.js,
etc.), and _data/css.yml + _data/js.yml + _data/shell.yml so layouts and
sw.js work without Jekyll plugins.

github-pages runs Jekyll in safe mode and skips docs/_plugins, so this
script must run from the GitHub Actions workflow before `jekyll build`
(same pattern as script/render-image-variants.py).
"""

from __future__ import annotations

import hashlib
import re
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
IMG_DIR = DOCS / "assets" / "img"
CSS_DATA = DOCS / "_data" / "css.yml"
JS_DATA = DOCS / "_data" / "js.yml"
SHELL_DATA = DOCS / "_data" / "shell.yml"

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


def write_css() -> dict[str, str]:
    CSS_DEST.mkdir(parents=True, exist_ok=True)
    for old in CSS_DEST.glob("*.css"):
        old.unlink()
    mapping: dict[str, str] = {}
    lines: list[str] = []
    for name in LINKED_CSS:
        mini = minify_css(name)
        digest = hashlib.sha256(mini.encode("utf-8")).hexdigest()[:10]
        filename = f"{name}.{digest}.css"
        (CSS_DEST / filename).write_text(mini, encoding="utf-8")
        # Unhashed fallback so layouts never ship empty hrefs if data is missing.
        (CSS_DEST / f"{name}.css").write_text(mini, encoding="utf-8")
        public = f"/assets/css/{filename}"
        mapping[name] = public
        lines.append(f"{name}: {public}")
        print(f"{name}\t{public}\t{len(mini)}")
    CSS_DATA.parent.mkdir(parents=True, exist_ok=True)
    CSS_DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return mapping


def write_js() -> dict[str, str]:
    JS_DEST.mkdir(parents=True, exist_ok=True)
    # Remove prior fingerprinted copies and known unhashed fallbacks.
    for old in JS_DEST.glob("*.*.js"):
        old.unlink()
    for filename, _key in LINKED_JS:
        fallback = JS_DEST / filename
        if fallback.is_file():
            fallback.unlink()
        stem = filename[:-3]
        for old in JS_DEST.glob(f"{stem}.*.js"):
            old.unlink()
    mapping: dict[str, str] = {}
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
        (JS_DEST / filename).write_text(raw, encoding="utf-8")
        public = f"/assets/js/{hashed}"
        mapping[key] = public
        lines.append(f"{key}: {public}")
        print(f"{stem}\t{public}\t{len(raw)}")
    JS_DATA.parent.mkdir(parents=True, exist_ok=True)
    JS_DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return mapping


def shell_icon(name: str) -> bool:
    lower = name.lower()
    if "favicon" in lower or "apple-touch" in lower:
        return True
    return bool(re.match(r"\Aicon-\d", lower))


def write_shell(css_map: dict[str, str], js_map: dict[str, str]) -> None:
    """Write _data/shell.yml for sw.js (replaces service_worker.rb plugin)."""
    pages = ["/"]
    images: list[str] = []
    hash_inputs: list[tuple[str, Path]] = []

    for public in css_map.values():
        pages.append(public)
        hash_inputs.append((public, DOCS / public.lstrip("/")))
    for public in js_map.values():
        pages.append(public)
        hash_inputs.append((public, DOCS / public.lstrip("/")))

    manifest = DOCS / "manifest.webmanifest"
    if manifest.is_file():
        pages.append("/manifest.webmanifest")
        hash_inputs.append(("/manifest.webmanifest", manifest))

    favicon = DOCS / "favicon.ico"
    if favicon.is_file():
        images.append("/favicon.ico")
        hash_inputs.append(("/favicon.ico", favicon))

    if IMG_DIR.is_dir():
        for path in sorted(IMG_DIR.iterdir()):
            if not path.is_file():
                continue
            if not shell_icon(path.name):
                continue
            public = f"/assets/img/{path.name}"
            images.append(public)
            hash_inputs.append((public, path))

    pages = list(dict.fromkeys(pages))
    images = sorted(set(images))

    digest = hashlib.sha256()
    for public, path in sorted(hash_inputs, key=lambda item: item[0]):
        digest.update(public.encode("utf-8"))
        digest.update(b"\0")
        if path.is_file():
            digest.update(hashlib.sha256(path.read_bytes()).hexdigest().encode("ascii"))
        digest.update(b"\0")
    version = digest.hexdigest()[:12]

    lines = [f'version: "{version}"', "pages:"]
    for path in pages:
        lines.append(f'  - "{path}"')
    lines.append("images:")
    for path in images:
        lines.append(f'  - "{path}"')
    SHELL_DATA.parent.mkdir(parents=True, exist_ok=True)
    SHELL_DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"shell\tversion={version}\tpages={len(pages)}\timages={len(images)}")


def main() -> None:
    if not CSS_SRC.is_dir() or not JS_SRC.is_dir():
        sys.exit(f"expected {CSS_SRC} and {JS_SRC}")
    css_map = write_css()
    js_map = write_js()
    write_shell(css_map, js_map)


if __name__ == "__main__":
    main()
