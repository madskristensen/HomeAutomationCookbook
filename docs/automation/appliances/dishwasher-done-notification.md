---
layout: automation
date: 2025-11-28
title: Dishwasher finished notification
description: Learn the dishwasher's power or vibration pattern and send one reliable completion alert without controlling appliance power.
keywords: dishwasher finished alert, dishwasher notification, dishwasher power monitoring, kitchen appliance automation, dishwasher done notification
last_modified_at: 2026-09-21
image: /assets/img/social/recipes/appliances/dishwasher-done-notification.png
compact: true
faqs:
  - question: What signal proves a dishwasher cycle is actually finished?
    answer: Look for a sustained drop to the dishwasher's stable idle level after it has already been confirmed running. A single low reading during a pause between wash phases is not proof of finished.
  - question: Why does the automation need to remember that the dishwasher was running?
    answer: Without a running marker, an idle dishwasher, or a monitoring device that just reconnected, can look finished and send a false alert.
  - question: Should the automation turn off power to the dishwasher?
    answer: No. Use any monitoring device only to observe, and keep its relay on. Do not remotely interrupt a wash or dry cycle.
---

# Get notified when the dishwasher finishes

<figure class="content-hero">
  <img src="/assets/img/social/recipes/appliances/dishwasher-done-notification.svg" alt="A dishwasher completion alert after the wash cycle finishes" width="1200" height="630">
</figure>

Learn the dishwasher's own running pattern, confirm a real cycle happened, and send one alert once it settles into its finished state.

**Best for:** Dishwashers whose electrical load can be observed safely and whose running and finished states are clearly different.

**Not for:** An unverified inline monitoring device, a shared circuit with combined readings, or a dishwasher whose pause between wash phases looks the same as its finished state.

## Why this exists

A dishwasher full of clean dishes is easy to forget when it is tucked under the counter. A useful alert has to tell a completed cycle apart from a pause between wash phases, a delayed start, and a monitoring device that just reconnected after an outage.

The reliable pattern is stateful: prove the dishwasher was running before treating sustained settling as done.

## Logic

<div class="automation-example">IF dishwasher power or vibration stays above the calibrated running threshold
THEN mark the dishwasher as running

IF the signal stays below the calibrated finished threshold
AND the dishwasher is marked as running
AND the low period is longer than any normal pause between wash phases
THEN send one "Dishwasher finished" notification
AND mark dishes as waiting
AND clear the running marker</div>

- **Trigger:** Measured power or vibration stays above the dishwasher's calibrated running threshold long enough to prove a cycle started.
- **Conditions:** Monitoring data is current and the dishwasher was not already marked as running.
- **Action:** Mark the dishwasher as running and clear any previous waiting-dishes state.
- **Wait / timeout:** After a real start, wait until the signal remains below the calibrated finished threshold longer than the dishwasher's longest normal pause between wash phases.
- **Stop condition:** Mark the cycle finished, send one notification, and set a waiting-dishes state.
- **Manual override:** A person can clear the waiting state without affecting the dishwasher.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Observe dishwasher power or vibration**

No personally verified recommendation yet. I have not verified a monitoring device rated for this appliance's load and startup current. Do not assume a general-purpose smart plug is suitable; a [vibration sensor](/getting-started/device-guide.html#vibration-sensing) may be a safer non-invasive alternative.

</div>
<div class="product-item" markdown="1">

**Clear the waiting-dishes state**

A manual dashboard or phone action. A manual reset is simpler and more reliable than an unverified door sensor.

</div>
</div>

See the full [gear guide](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Do not buy an inline monitor until its voltage, continuous-current, startup-current, grounding, and appliance-load ratings have been checked against the dishwasher and its manual.

## Setup notes

1. Check the dishwasher manual and nameplate before connecting any inline monitoring device.
2. Configure the monitoring device as observe-only. Keep its relay on and exclude it from broad "turn everything off" routines.
3. Record power or vibration through at least three complete cycles, including the modes the household actually uses.
4. Identify a running threshold that idle noise never reaches.
5. Identify a finished threshold and a delay longer than every pause seen between wash phases.
6. Create separate running and waiting-dishes states.
7. Test with silent logging before enabling notifications.
8. Enable one completion alert, then add a quiet reminder only if it proves useful.

## Advanced features

### Add one restrained reminder

Set a waiting-dishes state when the first alert is sent. If it is still set after a household-chosen interval, send one quiet reminder. Clear it manually rather than guessing from a door sensor.

### Respect quiet hours

Keep the completion event in history, but delay speaker announcements until daytime. A phone notification can remain silent overnight.

### Show data health

Display unavailable or stale monitoring as unknown, not idle. Missing measurements must never count as a finished cycle.

## Failure modes

- **Alert arrives during a pause between wash phases:** Lower the finished threshold, lengthen the delay, or use a different signal.
- **No alert arrives:** Confirm the running marker was set and that recent readings continued through the end of the cycle.
- **Alert arrives while the dishwasher is idle:** Require a sustained running state before completion can trigger.
- **Duplicate alerts arrive:** Clear the running marker atomically with the first completion alert.
- **The monitoring device reconnects at zero:** Treat unavailable-to-zero transitions as startup recovery, not completion.
- **Someone turns off the monitoring plug:** Restore power manually and remove the device from all remote shutoff routines.
- **The monitor is not rated for the dishwasher:** Remove it. Use a properly rated monitor or have an electrician install circuit-level monitoring.

## FAQ

### What signal proves a dishwasher cycle is actually finished?

Look for a sustained drop to the dishwasher's stable idle level after it has already been confirmed running. A single low reading during a pause between wash phases is not proof of finished.

### Why does the automation need to remember that the dishwasher was running?

Without a running marker, an idle dishwasher, or a monitoring device that just reconnected, can look finished and send a false alert.

### Should the automation turn off power to the dishwasher?

No. Use any monitoring device only to observe, and keep its relay on. Do not remotely interrupt a wash or dry cycle.

## Related recipes

- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)
- [Get notified when the dryer finishes](/automation/appliances/dryer-done-notification.html)
- [Appliance automations](/automation/appliances/index.html)

<div class="page-navigation">
  <a href="/automation/appliances/index.html">Back to appliance automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>