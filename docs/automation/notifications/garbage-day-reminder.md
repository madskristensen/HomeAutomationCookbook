---
layout: automation
title: Set up a garbage day reminder tile
description: A platform-neutral recipe that turns a dashboard tile red before garbage day and green again once the task is marked done.
keywords: garbage reminder, trash day, dashboard automation, virtual switch, weekly reminder
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: What happens if I forget to mark the tile as done?
    answer: The tile stays red until it is tapped or an auto-reset automation clears it the next morning. Either way, nothing is lost; the reminder simply persists until acknowledged.
  - question: Can I track more than one type of collection with this?
    answer: Yes, create a separate virtual switch and tile for each collection type, such as trash, recycling, and yard waste, since they often run on different schedules.
  - question: Should this account for holiday schedule changes?
    answer: If the local collection service publishes a calendar, checking it as a condition avoids a false reminder on a week when collection is skipped. Otherwise, the reminder runs on a fixed weekly schedule.
---

# Set up a garbage day reminder tile

Turn a dashboard tile red the evening before garbage day, and green again once the task is marked complete.

**Best for:** A household using a shared dashboard that already displays other status tiles, with a consistent weekly collection schedule.

**Not for:** A household without any shared dashboard; a simple phone notification may be a better fit in that case.

## Why this exists

A phone notification about trash day is easy to dismiss and forget. A tile that stays a visible color until the task is actually done gives a persistent reminder instead of a one-time alert, without needing any new hardware.

## Logic

<div class="automation-example">IF it is the evening before collection day
THEN turn on the "garbage out" virtual switch
(tile turns red on the dashboard)

IF the tile is tapped
OR it is the morning after collection day
THEN turn off the "garbage out" virtual switch
(tile returns to its normal color)</div>

- **Trigger:** A fixed time the evening before collection, such as 6:00 PM on the day before pickup.
- **Conditions:** None required for the basic version; a calendar check can be added if the collection schedule varies.
- **Action:** Turn on the virtual switch tied to the dashboard tile, which turns the tile red.
- **Wait / timeout:** The tile stays red until manually cleared.
- **Stop condition:** Tapping the tile, or an optional auto-reset the morning after collection, turns the virtual switch off again.
- **Manual override:** The tile can always be tapped directly regardless of the schedule.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Track and display the reminder**

No personally verified recommendation yet. This only needs a virtual switch or variable and a dashboard tile; no physical hardware is required.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Create a virtual switch or variable to represent the reminder's state.
2. Add a dashboard tile linked to that switch, with a clear color difference between the "needs attention" and "done" states.
3. Schedule the switch to turn on the evening before the actual collection day.
4. Confirm tapping the tile turns the switch back off, so the household has a simple way to clear the reminder.
5. If the collection schedule changes for holidays, consider checking a published collection calendar as a condition before the reminder fires.

## Advanced features

### Multiple collection types

Create a separate virtual switch and tile for each collection type, such as trash, recycling, and yard waste, since they often run on different days or frequencies.

### Auto-reset after collection

Add a second automation that turns the switch off automatically the morning after collection, in case the tile was never tapped, so it does not stay stuck on for the rest of the week.

## Failure modes

- **Reminder appears at the wrong time:** Check the hub's time zone setting and confirm any daylight saving adjustment is correct.
- **Tile does not change color:** Confirm the tile is linked to the correct virtual switch and refresh the dashboard if it is showing a cached view.
- **Reminder is forgotten because the tile was never tapped:** Add the auto-reset automation so the tile clears itself the next morning regardless.
- **Reminder fires on a week collection is skipped:** Add a calendar condition if the local service publishes a schedule.

## FAQ

### What happens if I forget to mark the tile as done?

The tile stays red until it is tapped or an auto-reset automation clears it the next morning. Either way, nothing is lost; the reminder simply persists until acknowledged.

### Can I track more than one type of collection with this?

Yes, create a separate virtual switch and tile for each collection type, such as trash, recycling, and yard waste, since they often run on different schedules.

### Should this account for holiday schedule changes?

If the local collection service publishes a calendar, checking it as a condition avoids a false reminder on a week when collection is skipped. Otherwise, the reminder runs on a fixed weekly schedule.

## Related recipes

- [Use status tiles instead of notifications](/automation/notifications/status-tiles.html)
- [Set up a maintenance reminder dashboard](/automation/notifications/maintenance-reminder-dashboard.html)
- [Set up a pet feeding reminder](/automation/notifications/pet-feeding-reminder.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>