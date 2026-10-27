"""Typeset covers (HTML, so the embedded fonts are used)."""
HOUSE = '''<svg viewBox="0 0 300 300" fill="none" stroke="#2c3e50" stroke-width="1.4" stroke-linecap="square">
<rect x="10" y="10" width="280" height="280"/><path d="M130 10v100h160M10 175h120v115M200 110v180"/>
<path d="M40 70a60 60 0 0 1 60 60H40z" stroke="#9a6b45" stroke-width="1"/><circle cx="40" cy="70" r="3" fill="#9a6b45" stroke="none"/>
<path d="M235 205h36M253 187v36" stroke="#9aa2a6"/><path d="M130 140v20M200 60h0" stroke="#faf8f3" stroke-width="3"/></svg>'''
CARDS = '''<svg viewBox="0 0 300 300" fill="none" stroke="#2c3e50" stroke-width="1.4">
<rect x="44" y="28" width="190" height="250" transform="rotate(-6 139 153)" stroke="#9aa2a6"/>
<rect x="70" y="24" width="190" height="250" fill="#faf8f3"/>
<path d="M92 62h90" stroke-width="2.2"/><path d="M92 92h140M92 112h120M92 132h132M92 152h96" stroke="#9aa2a6" stroke-width="1"/>
<rect x="196" y="210" width="44" height="44" stroke="#9a6b45" stroke-width="1"/><path d="M204 218h10v10h-10zM222 236h10v10h-10z" stroke="#9a6b45" stroke-width="1"/></svg>'''

def cover(kicker, title, sub, art, corner, edition="Printable edition"):
    return (f'<section class="cover"><div class="cv-top"><span>Home Automation Cookbook</span><span>{corner}</span></div>'
            f'<div class="cv-main"><p class="kicker">{kicker}</p><h1>{title}</h1><p class="cv-sub">{sub}</p></div>'
            f'<div class="cv-art">{art}</div><div class="cv-foot"><span>www.homeautomationcookbook.com</span><span>{edition}</span></div></section>')

STARTER = cover("Starter plan", "Starter house<br><i>setup guide</i>",
    "One hub, about ten devices, and one working recipe per room. A printable plan for your first month.", HOUSE, "Your first month")
RECIPES = cover("Recipe cards", "Recipe<br><i>cards</i>",
    "Every recipe from the site on one printable page each, with a QR code to the full recipe.", CARDS, "61 recipes")
