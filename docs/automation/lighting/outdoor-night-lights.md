---
layout: automation
date: 2025-11-29
title: Automate outdoor lights at dusk
description: A platform-neutral outdoor-lighting recipe that follows sunset, avoids unnecessary overnight runtime, and keeps physical control available.
keywords: outdoor lights automation, sunset lights, dusk lighting, exterior lighting, holiday lights, smart outdoor lights
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/lighting/outdoor-night-lights.png
compact: true
faqs:
  - question: Should outdoor lights use a sunset schedule or a light sensor?
    answer: Start with sunset because it is simple and predictable. Add a light sensor only when clouds, shade, or seasonal light make the schedule consistently wrong.
  - question: Should outdoor lights stay on all night?
    answer: Keep safety lighting on only where it is useful. Decorative and holiday lights can usually turn off at a fixed bedtime.
  - question: What happens when the hub or internet is down?
    answer: A local hub may continue running the schedule, but the outdoor switch or plug must remain easy to control manually.
---

# Turn outdoor lights on at dusk

<figure class="content-hero">
  <img src="/assets/img/social/recipes/lighting/outdoor-night-lights.svg" alt="" width="1200" height="630">
</figure>

At dusk, the useful outdoor lights come on. Decorative lights turn off at bedtime, and the physical switch or plug still works when automation does not.

**Best for:** Porch, driveway, path, landscape, and seasonal lights that should follow darkness instead of a fixed clock time.

**Not for:** A light that would shine into a neighbor's window, illuminate the sky, or stay on all night without a clear safety reason.

## Why this exists

A fixed clock schedule drifts away from daylight as the seasons change. A sunset trigger follows the useful part of the day without daily adjustment. Separate safety lighting from decorative lighting so each can turn off when its job is done.

## Logic

<div class="automation-example">IF sunset occurs AND the outdoor-lighting schedule is enabled
THEN turn on the selected outdoor lights
AT bedtime turn off decorative lights
AT sunrise turn off any remaining lights</div>

- **Trigger:** Sunset occurs, with an optional offset if the property becomes dark earlier or later.
- **Conditions:** The outdoor-lighting schedule is enabled. Seasonal lights also require their seasonal toggle to be on.
- **Action:** Turn on the selected outdoor lights.
- **Wait / timeout:** Turn decorative lights off at a household bedtime. Keep only genuinely useful safety lighting on longer.
- **Stop condition:** Sunrise or the chosen off time turns the lights off.
- **Manual override:** The wall switch or plug still wins.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Control outdoor plug-in lighting**

[Minoston Outdoor Smart Plug](https://www.amazon.com/dp/B07X52W1J8/ref=nosim?tag=madsk0f-20). Use only with an outdoor-rated fixture and receptacle.

</div>
<div class="product-item" markdown="1">

**Switch a fixed outdoor circuit**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Keep the physical paddle usable. Confirm the switch and installation suit the circuit.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Group lights by job: safety, path, decorative, and seasonal.
2. Start with sunset as the on trigger. Add an offset only after observing the property for several evenings.
3. Give decorative lights a fixed off time instead of leaving everything on until sunrise.
4. Add a sunrise off action as a failsafe, even when another rule should turn the lights off earlier.
5. Test the physical switch or plug after the automation is enabled.

## Advanced features

### Add a light sensor only when it solves a problem

Sunset is predictable and needs no outdoor sensor. A light sensor can help on heavily shaded properties or unusually dark cloudy days, but it also adds placement, threshold, and reliability concerns. Add one only after the sunset schedule has been tested.

### Use a dim baseline with temporary brightness

Where the hardware supports dimming, keep path lighting low and raise it temporarily when motion is detected. Return to the baseline rather than switching the entire property off after motion clears.

### Keep seasonal lights separate

Use a simple seasonal enable control. The normal outdoor-lighting schedule should still work when holiday lights are unplugged or disabled.

## Failure modes

- **Lights turn on too early or too late:** Verify the home's location and time zone, then adjust the sunset offset in small steps.
- **Lights remain on in daylight:** Add an explicit sunrise off action and check for another rule that turns them back on.
- **A cloudy day is too dark before sunset:** Add a carefully placed light sensor only if this happens often enough to matter.
- **The outdoor plug becomes unreachable:** Check the local mesh and move or add an appropriate repeater before relying on the schedule.
- **Lights bother neighbors:** Aim fixtures downward, reduce brightness, and shorten the schedule.
- **The hub or internet is down:** Use the physical control. Do not make a cloud-only path the only way to operate an exterior light.

## FAQ

### Should outdoor lights use a sunset schedule or a light sensor?

Start with sunset because it is simple and predictable. Add a light sensor only when clouds, shade, or seasonal light make the schedule consistently wrong.

### Should outdoor lights stay on all night?

Keep safety lighting on only where it is useful. Decorative and holiday lights can usually turn off at a fixed bedtime.

### What happens when the hub or internet is down?

A local hub may continue running the schedule, but the outdoor switch or plug must remain easy to control manually.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Away lighting](/automation/security/away-lights.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">Back to lighting automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
