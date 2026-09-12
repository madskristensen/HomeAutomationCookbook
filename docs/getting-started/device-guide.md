---
layout: guide
redirect_from:
  - /devices/index.html
  - /getting-started/devices/index.html
title: Choose smart-home devices and gear
description: Choose compatible smart-home devices by job, then compare the sensors, switches, plugs, and climate gear I have personally used.
last_modified_at: 2026-09-12
image: /assets/img/social/guides/choose-devices.png
---

# Choose smart-home devices and gear

<figure class="content-hero">
  <img src="/assets/img/social/guides/choose-devices.svg" alt="" width="1200" height="630">
</figure>

Do not start with a brand or a box of discounted devices. Start with one household job, write the rule in plain English, and identify the capabilities that rule needs.

The goal is not to collect compatible gadgets. It is to buy the smallest amount of equipment that removes a repeated task or makes everyday life easier to manage.

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

## Products I have used

I have bought and used every product named below. Amazon product links are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html) for details.

### Occupancy and motion

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Detect fast entry motion | [Shelly BLU Motion ZB](https://www.amazon.com/dp/B0H4GD6GGK/ref=nosim?tag=madsk0f-20) | [Aeotec SmartThings Motion Sensor](https://www.amazon.com/dp/B095TZTGNB/ref=nosim?tag=madsk0f-20) - my favorite for fast reactions. | Put it where it sees the doorway before someone reaches the switch. |
| Detect a person who is still | [Besisglas Zigbee Human Presence Sensor](https://www.amazon.com/dp/B0GYJ3LQ5W/ref=nosim?tag=madsk0f-20) | [Aqara Presence Sensor FP300](https://www.amazon.com/dp/B0FG2MD3YP/ref=nosim?tag=madsk0f-20) | Use this for home offices, showers, reading, or other rooms where a PIR can time out while someone is still. |
| Detect bathroom motion with humidity, temperature, and light | [Aeotec TriSensor 8](https://www.amazon.com/dp/B0D47WR1S2/ref=nosim?tag=madsk0f-20) | [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY/ref=nosim?tag=madsk0f-20) | Use it where the extra sensor readings are useful, not where the fastest motion response matters most. |
| Detect outdoor motion | [Ecolink Z-Wave PIR Motion Detector, Pet Immune](https://www.amazon.com/dp/B01MQXXG0I/ref=nosim?tag=madsk0f-20) | [Zooz ZSE70 Outdoor/Indoor Motion Sensor](https://www.amazon.com/dp/B0DCL43CS2/ref=nosim?tag=madsk0f-20) - Z-Wave Long Range with an 800-series radio for better range from a detached garage or driveway. | 💡 See [how to place motion sensors for reliable automations](/articles/motion-sensor-placement.html) before choosing the mounting location. |

### Household presence

This one usually isn't a separate product. Most platforms already offer a presence feature through their own phone app, using the phone's location or its connection to the home Wi-Fi or network. I use a Ubiquiti network that integrates directly with Hubitat to set each family member's presence from their phone's network connection, so nobody has to install a separate app. If your platform has an equivalent built-in presence feature, or your network gear integrates with it, start there before buying anything dedicated to this job.

### Lighting control

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Dim a fixed light | [TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20) | [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN/ref=nosim?tag=madsk0f-20) | The paddle remains a normal wall control. |
| Switch a fixed light on or off | [Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20) | [UltraPro Z-Wave Long Range On/Off Switch](https://www.amazon.com/dp/B0FX3CTLW2/ref=nosim?tag=madsk0f-20) | The paddle remains a normal wall control. |
| Control a plug-in light or appliance | [Minoston 800 Series Z-Wave plug](https://www.amazon.com/dp/B0CQX4JFV2/ref=nosim?tag=madsk0f-20) | [Ezlo 800 Series Z-Wave smart plug](https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20) | Keep the appliance's physical control usable. |
| Control outdoor plug-in lighting | [Minoston Outdoor Smart Plug](https://www.amazon.com/dp/B07X52W1J8/ref=nosim?tag=madsk0f-20) | [Minoston 800 Series outdoor Z-Wave plug](https://www.amazon.com/dp/B0B7MLX1ZC/ref=nosim?tag=madsk0f-20) | Use only where an outdoor-rated plug is appropriate. |

### Climate

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Adjust heating and cooling | [ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC/ref=nosim?tag=madsk0f-20) | [Honeywell Home T6 Pro Z-Wave thermostat](https://www.amazon.com/dp/B0BHTQF8NL/ref=nosim?tag=madsk0f-20) | Someone should be able to change the temperature at the thermostat. |
| Measure room temperature and humidity | [THIRDREALITY Zigbee Temperature and Humidity Sensor Lite](https://www.amazon.com/dp/B0D2NVJTS3/ref=nosim?tag=madsk0f-20) | [Zooz ZSE44 800LR Temperature/Humidity XS Sensor](https://www.amazon.com/dp/B0B3G9Z4LJ/ref=nosim?tag=madsk0f-20) | Placement matters more than the sensor. Keep it away from vents, drafts, and direct sun. |

### Power monitoring

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Detect whether a TV is on | [Ezlo 800 Series Z-Wave smart plug](https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20) | [Zooz ZEN15 Power Switch](https://www.amazon.com/dp/B07578W7KY/ref=nosim?tag=madsk0f-20) - a heavier-duty, hardwired-capable power-metering switch for a higher-draw load. | Use the power reading as a signal only. Keep the TV's remote and normal power controls unchanged. |

### Leaks and safety

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Detect water where it should not be | [THIRDREALITY WL2 Zigbee water leak sensor](https://www.amazon.com/dp/B0GK19F6Z2/ref=nosim?tag=madsk0f-20) | [NEO Z-Wave Plus 700 water leak sensor](https://www.amazon.com/dp/B0FSKFCKTB/ref=nosim?tag=madsk0f-20) | Test the alert and make sure the source is obvious. |
| Detect an open door or window | [SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL/ref=nosim?tag=madsk0f-20) | [Zooz ZSE41 800LR Open/Close XS Sensor](https://www.amazon.com/dp/B09JKKLRLW/ref=nosim?tag=madsk0f-20) | A contact sensor is easy for a guest to understand because the door itself is the trigger. |
| Know whether a garage door is open | [THIRDREALITY Zigbee Smart Garage Door Tilt Sensor](https://www.amazon.com/dp/B0CZP2CJXF/ref=nosim?tag=madsk0f-20) | [Ecolink Z-Wave Plus Garage Door Tilt Sensor](https://www.amazon.com/dp/B01MRZB0NT/ref=nosim?tag=madsk0f-20) | Use it for status and alerts before adding automatic closing. |

### Vibration sensing

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Detect appliance vibration (dryer, washer, garage door motor) | [THIRDREALITY Zigbee Smart Vibration Sensor](https://www.amazon.com/dp/B0C9DP249C/ref=nosim?tag=madsk0f-20) | [Aeotec SmartThings Multipurpose Sensor](https://www.amazon.com/dp/B095TPSQ3S/ref=nosim?tag=madsk0f-20) - a Zigbee door/window sensor with a built-in accelerometer for vibration and tilt, worth it if you also want the contact-sensor reading in the same spot. | Mount only on a cool, fixed exterior panel after testing surface temperature through a full cycle. Sensitivity usually needs adjusting to ignore normal household bumps. |

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

- [Choose a platform](/getting-started/choose-the-right-platform.html)
- [Read the philosophy](/getting-started/philosophy.html)
- [Build the first lighting recipe](/automation/lighting/lights-on-motion.html)

<div class="page-navigation">
  <a href="/getting-started/index.html">Back to getting started</a>
  <a href="/automation/index.html">Browse automations</a>
</div>
