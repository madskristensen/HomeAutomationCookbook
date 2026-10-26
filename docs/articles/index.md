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

<div class="card-grid">
{% for article in sorted_articles %}
  {% assign article_url = article.url | relative_url %}
  {% assign article_date = article.date | date: "%B %-d, %Y" %}
  {% include automation-card.html
    url=article_url
    title=article.title
    description=article.description
    meta_label="Published"
    meta_value=article_date
    link_text="Read article"
  %}
{% endfor %}
</div>

{% include page-navigation.html
  left_url="/"
  left_label="Back to home"
  right_url="/automation/index.html"
  right_label="Browse automation recipes"
%}
