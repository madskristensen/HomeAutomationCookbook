---
layout: automation
title: Set a cooking reminder that stays visible until you clear it
description: Keep a visible cooking reminder active until someone clears it, using a deliberate timer or an approved appliance status signal rather than an unsafe workaround.
keywords: stove reminder, oven left on alert, cooking timer, appliance status notification, kitchen safety
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: Can a normal smart plug monitor or shut off a stove or oven?
    answer: No general-purpose plug is recommended here. Ranges and ovens may be hard-wired or use high-current circuits, and gas appliances have additional hazards. Use only equipment approved for the exact appliance and installation.
  - question: Is no motion in the kitchen proof that cooking was abandoned?
    answer: No. Someone may be in another room while food cooks, and a motion sensor can miss a person who is still. Motion can add context but must not decide that a burner is safe.
  - question: Can a temperature sensor near a burner detect whether the stove is on?
    answer: It is not a dependable safety signal. Placement, steam, sunlight, another burner, and residual heat can all produce misleading readings.
---

# Get a stove reminder without pretending it is a safety system

Starting to cook also starts a reminder, and only a person or an appliance-approved status signal clears it.

**Best for:** Households that want a persistent cooking reminder tied to a deliberate timer or a manufacturer-supported appliance status.

**Not for:** Automatic shutoff through a general-purpose smart plug, improvised sensors near burners, or replacing smoke alarms and attentive cooking.

## Why this exists

A visible reminder that stays active until someone acknowledges it is more useful than a sensor guess about what is happening on the stove. It remains a reminder, not a claim that the smart home knows whether every burner is safe, because power, temperature, presence, and motion can all be ambiguous.

Use a timer every time cooking starts. If the appliance exposes a supported status through its manufacturer, that status can improve the message, but it still does not replace checking the controls in person.

## Logic

<div class="automation-example">IF a person starts Cooking mode
THEN start the chosen kitchen timer

IF the timer expires
THEN send a persistent reminder to check every control

CLEAR only after a person checks the appliance
DO NOT infer safe from no motion, low power, or cooling temperature</div>

- **Trigger:** A person deliberately starts Cooking mode or an approved appliance signal reports active cooking.
- **Conditions:** Record which signal started the reminder. Do not require missing motion or Away mode.
- **Action:** Start a visible timer and send a persistent reminder when the chosen interval expires.
- **Wait / timeout:** Use the cook's intended interval, with an earlier check for unfamiliar cooking.
- **Stop condition:** A person checks the appliance controls and clears the reminder.
- **Manual override:** The appliance's normal controls and a physical timer remain available.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Start a cooking reminder**

A physical kitchen timer or deliberate phone timer. Starting the timer must be part of starting the appliance.

</div>
<div class="product-item" markdown="1">

**Read appliance status**

Manufacturer-supported status for the exact appliance. Verify what each state means. Do not infer individual burner state from whole-appliance power.

</div>
<div class="product-item" markdown="1">

**Shut off cooking equipment**

A person uses the appliance controls. No general-purpose smart plug or improvised relay is recommended.

</div>
</div>

## Setup notes

1. Put a physical timer or one-tap Cooking control next to the normal cooking workflow.
2. Make the reminder name the appliance and ask a person to inspect every control.
3. Keep the reminder visible until acknowledged.
4. Do not silence it automatically when the house enters Away or Bedtime.
5. If using manufacturer-supported status, test preheat, normal cycling, residual heat, self-clean, disconnected, and unavailable states.
6. Treat unavailable or ambiguous status as "check the appliance," not "off."
7. Keep working smoke and carbon-monoxide alarms independent of this reminder.

## Advanced features

### Add a leaving-home check

When Away mode begins, remind the last person to check the stove if Cooking mode is still active. Do not remotely report that the stove is off unless the exact appliance provides a verified state.

### Escalate an unacknowledged reminder

Send one follow-up to another responsible adult if the first reminder remains unacknowledged. Avoid repeated messages that train people to ignore it.

## Failure modes

- **Nobody starts Cooking mode:** Keep a physical timer at the appliance and make it part of the cooking habit.
- **The timer is wrong for a long recipe:** Let the cook choose or extend the interval explicitly.
- **Appliance status is unavailable:** Ask for an in-person check and repair the integration.
- **Power appears low while a burner is hot:** Do not clear the reminder from power alone.
- **Motion stops while cooking continues:** Do not treat missing motion as abandonment or safety.
- **A reminder is acknowledged remotely:** Keep the wording focused on checking the physical controls, not merely tapping a notification.

## FAQ

### Can a normal smart plug monitor or shut off a stove or oven?

No general-purpose plug is recommended here. Ranges and ovens may be hard-wired or use high-current circuits, and gas appliances have additional hazards. Use only equipment approved for the exact appliance and installation.

### Is no motion in the kitchen proof that cooking was abandoned?

No. Someone may be in another room while food cooks, and a motion sensor can miss a person who is still. Motion can add context but must not decide that a burner is safe.

### Can a temperature sensor near a burner detect whether the stove is on?

It is not a dependable safety signal. Placement, steam, sunlight, another burner, and residual heat can all produce misleading readings.

## Related recipes

- [Support a fire evacuation](/automation/security/fire-safety.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Run a bedtime routine](/automation/daily-routines/bedtime-routine.html)

<div class="page-navigation">
  <a href="/automation/security/index.html">Back to safety and security automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
