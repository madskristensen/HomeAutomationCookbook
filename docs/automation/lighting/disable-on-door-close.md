---
layout: automation
title: Turn a closet light off after the door closes
description: A platform-neutral follow-up to door-triggered lighting that turns off only the light the automation turned on and cancels when the door reopens.
keywords: closet light door close, pantry light automation, contact sensor light off, automatic closet lighting, door sensor lighting
last_modified_at: 2026-08-30
faqs:
  - question: Should a closet light turn off the instant the door closes?
    answer: Use a short delay so a bouncing contact or quick return does not cycle the light. Cancel the pending off action if the door opens again.
  - question: Why track whether the automation turned the light on?
    answer: Ownership prevents the close event from undoing a person's manual choice, such as leaving the light on while cleaning or changing a shelf.
  - question: Can a closed door prove that a bathroom is occupied?
    answer: No. Door position alone cannot reliably prove occupancy. Use motion with a longer delay or mmWave presence sensing for bathrooms and quiet workspaces.
---

# Turn a closet light off after the door closes

Pair a reliable door-open light with a delayed door-close rule that turns off only the light that automation started.

**Best for:** A small closet, cupboard, or shallow pantry with one access door where nobody can remain safely inside after it closes.

**Not for:** Walk-in closets, bathrooms, bedrooms, offices, multi-door rooms, or any space where a closed door does not prove the lit task has ended.

## Why this exists

A small cupboard or closet light should turn itself off after the door closes without undoing a manual choice or cycling when the contact bounces. That requires ownership and cancellation, while a walk-in space needs occupancy logic instead of relying on the door alone.

This recipe is deliberately narrow. Door position is a good task signal for a small cupboard, but it is not a general occupancy sensor.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect the door closing**

[SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL). Align the magnet so closed reports remain stable.

</div>
<div class="product-item" markdown="1">

**Dim a fixed light**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W). Verify hub compatibility. Keep the physical paddle usable.

</div>
<div class="product-item" markdown="1">

**Switch a fixed light on or off**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6). Keep the physical paddle usable.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The contact sensor changes from open to closed.
- **Conditions:** The paired door-open recipe turned this light on, the sensor remains available, and no manual light change has canceled automation ownership.
- **Action:** Start a short off delay, then turn off the light and clear the ownership marker.
- **Wait / timeout:** Cancel the pending off action if the door opens again before the delay ends.
- **Stop condition:** The light turns off, the door reopens, or a person changes the light manually.
- **Manual override:** A wall-switch change clears automation ownership and wins immediately.

<div class="automation-example">IF the closet door closes
AND the paired door-open recipe owns the light
THEN wait a short delay

IF the door is still closed
AND automation still owns the light
THEN turn the light off
AND clear automation ownership

IF the door reopens or the wall switch changes
THEN cancel the pending off action</div>

## Setup notes

1. Complete and test the [door-open lighting recipe](/automation/lighting/toggle-lights-door.html) first.
2. When that recipe turns on the light, set a marker saying it owns the current on state.
3. Clear ownership whenever the wall switch or light changes outside the paired recipes.
4. Trigger this recipe only on a real open-to-closed transition.
5. Add a short delay and recheck both door state and ownership when it ends.
6. Cancel the pending action immediately when the door reopens.
7. Test contact bounce by closing the door gently, firmly, and incompletely.
8. Do not copy this rule to a room where someone can remain behind the closed door.

## Choose the off behavior by space

| Space | Safer off signal |
|---|---|
| Small cupboard or shallow closet | Door closed after a short delay |
| Pantry someone can step into | Door closed plus verified vacancy, or a longer occupancy timeout |
| Walk-in closet | Motion or presence inactivity with a manual switch fallback |
| Bathroom or quiet workspace | mmWave presence or a conservative motion timeout |
| Room with multiple doors | Occupancy sensing, not one door's position |

The more a space behaves like a room, the less useful the door is as an off signal.

## Advanced features

### Add a door-left-open reminder

If the automation owns the light and the door remains open much longer than a normal visit, send one quiet reminder. Do not turn the light off while someone may still be using the space.

### Handle unavailable sensors explicitly

An unavailable contact is unknown, not closed. Leave the light alone, clear any pending off timer, and show a maintenance warning.

### Use a maximum ownership timeout

Clear a stale ownership marker after a long, household-tested limit without forcing the light off. This prevents an old marker from affecting a later manual session.

## Failure modes

- **The light turns off after the door reopens:** Make the close timer cancelable and recheck the door after the delay.
- **A manual choice is reversed:** Clear automation ownership on every external light or wall-switch change.
- **The light cycles when the door closes:** Increase the delay and realign the contact sensor to prevent bounce.
- **The light stays on after a normal close:** Confirm the paired open recipe set ownership and that the sensor reported a stable close.
- **The sensor becomes unavailable:** Treat the state as unknown and leave manual control in charge.
- **Someone can remain inside:** Remove this recipe and use motion or presence sensing with a conservative timeout.
- **The hub or internet is down:** The physical wall switch remains the fallback. Verify local behavior before depending on it.

## Done when

- [ ] Ten open-and-close tests report every transition correctly.
- [ ] Closing the door turns off a light started by the paired automation.
- [ ] Reopening during the delay cancels the pending off action.
- [ ] A manual wall-switch change is never reversed.
- [ ] An unavailable sensor does not count as closed.
- [ ] A stale ownership marker cannot affect a later manual session.
- [ ] Someone who did not build the recipe can use the space normally.

## FAQ

### Should a closet light turn off the instant the door closes?

Use a short delay so a bouncing contact or quick return does not cycle the light. Cancel the pending off action if the door opens again.

### Why track whether the automation turned the light on?

Ownership prevents the close event from undoing a person's manual choice, such as leaving the light on while cleaning or changing a shelf.

### Can a closed door prove that a bathroom is occupied?

No. Door position alone cannot reliably prove occupancy. Use motion with a longer delay or mmWave presence sensing for bathrooms and quiet workspaces.

## Related recipes

- [Turn lights on when a door opens](/automation/lighting/toggle-lights-door.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">Back to lighting automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
