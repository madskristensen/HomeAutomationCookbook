---
layout: guide
title: Starter house setup guide
description: A practical plan for a first smart home. Pick one hub, buy about 10 devices, and set them up room by room with recipes that keep switches working for everyone.
date: 2026-10-25
last_modified_at: 2026-10-25
image: /assets/img/social/guides/starter-house-setup.png
---

# Starter house setup guide

{% include content-hero.html src="/assets/img/social/guides/starter-house-setup.svg" alt="A room-by-room starter plan with one hub and about ten devices" %}

This is a concrete plan for the first few weekends of a smart home. One hub, about 10 devices, and one working recipe per room.

It builds on [getting started](/getting-started/), which explains the mindset, and the [device guide](/getting-started/device-guide.html), which lists the products I have used. This page turns both into an order of work.

## The rules for a starter house

- **One hub.** Do not mix three apps on day one.
- **Local first.** Prefer Z-Wave and Zigbee devices that keep working when the internet is down.
- **Switches still work.** Every light keeps a normal wall control.
- **One room at a time.** Finish a room, live with it for a week, then move on.
- **No risky jobs yet.** Leave locks, heaters, and garage door control for later.

## Step 1: Pick the hub

I run Hubitat. It runs automations on the hub itself, supports Z-Wave and Zigbee, and lets me build simple rules or detailed ones later. SmartThings is a reasonable alternative, especially if you already own Samsung devices. Read [choose the right platform](/getting-started/choose-the-right-platform.html) and [Hubitat vs SmartThings for a family house](/articles/hubitat-vs-smartthings-family-house.html) before buying.

Set up the hub, give it a fixed IP address on your router, and turn on its backups.

## Step 2: The first 10 devices

This list covers four rooms and the whole-house basics. Every product here is one I have used. Pick the "good enough" option or the step up from the [device guide](/getting-started/device-guide.html#products-i-have-used).

| # | Device | Room | First recipe |
|---|---|---|---|
| 1 | Motion sensor ([Aeotec SmartThings Motion Sensor](https://www.amazon.com/dp/B095TZTGNB/ref=nosim?tag=madsk0f-20)) | Hallway or laundry | [Lights on motion](/automation/lighting/lights-on-motion.html) |
| 2 | Smart switch ([Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20)) | Same room | [Lights off after motion](/automation/lighting/lights-off-after-motion.html) |
| 3 | Bathroom multisensor ([Aeotec TriSensor 8](https://www.amazon.com/dp/B0D47WR1S2/ref=nosim?tag=madsk0f-20)) | Bathroom | [Bathroom night-light](/automation/lighting/bathroom-night-light.html) |
| 4 | Smart dimmer ([TP-Link Tapo S505D](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20)) | Bathroom or living room | [Bathroom night-light](/automation/lighting/bathroom-night-light.html) |
| 5 | Power-metering switch ([Zooz ZEN15](https://www.amazon.com/dp/B07578W7KY/ref=nosim?tag=madsk0f-20)) | Laundry | [Washer done alert](/automation/appliances/washer-done-notification.html) |
| 6 | Vibration sensor ([THIRDREALITY Zigbee Vibration Sensor](https://www.amazon.com/dp/B0C9DP249C/ref=nosim?tag=madsk0f-20)) | Laundry | [Dryer done alert](/automation/appliances/dryer-done-notification.html) |
| 7 | Leak sensor ([THIRDREALITY WL2](https://www.amazon.com/dp/B0GK19F6Z2/ref=nosim?tag=madsk0f-20)) | Water heater or under sink | [Water leak alerts](/automation/security/water-leak-response.html) |
| 8 | Leak sensor (second one) | Washer or dishwasher | [Water leak alerts](/automation/security/water-leak-response.html) |
| 9 | Contact sensor ([SONOFF SenseGuard Gen2](https://www.amazon.com/dp/B0GKFB3XCL/ref=nosim?tag=madsk0f-20)) | Closet or pantry door | [Turn lights on when a door opens](/automation/lighting/toggle-lights-door.html) |
| 10 | Garage tilt sensor ([THIRDREALITY Garage Tilt Sensor](https://www.amazon.com/dp/B0CZP2CJXF/ref=nosim?tag=madsk0f-20)) | Garage | [Garage door left-open alerts](/automation/security/garage-door-notification.html) |

Amazon product links on this page are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html) for details.

Mixing Zigbee and Z-Wave is fine. Mains-powered switches and plugs act as repeaters and make the mesh stronger, so install those before the battery sensors in far rooms.

## Step 3: Room by room

### Weekend 1: Hallway or laundry lights

Install the switch, then the motion sensor. Build [lights on motion](/automation/lighting/lights-on-motion.html). Live with it for a week before adding [lights off after motion](/automation/lighting/lights-off-after-motion.html).

Before mounting the sensor, read [motion sensor placement](/articles/motion-sensor-placement.html). Most "it does not work" problems are placement.

### Weekend 2: Laundry alerts

Put the ZEN15 on the washer and a vibration sensor on the dryer. Run three loads with logging only, then turn on notifications. The [power-monitoring plug guide](/articles/best-power-monitoring-plugs-appliance-alerts.html) explains which device fits which appliance.

On Hubitat, my [Appliance Cycle Monitor](https://github.com/madskristensen/hubitat-drivers/tree/main/apps/appliance-cycle-monitor) app handles the running and finished states for you.

### Weekend 3: Bathroom

Add the multisensor and a dimmer. Start with a dim [night-light](/automation/lighting/bathroom-night-light.html). If you want the fan to run on its own later, read [best humidity sensors for shower fan automation](/articles/best-humidity-sensors-shower-fan.html) and then the [shower fan recipe](/automation/climate/fan-shower.html).

### Weekend 4: Safety and status

Place the leak sensors where water shows up first: under the water heater, behind the washer, under the kitchen sink. Add the closet or pantry contact sensor and the garage tilt sensor. Then set up [low-battery alerts](/automation/notifications/low-battery-alerts.html) so a sensor never goes quiet without anyone knowing.

## Step 4: Add modes, then routines

Once the devices work on their own, add home modes. Day, Evening, Night, and Away are enough. Then build:

- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)

Modes make every later recipe simpler, because rules can check one mode instead of five conditions.

## What to skip in the first month

- **Smart locks and auto-closing garage doors.** Get alerts working first.
- **Plugs on heaters or cooking appliances.** Not safe for general-purpose plugs.
- **Voice-only control.** Fine as an extra, not as the only way to turn on a light.
- **Bundles of cheap devices.** Test one, then buy more of what works.

## A starter checklist

- [ ] Hub installed, fixed IP, backups on
- [ ] Switches and plugs paired before far battery sensors
- [ ] Every device named by room and job (for example, "Laundry Washer Power")
- [ ] One recipe per room, watched for a week
- [ ] Leak and low-battery alerts tested with a real wet towel and a weak battery
- [ ] Someone else in the house knows how the lights work without the app

{% include pdf-guide-promo.html variant="buy" %}

## Next steps

- [Practical home automation tips](/getting-started/tips.html)
- [Choose smart-home devices and gear](/getting-started/device-guide.html)
- [Browse all recipes](/automation/)

{% include page-navigation.html
  left_url="/getting-started/"
  left_label="Back to getting started"
  right_url="/getting-started/device-guide.html"
  right_label="Choose devices and gear"
%}
