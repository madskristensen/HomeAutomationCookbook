---
layout: automation
title: Set up a teeth brushing reminder for kids
description: A platform-neutral recipe that uses a power-monitoring smart plug on an electric toothbrush charger to confirm brushing happened, with a reminder if it did not.
keywords: teeth brushing reminder, kids routine automation, smart plug power monitoring, toothbrush charger sensor
last_modified_at: 2026-08-30
faqs:
  - question: Does this work with a manual, non-electric toothbrush?
    answer: Not directly. This recipe relies on detecting a power draw change when an electric toothbrush is removed from its charger, so it needs an electric toothbrush and a power-monitoring plug.
  - question: What if a child brushes but forgets to put the toothbrush back?
    answer: The automation only detects that the toothbrush was removed from the charger, not that it was actually used or returned. It is a reasonable proxy, not a certainty, and should be treated that way.
  - question: Can this be tied to a reward or chore system?
    answer: Yes, if the platform supports it, a successful morning and evening brushing detection can update a tracked count or virtual switch used elsewhere in a rewards routine.
---

# Set up a teeth brushing reminder for kids

Use a power-monitoring smart plug on an electric toothbrush charger to detect when the toothbrush is removed, as a proxy for brushing happening, with a reminder if it does not happen by a set time.

**Best for:** A household with kids using an electric toothbrush on a dedicated charger, wanting a lightweight nudge without manual check-ins.

**Not for:** A manual, non-electric toothbrush; there is no power draw to detect in that case.

## Why this exists

Reminding kids to brush their teeth often falls on a parent to check manually. Detecting when the toothbrush is picked up off its charger, based on the change in power draw, gives an automated proxy for whether brushing likely happened, without needing to physically check.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect the toothbrush being removed from its charger**

No personally verified recommendation yet. This specifically needs a smart plug with power or wattage monitoring, which is a different capability than the basic on/off plug jobs already covered.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The smart plug's reported power draw drops, indicating the toothbrush was removed from the charger, or a scheduled check runs near a target brushing time.
- **Conditions:** A removal has not already been detected within the current brushing window, such as morning or evening.
- **Action:** Log the brushing window as complete when a removal is detected; send a reminder notification if the target time passes without one.
- **Wait / timeout:** The reminder is sent once per missed window, not repeatedly.
- **Stop condition:** A detected removal for the current window clears any pending reminder for that window.
- **Manual override:** A parent can always mark a brushing window complete manually if the plug misses a detection.

<div class="automation-example">IF the toothbrush charger's power draw drops below its baseline
THEN mark the current brushing window (morning or evening) as complete

IF the target time for a brushing window passes
AND that window has not been marked complete
THEN send a reminder notification: "Time to brush teeth"</div>

## Setup notes

1. Plug the toothbrush charger into a smart plug that supports power or wattage monitoring, not just basic on/off control.
2. Observe the plug's normal power draw while charging, to establish a baseline for detecting removal.
3. Set a threshold drop from that baseline that reliably indicates the toothbrush was picked up.
4. Define morning and evening brushing windows with a target time for each.
5. Test by removing the toothbrush and confirming the platform correctly logs the window as complete.

## Advanced features

### Streak tracking

Track consecutive days with both windows completed, and tie it into a simple reward system if the platform supports counters or variables.

### Multiple children

If more than one child uses a separate electric toothbrush and charger, repeat the setup with its own smart plug and tracked windows per child.

## Failure modes

- **Removal is not detected:** Recheck the baseline power draw and threshold; some chargers draw very little power, making a drop harder to detect reliably.
- **False detection without actual brushing:** The plug only detects removal from the charger, not use; this is a known limitation, not a bug, and should be communicated to the household as such.
- **Reminder fires even after brushing happened:** Confirm the detected removal is being correctly logged against the current window before the target time passes.
- **Baseline power draw drifts over time:** Periodically re-check the baseline, since some chargers vary slightly as the battery ages.

## Done when

- [ ] The smart plug reliably reports power draw for the toothbrush charger.
- [ ] A real removal is detected and logged as a completed window.
- [ ] A missed window produces exactly one reminder.
- [ ] The household understands this detects removal, not confirmed brushing.

## FAQ

### Does this work with a manual, non-electric toothbrush?

Not directly. This recipe relies on detecting a power draw change when an electric toothbrush is removed from its charger, so it needs an electric toothbrush and a power-monitoring plug.

### What if a child brushes but forgets to put the toothbrush back?

The automation only detects that the toothbrush was removed from the charger, not that it was actually used or returned. It is a reasonable proxy, not a certainty, and should be treated that way.

### Can this be tied to a reward or chore system?

Yes, if the platform supports it, a successful morning and evening brushing detection can update a tracked count or virtual switch used elsewhere in a rewards routine.

## Related recipes

- [Set up baby sleep mode](/automation/notifications/baby-sleep-mode.html)
- [Start the morning routine](/automation/daily-routines/morning-routine.html)
- [Start a wind-down bedtime routine](/automation/daily-routines/bedtime-routine.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>