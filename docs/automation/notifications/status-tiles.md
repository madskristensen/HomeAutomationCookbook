---
layout: automation
title: Use status tiles instead of notifications
description: A platform-neutral recipe that replaces one-time push notifications with persistent dashboard tiles for household status information.
keywords: status tiles, dashboard status, notification alternative, smart home dashboard, persistent status display
last_modified_at: 2026-08-30
faqs:
  - question: Why use tiles instead of just sending more notifications?
    answer: Notifications are easy to dismiss without acting on them, and too many of them get ignored entirely. A tile stays visible until the underlying condition changes, so it does not rely on someone reacting the moment it fires.
  - question: Does this replace notifications completely?
    answer: Not necessarily. Time-sensitive alerts, such as a water leak, are still worth an actual notification. Tiles work best for ongoing status rather than urgent one-time events.
  - question: What kind of information works well as a tile?
    answer: Anything with a clear "needs attention" versus "fine" state, such as garbage day, a maintenance task, a door left open, or a load of laundry waiting to be moved to the dryer.
---

# Use status tiles instead of notifications

Replace one-time push notifications with persistent dashboard tiles that stay visible until the underlying condition is resolved.

**Best for:** A household with a shared dashboard already in use, and recurring status information that tends to get missed as a one-time notification.

**Not for:** Genuinely time-sensitive alerts, such as a security or safety event; those are better served by an actual notification that demands attention.

## Why this exists

A push notification is easy to dismiss with a swipe and then forget entirely. A dashboard tile that stays a visible color until the underlying condition changes works better for ongoing status information, such as garbage day or a pending maintenance task, where the goal is persistent visibility rather than a single alert.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Display persistent status information | No personally verified recommendation yet | No personally verified recommendation yet | This only needs virtual switches or variables and a dashboard; no physical hardware is required. |

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The underlying condition for a given tile changes, such as a scheduled reminder becoming due.
- **Conditions:** None beyond the specific condition each tile is tracking.
- **Action:** Update the tile's virtual switch or variable to reflect the new state, changing its color or label on the dashboard.
- **Wait / timeout:** The tile stays in its current state until the condition changes again.
- **Stop condition:** The condition being tracked resolves, either automatically or by a household member marking it done.
- **Manual override:** Any tile can be manually toggled if the automation misses an edge case.

<div class="automation-example">IF the tracked condition for a tile becomes true
THEN set that tile's virtual switch to its "needs attention" state

IF the tracked condition is resolved
OR the tile is tapped to mark it done
THEN set that tile's virtual switch back to its normal state</div>

## Setup notes

1. Identify recurring status information currently sent as one-time notifications that would work better as a persistent tile.
2. Create a virtual switch or variable for each piece of tracked status.
3. Add a dashboard section with one tile per tracked item, using a clear visual difference between "needs attention" and "fine."
4. Wire each tile's underlying automation to set the switch based on its specific condition, whether that is a schedule, a sensor, or a manual action.
5. Confirm each tile can also be cleared manually, in case its automatic condition does not cover every case.

## Advanced features

### Grouped dashboard section

Group related tiles together, such as all household chores in one section and all maintenance tasks in another, so the dashboard stays organized as more tiles are added.

### Tile history

If the platform supports it, log when each tile last changed state, to see how consistently a recurring task is actually being handled.

## Failure modes

- **A tile never updates:** Confirm the automation driving that tile's virtual switch is actually running and check its trigger conditions.
- **A tile is stuck in the wrong state:** Manually toggle the tile's switch to reset it, and check whether its automation properly handles the reset case.
- **Too many tiles make the dashboard cluttered:** Group related tiles into sections, or remove tiles for status information that is no longer useful.
- **A genuinely urgent event only shows as a tile:** Reserve actual notifications for time-sensitive alerts and use tiles only for ongoing status.

## Done when

- [ ] Each tracked piece of status information has its own tile and clear visual states.
- [ ] Each tile updates correctly based on its underlying condition.
- [ ] Tiles can be cleared manually as a fallback.
- [ ] Genuinely urgent alerts are still sent as actual notifications, not just tiles.

## FAQ

### Why use tiles instead of just sending more notifications?

Notifications are easy to dismiss without acting on them, and too many of them get ignored entirely. A tile stays visible until the underlying condition changes, so it does not rely on someone reacting the moment it fires.

### Does this replace notifications completely?

Not necessarily. Time-sensitive alerts, such as a water leak, are still worth an actual notification. Tiles work best for ongoing status rather than urgent one-time events.

### What kind of information works well as a tile?

Anything with a clear "needs attention" versus "fine" state, such as garbage day, a maintenance task, a door left open, or a load of laundry waiting to be moved to the dryer.

## Related recipes

- [Set up a garbage day reminder tile](/automation/notifications/garbage-day-reminder.html)
- [Add dashboard tiles for music playback controls](/automation/notifications/music-controls.html)
- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>