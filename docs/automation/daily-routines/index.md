---
layout: default
title: Daily routine automations
description: Take repeated steps out of mornings, bedtimes, departures, and arrivals while keeping each transition visible and easy to override.
permalink: /automation/daily-routines/index.html
canonical_url: https://www.homeautomationcookbook.com/automation/daily-routines/index.html
keywords: daily routine automation, morning routine, bedtime automation, away mode, home arrival, presence automation, smart home routines
---

# Daily routines

Daily routine automations quietly support the schedule your household already has: leaving, coming home, waking up, and winding down. Done well, they take the repeatable steps off your plate while keeping every transition visible and easy to override.

<div class="category-intro" markdown="1">

## Why automate daily routines?

**Consistent experience** - The same understandable start to each morning

**Less waste** - Away mode can reduce unnecessary lighting and climate runtime

**Safer transitions** - Security actions remain separate until the household verifies them

**Visible transitions** - The household can see when Home, Away, or Night changes

**Reduced mental load** - Fewer repeated checks

**Family coordination** - Routines work for everyone, not just the person who built them

</div>

## Essential automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Away mode when everyone leaves

Automatically activate Away Mode when the last person leaves. Includes energy savings, security activation, and verification strategies.

<span class="card-meta">**Best for:** Reversible lighting and climate changes after the home is confidently empty</span>

<p><a href="/automation/daily-routines/away-mode.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Quiet good-morning routine

Use an intentional signal to leave Night mode, light one person's route, and leave sleeping household members undisturbed.

<span class="card-meta">**Best for:** Different schedules, children, and guests</span>

<p><a href="/automation/daily-routines/morning-routine.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Family-safe bedtime routine

Offer a reversible wind-down, then use an intentional good-night action that preserves occupied rooms, path lighting, and urgent alerts.

<span class="card-meta">**Best for:** Different bedtimes, guests, and late arrivals</span>

<p><a href="/automation/daily-routines/bedtime-routine.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Prepare the house on arrival

Restore Home mode, light the entry when needed, and resume approved comfort settings without unlocking a door from phone location alone.

<span class="card-meta">**Best for:** Safe entry lighting and comfort recovery</span>

<p><a href="/automation/daily-routines/unlock-door-arrival.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Predictable guest mode

Keep physical controls and useful lighting normal, prevent false Away mode, and quiet only non-urgent personal automation.

<span class="card-meta">**Best for:** Overnight visitors, house sitters, babysitters, and gatherings</span>

<p><a href="/automation/daily-routines/guest-mode.html" class="card-link">View automation</a></p>

</div>

</div>

---

## Home modes

<div class="use-case-grid">

<div class="use-case-card">
<h4>Home mode</h4>
<ul>
<li>Normal lighting automation</li>
<li>Comfortable temperature</li>
<li>Motion sensors active</li>
<li>Entertainment available</li>
</ul>
</div>

<div class="use-case-card">
<h4>Away mode</h4>
<ul>
<li>Lights off (or security pattern)</li>
<li>Eco temperature settings</li>
<li>Security system armed</li>
<li>Cameras active</li>
</ul>
</div>

<div class="use-case-card">
<h4>Night mode</h4>
<ul>
<li>Low-brightness lighting only</li>
<li>Lower temperature</li>
<li>Minimal notifications</li>
<li>Motion sensors dimmed</li>
</ul>
</div>

<div class="use-case-card">
<h4>Custom modes</h4>
<ul>
<li><strong>Guest:</strong> Modified automation for visitors</li>
<li><strong>Vacation:</strong> Extended away with enhanced security</li>
<li><strong>Party:</strong> Special lighting and music</li>
<li><strong>Work from Home:</strong> Office-optimized settings</li>
</ul>
</div>

</div>

---

## Best practices

<div class="placement-grid">

<div class="placement-card">
<h3>Start conservative</h3>
<ul>
<li>Longer delays (15 min before away mode)</li>
<li>Multiple verification methods</li>
<li>Manual override always available</li>
<li>A home area large enough to avoid location flapping</li>
</ul>
</div>

<div class="placement-card">
<h3>Notification strategy</h3>
<ul>
<li><strong>Always notify:</strong> Away mode activation</li>
<li><strong>Always notify:</strong> Security state changes</li>
<li><strong>Optional:</strong> Home mode restored on arrival</li>
</ul>
</div>

<div class="placement-card">
<h3>Fail-safe design</h3>
<ul>
<li>When uncertain, don't activate away mode</li>
<li>Do not unlock doors from phone location alone</li>
<li>Better safe than automated</li>
<li>Physical controls always work</li>
</ul>
</div>

</div>

---

## Failure modes

<div class="troubleshooting-grid">

<div class="issue-card">
<div class="issue-header">
<h3>False away mode activation</h3>
</div>
<div class="issue-solutions">
<ul>
<li>Add motion sensor verification</li>
<li>Increase geofence radius</li>
<li>Add 10-15 minute delay</li>
<li>Check for TV/device activity</li>
</ul>
</div>
</div>

<div class="issue-card">
<div class="issue-header">
<h3>Delayed presence detection</h3>
</div>
<div class="issue-solutions">
<ul>
<li>Disable battery optimization for app</li>
<li>Enable "Always" location permission</li>
<li>Use local processing</li>
<li>Add WiFi presence backup</li>
</ul>
</div>
</div>

<div class="issue-card">
<div class="issue-header">
<h3>Kids without phones</h3>
</div>
<div class="issue-solutions">
<ul>
<li>Time-based overrides (school hours)</li>
<li>Extended motion detection periods</li>
<li>Manual "Kids Home" toggle</li>
<li>Door sensor verification</li>
</ul>
</div>
</div>

</div>

<div class="page-navigation">
  <a href="/automation/">← Back to All Automations</a>
  <a href="/automation/climate/index.html">Next: climate and comfort</a>
</div>
