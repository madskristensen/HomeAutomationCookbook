---
layout: automation
date: 2026-10-25
title: Garage lights that follow doors, motion, and the TV
description: Garage lights that turn on with the door or motion, stay on while you work, dim for the garage TV, and turn off only once the garage is empty.
keywords: garage lights automation, garage door lights on, garage motion lights, TV power monitoring dim lights, webCoRE garage piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/lighting/garage-lights-doors-motion-tv.png
compact: true
faqs:
  - question: Why check the TV power before turning the lights off?
    answer: Someone watching TV sits still, so motion sensors stop seeing them. The TV's power draw tells the automation someone is still using the space.
  - question: Why two power thresholds, 70 W and 30 W?
    answer: The gap keeps the lights from flickering between modes when the TV's draw moves around. Above 70 W means a movie is on. Under 30 W means the TV is off or in standby.
  - question: Why only turn the lights on if they were off?
    answer: If someone already set the lights to a different level, opening a door should not override that choice.
products:
  - job: "Know when a garage door opens"
    body: "A sensor on each garage door. See the [device guide](/getting-started/device-guide.html#products-i-have-used) for garage door tilt sensors."
  - job: "Know someone is in the garage"
    body: "Motion sensors in the garage and in the loft."
  - job: "Know the TV is on"
    body: "A smart plug with power metering on the TV. The [device guide](/getting-started/device-guide.html#products-i-have-used) lists the plugs I use to detect a TV."
  - job: "Light the garage"
    body: "Dimmable smart lights or a smart dimmer for the garage lights."
---

# Garage lights that follow doors, motion, and the TV

{% include content-hero.html src="/assets/img/social/recipes/lighting/garage-lights-doors-motion-tv.svg" alt="Garage lights stay on while doors, motion, or the TV show the space is in use" %}

Our garage has a loft and a TV. The lights need to come on the moment a garage door opens, stay on while anyone is out there, and dim when a movie starts. They should only turn off when the doors are closed, nobody is moving, and the TV is off.

**Best for:** A garage with smart dimmable lights, door sensors on the garage doors, a motion sensor or two, and maybe a TV.

**Not for:** A garage you only walk through. A simple [motion light](/automation/lighting/lights-on-motion.html) is enough there.

## Why this exists

Plain motion lights fail in a garage. You work under a car, or sit and watch TV, and the lights go out. Turning them off on a short timer leaves people in the dark. Requiring several "empty" signals at once fixes that. The TV adds one more signal and a nice bonus: dimming for movies.

## Logic

<div class="automation-example">IF either garage door opens
OR motion is detected in the garage
AND the garage lights are off
THEN set the garage lights to 80%

IF both garage doors have been closed for 2 minutes
AND there has been no motion in the garage or loft for 10 minutes
AND the TV has drawn under 30 W for 30 seconds
THEN turn off the garage lights

IF the TV power rises above 70 W
THEN dim the garage lights to 25%
AND remember that movie mode is on

IF movie mode is on
AND the TV has drawn under 30 W for 5 seconds
THEN set the garage lights back to 80%
AND clear movie mode</div>

- **Trigger:** A garage door opening, motion, or a change in the TV's power draw.
- **Conditions:** Lights only turn on if they were off. Turning off needs all three "empty" signals at the same time.
- **Action:** 80% for normal use, 25% for movies, off when empty.
- **Wait / timeout:** 2 minutes for doors, 10 minutes for motion, 30 seconds of low TV power before turning off. 5 seconds of low TV power to leave movie mode.
- **Stop condition:** All three empty signals together.
- **Manual override:** The wall switch still works.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Measure the TV's power draw when off, in standby, on a menu, and playing a movie. Set the thresholds from real numbers. Ours are under 30 W for off and above 70 W for a movie.
2. Keep a gap between the two power thresholds so small swings do not bounce the lights.
3. Put a motion sensor in every area where people spend time, including the loft. A single sensor misses someone in a corner.
4. Use a variable to remember movie mode. That way the lights only go back to 80% after a movie, not every time the TV draws a little less.
5. Test the off rule by sitting still in the garage with the TV on. The lights should stay on.

## How I do it in webCoRE

This is a real piston I run on Hubitat.

1. The piston subscribes to both garage door sensors, the garage and loft motion sensors, and the TV plug's power.
2. When either door opens or motion is detected, and the lights are off, it sets them to 80%.
3. For turning off, it uses webCoRE's "stays" conditions. Both doors must stay closed for 2 minutes, both motion sensors must stay inactive for 10 minutes, and the TV power must stay under 30 W for 30 seconds. Only when all of those are true does it turn the lights off.
4. When the TV power rises above 70 W, it dims the lights to 25% and sets a movie mode variable to true.
5. When the TV power stays under 30 W for 5 seconds and the variable is true, it sets the lights back to 80% and clears the variable.

## Advanced features

### Close the garage door too

Pair this with [safer automatic garage closing](/automation/security/garage-auto-close.html) so an empty garage gets its door closed as well as its lights turned off.

### Daytime brightness

Use a lower level during the day if the garage gets natural light through windows or open doors.

## Failure modes

- **Lights turn off during a movie:** The TV draw may dip under 30 W on dark scenes. Lower the off threshold or lengthen the 30 second wait.
- **Lights dim when the TV shows a menu:** The menu may draw more than 70 W. Raise the movie threshold based on your measurements.
- **Lights never turn off:** One of the three signals is stuck. Check each door sensor, both motion sensors, and the TV plug in the hub's device list.
- **Opening a door changes the lights someone set:** Make sure the "lights are off" condition is on the turn-on rule.

## FAQ

### Why check the TV power before turning the lights off?

Someone watching TV sits still, so motion sensors stop seeing them. The TV's power draw tells the automation someone is still using the space.

### Why two power thresholds, 70 W and 30 W?

The gap keeps the lights from flickering between modes when the TV's draw moves around. Above 70 W means a movie is on. Under 30 W means the TV is off or in standby.

### Why only turn the lights on if they were off?

If someone already set the lights to a different level, opening a door should not override that choice.

## Related recipes

- [Dim lights when the TV turns on](/automation/entertainment/tv-dim-lights.html)
- [Turn lights on with motion sensors](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Garage door left-open alerts](/automation/security/garage-door-notification.html)

{% include page-navigation.html
  left_url="/automation/lighting/"
  left_label="Back to lighting"
  right_url="/automation/"
  right_label="View all automations"
%}
