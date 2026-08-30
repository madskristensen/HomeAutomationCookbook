---
layout: automation
title: Get low battery alerts for smart home devices
description: A platform-neutral recipe that notifies when a battery-powered sensor, lock, or button drops below a set level, before it fails silently.
keywords: low battery alert, smart home battery, device battery notification, battery monitoring, smart device maintenance
last_modified_at: 2026-08-30
faqs:
  - question: What battery percentage should trigger a warning?
    answer: Around 20 to 25 percent is a reasonable starting point for most sensors, giving a few weeks of remaining life to plan a replacement. A smart lock is worth a slightly higher threshold, since running out unexpectedly is more disruptive.
  - question: Why does a device's battery sometimes jump straight from fine to dead?
    answer: Some devices only report a simple "ok" or "low" state instead of a percentage, or their battery chemistry drops voltage quickly near the end of its life. Where only a state is available, treat "low" as the trigger instead of a percentage threshold.
  - question: Should every device get the same alert priority?
    answer: No. A water leak sensor or smart lock losing power is more urgent than a motion sensor, so it is worth treating a small set of critical devices as higher priority than the rest.
---

# Get low battery alerts for smart home devices

Get a notification when a battery-powered device drops below a set level, so it can be replaced before the device stops working silently.

**Best for:** Any platform that reports battery percentage or a low-battery state for its connected sensors, locks, or buttons.

**Not for:** A device that does not report battery status at all; nothing can be automated against a reading that is not available.

## Why this exists

A dead battery in a motion sensor, door sensor, or lock does not usually announce itself. It just stops reporting, and the automations relying on it quietly stop working. A proactive alert catches this before it turns into a missed automation or, worse, a lock that will not open.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect low battery levels | No personally verified recommendation yet | No personally verified recommendation yet | This depends on the platform reporting battery data for each device, not on any single piece of hardware. |

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** A monitored device's battery level drops below its set threshold, or reports a "low battery" state.
- **Conditions:** The device has not already been flagged within the last several days, to avoid repeat alerts for the same drop.
- **Action:** Send a notification naming the device and its battery level.
- **Wait / timeout:** None; the notification is sent once the condition is met.
- **Stop condition:** The alert resets once the battery is replaced and reports a normal level again.
- **Manual override:** Battery levels can always be checked directly in the platform regardless of the automation.

<div class="automation-example">IF a monitored device's battery drops below its threshold
AND this device has not been flagged in the last 7 days
THEN send a notification: "[Device name] battery is at [level]"</div>

## Setup notes

1. Confirm which devices actually report battery data in the platform; some devices only expose a simple low-battery flag rather than a percentage.
2. Set a threshold, such as 20 to 25 percent, as a starting point, and adjust based on how quickly a specific device's battery tends to drop.
3. Add a cooldown so the same device does not send repeat alerts every time its reading is checked while still below the threshold.
4. Identify a small set of critical devices, such as locks and water leak sensors, and consider giving them a lower threshold or higher-priority notification.
5. Keep a small stock of the common battery types used across devices so a replacement does not require an extra trip.

## Advanced features

### Tiered alert levels

Use two thresholds, such as 25 percent for an early notice and 10 percent for an urgent one, so the household gets more time to plan a replacement before it becomes critical.

### Daily consolidated report

Instead of a separate notification per device, send one daily summary listing every device currently below its threshold, to reduce notification fatigue on days with several low devices.

## Failure modes

- **Battery reading jumps from fine to dead with no warning:** Some devices only report a simple low-battery state rather than a percentage; treat that state itself as the trigger instead of expecting a gradual decline.
- **Battery percentage fluctuates and causes repeat alerts:** Add a cooldown, or require the drop to hold for a period before alerting, rather than reacting to every reading.
- **A device is missing from monitoring:** Confirm it actually reports battery data to the platform; not every device type does.
- **Too many notifications arrive:** Raise the threshold slightly, add a longer cooldown, or switch to a consolidated daily report.

## Done when

- [ ] Every device expected to report battery status is confirmed to actually do so.
- [ ] A real low-battery condition produces exactly one notification, not several.
- [ ] Critical devices, such as locks, are treated with appropriate priority.
- [ ] The alert clears once a battery is replaced.

## FAQ

### What battery percentage should trigger a warning?

Around 20 to 25 percent is a reasonable starting point for most sensors, giving a few weeks of remaining life to plan a replacement. A smart lock is worth a slightly higher threshold, since running out unexpectedly is more disruptive.

### Why does a device's battery sometimes jump straight from fine to dead?

Some devices only report a simple "ok" or "low" state instead of a percentage, or their battery chemistry drops voltage quickly near the end of its life. Where only a state is available, treat "low" as the trigger instead of a percentage threshold.

### Should every device get the same alert priority?

No. A water leak sensor or smart lock losing power is more urgent than a motion sensor, so it is worth treating a small set of critical devices as higher priority than the rest.

## Related recipes

- [Set up water leak response](/automation/security/water-leak-response.html)
- [Set up away mode](/automation/daily-routines/away-mode.html)
- [Start a wind-down bedtime routine](/automation/daily-routines/bedtime-routine.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>