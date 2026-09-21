---
layout: automation
redirect_from:
  - /automation/media/shower-music.html
date: 2025-11-28
title: Play music when a shower starts
description: A platform-neutral recipe that starts music or a podcast in the bathroom when a shower begins, using a light or door sensor as the trigger.
keywords: shower music automation, bathroom speaker automation, automatic music, shower entertainment, bathroom audio control
last_modified_at: 2026-09-21
image: /assets/img/social/recipes/entertainment/shower-music.png
compact: true
faqs:
  - question: Which trigger works best, the light switch or a door sensor?
    answer: A light switch trigger is usually the most reliable since the light almost always goes on before the shower starts. A door sensor is a reasonable backup for a glass enclosure without a separate switch.
  - question: Will this wake other people in the house?
    answer: Not if a night-mode or quiet-hours condition is included. Restrict playback to normal waking hours, or add a condition that skips playback when the household is in a sleeping state.
  - question: Does the music stop automatically when the shower ends?
    answer: Yes, if a matching "lights off" or "door closed for a while" condition is set up to stop or pause playback a couple of minutes after the shower trigger clears.
---

# Play music when a shower starts

<figure class="content-hero">
  <img src="/assets/img/social/recipes/entertainment/shower-music.svg" alt="Music starts at a comfortable volume when a shower begins" width="1200" height="630">
</figure>

Start music or a podcast on a bathroom speaker automatically when the shower light goes on, and stop it again once the shower ends.

**Best for:** A bathroom with a smart light switch or door sensor that reliably signals when a shower is starting, paired with a speaker that already works in that room.

**Not for:** Waking a sleeping household. Restrict this to normal waking hours or add a quiet-hours condition.

## Why this exists

Remembering to start music before stepping into the shower, especially early in the morning, is easy to forget. Tying playback to a signal that already exists, like the light switch, removes the need to think about it and gives a consistent morning routine without extra steps.

## Logic

<div class="automation-example">IF the bathroom light turns on
AND the current time is within waking hours
AND the household is not in quiet hours
THEN play music on the bathroom speaker at the preset volume

IF the bathroom light has been off for a couple of minutes
THEN stop or pause the bathroom speaker</div>

- **Trigger:** The bathroom light turns on, or a door sensor reports the shower door opening.
- **Conditions:** The current time is within normal waking hours, and the household is not in a sleeping or quiet-hours state.
- **Action:** Start music or the last-used podcast on the bathroom speaker at a preset volume.
- **Wait / timeout:** Keep playing until the stop condition is met.
- **Stop condition:** The light stays off, or the door stays closed, for a couple of minutes.
- **Manual override:** The speaker's own controls always work to pause, stop, or change volume directly.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Trigger the automation**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Use the existing shower light switch as the trigger where possible.

</div>
<div class="product-item" markdown="1">

**Play the music**

Any speaker the platform can control works, for example a Sonos speaker, which is what I use. A waterproof or water-resistant model is worth considering for a bathroom, but no specific rating is required.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Choose one trigger, the light switch or a door sensor, and treat the other as an optional backup rather than combining both in a way that is hard to troubleshoot.
2. Add a quiet-hours or night-mode condition so this does not start music while someone else in the house is asleep.
3. Set a fixed starting volume so the result is predictable regardless of the speaker's last setting.
4. Require the stop condition to hold for a couple of minutes so briefly leaving the bathroom does not cut off the music early.
5. Confirm the speaker and trigger both respond reliably in the platform's automation log before relying on this daily.

## Advanced features

### Time-of-day content

Where useful, play a news podcast on weekday mornings and a relaxing playlist at other times, using the same trigger with different content chosen by time and day.

### Pause instead of stop for podcasts

Use a pause action rather than stop for podcast content so playback resumes from the same point on the next shower.

## Failure modes

- **Music does not start:** Confirm the speaker is online, the streaming account is still logged in, and the trigger is registering in the automation log.
- **Music starts at the wrong volume:** Set the volume explicitly as part of the action, not left to whatever the speaker was last set to.
- **Music plays at night:** Check that the quiet-hours condition is present and correctly configured.
- **Wrong content plays:** Confirm the playlist or podcast reference still matches what is expected, since streaming services occasionally change identifiers.
- **Music does not stop after the shower:** Confirm the off-condition requires a sustained clear period and is not just checking a single instantaneous reading.

## FAQ

### Which trigger works best, the light switch or a door sensor?

A light switch trigger is usually the most reliable since the light almost always goes on before the shower starts. A door sensor is a reasonable backup for a glass enclosure without a separate switch.

### Will this wake other people in the house?

Not if a night-mode or quiet-hours condition is included. Restrict playback to normal waking hours, or add a condition that skips playback when the household is in a sleeping state.

### Does the music stop automatically when the shower ends?

Yes, if a matching "lights off" or "door closed for a while" condition is set up to stop or pause playback a couple of minutes after the shower trigger clears.

## Related recipes

- [Turn on the bathroom fan when a shower starts](/automation/climate/fan-shower.html)
- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)
- [Use speaker volume presets](/automation/entertainment/speaker-volume-presets.html)

<div class="page-navigation">
  <a href="/automation/entertainment/index.html">Back to entertainment</a>
  <a href="/automation/index.html">View all automations</a>
</div>