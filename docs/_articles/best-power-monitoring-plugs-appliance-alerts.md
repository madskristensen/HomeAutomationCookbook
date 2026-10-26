---
layout: guide
title: Best power-monitoring plugs for washer, dishwasher, and TV alerts
description: Pick a power-monitoring plug or switch for washer, dishwasher, and TV alerts that works locally with your hub, plus what to use for a 240V dryer.
date: 2026-10-25
last_modified_at: 2026-10-25
image: /assets/img/social/guides/best-power-monitoring-plugs-appliance-alerts.png
pdf_promo_card: true
---

# Best power-monitoring plugs for washer, dishwasher, and TV alerts

{% include content-hero.html src="/assets/img/social/guides/best-power-monitoring-plugs-appliance-alerts.svg" alt="Power-metering plugs and sensors matched to washer, dryer, dishwasher, and TV alerts" %}

Most smart plug lists rank plugs for turning lamps on and off. That is not the job here. For a "washer is done" alert or a "TV is on" trigger, the plug is a measuring tool. It needs to report watts often enough, survive a motor load, and stay on.

This guide covers what to look for, then picks by appliance. Every product named below is one I have bought and used.

## The short answer

| Appliance | What to use | Why |
|---|---|---|
| Washer (120V) | [Zooz ZEN15 Power Switch](https://www.amazon.com/dp/B07578W7KY/ref=nosim?tag=madsk0f-20) | Heavy-duty relay built for motor loads. I use it on my washer. |
| TV or monitor | [Ezlo 800 Series Z-Wave smart plug](https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20) or the ZEN15 | Low, steady load. Any reliable metering plug can tell standby from on. |
| Electric dryer (240V) | [THIRDREALITY Zigbee Smart Vibration Sensor](https://www.amazon.com/dp/B0C9DP249C/ref=nosim?tag=madsk0f-20) | A plug cannot go on a 240V dryer outlet. Sense vibration instead. |
| Dishwasher | Check the rating first, or use a vibration sensor | Many are hardwired, and heating elements draw a lot. |

Amazon product links on this page are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html) for details.

## What to look for

### 1. It reports power, not just energy

Some plugs only report total kWh, or report watts once every few minutes. A done alert needs current watts, reported on change. Before buying, check that your hub's driver exposes a power attribute and lets you set how big a change triggers a report.

### 2. It is rated for the load

A washer is a motor load with a startup surge. Many small plugs are rated for lamps and electronics, not motors. Compare the appliance nameplate with the plug's rating for continuous current and motor loads. If the plug does not list a motor or inductive rating, do not use it on a washer.

### 3. It works locally with your hub

Z-Wave and Zigbee metering plugs pair straight to a local hub such as Home Assistant, Hubitat, SmartThings, or Homey, so the alert does not depend on a cloud service. Wi-Fi plugs often need polling or a cloud integration. Polling can work, but it adds delay and hub load.

### 4. The relay can be left alone

You will never switch this plug off. Pick one that remembers its on state after a power outage, and exclude it from every "all off" routine. A washer that loses power mid-cycle is worse than no alert.

### 5. Reporting is tunable

Chatty power reports can flood a mesh. A good driver lets you report on a watt change (for example, every 5 or 10 watts) instead of every second. Tune it once the pattern is known.

## Picks by appliance

### Washer: Zooz ZEN15 Power Switch

[Zooz ZEN15 Power Switch](https://www.amazon.com/dp/B07578W7KY/ref=nosim?tag=madsk0f-20)

This is the monitor on my washer. It is bulky, but it is built for heavier loads and motors, and it reports power reliably over Z-Wave. It is the long-standing community favorite for this job for the same reason.

Read power only. Keep the relay on. Check the washer nameplate against the ZEN15's rating before you plug in.

Recipe: [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html).

### TV or computer monitor: Ezlo 800 Series Z-Wave smart plug

[Ezlo 800 Series Z-Wave smart plug](https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20)

A TV is an easy load to read. Standby is a few watts and on is far higher, so any reliable metering plug works. I use power readings to know when a TV is on, and I listed this plug for that job in my [device guide](/getting-started/device-guide.html#power-monitoring). The ZEN15 also works here if you already have one.

Use the reading as a signal only. The TV remote and power button should keep working as normal.

Recipes: [Dim lights when the TV turns on](/automation/entertainment/tv-dim-lights.html) and [Garage lights that follow doors, motion, and the TV](/automation/lighting/garage-lights-doors-motion-tv.html).

### Electric dryer: a vibration sensor, not a plug

[THIRDREALITY Zigbee Smart Vibration Sensor](https://www.amazon.com/dp/B0C9DP249C/ref=nosim?tag=madsk0f-20), or the [Aeotec SmartThings Multipurpose Sensor](https://www.amazon.com/dp/B095TPSQ3S/ref=nosim?tag=madsk0f-20) if you also want a contact reading in the same spot.

Most electric dryers in the US use a 240V outlet. Normal smart plugs do not fit it and are not rated for it. Mount a battery vibration sensor on a cool, fixed outside panel and treat sustained vibration as running.

Other options people use: a metering plug on a 120V inline dryer vent booster fan, or a whole-home energy monitor installed in the panel by someone qualified. I have not used either, so I cannot recommend a specific product.

Recipe: [Get notified when the dryer finishes](/automation/appliances/dryer-done-notification.html).

### Dishwasher: check before you plug in

Many dishwashers are hardwired, and the ones with a plug can pull a lot of current while heating. I do not have a verified plug pick for this job. If your dishwasher plugs in, confirm the plug's rating covers the nameplate. If not, use a vibration sensor.

Recipe: [Get notified when the dishwasher finishes](/automation/appliances/dishwasher-done-notification.html).

## Thresholds matter more than the plug

The plug only gives you a number. The alert comes from logic that:

1. Marks the appliance as running after power stays above a running threshold.
2. Waits until power stays below a finished threshold for longer than any normal pause.
3. Sends one alert and clears the running state.

Record three full cycles before you pick numbers. Washers pause to fill and soak, so a single low reading does not mean done.

On Hubitat, I wrote an app that does this for you: [Appliance Cycle Monitor](https://github.com/madskristensen/hubitat-drivers/tree/main/apps/appliance-cycle-monitor). It takes a power meter or a vibration sensor and gives each appliance a Ready, Running, or Finished status you can use in Rule Machine, webCoRE, or a dashboard.

## Common mistakes

- **Using a cheap lamp plug on a washer.** It may work for a while, then fail under the motor load.
- **Turning the plug off in an "all off" routine.** Exclude metering plugs from every bulk off command.
- **One threshold rule.** Without a running state, every idle reading can look like "done".
- **Reporting every second.** Tune reports to a watt change so the mesh stays quiet.
- **Trusting stale data.** If the plug goes offline, show unknown, not finished.

## FAQ

### Can I use any smart plug with power monitoring for a washer?

Only if it is rated for the washer's motor load. Many small plugs are not. A heavy-duty metering switch such as the ZEN15 is the safer choice.

### Do these work without the cloud?

Z-Wave and Zigbee metering plugs pair directly to a local hub such as Home Assistant, Hubitat, SmartThings, or Homey and report locally. Check that your hub's driver exposes power readings before buying several.

### How do I monitor a 240V dryer?

Use a vibration sensor on the cabinet, a metering plug on a 120V vent booster fan if you have one, or professionally installed circuit-level monitoring. Do not use an adapter to put a normal plug on a 240V outlet.

{% include pdf-guide-promo.html %}

## Related

- [Choose smart-home devices and gear](/getting-started/device-guide.html)
- [Best humidity sensors for shower fan automation](/articles/best-humidity-sensors-shower-fan.html)
- [Starter house setup guide](/getting-started/starter-house-setup.html)
- [Appliance automations](/automation/appliances/)

{% include page-navigation.html
  left_url="/articles/"
  left_label="Back to articles"
  right_url="/automation/appliances/"
  right_label="Appliance automations"
%}
