---
layout: automation
date: 2025-11-30
title: Set up one-tap pool party mode
description: A platform-neutral recipe that starts music and lighting for a pool or backyard party with one button press, without touching safety alarms.
keywords: pool party automation, backyard party mode, outdoor entertainment, party scene, one tap party mode
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/entertainment/pool-party-mode.png
compact: true
faqs:
  - question: Does party mode disable any safety alarms?
    answer: No. This recipe should never touch pool alarms, gate sensors, or other safety features. It only controls lighting, music, and non-critical notifications.
  - question: Why include an automatic end time?
    answer: A party scene left running after everyone has gone home wastes electricity and can annoy neighbors with music or bright colored lights running unattended.
  - question: Can more than one button trigger the same scene?
    answer: Yes, a voice command, a physical button, and a dashboard tile can all point at the same automation, which keeps behavior consistent regardless of how it is started.
---

# Set up one-tap pool party mode

<figure class="content-hero">
  <img src="/assets/img/social/recipes/entertainment/pool-party-mode.svg" alt="" width="1200" height="630">
</figure>

Turn on party lighting and music around a pool or backyard with a single button press, and automatically end it after a set time.

**Best for:** A backyard or pool area with color-capable outdoor lighting and a weatherproof speaker that already respond to platform automation commands.

**Not for:** Disabling pool safety alarms, gate sensors, or any other safety feature. Those must keep working regardless of party mode.

## Why this exists

Turning on several outdoor devices individually is slow, and it is easy to forget one, or forget to turn everything off again afterward. A single trigger that sets lighting and music to a consistent state, and reverses itself automatically, is a better fit for something as informal as a pool gathering.

## Logic

<div class="automation-example">IF "pool party mode" is triggered
AND the current time is within allowed hours
THEN set outdoor lights to the party scene
AND start the party playlist at the preset volume
AND pause routine outdoor motion notifications

IF four hours have passed since party mode started
OR "end pool party" is triggered
THEN restore normal outdoor lighting
AND stop music
AND resume routine outdoor motion notifications</div>

- **Trigger:** A button press, voice command, or dashboard tile for "pool party mode."
- **Conditions:** The current time falls within hours the household considers reasonable for outdoor music.
- **Action:** Set outdoor lighting to a party scene, start the party playlist at a set volume, and pause only non-critical outdoor notifications, such as routine motion alerts.
- **Wait / timeout:** Run for a fixed duration, such as four hours, unless ended manually first.
- **Stop condition:** A separate "end party" trigger, or the automatic timeout, restores normal lighting and stops music.
- **Manual override:** Any light, speaker, or notification setting can still be changed directly at any time.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Outdoor party lighting**

No personally verified recommendation yet. Needs to be rated for outdoor use and support color or scene control from the platform.

</div>
<div class="product-item" markdown="1">

**Outdoor music playback**

Any speaker the platform can control works, for example a Sonos speaker, which is what I use. Choose a weatherproof or otherwise suitable model for the location.

</div>
<div class="product-item" markdown="1">

**Trigger the scene**

No personally verified recommendation yet. Any button, voice command, or dashboard tile the platform can use to start an automation.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Confirm outdoor lighting and the speaker both respond reliably to platform commands before wiring them into a single scene.
2. Set a maximum volume level as part of the automation so it cannot be started louder than the household considers acceptable for neighbors.
3. Choose which notifications, if any, should pause during party mode, and confirm safety-related alarms and sensors are explicitly excluded.
4. Build a matching "end party" action, whether a separate button or a timeout, so the scene does not run indefinitely.
5. Restrict activation to hours the household is comfortable with outdoor music and lights running.

## Advanced features

### Gradual wind-down

Instead of stopping abruptly at the timeout, gradually lower volume and dim lights over several minutes so the change feels less sudden.

### Scene variations

Where the platform supports more than one saved scene, offer a quieter daytime version and a more vivid evening version, selected by time of day.

## Failure modes

- **Lights and music start at different speeds:** Group devices by the same wireless protocol where possible, or add a short delay to the slower devices so they land closer together.
- **Music does not start:** Confirm the speaker is online and the streaming account used by the automation is still authenticated.
- **Party mode never ends:** Confirm the timeout action exists and is enabled; a scene should never rely on someone remembering to turn it off manually.
- **Safety notifications get paused by mistake:** Review exactly which notification types the automation pauses and remove anything safety-related.
- **Volume is too loud:** Lower the preset volume in the action itself rather than relying on someone adjusting it after the fact.

## FAQ

### Does party mode disable any safety alarms?

No. This recipe should never touch pool alarms, gate sensors, or other safety features. It only controls lighting, music, and non-critical notifications.

### Why include an automatic end time?

A party scene left running after everyone has gone home wastes electricity and can annoy neighbors with music or bright colored lights running unattended.

### Can more than one button trigger the same scene?

Yes, a voice command, a physical button, and a dashboard tile can all point at the same automation, which keeps behavior consistent regardless of how it is started.

## Related recipes

- [Play music when arriving home](/automation/entertainment/welcome-home-music.html)
- [Dim lights when the TV turns on](/automation/entertainment/tv-dim-lights.html)
- [Use speaker volume presets](/automation/entertainment/speaker-volume-presets.html)

<div class="page-navigation">
  <a href="/automation/entertainment/index.html">Back to entertainment</a>
  <a href="/automation/index.html">View all automations</a>
</div>