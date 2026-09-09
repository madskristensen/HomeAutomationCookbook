---
layout: automation
title: Turn on away lights to look occupied
description: A platform-neutral recipe that turns on a few strategic lights while away to make the home look occupied, without an unnatural all-lights-on pattern.
keywords: away lights, security lighting, home occupied simulation, break-in deterrent, smart home security
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: Will turning on a couple of lights actually deter a break-in?
    answer: There is no certainty either way, but a home that looks occupied is generally considered less appealing to an opportunistic intruder than one that clearly looks empty. This is one layer among several, not a guarantee.
  - question: Should every light in the house turn on?
    answer: No. Turning on every light at once tends to look unnatural. A couple of rooms that a person home alone would realistically use, such as a living room and one bedroom, reads as more convincing.
  - question: What if I forget to turn Away mode off when I get home?
    answer: Arriving home and disarming Away mode, however the platform signals that, should turn the lights back to their normal schedule. It is worth confirming this transition works before relying on it.
---

# Turn on away lights to look occupied

Turn on a couple of strategic lights while away, on a schedule that mimics normal evening use, so the home does not look obviously empty.

**Best for:** A household that already uses an away or vacation mode and wants a lighting pattern that looks natural from the street.

**Not for:** A home with no away mode concept at all; this recipe assumes the platform can distinguish "away" from "home" as a starting condition.

## Why this exists

A home with every light off every evening, night after night, is a visible pattern to anyone paying attention. Turning on a couple of lights that a person home alone would realistically use, on a normal evening schedule, is a simple layer that avoids an obviously empty appearance.

## Logic

<div class="automation-example">IF the home enters Away mode
AND the time is between sunset and 11:00 PM
THEN turn on the away lights scene

IF the time reaches 11:00 PM
AND the home is still in Away mode
THEN turn off the away lights scene</div>

- **Trigger:** The home enters Away mode, or the time reaches sunset while already in Away mode.
- **Conditions:** The home is currently in Away mode, and the time is between sunset and a set cutoff, such as 11:00 PM.
- **Action:** Turn on the selected away lights, ideally as a single scene rather than individually.
- **Wait / timeout:** The lights stay on until the cutoff time.
- **Stop condition:** The cutoff time is reached, or the home leaves Away mode because someone returns.
- **Manual override:** Every light switch keeps its normal physical and app-based control, regardless of Away mode.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Switch a fixed light on or off**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Good for a wired fixture the household wants to keep as a simple on/off.

</div>
<div class="product-item" markdown="1">

**Dim a fixed light**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20). Useful if a more natural, less bright evening look is preferred over a full-brightness on/off switch.

</div>
<div class="product-item" markdown="1">

**Control a plug-in light or appliance**

[Minoston 800 Series Z-Wave plug](https://www.amazon.com/dp/B0CQX4JFV2/ref=nosim?tag=madsk0f-20). Works for a lamp plugged into an outlet rather than a wired fixture.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Choose two or three lights that a person home alone would realistically use, such as a living room lamp and one bedroom light; avoid lighting every room.
2. Group the selected lights into a single scene if the platform supports it, so they can be turned on and off together.
3. Set the trigger to turn the scene on at sunset only while Away mode is active, and off again at a fixed cutoff time such as 11:00 PM.
4. Confirm returning home and leaving Away mode correctly stops the pattern and returns lights to their normal schedule.
5. Test the full cycle once with Away mode manually enabled, rather than waiting for an actual absence to find a problem.

## Advanced features

### Staggered timing

Turn on the living room light at sunset and the bedroom light 15 to 20 minutes later, rather than all at once, to look closer to normal evening activity.

### Room rotation

Alternate which rooms light up on different nights during an extended absence, so the pattern does not repeat identically every evening.

## Failure modes

- **Lights turn on during the day:** Confirm the sunset condition and the platform's time zone setting are both correct; add an explicit time window if the sunset trigger alone is unreliable.
- **Lights do not turn off at the cutoff:** Check that Away mode is still active at that time and that no other automation is overriding the schedule.
- **Pattern looks the same every night:** Add staggered timing or room rotation so it is less obviously automated.
- **Lights stay on after returning home:** Confirm arriving home correctly disables Away mode, since this automation depends on that condition to stop.

## FAQ

### Will turning on a couple of lights actually deter a break-in?

There is no certainty either way, but a home that looks occupied is generally considered less appealing to an opportunistic intruder than one that clearly looks empty. This is one layer among several, not a guarantee.

### Should every light in the house turn on?

No. Turning on every light at once tends to look unnatural. A couple of rooms that a person home alone would realistically use, such as a living room and one bedroom, reads as more convincing.

### What if I forget to turn Away mode off when I get home?

Arriving home and disarming Away mode, however the platform signals that, should turn the lights back to their normal schedule. It is worth confirming this transition works before relying on it.

## Related recipes

- [Set up away mode](/automation/daily-routines/away-mode.html)
- [Set up fire safety response](/automation/security/fire-safety.html)
- [Set up outdoor night lights](/automation/lighting/outdoor-night-lights.html)

<div class="page-navigation">
  <a href="/automation/security/index.html">Back to security</a>
  <a href="/automation/index.html">View all automations</a>
</div>