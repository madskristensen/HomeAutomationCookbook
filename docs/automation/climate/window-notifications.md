---
layout: automation
title: Get notified when to open or close windows
description: A platform-neutral recipe that compares indoor and outdoor temperature and notifies the household when opening or closing windows would save energy.
keywords: window notification automation, energy saving alerts, when to open windows, temperature notification, natural ventilation
last_modified_at: 2026-08-30
faqs:
  - question: How large should the temperature difference be before notifying?
    answer: Start with a difference of at least 5 degrees Fahrenheit between indoor and outdoor readings. A smaller difference is not worth interrupting anyone for.
  - question: Why require the difference to hold for a while before sending an alert?
    answer: Outdoor temperature can swing briefly with wind, clouds, or a passing shower. Requiring the difference to hold for several minutes avoids notifying on a reading that will not last.
  - question: Should the automation close windows automatically?
    answer: No. This recipe only notifies. Closing or opening a window is a manual action so a person can also check weather, security, and whether the window can be reached safely.
---

# Get notified when to open or close windows

Compare indoor and outdoor temperature, and send one notification when opening or closing windows would take advantage of free heating or cooling.

**Best for:** Homes with a working indoor and outdoor temperature reading that want a reminder instead of running heating or cooling unnecessarily.

**Not for:** Automatically opening or closing any window, or replacing a working thermostat schedule with notification-driven manual habits nobody follows.

## Why this exists

Free heating or cooling from outdoor air is easy to miss without a specific reminder. A one-time notification, sent only when the temperature difference is meaningful and has held steady for a while, is more useful than expecting anyone to check the weather and compare it against the thermostat throughout the day.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Track whether a window is open**

[SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL). Optional. Useful for skipping a notification about a window that is already open.

</div>
<div class="product-item" markdown="1">

**Compare indoor and outdoor temperature**

Many platforms already provide an outdoor reading through an existing weather integration, so a dedicated outdoor purchase may not be needed. For the indoor reading, see [temperature and humidity sensor gear](/getting-started/device-guide.html#climate) if the platform does not already have one placed well.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The gap between indoor and outdoor temperature crosses a chosen threshold in the useful direction for the current season.
- **Conditions:** The gap has held for several minutes, and any tracked windows are currently closed.
- **Action:** Send one notification suggesting windows be opened or closed.
- **Wait / timeout:** Wait for a cooldown period, such as two hours, before sending another notification of the same kind.
- **Stop condition:** The notification is sent once; the household decides whether to act on it.
- **Manual override:** Opening or closing any window is always a manual decision.

<div class="automation-example">IF outdoor temperature is at least 5 degrees warmer than indoor temperature
AND it is heating season
AND the gap has held for several minutes
AND tracked windows are currently closed
THEN send one notification: "Outside is warmer than inside. Consider opening a window."

IF outdoor temperature is at least 5 degrees cooler than indoor temperature
AND it is cooling season
AND the gap has held for several minutes
AND tracked windows are currently closed
THEN send one notification: "Outside is cooler than inside. Consider opening a window."</div>

## Setup notes

1. Confirm both the indoor and outdoor temperature readings are current and reasonably accurate before using them.
2. Choose a minimum temperature difference, starting around 5 degrees Fahrenheit, and adjust only after seeing how often it fires.
3. Require the difference to hold for several minutes before sending a notification.
4. Add a cooldown between notifications so a temperature hovering near the threshold does not send repeated alerts.
5. If window sensors are available, skip the notification for windows already open.
6. Restrict notifications to hours when someone is likely to see and act on them.

## Advanced features

### Include a rain warning

If a window sensor reports open and rain is forecast, send a separate notification suggesting the window be closed.

### Mention an approximate cost difference

Where the platform can estimate it, add a rough cost comparison to the notification to make the suggestion more concrete.

## Failure modes

- **Too many notifications:** Increase the required temperature difference, lengthen the confirmation delay, or add a longer cooldown between alerts.
- **Notifications arrive at unhelpful times:** Restrict them to daytime or waking hours.
- **Notification suggests opening a window that is already open:** Confirm the window-sensor condition is included and the sensor is reporting current data.
- **Outdoor reading looks wrong:** Check the sensor's placement away from direct sun and heat-radiating walls, or confirm the weather integration is using the correct location.
- **No notification arrives when it should:** Confirm both temperature sources are reporting and that the season condition matches the current time of year.

## Done when

- [ ] Indoor and outdoor readings are current and reasonably accurate.
- [ ] A real temperature swing produces exactly one notification.
- [ ] The cooldown prevents repeated notifications for the same swing.
- [ ] An already-open window does not trigger a redundant "open a window" notification.
- [ ] Notifications arrive only during hours someone can act on them.

## FAQ

### How large should the temperature difference be before notifying?

Start with a difference of at least 5 degrees Fahrenheit between indoor and outdoor readings. A smaller difference is not worth interrupting anyone for.

### Why require the difference to hold for a while before sending an alert?

Outdoor temperature can swing briefly with wind, clouds, or a passing shower. Requiring the difference to hold for several minutes avoids notifying on a reading that will not last.

### Should the automation close windows automatically?

No. This recipe only notifies. Closing or opening a window is a manual action so a person can also check weather, security, and whether the window can be reached safely.

## Related recipes

- [Pause heating or cooling when a window stays open](/automation/climate/thermostat-windows-open.html)
- [Run the air purifier when indoor air quality drops](/automation/climate/air-quality-purifier.html)
- [Monitor a cold room without smart-plug heater control](/automation/climate/room-heater-maintain-temp.html)

<div class="page-navigation">
  <a href="/automation/climate/index.html">Back to climate automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>