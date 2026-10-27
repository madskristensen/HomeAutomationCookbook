"""Shared recipe page markup for the Starter guide and the Recipe Cards."""
import base64, io, qrcode
SITE = "https://www.homeautomationcookbook.com"
SHORT = "www.homeautomationcookbook.com"

def qr(url):
    img = qrcode.make(url, box_size=6, border=1)
    b = io.BytesIO(); img.save(b, format="PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

def recipe_page(pill, num, title, lede, body, path, rid=""):
    return f'''<article class="rp" id="{rid}"><div class="rp-top"><span class="pill">{pill}</span><span class="rp-num">{num}</span></div>
<h2>{title}</h2><p class="lede">{lede}</p><div class="rp-cols"><div class="rp-main">{body}</div>
<aside class="rp-side"><div class="qrbox"><img src="{qr(SITE + path)}"><span>Scan for the full recipe</span><span class="url">{SHORT}{path}</span></div></aside></div></article>'''
