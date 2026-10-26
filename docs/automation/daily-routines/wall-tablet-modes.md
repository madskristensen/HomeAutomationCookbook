---
layout: automation
date: 2026-10-25
title: Manage wall tablets with home modes
description: Wake, dim, mute, and turn off wall-mounted dashboard tablets when the home mode changes, and let one tablet double as a night guide to the bathroom.
keywords: wall tablet automation, Fully Kiosk Browser Hubitat, dashboard tablet brightness, Fire tablet night light, webCoRE tablet piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/daily-routines/wall-tablet-modes.png
compact: true
faqs:
  - question: Why not just leave the tablets on all the time?
    answer: A bright screen in a dark house at night is annoying, and a screen nobody is looking at while the house is empty wastes power and wears out the display.
  - question: What does Fully Kiosk Browser add?
    answer: It runs the dashboard full screen and lets the hub control the screen, brightness, volume, and start page over the local network.
  - question: Why reload the start page in the morning?
    answer: Dashboards sometimes get left on a different page or freeze overnight. Loading the start URL when the house wakes up puts every tablet back on the right screen.
products:
  - job: "Show the dashboard"
    body: "Wall-mounted tablets. I use an Amazon Fire tablet in the hallway and a second tablet in the kitchen."
  - job: "Control the screen from the hub"
    body: "[Fully Kiosk Browser](https://www.fully-kiosk.com/en/) on each tablet, with its Remote Admin feature turned on. On Hubitat, I wrote [a small Fully Kiosk driver](https://github.com/madskristensen/hubitat-drivers/tree/main/drivers/fully-kiosk) for this, but other community drivers exist too."
---

# Manage wall tablets with home modes

{% include content-hero.html src="/assets/img/social/recipes/daily-routines/wall-tablet-modes.svg" alt="Wall tablets follow the home mode from bright daytime dashboards to dim night screens" %}

Wall tablets are great during the day and too bright at night. This recipe ties each tablet to the home mode. In Home mode the screens are on and readable. At Night they go nearly dark and quiet. In Away mode the screens turn off. One tablet near the bedrooms also brightens when someone turns on a bathroom light, so it works as a soft night guide.

**Best for:** A home with one or more wall-mounted tablets running a dashboard in Fully Kiosk Browser, and a hub that already switches between Home, Night, and Away modes.

**Not for:** A tablet that also needs to work as a regular tablet, since kiosk mode locks it to one app.

## Why this exists

A dashboard tablet at full brightness lights up a hallway at 2 AM. A tablet nobody is home to look at still burns its screen all day. Adjusting them by hand is the kind of chore nobody does. Home modes already describe what the house is doing, so the tablets can follow along.

## Logic

<div class="automation-example">IF the home mode changes to Home
THEN turn each tablet screen on
AND load the dashboard start URL
AND set brightness to 65%

IF the home mode changes to Night
THEN mute each tablet
AND set the kitchen tablet to 1% brightness
AND set the hallway tablet to 1% brightness

IF the mode is Night
AND any bathroom light is on
THEN set the hallway tablet to 40% brightness

IF the mode is Night
AND all bathroom lights are off
THEN set the hallway tablet back to 1%

IF the home mode changes to Away
THEN turn each tablet screen off</div>

- **Trigger:** A home mode change, or a bathroom light changing while the mode is Night.
- **Conditions:** The bathroom guide behavior only runs in Night mode.
- **Action:** Screen on or off, load the start URL, set brightness, and mute.
- **Wait / timeout:** None.
- **Stop condition:** The next mode change sets the tablets to that mode's state.
- **Manual override:** Touching a tablet still works. Fully Kiosk's own settings can wake the screen on touch or motion.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Turn on Remote Admin in Fully Kiosk Browser and set a password. The hub talks to the tablet over the local network.
2. Give each tablet a fixed IP address in your router so the hub can always find it.
3. Set the dashboard as the Fully Kiosk start URL. That is the page the Home mode action loads.
4. Test 1% brightness in a dark room. Some screens are still bright at the lowest level, and some are nearly black.
5. Pick the bathroom lights that matter. I use all the bathroom lights near the bedrooms, so any of them turning on brightens the hallway tablet.

## How I do it in webCoRE

This is a real piston I run on Hubitat.

1. The piston triggers on location mode changes and on the bathroom lights changing.
2. When the mode changes to Home, it turns on the screen on both tablets, loads the start URL, and sets brightness to 65%.
3. When the mode changes to Night, it mutes both tablets. The kitchen tablet goes to 1%.
4. For the hallway Fire tablet in Night mode, it checks the bathroom lights. If all of them are off, the tablet stays at 1%. If any of them is on, it goes to 40%. Because the piston subscribes to the bathroom lights, this updates every time one turns on or off.
5. When the mode changes to Away, it turns off both screens.

The hallway tablet happens to face the path to the bathroom. At 40% it gives just enough light to walk by without turning on a ceiling light.

## Advanced features

### Wake on motion

Fully Kiosk can use the tablet camera to wake the screen when someone walks up. Combine it with the mode rules so the screen wakes during the day but not at night.

### Show a different page at night

Load a simpler night dashboard with only a few large tiles instead of the full daytime page.

## Failure modes

- **Nothing happens on mode change:** Check that the tablet still has the same IP address and that Remote Admin is on.
- **Tablet is still too bright at night:** Some screens have a high minimum brightness. Try Fully Kiosk's screen dimming options or a darker night page.
- **Hallway tablet stays bright after the bathroom:** Make sure every bathroom light is included in the check. One missing light can keep the "any on" condition true.
- **Screen does not come back in the morning:** Some tablets fall asleep deeply. Check Fully Kiosk's power and screen-off settings.

## FAQ

### Why not just leave the tablets on all the time?

A bright screen in a dark house at night is annoying, and a screen nobody is looking at while the house is empty wastes power and wears out the display.

### What does Fully Kiosk Browser add?

It runs the dashboard full screen and lets the hub control the screen, brightness, volume, and start page over the local network.

### Why reload the start page in the morning?

Dashboards sometimes get left on a different page or freeze overnight. Loading the start URL when the house wakes up puts every tablet back on the right screen.

## Related recipes

- [Bathroom night-light automation](/automation/lighting/bathroom-night-light.html)
- [Smart home status tiles](/automation/notifications/status-tiles.html)
- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)

{% include page-navigation.html
  left_url="/automation/daily-routines/"
  left_label="Back to daily routines"
  right_url="/automation/"
  right_label="View all automations"
%}
