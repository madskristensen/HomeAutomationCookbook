"""Shared recipe page markup for the Starter guide and the Recipe Cards."""
import base64, io, qrcode
SITE = "https://www.homeautomationcookbook.com"
SHORT = "www.homeautomationcookbook.com"

def qr(url):
    img = qrcode.make(url, box_size=8, border=0)
    b = io.BytesIO(); img.save(b, format="PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

def side(path):
    return (f'<aside class="rp-side"><img src="{qr(SITE + path)}" alt="QR code">'
            f'<p class="cap">Scan for the full recipe</p></aside>')

def recipe_page(cat, num, title, lede, body, path, rid="", cont_body=None):
    """One recipe per page. If cont_body is given, it flows onto a second page with a 'continued' marker."""
    head = f'<header class="rp-head"><span class="rp-cat">{cat}</span><span class="rp-num">{num}</span></header>'
    p1 = (f'<article class="rp" id="{rid}">{head}<h2>{title}</h2><p class="lede">{lede}</p>'
          f'<div class="rp-cols"><div class="rp-main">{body}'
          + ('<p class="rp-cont">Continued overleaf</p>' if cont_body else "")
          + f'</div>{side(path)}</div></article>')
    if not cont_body:
        return p1
    p2 = (f'<article class="rp">{head}<p class="rp-cont rp-cont-top" style="text-align:left">Continued</p><h2>{title}</h2>'
          f'<div class="rp-cols"><div class="rp-main">{cont_body}</div><aside class="rp-side"></aside></div></article>')
    return p1 + p2
