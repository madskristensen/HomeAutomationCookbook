---
layout: automation
redirect_from:
  - /automation/motion/bathroom-night-light.html
date: 2025-11-28
title: Bathroom night-light automation
description: A local-first bathroom night-light recipe that uses motion, low brightness, and a reliable wall-switch fallback.
keywords: bathroom night light, nighttime motion lighting, low brightness automation, smart bathroom lighting, motion sensor dimming, night mode lighting
last_modified_at: 2026-09-14
image: /assets/img/social/recipes/lighting/bathroom-night-light.png
compact: true
faqs:
  - question: What brightness should a bathroom night light use?
    answer: Start at 10 percent, then test it in the dark. Raise it only enough for safe navigation.
  - question: Why does a bathroom motion light turn off during a shower?
    answer: A PIR sensor can miss someone who is still or hidden by steam and a shower curtain. Use a longer timeout or a presence sensor.
  - question: What happens if the hub or internet connection goes down?
    answer: The physical wall switch still works independent of the automation, so the bathroom light can always be turned on manually.
---

# Turn on a dim bathroom light at night

<figure class="content-hero">
  <img src="/assets/img/social/recipes/lighting/bathroom-night-light.svg" alt="" width="1200" height="630">
</figure>

Walk in half asleep, get enough light to see, and do not wake the house. If it fails, the wall switch still works.

**Best for:** Bathrooms with a dimmable light and a sensor placed near the entry.

**Not for:** A bathroom where a short PIR timeout would turn lights off during a shower. A PIR sees movement, not a still person. Start with a longer timeout or use the [PIR vs mmWave presence article](/articles/pir-vs-mmwave-presence.html) to add occupancy sensing.

## Why this exists

Bright bathroom light at 2am is miserable. This recipe uses only enough light to navigate safely, then hands the shutoff to the paired motion-lighting recipe. It should work without explaining a special night mode to a guest.

💡 For sensor positioning and coverage testing, see [how to place motion sensors for reliable automations](/articles/motion-sensor-placement.html).

## Logic

<div class="automation-example">IF bathroom motion is detected during Night mode or the night window
THEN turn on the light at 10%</div>

- **Trigger:** Bathroom or entry motion is detected.
- **Conditions:** Night mode is active or it is within your chosen night window, and optionally the room is dark enough.
- **Action:** Turn on the bathroom light at 10 percent. Set a warm color temperature only if the light supports it.
- **Wait / timeout:** The paired [turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html) recipe owns the timeout. Start at 10 minutes for a shower bathroom.
- **Stop condition:** New motion cancels the shutoff. A manual wall-switch change wins.
- **Manual override:** The wall switch still wins.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect bathroom motion, humidity, temperature, and light**

[Aeotec TriSensor 8](https://www.amazon.com/dp/B0D47WR1S2/ref=nosim?tag=madsk0f-20). Use the extra readings where they solve a real bathroom problem.

</div>
<div class="product-item" markdown="1">

**Dim a fixed light**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20). Verify hub compatibility. The physical paddle must remain usable.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

Choose one understandable signal for nighttime behavior. A fixed night window is simplest. If the household already uses a reliable Night mode, the lighting rule can check that instead.

Do not infer Night mode only because someone entered a bedroom. Different schedules, illness, guests, and brief trips make that signal unreliable. If Night mode is not already dependable, use a fixed time window. See [daily routine automations](/automation/daily-routines/index.html) for deliberate night-mode patterns.

## Platform notes

The platform must combine a motion trigger with a dependable night condition and set a specific dimming level. Keep the physical wall switch available, and let the separate no-motion rule own shutoff timing. See the [platform guides](/platforms/index.html) for broader fit and maintenance tradeoffs.

### Amazon Alexa

Build this as an Alexa routine only when the sensor appears as a motion trigger under **When**, the schedule can limit the routine to nighttime, and the light exposes brightness under **Alexa Will**. Amazon documents the underlying [motion-sensor state model](https://developer.amazon.com/docs/alexaplus/device-apis/alexa-motionsensor.html), but trigger and dimming choices still vary by device and region. Test the routine in the dark and keep shutoff in a separate routine.

### SmartThings

Create an automatic SmartThings Routine with motion and a nighttime period as IF conditions, then set the dimmer level in the THEN action. Use location mode or illuminance instead of a fixed time only when that signal is already dependable. The available conditions and actions come from the device's exposed [SmartThings capabilities](https://developer.smartthings.com/docs/devices/capabilities).

### Hubitat

Use Hubitat [Room Lighting](https://docs2.hubitat.com/en/apps/room-lighting) to activate the bathroom light from motion and apply a low level by mode or time period. Keep the delayed shutoff and physical-change behavior explicit so shower activity and a wall-switch choice are not overridden.

### Home Assistant

Home Assistant is a technical fit for combining motion, time or house state, and a dimming action, but I have not personally run it. Verify the current sensor and light integrations, then preserve the same low-light default, separate shutoff, and physical-control requirements.

## Advanced features

Keep one nighttime level until the recipe is dependable. If the household needs different levels before bed and during deep night, add one extra time period rather than a complicated schedule. A warmer color temperature can feel less disruptive, but safe footing matters more than a particular number or color.

Use the separate [turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html) recipe for shutoff behavior. Add another sensor or presence sensing only when normal shower use proves that the entry sensor is not enough.

## Failure modes

- **The light is too bright:** Start at 10 percent, then test in a dark bathroom. Increase only enough for safe footing.
- **It turns off during a shower:** A PIR can miss a still person through steam or a shower curtain. Use the paired off recipe with a 10-minute starting timeout, or follow the [PIR vs mmWave presence article](/articles/pir-vs-mmwave-presence.html) to keep detecting a person after motion stops.
- **The sensor sees a hallway instead:** Aim and test the sensor so passing traffic does not light the bathroom unnecessarily.
- **A guest uses the wall switch:** Treat it as the final answer. The next automation must not immediately undo that choice.
- **The hub or internet is down:** The wall switch remains the fallback. Confirm that any relied-on Level 2 path is local.

## FAQ

### What brightness should a bathroom night light use?

Start at 10 percent, then test it in the dark. Raise it only enough for safe navigation.

### Why does a bathroom motion light turn off during a shower?

A PIR sensor can miss someone who is still or hidden by steam and a shower curtain. Use a longer timeout or a presence sensor.

### What happens if the hub or internet connection goes down?

The physical wall switch still works independent of the automation, so the bathroom light can always be turned on manually.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">← Back to lighting automations</a>
  <a href="/automation/index.html">View all automations →</a>
</div>
