#!/usr/bin/env python3
"""Make a vertical, mobile-friendly copy (<name>-stacked.svg) of each wide flow diagram in docs/assets/img/diagrams.
Reads each box's title and subtitle in order, then stacks them with down arrows. Run after editing a diagram."""
import pathlib, re
D = pathlib.Path(__file__).resolve().parent.parent / "docs/assets/img/diagrams"
for f in sorted(D.glob("*.svg")):
    if f.stem.endswith("-stacked"): continue
    s = f.read_text()
    title = re.search(r"<title[^>]*>(.*?)</title>", s).group(1); desc = re.search(r"<desc[^>]*>(.*?)</desc>", s).group(1)
    style = re.search(r"<style>.*?</style>", s, re.S).group(0)
    boxes = []
    for attrs, t in re.findall(r'<text([^>]*)>(.*?)</text>', s):
        if "font-weight" in attrs or not boxes: boxes.append([t])
        else: boxes[-1].append(t)
    W, BW, BH, GAP, P = 360, 320, 104, 56, 20
    H = P * 2 + len(boxes) * BH + (len(boxes) - 1) * GAP
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc>{style}',
           f'<rect width="{W}" height="{H}" rx="16" fill="#fafafa" /><g font-family="system-ui, sans-serif" text-anchor="middle" fill="#2c3e50">']
    arrows = []
    for i, b in enumerate(boxes):
        y = P + i * (BH + GAP)
        out.append(f'<rect x="{(W-BW)//2}" y="{y}" width="{BW}" height="{BH}" rx="12" fill="#f8f9fa" stroke="#e0e0e0" stroke-width="2" />')
        out.append(f'<text x="{W//2}" y="{y+44}" font-size="22" font-weight="600">{b[0]}</text>')
        if len(b) > 1: out.append(f'<text x="{W//2}" y="{y+76}" font-size="18">{b[1]}</text>')
        if i < len(boxes) - 1:
            a, z = y + BH + 8, y + BH + GAP - 8
            arrows.append(f'<line x1="{W//2}" y1="{a}" x2="{W//2}" y2="{z-12}" /><polygon points="{W//2},{z} {W//2-10},{z-16} {W//2+10},{z-16}" />')
    out.append('</g><g stroke="#2c3e50" stroke-width="4" fill="#2c3e50">' + "".join(arrows) + '</g></svg>')
    (D / f"{f.stem}-stacked.svg").write_text("".join(out))
    print(f.stem, [b[0] for b in boxes])
