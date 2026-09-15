---
layout: default
title: Automation recipes
description: Browse platform-neutral home automation recipes with plain-English logic, physical controls, tested failure behavior, and clear acceptance checks.
permalink: /automation/index.html
canonical_url: https://www.homeautomationcookbook.com/automation/index.html
recipe_directory: true
---

# Automation recipes

Start with the household job, not the app. Choose something you want to stop remembering, checking, or adjusting. Each recipe then explains what triggers the automation, what conditions must be true, what ends it, and what should happen when a device stops reporting.

You can copy a recipe, change it to fit your household, or use its logic as a starting point for a routine that is entirely your own.

## Find a recipe by what you need

<div class="job-grid">
  <div class="job-card">
    <h3>Stop remembering and checking</h3>
    <ul>
      <li><a href="/automation/appliances/washer-done-notification.html">Know when the washer finishes</a></li>
      <li><a href="/automation/security/garage-door-notification.html">Notice a garage door left open</a></li>
      <li><a href="/automation/appliances/fridge-door-alert.html">Catch an open fridge or freezer</a></li>
      <li><a href="/automation/notifications/low-battery-alerts.html">Find batteries before devices fail</a></li>
    </ul>
  </div>

  <div class="job-card">
    <h3>Move through the house more easily</h3>
    <ul>
      <li><a href="/automation/lighting/lights-on-motion.html">Turn lights on when entering</a></li>
      <li><a href="/automation/lighting/lights-off-after-motion.html">Turn lights off after leaving</a></li>
      <li><a href="/automation/lighting/bathroom-night-light.html">Use gentle bathroom light at night</a></li>
      <li><a href="/automation/lighting/toggle-lights-door.html">Light a closet or pantry</a></li>
    </ul>
  </div>

  <div class="job-card">
    <h3>Reduce repeated adjustments</h3>
    <ul>
      <li><a href="/automation/climate/thermostat-windows-open.html">Pause HVAC for an open window</a></li>
      <li><a href="/automation/climate/safe-thermostat-away.html">Use a safe away temperature</a></li>
      <li><a href="/automation/climate/fan-shower.html">Run the fan after a shower</a></li>
      <li><a href="/automation/climate/blinds-sunset-sunrise.html">Move blinds with sunrise and sunset</a></li>
    </ul>
  </div>

  <div class="job-card">
    <h3>Coordinate household transitions</h3>
    <ul>
      <li><a href="/automation/daily-routines/away-mode.html">Settle the house after everyone leaves</a></li>
      <li><a href="/automation/daily-routines/unlock-door-arrival.html">Prepare the house on arrival</a></li>
      <li><a href="/automation/daily-routines/guest-mode.html">Keep the house predictable for guests</a></li>
      <li><a href="/automation/daily-routines/bedtime-routine.html">Wind down without disturbing others</a></li>
    </ul>
  </div>

  <div class="job-card">
    <h3>Notice safety-related conditions</h3>
    <ul>
      <li><a href="/automation/security/water-leak-response.html">Respond to detected water</a></li>
      <li><a href="/automation/security/garage-door-notification.html">Keep an open garage visible</a></li>
      <li><a href="/automation/security/fire-safety.html">Add supplemental fire response</a></li>
      <li><a href="/automation/security/stove-left-on-alert.html">Create a stove reminder</a></li>
    </ul>
  </div>
</div>

Not sure where an idea belongs? Search by a room, device, or burden such as "laundry," "bathroom," "guest," or "window."

## Choose a category

<div class="category-grid">

<a href="/automation/lighting/index.html" class="category-card">
<h3>Lighting</h3>
<p>Use motion, doors, schedules, and light levels without taking away the wall switch.</p>
<span class="category-count">8 recipes</span>
</a>

<a href="/automation/daily-routines/index.html" class="category-card">
<h3>Daily routines</h3>
<p>Coordinate morning, bedtime, guest, arrival, and away behavior without guessing who is home.</p>
<span class="category-count">5 recipes</span>
</a>

<a href="/automation/climate/index.html" class="category-card">
<h3>Climate and comfort</h3>
<p>Reduce waste while preserving thermostat limits, manual holds, ventilation, and safe temperatures.</p>
<span class="category-count">6 recipes + 1 guide</span>
</a>

<a href="/automation/entertainment/index.html" class="category-card">
<h3>Entertainment</h3>
<p>Make music and TV behavior easier to start, stop, and adjust with familiar controls.</p>
<span class="category-count">6 recipes</span>
</a>

<a href="/automation/appliances/index.html" class="category-card">
<h3>Appliances</h3>
<p>Observe appliance cycles, send useful reminders, and avoid unsafe power control.</p>
<span class="category-count">7 recipes</span>
</a>

<a href="/automation/security/index.html" class="category-card">
<h3>Safety and security</h3>
<p>Use alerts and approved equipment without treating weak sensor signals as proof of safety.</p>
<span class="category-count">7 recipes</span>
</a>

<a href="/automation/notifications/index.html" class="category-card">
<h3>Notifications and alerts</h3>
<p>Keep important conditions visible while limiting duplicates and unnecessary interruptions.</p>
<span class="category-count">10 recipes</span>
</a>

</div>

## Search all recipes

<div class="recipe-search" role="search">
  <div class="recipe-search-controls">
    <div class="recipe-search-field">
      <label for="recipe-query">What do you want the house to help with?</label>
      <input id="recipe-query" type="search" placeholder="Try laundry, bathroom, guest, or window" autocomplete="off">
    </div>
    <div class="recipe-filter-field">
      <label for="recipe-category">Category</label>
      <select id="recipe-category">
        <option value="">All categories</option>
        <option value="lighting">Lighting</option>
        <option value="daily-routines">Daily routines</option>
        <option value="climate">Climate and comfort</option>
        <option value="entertainment">Entertainment</option>
        <option value="appliances">Appliances</option>
        <option value="security">Safety and security</option>
        <option value="notifications">Notifications and alerts</option>
      </select>
    </div>
  </div>
  <p id="recipe-results-status" class="recipe-results-status" aria-live="polite"></p>
</div>

{% assign recipes = site.pages | where: "layout", "automation" | sort: "title" %}
<div id="recipe-directory" class="automation-cards recipe-directory">
{% for recipe in recipes %}
  {% assign path_parts = recipe.url | split: "/" %}
  {% assign category_key = path_parts[2] %}
  {% case category_key %}
    {% when "lighting" %}
      {% assign category_name = "Lighting" %}
      {% assign recipe_type = "Reversible control" %}
      {% assign recipe_needs = "A trigger plus a controllable light" %}
    {% when "daily-routines" %}
      {% assign category_name = "Daily routines" %}
      {% assign recipe_type = "Routine coordination" %}
      {% assign recipe_needs = "Household modes plus a deliberate or tested trigger" %}
    {% when "climate" %}
      {% assign category_name = "Climate and comfort" %}
      {% assign recipe_type = "Comfort control or alert" %}
      {% assign recipe_needs = "A condition sensor plus approved controls" %}
    {% when "entertainment" %}
      {% assign category_name = "Entertainment" %}
      {% assign recipe_type = "Reversible control" %}
      {% assign recipe_needs = "A tested media trigger plus a speaker or light" %}
    {% when "appliances" %}
      {% assign category_name = "Appliances" %}
      {% assign recipe_type = "Observation or reminder" %}
      {% assign recipe_needs = "An appliance signal plus a notification path" %}
    {% when "security" %}
      {% assign category_name = "Safety and security" %}
      {% assign recipe_type = "Alert or supplemental action" %}
      {% assign recipe_needs = "A purpose-fit sensor plus a notification path" %}
    {% when "notifications" %}
      {% assign category_name = "Notifications and alerts" %}
      {% assign recipe_type = "Status or reminder" %}
      {% assign recipe_needs = "A source signal plus shared status or notifications" %}
  {% endcase %}
  {% assign starter_urls = "/automation/lighting/lights-on-motion.html|/automation/lighting/lights-off-after-motion.html|/automation/appliances/washer-done-notification.html|/automation/notifications/low-battery-alerts.html" %}
  <article class="automation-card recipe-directory-card"
    data-category="{{ category_key }}"
    data-search="{{ recipe.title | append: ' ' | append: recipe.description | append: ' ' | append: recipe.keywords | append: ' ' | append: category_name | append: ' ' | append: recipe_type | append: ' ' | append: recipe_needs | downcase | escape }}">
    <span class="card-meta">{{ category_name }}</span>
    <h3><a href="{{ recipe.url }}">{{ recipe.title }}</a></h3>
    <p>{{ recipe.description }}</p>
    <dl class="recipe-card-details">
      <div><dt>Type</dt><dd>{{ recipe_type }}</dd></div>
      <div><dt>Needs</dt><dd>{{ recipe_needs }}</dd></div>
      <div><dt>Starting point</dt><dd>{% if starter_urls contains recipe.url %}Good first automation{% else %}Review setup and failure modes first{% endif %}</dd></div>
    </dl>
    <p><a href="{{ recipe.url }}" class="card-link">View recipe</a></p>
  </article>
{% endfor %}
</div>

<p id="recipe-no-results" class="recipe-no-results" hidden>No recipes match that search. Try a room, task, or broader category.</p>

## What every recipe includes

<div class="placement-grid">

<div class="placement-card">
<h3>Plain-English logic</h3>
<p>The trigger, conditions, action, delay, stop condition, and manual override are stated before setup details.</p>
</div>

<div class="placement-card">
<h3>Honest hardware guidance</h3>
<p>Named products are limited to devices I have used. Missing recommendations remain clearly identified.</p>
</div>

<div class="placement-card">
<h3>Failure behavior</h3>
<p>Recipes account for stale sensors, unavailable devices, hub restarts, internet loss, guests, and manual changes where they matter.</p>
</div>

</div>

## Good first recipes

- [Turn on lights when motion is detected](/automation/lighting/lights-on-motion.html)
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)
- [Get low-battery alerts](/automation/notifications/low-battery-alerts.html)

Build one, observe it for a week, and add complexity only when normal household use exposes a specific failure.

<div class="page-navigation">
  <a href="/">Back to home</a>
  <a href="/getting-started/index.html">Getting started</a>
</div>
