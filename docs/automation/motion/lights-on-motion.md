---
layout: default
title: Turn On Lights When Motion is Detected - Smart Home Automation Guide
description: Learn how to automatically turn on lights when motion is detected. Step-by-step guide for motion sensor lighting automation with examples for all smart home platforms.
keywords: motion sensor, automatic lights, smart home lighting, motion detection, home automation, smart lights
---

# Turn on lights when motion is detected

Automatically turning on lights when motion is detected is one of the most popular and useful smart home automations. It solves the everyday problem of fumbling for light switches in the dark and creates a seamless, effortless lighting experience.

## Use cases

* **Nighttime navigation** - Bathroom lights turn on at low brightness when you get up at night
* **Home office** - Lights automatically turn on when you enter your workspace
* **Garden shed** - Motion sensor triggers light when you enter
* **Porch light** - Automatically lights up for guests and delivery drivers
* **Hallways** - Lights turn on as you move through the house
* **Closets** - No more fumbling for switches in dark spaces

## Products needed

### Essential equipment

* **Motion sensor** - Indoor or outdoor rated depending on location
  - Popular brands: Philips Hue, Aqara, SmartThings, Wyze
  - Indoor: Standard motion sensors
  - Outdoor: Weatherproof IP65+ rated sensors
* **Smart light switch or bulb** - To control the lighting
  - Smart switches: Lutron, GE, Inovelli, Leviton
  - Smart bulbs: Philips Hue, LIFX, Wyze, Sengled

### Outdoor motion sensing tip

> **💡 Important:** For outdoor applications, either:
> - Use sensors specifically rated for outdoor use (IP65 or higher)
> - Protect indoor sensors with weatherproof enclosures
> - Place sensors under eaves to avoid direct water exposure

## Basic automation setup

### Triggers
* Motion detected by sensor

### Conditions (optional)
* Time-based: Different behavior for day vs. night
* Lux sensor: Only activate if room is dark (below certain lux level)
* Home mode: Only when home is occupied

### Actions
* Turn on light switch or bulb
* Set to preferred brightness level (dimming percentage)

## Elevation tips: day vs. night dimming

One of the best enhancements is adjusting brightness based on time of day:

**Daytime automation:**
- Brightness: 100%
- Or skip turning on if room has natural light (use lux sensor)

**Nighttime automation:**
- Brightness: 10-30%
- Warm color temperature (if using color bulbs)
- Reduces eye strain and doesn't disturb sleep

**Example schedule:**
- 6 AM - 9 PM: Full brightness (100%)
- 9 PM - 11 PM: Medium brightness (50%)
- 11 PM - 6 AM: Low brightness (10-20%)

## Platform-specific examples

### Home Assistant

Create an automation with these elements:
- **Trigger:** Motion sensor state changes to "on"
- **Condition:** Light level (lux) is below 100
- **Action:** Turn on bathroom light
  - If time is between 10 PM and 6 AM: Set brightness to 10%
  - If time is between 6 AM and 10 PM: Set brightness to 100%

### SmartThings

Create a routine:
1. **IF** Motion is detected on "Bathroom Motion Sensor"
2. **AND** Time is between 10 PM and 6 AM
3. **THEN** Turn on "Bathroom Light" to 10%

Create a second routine for daytime with 100% brightness.

### Apple HomeKit

1. Create automation in Home app
2. When: Motion sensor detects motion
3. Time: Between 10 PM and 6 AM
4. Do: Turn on bathroom light at 10%
5. Repeat for daytime hours at 100%

### Alexa

Create routine:
1. When: "Bathroom Motion" detects motion
2. Add condition: Between 10 PM and 6 AM
3. Action: Turn on "Bathroom Light" to 10%

### Google Home

Create household routine:
1. When: "Bathroom Motion Sensor" detects motion
2. Add starter condition: Time between 10 PM - 6 AM
3. Action: Set "Bathroom Light" to 10%

## Advanced features

### Multiple brightness levels

Create different levels throughout the night:

- **Early night (9 PM - 11 PM):** 30% - still awake, need moderate light
- **Deep night (11 PM - 5 AM):** 10% - minimal disturbance
- **Early morning (5 AM - 7 AM):** 20% - gentle wake-up
- **Daytime (7 AM - 9 PM):** 100% - full brightness

### Lux-based activation

Only turn on lights if the room is actually dark:
- Add a condition that light level must be below a certain threshold (e.g., 100 lux)
- This prevents lights from turning on during daytime when natural light is sufficient

### Zone-based motion

For larger rooms, use multiple motion sensors to track which area someone is in and only light that zone.

## Common issues and solutions

### Issue: Lights turn on too slowly

**Problem:** Delay between motion detection and lights turning on causes you to reach for the switch.

**Solutions:**
- Check sensor placement - should detect motion before entering room
- Reduce automation processing time - use local control instead of cloud
- Use faster communication protocols (Zigbee/Z-Wave vs WiFi)
- Optimize automation logic to minimize conditions

### Issue: Lights turn on when not needed

**Problem:** Lights activate from pets, sunlight reflections, or other false triggers.

**Solutions:**
- Adjust motion sensor sensitivity
- Add lux sensor condition to prevent daytime activation
- Use pet-immune motion sensors
- Position sensor away from windows and heat sources
- Add time-based conditions

### Issue: Inconsistent performance

**Problem:** Sometimes works, sometimes doesn't.

**Solutions:**
- Check sensor battery levels
- Verify wireless signal strength (Zigbee/Z-Wave mesh)
- Replace batteries before completely dead
- Add repeaters/extenders for distant sensors
- Check for interference from other devices

## Sensor placement best practices

### Height
- **Optimal:** 6-8 feet high for best coverage
- **Corners:** Good for monitoring entire room
- **Entry points:** Near doors for immediate detection

### Angle
- **Ceiling mount:** Wide coverage, detects all motion
- **Wall mount:** Directional, catches people entering
- **Corner mount:** 90° coverage, good for hallways

### Coverage testing

1. Mount sensor temporarily with tape
2. Walk through room at different paths
3. Verify all entry points are covered
4. Check for dead zones
5. Adjust position or add additional sensors
6. Permanently mount once confirmed

### What to avoid

❌ **Near windows** - Sunlight and outdoor motion cause false triggers
❌ **Near heating/AC vents** - Temperature changes trigger sensors
❌ **Pointed at moving objects** - Ceiling fans, curtains, pets
❌ **Behind furniture** - Blocks detection zone

---

**Related automations:**
- [Turn off lights after motion stops](/automation/motion/lights-off-after-motion/)
- [Nighttime bathroom lighting](/automation/motion/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/motion/">← Back to Motion Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
