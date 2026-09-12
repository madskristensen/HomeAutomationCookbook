---
layout: automation
title: Run the vacuum only while the house stays empty
description: A platform-neutral recipe that starts a robot vacuum only after confirming the home is empty and sends it back to the dock the moment anyone returns.
keywords: robot vacuum automation, presence-based cleaning, robot vacuum when away, smart vacuum scheduling, vacuum return protection
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/appliances/vacuum-when-empty.png
compact: true
faqs:
  - question: How is this different from a simple auto-start recipe?
    answer: This recipe adds a once-per-day limit and immediately docks the vacuum if anyone returns early, instead of only starting a cleaning cycle.
  - question: What happens if someone comes home while the vacuum is cleaning?
    answer: The vacuum is sent back to its dock as soon as the tested presence signal reports anyone home, rather than finishing the room it is in.
  - question: Can this run more than once if someone leaves and returns several times in a day?
    answer: No. A per-day flag prevents a second run once the vacuum has completed a cycle that day.
---

# Run the vacuum only while the house stays empty

<figure class="content-hero">
  <img src="/assets/img/social/recipes/appliances/vacuum-when-empty.svg" alt="" width="1200" height="630">
</figure>

Start the robot vacuum only after the home is confirmed empty, limit it to once a day, and send it back to the dock immediately if anyone returns early.

**Best for:** Households that want the vacuum to stay out from underfoot completely, including sending it home the moment someone returns.

**Not for:** A household without a presence signal tested across every regular occupant, or a vacuum that cannot be commanded to dock from automation.

## Why this exists

A vacuum that starts when the house is empty is only half the job. It also needs to stop cleaning and return to its dock the moment anyone comes home early, and it should not restart every time someone steps out briefly during the same day.

## Logic

<div class="automation-example">IF the tested presence signal reports the home as empty
AND the vacuum has not completed a cycle today
THEN wait a short confirmation period
IF the home is still reported empty
THEN start the vacuum's cleaning cycle
AND mark the daily run as complete

IF the tested presence signal reports anyone home
AND the vacuum is currently cleaning
THEN send the vacuum back to its dock immediately</div>

- **Trigger:** The tested presence signal reports the home as empty during the chosen daytime window.
- **Conditions:** The vacuum has not already completed a cycle today.
- **Action:** Wait briefly to confirm the departure is real, then start cleaning.
- **Wait / timeout:** If the confirmed-empty period ends before the wait completes, skip the run for today.
- **Stop condition:** As soon as the presence signal reports anyone home, send the vacuum back to its dock immediately, whether or not the room it was cleaning is finished.
- **Manual override:** The vacuum's own app or button can start, stop, or dock it at any time regardless of this automation.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Confirm the whole household has left and returned**

Use your platform's built-in presence feature (phone location or network connection) rather than a dedicated product. Test it against both departure and arrival for every household member before trusting it.

</div>
<div class="product-item" markdown="1">

**Robot vacuum with remote dock command**

No personally verified recommendation yet. Confirm the vacuum accepts a return-to-dock command from automation, not only a manual app tap.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist.

## Setup notes

1. Confirm the presence signal against a week of real comings and goings for every household member before using it here.
2. Choose a daytime window and add a short confirmation wait before starting, as in the simpler auto-start recipe.
3. Track a per-day completed flag so a brief errand does not trigger a second run once today's cycle already finished.
4. Reset the per-day flag at a fixed time, such as midnight.
5. Add the return-to-dock action as its own rule so it fires immediately, independent of the start logic.
6. Test by starting the vacuum manually and then simulating an early return to confirm it docks promptly.

## Advanced features

### Skip a day intentionally

Offer a simple manual control that skips today's run, for a day someone is working from home without leaving.

### Notify on completion

Send one notification when the vacuum reports it has returned to its dock after a completed cycle.

## Failure modes

- **Vacuum keeps cleaning after someone returns:** Confirm the dock command is wired to the presence signal directly, not only checked at the next scheduled interval.
- **Vacuum runs again the same day:** Confirm the per-day flag is being set and is not being reset by an unrelated automation.
- **Vacuum never starts:** Confirm the presence signal actually reports empty during the chosen window and that the per-day flag was reset that day.
- **Vacuum docks and immediately restarts:** Separate the stop logic from the start logic so a docking event does not itself look like a new empty-house signal.
- **The presence signal disagrees with reality:** Stop relying on it and retest with a longer confirmation wait rather than tuning indefinitely.

## FAQ

### How is this different from a simple auto-start recipe?

This recipe adds a once-per-day limit and immediately docks the vacuum if anyone returns early, instead of only starting a cleaning cycle.

### What happens if someone comes home while the vacuum is cleaning?

The vacuum is sent back to its dock as soon as the tested presence signal reports anyone home, rather than finishing the room it is in.

### Can this run more than once if someone leaves and returns several times in a day?

No. A per-day flag prevents a second run once the vacuum has completed a cycle that day.

## Related recipes

- [Start the robot vacuum when everyone leaves](/automation/appliances/robot-vacuum-auto-start.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)

<div class="page-navigation">
  <a href="/automation/appliances/index.html">Back to appliance automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>