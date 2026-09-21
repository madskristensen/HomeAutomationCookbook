---
layout: automation
date: 2025-11-28
title: Cold-room temperature alerts
description: Get an alert before a cold room leaves its safe temperature range without controlling a portable heater through a general smart plug.
keywords: cold room alert, room temperature monitoring, space heater safety, thermostat alert, supplemental heating
last_modified_at: 2026-09-21
image: /assets/img/social/recipes/climate/room-heater-maintain-temp.png
compact: true
faqs:
  - question: Can I control a portable space heater with a general smart plug?
    answer: Do not assume that is safe. Follow the heater manufacturer's instructions. This recipe does not switch a portable heater through a general-purpose smart plug.
  - question: What should happen when the temperature sensor stops reporting?
    answer: Send a maintenance alert and stop making automatic heating decisions from that sensor. Missing data must not be treated as a comfortable room.
  - question: Can this protect pipes or vulnerable people by itself?
    answer: No. Use appropriate building heat, freeze protection, supervision, and professional advice. A hobby sensor and hub are supplemental.
---

# Monitor a cold room without smart-plug heater control

<figure class="content-hero">
  <img src="/assets/img/social/recipes/climate/room-heater-maintain-temp.svg" alt="A cold-room temperature alert helps maintain comfort without unsafe heater control" width="1200" height="630">
</figure>

The house reports a room that is too cold or too warm, while any automatic heat control remains inside equipment designed and approved for thermostat operation.

**Best for:** Finding cold rooms, watching nurseries or workspaces, and verifying that permanent heating is keeping up.

**Not for:** Remotely switching a portable space heater, using a hobby sensor as freeze protection, or heating an unattended room with equipment not approved for that use.

## Why this exists

A temperature alert is useful. Turning a high-wattage portable heater on through a general-purpose smart plug adds failure points around an appliance that can start a fire if it is covered, tipped, damaged, or used contrary to its instructions.

Start with monitoring. If a room needs automatic supplemental heat, use a fixed or purpose-built heating system with its own approved thermostat, limits, and professional installation where required.

## Logic

<div class="automation-example">IF the room stays below its alert threshold
OR the temperature sensor becomes unavailable
THEN alert a responsible person
AND name the room and current sensor state

DO NOT switch a portable heater through a general-purpose smart plug</div>

- **Trigger:** The room remains outside its chosen temperature range, or the sensor stops reporting.
- **Conditions:** The reading is recent and the sensor has been compared with a known thermometer.
- **Action:** Send an alert naming the room and show the current reading.
- **Wait / timeout:** Require a sustained reading long enough to avoid alerts from a brief draft.
- **Stop condition:** A person inspects the room and acknowledges the alert.
- **Manual override:** Heating remains controllable at its normal thermostat or appliance controls.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Measure room temperature**

[THIRDREALITY Zigbee Temperature and Humidity Sensor Lite](https://www.amazon.com/dp/B0D2NVJTS3/ref=nosim?tag=madsk0f-20). Compare the reading with a known thermometer before using it for alerts.

</div>
<div class="product-item" markdown="1">

**Control central heating**

[ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC/ref=nosim?tag=madsk0f-20). I have used both. Keep safe limits and manual control at the thermostat.

</div>
<div class="product-item" markdown="1">

**Add supplemental heat**

Manually operated equipment used exactly as instructed. Have wiring and equipment evaluated by a qualified professional where appropriate.

</div>
</div>

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the products I have used. This page does not recommend a smart plug for a portable heater.

## Setup notes

1. Put the sensor away from direct sunlight, supply vents, exterior doors, and the heater itself.
2. Compare it with a known thermometer over several hours.
3. Choose alert thresholds for the people, pets, pipes, plants, and materials in that specific room.
4. Add a stale-data alert based on the sensor's normal reporting interval.
5. Test notifications with phones locked and muted as they normally are.
6. Keep the room's normal heat source and manual controls independent of the hub.
7. If permanent supplemental heat is needed, select equipment designed for that job and follow installation requirements.

## If a portable heater is used manually

- Follow the manufacturer's location, clearance, outlet, supervision, and operating instructions.
- Plug it directly into an appropriate wall outlet unless the manufacturer explicitly says otherwise.
- Keep it away from bedding, curtains, furniture, water, children, and pets.
- Do not defeat tip-over, overheat, timer, or thermostat protection.
- Turn it off when unattended if the instructions require that.
- Stop using equipment or outlets that are damaged, loose, discolored, unusually warm, or unreliable.

## Advanced features

### Compare nearby rooms

Track the room against a nearby conditioned space. A growing difference can reveal a closed vent, draft, equipment problem, or poor sensor placement.

### Watch recovery time

After the central system starts, note whether the room moves toward the expected range. Alert on a sustained failure to recover rather than repeatedly changing the setpoint.

## Failure modes

- **Sensor reads warmer than the occupied area:** Move it away from the heater, electronics, sunlight, or ceiling.
- **Sensor reads colder near a window:** Decide whether that location represents the room or only the draft.
- **Sensor stops reporting:** Send a maintenance alert and stop using it for decisions.
- **Alerts repeat constantly:** Add acknowledgment and hysteresis without hiding a sustained unsafe condition.
- **Central heat cannot maintain the room:** Inspect vents, doors, insulation, and the heating system rather than adding unverified plug control.
- **The hub is down:** The normal thermostat and heating equipment continue operating independently.

## FAQ

### Can I control a portable space heater with a general smart plug?

Do not assume that is safe. Follow the heater manufacturer's instructions. This recipe does not switch a portable heater through a general-purpose smart plug.

### What should happen when the temperature sensor stops reporting?

Send a maintenance alert and stop making automatic heating decisions from that sensor. Missing data must not be treated as a comfortable room.

### Can this protect pipes or vulnerable people by itself?

No. Use appropriate building heat, freeze protection, supervision, and professional advice. A hobby sensor and hub are supplemental.

## Related recipes

- [Pause HVAC when windows stay open](/automation/climate/thermostat-windows-open.html)
- [Safe thermostat auto-away](/automation/climate/safe-thermostat-away.html)
- [Climate automations](/automation/climate/index.html)

<div class="page-navigation">
  <a href="/automation/climate/index.html">Back to climate automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
