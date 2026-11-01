---
cta_category: security
layout: guide
title: "Garage door left open sensor: what to buy and where to mount it"
description: Pick a garage door left open sensor that fits your door and hub, mount it where it reads open and closed reliably, and get an alert when it stays open.
date: 2026-11-01
last_modified_at: 2026-11-01
image: /assets/img/social/guides/garage-door-left-open-sensor.png
---

# Garage door left open sensor: what to buy and where to mount it

{% include content-hero.html src="/assets/img/social/guides/garage-door-left-open-sensor.svg" alt="A garage door with a tilt sensor on the top panel and a phone alert that the door is still open" %}

To know when the garage door is left open, add a sensor that reports open and closed to your hub. A tilt sensor on the top door panel is the easiest choice for most sectional doors. Then set an alert for when the door stays open too long. The [garage door left open alert recipe](/automation/security/garage-door-notification.html) has the full rule.

## The short answer

| Your setup | Good fit | Mount it |
|---|---|---|
| Sectional door that rolls up | Tilt sensor | On the inside of the top panel |
| Door that swings up in one piece | Tilt sensor | On the door, where it tips past level when open |
| You want app control too | Smart garage controller | Wired to the opener, as its instructions say |
| Side door or other hinged door | Contact sensor | On the frame, magnet on the door |

Pick one that works with your hub or app. Check the listing for the radio type your hub supports, such as Zigbee, Z-Wave, Matter, or Wi-Fi.

## Three kinds of sensor

### Tilt sensor

A tilt sensor reports open when it tips past a set angle. On a sectional door, the top panel goes from upright to flat as the door opens, so that panel is where it belongs. It does not touch the opener. It runs on a battery.

### Contact sensor

A contact sensor has two parts. It reports open when the magnet moves away from the sensor. It suits hinged doors well. On a garage door, the gap and the movement can be hard to line up, so a tilt sensor is usually simpler.

### Smart garage controller

A controller connects to the opener. It reports the door state and can also open or close it from an app. If you only want an alert, you do not need one. If you do want remote closing, read [close a garage safely after an open-door alert](/automation/security/garage-auto-close.html) first.

## Where to mount it

- **Tilt sensor:** the top door panel, on the inside, in the middle. Follow the arrow or orientation mark on the sensor.
- **Away from the rails and rollers:** nothing should hit it as the door moves.
- **Within range of the hub:** a detached or far garage may need a repeater, such as a plugged-in device on the same radio type.
- **Easy to reach:** you will change the battery someday.

## Test it before you trust it

1. Open the door all the way and check the state in your app.
2. Close it and check again.
3. Stop the door halfway. Note what it reports. A tilt sensor may say open or closed depending on the angle.
4. Repeat a few times over a day, including in cold weather if you can.

## Then set the alert

Once the sensor reports reliably, add the rule. Send an alert when the door has been open for about 10 to 15 minutes, plus a check at bedtime. Keep it alert-only. The [garage door left open alert recipe](/automation/security/garage-door-notification.html) walks through it.

## Failure modes

- **Wrong state:** Recheck the mounting angle or the magnet gap, then the battery.
- **Sensor drops offline:** Move it, or add a repeater between the hub and the garage.
- **Alert after the door closed:** The sensor reported late. Make the rule check that the door is still open before it alerts.
- **Unknown state:** Treat it as not closed, and alert anyway.

## FAQ

### Do I need a smart garage door opener to get an alert?

No. A battery tilt sensor on the door is enough for an open-door alert. A smart controller is only needed if you also want to open or close the door from an app.

### Where should a garage door tilt sensor go?

On the inside of the top panel of a sectional door. That panel moves from upright to flat, so the sensor sees a clear change between open and closed.

### Can the sensor close the door for me?

No. A sensor only reports. Closing needs a controller and opener built and approved for unattended closing. See the auto-close recipe for the precautions.

## Related guides and recipes

- [Garage door left open alarm and alerts](/automation/security/garage-door-notification.html)
- [Auto close a garage door safely after an alert](/automation/security/garage-auto-close.html)
- [Garage lights that follow doors, motion, and the TV](/automation/lighting/garage-lights-doors-motion-tv.html)
- [Why smart devices go offline](/articles/why-smart-devices-go-offline.html)
