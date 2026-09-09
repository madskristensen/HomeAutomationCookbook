---
layout: guide
title: How to place motion sensors for reliable automations
description: A practical guide to placing and testing PIR and presence sensors so automations respond at the right moment without false triggers.
date: 2026-09-09
---

# How to place motion sensors for reliable automations

A good motion automation starts with where the sensor can see the useful event. The best device in the wrong place will still turn lights on too late, miss someone who is sitting still, or react to movement in the wrong room.

Use this guide for motion lighting, bathroom ventilation, arrival routines, and any other automation that depends on a sensor reporting a meaningful change.

## Start with the job

Before mounting anything, describe the event the automation needs:

- **Entry:** See someone approaching before they reach the switch.
- **Movement through a room:** Cover the path people normally take.
- **Still occupancy:** Keep detecting someone who is reading, working, or showering.
- **Outdoor arrival:** Detect activity in the intended area without treating passing traffic as an arrival.

A PIR sensor is usually a good fast trigger for movement. A presence or mmWave sensor can be a better hold signal when people remain still. Read [PIR vs mmWave presence sensors](/articles/pir-vs-mmwave-presence.html) when the automation needs more than a recent motion event.

## Place PIR sensors across the path

PIR sensors usually detect movement best when a person crosses their detection zones rather than walks directly toward the sensor. For an entry light, aim the sensor across the approach to the doorway so it sees the person before they reach the wall switch.

Choose a height and angle that cover the actual path, not just the center of the room. Corners can provide broad coverage, while a wall near an entry can provide a more deliberate direction of travel. Follow the sensor's installation instructions when they differ from these general patterns.

## Give presence sensors a clear boundary

Presence sensors can be useful in offices, bathrooms, and reading areas where a PIR may lose someone who is still. They also need more careful tuning. A sensor aimed through an open doorway, thin wall, or toward a nearby room can keep the wrong area occupied.

Start with the smallest range that covers the room. Test the places where someone sits or showers, then test the spaces that should not count, such as a hallway, neighboring room, fan, curtain, or nearby traffic.

## Avoid common false triggers

Keep the sensing area away from:

- Direct sunlight and strong reflections.
- Heating or cooling vents and rapid temperature changes.
- Ceiling fans, curtains, and other moving objects.
- Pet paths when the sensor is not pet-immune.
- Steam and water unless the sensor is specifically rated and approved for that location.
- Outdoor traffic, trees, and street activity when the sensor covers an exterior area.

Do not use motion or presence as proof that a home is empty, a doorway is safe, or a person has been identified. Those decisions need stronger signals and separate safety controls.

## Outdoor motion sensing

Outdoor placement adds weather, temperature, and moving-background problems. Use a sensor specifically rated for the exposure it will face, such as an outdoor-rated model with an appropriate IP rating. Do not assume an indoor sensor becomes outdoor-safe just because it is placed under an eave or inside a weatherproof enclosure. Follow the sensor and enclosure manufacturer's instructions.

Mount the sensor under an eave or other approved shelter when that still gives it the required view. Aim it away from passing cars, sidewalks, blowing branches, and reflective surfaces. Test it during daylight, darkness, rain, wind, and normal delivery or driveway activity before using it to trigger lights or notifications.

## Test before permanent mounting

Mount the sensor temporarily with tape or another reversible method. Watch its raw states before connecting it to lights, fans, locks, or other actions.

1. Walk every normal entry path.
2. Stand or sit in every area that should remain detected.
3. Walk past the room and use nearby doors to check for unwanted triggers.
4. Test normal conditions such as daylight, darkness, pets, fans, curtains, and steam.
5. Check how quickly the sensor reports motion and how long it takes to clear.
6. Adjust the position, angle, range, or zones and repeat the test.
7. Permanently mount it only after the coverage matches the job.

Start the automation with a notification or observation mode when a false action would be disruptive. Use a forgiving timeout until normal household behavior proves the placement reliable.

## Failure modes

- **The light turns on after someone reaches the switch:** Aim a PIR across the approach and move it closer to the entry path.
- **A person disappears while sitting still:** Use a longer timeout, add a second sensor, or use presence sensing for the occupied area.
- **A neighboring room keeps the automation active:** Reduce presence range, narrow detection zones, or change the sensor angle.
- **Outdoor motion triggers too often:** Move the sensor away from traffic and moving vegetation, then retest in normal weather.
- **Steam or temperature changes cause unreliable results:** Move the sensor to a dry location and verify that its rating permits the environment.
- **The sensor becomes unavailable:** Keep the physical control usable and make missing data fail safely rather than look like an empty room.

## FAQ

### Should a motion sensor face the door?

Usually, aim a PIR so a person crosses its detection zones while approaching the door. A sensor pointed directly at someone walking toward it may detect them later than one placed across the path.

### Is a higher mounting position always better?

No. Use the height and field of view that cover the job without seeing unwanted areas. Follow the device instructions and test the actual room rather than relying on a general measurement.

### Can one sensor cover multiple rooms?

Sometimes, but wider coverage often creates false triggers or unclear room boundaries. Use one sensor per meaningful area when the automation needs reliable room-specific behavior.

### Should I use motion to turn lights off?

Use a delay after the last motion event, not an immediate off action. A PIR reports movement, not certainty that nobody remains. Presence sensing can help where people often sit still.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Turn on a dim bathroom light at night](/automation/lighting/bathroom-night-light.html)
- [Turn on the bathroom fan when a shower starts](/automation/climate/fan-shower.html)
- [PIR vs mmWave presence sensors](/articles/pir-vs-mmwave-presence.html)
