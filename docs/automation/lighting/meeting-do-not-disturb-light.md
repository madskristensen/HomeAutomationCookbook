---
layout: automation
date: 2026-10-25
title: Meeting button with a do-not-disturb light
description: One button press turns on a light outside the office, dims the office lights, and pauses the music, then puts everything back when the meeting ends.
keywords: do not disturb light, meeting light automation, office meeting button, pause Sonos meeting, webCoRE meeting piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/lighting/meeting-do-not-disturb-light.png
compact: true
faqs:
  - question: Why use a button instead of watching my calendar?
    answer: Meetings start early, run late, and sometimes get skipped. A button press is a deliberate signal, so the light outside the door is always right.
  - question: Will the music start again if it was off before the meeting?
    answer: No. The automation remembers whether music was playing when the light turned on, and only resumes it if it was.
  - question: What if someone turns the outside light on or off by hand?
    answer: The rest of the routine follows the light, not the button. Turning the light on or off any way you like runs the same steps.
---

# Meeting button with a do-not-disturb light

{% include content-hero.html src="/assets/img/social/recipes/lighting/meeting-do-not-disturb-light.svg" alt="A light outside the office shows a meeting is in progress" %}

Press one button before a call. A light outside the office turns on so the family knows not to barge in. The office lights dim and the music pauses. Press it again after the call and the room goes back to normal.

**Best for:** A home office with a door, a dimmable light inside, a speaker the hub can control, and a small light or lamp just outside.

**Not for:** A shared space where other people need the lights or music to keep going during your calls.

## Why this exists

Kids and other family members cannot see through a closed door. A small light outside the office answers the question "can I come in?" without anyone knocking. Pausing music and dimming the lights at the same time removes two more things to do right before a call starts.

## Logic

<div class="automation-example">IF the meeting button is pressed
THEN toggle the do-not-disturb light outside the office

IF the do-not-disturb light turns on
THEN remember whether the office speaker is playing
AND pause the office speaker
AND dim the office lights to 15%

IF the do-not-disturb light turns off
THEN set the office lights to 60%
AND resume the office speaker only if it was playing before</div>

- **Trigger:** A button press toggles the outside light. The light turning on or off drives everything else.
- **Conditions:** On the way out of a meeting, music resumes only if it was playing when the meeting started.
- **Action:** Dim or restore the office lights, pause or resume the office speaker.
- **Wait / timeout:** None. Everything happens right away.
- **Stop condition:** Turning the light off ends meeting mode.
- **Manual override:** The wall switch and the speaker's own app keep working. Switching the outside light by hand runs the same steps as the button.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Start and end the meeting**

Any smart button the hub can see. A single press is all this needs.

</div>
<div class="product-item" markdown="1">

**Show do-not-disturb outside the door**

Any small smart light or a lamp on a smart plug. I use one with a moon shape, which the kids understand without explanation.

</div>
<div class="product-item" markdown="1">

**Pause the music**

A speaker the hub can pause and resume. I use a Sonos speaker in the office.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Put the button where you can reach it from your chair. You will press it with a call already ringing.
2. Make the outside light the source of truth. The button only toggles it, and the rest of the rule watches the light. That way a dashboard tile or a voice command works the same as the button.
3. Save whether music was playing before you pause it. Without that, the routine either never resumes music or starts music you had turned off.
4. Pick brightness levels that work on camera. 15% during the call and 60% after works for my office, but test yours with the camera on.
5. Explain the light to the household once. A rule only works if people know what the light means.

## How I do it in webCoRE

This is a real piston I run on Hubitat. It has two parts.

1. The first part listens for the button. When the button is pressed, it toggles the moon light outside the office.
2. The second part watches the moon light. When it changes to on, it stores the office Sonos playback status in a variable, pauses the Sonos, and sets the office lights to 15%.
3. When the moon light changes to off, it sets the office lights to 60%. Then it checks the variable. If the Sonos was playing before, it sends play. If not, it leaves the speaker alone.

Keeping the button and the light as separate triggers is the important part. I can turn the moon light on from a dashboard and get the exact same result.

## Advanced features

### Show it on a dashboard

Add the outside light to a wall tablet dashboard so anyone in the house can see that a call is in progress.

### Use a presence sensor as a backup

If you often forget to press the button after a call, add a rule that turns the light off when the office has been empty for a while.

## Failure modes

- **Music starts after a meeting when it was off before:** Check that the playing state is saved before the pause, not after.
- **Lights do not dim:** Confirm the office lights are dimmable and respond to a set level command from the hub.
- **The button does nothing:** Check the battery and confirm presses show up in the hub's event log.
- **The light stays on all evening:** You forgot to press the button. Consider the presence backup above.

## FAQ

### Why use a button instead of watching my calendar?

Meetings start early, run late, and sometimes get skipped. A button press is a deliberate signal, so the light outside the door is always right.

### Will the music start again if it was off before the meeting?

No. The automation remembers whether music was playing when the light turned on, and only resumes it if it was.

### What if someone turns the outside light on or off by hand?

The rest of the routine follows the light, not the button. Turning the light on or off any way you like runs the same steps.

## Related recipes

- [Link lights to a wireless button](/automation/lighting/wireless-button-linked-lights.html)
- [Control music with a physical switch](/automation/entertainment/music-switch-control.html)
- [Smart home status tiles](/automation/notifications/status-tiles.html)

{% include page-navigation.html
  left_url="/automation/lighting/index.html"
  left_label="Back to lighting"
  right_url="/automation/index.html"
  right_label="View all automations"
%}
