#!/usr/bin/env python3
"""Build the printable Recipe Cards PDF from docs/automation/**/*.md.

Usage: python3 scripts/build-recipe-pdf.py [--out PATH] [--html-only]
Requires: PyYAML, qrcode, google-chrome (headless) for PDF output.
"""
import argparse, base64, html, io, pathlib, re, subprocess, sys
import yaml, qrcode
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "recipe-pdf"))

ROOT = pathlib.Path("/workspace/HomeAutomationCookbook")
DOCS = ROOT / "docs"
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from rp import recipe_page
SITE = "https://www.homeautomationcookbook.com"
SHORT = "homeautomationcookbook.com"
ORDER = ["lighting", "security", "appliances", "climate", "notifications", "daily-routines", "entertainment"]
DEFAULT_OUT = HERE.parent / "hac-recipe-cards-v2.pdf"

def clean(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\*\*|__|`|\{%.*?%\}|<[^>]+>", "", s)
    s = re.sub(r",? (?:which|that) is what I use", "", s)
    s = re.sub(r"^On \w+, I use (?:the )?", "", s)
    s = s.replace("\u2014", ", ").replace("\u2013", "-")
    return html.escape(re.sub(r"\s+", " ", s).strip())

def first_sentences(s, n=2):
    s = re.sub(r",? (?:which|that) is what I use", "", s)
    parts = [x for x in re.split(r"(?<=[.!?])\s+", s.strip()) if not re.search(r"\bI\b|\b[Mm]y\b", x)]
    return " ".join(parts[:n])

def section(body, name):
    m = re.search(r"^## " + name + r"[^\n]*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return m.group(1) if m else ""

def parse(path):
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    _, fm, body = raw.split("---", 2)
    meta = yaml.safe_load(fm)
    cat = path.parent.name
    url = f"/automation/{cat}/{path.stem}.html"
    logic = {}
    for key, label in [("Trigger", "When"), ("Conditions?", "Only if"), ("Actions?", "Do"), ("Stop condition", "Stop")]:
        m = re.search(r"^- \*\*" + key + r":\*\*\s*(.+)$", body, re.M)
        if m:
            logic[label] = first_sentences(clean(m.group(1)), 2)
    devices = []
    used = section(body, "What I used")
    for job, txt in re.findall(r"\*\*([^*\n]+)\*\*\s*\n\s*\n([^\n]+)", used):
        lm = re.match(r"\s*\[([^\]]+)\]", txt)
        prod = lm.group(1) if lm else re.split(r"\.\s", txt, maxsplit=1)[0]
        if re.match(r"(I |My |We )", prod):
            prod = ""
        devices.append((clean(job), clean(prod)))
    tip = ""
    notes = section(body, "Setup notes")
    m = re.search(r"^\s*(?:\d+\.|-)\s+(.+)$", notes, re.M)
    if m:
        tip = first_sentences(clean(m.group(1)), 2)
    if not devices:
        devices = []
    return dict(title=clean(meta["title"]), desc=clean(meta.get("description", "")), url=url, cat=cat,
                logic=logic, devices=devices, tip=tip)

def qr(url):
    img = qrcode.make(url, box_size=6, border=1)
    b = io.BytesIO(); img.save(b, format="PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

def cat_title(cat):
    t = yaml.safe_load((DOCS / "automation" / cat / "index.md").read_text(encoding="utf-8").split("---")[1])["title"]
    return re.sub(r"\s*automation recipes$", "", t, flags=re.I)

ZEN = ('<div class="callout warn"><b class="lbl">Check your hub</b><p>The Zooz ZEN15 is a Z-Wave plug-in switch that measures power. '
 'It needs a hub with a Z-Wave radio and does not work with Apple Home, Google Home or Alexa. On those, use any Matter or Zigbee smart plug '
 'with energy monitoring that your hub supports and that is rated for the load.</p></div>')
def card(n, r, cat, page):
    logic = "".join(f'<div class="lg"><b>{k}</b><span>{v}</span></div>' for k, v in r["logic"].items())
    devs = "".join(f"<li>{j}{': ' + p if p else ''}</li>" for j, p in r["devices"]) or "<li>See the full recipe for device options.</li>"
    tip = f'<div class="callout"><b class="lbl">Tip</b><p>{r["tip"]}</p></div>' if r["tip"] else ""
    z = ZEN if "ZEN15" in devs else ""
    body = f"<h4>Devices</h4><ul>{devs}</ul>{z}<h4>Logic</h4>{logic}{tip}"
    return recipe_page(cat, f"Recipe {n}", r["title"], r["desc"], body, r["url"], f"r{n}")

def build():
    recipes = []
    cats = ORDER + sorted(p.name for p in (DOCS / "automation").iterdir() if p.is_dir() and p.name not in ORDER)
    groups = []
    for c in cats:
        files = sorted(p for p in (DOCS / "automation" / c).glob("*.md") if p.name != "index.md")
        rs = sorted((parse(p) for p in files), key=lambda r: r["title"].lower())
        if rs:
            groups.append((c, rs))
    # Page 1 is the cover, page 2 the contents, then exactly one recipe per page.
    FIRST = 3
    n = 0; body = []; toc = []; index = []
    for c, rs in groups:
        start = n + 1
        for r in rs:
            n += 1
            body.append(card(n, r, cat_title(c), n + FIRST - 1)); index.append((r["title"], n + FIRST - 1))
        toc.append(f"<li><span>{cat_title(c)} <small>({n - start + 1} recipes)</small></span><span>{start + FIRST - 1}</span></li>")
    idx_page = n + FIRST
    toc.append(f"<li><span>Index</span><span>{idx_page}</span></li>")
    idx = "".join(f"<li><span>{t}</span><span>{k}</span></li>" for t, k in sorted(index, key=lambda x: x[0].lower()))
    tpl = (HERE / "cards-template.html").read_text(encoding="utf-8")
    out = (tpl.replace("{{COUNT}}", str(n)).replace("{{TOC}}", "".join(toc))
              .replace("{{BODY}}", "".join(body)).replace("{{INDEX}}", idx).replace("{{IDXPAGE}}", str(idx_page)))
    assert "\u2014" not in out, "em dash found"
    return out, n

def main():
    pass
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(DEFAULT_OUT)); ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()
    doc, n = build()
    tmp = HERE / "recipe-cards.html"
    tmp.write_text(doc, encoding="utf-8")
    print(f"{n} recipes -> {tmp}")
    if a.html_only:
        return
    pathlib.Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={a.out}", tmp.as_uri()], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    pass
    print("PDF ->", a.out)
    info = subprocess.run(["pdfinfo", a.out], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    print(f"{pages} pages (expected {n + 3}: cover, contents, {n} recipes, index)")
    if pages != n + 3:
        sys.exit("Page count mismatch: a card or the index overflowed, so printed page numbers are wrong.")

if __name__ == "__main__":
    main()
