---
layout: automation
redirect_from:
  - /automation/misc/doorbell-notification.html
date: 2025-11-29
title: Traditional doorbell phone alerts
description: A platform-neutral recipe that wires a contact sensor in parallel with an existing wired doorbell chime so ringing it sends a phone notification.
keywords: doorbell notification, traditional doorbell, dumb doorbell alert, doorbell sensor, contact sensor doorbell
last_modified_at: 2026-10-05
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

Close a contact sensor's dry terminals when the existing doorbell rings, so the press also sends a phone notification without replacing the doorbell.

**Best for:** A household with an existing wired doorbell and chime, and someone comfortable doing simple low-voltage wiring or willing to have it done once.

**Not for:** A doorbell that is already a smart doorbell, or a household not comfortable with any wiring, even low voltage. A standalone smart doorbell may be simpler in that case.

## Why this exists

Not everyone wants to replace a working doorbell with a smart one, especially if the traditional chime is loud enough indoors but easy to miss from the backyard or a distant room. Wiring a contact sensor in parallel with the existing chime adds a notification without changing how the doorbell itself works.

## Logic

<div class="automation-example">IF the contact sensor changes state
AND it has not changed state again within the last 10 seconds
THEN send a phone notification: "Someone is at the front door"</div>

- **Trigger:** The contact sensor changes state when the doorbell press closes its dry terminals.
- **Conditions:** None; every press should notify.
- **Action:** Send a phone notification, such as "Someone is at the front door."
- **Wait / timeout:** None; the notification is sent immediately.
- **Stop condition:** Not applicable; each press is a separate event.
- **Manual override:** The physical doorbell button and chime continue to work exactly as before, independent of the automation.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect the doorbell press**

[Ecolink Z-Wave Plus Door/Window Sensor (DWZWAVE2.5-ECO)](https://www.amazon.com/dp/B01N5HB4U5/ref=nosim?tag=madsk0f-20). The external screws are a non-powered dry contact, in parallel with the built-in magnet. Do not land the doorbell transformer's voltage on them. Use a relay so a press closes those terminals while the chime stays on its own wiring. Keep the magnet away from the sensor when the terminals are in use.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Turn off power to the doorbell transformer before doing any wiring.
2. Treat the sensor terminals as a dry contact. A press should close them through a relay. Do not connect the chime's low-voltage wires directly to the sensor. The original button and chime keep working on their own circuit.
3. Restore power and test by pressing the doorbell button; confirm the sensor changes state in the platform's automation log.
4. Add a short debounce delay, such as 10 seconds, so a single press that causes more than one signal does not send duplicate notifications.
5. If unsure about any part of the wiring, consult an electrician; doorbell transformers are low voltage but the wiring should still be done carefully.

## Advanced features

### Quiet hours behavior

Reduce or silence any accompanying chime sound overnight while still sending the phone notification, so a late visitor does not wake the household unnecessarily.

### Visual alert for accessibility

For a household member who is hard of hearing, add a light flash as part of the same automation so the doorbell is noticeable without relying on sound.

## Failure modes

- **Sensor does not trigger on a press:** Confirm the relay is closing the dry terminals, the magnet is not sitting on the sensor, and the hub saw the state change.
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