---
layout: guide
title: Best humidity sensors for shower fan automation
description: Pick a humidity sensor that reacts fast enough to run a bathroom exhaust fan when the shower starts, works locally with your hub, and lets the fan stop once the room dries.
date: 2026-10-25
last_modified_at: 2026-10-25
image: /assets/img/social/guides/best-humidity-sensors-shower-fan.png
pdf_promo_card: true
---

# Best humidity sensors for shower fan automation

{% include content-hero.html src="/assets/img/social/guides/best-humidity-sensors-shower-fan.svg" alt="Humidity sensors compared for starting a bathroom fan when a shower begins" %}

A shower fan automation lives or dies on one thing: how fast the sensor notices the shower. A sensor that reports every 10 minutes will turn the fan on after the mirror is already fogged.

Most "best humidity sensor" lists rate accuracy and app polish. For this job, reporting speed and placement matter more. This guide explains what to look for, then gives picks by setup. Every smart sensor named below is one I have bought and used.

## The short answer

| Setup | Pick | Why |
|---|---|---|
| Z-Wave, want fast and tunable | [Zooz ZSE44 800LR Temperature/Humidity XS Sensor](https://www.amazon.com/dp/B0B3G9Z4LJ/ref=nosim?tag=madsk0f-20) | Small, battery powered, and humidity reporting is configurable. |
| Zigbee, low cost | [THIRDREALITY Zigbee Temperature and Humidity Sensor Lite](https://www.amazon.com/dp/B0D2NVJTS3/ref=nosim?tag=madsk0f-20) | Simple and inexpensive. Good to test the idea in one bathroom. |
| One device for motion, humidity, and light | [Aeotec TriSensor 8](https://www.amazon.com/dp/B0D47WR1S2/ref=nosim?tag=madsk0f-20) | The sensor I use for the humidity trigger in my shower fan recipe. |
| Z-Wave multisensor with more readings | [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY/ref=nosim?tag=madsk0f-20) | Motion, humidity, temperature, and light in one place. |
| No hub at all | A humidity-sensing fan wall switch | Purpose-built, no automation to maintain. |

Amazon product links on this page are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html) for details.

## What to look for

### 1. Reporting on change, not on a long timer

This is the big one. Look for a sensor whose humidity report can be set to trigger on a small change, such as 2 to 5 percent. Some sensors only check in on a fixed interval. That is fine for a living room, but too slow for a shower.

Check the driver on your hub too. The sensor may support fast reporting while the default driver does not let you set it.

### 2. Local pairing with your hub

Zigbee and Z-Wave sensors pair directly to a local hub such as Home Assistant, Hubitat, SmartThings, or Homey. The fan then reacts even if the internet is down. Wi-Fi sensors with a cloud app can add delay and a dependency you do not need.

### 3. A mounting spot it can survive

The best spot is near the shower but out of direct spray. Most of these sensors are not waterproof. Read the operating range on the product page and keep the sensor out of the splash zone.

### 4. Battery life you can live with

Faster reporting uses more battery. A sensor that reports often and runs a year or more on a battery is worth more than one with better accuracy that needs a new battery every few months.

## Picks in more detail

### Zooz ZSE44: the fast, tunable Z-Wave pick

[Zooz ZSE44 800LR Temperature/Humidity XS Sensor](https://www.amazon.com/dp/B0B3G9Z4LJ/ref=nosim?tag=madsk0f-20)

It is small, so it is easy to mount high on a bathroom wall. Its humidity reporting threshold is configurable, which is what this job needs. Hubitat community users who have tried many sensors for a shower fan often land on this one for the same reason.

### THIRDREALITY Temperature and Humidity Sensor Lite: the budget Zigbee pick

[THIRDREALITY Zigbee Temperature and Humidity Sensor Lite](https://www.amazon.com/dp/B0D2NVJTS3/ref=nosim?tag=madsk0f-20)

A good way to test the automation in one bathroom before spending more. Watch a few showers in the hub's event log. If it reacts within a minute or two of the water starting, it is fast enough.

### Aeotec TriSensor 8: one sensor for motion, humidity, and light

[Aeotec TriSensor 8](https://www.amazon.com/dp/B0D47WR1S2/ref=nosim?tag=madsk0f-20)

This is the sensor I use for the humidity trigger in my [shower fan recipe](/automation/climate/fan-shower.html). The extra motion and light readings are useful for a [bathroom night-light](/automation/lighting/bathroom-night-light.html) in the same room. Use it where the extra readings help, not where the fastest motion response matters most.

### Zooz ZSE11 Q Sensor: a Z-Wave multisensor alternative

[Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY/ref=nosim?tag=madsk0f-20)

Similar idea to the TriSensor on Z-Wave Long Range. It works well if you want one device per bathroom covering motion and humidity.

### No hub: a humidity-sensing fan switch

If you do not want a hub involved, a wall switch with a built-in humidity sensor replaces the fan switch. For example, the Lutron XactSense switch can turn on for a rapid rise in humidity and has adjustable timeouts, according to its [spec sheet](https://assets.lutron.com/a/documents/3691321_eng.pdf). I have not used it. It needs the right wiring for your fan, and it does not give your hub any data.

## Use the rise, not a fixed number

A fixed rule such as "fan on above 70 percent" breaks with the seasons. Bathroom humidity on a wet winter day can sit near that number with no shower at all.

A better rule:

- **Turn on** when humidity rises a set amount above the recent baseline, for example 8 to 10 points within a few minutes.
- **Turn off** when humidity is back within a few points of the baseline and has stayed there for several minutes.
- **Cap the run time** so a stuck sensor cannot run the fan all day.

Hubitat's built-in rule tools and webCoRE can both compare current humidity to a stored baseline. Record a few normal showers first and pick numbers from what you see.

## When humidity is not the best trigger

Some people find every humidity sensor too slow, especially in a large bathroom with a strong fan. Two faster signals are worth trying:

- **The shower light.** If the shower has its own light, its switch turning on is an instant trigger. Use humidity only to decide when to stop.
- **Motion or presence in the shower area.** A sensor mounted high and aimed at the shower can start the fan right away. Read [PIR vs mmWave presence sensors](/articles/pir-vs-mmwave-presence.html) and [motion sensor placement](/articles/motion-sensor-placement.html) first.

## Do not forget the fan switch

The sensor only tells the hub to act. The fan still needs a smart switch rated for a fan motor, and the physical paddle should keep working for guests. I do not have a personally verified fan switch pick yet, so check the switch's motor rating and wiring needs before buying.

## FAQ

### How fast should a humidity sensor report for a shower fan?

Fast enough that the fan starts within a minute or two of the shower. Set humidity reporting to a small change (2 to 5 percent) rather than a long interval, and confirm it in the hub's event log.

### Where should I mount the sensor?

High on a wall near the shower, out of direct spray, and away from the fan intake so it does not read dry air too early.

### Do these sensors need the cloud?

No. The Zigbee and Z-Wave sensors here pair directly to a local hub such as Home Assistant, Hubitat, SmartThings, or Homey and report locally.

{% include pdf-guide-promo.html %}

## Related

- [Turn on the bathroom fan when a shower starts](/automation/climate/fan-shower.html)
- [Play music when a shower starts](/automation/entertainment/shower-music.html)
- [Best power-monitoring plugs for washer, dishwasher, and TV alerts](/articles/best-power-monitoring-plugs-appliance-alerts.html)
- [Starter house setup guide](/getting-started/starter-house-setup.html)
- [Choose smart-home devices and gear](/getting-started/device-guide.html)

{% include page-navigation.html
  left_url="/articles/"
  left_label="Back to articles"
  right_url="/automation/climate/"
  right_label="Climate automations"
%}
