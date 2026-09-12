---
layout: default
title: Home automation articles
description: Explanations and comparisons that support the recipe library, listed with the newest article first.
permalink: /articles/index.html
canonical_url: https://www.homeautomationcookbook.com/articles/index.html
---

# Home automation articles

Articles explain a technology, tradeoff, or design decision that applies across several recipes. Use them to understand your options and make confident choices for your own rooms and routines. Unlike the recipe library, this section is chronological.

{% assign sorted_articles = site.articles | sort: "date" | reverse %}

<div class="automation-cards">
{% for article in sorted_articles %}

<div class="automation-card" markdown="1">

<time datetime="{{ article.date | date_to_xmlschema }}">{{ article.date | date: "%B %d, %Y" }}</time>

## [{{ article.title }}]({{ article.url }})

{{ article.description }}

</div>

{% endfor %}
</div>

<div class="page-navigation">
  <a href="/">Back to home</a>
  <a href="/automation/index.html">Browse automation recipes</a>
</div>
