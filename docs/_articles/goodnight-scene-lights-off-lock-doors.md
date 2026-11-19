---
cta_category: daily-routines
layout: guide
title: "Goodnight scene: turn off the lights and lock the doors"
description: Build a goodnight scene that turns off the lights and locks the doors with one tap or phrase. Check the doors are closed first and confirm each lock.
date: 2026-11-19
last_modified_at: 2026-11-19
image: /assets/img/social/guides/goodnight-scene-lights-off-lock-doors.png
---

# Goodnight scene: turn off the lights and lock the doors

{% include content-hero.html src="/assets/img/social/guides/goodnight-scene-lights-off-lock-doors.svg" alt="Bedtime guide card titled Goodnight scene: turn off the lights and lock the doors, with a simple checklist illustration" %}

To create a goodnight scene that turns off the lights and locks the doors, make one routine that you start on purpose, with a button, a phrase like "Alexa, good night", or a tap in your app. The routine turns off the lights you chose, leaves a dim path light on, locks each smart lock, and then tells you if any door did not lock. Most hubs and voice assistants can do this. The [bedtime routine recipe](/automation/daily-routines/bedtime-routine.html) has the full rule.

## The short answer

| Step | What it does | Why |
|---|---|---|
| 1. Start it on purpose | A button by the stairs, a voice phrase, or a tap | Bedtimes vary, so a fixed time can leave someone in the dark |
| 2. Check doors are closed | Skip the lock and warn you if a door sensor says open | A deadbolt thrown on an open door does not secure anything |
| 3. Turn off chosen lights | Living areas, kitchen, porch | Leave bedrooms and anyone still up alone |
| 4. Keep a path light | A hallway or bathroom light at low level | Safer for kids and late trips to the bathroom |
| 5. Lock the doors | Each smart lock that the hub can control | One step instead of walking the house |
| 6. Report what failed | "Back door did not lock" | A lock can jam or run low on battery |

## What you need

- **A trigger you start yourself.** A smart button near the stairs is the easiest for the whole family. On Zigbee, the [SONOFF SNZB-01P Zigbee Wireless Button](https://www.amazon.com/dp/B0CL9JTMWF/ref=nosim?tag=madsk0f-20) works. On Z-Wave, the [Zooz ZEN34 Remote Switch](https://www.thesmartesthouse.com/products/zooz-z-wave-plus-700-series-remote-switch-zen34-battery-powered?sca_ref=12757918.GPRWSTNoUrpgR) mounts on the wall like a switch. A voice phrase or a tap in the app also works.
- **Smart lights or switches** for the rooms you want off. Smart switches are best, because the wall paddle still works for everyone.
- **A smart lock your hub can control.** Check that it reports locked, unlocked, and jammed, not just that a command was sent. Keep a physical key.
- **Optional: a door sensor** on each locked door, so the routine knows the door is actually closed.

See the [device guide](/getting-started/device-guide.html) for which hubs support which radio. Amazon product links are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html).

## How to set it up on your platform

The steps are the same everywhere: one trigger, then lights off, path light on, locks locked, and a check. Menu names change often, so look for these pieces in your app.

- **Alexa:** Create a routine with "When you say" set to "good night". Add Smart Home actions to turn off a light group and lock each lock. Alexa lets a routine lock a supported lock, but it will not unlock one from a routine. The [Start an Alexa smart home guide](/articles/start-an-alexa-smart-home.html) covers routines.
- **Google Home and Apple Home:** Both have a goodnight style routine or scene you can start by voice or from the app. Add your lights and your lock, then check that the lock shows up as an action before you rely on it.
- **Hubitat:** Use a button or a virtual switch as the trigger and build the rule in Basic Rules or Rule Machine. Set the mode to Night, turn off the lights, lock the locks, and send a notification if a lock reports anything other than locked. The [Start a Hubitat smart home guide](/articles/start-a-hubitat-smart-home.html) covers the basics.
- **SmartThings:** Make a routine you run manually, or start it from a button. Add the lights, the lock, and a notification.
- **Home Assistant:** Make a script that turns off the lights and locks the locks, then trigger it from a button or a dashboard tile. Add a condition that checks the door sensor first.

## Check the doors before you lock them

A smart lock does not know if the door is open. If someone left the back door open, the deadbolt can extend into the air and the app still says locked. If you have a door sensor on that door, make the routine skip the lock and send "Back door is open" instead. If you do not, add a "check the back door" reminder to the message until you do.

## Check the result, not the command

Locks jam, batteries run low, and a radio message can get lost. Wait about 30 seconds after the lock command, then read each lock's state. If any lock is not locked, send one clear message that names it. The [door left unlocked recipe](/automation/security/door-unlocked-bedtime-check.html) has this check built in, and it also works as a standalone bedtime check.

## What to leave out

- **The garage door.** Do not close a garage door from a goodnight scene unless the opener is built and approved for unattended closing. Get an alert instead with the [garage door left open recipe](/automation/security/garage-door-notification.html).
- **Bedrooms and anyone still up.** Only turn off rooms you picked. If a room has motion, skip it.
- **Safety alerts.** Never mute smoke, carbon monoxide, or water leak alerts as part of a quiet night.
- **A fixed time.** A schedule can suggest bedtime, but let a person start the final step. Someone may still be coming home.

## Failure modes

- **A lock did not lock:** Check that the door lines up and the bolt moves freely, then the battery. Most jams are a door that sags a little.
- **The lights came back on:** Another rule, often a motion rule, turned them back on. Make that rule skip Night mode.
- **Nothing happened by voice:** The voice assistant may not have heard the phrase, or the internet was down. A button on a local hub keeps working when the internet is out.
- **Someone got locked out:** Keep a physical key, and do not add an auto-lock on a timer until the whole family is used to the routine.

## FAQ

### Can I lock the doors with a voice command?

Usually yes. Most voice assistants let you lock by voice or from a routine. Unlocking by voice usually needs a PIN or is blocked, which is a good thing.

### Should the goodnight scene run automatically at a set time?

It is better to start it yourself. A time can send a reminder, like "Ready for good night?", but the final step should wait for a person.

### What if I do not have a smart lock?

Use a door sensor and a bedtime message that says which doors are still open. Then lock them by hand. You still save the walk around the house.

## Related guides and recipes

- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Alert when an exterior door is left unlocked](/automation/security/door-unlocked-bedtime-check.html)
- [Bathroom night lighting](/automation/lighting/bathroom-night-light.html)
- [Garage door left open alarm](/automation/security/garage-door-notification.html)
- [Smart home tips for light sleepers](/articles/smart-home-tips-for-light-sleepers.html)
- [Smart home routines: morning, overnight, and away](/automation/smart-home-routines/)
