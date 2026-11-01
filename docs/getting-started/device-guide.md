---
layout: guide
redirect_from:
  - /devices/index.html
  - /getting-started/devices/index.html
  - /getting-started/device-guide-mockup.html
title: Choose smart-home devices by radio
description: One Zigbee and one Z-Wave device for each job, from switches to leak sensors, plus which hubs support each radio.
last_modified_at: 2026-11-01
image: /assets/img/social/guides/choose-devices.png
---

# Choose smart-home devices by radio

{% include content-hero.html src="/assets/img/social/guides/choose-devices.svg" alt="Sensors, switches, plugs, and climate devices chosen for a specific household job" %}


Do not start with a brand or a box of discounted devices. Start with one household job, write the rule in plain English, and identify the capabilities that rule needs.

The goal is not to collect compatible gadgets. It is to buy the smallest amount of equipment that removes a repeated task or makes everyday life easier to manage.

Amazon product links are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html) for details.

<div class="dm" markdown="0">
<p>Each job has two picks. One is Zigbee and one is Z-Wave. Buy the one your hub supports.</p>
<table class="dm-legend"><caption>Which hubs talk Zigbee or Z-Wave</caption><thead><tr><th scope="col">Hub</th><th scope="col">Zigbee</th><th scope="col">Z-Wave</th><th scope="col">Note</th></tr></thead><tbody><tr><th scope="row">Amazon Echo</th><td class="y">Yes, on some models</td><td class="n">No</td><td>Zigbee only on models with a built-in hub, like Echo (4th Gen), Echo Hub, and Echo Show 10 (3rd Gen).</td></tr><tr><th scope="row">Google Home / Nest</th><td class="n">No</td><td class="n">No</td><td>Needs a separate hub.</td></tr><tr><th scope="row">Apple Home</th><td class="n">No</td><td class="n">No</td><td>Not built in. Hubitat or Home Assistant can share your Zigbee and Z-Wave devices with Apple Home.</td></tr><tr><th scope="row">Home Assistant</th><td class="y">Yes</td><td class="y">Yes</td><td>Add a USB stick, like Connect ZBT-2 for Zigbee or ZWA-2 for Z-Wave. Yellow has Zigbee built in.</td></tr><tr><th scope="row">Hubitat</th><td class="y">Yes</td><td class="y">Yes</td><td>Both built into the C-8 and C-8 Pro. The Thread edition has no Zigbee.</td></tr><tr><th scope="row">SmartThings</th><td class="y">Yes</td><td class="y">Yes</td><td>Both built into the SmartThings hub.</td></tr><tr><th scope="row">Homey Pro</th><td class="y">Yes</td><td class="y">Yes</td><td>Both built into Homey Pro. Homey Pro mini has no Z-Wave.</td></tr></tbody></table><ul class="dm-legend-notes"><li>Amazon Echo: Zigbee only on models with a built-in hub, like Echo (4th Gen), Echo Hub, and Echo Show 10 (3rd Gen).</li><li>Home Assistant: Add a USB stick, like Connect ZBT-2 for Zigbee or ZWA-2 for Z-Wave. Yellow has Zigbee built in.</li><li>Hubitat: Both built into the C-8 and C-8 Pro. The Thread edition has no Zigbee.</li><li>Apple Home: Not built in. Hubitat or Home Assistant can share your Zigbee and Z-Wave devices with Apple Home.</li><li>SmartThings: Both built into the SmartThings hub.</li><li>Homey Pro: Both built into Homey Pro. Homey Pro mini has no Z-Wave.</li></ul>
<p>On Alexa or Google Home and not sure? Only the Echo models named above have a Zigbee hub. Anything else needs a separate hub.</p>
<div id="products-i-have-used"></div>
<section class="dm-job" id="lighting-control"><h2>Smart switch or dimmer</h2><p class="dm-use">Recipes that light a room, scenes, and double-tap controls.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20">Leviton DG15S Zigbee switch</a></p><p>On/off switch. The paddle stays a normal wall control.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0FX36Z8VN/ref=nosim?tag=madsk0f-20">UltraPro Z-Wave Long Range Dimmer</a></p><p>Dims and stays a normal wall control.</p><p class="dm-alt">On/off only: <a href="https://www.amazon.com/dp/B0FX3CTLW2/ref=nosim?tag=madsk0f-20">UltraPro Z-Wave Long Range On/Off Switch</a></p></div></div></section>
<section class="dm-job" id="plug"><h2>Smart plug</h2><p class="dm-use">Lamps, fans, and small appliances.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0BPY2KRHH/ref=nosim?tag=madsk0f-20">THIRDREALITY Zigbee Smart Plug</a></p><p>Switches the load and reports power too.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0CQX4JFV2/ref=nosim?tag=madsk0f-20">Minoston 800 Series Z-Wave plug</a></p><p>Simple indoor on/off plug.</p><p class="dm-alt">Outdoors: <a href="https://www.amazon.com/dp/B0B7MLX1ZC/ref=nosim?tag=madsk0f-20">Minoston 800 Series outdoor Z-Wave plug</a></p></div></div></section>
<section class="dm-job" id="power-monitoring"><h2>Power-monitoring plug</h2><p class="dm-use">Know when a TV, white noise machine, or charger is on.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0BPY2KRHH/ref=nosim?tag=madsk0f-20">THIRDREALITY Zigbee Smart Plug with power monitoring</a></p><p>Real-time power readings at a low price.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20">Ezlo 800 Series Z-Wave smart plug</a></p><p>Sees the draw of a TV or toothbrush charger in my house.</p></div></div></section>
<section class="dm-job" id="heavy-duty-plug"><h2>Heavy-duty power plug</h2><p class="dm-use">Washers, fridges, sump pumps, and other big appliances.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-gap">GAP: needs a pick</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B07578W7KY/ref=nosim?tag=madsk0f-20">Zooz ZEN15 Power Switch</a></p><p>Rated for one device up to 15 A (1800 W). Reports power. Zooz says not to use it for heaters.</p></div></div></section>
<section class="dm-job" id="motion"><h2>Motion sensor</h2><p class="dm-use">Lights on when someone walks in.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B095TZTGNB/ref=nosim?tag=madsk0f-20">Aeotec SmartThings Motion Sensor</a></p><p>My favorite for fast reactions.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0DCL43CS2/ref=nosim?tag=madsk0f-20">Zooz ZSE70 Outdoor/Indoor Motion Sensor</a></p><p>Long Range radio reaches a garage or driveway.</p></div></div></section>
<section class="dm-job" id="presence"><h2>Presence sensor</h2><p class="dm-use">Keep lights on while someone sits still.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GYJ3LQ5W/ref=nosim?tag=madsk0f-20">Besisglas Zigbee Human Presence Sensor</a></p><p>Sees a person who is still, like at a desk.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p>No Z-Wave presence sensors yet. Use the Zigbee pick, or a Z-Wave motion sensor.</p></div></div></section>
<section class="dm-job" id="contact"><h2>Door and window sensor</h2><p class="dm-use">Open door alerts, window and thermostat recipes.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GKFB3XCL/ref=nosim?tag=madsk0f-20">SONOFF SenseGuard Gen2 Zigbee contact sensor</a></p><p>The door itself is the trigger. Easy for guests.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B09JKKLRLW/ref=nosim?tag=madsk0f-20">Zooz ZSE41 800LR Open/Close XS Sensor</a></p><p>Small, with a Long Range radio.</p></div></div></section>
<section class="dm-job" id="button"><h2>Smart button</h2><p class="dm-use">Bedtime, quiet mode, pet feeding, and scene buttons.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0CL9JTMWF/ref=nosim?tag=madsk0f-20">SONOFF SNZB-01P Zigbee Wireless Button</a></p><p>Single, double, and long press. Runs on a coin cell.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B08TMWLY74/ref=nosim?tag=madsk0f-20">Zooz ZEN34 800LR Z-Wave Remote Switch</a></p><p>Two paddles with multi-tap. Mounts on a wall or a switch box.</p></div></div></section>
<section class="dm-job" id="leak"><h2>Leak sensor</h2><p class="dm-use">Water where it should not be.</p><div class="dm-pair"><div class="dm-opt"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GK19F6Z2/ref=nosim?tag=madsk0f-20">THIRDREALITY WL2 Zigbee water leak sensor</a></p><p>Test the alert and make the source obvious.</p></div><div class="dm-opt"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0FSKFCKTB/ref=nosim?tag=madsk0f-20">NEO Z-Wave Plus 700 water leak sensor</a></p><p>Test the alert and make the source obvious.</p></div></div></section>
<section class="dm-job"><h2>Wi-Fi and HomeKit</h2><p>Wi-Fi devices skip the hub but depend on the cloud and your router. Apple Home needs Home Assistant or Hubitat as a bridge for Zigbee and Z-Wave devices.</p></section>
</div>
<style>
.dm-legend{border-collapse:collapse;width:100%;font-size:.9rem;margin:.5rem 0 1rem}
.dm-legend caption{text-align:left;font-weight:600;padding-bottom:.25rem}
.dm-legend th,.dm-legend td{border:1px solid #e0e0e0;padding:.3rem .5rem;text-align:left;vertical-align:top}
.dm-legend .y{color:#1d6b33;font-weight:600}.dm-legend .n{color:#8a3b12}.dm-legend .b{color:#7a5a00;font-weight:600}
.dm-job{border-top:1px solid #e0e0e0;padding:.75rem 0}.dm-job h2{margin:.25rem 0}.dm-use{color:#5d6d75;margin:0 0 .5rem}
.dm-pair{display:grid;grid-template-columns:1fr 1fr;gap:.75rem}
.dm-opt{border:1px solid #e6e9ea;border-radius:8px;padding:.5rem .75rem;overflow-wrap:anywhere}
.dm-opt p{margin:.2rem 0}.dm-tag{font-size:.8rem;font-weight:600;text-transform:uppercase;color:#5d6d75}
.dm-pick{font-weight:600}.dm-alt{font-size:.9rem;color:#5d6d75}
.dm-gap{font-weight:700;color:#8a3b12;background:#fff1e6;padding:.25rem .5rem;border-radius:4px;display:inline-block}
@media (max-width:600px){.dm-pair{grid-template-columns:1fr}.dm-legend td:last-child,.dm-legend th:last-child{display:none}.dm-legend-notes{display:block}}
.dm-legend-notes{display:none;font-size:.85rem;color:#5d6d75;padding-left:1.1rem}
</style>

## More gear I use

These jobs do not fit the two-radio table above.

### Bathroom multisensor

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Detect bathroom motion with humidity, temperature, and light | [Aeotec TriSensor 8](https://www.amazon.com/dp/B0D47WR1S2/ref=nosim?tag=madsk0f-20) | [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY/ref=nosim?tag=madsk0f-20) | Use it where the extra sensor readings are useful, not where the fastest motion response matters most. |

### Household presence

This one usually isn't a separate product. Most platforms already offer a presence feature through their own phone app, using the phone's location or its connection to the home Wi-Fi or network. I use a Ubiquiti network that integrates directly with Hubitat to set each family member's presence from their phone's network connection, so nobody has to install a separate app. If your platform has an equivalent built-in presence feature, or your network gear integrates with it, start there before buying anything dedicated to this job.

### Climate

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Adjust heating and cooling | [ecobee Smart Thermostat Enhanced](https://www.amazon.com/dp/B09XXTQPXC/ref=nosim?tag=madsk0f-20) | [Honeywell Home T6 Pro Z-Wave thermostat](https://www.amazon.com/dp/B0BHTQF8NL/ref=nosim?tag=madsk0f-20) | Someone should be able to change the temperature at the thermostat. |
| Measure room temperature and humidity | [THIRDREALITY Zigbee Temperature and Humidity Sensor Lite](https://www.amazon.com/dp/B0D2NVJTS3/ref=nosim?tag=madsk0f-20) | [Zooz ZSE44 800LR Temperature/Humidity XS Sensor](https://www.amazon.com/dp/B0B3G9Z4LJ/ref=nosim?tag=madsk0f-20) | Placement matters more than the sensor. Keep it away from vents, drafts, and direct sun. |

For a bathroom fan, reporting speed matters most. See [best humidity sensors for shower fan automation](/articles/best-humidity-sensors-shower-fan.html).

### Power monitoring help

For which device fits which appliance, see [best power-monitoring plugs for washer, dishwasher, and TV alerts](/articles/best-power-monitoring-plugs-appliance-alerts.html).

### Garage door position

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Know whether a garage door is open | [THIRDREALITY Zigbee Smart Garage Door Tilt Sensor](https://www.amazon.com/dp/B0CZP2CJXF/ref=nosim?tag=madsk0f-20) | [Ecolink Z-Wave Plus Garage Door Tilt Sensor](https://www.amazon.com/dp/B01MRZB0NT/ref=nosim?tag=madsk0f-20) | Use it for status and alerts before adding automatic closing. |

### Vibration sensing

| Job | Good enough | Never think about it | Guest-proof note |
|---|---|---|---|
| Detect appliance vibration (dryer, washer, garage door motor) | [THIRDREALITY Zigbee Smart Vibration Sensor](https://www.amazon.com/dp/B0C9DP249C/ref=nosim?tag=madsk0f-20) | [Aeotec SmartThings Multipurpose Sensor](https://www.amazon.com/dp/B095TPSQ3S/ref=nosim?tag=madsk0f-20) - a Zigbee door/window sensor with a built-in accelerometer for vibration and tilt, worth it if you also want the contact-sensor reading in the same spot. | Mount only on a cool, fixed exterior panel after testing surface temperature through a full cycle. Sensitivity usually needs adjusting to ignore normal household bumps. |

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

- [Follow the starter house setup plan](/getting-started/starter-house-setup.html)
- [Choose a platform](/getting-started/choose-the-right-platform.html)
- [Read the philosophy](/getting-started/philosophy.html)
- [Build the first lighting recipe](/automation/lighting/lights-on-motion.html)

{% include page-navigation.html
  left_url="/getting-started/"
  left_label="Back to getting started"
  right_url="/automation/"
  right_label="Browse automations"
%}
