---
layout: automation
title: Get an alert when the fridge or freezer door is left open
description: A platform-neutral recipe that alerts when a refrigerator or freezer door has been open too long, with a shorter delay for the freezer and conservative handling of missing sensor data.
keywords: fridge door alert, freezer door notification, refrigerator door left open, food spoilage prevention, door sensor fridge
last_modified_at: 2026-08-30
faqs:
  - question: Why does the freezer need a shorter delay than the fridge?
    answer: Frozen food starts to soften sooner than refrigerated food tolerates a temperature swing, so a shorter open-door delay is safer for the freezer.
  - question: Will normal grocery loading trigger a false alert?
    answer: A door open for a minute or two while unloading groceries should not reach the delay. If it does, lengthen the delay slightly rather than removing it.
  - question: Can the same contact sensor go in both the fridge and the freezer?
    answer: Only if its documented operating temperature range covers the freezer. Check the manufacturer's rating before relying on it below freezing.
---

# Get an alert when the fridge or freezer door is left open

Send one alert when a refrigerator or freezer door has stayed open past a safe delay, with a shorter delay for the freezer.

**Best for:** Households that want a simple reminder before food spoils, energy is wasted, or the compressor runs longer than necessary.

**Not for:** Treating a missing or low-battery sensor reading as a closed door, or as the sole safeguard against a failing appliance.

## Why this exists

A door left open a few seconds while grabbing something is normal. A door left open for several minutes is a problem, and freezer contents tolerate far less warm-up time than refrigerator contents. Two separate delays, one per appliance, keep the alert useful without nagging over routine use.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect an open refrigerator or freezer door**

[SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL). Confirm the manufacturer's operating temperature range before using one inside a freezer rather than a refrigerator.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The fridge or freezer door sensor reports open.
- **Conditions:** The sensor is available and reporting current data.
- **Action:** Start a timer specific to that appliance.
- **Wait / timeout:** The freezer uses a shorter delay than the fridge because frozen food tolerates less warm-up time.
- **Stop condition:** The door closes before the delay elapses, which cancels the alert.
- **Manual override:** Anyone can close the door at any time. The automation only observes.

<div class="automation-example">IF fridge door sensor reports open
AND remains open for the fridge delay
THEN send one "Fridge door left open" notification

IF freezer door sensor reports open
AND remains open for the shorter freezer delay
THEN send one "Freezer door left open" notification

IF either sensor closes before its delay elapses
THEN cancel that pending alert</div>

## Setup notes

1. Mount the sensor body on the door frame and the magnet on the door edge, where the gap stays smallest when closed.
2. Confirm the sensor's rated operating temperature before placing it in a freezer.
3. Time a normal grocery-unloading session and set the fridge delay comfortably longer than that.
4. Set a shorter delay for the freezer to reflect its lower tolerance for warming.
5. Send exactly one alert per open event, and reset it only when the door closes.
6. Test with the door propped open on purpose before trusting the alert during real use.

## Failure modes

- **Alert fires during normal grocery loading:** Lengthen the fridge delay slightly rather than removing the alert.
- **No alert arrives:** Confirm the sensor is paired, has a working battery, and is reporting current data.
- **The sensor stops reporting in cold temperatures:** Replace it with one rated for the freezer's operating range, or move it to the door frame where it may run slightly warmer.
- **Sensor reports the wrong state:** Check the magnet-to-sensor gap and realign it; a gap larger than the manufacturer's spec will misreport.
- **Repeated alerts for one open event:** Reset the pending alert only on a confirmed close, not on every sensor report.
- **A stale or unavailable sensor:** Treat unavailable as unknown, not closed, and mention it in the notification rather than staying silent.

## Done when

- [ ] The fridge and freezer each have their own tested delay.
- [ ] A normal grocery-loading session does not trigger an alert.
- [ ] Propping the freezer door open triggers an alert sooner than propping the fridge door open.
- [ ] Closing the door before the delay elapses cancels the pending alert.
- [ ] Exactly one alert arrives per open event.
- [ ] An unavailable sensor is reported as unknown rather than assumed closed.

## FAQ

### Why does the freezer need a shorter delay than the fridge?

Frozen food starts to soften sooner than refrigerated food tolerates a temperature swing, so a shorter open-door delay is safer for the freezer.

### Will normal grocery loading trigger a false alert?

A door open for a minute or two while unloading groceries should not reach the delay. If it does, lengthen the delay slightly rather than removing it.

### Can the same contact sensor go in both the fridge and the freezer?

Only if its documented operating temperature range covers the freezer. Check the manufacturer's rating before relying on it below freezing.

## Related recipes

- [Low battery alerts](/automation/notifications/low-battery-alerts.html)
- [Detect a water leak before it spreads](/automation/security/water-leak-response.html)
- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)

<div class="page-navigation">
  <a href="/automation/appliances/index.html">Back to appliance automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>