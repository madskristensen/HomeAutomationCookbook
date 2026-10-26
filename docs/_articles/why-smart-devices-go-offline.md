---
layout: guide
title: Why smart devices go offline
description: A checklist when a sensor, plug, or bulb stops responding. Check power, batteries, signal, and the hub before you replace anything.
date: 2026-10-26
last_modified_at: 2026-10-26
image: /assets/img/social/guides/why-smart-devices-go-offline.png
---

# Why smart devices go offline

{% include content-hero.html src="/assets/img/social/guides/why-smart-devices-go-offline.svg" alt="A checklist for a smart device that stopped responding" %}

A device that goes offline usually has a boring cause. It lost power, its battery got weak, it lost its path to the hub, or the hub itself had a bad moment. The fix is rarely a new device.

## The short answer

| What you see | Usual cause | Check this first |
|---|---|---|
| One battery sensor stopped reporting | Weak battery or cold location | Replace the battery, even if it still shows some charge |
| A bulb shows offline | Someone turned off the wall switch | The switch, then [bulbs vs. switches](/articles/smart-bulbs-vs-smart-switches-power-outages.html) |
| Several devices in one area dropped | A weak spot in the mesh or Wi-Fi | A nearby powered device that was unplugged or moved |
| Everything dropped at once | The hub, router, or internet | Restart order and power for the hub and router |
| A device works, then drops at the same time each day | Interference or a scheduled restart | What else runs at that time |

Change one thing. Wait a day. Then change the next thing.

## Power comes first

A smart bulb with its wall switch turned off has no power. It cannot answer. This is the most common offline device in a house with guests or kids. A switch guard or a smart switch fixes the habit better than a rule does.

Plugs and powered sensors drop when a power strip gets turned off, or a breaker trips. After an outage, some devices take a while to rejoin. Give them time before you start pairing again.

## Batteries fade before they die

Battery sensors often report a charge that looks fine and then stop. Cold garages, freezers, and outdoor spots drain batteries faster. A sensor that misses a few check-ins is often a battery problem before the level says so.

Replace the battery first. It is cheap and quick. [Smart home low-battery alerts](/automation/notifications/low-battery-alerts.html) can warn you before the next one goes quiet.

## Signal and the mesh

Zigbee, Z-Wave, and Thread devices pass messages through powered devices nearby. If you unplug a plug that was a stepping stone, devices behind it can lose their path. Metal boxes, appliances, and thick walls block signal too.

Look at what changed near the dropped devices. A moved plug, a new fridge, or a closed metal cabinet is a common answer. Adding a powered device between the hub and the far end of the house often helps more than anything else.

For Wi-Fi devices, a router change is the usual cause. A new network name, a new password, or a band setting can strand every Wi-Fi device at once.

## The hub and the internet

When everything drops at the same time, look at the center. A hub that ran out of storage, a router that rebooted, or an internet outage can look like many failed devices.

Cloud-only devices stop working when the internet does. A hub that runs rules locally, such as Home Assistant, Hubitat, Homey, or HomeSeer, keeps local devices working through an outage. Apple Home, Google Home, and Alexa can also run some devices locally through a home hub, depending on the device. Local control is worth preferring for the rooms you rely on most.

Put the hub and router on a small battery backup if outages are common where you live.

## Make offline visible

A device that drops quietly is worse than one that drops loudly. A motion light that misses one report fails in a small way. A leak sensor that went silent can fail when it matters.

Treat missing data as unknown, not as safe. Show offline devices on a single status view, such as [a house status check on demand](/automation/notifications/house-status-on-demand.html). Send an alert when a safety sensor has not checked in for longer than it normally would.

## Failure modes

- **A bulb is offline every evening:** Someone is using the wall switch. Guard the switch or replace it with a smart switch.
- **A freezer or garage sensor keeps dropping:** Cold drains the battery. Use a battery rated for the cold, or a sensor with a wired probe so the radio stays outside.
- **Devices at the far end of the house drop together:** Add a powered device in between to strengthen the mesh.
- **Every Wi-Fi device dropped after a router change:** Match the old network name and password, or rejoin each device.
- **A rule treated a dead sensor as all clear:** Change the rule so missing data counts as unknown.

## FAQ

### Should I re-pair a device as soon as it goes offline?

No. Check power and the battery first. Re-pairing can break automations that point to the old device.

### Why did many devices drop after a power outage?

Hubs and devices restart in a different order, and some take a while to rejoin. Give them time. If a few stay offline, power cycle them one at a time.

### Is local control really more reliable?

It removes the internet as a point of failure for local devices. The hub, the power, and the radio signal still have to work.

## Related guides and recipes

- [Smart home low-battery alerts](/automation/notifications/low-battery-alerts.html)
- [House status check on demand](/automation/notifications/house-status-on-demand.html)
- [Smart bulbs vs. smart switches after a power outage](/articles/smart-bulbs-vs-smart-switches-power-outages.html)
- [Monitor freezer temperature and outbuilding power](/automation/notifications/freezer-temperature-power-loss.html)
- [Water leak detection alerts](/automation/security/water-leak-response.html)
- [Choose smart-home devices and gear](/getting-started/device-guide.html)
