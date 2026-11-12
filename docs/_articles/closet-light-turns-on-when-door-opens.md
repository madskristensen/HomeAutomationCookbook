---
cta_category: lighting
layout: guide
title: Closet and pantry lights that turn on when the door opens
description: Make a closet or pantry light turn on when the door opens. Add a door sensor and a smart switch, pick a safe off delay, and keep the wall switch working.
date: 2026-11-12
last_modified_at: 2026-11-12
image: /assets/img/social/guides/closet-light-turns-on-when-door-opens.png
---

# Closet and pantry lights that turn on when the door opens

{% include content-hero.html src="/assets/img/social/guides/closet-light-turns-on-when-door-opens.svg" alt="A pantry door opening with a door sensor on the frame and the light inside switching on" %}

To make a closet or pantry light turn on when the door opens, put a door sensor (also called a contact sensor) on the door frame and control the light with a smart switch. When the sensor reports open, your hub turns the light on. When the door has been closed for a minute or two, it turns the light off. The wall switch keeps working the whole time. The [turn lights on when a door opens recipe](/automation/lighting/toggle-lights-door.html) has the full rule.

## The short answer

| Your space | What to use | Off rule to start with |
|---|---|---|
| Small reach-in closet | Door sensor plus a smart switch | Off about 1 minute after the door closes |
| Pantry you step into | Door sensor plus a smart switch | Off a few minutes after the door closes, so a quick return trip stays lit |
| Walk-in closet or a room with two doors | A motion or presence sensor instead | Off after no motion for a while |
| No hub and no smart home | A battery closet light with its own door or motion switch | Handled by the light itself |

A door is a clear signal in a small space. Opening it means someone wants light right now. In a bigger room, people stay inside with the door closed, so a door rule can leave them in the dark. Use [motion lights](/automation/lighting/lights-on-motion.html) there instead.

## What you need

- **A door sensor.** It has two parts: the sensor on the frame and a small magnet on the door. It reports open when the magnet moves away. On a Zigbee hub, the [SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL/ref=nosim?tag=madsk0f-20) works. On a Z-Wave hub, use the [Zooz ZSE41 Open/Close XS Sensor](https://www.thesmartesthouse.com/products/zooz-z-wave-plus-700-series-xs-open-close-sensor-zse41?sca_ref=12757918.GPRWSTNoUrpgR).
- **A way to switch the light.** A smart wall switch is best, because the paddle still works for guests. On Zigbee, the [Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20) is a plain on/off switch. On Z-Wave, the [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN/ref=nosim?tag=madsk0f-20) also dims. Check the wiring needs, like a neutral wire, before you buy, and use an electrician if you are not sure. A smart bulb also works if nobody turns the wall switch off.
- **A hub or app that can run the rule.** Both radios need a hub that speaks them. Amazon Echo models with a built-in Zigbee hub can talk to Zigbee sensors, but not Z-Wave. See the [device guide](/getting-started/device-guide.html#contact) for which hubs support which radio.

Amazon product links are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html).

## Where to mount the sensor

- Put the sensor on the frame and the magnet on the door, on the side away from the hinges. That edge moves the most, so the sensor reads open sooner.
- Keep the gap between the two parts as small as the instructions say. A wide gap can make the sensor report open when the door is shut.
- Mount it on the inside of the closet if you can, so it is out of sight and out of reach of small hands.
- Open and close the door ten times and watch the state in your app before you build the rule.

## Pick a safe off rule

Turning the light on is the easy part. Turning it off is where people get annoyed.

- **Small closet:** turn the light off about 1 minute after the door closes. The [turn off closet lights on door close recipe](/automation/lighting/disable-on-door-close.html) walks through it.
- **Pantry:** start with a longer delay, a few minutes, so the light does not go out between trips.
- **Only turn off what the rule turned on.** If someone used the wall switch, leave the light alone.
- **Never shut someone in the dark.** If a person can stand inside with the door closed, use a motion sensor for the off rule instead. The [lights off after motion stops recipe](/automation/lighting/lights-off-after-motion.html) covers that.

## Can a smart lock turn on lights when the door opens?

Sometimes, but unlocking is not the same as opening. A lock reports locked and unlocked, which does not tell you the door actually moved. Some smart locks also include a door position sensor that reports open and closed. If your lock shares that state with your hub, you can use it as the trigger. If not, add a regular door sensor next to the lock. For an entry door, an unlock is still a good signal to light the way in. The [prepare the house when someone arrives recipe](/automation/daily-routines/unlock-door-arrival.html) uses it that way.

## Failure modes

- **The light turns on by itself:** The magnet and sensor are too far apart, or the door flexes. Realign them, then check the battery.
- **The light is slow to turn on:** Cloud routines add a little delay. A rule that runs locally on the hub is usually faster. A weak signal between the sensor and the hub can also slow it down, so a plugged-in device on the same radio nearby can help.
- **The light turns off while you are inside:** Make the off delay longer, or switch to a motion sensor for the off rule.
- **Nothing happens when the internet is down:** Cloud routines stop. Local hubs keep working. Either way, the wall switch still turns the light on.

## FAQ

### Do I need a smart switch, or will a smart bulb work?

A smart bulb works if the wall switch always stays on. If someone flips the switch off, the bulb loses power and the automation cannot turn it on. A smart switch avoids that, and the paddle still works for everyone.

### How fast does the light turn on?

With a rule that runs locally on the hub, it usually feels close to instant. Cloud routines can lag a little. Test it a few times and judge it in the dark.

### Will this work with Alexa?

It can. Use an Alexa routine with the door sensor opening as the trigger, if your sensor shows up as a trigger under When. Check that before you buy, because each integration decides what it shares. The [Start an Alexa smart home guide](/articles/start-an-alexa-smart-home.html) covers the basics.

## Related guides and recipes

- [Turn lights on when a door opens](/automation/lighting/toggle-lights-door.html)
- [Turn off closet lights on door close](/automation/lighting/disable-on-door-close.html)
- [Turn lights on with motion sensors](/automation/lighting/lights-on-motion.html)
- [Lights turning on by themselves](/articles/lights-turning-on-by-themselves.html)
- [Motion sensor placement guide](/articles/motion-sensor-placement.html)
- [Lighting automations](/automation/lighting/)
