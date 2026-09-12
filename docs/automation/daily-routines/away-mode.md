---
layout: automation
title: Set away mode when everyone leaves
description: A conservative, platform-neutral away-mode recipe that verifies the home is empty before changing lights, climate, or security behavior.
keywords: away mode automation, presence detection, leave home automation, location based automation, smart home away mode
last_modified_at: 2026-09-12
compact: true
faqs:
  - question: How long should away mode wait after everyone leaves?
    answer: Start with 10 to 15 minutes. A delayed away mode is less disruptive than a false activation while a child, guest, or person without a phone is still home.
  - question: Is phone location enough to know the house is empty?
    answer: No. Phones can be left behind, run out of battery, or report the wrong location. Use a delay, recent motion or door activity, and a guest override.
  - question: Should away mode automatically lock doors and arm an alarm?
    answer: Add security actions only after the household has tested presence detection and the security system's own entry, exit, and emergency behavior.
---

# Set away mode when everyone leaves

When the house is confidently empty, it switches to Away, turns off what is safe to turn off, and tells the household what changed.

**Best for:** Households with reliable presence signals, a manual Home or Guest override, and people willing to test false-away scenarios.

**Not for:** A home where children, guests, caregivers, or anyone without a tracked device may remain inside without a dependable override.

## Why this exists

The expensive failure is not forgetting to save a little energy. It is locking in a guest, arming an occupied house, or changing the temperature unsafely because a phone reported the wrong location. Away mode should be a shared state that other automations can use, not one giant routine with every possible action.

Start with reversible actions and a notification. Add locks, alarms, or appliance control only after the empty-home decision has proved reliable.

## Logic

<div class="automation-example">IF every tracked person has been away for 15 minutes
AND Guest or Staying Home mode is off
AND recent indoor activity does not suggest someone is home
THEN set the house to Away
AND make only the reversible changes the household has approved
AND send a summary notification</div>

- **Trigger:** The last tracked household member leaves the home area.
- **Conditions:** Everyone has remained away for 10 to 15 minutes, Guest or Staying Home mode is off, and no recent indoor activity suggests someone remains.
- **Action:** Set the shared house state to Away, turn off nonessential lights, apply a safe thermostat setback, and notify the household.
- **Wait / timeout:** Start with 15 minutes. Shorten it only after several weeks without a false activation.
- **Stop condition:** Someone returns, indoor activity appears during the delay, or a person selects Home, Guest, or Staying Home.
- **Manual override:** A visible Home or Guest control cancels Away immediately.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Decide who is home**

Use your platform's built-in presence feature, usually driven by each family member's phone location or its connection to the home network, rather than a dedicated product. Every person and guest still needs a safe path through the logic.

</div>
<div class="product-item" markdown="1">

**Detect recent indoor activity**

[Aeotec SmartThings Motion Sensor](https://www.amazon.com/dp/B095TZTGNB/ref=nosim?tag=madsk0f-20). Use activity as a reason to delay Away, not as proof that the home is empty.

</div>
<div class="product-item" markdown="1">

**Adjust heating and cooling**

[ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC/ref=nosim?tag=madsk0f-20). Keep safe minimum and maximum temperatures at the thermostat.

</div>
<div class="product-item" markdown="1">

**Control fixed lights**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Physical paddles must keep working.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Create one shared state with at least Home, Away, and Guest values.
2. Add every tracked household member, then test each person's arrival and departure independently.
3. Create an obvious Guest or Staying Home control before enabling automatic Away.
4. Start with only a notification that says Away would have activated.
5. After a week of correct notifications, allow reversible actions such as turning off nonessential lights.
6. Add thermostat changes only with safe heating and cooling limits. Use the [safe thermostat auto-away guide](/automation/climate/safe-thermostat-away.html) to account for pets, pipes, unavailable sensors, and manual holds.
7. Treat locks, garage doors, alarms, cooking appliances, and space heaters as separate safety automations with their own tests.

## Platform notes

Presence is a reason to delay Away, not proof that the house is empty. Preserve a visible Guest or Staying Home override whichever platform runs the routine.

### Amazon Alexa

I could not verify current geofence and multi-person presence behavior as universal Alexa routine capabilities. Use Alexa for this pattern only after confirming the exact arrival and departure triggers available in the household's app and region; never let an unverified presence rule control access or safety equipment.

### SmartThings

SmartThings calls phone presence **Get your location from this phone**. Use the correct All or Any behavior for multiple residents, and keep a [Manually run Routine](https://support.smartthings.com/hc/en-us/articles/360051931952-Routines-in-SmartThings) as the Guest or Staying Home override.

### Hubitat

Hubitat [Mode Manager](https://docs2.hubitat.com/en/apps/mode-manager) can change mode from presence sensors. A conservative pattern sets Away only after every tracked resident has departed and exits Away when any resident returns. Add delay and recent indoor activity as reasons not to leave Home mode.

### Home Assistant

Home Assistant may be a technical fit for combined presence signals, but I have not personally run it. Verify every tracker and retain the same delay, override, and safe-default requirements.

## Safe first actions

### Start here

- Set the shared house state to Away.
- Turn off nonessential interior and decorative lights.
- Apply a modest thermostat setback within safe limits.
- Send a notification listing exactly what changed.
- Enable other automations that already use Away as a condition.

### Add only after separate testing

- Locking exterior doors.
- Closing a garage door.
- Arming an alarm with interior motion sensors.
- Switching off an appliance that may be unsafe to interrupt remotely.
- Starting a robot vacuum where pets, cords, or closed doors may create problems.

## Advanced features

### Use a pending-away stage

Set a temporary Pending Away state as soon as the last tracked person leaves. During the delay, cancel it if motion, a door event, or a manual override suggests someone remains. Promote it to Away only when the delay finishes cleanly.

### Distinguish a short trip from vacation

Normal Away mode should make reversible daily changes. Vacation mode can use different climate limits, water monitoring, lighting patterns, and notification rules, but it should be selected explicitly rather than inferred from a long absence.

### Keep away lighting separate

Away mode can enable an [away-lighting recipe](/automation/security/away-lights.html), but it should not contain the entire lighting schedule. Separating the state from its consumers makes failures easier to understand.

## Failure modes

- **Away activates while someone is home:** Increase the delay, fix the missing person's presence signal, and make Guest or Staying Home easier to find.
- **Away never activates:** Identify which person or device remains falsely present. Do not silently ignore a stuck signal.
- **A phone battery dies:** Treat missing data as uncertain, not automatically away.
- **Someone returns during the delay:** Cancel Pending Away and leave the house in Home mode.
- **Someone returns just after activation:** Switch to Home immediately and reverse only the actions that are safe to reverse.
- **The thermostat changes too far:** Enforce safe temperature limits on the thermostat itself, independent of Away mode.
- **The hub or internet is down:** Physical switches, locks, alarm controls, and thermostat controls must remain usable.

## FAQ

### How long should away mode wait after everyone leaves?

Start with 10 to 15 minutes. A delayed away mode is less disruptive than a false activation while a child, guest, or person without a phone is still home.

### Is phone location enough to know the house is empty?

No. Phones can be left behind, run out of battery, or report the wrong location. Use a delay, recent motion or door activity, and a guest override.

### Should away mode automatically lock doors and arm an alarm?

Add security actions only after the household has tested presence detection and the security system's own entry, exit, and emergency behavior.

## Related recipes

- [Safe thermostat auto-away for pets and pipes](/automation/climate/safe-thermostat-away.html)
- [Away lighting](/automation/security/away-lights.html)
- [Outdoor night lights](/automation/lighting/outdoor-night-lights.html)
- [Prepare the house when someone arrives](/automation/daily-routines/unlock-door-arrival.html)
- [Daily routine automations](/automation/daily-routines/index.html)

<div class="page-navigation">
  <a href="/automation/daily-routines/index.html">Back to daily routine automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
