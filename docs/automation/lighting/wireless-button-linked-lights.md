---
layout: automation
date: 2026-09-24
title: Control lights with a wireless button or linked switch
description: Let a physical button, remote, or smart switch control other lights while every room keeps an understandable manual fallback.
keywords: wireless light button, smart light remote, one switch controls multiple lights, linked smart switches, scene controller
last_modified_at: 2026-09-24
image: /assets/img/social/recipes/lighting/wireless-button-linked-lights.png
compact: true
faqs:
  - question: Should one button toggle the lights or have separate on and off actions?
    answer: Separate on and off actions are more predictable. Use toggle only when every controlled light reliably reports current state and the group cannot drift out of sync.
  - question: Can a smart switch control lights that are not wired to it?
    answer: Yes when the switch exposes button or scene events, or when compatible devices support a direct association or binding. Keep the local load and remote behavior understandable if the hub is unavailable.
  - question: What if the remote or hub stops working?
    answer: Each light should still have a familiar local control. A linked control adds convenience; it should not become the only way to use a room.
---

# Control lights with a wireless button or linked switch

<figure class="content-hero">
  <img src="/assets/img/social/recipes/lighting/wireless-button-linked-lights.svg" alt="A wireless button or wall switch sends predictable on and off commands to several lights" width="1200" height="630">
</figure>

Put a physical control where it is useful, then let it operate one light, a group of lights, or a tested scene without taking away the controls already in each room.

**Best for:** Bedside controls, chair-side lamps, rooms with an inconvenient switch location, detached lamps, and one wall switch that should coordinate nearby lights.

**Not for:** Hiding the only control in an app, cutting power to smart bulbs, or making one room unusable when the hub or wireless path is unavailable.

## Why this exists

Voice and phone controls are useful when they are optional. A button or familiar wall control is faster, works for guests, and does not require anyone to remember a phrase.

The reusable pattern is to separate the physical input from the lighting action. The button reports an intentional press. The rule sends explicit commands to the approved lights. Every light still has a normal way to be controlled locally.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Provide a physical input**

No personally verified wireless button recommendation yet. Use a compatible button, remote, or scene-capable wall switch that reports distinct press events and battery or unavailable state.

</div>
<div class="product-item" markdown="1">

**Control fixed lighting**

A smart wall switch or dimmer that keeps its paddle working locally. See [recommended gear](/getting-started/device-guide.html#lighting-control) for switches I have used.

</div>
</div>

## Logic

<div class="automation-example">IF the top button is pressed
THEN turn on the approved light group

IF the bottom button is pressed
THEN turn off the approved light group

IF the dim-up or scene button is pressed
THEN apply the tested brightness or scene

IF the button or control is unavailable
THEN leave every local light control working</div>

- **Trigger:** A distinct button press, remote action, or scene event.
- **Conditions:** The control is available, the command is allowed for the current time or mode, and no manual override is active.
- **Action:** Send an explicit on, off, dim, or scene command to the selected lights.
- **Wait / timeout:** None for on and off. For press-and-hold dimming, stop when the release event arrives or a short safety timeout expires.
- **Stop condition:** The command completes once the target lights report their expected state, or the platform reports that confirmation is unavailable.
- **Manual override:** Every light keeps its own wall switch, lamp control, or other familiar local control.

## Setup notes

1. Choose one narrow job, such as turning off the downstairs lights from the bedroom.
2. Confirm the button reports separate events for the presses you plan to use.
3. Start with explicit on and off commands instead of toggle.
4. Add only the lights that should always act together.
5. Preserve local control at every connected room or fixture.
6. Name the button action by outcome, such as "Downstairs off," rather than by device number.
7. Test the rule with one target light, then add the rest of the group.
8. Disconnect the hub or wireless path and confirm every local control still works.

## One switch controlling other lights

A scene-capable smart switch can control its wired load normally and also report extra taps or button events to the hub. For example:

- A normal press controls the connected ceiling light.
- A double tap turns on nearby lamps.
- A long press turns off all approved lights on the floor.

Keep the normal press unsurprising. Do not make a basic on action depend on the hub when the switch can control its own load locally.

Some compatible devices support direct association or binding, which can let one device command another without routing each press through the hub. This may improve resilience, but support varies by protocol, device, driver, command type, and group size. Verify that the direct path does not create duplicate commands or remove centralized visibility.

## Smart bulbs need continuous power

If the targets are smart bulbs, do not let an ordinary wall switch cut their power. Use a compatible wall controller, scene device, or wall module that leaves the bulbs powered.

Read [smart bulbs vs. smart switches after a power outage](/articles/smart-bulbs-vs-smart-switches-power-outages.html) before choosing that design. The article covers power recovery, flashing after an outage, Hue wall switch modules, and no-neutral switch tradeoffs.

## Advanced features

### Use scenes for a known result

A scene should set explicit light levels rather than invert whatever happens to be on. "Reading" can set the chair lamp to a tested level and leave the rest of the room unchanged. "Room off" can explicitly turn off only the lights the household approved.

### Make a portable control

A wireless button can move between a bedside table, wheelchair tray, desk, or guest area. Give it a stable label and a predictable job rather than changing its meaning by day.

### Reflect one switch state to other lights

If a smart wall switch should make remote lights follow its local load, react to confirmed on and off state changes. Prevent loops by designating that switch as the source and not reflecting the remote lights back into it.

## Failure modes

- **A toggle press leaves half the group on:** Replace toggle with explicit on and off actions.
- **The same press runs twice:** A direct association and hub rule may both be sending commands. Keep one control path.
- **Remote lights lag behind the wired light:** Prefer local or direct behavior where supported, reduce unnecessary cloud dependencies, and keep the delay acceptable for the room.
- **A smart bulb becomes unavailable:** Its wall power was cut. Replace the ordinary switch pattern with a compatible control.
- **A double tap triggers the normal action too:** Verify the switch or driver exposes distinct scene events before depending on multi-tap behavior.
- **A battery button silently stops working:** Add low-battery and unavailable-device alerts.
- **The hub fails:** The wired switch and every target light's local control remain usable.

## FAQ

### Should one button toggle the lights or have separate on and off actions?

Separate on and off actions are more predictable. Use toggle only when every controlled light reliably reports current state and the group cannot drift out of sync.

### Can a smart switch control lights that are not wired to it?

Yes when the switch exposes button or scene events, or when compatible devices support a direct association or binding. Keep the local load and remote behavior understandable if the hub is unavailable.

### What if the remote or hub stops working?

Each light should still have a familiar local control. A linked control adds convenience; it should not become the only way to use a room.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Use a gentle bathroom night light](/automation/lighting/bathroom-night-light.html)
- [Get low-battery alerts](/automation/notifications/low-battery-alerts.html)
- [Smart bulbs vs. smart switches after a power outage](/articles/smart-bulbs-vs-smart-switches-power-outages.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">Back to lighting automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
