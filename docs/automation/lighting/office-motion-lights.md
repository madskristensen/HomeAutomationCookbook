---
layout: automation
date: 2026-10-25
title: Office lights that stay on while you work
description: Office lights turn on with motion at a level that fits the time of day, and stay on while you sit still because the monitor's power draw shows someone is at the desk.
keywords: office motion lights, lights turn off while sitting still, monitor power monitoring, smart plug desk occupancy, webCoRE office piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/lighting/office-motion-lights.png
compact: true
faqs:
  - question: Why watch the monitor instead of the computer?
    answer: The monitor has a clear on and off state. Windows turns it off after a few minutes without input, and its power drops to standby. That makes it a simple signal for whether someone is at the desk.
  - question: What if I read at the desk without touching the computer?
    answer: The monitor turns off after the Windows timeout, and once motion has also been quiet for 15 minutes the lights turn off. Move a little or tap a key.
  - question: Why does the music pause when the lights turn off?
    answer: If the lights are off, nobody is working in the office, so the music has no reason to keep playing.
products:
  - job: "Know someone is at the desk"
    body: "A smart plug with power metering on the monitor. The [device guide](/getting-started/device-guide.html#products-i-have-used) lists power-metering plugs."
  - job: "Know someone walked in"
    body: "A motion sensor in the office, and an outdoor light sensor in the front yard for the dark check."
  - job: "Know I am home"
    body: "Phone presence from the UniFi network."
  - job: "Play the music"
    body: "A Sonos speaker in the office."
---

# Office lights that stay on while you work

{% include content-hero.html src="/assets/img/social/recipes/lighting/office-motion-lights.svg" alt="Office lights stay on while the monitor shows someone is at the desk" %}

Motion lights in an office have one big problem. You sit still at the desk and the lights go out. This recipe fixes that with a smart plug that measures the monitor's power. While the monitor is on, someone is at the desk, so the lights stay on.

**Best for:** A home office with a desk computer, dimmable lights, a motion sensor, and a monitor on a power-metering smart plug.

**Not for:** An office where you mostly work on a laptop with no external monitor.

## Why this exists

A motion sensor cannot see someone typing. After a while it reports no motion, and the lights turn off in the middle of work. A presence sensor is one fix. Another is to use a signal you already have. Windows turns the display off after a few minutes without input, so the monitor's power draw tells the house whether anyone is using the computer.

## Logic

<div class="automation-example">IF office motion is detected
AND the office lights are off
THEN set the office lights to 12% if it is dark outside and between 8 PM and 8 AM
OR ELSE set them to 60%

IF office motion is detected
AND it is a weekday between 9 AM and 4 PM
AND my phone is home
THEN set the office speaker to volume 4
AND load the "feel good" favorite

IF the office lights are on
AND there has been no motion for 15 minutes
AND the monitor draws under 10 W
THEN turn off the office lights

IF the office lights turn off
THEN pause the office speaker</div>

- **Trigger:** Office motion, the monitor's power, or the lights turning off.
- **Conditions:** Lights only turn on if they were off. The music only starts on weekday work hours when my phone is home.
- **Action:** Set the lights, start or pause the music.
- **Wait / timeout:** 15 minutes without motion, plus the monitor in standby.
- **Stop condition:** Both "empty" signals together turn off the lights.
- **Manual override:** The wall switch and the speaker's own app keep working.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. In Windows power settings, set the screen to turn off after a short idle time. I use 5 minutes.
2. Plug the monitor into the power-metering plug. Watch its power while on and in standby. In standby it should read well under 10 W.
3. Set the "off" threshold between those two readings.
4. Check the dark threshold on the outdoor light sensor at dusk, so the 12% night level kicks in when it should.

## How I do it in webCoRE

This is a real piston I run on Hubitat.

1. When office motion is detected and the office lights are off, it checks the front yard light sensor and the time. If it is under 15 lux and between 8 PM and 8 AM, the lights go to 12%. Otherwise they go to 60%.
2. On weekdays between 9 AM and 4 PM, if my phone is present on the UniFi network, the office Sonos is set to volume 4 and loads the "feel good" Sonos favorite.
3. When the lights are on, motion has been inactive for 15 minutes, and the monitor plug reads under 10 W, the lights turn off.
4. Whenever the office lights turn off, for any reason, the office Sonos pauses.

The monitor is the key. As long as I am using the computer, Windows keeps the display on, the plug reads above 10 W, and the lights stay on no matter how still I sit.

## Advanced features

### Pair it with the call button

Use the [video call lighting button](/automation/lighting/video-call-lighting-button.html) for calls. It sets the camera lighting and pauses the same speaker.

## Failure modes

- **Lights turn off while working:** The monitor may be going to standby too early, or its power reading is close to the threshold. Check the Windows timeout and the real watt numbers.
- **Lights never turn off:** The monitor is not going to standby. Check that Windows turns off the display, and that nothing like a video keeps it awake.
- **Music starts when I am away:** Check the phone presence. A phone left at home counts as home.

## FAQ

### Why watch the monitor instead of the computer?

The monitor has a clear on and off state. Windows turns it off after a few minutes without input, and its power drops to standby. That makes it a simple signal for whether someone is at the desk.

### What if I read at the desk without touching the computer?

The monitor turns off after the Windows timeout, and once motion has also been quiet for 15 minutes the lights turn off. Move a little or tap a key.

### Why does the music pause when the lights turn off?

If the lights are off, nobody is working in the office, so the music has no reason to keep playing.

## Related recipes

- [Video call lighting button](/automation/lighting/video-call-lighting-button.html)
- [Turn lights on with motion sensors](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Set smart-speaker volume presets](/automation/entertainment/speaker-volume-presets.html)

{% include page-navigation.html
  left_url="/automation/lighting/"
  left_label="Back to lighting"
  right_url="/automation/"
  right_label="View all automations"
%}
