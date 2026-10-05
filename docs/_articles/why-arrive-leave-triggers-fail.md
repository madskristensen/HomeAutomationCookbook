---
layout: guide
title: Why arrive and leave triggers fail
description: Phone location is a hint, not proof the house is empty. Confirm Away and Home with a second signal before the house changes.
date: 2026-10-05
image: /assets/img/social/guides/why-arrive-leave-triggers-fail.png
---

# Why arrive and leave triggers fail

<figure class="content-hero">
  <img src="/assets/img/social/guides/why-arrive-leave-triggers-fail.svg" alt="A house geofence, a phone, and a second check before Away or Home changes anything" width="1200" height="630">
</figure>

Phone location is a useful hint. It is a bad proof that someone arrived, left, or that the house is empty.

Away and Home should change only after that hint survives a second check. Until it does, the wall switches, locks, and thermostat still have to work by hand.

## What a geofence actually reports

A geofence is a circle around the house. The phone tells the hub when it thinks that circle was crossed.

The circle is coarse. A drive past the block, GPS drift in a parking spot, or a radius that reaches the street can look like an arrival. A phone in a bag, underground, or inside a large building can report the exit late, or not at all.

The hub only knows the last report. It does not know whether a person is standing in the kitchen.

| Signal | What it can mean | What it does not mean |
|---|---|---|
| Phone left the geofence | Location services think the phone crossed the circle | A person left, or the house is empty |
| Phone entered the geofence | The phone thinks it is near the house | The right person is at the door |
| No recent report | The phone is asleep, dead, or blocked from updating | That person has left |
| Phone joined home Wi-Fi | Some device associated to the network | A resident is home and will stay |

## Battery saving delays the update

Phones pause background location to save battery. A low-power mode, a vendor battery tool, or location permission limited to "while using the app" can freeze the last report for hours.

Two failures look the same from the hub:

- The phone is still home, but the last report said away. Lights go off, or the thermostat sets back, while someone is there.
- The phone left hours ago, and the away report arrives at midnight. A vacuum, a lighting scene, or an away routine runs at the wrong time.

Treat a phone that stops reporting as unknown. Do not treat silence as "this person left." A dead battery is uncertain, not automatically away. The [away mode recipe](/automation/daily-routines/away-mode.html) uses that rule.

## Wi-Fi presence is a different hint

A phone joining the home Wi-Fi can confirm that a device is in or near the house. It still does not prove who is home.

Phones drop Wi-Fi while they sit on a table. They can stay associated from the yard or the driveway. A randomized hardware address can look like a new device every day. A guest who knows the password shows up as present without being a resident you meant to track.

Use Wi-Fi as a second vote. Do not use it as the only reason to change Away or Home. Do not use it to unlock a door.

Network presence can be that second vote when the platform already supports it. The [device guide](/getting-started/device-guide.html#household-presence) describes the network presence I use at home. A sleeping phone radio still makes it fail, so it does not replace the delay or the Guest control.

## Confirm with more than one signal

One signal can start a pending state. It should not commit the house.

A practical confirm before leaving:

1. Every tracked resident phone reports away.
2. Wait 10 to 15 minutes. That is the starting range in the [away mode recipe](/automation/daily-routines/away-mode.html).
3. During the wait, cancel if there is fresh indoor evidence: motion in a lived-in room, a door, or a switch someone just used.
4. Guest mode and Staying Home both count as occupied. If either is on, do not enter Away.

A practical confirm before arrival actions:

1. The house was actually Away. A drive-by should not replay a welcome routine when someone is already home.
2. The arrival stays stable for a short period before nonessential actions run.
3. A Wi-Fi join or an entry door can support the phone report. Neither one identifies the person.
4. Light a path and restore comfort. Do not unlock a door from location alone. That is the point of the [arrival recipe](/automation/daily-routines/unlock-door-arrival.html).

If the signals disagree, stay in the safer state. Pending Away returns to Home. A shaky arrival does not unlock anything or start an appliance.

## Guest mode and Staying Home

Guests, sitters, cleaners, and relatives often have no tracked phone. If every resident leaves, a geofence will say the house is empty. It is not.

Guest mode is a switch a host sets on purpose. While it is on, the house stays occupied even when every resident phone is gone. The [guest mode recipe](/automation/daily-routines/guest-mode.html) keeps ordinary lights and safety alerts working, and it pauses the personal routines.

Staying Home is the same idea for a resident whose phone is not a reliable witness that day. The phone was left on the counter, location permission is off, or someone is home without the tracked device. The control has to be obvious. A hidden variable that only one person can find will not get used.

Turn both on before you trust automatic Away. Test by leaving while a guest is still home. Test by leaving a phone on the counter and walking around the block.

## Make Away and Home trustworthy

Start with a notification that says what the house would have done. Watch a week of real departures and returns, including one person leaving while others stay.

Then allow reversible actions: nonessential lights, and a modest thermostat change that has its own safe limits. Keep locks, garage doors, alarms, and appliance starts on separate tests.

Use one shared state the household can see: Home, Away, and Guest. Add Pending Away if the delay should be visible. When the hub or the internet fails, the physical controls still work. Away mode is not a substitute for a key or a wall switch.

Check each person alone. One phone that never clears will block Away forever. One phone that drops early will empty the house too soon. Fix that device or stop tracking it. Do not silently ignore a stuck signal.

Phone-location names differ by app. I have used Alexa, SmartThings, and Hubitat for household routines. SmartThings calls this signal "Get your location from this phone." Hubitat can change mode from presence sensors. I could not verify one Alexa routine shape that fits every account, and I have not personally run Home Assistant. Use the platform notes on the [away mode recipe](/automation/daily-routines/away-mode.html) rather than copying an untested click-path.

## FAQ

### Is phone location enough to mark the house empty?

No. Phones get left behind, run out of battery, and report late. Require every tracked person, a delay, no fresh indoor activity, and an off switch for guests.

### Should a Wi-Fi disconnect mean someone left?

No. Phones disconnect while they are still on the kitchen table. Use Wi-Fi as a supporting hint, not as proof of departure.

### What should happen when the reports disagree?

Keep the previous safer state. Cancel a pending away if anything suggests a person remains. Do not unlock, disarm, or start a machine on a single arrive event.

## Related guides and recipes

- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Prepare the house when someone arrives](/automation/daily-routines/unlock-door-arrival.html)
- [Make the smart home predictable for guests](/automation/daily-routines/guest-mode.html)
- [Start the robot vacuum when everyone leaves](/automation/appliances/robot-vacuum-auto-start.html)
