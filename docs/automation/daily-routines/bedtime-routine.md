---
layout: automation
title: Run a bedtime routine without surprising the household
description: A platform-neutral bedtime routine that separates a gentle wind-down from an intentional good-night action and preserves occupied rooms, safety alerts, and manual control.
keywords: bedtime routine automation, good night routine, night mode automation, family bedtime automation, smart home bedtime
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: Should bedtime run automatically at a fixed time?
    answer: Use a schedule to offer or begin a limited wind-down, not to put the entire home into Night mode. Require an intentional button, phrase, or control for the final good-night action.
  - question: Should the routine lock doors and close the garage?
    answer: Start by reporting their status. Add a command only after each lock or door has separate position feedback, obstruction handling, and a tested manual fallback.
  - question: What should quiet mode never silence?
    answer: Keep smoke, carbon-monoxide, water-leak, security, medical, and other urgent household alerts outside routine notification muting.
---

# Run a bedtime routine without surprising the household

Offer a gentle wind-down, then use an intentional good-night signal to change Night mode and turn off only the lights that are safe to change.

**Best for:** Families with different bedtimes, occupied common rooms, guests, and a need for predictable path lighting after dark.

**Not for:** A fixed-time "all off" command, automatic garage movement, unverified lock or security changes, or muting urgent safety alerts.

## Why this exists

Bedtime is rarely one moment for everyone. Someone may be finishing homework, arriving late, hosting a guest, feeding a baby, or using the kitchen. A schedule that suddenly darkens the home or locks an expected person out is not helpful.

Separate the recipe into two stages: a reversible wind-down and an intentional final transition. The final stage changes only the devices the household has approved.

## Logic

<div class="automation-example">IF the wind-down schedule arrives
AND the home is in normal Home mode
THEN offer wind-down with a cancel action
AND gently adjust only approved shared-room lights

IF someone intentionally starts Good night
THEN change Home mode to Night
AND turn off approved unoccupied lights
AND preserve path lighting and urgent alerts
AND report anything that still needs a person</div>

- **Trigger:** A scheduled wind-down prompt or an intentional good-night button, phrase, or control.
- **Conditions:** The home is occupied, no emergency mode is active, and the selected stage is allowed in the current Home or Guest mode.
- **Action:** For wind-down, gently adjust only approved shared-room lights. For good night, set Night mode, turn off approved unoccupied lights, preserve path lighting, apply an approved climate setting, and report unresolved door or appliance status.
- **Wait / timeout:** Give delayed light changes a visible cancel window and cancel them when someone manually changes that room.
- **Stop condition:** Complete one pass, report anything needing a person, and do not repeat until Night mode ends.
- **Manual override:** Wall controls, thermostat controls, urgent alerts, and a one-action cancel always remain available.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Start bedtime**

A "Good night" phrase or manual scene control. The final trigger should be intentional and available without an app.

</div>
<div class="product-item" markdown="1">

**Dim selected lights**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20). Wall paddles remain normal controls before, during, and after the routine.

</div>
<div class="product-item" markdown="1">

**Apply an approved sleep setting**

[ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC/ref=nosim?tag=madsk0f-20). Respect manual holds, safety limits, and the open-window pause recipe.

</div>
<div class="product-item" markdown="1">

**Report open doors or windows**

[SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL/ref=nosim?tag=madsk0f-20). Report status first; do not treat a contact sensor as proof that a door is locked.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. List the devices the final routine may change. Leave everything else out.
2. Create separate Wind-down and Good-night actions.
3. Make Wind-down optional, limited to shared-room lighting, and easy to cancel.
4. Require an intentional trigger before setting Night mode.
5. Exclude occupied rooms, guest rooms, children's rooms, stairs, bathrooms, and emergency path lighting from broad off commands.
6. Use door, window, garage, lock, and appliance information as a checklist before adding any control command.
7. Keep safety alerts outside quiet-notification rules.
8. Test each action separately, then test the complete routine with someone intentionally staying awake.

## Build a night checklist

Status is safer than control for the first version:

| Check | Initial behavior |
|---|---|
| Exterior door or window open | Name the opening and ask a person to inspect it |
| Lock state unknown | Report unknown; do not infer locked from a closed contact sensor |
| Garage position unknown | Report unknown; do not issue a blind close command |
| Washer or dryer running | Leave power alone and show the current state |
| Thermostat on manual hold | Preserve the hold |
| Urgent incident active | Cancel bedtime changes that could hide or hinder the response |

Add control later only when feedback, obstruction behavior, manual fallback, and household expectations have been verified for that exact device.

## Advanced features

### Scope bedtime by person

A child's bedtime can affect only that bedroom and nearby path lighting. The final household Good-night action can run later without replaying the earlier room changes.

### Hand rooms back to local automation

After the routine sets an initial state, occupancy and wall controls should take over. Do not keep forcing a room dark after someone turns its light back on.

### Delay non-urgent notifications

Queue routine summaries until morning, but keep urgent leak, fire, carbon-monoxide, medical, and security alerts immediate.

## Failure modes

- **Lights change while someone is using the room:** Require occupancy-aware exclusions or remove the room from the broad scene.
- **A fixed schedule starts Night mode too early:** Make the schedule a prompt and keep final activation intentional.
- **A manual light change is reversed:** Cancel pending actions for that device or room.
- **A guest room is affected:** Use a Guest-mode scope that excludes private rooms and global announcements.
- **A late arrival is locked out:** Report lock status until household arrival expectations and lock feedback are explicitly verified.
- **The thermostat fights another recipe:** Preserve manual holds, safety limits, and climate automation ownership.
- **Urgent alerts become quiet:** Exempt all safety and security channels from notification muting.
- **The hub is unavailable:** Wall switches, thermostat controls, keys, and manual door operation still work.

## FAQ

### Should bedtime run automatically at a fixed time?

Use a schedule to offer or begin a limited wind-down, not to put the entire home into Night mode. Require an intentional button, phrase, or control for the final good-night action.

### Should the routine lock doors and close the garage?

Start by reporting their status. Add a command only after each lock or door has separate position feedback, obstruction handling, and a tested manual fallback.

### What should quiet mode never silence?

Keep smoke, carbon-monoxide, water-leak, security, medical, and other urgent household alerts outside routine notification muting.

## Related recipes

- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)
- [Bathroom night lighting](/automation/lighting/bathroom-night-light.html)
- [Daily routines](/automation/daily-routines/index.html)

<div class="page-navigation">
  <a href="/automation/daily-routines/index.html">Back to daily routines</a>
  <a href="/automation/index.html">View all automations</a>
</div>
