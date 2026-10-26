---
layout: default
title: Printable guides
description: Printable PDF guides from Home Automation Cookbook. A starter house setup guide, condensed recipe cards for every recipe, or both together.
permalink: /shop/
---

# Printable guides

Everything on this site stays free to read. These PDFs are for people who want the same advice on paper, next to the hub, with boxes to check.

<div class="shop-grid">
<div class="shop-item">
{% include responsive-img.html src="/assets/img/guides/starter-pdf-cover.jpg" alt="Cover of the Starter House Setup Guide PDF" width="640" height="829" sizes="220px" loading="lazy" %}
<h2>Starter House Setup Guide</h2>
<p>A plan for your first month: one hub, about ten devices, room-by-room checklists, a shopping list, and step-by-step walkthroughs for 11 starter recipes.</p>
<p class="shop-meta">PDF, 14 pages, US Letter</p>
<p class="shop-price">$12</p>
<a class="home-button-primary" href="https://buy.stripe.com/00w14o94T6c2fGf1tggrS00">Buy for $12</a>
</div>
<div class="shop-item">
{% include responsive-img.html src="/assets/img/guides/recipe-pdf-cover.jpg" alt="Cover of the Recipe Cards PDF" width="640" height="829" sizes="220px" loading="lazy" %}
<h2>Recipe Cards</h2>
<p>Every recipe on the site, condensed to one printable page: what it does, devices, trigger, conditions, and actions, one tip, and a QR code to the full recipe. Grouped by category, with contents and an index.</p>
<p class="shop-meta">PDF, 64 pages, 61 recipes, one per page, US Letter</p>
<p class="shop-price">$12</p>
<a class="home-button-primary" href="https://buy.stripe.com/14AcN63Kz2ZQeCb9ZMgrS01">Buy for $12</a>
</div>
<div class="shop-item shop-item--best">
{% include responsive-img.html src="/assets/img/guides/bundle-pdf-cover.jpg" alt="Covers of both printable guides" width="640" height="829" sizes="220px" loading="lazy" %}
<span class="shop-tag" id="bundle-tag">Best value</span>
<h2>Both guides</h2>
<p>The Starter House Setup Guide and the Recipe Cards together. Start with the plan, then keep the cards for everything you add later.</p>
<p class="shop-meta">2 PDFs, 78 pages total</p>
<p class="shop-price" id="bundle-price">$20 <span class="shop-meta">instead of $24</span></p>
<a class="home-button-primary" id="bundle-buy" href="https://buy.stripe.com/3cIcN66WL57Y1Ppb3QgrS02">Buy both for $20</a>
</div>
</div>

Payment is handled by Stripe. After paying, you go straight to a download page. Questions? Email [mads@homeautomationcookbook.com](mailto:mads@homeautomationcookbook.com).

{% include sale-window.html %}
<script>(function(){var s=window.hacSale&&window.hacSale();if(!s)return;var d={{ site.data.sales | jsonify }};
document.getElementById("bundle-tag").textContent=s.label+": $"+d.sale_price+" through "+s.endLabel;
document.getElementById("bundle-price").innerHTML="$"+d.sale_price+" <s class=\"shop-meta\">$"+d.regular_price+"</s> <span class=\"shop-meta\">(instead of $"+d.list_price+")</span>";
var b=document.getElementById("bundle-buy");b.href=d.sale_link;b.textContent="Buy both for $"+d.sale_price;})();</script>
