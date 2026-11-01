#!/usr/bin/env python3
"""Build the free '10 starter recipes' PDF (newsletter lead magnet) with the recipe card pipeline.

Usage: python3 scripts/build-starter-pdf.py --out docs/<dl-folder>/hac-10-starter-recipes.pdf
Picks: the 10 recipes with the most Google Search impressions (Aug to Oct 2026).
"""
import argparse, importlib.util, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rp", HERE / "build-recipe-pdf.py"); rp = importlib.util.module_from_spec(spec); spec.loader.exec_module(rp)
sys.path.insert(0, str(rp.HERE)); import covers
PICKS = ["lighting/wake-up-lights", "lighting/lights-on-motion", "lighting/lights-off-after-motion", "lighting/toggle-lights-door",
         "security/fake-dog-deterrent", "security/garage-door-notification", "security/stove-left-on-alert",
         "appliances/fridge-door-alert", "daily-routines/away-mode", "daily-routines/morning-routine"]
SHOP = "https://www.homeautomationcookbook.com/shop/"

def build():
    total = sum(1 for p in (rp.DOCS / "automation").glob("*/*.md") if p.name != "index.md")
    more = total - len(PICKS)
    body, toc = [], []
    for n, k in enumerate(PICKS, 1):
        cat = k.split("/")[0]; r = rp.parse(rp.DOCS / "automation" / f"{k}.md")
        body.append(rp.card(n, r, rp.cat_title(cat), n + 2)); toc.append(f"<li><span>{r['title']}</span><span>{n + 2}</span></li>")
    last = (f'<section class="idxwrap"><h2>{more} more in the full set</h2>'
            f'<p>You have the 10 most popular recipes. The full Recipe Cards PDF has all {total}, one page each, with the same QR codes.</p>'
            f'<p>Lighting, security, climate, appliances, notifications, routines, and music. Print the ones you need and keep them by the hub.</p>'
            f'<div class="qr" style="margin:28px 0"><img src="{rp.qr(SHOP)}"><span>Scan to see the full set</span></div>'
            f'<p><a href="{SHOP}">{SHOP}</a></p>'
            f'<p class="small">Every recipe also stays free to read on the site.</p></section>')
    tpl = (rp.HERE / "template.html").read_text(encoding="utf-8")
    tpl = tpl.replace("cover-recipes.svg", "cover-starter10.svg").replace("Recipe Cards</title>", "10 Starter Recipes</title>")
    tpl = re.sub(r'<section class="idxwrap">.*?</section>', "{{LAST}}", tpl, flags=re.S)
    out = tpl.replace("{{TOC}}", "".join(toc)).replace("{{BODY}}", "".join(body)).replace("{{LAST}}", last)
    assert "\u2014" not in out and "{{" not in out
    return out, more

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    (rp.HERE / "cover-starter10.svg").write_text(covers.cover("FREE SAMPLER", ["10 starter", "recipes"],
        ["The most popular recipes from the site,", "one printable page each, with a QR code", "to the full recipe."], "cards"))
    doc, more = build(); tmp = rp.HERE / "starter10.html"; tmp.write_text(doc, encoding="utf-8")
    pathlib.Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={a.out}", tmp.as_uri()], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    tmp.unlink()
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", a.out], capture_output=True, text=True).stdout).group(1))
    print(f"PDF -> {a.out}: {pages} pages (expected 13), {more} more in full set")
    if pages != 13: sys.exit("page count mismatch")

if __name__ == "__main__":
    main()
