---
layout: automation
title: Set up gradual wake-up lighting
description: A platform-neutral recipe that gradually brightens a bedroom light before a set wake time, simulating a sunrise instead of a jarring alarm.
keywords: wake up lights, sunrise alarm, gradual lighting, morning light automation, gentle wake up
last_modified_at: 2026-08-30
faqs:
  - question: How long should the wake-up transition last?
    answer: Fifteen to thirty minutes is a reasonable starting range. A longer transition, up to 45 or 60 minutes, feels more gradual for deep sleepers, but takes more advance planning around the actual wake time.
  - question: What if my bulb does not dim low enough to start comfortably dim?
    answer: Some bulbs have a higher minimum brightness than others. If the starting level is already too bright, consider pointing the light away from the bed for the first part of the transition, or choosing a bulb with a lower documented minimum.
  - question: Can this wake one person without disturbing a partner?
    answer: Yes, using a single bedside lamp facing away from the partner's side of the bed, and keeping the maximum brightness lower, reduces the effect on someone who is not meant to wake up yet.
---

# Set up gradual wake-up lighting

Gradually brighten a bedroom light before a set wake time, so the room fills with light like a sunrise instead of relying on a jarring alarm alone.

**Best for:** A bedroom with a smart bulb or light strip that supports a wide dimming range and a fixed wake time worth planning around.

**Not for:** A room where the light cannot be dimmed low enough to start comfortably, or a household with an unpredictable wake schedule where the transition would rarely line up.

## Why this exists

Waking to a sudden bright light or a loud alarm in a dark room can feel abrupt. Gradually brightening a light over a set period gives a more natural transition into the morning and does not require anything beyond a light that is already in the room.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Gradually brighten the light | [TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W) | [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN) | Confirm the switch or bulb supports a low enough minimum brightness and a smooth transition, not just stepped levels. |

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** A fixed time before the desired wake time, such as 30 minutes prior.
- **Conditions:** The day matches the intended schedule, such as weekdays only, and any vacation or skip setting is off.
- **Action:** Set the light to a low starting brightness, then gradually raise it toward full brightness over the chosen duration.
- **Wait / timeout:** The transition runs for its full set duration.
- **Stop condition:** The transition ends once it reaches full brightness, or is cancelled by a manual override.
- **Manual override:** The light switch or app always works to change brightness directly, and a skip option can disable the next scheduled run.

<div class="automation-example">IF the current time is 30 minutes before the desired wake time
AND today matches the intended schedule
AND the skip-tomorrow setting is off
THEN set the light to a low starting brightness
AND gradually increase it to full brightness over 30 minutes</div>

## Setup notes

1. Decide on the wake time and the transition length, then calculate the start time by subtracting the two, for example 6:00 AM start for a 6:30 AM wake time with a 30 minute transition.
2. Confirm the light or switch actually supports a smooth transition to the target brightness, rather than jumping in large steps, since some platforms handle this better than others.
3. Test the lowest brightness the bulb can reach; if it is still too bright to start comfortably, consider pointing the fixture away from the bed for the first part of the cycle.
4. Add a day-of-week condition if the wake-up schedule differs between weekdays and weekends.
5. Add a simple way to skip the next run, such as a virtual switch or dashboard toggle, for days the schedule does not apply.

## Advanced features

### Color temperature shift

Where the bulb supports it, start with a warmer color temperature and shift toward a cooler, more daylight-like temperature as brightness increases, to more closely resemble an actual sunrise.

### Partner-friendly mode

Use a single bedside lamp facing away from a partner's side of the bed, and cap the maximum brightness lower than a full ceiling fixture would need, to reduce the effect on someone who should stay asleep.

## Failure modes

- **Transition feels too fast or abrupt:** Increase the total transition time or lower the starting brightness.
- **Light does not dim low enough to start:** Check the bulb's documented minimum brightness, or reposition the fixture away from direct line of sight to the bed.
- **Transition jumps in visible steps instead of fading smoothly:** Confirm the platform and device both support a gradual transition command, not just discrete brightness levels.
- **The automation wakes someone who should stay asleep:** Reduce maximum brightness, reposition the light, or restrict it to a single lamp rather than the whole room.
- **The automation runs on a day it should not:** Check the day-of-week condition and confirm any skip setting was applied correctly.

## Done when

- [ ] The wake time and transition length are set and the start time is calculated correctly.
- [ ] The light fades smoothly rather than in visible steps.
- [ ] The starting brightness is comfortably dim for the room.
- [ ] The schedule matches the intended days, with a working way to skip a single day.

## FAQ

### How long should the wake-up transition last?

Fifteen to thirty minutes is a reasonable starting range. A longer transition, up to 45 or 60 minutes, feels more gradual for deep sleepers, but takes more advance planning around the actual wake time.

### What if my bulb does not dim low enough to start comfortably dim?

Some bulbs have a higher minimum brightness than others. If the starting level is already too bright, consider pointing the light away from the bed for the first part of the transition, or choosing a bulb with a lower documented minimum.

### Can this wake one person without disturbing a partner?

Yes, using a single bedside lamp facing away from the partner's side of the bed, and keeping the maximum brightness lower, reduces the effect on someone who is not meant to wake up yet.

## Related recipes

- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)
- [Start a wind-down bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Adjust blinds at sunset and sunrise](/automation/climate/blinds-sunset-sunrise.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">Back to lighting automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>