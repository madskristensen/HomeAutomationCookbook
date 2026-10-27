---
layout: guide
title: "Start an Alexa smart home: a beginner's guide"
description: Start Alexa home automation with an Echo you may already own. See which Echo models act as a smart home hub, what to buy first, and your first routine.
date: 2026-10-27
last_modified_at: 2026-10-27
image: /assets/img/social/platform-alexa.png
---

# Start an Alexa smart home

{% include content-hero.html src="/assets/img/social/platform-alexa.svg" alt="Alexa connects voice control with smart bulbs, a Zigbee hub, and smart switches" %}

You can start Alexa home automation with one Echo speaker, one smart light, and one routine. Many Echo models already have a smart home hub built in, so you may not need to buy a separate hub at all. This guide walks you through it one small step at a time.

Alexa was my own first smart home. I started with smart bulbs, then got an Echo with a built-in Zigbee hub, then added smart light switches. That order worked well, and it is the path below.

## Step 1: Check what your Echo can connect to

An Echo is Amazon's smart speaker or smart display. Every current Echo can control devices over Wi-Fi. Some models also have a built-in hub, which is a small radio that talks directly to low-power smart devices.

There are two hub features to look for:

- **Zigbee.** Zigbee is a low-power wireless standard used by many bulbs, plugs, switches, sensors, and locks. A Zigbee device needs a hub, and some Echo models are that hub.
- **Matter.** Matter is a newer standard that lets devices from different brands work with several platforms. Many Echo models can add Matter devices. Matter devices that use Thread, a low-power network, also need a Thread border router, which some Echo models include.

According to Amazon's developer documentation, these Echo models have a built-in Zigbee hub and a Thread border router:

| Echo model | Zigbee hub | Thread border router |
|---|---|---|
| Echo (4th Gen) | Yes | Yes |
| Echo Dot Max (2025) | Yes | Yes |
| Echo Hub (a wall-mounted smart home control screen) | Yes | Yes |
| Echo Plus (2nd Gen) | Yes | Yes |
| Echo Show 21, Show 15 (2nd Gen), Show 11 (2025), Show 10 (3rd Gen), Show 8 (3rd Gen, 2025) | Yes | Yes |
| Echo Studio (2025) | Yes | Yes |

A regular Echo Dot or Echo Pop can still add Matter devices over Wi-Fi, but it is not a Zigbee hub. Some eero Wi-Fi routers, which Amazon also makes, have the same hub features.

**Watch out for Z-Wave.** Z-Wave is another common smart home radio. Amazon lists Zigbee, Matter, and Thread as the built-in options, not Z-Wave, so Z-Wave devices need a hub like Hubitat or SmartThings that then connects to Alexa.

**What will be working:** you will know whether your Echo can be your hub, or whether to shop for devices that connect over Wi-Fi or Matter instead.

## Step 2: Add one smart light

Start with a single light you use every day. A light is easy to test and easy to undo, so it is a gentle first device.

- **A smart bulb** screws into a lamp. It is the easiest start. It works best in a lamp that is always left switched on at the wall.
- **A smart switch** replaces a wall switch. It is a better long-term choice for ceiling lights, because the wall switch keeps working for everyone. Installing one means working with household wiring, so use a qualified electrician if you are not sure.

Before you buy, check the box for "Works with Alexa," Zigbee, or Matter, and match it to what your Echo supports from step 1. To add it, open the Alexa app and follow the steps to add a device, or say "Alexa, discover my devices" for a Zigbee device.

**What will be working:** you can say "Alexa, turn on the living room lamp," and the light responds. The normal switch still works too.

## Step 3: Build your first routine

A routine is how Alexa automates things for you. Each routine has a **When** part, the event that starts it, and one or more actions that Alexa then runs.

In the Alexa app, go to **More**, then **Routines**, then the plus button. Menu names can differ slightly depending on your app version. Choose what starts the routine, add an action, and save. Common starting events are:

- **A phrase you say**, such as "Alexa, good night."
- **A schedule**, such as every weekday at 6:30 in the evening.
- **A smart home device**, such as a motion sensor detecting motion or a door sensor opening.
- **Your location**, when your phone arrives at or leaves a place. Location triggers use the phone with the Alexa app and location turned on. Check how it works for other people in your household.

You can also pause between actions. Tap **Add action**, then **Wait**, and choose how long, up to 4 hours. For example, turn a hallway light on, wait a few minutes, then turn it off again.

A good first routine is a schedule that turns on a lamp before you usually get home. It runs at a time you choose, so it is easy to check.

**What will be working:** the lamp turns on by itself at the time you chose. If anything goes wrong, you can switch the routine off in the app and the light works normally again.

## Step 4: Add one sensor and let the house react

Once a schedule works, try a sensor. A **motion sensor** notices movement. A **contact sensor** is a small two-piece sensor that notices when a door or drawer opens.

Pick one that pairs with your Echo, often a Zigbee sensor if your Echo is a Zigbee hub. Then check that it appears as a choice under **When** in a new routine. A device can show up in the Alexa app but still not be offered as a routine trigger, so this check matters.

Good first sensor routines are on this site:

{% assign alexa_recipes = "/automation/lighting/lights-on-motion.html,/automation/lighting/lights-off-after-motion.html,/automation/lighting/bathroom-night-light.html,/automation/lighting/toggle-lights-door.html" | split: "," %}
<div class="card-grid">
{% for u in alexa_recipes %}
{% assign recipe = site.pages | where: "url", u | first %}
{% if recipe %}
{% include automation-card.html url=recipe.url title=recipe.title description=recipe.description %}
{% endif %}
{% endfor %}
</div>

**What will be working:** a light turns on when you walk in or open a door, and the wall switch still works when someone wants it.

## Keep it friendly for the whole household

- Keep a normal switch for every light. Voice and routines are a bonus, not the only way in.
- Change one thing at a time, and live with it for a few days.
- Tell the family what the new routine does, so nobody is surprised.
- Treat a sensor that stops reporting as unknown, not as proof a room is empty.

Alexa Guard, the old built-in "away" listening feature, was discontinued in January 2024. Home and Away modes and away lighting are still part of the Alexa app. Smoke and carbon monoxide alarm detection moved to a paid service called Alexa Emergency Assist. Do not rely on any of these as a replacement for real smoke alarms or a monitored security system.

## Where to go next

When the basics feel easy, the [Alexa automation guide](/platforms/alexa.html) covers what routines can and cannot do, the local and cloud limits, and more recipes that fit Alexa.
