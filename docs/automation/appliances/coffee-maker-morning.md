---
layout: automation
title: Prepare morning coffee with a deliberate ready step
description: Prepare the coffee maker the night before and get a clear morning result without wondering whether it was actually made ready.
keywords: morning coffee reminder, delayed brew coffee, coffee ready mode, morning routine, coffee maker safety
last_modified_at: 2026-08-30
faqs:
  - question: Does an off smart plug prove that the coffee maker is loaded?
    answer: No. Plug state says nothing about water, grounds, the carafe, or whether the machine is clean and assembled. Readiness must come from a deliberate person.
  - question: Should a smart plug energize a coffee maker on a schedule?
    answer: This recipe does not recommend that. Use the coffee maker's documented delayed-brew feature or another manufacturer-supported start method.
  - question: What happens if nobody marks the coffee maker ready?
    answer: It does not brew automatically. Send a preparation reminder if useful, then let a person prepare and start it normally.
---

# Prepare morning coffee with a deliberate ready step

A person loads the coffee maker and explicitly marks it ready, then the machine uses its own approved delayed-brew feature for the morning.

**Best for:** Coffee makers with a documented delayed-brew function and households willing to make preparation part of the evening routine.

**Not for:** Treating plug state as proof of preparation, energizing an empty machine remotely, or bypassing the appliance's controls.

## Why this exists

The coffee maker's delayed-brew feature can remove one more step from the morning, while an explicit Ready state keeps anyone from wondering whether it was prepared the night before. An outlet cannot see water, grounds, the carafe, or a blocked basket, so an off plug is not a ready signal.

Keep brewing inside the coffee maker's documented controls. Home automation can remind someone to prepare it and track an explicit Ready for morning state, but it should fail by skipping coffee rather than starting an unprepared heating appliance.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Brew on a schedule | Coffee maker with a documented delayed-brew feature | No personally verified recommendation yet | Follow the appliance instructions, including cleaning and auto-off guidance. |
| Record readiness | A visible note or physical checklist | A deliberate Ready for morning button or mode | Only the person who loaded the machine sets it ready. |
| Remind the household | Evening phone reminder | A reminder near the bedtime routine | The reminder never starts the appliance. |

No coffee maker or remote-start accessory is recommended until I have verified it.

## Logic

- **Trigger:** Evening preparation time or the household bedtime routine.
- **Conditions:** None for the reminder.
- **Action:** Remind a person to load the machine, set its approved delayed-brew controls, and deliberately mark Ready for morning.
- **Wait / timeout:** Clear Ready after the expected brew window whether brewing occurred or not.
- **Stop condition:** A person cancels Ready or the morning window ends.
- **Manual override:** The coffee maker's own controls always remain primary.

<div class="automation-example">AT evening preparation time
THEN remind a person to prepare the coffee maker

IF a person loads and checks the machine
AND sets the machine's own delayed-brew control
THEN the person marks Ready for morning

IF Ready was never set
THEN do not brew automatically</div>

## Setup notes

1. Read the coffee maker's instructions for delayed brew, auto-off, cleaning, water level, basket, and carafe placement.
2. Use only the appliance's documented scheduled-start feature.
3. Create a Ready for morning control that cannot be set by plug state, motion, time, or presence.
4. Put the preparation reminder where it does not wake the household.
5. Clear Ready automatically after the morning window so yesterday's state cannot carry forward.
6. Make Cancel easy from the kitchen and bedtime routine.
7. Keep the appliance's normal buttons and safety features unchanged.

## Preparation checklist

- Add the intended amount of water.
- Add coffee and the correct filter or basket.
- Seat the carafe and basket as the instructions require.
- Check that the machine is clean, undamaged, and on a suitable surface.
- Set the appliance's own delayed-brew time.
- Mark Ready for morning only after those steps are complete.

## Advanced features

### Skip when the morning routine changes

A person can cancel Ready when sleeping late, traveling, or changing plans. Do not infer cancellation solely from phone location.

### Show preparation state

Display Not prepared, Ready for morning, and Expired. Do not display Brewed unless the appliance itself provides a verified status or a person confirms it.

## Failure modes

- **Ready remains set from yesterday:** Expire it after every morning window.
- **The machine is prepared but the schedule is wrong:** Verify its clock and delayed-brew indicator at the appliance.
- **A reminder is ignored:** Skip automatic brewing. Do not substitute an inferred ready state.
- **The carafe or basket is missing:** The person preparing the machine catches it before setting Ready.
- **Power returns after an outage:** Follow the appliance instructions and require preparation again if its clock or schedule reset.
- **The hub is unavailable:** The appliance's documented delayed-brew feature and manual controls remain independent.

## Done when

- [ ] The coffee maker's own instructions support delayed brewing.
- [ ] A person completes the preparation checklist before marking Ready.
- [ ] Plug, motion, time, and presence states cannot mark the machine ready.
- [ ] Ready expires after each morning window.
- [ ] Cancel is available from the normal household routine.
- [ ] Missing preparation results in no automatic brew.
- [ ] Appliance controls and safety features remain unchanged.

## FAQ

### Does an off smart plug prove that the coffee maker is loaded?

No. Plug state says nothing about water, grounds, the carafe, or whether the machine is clean and assembled. Readiness must come from a deliberate person.

### Should a smart plug energize a coffee maker on a schedule?

This recipe does not recommend that. Use the coffee maker's documented delayed-brew feature or another manufacturer-supported start method.

### What happens if nobody marks the coffee maker ready?

It does not brew automatically. Send a preparation reminder if useful, then let a person prepare and start it normally.

## Related recipes

- [Run a good-morning routine](/automation/daily-routines/morning-routine.html)
- [Run a bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Appliance automations](/automation/appliances/index.html)

<div class="page-navigation">
  <a href="/automation/appliances/index.html">Back to appliance automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
