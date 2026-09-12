---
layout: automation
title: Start the robot vacuum when everyone leaves
description: A platform-neutral recipe that starts a robot vacuum only after a tested presence signal confirms the home is empty, and only during a daytime window.
keywords: robot vacuum automation, auto start vacuum, vacuum when away, presence detection vacuum, away mode cleaning
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/appliances/robot-vacuum-auto-start.png
compact: true
faqs:
  - question: What proves the house is actually empty?
    answer: Only a presence signal you have tested for every regular occupant. A single phone leaving a geofence is not enough if other household members or their phones behave differently.
  - question: Why restrict the vacuum to a daytime window?
    answer: A daytime window avoids starting the vacuum during sleeping hours if a presence signal is briefly wrong, and matches when the house is normally empty.
  - question: What should happen if someone comes home while the vacuum is running?
    answer: Send it back to its dock immediately. See the companion recipe for returning-early handling.
---

# Start the robot vacuum when everyone leaves

<figure class="content-hero">
  <img src="/assets/img/social/recipes/appliances/robot-vacuum-auto-start.svg" alt="" width="1200" height="630">
</figure>

Once a tested presence signal confirms the home is empty during a daytime window, start the robot vacuum's existing cleaning cycle.

**Best for:** A household with a presence signal that has been tested for every regular occupant and a robot vacuum with its own scheduling and app control.

**Not for:** A single untested phone-location trigger, night hours, or a vacuum with no reliable dock or error reporting.

## Why this exists

Vacuuming is more useful, and less disruptive, when nobody is underfoot and no pet is startled by it. The trigger only matters if it reliably reflects that everyone has actually left; an unverified presence signal can start the vacuum while someone is still home.

## Logic

<div class="automation-example">IF the tested presence signal reports the home as empty
AND the time is within the daytime window
AND the vacuum has not already run today
THEN wait a short confirmation period
IF the home is still reported empty
THEN start the vacuum's cleaning cycle

IF the presence signal reports that someone returned while the vacuum is cleaning
THEN send the vacuum back to its dock</div>

- **Trigger:** The tested presence signal reports the home as empty.
- **Conditions:** The time is within the chosen daytime window, Guest mode is off, and the vacuum has not already run today.
- **Action:** Wait briefly to confirm the departure is real, then start the vacuum's existing cleaning cycle.
- **Wait / timeout:** Skip the run if the confirmed-empty period ends before the wait completes.
- **Stop condition:** The vacuum finishes, or the tested presence signal reports that someone returned; in either case, send it back to its dock.
- **Manual override:** The vacuum's own app or button can start or stop it at any time regardless of this automation.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Confirm the whole household has left**

Use your platform's built-in presence feature (phone location or network connection) rather than a dedicated product. Test whatever signal is available against real daily patterns before trusting it, since not every phone or platform behaves the same way.

</div>
<div class="product-item" markdown="1">

**Robot vacuum with app control**

No personally verified recommendation yet. Confirm the vacuum supports remote start, reports errors, and can be sent back to its dock from automation before relying on this recipe.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist.

## Setup notes

1. Confirm the presence signal against at least a week of real household comings and goings before using it to start anything.
2. Choose a daytime window that matches when the home is normally empty.
3. Add a short confirmation wait after the empty signal to avoid reacting to a brief false departure.
4. Disable automatic starts while Guest mode is active so a visitor without a tracked presence signal is not treated as an empty home.
5. Track whether the vacuum has already run today so a return-and-leave-again pattern does not start a second run.
6. Confirm the vacuum reports docked, cleaning, and error states before relying on any of them.
7. Test manually with someone intentionally staying home, then with someone returning during a test run.

## Advanced features

### Skip when maintenance is needed

Check that the vacuum is docked and not already reporting an error or a full bin before starting a new cycle.

### Notify on a stuck vacuum

Send an alert if the vacuum reports an error state during a cycle so it is not left stuck for hours.

## Failure modes

- **Vacuum starts while someone is still home:** The presence signal is not reliable enough. Add a longer confirmation wait or combine more than one tested signal.
- **Vacuum runs more than once a day:** Track a per-day run flag and reset it at a fixed time, such as midnight.
- **Vacuum gets stuck:** Clear obstacles and closed-off areas the vacuum can wander into, and add a stuck-error notification.
- **Vacuum does not start:** Confirm it is docked, charged, and not already reporting an error before the automation runs.
- **The presence signal disagrees with reality:** Stop relying on it and retest, rather than tuning the delay indefinitely.

## FAQ

### What proves the house is actually empty?

Only a presence signal you have tested for every regular occupant. A single phone leaving a geofence is not enough if other household members or their phones behave differently.

### Why restrict the vacuum to a daytime window?

A daytime window avoids starting the vacuum during sleeping hours if a presence signal is briefly wrong, and matches when the house is normally empty.

### What should happen if someone comes home while the vacuum is running?

Send it back to its dock immediately. See the companion recipe for returning-early handling.

## Related recipes

- [Run the vacuum only while the house stays empty](/automation/appliances/vacuum-when-empty.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)

<div class="page-navigation">
  <a href="/automation/appliances/index.html">Back to appliance automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>