---
layout: default
title: Printable guides
description: Printable PDF guides from Home Automation Cookbook. A starter house setup guide, condensed recipe cards for every recipe, or both together.
permalink: /shop/
---

# Printable guides

Everything on this site stays free to read. The PDFs save you time. Print them, keep them by the hub, and follow along.

<div class="shop-grid">
<div class="shop-item">
{% include responsive-img.html src="/assets/img/guides/starter-pdf-cover.jpg" alt="Cover of the Starter House Setup Guide PDF" width="640" height="829" sizes="220px" loading="lazy" %}
<h2>Starter House Setup Guide</h2>
<p>Setting up your first smart home? Get your questions answered before you buy. Follow a four-weekend plan to a working house, one room at a time. Then add more as you go, without starting over.</p>
<p class="shop-meta">Includes a shopping list, room-by-room checklists, 11 step-by-step walkthroughs and troubleshooting.</p>
<p class="shop-meta">PDF, 14 pages, US Letter</p>
<p class="shop-price">$12</p>
<a class="home-button-primary" href="https://buy.stripe.com/00w14o94T6c2fGf1tggrS00">Buy for $12</a>
</div>
<div class="shop-item">
{% include responsive-img.html src="/assets/img/guides/recipe-pdf-cover.jpg" alt="Cover of the Recipe Cards PDF" width="640" height="829" sizes="220px" loading="lazy" %}
<h2>Recipe Cards</h2>
<p>Automations that work, ready to print. Each card shows the devices, trigger, conditions and actions on one page, so you can set it up quickly. No digging through the site. Scan the QR code when you want the full details.</p>
<p class="shop-meta">PDF, 64 pages, 61 recipes, one per page, US Letter</p>
<p class="shop-price">$12</p>
<a class="home-button-primary" href="https://buy.stripe.com/14AcN63Kz2ZQeCb9ZMgrS01">Buy for $12</a>
</div>
<div class="shop-item shop-item--best">
{% include responsive-img.html src="/assets/img/guides/bundle-pdf-cover.jpg" alt="Covers of both printable guides" width="640" height="829" sizes="220px" loading="lazy" %}
<span class="shop-tag" id="bundle-tag">Best value</span>
<h2>Both guides</h2>
<p>Everything from your first setup to everyday wins. Use the plan to get a working house, then pick your next automation from the cards.</p>
<p class="shop-meta">2 PDFs, 78 pages total</p>
<p class="shop-price" id="bundle-price">$20 <span class="shop-meta">instead of $24</span></p>
<a class="home-button-primary" id="bundle-buy" href="https://buy.stripe.com/3cIcN66WL57Y1Ppb3QgrS02">Buy both for $20</a>
</div>
</div>

Payment is handled by Stripe. After paying, you go straight to a download page. Questions? Email [mads@homeautomationcookbook.com](mailto:mads@homeautomationcookbook.com).

{% include sale-window.html %}
<script>(function(){var s=window.hacSale&&window.hacSale();if(!s)return;var d={{ site.data.sales | jsonify }};
document.getElementById("bundle-tag").textContent=(s.emoji?s.emoji+" ":"")+s.label+": $"+d.sale_price+" through "+s.endLabel;
document.getElementById("bundle-price").innerHTML="$"+d.sale_price+" <s class=\"shop-meta\">$"+d.regular_price+"</s> <span class=\"shop-meta\">(instead of $"+d.list_price+")</span>";
var b=document.getElementById("bundle-buy");b.href=d.sale_link;b.textContent="Buy both for $"+d.sale_price;})();</script>
