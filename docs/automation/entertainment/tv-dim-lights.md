---
layout: automation
title: Dim lights when the TV turns on
description: A platform-neutral recipe that dims the living room lights when the TV turns on, using either power monitoring or a smart TV signal, and restores them afterward.
keywords: TV lighting automation, dim lights TV, theater mode automation, movie lighting, automatic TV lights
last_modified_at: 2026-09-09
compact: true
faqs:
  - question: Should I use power monitoring or a smart TV signal as the trigger?
    answer: A compatible power-monitoring plug works with many TVs, but can be fooled by a menu screen drawing similar power to active playback. A smart TV or streaming device signal is more accurate if the platform supports it reliably.
  - question: Why does the TV menu sometimes dim the lights by mistake?
    answer: A power-based trigger cannot always tell a menu screen from active playback, since both can draw similar wattage. Raising the power threshold or adding a short delay before dimming reduces this.
  - question: Will the lights go back to their previous brightness after the TV turns off?
    answer: Yes, if the previous brightness is saved before dimming and restored once the TV has been off for a couple of minutes, rather than always returning to one fixed level.
---

# Dim lights when the TV turns on

Automatically dim the living room lights when the TV turns on, and restore them to their previous level once the TV turns off.

**Best for:** A living room with dimmable smart lights and either a smart plug with power monitoring or a TV/streaming device that reports its power or playback state reliably.

**Not for:** A room where lights need to stay bright regardless of what is on screen, or a TV whose power state cannot be read reliably by the platform.

## Why this exists

Dimming the lights by hand every time a movie starts is a small chore that is easy to skip, and it means the room does not settle into a consistent viewing setup. Automating it removes the extra step, and restoring the previous brightness afterward avoids leaving the room dim once viewing is over.

## Logic

<div class="automation-example">IF TV power draw rises above the "on" threshold
OR the TV/streaming device reports it is playing
THEN save the current light brightness
AND dim the living room lights to the preset level

IF TV power draw has stayed below the "off" threshold for a couple of minutes
OR the TV has reported "off" for the same period
THEN restore the living room lights to the saved brightness</div>

- **Trigger:** Power draw on the TV's smart plug rises above a threshold, or the TV/streaming device reports it is playing.
- **Conditions:** The current time is after a chosen hour, such as sunset, if daytime dimming is not wanted.
- **Action:** Save the current light brightness, then dim the living room lights to a low level.
- **Wait / timeout:** Keep the lights dimmed until the stop condition is met.
- **Stop condition:** Power draw drops below a lower threshold, or the TV reports it has stopped, for a couple of minutes.
- **Manual override:** The physical light switch or app always works to change brightness directly.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect the TV turning on**

Zooz ZEN15 Power Switch. I use the ZEN15's power readings to distinguish standby from the TV being on. Measure the TV's actual draw before setting thresholds.

</div>
<div class="product-item" markdown="1">

**Dim the living room lights**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20). Requires a dimmable fixture and a switch rated for the load.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. If using power monitoring, test the TV's actual wattage in both standby and active playback so the "on" and "off" thresholds are set apart from real values, not guessed.
2. Add a short delay, such as thirty seconds, before dimming so a menu screen briefly drawing similar power does not trigger it.
3. If using a smart TV or streaming device signal instead, confirm the platform reads its state reliably before relying on it daily.
4. Save the current brightness before dimming so the lights can return to where they were, rather than always resetting to one fixed level.
5. Require the "off" condition to hold for a couple of minutes so a brief pause does not restore full brightness mid-movie.

## Advanced features

### Daytime versus evening dimming

Use a lighter dim, such as 40 percent, during the day for glare control, and a deeper dim, such as 10 percent, in the evening once natural light is gone.

### Skip dimming during activity

Add a condition that skips dimming if recent motion has been detected in the room, so lights stay normal while people are still moving around rather than settling in to watch.

## Failure modes

- **Lights dim when only the menu is open:** Raise the power threshold or add a longer delay before dimming; consider switching to a TV-state trigger if available.
- **Lights do not restore when the TV turns off:** Confirm the "off" threshold or state check is set below actual standby power, and that the previous brightness was saved before dimming.
- **Lights dim during the day unexpectedly:** Add or correct a time-of-day condition if daytime dimming is not wanted.
- **TV state reported inaccurately:** Check the TV or streaming device's network connection and platform integration; power monitoring can serve as a fallback trigger.

## FAQ

### Should I use power monitoring or a smart TV signal as the trigger?

A compatible power-monitoring plug works with many TVs, but can be fooled by a menu screen drawing similar power to active playback. A smart TV or streaming device signal is more accurate if the platform supports it reliably.

### Why does the TV menu sometimes dim the lights by mistake?

A power-based trigger cannot always tell a menu screen from active playback, since both can draw similar wattage. Raising the power threshold or adding a short delay before dimming reduces this.

### Will the lights go back to their previous brightness after the TV turns off?

Yes, if the previous brightness is saved before dimming and restored once the TV has been off for a couple of minutes, rather than always returning to one fixed level.

## Related recipes

- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)
- [Start a wind-down bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Set every speaker to the right volume with one command](/automation/entertainment/speaker-volume-presets.html)

<div class="page-navigation">
  <a href="/automation/entertainment/index.html">Back to entertainment</a>
  <a href="/automation/index.html">View all automations</a>
</div>