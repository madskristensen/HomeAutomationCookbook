---
layout: automation
date: 2026-10-05
title: Limit an IR-controlled mini-split
description: Send only a capped infrared setpoint. Never trust blaster state, and keep the physical remote.
keywords: mini split automation, IR blaster air conditioner, window AC setpoint limit, infrared climate control, hard temperature limit
last_modified_at: 2026-10-05
image: /assets/img/social/recipes/climate/mini-split-ir-setpoint-limit.png
compact: true
faqs:
  - question: Can I trust the IR blaster's on or off state?
    answer: No. A blaster records what it sent. It does not know whether the mini-split or window unit received the command, or which mode and setpoint the unit is actually holding.
  - question: What if the remote only has a power toggle and temperature up and down?
    answer: Leave that unit on the physical remote. A toggle can turn the unit the wrong way, and repeated up or down presses walk the setpoint because the hub cannot see the starting point.
  - question: Should this change the unit when nobody is home?
    answer: Only inside limits you would already leave set on the unit itself, and only if someone can notice a missed command. A weak away signal is the wrong reason to send infrared.
---

# Keep a mini-split or window unit inside a hard setpoint limit

{% include content-hero.html src="/assets/img/social/recipes/climate/mini-split-ir-setpoint-limit.svg" alt="An infrared blaster sends a capped setpoint while the physical remote stays in the room" %}

An IR blaster can press buttons. It cannot tell you whether the mini-split or window unit heard them, which mode it is in, or what setpoint it is holding. Send only a temperature inside a hard cap. The manufacturer's remote stays in the room and wins.

**Best for:** A mini-split or window air conditioner with a discrete infrared code for the setpoint you intend to send, plus a separate thermometer you have checked against a known reading.

**Not for:** A power button that toggles, a remote that only steps the temperature up and down, or any unit you cannot keep under a hard heat ceiling and a hard cool floor.

## Why this exists

The quiet failure of infrared is a hub that says "sent" while the room does something else. Power was a toggle, a press was missed, or the unit was already in the other mode because someone used the remote an hour ago.

A hard cap does not make a missed command visible. It stops the rule from being the thing that walks the unit to an extreme because a loop thought it was helping. Heat has a ceiling. Cool has a floor. The automation is not allowed to ask for anything outside them.

## Logic

<div class="automation-example">IF the room stays outside the allowed band
AND the thermometer reading is recent
AND the command is inside the hard heat ceiling and cool floor
AND nobody has used the physical remote since the last command
THEN send one discrete infrared setpoint command
AND wait long enough for the room to move before sending again

DO NOT send a power toggle
DO NOT send a temperature outside the cap
DO NOT treat the last infrared command as the unit's state</div>

- **Trigger:** The room temperature stays outside the band you chose for that mode.
- **Conditions:** The reading is recent, the command is inside the hard cap, heat or cool was chosen on purpose, and the physical remote has not been used since the last send.
- **Action:** Send one discrete setpoint code. Prefer a single code that means the mode and temperature together.
- **Wait / timeout:** Wait long enough to see whether the room actually moves. Do not repeat the correction in a tight loop.
- **Stop condition:** The room is back inside the band, the sensor goes stale, someone uses the remote, or the command would fall outside the cap.
- **Manual override:** The manufacturer's remote wins. After anyone uses it, stop automatic sends until the next day or until someone turns the rule back on.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Send infrared commands**

No personally verified recommendation yet. Confirm the blaster can send the exact discrete code you intend. A successful send in the app is not proof the unit changed.

</div>
<div class="product-item" markdown="1">

**Read the room**

No personally verified recommendation on this page. Use a thermometer or sensor you have compared with a known reading, placed where people actually are. For a room sensor I have used on its own, see the [cold-room alert](/automation/climate/room-heater-maintain-temp.html). That does not mean it was tested here with an infrared blaster.

</div>
<div class="product-item" markdown="1">

**Control the unit by hand**

The remote that came with the mini-split or window unit. Keep it in the room. If the unit itself has a limit or lock, set that too, so the hub is not the only place the cap exists.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist.

## Setup notes

1. Write the heat ceiling and the cool floor on a card by the remote, and put the same numbers in the rule. The rule refuses to send anything outside them.
2. Leave a gap between the hottest heat command and the coldest cool command. If a command is missed, the two modes should not be able to chase each other.
3. Use discrete codes. One code for a specific cool or heat setpoint is usable. A power toggle is not. Temperature up or down, pressed several times, is not, because you cannot see the starting point.
4. Put the thermometer out of the sun and off the blaster. Compare it with a known thermometer before the rule is allowed to send anything.
5. If the sensor has not reported inside its normal interval, send nothing. A stale room is an unknown room.
6. Send one command, then wait. Repeating a discrete code can be reasonable. Repeating up and down is how the setpoint walks away from you.
7. A person chooses heat or cool for the season, or with an obvious mode control. Do not infer the mode from the last infrared command.
8. If anyone uses the physical remote, pause automatic sends. The state you remember is now wrong.
9. Test the refusal first. Aim the blaster away, or leave the unit off, and confirm the rule will send a legal command and will refuse an illegal one. Then send one real command with someone in the room watching the unit, not the app.

Some mini-splits have a real integration that reports mode, setpoint, and on or off. If you have that, and you have watched the reported state match the unit, use the reported state and still keep the cap and the remote. This recipe is for the infrared-only case, where the hub can talk and cannot listen.

## Platform notes

The platform has to send a specific infrared code and read a separate thermometer. The blaster's own on or off tile is not the air conditioner. See the [platform guides](/platforms/index.html) for the broader fit.

### Amazon Alexa

Infrared skills and routine actions vary by device and region. I could not verify a universal Alexa routine that reads a separate thermometer and refuses a command outside a hard cap. Prefer the physical remote unless the exact code and the refusal both test cleanly.

### SmartThings

Use this only when the blaster exposes the discrete command you mean, and a separate temperature sensor is available to the routine or rule. An advanced [SmartThings Rule](https://developer.smartthings.com/docs/automations/rules) is a better fit than a simple routine if you need the cap, the stale-data check, and the pause after manual use. Do not treat the blaster device state as the unit.

### Hubitat

[Rule Machine](https://docs2.hubitat.com/en/apps/rule-machine/rule-5-1) can express a cap, a wait, and a stop after the remote is used. You still need a thermometer driver and a blaster driver that sends the intended code. I do not have a personally verified blaster to name here.

### Home Assistant

Home Assistant is a technical fit for a capped infrared command, but I have not personally run it. Verify the current climate or remote integration, especially whether it reports real unit state or only the last code sent.

## Advanced features

### Show that the last command was only a send

Put the last code, the time, and a plain "unconfirmed" label where the household can see it. A green on tile teaches the wrong lesson.

### Keep empty-house changes boring

A false Away signal is a bad reason to send infrared. Read [why arrive and leave triggers fail](/articles/why-arrive-leave-triggers-fail.html) before any empty-house climate change, and keep setbacks inside the limits in [safe thermostat auto-away](/automation/climate/safe-thermostat-away.html) even when the equipment is a mini-split instead of a central thermostat.

## Failure modes

- **The app says sent and the room does not change:** The blaster missed. Check aim, distance, sunlight on the receiver, and whether someone was standing in the way. Believe the room.
- **The unit turned the wrong way:** Power was a toggle, or the mode was not what you remembered. Stop automating that code.
- **The setpoint walked hotter or colder over the day:** Up and down presses are stacking. Switch to a discrete code or stop the rule.
- **The manufacturer's schedule fights the hub:** Pick one owner. Two schedules will undo each other.
- **Power came back at a factory setpoint:** The hub cap does nothing while the hub is down. Use the unit's own limit if it has one, and check the room after an outage.
- **A stale thermometer requested a change the room no longer needed:** Send nothing until the reading is fresh.
- **A guest used the remote and the rule undid it:** Manual use has to pause the rule. The remote stays the override.
- **The hub is down:** The physical remote still works. That is the point of leaving it in the room.

## FAQ

### Can I trust the IR blaster's on or off state?

No. A blaster records what it sent. It does not know whether the mini-split or window unit received the command, or which mode and setpoint the unit is actually holding.

### What if the remote only has a power toggle and temperature up and down?

Leave that unit on the physical remote. A toggle can turn the unit the wrong way, and repeated up or down presses walk the setpoint because the hub cannot see the starting point.

### Should this change the unit when nobody is home?

Only inside limits you would already leave set on the unit itself, and only if someone can notice a missed command. A weak away signal is the wrong reason to send infrared.

## Related recipes

- [Safe thermostat auto-away](/automation/climate/safe-thermostat-away.html)
- [Pause HVAC when a window stays open](/automation/climate/thermostat-windows-open.html)
- [Monitor a cold room without smart-plug heater control](/automation/climate/room-heater-maintain-temp.html)
- [Why arrive and leave triggers fail](/articles/why-arrive-leave-triggers-fail.html)
- [Climate automations](/automation/climate/index.html)

{% include page-navigation.html
  left_url="/automation/climate/index.html"
  left_label="Back to climate automations"
  right_url="/automation/index.html"
  right_label="View all automations"
%}
