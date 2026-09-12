---
layout: automation
title: Home maintenance reminder dashboard
description: A platform-neutral recipe that tracks recurring home maintenance tasks, such as filter changes, on a shared dashboard instead of relying on memory.
keywords: maintenance reminder, home maintenance dashboard, filter change reminder, recurring task tracker, smart home dashboard
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/notifications/maintenance-reminder-dashboard.png
compact: true
faqs:
  - question: How is this different from a phone calendar reminder?
    answer: A calendar reminder is easy to dismiss and forget. A dashboard tile stays visibly overdue until someone marks the task done, which works better for tasks that are easy to keep postponing.
  - question: What tasks work well on this kind of dashboard?
    answer: Recurring tasks with a rough interval rather than an exact date work best, such as changing an HVAC filter every 60 to 90 days, replacing a water filter, or checking smoke detector batteries twice a year.
  - question: Do I need a wall-mounted tablet for this to work?
    answer: No. A shared dashboard on a phone, a tablet, or even a wall-mounted display all work the same way; the important part is that it is somewhere the household actually looks.
---

# Build a home maintenance reminder dashboard

<figure class="content-hero">
  <img src="/assets/img/social/recipes/notifications/maintenance-reminder-dashboard.svg" alt="" width="1200" height="630">
</figure>

Track recurring home maintenance tasks, such as HVAC filter changes, on a shared dashboard so they stay visible instead of relying on memory.

**Best for:** A household with a shared dashboard already in use, and a handful of recurring maintenance tasks that tend to get forgotten.

**Not for:** A single task with an exact one-time deadline; a simple calendar reminder is likely simpler for that.

## Why this exists

Maintenance tasks like changing an HVAC filter or checking smoke detector batteries do not have a hard deadline, which makes them easy to keep pushing back. A dashboard tile that stays visibly overdue until marked done works better than a one-time notification that gets dismissed and forgotten.

## Logic

<div class="automation-example">IF it has been more than 75 days since the HVAC filter was last marked done
THEN mark the "HVAC filter" tile as overdue on the dashboard

IF the "HVAC filter" tile is marked done
THEN reset its overdue state and restart the 75 day interval</div>

- **Trigger:** A fixed interval since the task was last marked done, such as every 60 to 90 days for an HVAC filter.
- **Conditions:** The task has not already been marked done within that interval.
- **Action:** Mark the dashboard tile for that task as overdue.
- **Wait / timeout:** The tile stays overdue until marked done.
- **Stop condition:** Marking the task done resets the interval and clears the tile.
- **Manual override:** Any task can be marked done manually at any time, independent of the schedule.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Track and display maintenance tasks**

No personally verified recommendation yet. This only needs virtual switches or variables and a dashboard; no physical hardware is required.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. List the recurring maintenance tasks worth tracking, along with a rough interval for each one.
2. Create a virtual switch or variable per task to represent its "done" state and the date it was last completed.
3. Add a dashboard section with one tile per task, showing a clear visual difference between "on schedule" and "overdue."
4. Schedule a check that compares the current date to the last completed date and flags a task as overdue once its interval has passed.
5. Confirm marking a tile done resets both its overdue state and its interval starting point.

## Advanced features

### Different intervals per task type

Give each task its own interval instead of a single shared schedule, since an HVAC filter, a water filter, and smoke detector batteries do not follow the same timeline.

### Overdue escalation

Add a secondary notification, separate from the dashboard tile, once a task has been overdue for an extended period, such as two weeks past its interval, so it is not indefinitely ignored.

## Failure modes

- **A task never gets marked overdue:** Confirm the last-completed date was actually recorded when the task was marked done, and check the interval comparison logic.
- **A task shows overdue immediately after being marked done:** Check that the "last completed" timestamp is being updated correctly rather than left at its previous value.
- **Dashboard tiles do not update:** Refresh the dashboard view, since some platforms cache tile states.
- **Too many tasks pile up as overdue at once:** Stagger the initial setup dates so tasks do not all become due in the same week.

## FAQ

### How is this different from a phone calendar reminder?

A calendar reminder is easy to dismiss and forget. A dashboard tile stays visibly overdue until someone marks the task done, which works better for tasks that are easy to keep postponing.

### What tasks work well on this kind of dashboard?

Recurring tasks with a rough interval rather than an exact date work best, such as changing an HVAC filter every 60 to 90 days, replacing a water filter, or checking smoke detector batteries twice a year.

### Do I need a wall-mounted tablet for this to work?

No. A shared dashboard on a phone, a tablet, or even a wall-mounted display all work the same way; the important part is that it is somewhere the household actually looks.

## Related recipes

- [Use status tiles instead of notifications](/automation/notifications/status-tiles.html)
- [Set up a garbage day reminder tile](/automation/notifications/garbage-day-reminder.html)
- [Get low battery alerts for smart home devices](/automation/notifications/low-battery-alerts.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>