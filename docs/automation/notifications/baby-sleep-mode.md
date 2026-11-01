---
layout: automation
redirect_from:
  - /automation/misc/baby-sleep-mode.html
date: 2025-11-29
title: Start nursery quiet mode when the white noise turns on
description: Plug the white noise machine into a power-monitoring plug. When it turns on, the house goes quiet. When it turns off, lights fade back up.
keywords: nursery quiet mode, white noise automation, baby sleep automation, power monitoring plug, smart plug nursery
last_modified_at: 2026-11-01
image: /assets/img/social/recipes/notifications/baby-sleep-mode.png
compact: true
faqs:
  - question: What does quiet mode do?
    answer: It is a house state you name Quiet. While it is on, the lights near the nursery dim, blinds can close, and optional sounds like announcements and chimes stay silent. Urgent alerts still play.
  - question: How do I find the right power threshold?
    answer: Turn the white noise machine on and read the watts in your hub app. Then turn it off and read again. Set the threshold between the two numbers.
  - question: Can white noise power prove that a baby is asleep?
    answer: No. It only shows the machine is on. Treat it as a sign that bedtime has started, not as a baby monitor.
products:
  - job: "Sense the white noise machine"
    body: "[Ezlo 800 Series Z-Wave smart plug](https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20). It is the power-monitoring plug on the [device guide](/getting-started/device-guide.html#power-monitoring). Check that it sees your machine's draw first."
  - job: "Dim the lights"
    body: "Dimmable smart lights or dimmer switches in the nursery and nearby hallway."
  - job: "Start quiet mode by hand (optional)"
    body: "A smart button, or a smart switch that supports multi-tap scenes."
tags: [notifications, kids, bedtime]
---

# Start nursery quiet mode when the white noise turns on

{% include content-hero.html src="/assets/img/social/recipes/notifications/baby-sleep-mode.svg" alt="A bell and phone icon next to the title Start nursery quiet mode when the white noise turns on" %}

The white noise machine already marks bedtime. Plug it into a smart plug that measures power. When the machine turns on, the house goes into quiet mode. When it turns off, quiet mode ends and the lights fade back up.

This has worked reliably for years in my house.

**Best for:** Nurseries and nap rooms where a white noise machine runs at every nap and bedtime.

**Not for:** Detecting sleep, watching a child, or replacing a baby monitor.

## What quiet mode means

Quiet mode is a house state. You can call it a mode, a scene, or a switch, depending on your platform. While it is on:

- The nursery and hallway lights dim to a low level.
- Smart blinds in the nursery close (optional).
- Optional sounds stay silent. That means announcements, doorbell chimes, and speaker reminders.
- Urgent alerts still play. Smoke, carbon monoxide, leak, and security alerts are never muted.

When quiet mode ends, those changes undo themselves. The lights fade up slowly instead of snapping on.

## Logic

<div class="automation-example">IF the white noise plug power rises above the threshold
THEN turn on quiet mode
AND dim the nursery and hallway lights
AND close the nursery blinds (optional)
AND mute announcements and chimes

IF the white noise plug power falls below the threshold
THEN turn off quiet mode
AND fade the lights up slowly
AND turn announcements and chimes back on

KEEP smoke, carbon monoxide, leak, and security alerts active</div>

- **Trigger:** The plug sees the white noise machine start or stop drawing power.
- **Conditions:** Only change state when the power crosses the threshold you set.
- **Action:** Turn quiet mode on or off.
- **Stop condition:** The white noise machine turns off, or someone ends quiet mode by hand.
- **Manual override:** Normal light switches and blind controls keep working.

## What I used

{% include product-list.html %}

## Setup notes

1. Plug the white noise machine into the power-monitoring plug.
2. Check the machine's on-draw. Turn it on and read the watts in your hub app. Turn it off and read again.
3. Set a threshold between those two numbers. Some machines draw only a few watts, so test yours.
4. Create a quiet mode in your hub. A mode, a virtual switch, or a scene all work.
5. Have quiet mode dim the lights, close the blinds, and mute announcements and chimes.
6. Have the end of quiet mode fade the lights up over a minute or so.
7. Leave every urgent alert out of quiet mode.

## Other ways to start quiet mode

The white noise plug is the main method. You can add a manual control for naps without white noise, or for a guest who does not know the routine.

- **A smart button:** One press starts quiet mode for the room. Another press ends it.
- **A smart switch with double-tap:** Double-tap down starts quiet mode for the room. Double-tap up ends it. This needs a switch that supports multi-tap scenes. Check that your hub sees the double-tap as its own event.

## Advanced features

### Add more quiet

You can also lower speaker volume in nearby rooms, pause a robot vacuum, or hold a scheduled reminder until quiet mode ends.

### Keep a night path light

Leave one light at a very low level so a caregiver can walk in at night.

## Failure modes

- **Quiet mode never starts:** The machine draws less than the threshold. Lower it, or try a different plug.
- **Quiet mode flickers on and off:** Power hovers near the threshold. Add a short delay, such as 30 seconds, before the state changes.
- **Quiet mode stays on all day:** Someone left the white noise running. Add a reminder after a set time.
- **An urgent alert is muted:** Take that alert out of quiet mode and test it again.
- **The hub restarts:** Check that quiet mode comes back in the right state.

## FAQ

### What does quiet mode do?

It is a house state you name Quiet. While it is on, the lights near the nursery dim, blinds can close, and optional sounds like announcements and chimes stay silent. Urgent alerts still play.

### How do I find the right power threshold?

Turn the white noise machine on and read the watts in your hub app. Then turn it off and read again. Set the threshold between the two numbers.

### Can white noise power prove that a baby is asleep?

No. It only shows the machine is on. Treat it as a sign that bedtime has started, not as a baby monitor.

## Related recipes

- [All kids and family routines](/articles/smart-home-automations-for-kids.html)
- [Open and close blinds at sunrise and sunset](/automation/climate/blinds-sunset-sunrise.html)
- [Guest mode](/automation/daily-routines/guest-mode.html)
- [Dim bathroom lighting at night](/automation/lighting/bathroom-night-light.html)
- [Notification automations](/automation/notifications/)

{% include page-navigation.html
  left_url="/automation/notifications/"
  left_label="Back to notification automations"
  right_url="/automation/"
  right_label="View all automations"
%}
