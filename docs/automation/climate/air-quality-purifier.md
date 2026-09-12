---
layout: automation
title: Automate an indoor air purifier
description: A platform-neutral recipe that runs a plug-controlled air purifier when an air quality sensor reports a sustained drop, and stops nagging once the air clears.
keywords: air quality automation, air purifier control, AQI sensor automation, PM2.5 automation, indoor air quality
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/climate/air-quality-purifier.png
compact: true
faqs:
  - question: Why require a sustained reading instead of reacting to a single spike?
    answer: Cooking and brief odors cause short spikes that clear on their own. A sustained reading over several minutes better reflects an actual air quality problem worth running the purifier for.
  - question: What if there is no air quality sensor at all?
    answer: Send a notification suggesting ventilation instead of guessing. Do not run the purifier on a fixed schedule with no sensor to justify it.
  - question: Should the purifier ever run at maximum speed automatically?
    answer: Only when the sensor is available and reporting a clearly unhealthy reading. Treat a missing or unavailable reading as unknown, not as a reason to run at maximum.
---

# Run the air purifier when indoor air quality drops

<figure class="content-hero">
  <img src="/assets/img/social/recipes/climate/air-quality-purifier.svg" alt="" width="1200" height="630">
</figure>

Watch an air quality sensor for a sustained unhealthy reading, run the purifier, and turn it off again once the air has stayed clear for a while.

**Best for:** A room with both an air quality sensor and a purifier that can be switched or controlled remotely.

**Not for:** Homes without any air quality sensor, or treating this as a substitute for evacuating during a genuine hazard such as heavy smoke.

## Why this exists

Cooking, cleaning products, and pet activity all cause brief air quality dips that clear on their own. Reacting to every small spike leads to a purifier that runs constantly and an alert nobody trusts. Requiring a sustained reading, then confirming the air has cleared before stopping, keeps the automation both useful and quiet.

## Logic

<div class="automation-example">IF the air quality sensor reports unhealthy
AND the reading holds for several minutes
THEN turn on the purifier

IF the air quality sensor reports healthy
AND the purifier is currently on
AND the healthy reading holds for a similar confirmation period
THEN turn off the purifier</div>

- **Trigger:** The air quality sensor reports an unhealthy reading.
- **Conditions:** The sensor is available and the reading has held at an unhealthy level for several minutes.
- **Action:** Turn on the purifier, choosing a higher speed for a worse reading if the purifier supports it.
- **Wait / timeout:** Keep the purifier running until the reading returns to a healthy level and stays there for a similar confirmation period.
- **Stop condition:** Turn off the purifier once the air has stayed clear through the confirmation period.
- **Manual override:** The purifier's own power button or app control always works regardless of the automation.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Control a plug-in air purifier**

[Minoston 800 Series Z-Wave plug](https://www.amazon.com/dp/B0CQX4JFV2/ref=nosim?tag=madsk0f-20). Confirm the plug's current rating covers the purifier's startup draw, and keep the purifier's own physical switch usable.

</div>
<div class="product-item" markdown="1">

**Measure indoor air quality**

No personally verified recommendation yet. I have not verified a specific air quality or PM2.5 sensor. Any sensor used here should report a stable, current reading before it drives the purifier.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Place the sensor away from the kitchen, a litter box, or other constant local sources so it reflects the room's general air rather than one corner.
2. Record a few days of readings to see the sensor's normal range before choosing thresholds.
3. Require the unhealthy reading to hold for several minutes before starting the purifier, so a brief cooking spike does not trigger it.
4. Require a similar clear period before stopping, so the purifier does not cycle on and off around the threshold.
5. Confirm the purifier's own switch and app control still work after wiring it through a smart plug.
6. Test with a deliberate short-lived source, such as burnt toast, to confirm the automation ignores it.

## Advanced features

### Graduated speed by severity

Where the purifier supports more than one speed, use a lower speed for a moderate reading and reserve the highest speed for a clearly unhealthy one.

### Notify without a purifier

If no purifier is connected yet, send a notification suggesting ventilation or checking outdoor air quality before opening windows, instead of taking no action at all.

## Failure modes

- **Purifier runs almost constantly:** Move the sensor away from a nearby pollution source and confirm the purifier's filter is still effective.
- **Purifier never turns on:** Confirm the sensor is reporting current data and that the unhealthy threshold is realistic for the sensor's normal range.
- **Cooking triggers the purifier every time:** Lengthen the sustained-reading delay or raise the threshold slightly during cooking hours.
- **Purifier cycles on and off repeatedly:** Widen the gap between the on and off thresholds, or require a longer confirmation period.
- **Sensor goes unavailable:** Treat the missing reading as unknown and leave the purifier in its current state rather than assuming clean air.

## FAQ

### Why require a sustained reading instead of reacting to a single spike?

Cooking and brief odors cause short spikes that clear on their own. A sustained reading over several minutes better reflects an actual air quality problem worth running the purifier for.

### What if there is no air quality sensor at all?

Send a notification suggesting ventilation instead of guessing. Do not run the purifier on a fixed schedule with no sensor to justify it.

### Should the purifier ever run at maximum speed automatically?

Only when the sensor is available and reporting a clearly unhealthy reading. Treat a missing or unavailable reading as unknown, not as a reason to run at maximum.

## Related recipes

- [Get notified when to open or close windows](/automation/climate/window-notifications.html)
- [Pause heating or cooling when a window stays open](/automation/climate/thermostat-windows-open.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)

<div class="page-navigation">
  <a href="/automation/climate/index.html">Back to climate automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>