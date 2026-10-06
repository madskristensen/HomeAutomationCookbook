---
layout: default
title: Home automation articles
description: Explanations and comparisons that support the recipe library, listed with the newest article first.
image: /assets/img/social/guides/articles.png
permalink: /articles/index.html
canonical_url: https://www.homeautomationcookbook.com/articles/index.html
---

# Home automation articles

{% include content-hero.html src="/assets/img/social/guides/articles.svg" alt="Home automation articles explaining technologies, tradeoffs, and design choices" %}

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

{% include page-navigation.html
  left_url="/"
  left_label="Back to home"
  right_url="/automation/index.html"
  right_label="Browse automation recipes"
%}
