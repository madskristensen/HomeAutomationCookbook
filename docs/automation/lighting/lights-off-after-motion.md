---
layout: automation
redirect_from:
  - /automation/motion/lights-off-after-motion.html
date: 2025-11-28
title: Turn lights off after motion stops
description: A conservative motion-lighting off recipe that respects still occupants, manual wall-switch choices, and local-first control.
keywords: motion sensor lights off, automatic light shutoff, occupancy detection, smart lighting automation, turn off lights automatically
last_modified_at: 2026-09-14
image: /assets/img/social/recipes/lighting/lights-off-after-motion.png
compact: true
faqs:
  - question: How long should motion lights stay on?
    answer: Start longer than you think, then reduce the timeout only after the household has used the room normally for several days.
  - question: Why do bathroom motion lights turn off while someone is inside?
    answer: A PIR sensor can miss someone who is still or behind a shower curtain. Use a longer timeout, another sensor, or presence detection.
  - question: Can a wall switch override the automatic shutoff?
    answer: It should. Treat a manual change as an explicit choice and avoid turning the light back off immediately.
---

# Turn lights off after motion stops

<figure class="content-hero">
  <img src="/assets/img/social/recipes/lighting/lights-off-after-motion.svg" alt="" width="1200" height="630">
</figure>

Leave the room, lights off. Stay still, and they should not leave you in the dark. The wall switch still wins when someone wants a different answer.

**Best for:** Hallways, closets, laundry rooms, and other spaces with predictable short visits.

**Not for:** A bathroom with a short PIR timer, or a home office where someone sits still for long periods. A PIR detects movement, not a person sitting still. Start with a longer delay, or follow the [PIR vs mmWave presence article](/articles/pir-vs-mmwave-presence.html).

## Why this exists

The off half makes automatic lighting useful without making it hostile. It should wait long enough for real people, then turn the light off after the room is clear. It must not fight a guest who used the familiar wall switch.

💡 For reliable coverage and testing, see [how to place motion sensors for reliable automations](/articles/motion-sensor-placement.html).

## Logic

<div class="automation-example">IF the room has been clear for the timeout
AND no manual override is active
THEN turn off the light</div>

- **Trigger:** The room sensor reports no motion for the chosen timeout.
- **Conditions:** The light was turned on by this automation, no other room sensor is active, and no manual override is active.
- **Action:** Turn the light off.
- **Wait / timeout:** Start at 5 to 10 minutes for a bathroom or quiet room. Reduce only after normal household testing.
- **Stop condition:** New motion, another active sensor, or a manual wall-switch change cancels the shutoff.
- **Manual override:** The wall switch still wins.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect fast entry motion**

[Shelly BLU Motion ZB](https://www.amazon.com/dp/B0H4GD6GGK/ref=nosim?tag=madsk0f-20). A PIR needs a conservative timer for people who sit still.

</div>
<div class="product-item" markdown="1">

**Dim a fixed light**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20). Verify hub compatibility. Keep the physical paddle usable.

</div>
<div class="product-item" markdown="1">

**Switch a fixed light on or off**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Keep the physical paddle usable.

</div>
</div>

For a bathroom that needs humidity, temperature, and light readings too, use the [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY/ref=nosim?tag=madsk0f-20) instead. It is not my first choice when the fastest motion response is the job.

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

Start with a longer delay than you expect to need, then shorten it only after normal household use.

- **Quick access spaces:** One to two minutes can work for a closet or hallway.
- **Living spaces:** Start at three to five minutes.
- **Bathrooms and quiet spaces:** Start at 10 minutes, or use a contact sensor, another motion sensor, or [mmWave presence sensing](/articles/pir-vs-mmwave-presence.html) before reducing the delay.

Test every normal path through the room and leave the timeout unchanged for several days. Fix sensor blind spots before shortening it.

## Platform notes

The platform must distinguish motion from no motion, wait for a room-specific timeout, and cancel the pending shutoff when activity returns. Keep the physical switch available regardless of platform. See the [platform guides](/platforms/index.html) for broader fit and maintenance tradeoffs.

### Amazon Alexa

Use an Alexa routine only when the sensor offers a no-motion trigger with a suitable duration under **When** and the light appears as an action under **Alexa Will**. Available routine options vary by device and region even though Amazon defines the underlying [motion-sensor state model](https://developer.amazon.com/docs/alexaplus/device-apis/alexa-motionsensor.html). Confirm that new motion prevents an unwanted shutoff before relying on the routine.

### SmartThings

Create an automatic SmartThings Routine with no motion for the chosen duration as the IF condition and light off as the THEN action. Add switch-state, mode, or additional-sensor conditions only when those capabilities are exposed. SmartThings explains the [IF and THEN routine model](https://support.smartthings.com/hc/en-us/articles/360051931952-Routines-in-SmartThings); local execution still depends on every device feature and service used by the rule.

### Hubitat

Hubitat [Room Lighting](https://docs2.hubitat.com/en/apps/room-lighting) supports motion-based shutoff delays, conditions, and options for responding to physical changes. Start with one conservative inactivity timeout, then add other sensors or override behavior only after the basic off rule is dependable.

### Home Assistant

Home Assistant is a technical fit for delayed no-motion logic, but I have not personally run it. Adapt the same timeout, cancellation, and manual-override requirements only after verifying the current automation behavior for the exact sensor and light integrations.

## Advanced features

In a larger room, require every relevant sensor to remain clear before turning the light off. Add an activity condition, such as a television or computer being in use, only when it reliably represents occupancy. Different day and night timeouts are useful only when one conservative timeout cannot serve both patterns.

## Failure modes

- **The light turns off while someone is still:** Increase the timeout before changing anything else. A PIR does not see a person working quietly, reading, showering, or standing behind a towel. For those rooms, follow the [PIR vs mmWave presence article](/articles/pir-vs-mmwave-presence.html).
- **A guest uses the wall switch:** Treat that as an override. Do not let the next sensor event immediately undo it.
- **The sensor sees motion outside the room:** Reposition it or narrow its view before shortening the timeout.
- **The hub reboots or the internet is down:** The wall switch remains the fallback. A local automation may resume after the hub is ready, but do not rely on it for Level 1 control.
- **The room is in use at night:** Use a longer timeout for quiet nighttime use, especially in bathrooms.

## FAQ

### How long should motion lights stay on?

Start longer than you think, then reduce the timeout only after the household has used the room normally for several days.

### Why do bathroom motion lights turn off while someone is inside?

A PIR sensor can miss someone who is still or behind a shower curtain. Use a longer timeout, another sensor, or presence detection.

### Can a wall switch override the automatic shutoff?

It should. Treat a manual change as an explicit choice and avoid turning the light back off immediately.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Bathroom night light](/automation/lighting/bathroom-night-light.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">← Back to lighting automations</a>
  <a href="/automation/index.html">View all automations →</a>
</div>
