---
layout: guide
title: Choose smart-home devices by the job
description: A practical checklist for choosing compatible sensors, switches, plugs, and climate devices without relying on generic brand rankings.
last_modified_at: 2026-08-30
---

# Choose smart-home devices by the job

Do not start with a brand or a box of discounted devices. Start with one household job, write the rule in plain English, and identify the capabilities that rule needs.

For named products I have personally used, see [Recommended gear](/gear.html). This page explains how to evaluate everything else.

## Start with the automation

Write these six lines before buying:

1. **Trigger:** What changes?
2. **Conditions:** What must also be true?
3. **Action:** What should happen?
4. **Wait or timeout:** How long should the rule wait?
5. **Stop condition:** What ends or reverses it?
6. **Manual override:** What works when the hub does not?

That list turns "I need a smart sensor" into a testable requirement such as "I need a sensor that reports motion quickly, reports unavailable separately, and works with my hub."

## Choose the control before the sensor

### Fixed lighting

Prefer a wall switch or dimmer when the light serves a shared room. The familiar paddle remains useful to kids and guests. Check neutral-wire requirements, box depth, load type, minimum load, multi-way wiring, and local electrical requirements before buying.

Use a smart bulb when color or per-bulb control matters and the fixture can remain powered. It is usually a poor fit where someone will keep turning off the ordinary wall switch.

### Plug-in loads

A smart plug is not a general-purpose way to automate every appliance. Check the appliance instructions and the plug's supported load type. Do not use a general-purpose plug to control portable heaters, cooking appliances, medical equipment, safety systems, or anything that should not restart when power returns.

### Climate

Keep manual temperature control and safe limits at the thermostat or purpose-built controller. Verify wiring, equipment compatibility, installer requirements, and what happens when a remote sensor or hub is unavailable.

### Locks, doors, and safety equipment

Use equipment approved for the exact job. Hobby motion, location, and contact sensors do not replace alarm listings, entrapment protection, appliance interlocks, or a person's safety check.

## Choose the sensor for the human behavior

| Job | Sensor type to consider | Main limitation |
|---|---|---|
| Detect someone entering | PIR motion | Can miss someone who remains still. |
| Detect someone staying in a room | mmWave presence | Placement and sensitivity require careful tuning. |
| Know whether a door or window moved | Contact sensor | Misalignment or stale data can look like a normal state. |
| Detect water at one point | Leak sensor | Water can flow around the contacts. |
| Measure room conditions | Temperature or humidity sensor | Placement may represent a draft, vent, or wall rather than the occupied area. |
| Know garage-door position | Tilt or purpose-built position sensor | Position does not prove that the doorway is clear. |

Read [PIR vs mmWave presence](/articles/pir-vs-mmwave-presence.html) before choosing occupancy sensors for bathrooms or home offices.

## Verify compatibility

Check the exact model, hardware revision, region, and firmware against the platform's current documentation. "Works with Zigbee," "supports Matter," or "compatible with Alexa" does not prove that your hub exposes every capability the recipe needs.

Before buying several:

- Pair one device.
- Confirm every required state and command.
- Confirm unavailable and low-battery behavior.
- Measure response time in the intended location.
- Restart the hub and device.
- Disconnect the internet if local behavior matters.
- Remove and re-pair it while you still remember the process.

## Check physical installation

- Measure wall boxes, fixture bases, clearances, cable access, and sensor mounting surfaces.
- Check power, neutral, grounding, load, weather, temperature, and humidity requirements.
- Follow local electrical and building requirements.
- Use a qualified professional where the product or installation calls for one.
- Confirm batteries are available and replaceable.
- Keep labels, model numbers, manuals, and reset instructions.

## Plan failure behavior

The device is not ready until these states have an answer:

| State | Safe response |
|---|---|
| Sensor unavailable | Stop trusting its last state and create a maintenance alert. |
| Battery low | Notify before the device becomes silent. |
| Hub restarting | Keep physical controls available. |
| Internet unavailable | Preserve any behavior that was promised as local. |
| Command sent but final state unknown | Report "not confirmed," not success. |
| Conflicting sensors | Prefer the conservative state and ask for inspection. |

## Avoid these buying shortcuts

- Generic "best brand" lists without a specific job.
- Hardcoded budgets that encourage buying a bundle before testing one room.
- Assuming a protocol logo guarantees feature support.
- Treating cloud voice control as the only physical control.
- Choosing a product because it exposes more data than the automation needs.
- Buying safety-related control equipment without checking approvals and instructions.

## A good first purchase

Choose one fast motion sensor and one wall-controlled light for a low-risk room. Build [lights on motion](/automation/lighting/lights-on-motion.html), keep the switch working, and observe it for a week. That small test teaches more than a whole-home shopping list.

## Next steps

- [See products I have used](/gear.html)
- [Choose a platform](/getting-started/choose-the-right-platform.html)
- [Read the philosophy](/getting-started/philosophy.html)
- [Build the first lighting recipe](/automation/lighting/lights-on-motion.html)

<div class="page-navigation">
  <a href="/getting-started/index.html">Back to getting started</a>
  <a href="/gear.html">Recommended gear</a>
</div>
