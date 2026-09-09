---
layout: automation
title: Prepare the house when someone arrives (without automatic unlocking)
description: Restore Home mode, light a safe path, and return the house to its normal comfort settings without treating phone location as proof that the right person is at the door.
keywords: arrival home automation, welcome home automation, presence detection, entry lighting, home mode automation
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: Should arrival automation unlock the front door?
    answer: Not from phone location alone. Keep a key, keypad, or deliberate lock action as the normal entry path unless a separately tested lock feature meets the household's security requirements.
  - question: Why does arrival sometimes trigger while passing nearby?
    answer: The home area may be too large or the phone location may drift. Require a real Away-to-Home transition and delay nonessential actions until arrival remains stable.
  - question: What should happen for the second person arriving home?
    answer: Usually very little. Reserve whole-house Home actions for the first arrival and use only entry lighting or a notification for later arrivals.
---

# Prepare the house when someone arrives

When the first person returns, the house switches to Home, lights a safe path when needed, and restores the approved comfort settings. The door stays locked until someone deliberately unlocks it.

**Best for:** Households with a reliable Away state and simple arrival actions that are safe when phone location is briefly wrong.

**Not for:** Automatically unlocking a door, opening a garage, disarming an alarm, or starting an appliance based only on a geofence.

## Why this exists

Arrival automation should remove small annoyances without creating a security shortcut. Phone location is useful for preparing lights and climate because those actions are easy to reverse. It is not strong proof that the right person is standing at the door.

Use arrival to restore Home mode. Keep entry access deliberate unless the household separately tests and accepts a lock's own arrival feature.

## Logic

<div class="automation-example">IF the first person changes from Away to Home
AND the arrival remains stable
THEN set the house to Home
AND light the entry path if it is dark
AND restore approved comfort settings
BUT do not unlock a door from phone location alone</div>

- **Trigger:** A tracked household member changes from Away to Home.
- **Conditions:** The house was actually in Away mode, the arrival remains stable briefly, and this is the first person home.
- **Action:** Set the house to Home, turn on entry or path lights if it is dark, restore the approved thermostat setting, and send a concise status notification.
- **Wait / timeout:** Wait long enough to reject a momentary location jump before running nonessential actions.
- **Stop condition:** The presence signal returns to Away before the confirmation delay ends.
- **Manual override:** Physical switches, thermostat controls, keys, and keypads still work normally.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect the first return home**

Use your platform's built-in presence feature (phone location or network connection) rather than a dedicated product. Require a real Away-to-Home transition.

</div>
<div class="product-item" markdown="1">

**Light the entry path**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Keep the physical paddle usable.

</div>
<div class="product-item" markdown="1">

**Restore heating and cooling**

[ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC/ref=nosim?tag=madsk0f-20). The thermostat's safe limits remain authoritative.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Make the arrival routine consume the same Home and Away states used by the [away-mode recipe](/automation/daily-routines/away-mode.html).
2. Start with a notification-only test and record false arrivals for at least a week.
3. Add entry lighting next because it is visible and easy to reverse.
4. Restore climate only within the thermostat's independent safe limits.
5. Run whole-house actions only for the first arrival. Later arrivals should not restart music, change temperatures, or disturb people already home.
6. Keep door access manual unless I have verified a separate lock feature with its own safeguards and audit trail.

## Safe first actions

- Change the shared state from Away to Home.
- Cancel pending away actions.
- Turn on the porch, entry, or path light when it is dark.
- Resume a normal thermostat schedule.
- Stop an away-lighting pattern.
- Notify the household that Home mode was restored.

## Actions to keep separate

- Unlocking an exterior door.
- Opening a garage door or gate.
- Disarming an alarm.
- Starting a coffee maker, fireplace, heater, or cooking appliance.
- Playing audio without checking the time and current occupants.

Each of these needs its own trigger, safeguards, and acceptance tests. Arrival should not silently grant access or start equipment.

## Advanced features

### First arrival versus later arrivals

The first arrival can restore Home mode and normal comfort. A later arrival may need only entry lighting. This prevents repeated thermostat changes and unwanted announcements.

### Approaching versus home

An approaching signal can prepare slow, reversible actions such as climate recovery. Do not treat approaching as proof that someone has reached the property.

### Physical arrival confirmation

A deliberate door unlock, garage-door operation, or entry contact event can confirm that someone reached the house. Use it to improve lighting timing, not to weaken the security of the access control itself.

## Failure modes

- **Arrival triggers while passing nearby:** Reduce the home area, require the previous state to be Away, and add a stability delay.
- **The house remains Away after entry:** Check the person's location permissions and provide a visible Home control.
- **The second arrival repeats every action:** Gate whole-house actions on whether anyone is already home.
- **Lights turn on during daylight:** Add a darkness condition to lighting actions, not to the Home-state change.
- **Climate restores too early:** Move climate recovery to a confirmed Home state or use a smaller approaching area.
- **The hub or internet is down:** Keys, keypads, wall switches, alarm controls, and thermostat controls remain the fallback.

## FAQ

### Should arrival automation unlock the front door?

Not from phone location alone. Keep a key, keypad, or deliberate lock action as the normal entry path unless a separately tested lock feature meets the household's security requirements.

### Why does arrival sometimes trigger while passing nearby?

The home area may be too large or the phone location may drift. Require a real Away-to-Home transition and delay nonessential actions until arrival remains stable.

### What should happen for the second person arriving home?

Usually very little. Reserve whole-house Home actions for the first arrival and use only entry lighting or a notification for later arrivals.

## Related recipes

- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Outdoor night lights](/automation/lighting/outdoor-night-lights.html)
- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Daily routine automations](/automation/daily-routines/index.html)

<div class="page-navigation">
  <a href="/automation/daily-routines/index.html">Back to daily routine automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
