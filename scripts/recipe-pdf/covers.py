#!/usr/bin/env python3
"""Portrait PDF covers in the site's card style (see scripts/generate-guide-images.rb).

Usage: python3 scripts/recipe-pdf/covers.py  -> writes cover-starter.svg and cover-recipes.svg here.
"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
F = 'font-family="Segoe UI, Arial, sans-serif"'
ART = {
"floorplan": '''<g transform="translate(208 520) scale(.85)" fill="none" stroke="#2c3e50" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">
  <rect x="25" y="25" width="420" height="420" fill="#eef2f3"/>
  <path d="M205 25v155h240M25 275h180v170M310 180v265"/>
  <path d="M78 112a120 120 0 0 1 120 120H78z" fill="#ffffff" stroke="#6f8f96"/>
  <circle cx="78" cy="112" r="15" fill="#6f8f96" stroke="none"/>
  <path d="M310 320h74M347 283v74" stroke="#9db1b6"/></g>''',
"cards": '''<g transform="translate(168 480)" fill="none" stroke="#2c3e50" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">
  <rect x="60" y="20" width="330" height="390" rx="26" fill="#eef2f3" transform="rotate(-8 225 215)"/>
  <rect x="90" y="40" width="330" height="390" rx="26" fill="#ffffff"/>
  <path d="M135 110h150M135 165h220M135 220h190M135 275h120" stroke="#6f8f96" stroke-width="7"/>
  <rect x="300" y="320" width="80" height="80" rx="8" stroke="#9db1b6" stroke-width="7"/>
  <path d="M322 342h12v12h-12zM346 366h12v12h-12z" stroke="#9db1b6" stroke-width="6"/></g>''',
}
def cover(pill, title_lines, sub_lines, art):
    pw = 30 + len(pill) * 12.5
    t = "".join(f'<text x="96" y="{230 + i*72}" fill="#2c3e50" {F} font-size="64" font-weight="700">{l}</text>' for i, l in enumerate(title_lines))
    y0 = 230 + len(title_lines) * 72 + 28
    s = "".join(f'<text x="96" y="{y0 + i*36}" fill="#5d6d75" {F} font-size="25">{l}</text>' for i, l in enumerate(sub_lines))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="816" height="1056" viewBox="0 0 816 1056">
<rect width="816" height="1056" fill="#f8f9fa"/>
<rect x="40" y="40" width="736" height="976" rx="28" fill="#ffffff" stroke="#e0e0e0" stroke-width="2"/>
<rect x="96" y="96" width="{pw:.0f}" height="43" rx="21" fill="#eef2f3"/>
<text x="117" y="124" fill="#2c3e50" {F} font-size="19" font-weight="600">{pill}</text>
{t}{s}{ART[art]}
<text x="96" y="975" fill="#6b777c" {F} font-size="20">HOME AUTOMATION COOKBOOK</text>
<text x="720" y="975" text-anchor="end" fill="#6b777c" {F} font-size="20">PRINTABLE PDF</text>
</svg>'''
def main():
    (HERE / "cover-starter.svg").write_text(cover("STARTER PLAN", ["Starter house", "setup guide"],
        ["One hub, about ten devices, and one working", "recipe per room. A printable plan for your", "first month."], "floorplan"))
    (HERE / "cover-recipes.svg").write_text(cover("RECIPE CARDS", ["Recipe cards"],
        ["Every recipe from the site on one printable", "page each, with a QR code to the full recipe."], "cards"))
if __name__ == "__main__":
    main()
