---
layout: automation
title: Pause heating or cooling when a window stays open
description: A platform-neutral climate recipe that pauses HVAC after a window remains open and resumes only when every monitored opening is closed.
keywords: thermostat window sensor, stop HVAC windows open, smart thermostat control, window sensor thermostat, prevent heating outside
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: How long should a window stay open before HVAC pauses?
    answer: Start with two minutes for windows. Use a longer delay or exclude exterior doors that normally open for brief trips.
  - question: When should the thermostat resume?
    answer: Resume only after every monitored window and door has remained closed briefly, and only if this automation was responsible for the pause.
  - question: What if someone changes the thermostat while a window is open?
    answer: Treat the manual thermostat change as the new instruction. Do not restore an older saved mode over it when the window closes.
---

# Pause heating or cooling when a window stays open

Open a window for fresh air, and heating or cooling pauses after a short delay. Close every monitored opening, and the system resumes only if this recipe paused it.

**Best for:** Homes with a controllable thermostat and reliable contact sensors on the windows or patio doors people intentionally leave open.

**Not for:** Briefly used exterior doors, homes with unmonitored openings, or HVAC equipment whose thermostat mode cannot be safely paused and restored.

## Why this exists

Pausing heating or cooling when a window stays open avoids using energy on air that is immediately lost outside. The recipe must ignore quick door trips, remember whether it caused the pause, wait for every monitored opening to close, and avoid undoing a manual thermostat change.

Start with one frequently used window. Expand only after the full pause-and-resume cycle works reliably.

## Logic

<div class="automation-example">IF any monitored window remains open for two minutes
AND heating or cooling is active
THEN mark HVAC as paused by this recipe
AND pause the thermostat

IF every monitored opening remains closed
AND this recipe still owns the pause
THEN restore the saved thermostat mode
AND clear the pause marker</div>

- **Trigger:** Any monitored window or door remains open for two minutes.
- **Conditions:** Heating or cooling is active, climate pause is enabled, and no safety condition requires HVAC to continue.
- **Action:** Record that this recipe owns the pause, save the current thermostat mode if the system can do so reliably, pause HVAC, and identify the opening in a notification.
- **Wait / timeout:** Ignore quick openings. Remind the household if an opening remains open long enough for indoor temperature to become a concern.
- **Stop condition:** Every monitored opening has remained closed briefly.
- **Manual override:** A thermostat change made during the pause cancels automatic restoration of the old state.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Control heating and cooling**

[ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC). Keep safe limits and manual control at the thermostat.

</div>
<div class="product-item" markdown="1">

**Detect an open window or door**

[SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL). Test every open and closed report before enabling HVAC control.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Start with windows people intentionally leave open. Exclude exterior doors used for quick trips.
2. Verify each contact sensor reports open and closed correctly ten times.
3. Create one combined "any monitored opening is open" state.
4. Add a two-minute open delay and a short all-closed delay to prevent rapid cycling.
5. Track whether this recipe paused HVAC. Never resume merely because a window closed.
6. During testing, notify without changing the thermostat.
7. After notifications are reliable, test pause and resume while someone watches the thermostat.

## Safe restoration

The resume half is more important than the pause:

- Resume only when all monitored openings are closed.
- Resume only when the recipe still owns the pause.
- Restore the saved mode, not an assumed seasonal mode.
- If the saved state is missing or invalid, notify instead of guessing.
- If someone manually changed the thermostat, clear recipe ownership and leave their choice alone.
- Keep independent freeze and overheat protection active.

## Advanced features

### Use different delays by opening

A window intended for ventilation can use a short delay. A frequently used patio door needs a longer delay or should be excluded. The goal is to catch sustained openings without cycling HVAC during normal traffic.

### Add a reminder instead of a blinking light

Send one useful notification when HVAC pauses and another only if the opening remains open. Repeated blinking or phone alerts become noise and teach the household to ignore the recipe.

### Show which opening blocks resume

A status tile can list the windows still open. This makes a failed resume understandable without exposing platform-specific implementation details.

## Failure modes

- **HVAC cycles during quick door trips:** Increase that door's delay or remove it from the monitored group.
- **HVAC never resumes:** Find the sensor still reporting open and verify that this recipe owns the pause.
- **The wrong mode resumes:** Do not guess heat, cool, or auto. Validate saved-state handling before enabling restoration.
- **A manual thermostat change is reversed:** Clear recipe ownership whenever the thermostat changes outside this automation.
- **A sensor battery dies while reporting open:** Alert on unavailable or stale sensors and require manual review instead of forcing a resume.
- **Indoor temperature becomes unsafe:** Independent thermostat limits override the automation and notify the household.
- **The hub or internet is down:** The thermostat remains usable at the wall and continues enforcing its own safety limits.

## FAQ

### How long should a window stay open before HVAC pauses?

Start with two minutes for windows. Use a longer delay or exclude exterior doors that normally open for brief trips.

### When should the thermostat resume?

Resume only after every monitored window and door has remained closed briefly, and only if this automation was responsible for the pause.

### What if someone changes the thermostat while a window is open?

Treat the manual thermostat change as the new instruction. Do not restore an older saved mode over it when the window closes.

## Related recipes

- [Safe thermostat auto-away for pets and pipes](/automation/climate/safe-thermostat-away.html)
- [Window open and close notifications](/automation/climate/window-notifications.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Climate automations](/automation/climate/index.html)

<div class="page-navigation">
  <a href="/automation/climate/index.html">Back to climate automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
