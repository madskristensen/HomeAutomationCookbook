---
layout: automation
redirect_from:
  - /automation/lighting/meeting-do-not-disturb-light.html
date: 2026-10-25
title: Video call lighting button
description: One button press turns on a warm backlight behind you, dims the overhead lights, and pauses the music for a video call, then puts everything back when the call ends.
keywords: video call lighting, webcam lighting automation, office meeting button, pause Sonos meeting, webCoRE meeting piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/lighting/video-call-lighting-button.png
compact: true
faqs:
  - question: Why dim the overhead lights instead of making the room brighter?
    answer: Bright overhead light flattens your face on camera. Dimming it and adding a warm light behind you gives the image depth and separates you from the wall.
  - question: Will the music start again if it was off before the call?
    answer: No. The automation remembers whether music was playing when the backlight turned on, and only resumes it if it was.
  - question: What if someone turns the backlight on or off by hand?
    answer: The rest of the routine follows the backlight, not the button. Turning it on or off any way you like runs the same steps.
products:
  - job: "Start and end the call"
    body: "Any smart button the hub can see. A single press is all this needs."
  - job: "Light you from behind"
    body: "Any warm smart light, or a lamp on a smart plug, on the wall behind your chair."
  - job: "Pause the music"
    body: "A speaker the hub can pause and resume. I use a Sonos speaker in the office."
---

# Video call lighting button

{% include content-hero.html src="/assets/img/social/recipes/lighting/video-call-lighting-button.svg" alt="A warm backlight and dimmed ceiling lights set up the office for a video call" %}

Press one button before a video call. A warm light on the wall behind you turns on, the office ceiling lights dim, and the music pauses. Press it again after the call and the lights and music go back to how they were.

The same button setup also works as a do-not-disturb light. For that use, the light goes outside the office door, not behind you on the wall, so the family can see from the hallway that a call is in progress.

**Best for:** A home office with dimmable ceiling lights, a speaker the hub can control, and a smart light or lamp that can sit on the wall behind your chair.

**Not for:** A shared space where other people need the lights or music to keep going during your calls.

## Why this exists

Ceiling lights at full brightness make a flat, washed out webcam image. Dimming them and adding a warm light behind you gives the picture depth and separates you from the wall. Getting the room ready by hand means several steps right as a call starts. Doing it with one button, and pausing the music at the same time, removes all of that.

## Logic

<div class="automation-example">IF the call button is pressed
THEN toggle the backlight behind the desk

IF the backlight turns on
THEN remember whether the office speaker is playing
AND pause the office speaker
AND dim the office ceiling lights to 15%

IF the backlight turns off
THEN set the office ceiling lights to 60%
AND resume the office speaker only if it was playing before</div>

- **Trigger:** A button press toggles the backlight. The backlight turning on or off drives everything else.
- **Conditions:** After the call, music resumes only if it was playing when the call started.
- **Action:** Dim or restore the ceiling lights, pause or resume the office speaker.
- **Wait / timeout:** None. Everything happens right away.
- **Stop condition:** Turning the backlight off ends call mode.
- **Manual override:** The wall switch and the speaker's own app keep working. Switching the backlight by hand runs the same steps as the button.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Put the button where you can reach it from your chair. You will press it with a call already ringing.
2. Make the backlight the source of truth. The button only toggles it, and the rest of the rule watches the light. That way a dashboard tile or a voice command works the same as the button.
3. Save whether music was playing before you pause it. Without that, the routine either never resumes music or starts music you had turned off.
4. Pick brightness levels with the camera on. 15% during the call and 60% after works for my office, but test yours.
5. Place the backlight so it lights the wall behind you, not the lens. Light shining straight into the camera hurts the image.

## How I do it in webCoRE

This is a real piston I run on Hubitat. It has two parts.

1. The first part listens for the button. When the button is pressed, it toggles the warm backlight on the wall behind my desk.
2. The second part watches the backlight. When it changes to on, it stores the office Sonos playback status in a variable, pauses the Sonos, and sets the office ceiling lights to 15%.
3. When the backlight changes to off, it sets the office ceiling lights to 60%. Then it checks the variable. If the Sonos was playing before, it sends play. If not, it leaves the speaker alone.

Keeping the button and the backlight as separate triggers is the important part. I can turn the backlight on from a dashboard and get the exact same result.

## Advanced features

### Show it on a dashboard

Add the backlight to a wall tablet dashboard so anyone in the house can see that a call is in progress.

### Use a presence sensor as a backup

If you often forget to press the button after a call, add a rule that turns the backlight off when the office has been empty for a while.

## Failure modes

- **Music starts after a call when it was off before:** Check that the playing state is saved before the pause, not after.
- **Lights do not dim:** Confirm the ceiling lights are dimmable and respond to a set level command from the hub.
- **The button does nothing:** Check the battery and confirm presses show up in the hub's event log.
- **The backlight stays on all evening:** You forgot to press the button. Consider the presence backup above.

## FAQ

### Why dim the overhead lights instead of making the room brighter?

Bright overhead light flattens your face on camera. Dimming it and adding a warm light behind you gives the image depth and separates you from the wall.

### Will the music start again if it was off before the call?

No. The automation remembers whether music was playing when the backlight turned on, and only resumes it if it was.

### What if someone turns the backlight on or off by hand?

The rest of the routine follows the backlight, not the button. Turning it on or off any way you like runs the same steps.

## Related recipes

- [Office lights that stay on while you work](/automation/lighting/office-motion-lights.html)
- [Control lights with a wireless button or linked switch](/automation/lighting/wireless-button-linked-lights.html)
- [Control music with a physical switch](/automation/entertainment/music-switch-control.html)
- [Smart home status tiles](/automation/notifications/status-tiles.html)

{% include page-navigation.html
  left_url="/automation/lighting/"
  left_label="Back to lighting"
  right_url="/automation/"
  right_label="View all automations"
%}
