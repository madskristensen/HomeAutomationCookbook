---
layout: automation
title: Get notified about entrance activity that may indicate a delivery
description: A platform-neutral recipe that uses an outdoor motion sensor near the front door to send a phone notification about entrance activity that may indicate a delivery.
keywords: package delivery alert, delivery notification, outdoor motion sensor, front porch sensor, entrance activity detection
last_modified_at: 2026-08-30
faqs:
  - question: Will this only trigger for actual deliveries?
    answer: No. It triggers on any motion near the front door, including people walking by, so it is a "something happened at the door" alert rather than a confirmed delivery alert.
  - question: How is this different from a video doorbell's delivery detection?
    answer: A video doorbell with package recognition is more specific, but this recipe describes a plain motion sensor approach, which is simpler and works without a camera.
  - question: Does the sensor need to be rated for outdoor use?
    answer: Yes, if it is mounted outside a covered porch or in an area exposed to weather. Standard indoor motion sensors are not designed for that exposure.
---

# Get notified about entrance activity that may indicate a delivery

Use a motion sensor near the front door to send a phone notification about entrance activity that may indicate a delivery, without claiming to confirm one.

**Best for:** A front entrance where packages are commonly left, and a household that wants a heads up without a video doorbell.

**Not for:** Confirming an actual package arrived; this only detects motion, not the presence of a package itself.

## Why this exists

Missing a delivery notification from a carrier, or not hearing a knock, can mean a package sits outside longer than it should. A motion sensor near the entrance gives a general heads up that something happened at the door, prompting a quick check.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect motion near the front entrance | No personally verified recommendation yet | No personally verified recommendation yet | This specifically needs a sensor rated for outdoor exposure if it is mounted outside; the motion sensor options already covered are evaluated for indoor use. |

See [recommended gear](/gear.html) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The entrance motion sensor detects movement.
- **Conditions:** No motion has already been detected within a short cooldown window, to avoid repeat notifications for the same visit.
- **Action:** Send a phone notification, such as "Motion detected at the front door."
- **Wait / timeout:** None; the notification is sent as soon as motion is detected.
- **Stop condition:** Not applicable; each motion event is a separate notification, subject to any cooldown.
- **Manual override:** None needed; this is a passive alert rather than a controllable device.

<div class="automation-example">IF the front entrance motion sensor detects movement
AND no motion has been detected in the last 5 minutes
THEN send a phone notification: "Motion detected at the front door"</div>

## Setup notes

1. Mount a motion sensor rated for the entrance's actual exposure, whether that is a covered porch or a fully exposed area.
2. Aim the sensor to cover the area packages are typically left, without pointing at a public sidewalk or street where it would trigger constantly.
3. Add a cooldown, such as 5 minutes, so a single visitor does not generate repeat notifications while lingering near the door.
4. Test the notification by walking through the sensor's detection area.

## Advanced features

### Time-of-day filtering

Suppress or lower the notification priority overnight, when deliveries are unlikely and the alert is more likely to be about something else worth noting differently.

### Combine with a camera snapshot

If a camera already covers the entrance, attach a snapshot to the notification so it is possible to see what triggered the motion without walking to the door.

## Failure modes

- **Sensor triggers constantly from street traffic:** Adjust the sensor's position or angle to narrow its detection area to the entrance itself.
- **Sensor misses a delivery:** Check its detection range and confirm it covers where packages are actually placed, not just the walkway.
- **Repeated notifications for one visit:** Increase the cooldown period.
- **Sensor fails outdoors after a period of use:** Confirm it is actually rated for the exposure level at its mounting location; an indoor-rated sensor will degrade faster outside.

## Done when

- [ ] The sensor reliably detects motion in the area packages are left.
- [ ] A single visit produces one notification, not several.
- [ ] The sensor does not trigger constantly from unrelated street activity.
- [ ] The sensor is rated appropriately for its actual outdoor exposure.

## FAQ

### Will this only trigger for actual deliveries?

No. It triggers on any motion near the front door, including people walking by, so it is a "something happened at the door" alert rather than a confirmed delivery alert.

### How is this different from a video doorbell's delivery detection?

A video doorbell with package recognition is more specific, but this recipe describes a plain motion sensor approach, which is simpler and works without a camera.

### Does the sensor need to be rated for outdoor use?

Yes, if it is mounted outside a covered porch or in an area exposed to weather. Standard indoor motion sensors are not designed for that exposure.

## Related recipes

- [Get a phone notification when a traditional doorbell rings](/automation/notifications/doorbell-notification.html)
- [Set up away mode](/automation/daily-routines/away-mode.html)
- [Turn on lights when motion is detected](/automation/lighting/lights-on-motion.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>