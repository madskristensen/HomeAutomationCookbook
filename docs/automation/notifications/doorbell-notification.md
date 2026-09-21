---
layout: automation
redirect_from:
  - /automation/misc/doorbell-notification.html
date: 2025-11-29
title: Traditional doorbell phone alerts
description: A platform-neutral recipe that wires a contact sensor in parallel with an existing wired doorbell chime so ringing it sends a phone notification.
keywords: doorbell notification, traditional doorbell, dumb doorbell alert, doorbell sensor, contact sensor doorbell
last_modified_at: 2026-09-21
image: /assets/img/social/recipes/notifications/doorbell-notification.png
compact: true
faqs:
  - question: Do I need to replace my doorbell with a smart doorbell?
    answer: No. This recipe wires a contact sensor in parallel with the existing chime, so the original doorbell keeps working exactly as before, and a notification is added on top.
  - question: Is it safe to wire into the doorbell chime?
    answer: Doorbell transformers are typically low voltage, around 16 to 24 volts AC, but power should still be turned off before any wiring work, and anyone unsure should consult an electrician.
  - question: Why do I need a debounce delay in the automation?
    answer: A doorbell button can send more than one signal for a single press. A short debounce window after the first trigger prevents multiple notifications for the same ring.
---

# Get a phone notification when a traditional doorbell rings

<figure class="content-hero">
  <img src="/assets/img/social/recipes/notifications/doorbell-notification.svg" alt="A traditional doorbell sends a phone alert while the existing chime continues to work" width="1200" height="630">
</figure>

Wire a contact sensor in parallel with an existing wired doorbell chime so pressing the doorbell also sends a phone notification, without replacing the doorbell itself.

**Best for:** A household with an existing wired doorbell and chime, and someone comfortable doing simple low-voltage wiring or willing to have it done once.

**Not for:** A doorbell that is already a smart doorbell, or a household not comfortable with any wiring, even low voltage. A standalone smart doorbell may be simpler in that case.

## Why this exists

Not everyone wants to replace a working doorbell with a smart one, especially if the traditional chime is loud enough indoors but easy to miss from the backyard or a distant room. Wiring a contact sensor in parallel with the existing chime adds a notification without changing how the doorbell itself works.

## Logic

<div class="automation-example">IF the contact sensor changes state
AND it has not changed state again within the last 10 seconds
THEN send a phone notification: "Someone is at the front door"</div>

- **Trigger:** The contact sensor changes state, wired in parallel with the doorbell chime circuit.
- **Conditions:** None; every press should notify.
- **Action:** Send a phone notification, such as "Someone is at the front door."
- **Wait / timeout:** None; the notification is sent immediately.
- **Stop condition:** Not applicable; each press is a separate event.
- **Manual override:** The physical doorbell button and chime continue to work exactly as before, independent of the automation.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect the doorbell press**

No personally verified recommendation yet. This job specifically needs a contact sensor with external wire terminals, which is a different requirement than a standard door or window contact sensor.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Turn off power to the doorbell transformer before doing any wiring.
2. Connect the contact sensor's external wire terminals in parallel with the doorbell chime's existing wiring, so the original doorbell circuit is unaffected.
3. Restore power and test by pressing the doorbell button; confirm the sensor changes state in the platform's automation log.
4. Add a short debounce delay, such as 10 seconds, so a single press that causes more than one signal does not send duplicate notifications.
5. If unsure about any part of the wiring, consult an electrician; doorbell transformers are low voltage but the wiring should still be done carefully.

## Advanced features

### Quiet hours behavior

Reduce or silence any accompanying chime sound overnight while still sending the phone notification, so a late visitor does not wake the household unnecessarily.

### Visual alert for accessibility

For a household member who is hard of hearing, add a light flash as part of the same automation so the doorbell is noticeable without relying on sound.

## Failure modes

- **Sensor does not trigger on a press:** Verify the wiring connections at the chime and confirm which terminals were used; test with a multimeter during a press if available.
- **Sensor triggers without anyone pressing the doorbell:** Check for loose connections or electrical interference near the wiring, and confirm the transformer voltage matches what the sensor expects.
- **Multiple notifications for one press:** Add or lengthen the debounce delay in the automation.
- **Notifications arrive with a noticeable delay:** Check the sensor's wireless connection to the hub and consider moving it closer or adding a repeater.

## FAQ

### Do I need to replace my doorbell with a smart doorbell?

No. This recipe wires a contact sensor in parallel with the existing chime, so the original doorbell keeps working exactly as before, and a notification is added on top.

### Is it safe to wire into the doorbell chime?

Doorbell transformers are typically low voltage, around 16 to 24 volts AC, but power should still be turned off before any wiring work, and anyone unsure should consult an electrician.

### Why do I need a debounce delay in the automation?

A doorbell button can send more than one signal for a single press. A short debounce window after the first trigger prevents multiple notifications for the same ring.

## Related recipes

- [Turn on lights when motion is detected](/automation/lighting/lights-on-motion.html)
- [Set up away mode](/automation/daily-routines/away-mode.html)
- [Use status tiles instead of notifications](/automation/notifications/status-tiles.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>