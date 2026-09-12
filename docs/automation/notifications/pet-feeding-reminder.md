---
layout: automation
date: 2025-11-30
title: Set up a pet feeding reminder
description: A platform-neutral recipe that uses a smart button or repurposed sensor to track and remind about pet feeding times.
keywords: pet feeding reminder, pet feeding tracker, smart button pet care, feeding schedule automation
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/notifications/pet-feeding-reminder.png
compact: true
faqs:
  - question: What if more than one person feeds the pet?
    answer: The button or tracked action should be pressed by whoever actually feeds the pet, regardless of who it is. The reminder cares about whether feeding happened, not who did it.
  - question: What happens if feeding is logged twice by accident?
    answer: A double press simply resets the "last fed" timestamp again with no harmful effect; the next reminder timing is based on whichever press was most recent.
  - question: Can this track more than one pet?
    answer: Yes, use a separate button and tracked state for each pet, since they may have different feeding schedules or need separate confirmation.
---

# Set up a pet feeding reminder

<figure class="content-hero">
  <img src="/assets/img/social/recipes/notifications/pet-feeding-reminder.svg" alt="" width="1200" height="630">
</figure>

Use a smart button or repurposed sensor to track when a pet was last fed and send a reminder if too much time passes without it being logged.

**Best for:** A household where feeding responsibilities are shared and it is easy to lose track of whether the pet has already been fed.

**Not for:** A household with a single consistent feeder who already reliably tracks feeding mentally; the added button press may not be worth it.

## Why this exists

When feeding responsibilities are shared across household members, it is easy for everyone to assume someone else already fed the pet, or to forget entirely. A simple button press to log feeding, paired with a reminder if too much time passes, keeps this from slipping through the cracks.

## Logic

<div class="automation-example">IF the feeding button is pressed
THEN reset the "last fed" timestamp to now

IF more than 10 hours have passed since the last fed timestamp
THEN send a reminder notification: "Has the dog been fed?"
AND repeat every 30 minutes until the button is pressed</div>

- **Trigger:** The feeding button is pressed, or a scheduled check runs to see how long it has been since the last press.
- **Conditions:** More time has passed than the expected feeding interval, such as 8 to 12 hours.
- **Action:** Send a reminder notification if feeding has not been logged within the expected window; reset the "last fed" timestamp when the button is pressed.
- **Wait / timeout:** The reminder repeats at intervals, such as every 30 minutes, until feeding is logged.
- **Stop condition:** Pressing the feeding button clears the reminder and resets the timer.
- **Manual override:** The pet can always be fed and the button pressed regardless of the reminder state.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Log a feeding event**

No personally verified recommendation yet. A smart button or a contact sensor repurposed for this job works, but this specific use case is not directly matched by the door and window sensor jobs already covered.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Choose a smart button, or repurpose a contact sensor, as the physical feeding-log trigger, placed somewhere convenient near the feeding area.
2. Create a variable or virtual switch to track the "last fed" timestamp.
3. Set the expected feeding interval, such as 8 to 12 hours, based on the pet's actual schedule.
4. Schedule a check that compares the current time to the last-fed timestamp and sends a reminder once the interval is exceeded.
5. Confirm pressing the button both logs the feeding and clears any active reminder.

## Advanced features

### Multiple pets

Add a separate button and tracked timestamp for each pet, since feeding schedules or reminder intervals may differ between them.

### Escalating reminders

If the first reminder is ignored for an extended period, such as an hour, escalate to a different notification method or a louder in-home alert.

## Failure modes

- **Reminder never clears after feeding:** Confirm the button press is correctly resetting the "last fed" timestamp, not just triggering a one-time action.
- **Reminder fires too early or too late:** Adjust the expected feeding interval to better match the pet's actual schedule.
- **Button is pressed but nothing resets:** Check the button's battery and its connection to the hub.
- **Repeated reminders become annoying:** Lengthen the repeat interval, or add an escalation step instead of repeating the same notification indefinitely.

## FAQ

### What if more than one person feeds the pet?

The button or tracked action should be pressed by whoever actually feeds the pet, regardless of who it is. The reminder cares about whether feeding happened, not who did it.

### What happens if feeding is logged twice by accident?

A double press simply resets the "last fed" timestamp again with no harmful effect; the next reminder timing is based on whichever press was most recent.

### Can this track more than one pet?

Yes, use a separate button and tracked state for each pet, since they may have different feeding schedules or need separate confirmation.

## Related recipes

- [Set up a garbage day reminder tile](/automation/notifications/garbage-day-reminder.html)
- [Use status tiles instead of notifications](/automation/notifications/status-tiles.html)
- [Get low battery alerts for smart home devices](/automation/notifications/low-battery-alerts.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>