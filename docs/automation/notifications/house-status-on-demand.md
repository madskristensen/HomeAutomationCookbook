---
layout: automation
date: 2026-10-25
title: House status check on demand
description: Press a button and get one push message that sums up the house, with the mode, open windows and doors, the front door lock, air quality, rain, and appliances that are still running.
keywords: house status check, smart home health check, on demand status notification, Hubitat status push, webCoRE status piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/notifications/house-status-on-demand.png
compact: true
faqs:
  - question: Why on demand instead of automatic?
    answer: You only want a full summary at certain moments, like before bed or before leaving. Running it on demand means no extra notifications the rest of the day.
  - question: Why one message instead of several alerts?
    answer: One short message is quick to read. A pile of separate alerts is easy to ignore.
  - question: What does the message say when everything is fine?
    answer: It only says which mode the house is in. Every other line is added only when something needs attention.
---

# House status check on demand

{% include content-hero.html src="/assets/img/social/recipes/notifications/house-status-on-demand.svg" alt="One push message sums up what in the house needs attention" %}

Press one button and get a single push message about the house. It tells you the mode, and then only the things that need attention: an open window or door, an unlocked front door, poor air outside, rain, or an appliance that is not done.

**Best for:** Checking the house before bed, before leaving, or from another room, without opening several apps.

**Not for:** Urgent problems like leaks or smoke. Those need their own alert the moment they happen.

## Why this exists

Before bed or before leaving, I want to know a few things at once. Are the windows closed? Is the front door locked? Is the washer done? Checking each one in an app takes too long. One message that only lists what is wrong answers all of it in a few seconds.

## Logic

<div class="automation-example">WHEN the status check is started from a button or dashboard
THEN start a message with "The house is in [mode] mode."
AND add "A window upstairs is open." if any upstairs window is open
AND add "A window downstairs is open." if any downstairs window is open
AND add "A door is open." if any door is open
OR ELSE add "The front door is unlocked." if it is unlocked
AND add "The outside air quality isn't great." if the outdoor AQI is above 50
AND add "It's raining." if the weather says rain
AND add "[Appliance] is [status]." for each appliance that is not ready
THEN send the message as one push notification</div>

- **Trigger:** A button press, a dashboard tile, or a voice command. Nothing triggers it on its own.
- **Conditions:** Each line has its own check.
- **Action:** Send one push message.
- **Wait / timeout:** None.
- **Stop condition:** The message is sent once per request.
- **Manual override:** Not needed. It only reports.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Know what is open**

Contact sensors on the windows and doors, grouped by floor.

</div>
<div class="product-item" markdown="1">

**Know the outside conditions**

An outdoor air quality sensor and a weather service. I wrote [Hubitat drivers](https://github.com/madskristensen/hubitat-drivers) for PurpleAir air quality and Open-Meteo weather.

</div>
<div class="product-item" markdown="1">

**Know the appliance status**

A way to report whether the dishwasher, dryer, and washer are running or ready. I use a generic appliance driver from the same repo.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Group the window sensors by floor, so the message can say where the open window is.
2. Write each line as a short sentence.
3. Only add a line when something needs attention. A message that is always long stops being read.
4. Put the trigger somewhere easy, like a dashboard tile or a button by the bed.
5. Trim the message before sending so there is no trailing space.

## How I do it in webCoRE

This is a real piston I run on Hubitat. I named it the health status check.

1. Event subscriptions are turned off, so the piston never runs on its own. I start it from a dashboard or a button.
2. It starts a text variable with "The house is in" plus the current mode.
3. It checks the upstairs window group, then the downstairs window group, and adds a line for each that has an open window.
4. If any door is open, it adds "A door is open." If no door is open but the front door is unlocked, it adds "The front door is unlocked."
5. If the PurpleAir AQI is above 50, it adds "The outside air quality isn't great."
6. If the Open-Meteo weather description contains "rain", it adds "It's raining."
7. For the dishwasher, dryer, and washer, if the appliance status is not Ready, it adds "[Appliance] is [status]."
8. It trims the text and sends it as a push notification.

## Advanced features

### Speak it instead

Send the same text to a speaker in the bedroom for a spoken summary at bedtime.

### Add more lines

Low batteries, the garage door, or a thermostat that is off all fit the same pattern.

## Failure modes

- **A line is missing:** Check that the sensor still reports in the hub. An offline sensor reads as closed or ready.
- **Rain never shows up:** Check the exact wording the weather driver uses. The check looks for "rain" in the text.
- **Message never arrives:** Test the push notification device on its own.

## FAQ

### Why on demand instead of automatic?

You only want a full summary at certain moments, like before bed or before leaving. Running it on demand means no extra notifications the rest of the day.

### Why one message instead of several alerts?

One short message is quick to read. A pile of separate alerts is easy to ignore.

### What does the message say when everything is fine?

It only says which mode the house is in. Every other line is added only when something needs attention.

## Related recipes

- [Smart home status tiles](/automation/notifications/status-tiles.html)
- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)
- [Pause HVAC when a window stays open](/automation/climate/thermostat-windows-open.html)

{% include page-navigation.html
  left_url="/automation/notifications/index.html"
  left_label="Back to notifications"
  right_url="/automation/index.html"
  right_label="View all automations"
%}
