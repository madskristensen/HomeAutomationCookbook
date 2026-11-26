---
cta_category: security
layout: guide
title: "Garage door auto close: when it is safe and how to set it up"
description: Auto close a garage door safely. Start with an open-door alert, then close unattended only with an opener that flashes and beeps first and has working photo eyes.
date: 2026-11-26
last_modified_at: 2026-11-26
image: /assets/img/social/guides/is-it-safe-to-auto-close-a-garage-door.png
---

# Garage door auto close: when it is safe and how to set it up

{% include content-hero.html src="/assets/img/social/guides/is-it-safe-to-auto-close-a-garage-door.svg" alt="Security guide card titled Garage door auto close: when it is safe and how to set it up, with a simple checklist illustration" %}

Yes, a garage door can close automatically and safely, but only when the opener or its add-on controller is built for unattended closing. That means it flashes a light and beeps for at least 5 seconds before the door moves, it reverses if something is in the way, and it works on a sectional door that rolls up in panels. If your setup cannot do that, the safe version is an alert on your phone and a person who closes the door. The [garage door left open alert recipe](/automation/security/garage-door-notification.html) is the place to start.

## The short answer

| Your setup | Safe to auto close? | What to do |
|---|---|---|
| Opener with a built-in timer-to-close or app close feature, sectional door, photo eyes working | Yes, as the opener's manual describes | Turn on the feature in the opener's own settings and test the warning |
| Smart hub plus a tilt sensor only | No, a sensor cannot close anything | Use it for an open-door alert |
| A relay or smart plug that "presses" the wall button | No | It skips the required warning. Use an alert instead |
| One-piece door that swings up, or a swinging door | No | US safety rules do not allow unattended closing on these doors |
| Photo eyes blocked, misaligned, or disconnected | No | Fix them before any remote closing at all |

## Why the rules are strict

A garage door is the heaviest moving thing in most homes, and an automatic close happens when nobody is watching. A child, a pet, or a bike can be in the doorway. That is why the US safety standard for residential garage door openers (16 CFR 1211, which follows UL 325) sets extra rules for closing without a person standing at the wall button:

- **A warning first.** The opener must flash a light and sound an alarm inside the garage for at least 5 seconds before the door starts to close.
- **Any button cancels it.** Pressing the wall control, a remote, or the keypad during that warning stops the close.
- **Entrapment protection.** The door must reverse if it hits something, and the photo eyes near the floor must stop it if the beam is broken.
- **Sectional doors only.** Unattended closing is not allowed on one-piece or swinging doors.
- **Two tries, then stop.** If the door reverses twice during an unattended close, the opener stops trying until someone uses a normal control.

You do not need to memorize any of this. The takeaway is simple: the opener does the safety work, not your hub, your phone, or a motion sensor.

## Start with an alert

Most families get what they want from an alert alone. A tilt sensor on the door tells your hub when it is open, and the hub sends a message when it has been open for about 10 to 15 minutes, plus a check at bedtime. You still decide whether to close it.

- **Zigbee hubs:** this is the tilt sensor I use on my garage, the [THIRDREALITY Zigbee Smart Garage Door Tilt Sensor](https://www.amazon.com/dp/B0CZP2CJXF/ref=nosim?tag=madsk0f-20). It is a small battery sensor that reports open when the door tips past an angle. It works with Zigbee hubs such as Hubitat, SmartThings, and Echo models with a built-in Zigbee hub.
- **Z-Wave hubs:** the [Ecolink Z-Wave Plus Garage Door Tilt Sensor](https://www.amazon.com/dp/B01MRZB0NT/ref=nosim?tag=madsk0f-20) does the same job on Z-Wave. Z-Wave needs a hub like Hubitat or SmartThings. It does not work with an Echo or a Google Home speaker, so on Alexa pick the Zigbee sensor with a Zigbee Echo instead.
- **Google Home or Apple Home only:** neither pairs Zigbee or Z-Wave sensors directly. Add a hub that does, or use the opener maker's own app alerts if your opener has them.

The [garage door left open sensor guide](/articles/garage-door-left-open-sensor.html) covers where to mount it. Amazon product links are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html).

## When auto close makes sense

Once the alert has run for a few weeks and you trust it, auto close can be worth it for a door that is often left open at night. Do it this way:

1. **Use the opener's own feature.** Many openers have a timer-to-close setting or an app close button that already includes the warning light and beep. Check the opener's manual for the exact name and steps.
2. **Test the safety parts first.** Follow the safety test in the opener's manual. A common one is to lay a 2x4 board flat in the doorway and close the door. It should reverse when it touches the board. Then break the photo eye beam with an object, not a person, while the door closes. It should stop and reverse.
3. **Listen and look.** Start an unattended close and check that the light flashes and the beeper sounds before the door moves.
4. **Keep the alert.** Let your hub keep reporting the door state. If the door is still open a few minutes after it should have closed, send "Garage did not close" so a person checks it.
5. **Tell the family.** Everyone should know what the beeping means and that pressing the wall button cancels the close.

The [auto close a garage door safely recipe](/automation/security/garage-auto-close.html) has the full checklist and the alert logic.

## What not to use as a safety check

- **A motion sensor.** It can miss a child or pet standing still.
- **Phone location.** Everyone being away does not mean the doorway is clear. Location is fine for deciding who gets the alert.
- **A camera.** It shows you the garage, but it is not entrapment protection.
- **The tilt sensor.** It reports where the door is, not whether the path is clear.

## Failure modes

- **Door reverses during an auto close:** Something blocked it or the photo eyes are out of line. Check in person before trying again.
- **Sensor shows unknown or offline:** Treat the door as open and send the alert anyway.
- **Auto close fires while someone is loading the car:** Make the timer longer, or turn it on only at night.
- **No beep before closing:** Stop using unattended close until the opener or controller is checked. The warning is required.

## FAQ

### Can my smart home hub close the garage door on its own?

Only through an opener or controller that is approved for unattended closing and gives the required warning. A hub switching a relay wired to the wall button skips that warning, so do not use one for unattended closing.

### How long should the garage door stay open before it closes?

Pick a time that fits how your family uses the garage, often 10 to 15 minutes during the day and shorter at night. Start with an alert at that time, and only add auto close after the alert feels right for a few weeks.

### Can I add auto close to an older opener?

Openers and add-on controllers sold for unattended closing have to meet the warning and safety rules above. An older opener may not support it. Follow the opener's manual, and if it does not list an unattended close feature, stay with alerts.

## Related guides and recipes

- [Garage door left open alarm and alerts](/automation/security/garage-door-notification.html)
- [Auto close a garage door safely after an alert](/automation/security/garage-auto-close.html)
- [Garage door left open sensor: what to buy and where to mount it](/articles/garage-door-left-open-sensor.html)
- [Goodnight scene: turn off the lights and lock the doors](/articles/goodnight-scene-lights-off-lock-doors.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
