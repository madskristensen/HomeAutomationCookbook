---
layout: default
title: Climate automations
description: Practical recipes for HVAC, humidity, air quality, blinds, and cold-room monitoring with safe limits and manual control.
permalink: /automation/climate/index.html
canonical_url: https://www.homeautomationcookbook.com/automation/climate/index.html
---

# Climate automations

Climate automation works best when it quietly picks up the routine adjustments you already mean to make, like starting the bathroom fan or closing the blinds, without hiding what the heating, cooling, or ventilation system is actually doing or taking away the manual controls you already trust.

<div class="category-intro" markdown="1">

## Start with safe limits

- Keep the thermostat, fan switch, and blind controls usable by hand.
- Treat missing sensor data as unknown, not as permission to change equipment.
- Use temperature limits that protect people, pets, plumbing, and the building.
- Use only equipment approved for the load and type of control.
- Make automatic changes visible and easy to reverse.

[Set safe thermostat auto-away limits](/automation/climate/safe-thermostat-away.html) before allowing Away or Vacation mode to change the temperature.

</div>

## Choose a recipe

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Use safe thermostat auto-away limits

Apply only a modest setback while protecting pets, plumbing, manual holds, and uncertain presence.

[View guide](/automation/climate/safe-thermostat-away.html)

</div>

<div class="automation-card" markdown="1">

### Pause HVAC when a window stays open

Pause heating or cooling after a delay, then resume only when every monitored opening is closed.

[View automation](/automation/climate/thermostat-windows-open.html)

</div>

<div class="automation-card" markdown="1">

### Turn on the bathroom fan for a shower

Use a measured humidity rise or the bathroom light as the trigger, then stop after humidity settles, so nobody has to remember to switch the fan on or off.

[View automation](/automation/climate/fan-shower.html)

</div>

<div class="automation-card" markdown="1">

### Open and close blinds with the sun

Use sunrise and sunset with a fixed privacy fallback and physical controls that still work.

[View automation](/automation/climate/blinds-sunset-sunrise.html)

</div>

<div class="automation-card" markdown="1">

### Run an air purifier when air quality drops

Respond to a sustained sensor reading without cycling the purifier on every brief change, so nobody has to watch an air quality app themselves.

[View automation](/automation/climate/air-quality-purifier.html)

</div>

<div class="automation-card" markdown="1">

### Monitor a cold room safely

Alert when a room leaves its safe range without putting a portable heater on a general-purpose smart plug.

[View automation](/automation/climate/room-heater-maintain-temp.html)

</div>

<div class="automation-card" markdown="1">

### Suggest when to open or close windows

Compare indoor and outdoor conditions, then notify the household instead of moving windows automatically.

[View automation](/automation/climate/window-notifications.html)

</div>

</div>

## What to verify

Test each recipe through sensor loss, a hub restart, manual changes, and the edge of its temperature or humidity range. An unavailable sensor should produce a visible unknown state. It should not look like a successful reading.

<div class="page-navigation">
  <a href="/automation/index.html">Back to all automations</a>
  <a href="/automation/entertainment/index.html">Next: entertainment</a>
</div>
