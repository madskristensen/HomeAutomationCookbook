#!/usr/bin/env python3
"""Fail if a PR changes the content of a dated docs page without updating last_modified_at.

A dated page is a docs/*.md file that has a last_modified_at field on the
base or head revision. Content means the markdown body plus content-bearing
frontmatter such as products and faqs. Title, description, tags, and other
metadata changes do not require a lastmod bump.

Bypass a mass frontmatter or template sweep by adding the skip-lastmod-check
label on the pull request, or by putting Skip-Lastmod-Check: true in a commit
message on the branch.

Usage:
  python3 script/check-lastmod.py --base ORIGIN/MAIN --head HEAD
  python3 script/check-lastmod.py --base SHA --head SHA

Environment:
  BASE_SHA, HEAD_SHA, PR_LABELS (comma-separated), SKIP_LASTMOD_CHECK=1
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

METADATA_KEYS = {
    "layout",
    "title",
    "description",
    "date",
    "last_modified_at",
    "image",
    "keywords",
    "tags",
    "compact",
    "cta_category",
    "cta_newsletter",
    "cta_recipe",
    "permalink",
    "canonical_url",
    "canonical",
    "pdf_promo_card",
    "redirect_from",
    "sitemap",
    "published",
    "categories",
    "excerpt",
}

LASTMOD_RE = re.compile(r"^last_modified_at:\s*['\"]?([^\s#]+)", re.M)
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)
TOP_KEY_RE = re.compile(r"^([A-Za-z0-9_]+)\s*:")
SKIP_TOKEN = "skip-lastmod-check"
SKIP_TRAILER_RE = re.compile(r"(?im)^skip-lastmod-check:\s*(true|yes|1)\s*$")


def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def show_file(rev: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{rev}:{path}"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def split_frontmatter(text: str) -> tuple[str, str]:
    match = FM_RE.match(text)
    if not match:
        return "", text
    return match.group(1), text[match.end() :]


def frontmatter_blocks(fm: str) -> dict[str, str]:
    blocks: dict[str, list[str]] = {}
    current = None
    for line in fm.splitlines():
        key_match = TOP_KEY_RE.match(line)
        if key_match and not line.startswith((" ", "\t")):
            current = key_match.group(1)
            blocks[current] = [line]
        elif current is not None:
            blocks[current].append(line)
    return {key: "\n".join(lines) for key, lines in blocks.items()}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def lastmod_value(text: str | None) -> str | None:
    if not text:
        return None
    fm, _ = split_frontmatter(text)
    match = LASTMOD_RE.search(fm)
    return match.group(1).strip().strip("\"'") if match else None


def content_fingerprint(text: str | None) -> str | None:
    if text is None:
        return None
    fm, body = split_frontmatter(text)
    blocks = frontmatter_blocks(fm)
    content_fm = []
    for key, raw in sorted(blocks.items()):
        if key in METADATA_KEYS:
            continue
        content_fm.append(f"{key}:{normalize(raw)}")
    return "\n".join(content_fm) + "\n--BODY--\n" + normalize(body)


def content_changed(old: str | None, new: str | None) -> bool:
    if old is None or new is None:
        return old != new
    return content_fingerprint(old) != content_fingerprint(new)


def changed_markdown_paths(base: str, head: str) -> list[tuple[str, str, str]]:
    """Return (status, old_path, new_path) for docs markdown changes."""
    output = git("diff", "--name-status", "--find-renames", f"{base}...{head}", "--", "docs")
    rows = []
    for line in output.splitlines():
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") and len(parts) == 3:
            old, new = parts[1], parts[2]
        elif status.startswith("C") and len(parts) == 3:
            old, new = parts[1], parts[2]
        elif len(parts) == 2:
            old = new = parts[1]
        else:
            continue
        if not new.endswith(".md") and not old.endswith(".md"):
            continue
        rows.append((status[0], old, new))
    return rows



def today_pt() -> str:
    return datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()


def skip_requested(labels: str, log: str) -> str | None:
    if os.environ.get("SKIP_LASTMOD_CHECK", "").strip() in {"1", "true", "yes"}:
        return "SKIP_LASTMOD_CHECK is set"
    for label in labels.split(","):
        if label.strip().lower() == SKIP_TOKEN:
            return f"pull request has the {SKIP_TOKEN} label"
    if SKIP_TRAILER_RE.search(log):
        return "a commit message has a Skip-Lastmod-Check: true trailer"
    return None


def annotate(kind: str, path: str, message: str) -> None:
    # GitHub workflow command. Path is repo-relative.
    safe = message.replace("\n", " ").replace("%", "%25")
    print(f"::{kind} file={path}::{safe}")


def check(base: str, head: str, labels: str) -> int:
    log = git("log", "--format=%B", f"{base}..{head}", check=False)
    reason = skip_requested(labels, log)
    if reason:
        print(f"::notice::last_modified_at check skipped because {reason}.")
        print(f"lastmod check: skipped ({reason}).")
        return 0

    problems = []
    checked = 0
    for status, old_path, new_path in changed_markdown_paths(base, head):
        old_text = None if status == "A" else show_file(base, old_path)
        new_text = None if status == "D" else show_file(head, new_path)
        old_lastmod = lastmod_value(old_text)
        new_lastmod = lastmod_value(new_text)
        if old_lastmod is None and new_lastmod is None:
            continue
        checked += 1
        path = new_path if new_text is not None else old_path
        if status == "D":
            # Deleting a dated page is not a lastmod issue.
            continue
        if not content_changed(old_text, new_text):
            continue
        if new_lastmod is None:
            problems.append(
                (path, "content changed but last_modified_at was removed")
            )
        elif new_lastmod == old_lastmod:
            if new_lastmod == today_pt():
                # Already set to today in PT; a later same-day edit is fine.
                continue
            problems.append(
                (
                    path,
                    "content changed but last_modified_at stayed "
                    f"{old_lastmod}; update it to the date of this change "
                    f"(or bypass with the {SKIP_TOKEN} label or a "
                    "Skip-Lastmod-Check: true commit trailer)",
                )
            )
    for path, message in problems:
        annotate("error", path, message)
        print(f"ERROR {path}: {message}")
    print(f"lastmod check: {checked} dated content file(s) inspected, {len(problems)} problem(s).")
    return 1 if problems else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default=os.environ.get("BASE_SHA") or "")
    parser.add_argument("--head", default=os.environ.get("HEAD_SHA") or "HEAD")
    parser.add_argument(
        "--labels",
        default=os.environ.get("PR_LABELS") or "",
        help="comma-separated PR labels",
    )
    args = parser.parse_args()
    if not args.base:
        print("ERROR: --base or BASE_SHA is required", file=sys.stderr)
        return 2
    return check(args.base, args.head, args.labels)


if __name__ == "__main__":
    sys.exit(main())
