---
layout: guide
title: Why arrive and leave triggers fail
description: Phone geofences, battery saving, and Wi-Fi hints often disagree with who is home. Confirm Away and Home before the house acts.
date: 2026-10-05
last_modified_at: 2026-10-05
image: /assets/img/social/guides/why-arrive-leave-triggers-fail.png
---

# Why arrive and leave triggers fail

<figure class="content-hero">
  <img src="/assets/img/social/guides/why-arrive-leave-triggers-fail.svg" alt="A phone location hint set beside the people who are actually home" width="1200" height="630">
</figure>

A phone crossing a circle on a map is a hint. It is not a headcount. Away and Home go wrong when the house treats that hint as everyone who might still be inside.

## The short answer

| What you wanted | What usually happened | What to require before the house acts |
|---|---|---|
| Away when the last person leaves | A phone slept, stayed on the counter, or never reported the exit | Every tracked resident away for a delay, no fresh indoor activity, and Guest or Staying Home off |
| Home when someone arrives | The geofence fired from the road, or it fired after they were already inside | A stable arrival, then only reversible actions until a door, garage, or manual Home control agrees |
| One routine that does everything | A late or early signal changed a lock, an alarm, or the thermostat too far | Split the decision from the actions. A weak signal only gets a reversible job |

## A geofence is a rough circle

Phone location is a point with some error, dropped into a circle you chose. That circle is easy to get wrong during an ordinary week.

- The radius is large enough that driving past the house looks like an arrival.
- The radius is small enough that the backyard, the garage, or the far side of the building looks like Away.
- The phone updates late. The house is still Away while someone is in the kitchen, or still Home while the car is already down the block.
- The point drifts. A phone on a windowsill can wander in and out of the circle without anyone moving.

Change the circle only after you have watched real arrivals and departures. A tighter circle does not fix a phone that reports late.

## Battery saving hides the transition

Phones are built to avoid constant location checks. A low-power mode, a location permission that only works while the app is open, and a nearly empty battery all delay the update the automation is waiting on.

A missing update is not proof that someone left, and it is not proof that someone is home. Treat a stale or silent phone as uncertain. The [away mode recipe](/automation/daily-routines/away-mode.html) waits through that uncertainty instead of switching the house immediately.

If a phone dies, or someone leaves it on the counter, the person and the phone are in different places. No radius setting repairs that.

## Wi-Fi presence is a different hint

A phone on the home Wi-Fi can support an arrival, or a check that someone is still around. It answers a narrower question than a geofence: is this device on the network right now?

It still fails in ordinary ways.

- A phone drops Wi-Fi and stays on cellular while the person is in the house.
- A phone left on a charger keeps the house looking occupied.
- A guest phone, a tablet, or a spare handset looks like a resident.
- Sleep and privacy settings change how often a phone shows up on the network.

Wi-Fi is a useful second hint. It is a poor only hint. A phone joining the network is not the same event as a person coming through the door.

## Ask more than one signal to agree

A Home or Away change you can live with is a small vote, not a single event.

1. Every regular resident you track has been in the new state long enough to survive a glitch. Ten to fifteen minutes is the starting delay in the away recipe. Shorter feels clever until it is wrong once.
2. Recent indoor motion, a door, or a deliberate control does not contradict the phone. Someone walking around inside is a reason to stay Home.
3. [Guest mode](/automation/daily-routines/guest-mode.html) or Staying Home is off before any Away action. A babysitter, a grandparent, or a kid without a tracked phone is still occupancy.
4. On arrival, start with reversible actions. The [arrival recipe](/automation/daily-routines/unlock-door-arrival.html) can restore Home and comfort settings. It does not unlock the door from location alone.

If the signals disagree, leave the house as it is and show that presence is uncertain. Guessing Away is the expensive direction.

## What a weak signal may change

| Action | When a flaky arrive or leave signal is enough |
|---|---|
| Entry lights after dark | Often, when the wall switch still works and daylight can suppress them |
| A modest thermostat setback inside limits you already trust | Only after the empty-home decision has been boring for a while. See [safe thermostat auto-away](/automation/climate/safe-thermostat-away.html) |
| Starting a vacuum | Only with the same tested empty signal, a daytime window, and a way to dock if someone is actually home |
| Locks, alarms, or a deep temperature change | Keep these on a deliberate control. A phone circle is the wrong proof |

The physical controls have to keep working when the vote is wrong. A wall switch, a key, a keypad, and the thermostat on the wall are the fallback.

## Platform notes

I have used Alexa, SmartThings, and Hubitat. All three can see a phone's location in some form. None of them can repair a phone in a drawer, a permission set to save battery, or a person who was never given a tracked device.

SmartThings labels the phone signal **Get your location from this phone**. On Hubitat, the same decision often lives in Mode Manager, and other rules follow the mode. Alexa can use a location trigger when the phone and the routine allow it. The names differ. The failure is the same: one device update is not the household.

I have not personally run Home Assistant. If you use it, apply the same vote and the same refusal to guess. Check the current presence integration yourself. This page is not a hands-on review of that platform.

Another phone app does not help until you have watched it miss, and decided what a miss should do.

## Failure modes

- **Away turns on while someone is home:** Lengthen the delay, fix the person who is not tracked, and make Guest or Staying Home obvious.
- **The house stays Away after someone is inside:** Location updated late. Give people a visible Home control. Lights and the thermostat still have to work by hand before the phone catches up.
- **Arrival fires from the street:** Watch a real drive-by before you shrink the area, and require the previous state to be Away.
- **Wi-Fi says home and the geofence says away:** Call it uncertain. Do not blend the two into a confident empty house.
- **A phone battery dies:** Missing data stays uncertain. Silence is not Away.
- **The second person to arrive replays the whole welcome:** Gate whole-house actions on whether anyone is already home.
- **The hub or internet is down:** Keys, switches, and the thermostat still work. Location rules will not.

## FAQ

### Is a geofence enough if the circle is smaller?

A smaller circle changes where the hint fires. It does not tell you about a phone left on the counter, a delayed update, or a person who is not tracked.

### Should Wi-Fi presence replace phone location?

Use it as a confirming hint. A phone can sit on the network after someone left, or fall off the network while someone is home.

### What should Guest mode block?

Treat Guest or Staying Home as occupied. Away waits. Personal announcements and aggressive empty-house actions wait with it. Ordinary wall switches stay as they are.

### Can arrival automation unlock the door?

Keep a key, a keypad, or another deliberate lock action as the normal way in. Location can prepare lights and a modest comfort change. It is the wrong signal to be the only key.

## Related recipes

- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Prepare the house when someone arrives](/automation/daily-routines/unlock-door-arrival.html)
- [Make the smart home predictable for guests](/automation/daily-routines/guest-mode.html)
- [Safe thermostat auto-away](/automation/climate/safe-thermostat-away.html)
