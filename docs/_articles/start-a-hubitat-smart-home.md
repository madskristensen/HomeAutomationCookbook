---
layout: guide
title: "Start a Hubitat smart home: a beginner's guide"
description: Start Hubitat home automation with a local Zigbee and Z-Wave hub. Set up the hub, add one light, build your first rule, then add a sensor that reacts.
date: 2026-11-05
last_modified_at: 2026-11-05
image: /assets/img/social/platform-hubitat.png
---

# Start a Hubitat smart home

{% include content-hero.html src="/assets/img/social/platform-hubitat.svg" alt="A Hubitat hub connects Zigbee and Z-Wave devices with local automation rules" %}

You can start Hubitat home automation with one local hub, one smart light, and one simple rule. Hubitat Elevation includes Zigbee and Z-Wave radios, so many sensors, switches, and bulbs talk to the hub without needing a separate radio stick. This guide walks through setup, your first device, and your first automation one small step at a time.

Hubitat is my current platform. I moved to it during a whole-house remodel after SmartThings, when I wanted faster local rules and more room for detailed logic. The path below is the beginner path I wish I had on day one: place the hub well, add one light you can undo, then let a sensor react.

## Step 1: Set up the hub

Hubitat Elevation is a small box that runs your automations on your home network. Current C-8 kits include the hub with built-in Zigbee and Z-Wave radios, antennas, Ethernet and USB-C power cables, and a Get Started card. Older C-7 hubs use micro-USB and do not have external antennas.

Place the hub near the center of your home, away from large metal objects, and keep at least about a foot of space from your Wi-Fi router so the 2.4 GHz Zigbee radio is not drowned out. A wired Ethernet connection is the most reliable choice. Hubitat does not support Power over Ethernet, so do not plug the hub into a PoE port.

1. Connect Ethernet to your router (or use Wi-Fi on C-8 and later if a cable is not possible).
2. Power the hub with the included adapter. The front light is blue while it boots and turns green when it is ready.
3. On a computer or phone on the same home network, open findmyhub.hubitat.com, or start at go.hubitat.com and follow the prompts. Guest Wi-Fi isolation can hide the hub, so use your main LAN.
4. Choose Get Started, agree to the terms, name the hub, and set your location or postal code so sunrise and sunset times are correct.
5. Create or sign in to a Hubitat account, then register the hub so the mobile app and cloud features can work later.

Bookmark the hub's local IP address from the browser bar. That is the fastest way back into the admin interface after setup.

**What will be working:** the hub shows green, you can open its Main Menu from your LAN, and it is registered to your account.

## Step 2: Add one smart light

Start with a single light you use every day. A light is easy to test and easy to undo, so it is a gentle first device.

- A **smart bulb** screws into a lamp. Leave that lamp's wall switch on so the bulb keeps power.
- A **smart switch** or dimmer replaces a wall switch. It is a better long-term choice for ceiling lights because the paddle still works for everyone. Installing one means household wiring, so use a qualified electrician if you are not sure.

Prefer Zigbee or Z-Wave devices that Hubitat lists as compatible, then add them from **Devices**, then **Add Device**. You can find by device type or brand, or add Zigbee or Z-Wave manually and put the device into pairing or inclusion mode. For some Z-Wave devices that use S2 security, the hub may ask you to confirm a short code from a sticker on the device or its packaging.

**What will be working:** the light appears on the Devices page, you can turn it on and off from the hub, and the normal switch or lamp still works when someone wants it.

## Step 3: Build your first rule

Hubitat includes several automation apps. For a first light, stay simple:

- **[Basic Rules](https://docs2.hubitat.com/en/apps/basic-rules)** for a clear when-this-happens, do-that path, with common waits and restrictions.
- **[Room Lighting](https://docs2.hubitat.com/en/apps/room-lighting)** when the job is lighting with motion or contact activation, delayed off, and overrides.

Open **Apps**, add Basic Rules or Room Lighting, and name the automation after the household outcome, such as "Hall lamp at sunset." A good first rule is a schedule or sunset trigger that turns on the lamp before you usually get home. Live with it for a few days before adding conditions.

Save Rule Machine and webCoRE for later. They are powerful when a job needs remembered state or branches, but they are easier to maintain after one simple rule already works.

**What will be working:** the lamp turns on by itself at the time or sunset you chose. If anything feels wrong, you can pause or remove the app and the light still works from the switch.

## Step 4: Add one sensor and let the house react

Once a schedule works, add a sensor. A **motion sensor** notices movement. A **contact sensor** notices when a door or drawer opens. Pair it the same way as the light, then confirm the hub shows the open, closed, or motion events you expect before you build a rule on them.

Good first sensor recipes on this site:

{% assign hubitat_recipes = "/automation/lighting/lights-on-motion.html,/automation/lighting/lights-off-after-motion.html,/automation/lighting/bathroom-night-light.html,/automation/lighting/toggle-lights-door.html" | split: "," %}
<div class="card-grid">
{% for u in hubitat_recipes %}
{% assign recipe = site.pages | where: "url", u | first %}
{% if recipe %}
{% include automation-card.html url=recipe.url title=recipe.title description=recipe.description %}
{% endif %}
{% endfor %}
</div>

On Hubitat, Room Lighting is usually the starting point for those lighting jobs. For a garage left-open alert later, Basic Rules or the Notifications app can wait until the door stays open, then notify. For Away and arrival, Mode Manager can change a shared household mode that other rules watch.

**What will be working:** a light turns on when you walk in or open a door, and you can still use the wall switch when someone wants manual control.

## Keep it friendly for the whole household

- Keep a normal switch for every light. Automations are a bonus, not the only way in.
- Change one thing at a time, and live with it for a few days.
- Tell the family what the new rule does, so nobody is surprised.
- Treat a sensor that stops reporting as unknown, not as proof a room is empty.
- Test with the internet disconnected once. Hubitat apps run on the hub, but phone push, voice assistants, and cloud integrations can still fail on their own path.

## Where to go next

When the basics feel easy, the [Hubitat home automation guide](/platforms/hubitat.html) covers which built-in app fits which job, local versus cloud behavior, and how recipes map to Hubitat tools.

If you are choosing between hubs, [Hubitat vs SmartThings for a family house](/articles/hubitat-vs-smartthings-family-house.html) compares both from a large family home. For device picks that work across Zigbee and Z-Wave, see the [device guide](/getting-started/device-guide.html).
