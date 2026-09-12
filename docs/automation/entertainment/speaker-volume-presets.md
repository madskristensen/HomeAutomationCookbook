---
layout: automation
redirect_from:
  - /automation/media/speaker-volume-presets.html
date: 2025-11-28
title: Set smart-speaker volume presets
description: Choose a quiet, normal, or loud preset once instead of adjusting each speaker by hand whenever the household changes activities.
keywords: speaker volume automation, audio presets, volume control scenes, smart speaker volume, consistent volume
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/entertainment/speaker-volume-presets.png
compact: true
faqs:
  - question: Why use presets instead of just adjusting volume manually?
    answer: A preset gives the same result every time with one action, instead of guessing at a percentage on each speaker separately, especially across more than one room.
  - question: Will a preset override someone who just manually changed the volume?
    answer: Yes, running a preset sets an explicit level regardless of the current volume. Reserve automatic time-based presets for hours where that tradeoff is acceptable.
  - question: Can different rooms use different volume levels for the same preset?
    answer: Yes, a preset can hold a different percentage for each room or speaker, since a comfortable volume in a small bedroom is not the same as in an open living room.
---

# Use speaker volume presets

<figure class="content-hero">
  <img src="/assets/img/social/recipes/entertainment/speaker-volume-presets.svg" alt="" width="1200" height="630">
</figure>

Set every speaker to a defined low, medium, or loud level with a single command instead of adjusting each one by hand.

**Best for:** A household with more than one speaker where a repeatable, predictable volume level matters more than fine manual control every time.

**Not for:** A single-speaker setup where reaching for the volume control is just as fast as running a preset.

## Why this exists

Manually adjusting several speakers to a consistent level takes longer than it should, and a preset gives the same result every time. It also makes handing off a "party" or "quiet" moment to a single command instead of remembering the right percentage for each room.

## Logic

<div class="automation-example">IF the "low" preset is selected
THEN set all grouped speakers to their low-volume level

IF the "medium" preset is selected
THEN set all grouped speakers to their medium-volume level

IF the "loud" preset is selected
THEN set all grouped speakers to their loud-volume level</div>

- **Trigger:** A button, voice command, or scheduled time selects a preset (low, medium, or loud).
- **Conditions:** None required; the chosen preset applies immediately.
- **Action:** Set every speaker in the group to the percentage defined for that preset.
- **Wait / timeout:** None; the change applies once and stays until another preset or manual adjustment changes it.
- **Stop condition:** Not applicable; a preset simply sets a level rather than starting or stopping something.
- **Manual override:** Any speaker can still be adjusted directly at any time after a preset is applied.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Store and apply the preset**

No personally verified recommendation yet. Any platform that supports scenes or scripts can store a set of volume levels and apply them together.

</div>
<div class="product-item" markdown="1">

**Play and adjust audio**

Any speaker the platform can control works, for example a Sonos speaker, which is what I use.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Decide on a small number of presets, such as low, medium, and loud, rather than a long list that becomes hard to remember.
2. Set a specific percentage for each speaker under each preset, since a comfortable level in one room is not the same in another.
3. Choose how each preset will be triggered, whether by button, voice command, or schedule, and confirm each method reliably applies the preset.
4. If using a scheduled preset, such as automatically lowering volume at night, make sure the household understands it will override a volume they set manually earlier.

## Advanced features

### Scheduled quiet hours

Automatically apply the low preset at a set time each night, so volume settles to a quiet level without anyone remembering to do it.

### Activity-based presets

Where useful, add presets tied to an activity rather than just a volume level, such as a lower level for podcasts and a higher one for music, each still defined as a specific percentage per speaker.

## Failure modes

- **Some speakers do not change:** Confirm every speaker in the group is online and still recognized under its expected name in the platform.
- **Volume looks wrong for a specific room:** Adjust that room's percentage under the preset rather than changing the preset globally.
- **A scheduled preset overrides a volume someone just set:** Either accept that tradeoff for the intended hours, or narrow the schedule so it only applies when the household is likely to be away or asleep.
- **Preset does not apply at all:** Check the trigger, whether a button, voice command, or schedule, is still correctly linked to the preset action.

## FAQ

### Why use presets instead of just adjusting volume manually?

A preset gives the same result every time with one action, instead of guessing at a percentage on each speaker separately, especially across more than one room.

### Will a preset override someone who just manually changed the volume?

Yes, running a preset sets an explicit level regardless of the current volume. Reserve automatic time-based presets for hours where that tradeoff is acceptable.

### Can different rooms use different volume levels for the same preset?

Yes, a preset can hold a different percentage for each room or speaker, since a comfortable volume in a small bedroom is not the same as in an open living room.

## Related recipes

- [Play music when a shower starts](/automation/entertainment/shower-music.html)
- [Play music when arriving home](/automation/entertainment/welcome-home-music.html)
- [Play or pause music with a physical switch](/automation/entertainment/music-switch-control.html)

<div class="page-navigation">
  <a href="/automation/entertainment/index.html">Back to entertainment</a>
  <a href="/automation/index.html">View all automations</a>
</div>