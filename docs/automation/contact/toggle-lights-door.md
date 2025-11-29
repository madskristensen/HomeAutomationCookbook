---
layout: default
title: Toggle Lights When Door Opens - Contact Sensor Automation
description: Automatically turn on lights when doors open. Complete guide for door sensor lighting automation with examples for closets, rooms, and outdoor areas.
keywords: door sensor automation, contact sensor lights, automatic closet lights, door activated lighting, smart door sensor
---

# Toggle lights on/off when door opens

Automatically turning on lights when doors open is a versatile automation that solves lighting problems in many areas of your home. From closets that never have enough light to garage entries that leave you fumbling in the dark, this automation makes life easier.

## Use cases

### Indoor applications
* **Closets** - Turn on closet lights when door opens, illuminate contents automatically
* **Hallway closets** - Lights spill into hallway to light both areas
* **Pantry** - See all shelves clearly when door opens
* **Linen closet** - Find what you need without searching in dim light
* **Room entry** - Automatic lighting when entering any room
* **Bathroom** - Combined with motion for complete coverage

### Outdoor applications  
* **Garage entry** - Light up garage when opening door from house
* **Exterior doors** - Porch/patio lights when doors open
* **Shed/storage** - Outdoor building illumination
* **Gate entry** - Pathway lights when gate opens

## Products needed

### Essential equipment

* **Contact sensor** (door/window sensor)
  - Popular brands: Aqara, SmartThings, Ring, Wyze
  - Battery-powered for easy installation
  - Zigbee/Z-Wave for reliability
  - Recessed options for clean look
  
* **Smart light switch or bulb**
  - In-wall switch for permanent fixtures
  - Smart bulbs for flexibility
  - Dimming capability recommended

### Outdoor requirements

> **💡 Important:** For outdoor installations:
> - Use weather-rated sensors (IP65+)
> - Protect with weatherproof enclosures
> - Consider temperature range (-20°F to 120°F)
> - Use UV-resistant materials

## Basic automation setup

### Triggers
* Contact sensor state changes to "open"
* Door opens (specific door)

### Conditions (optional)
* **Time-based:** Only during certain hours
* **Occupancy:** Only when home is occupied
* **Lux sensor:** Only if room is dark (below threshold)
* **Day vs. Night:** Different brightness levels

### Actions
* Turn on light switch/bulb
* Set to preferred brightness level
* Optional: Set color temperature

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Closet door sensor changes to "open"
- **Condition (optional):** Room light level below 50 lux (only activate if dark)
- **Action:** Turn on closet light at 100% brightness

### Advanced: Day vs. night brightness

Adjust brightness based on time of day:
- **Nighttime (10 PM - 6 AM):** 30% brightness with warm white (2200K)
- **Daytime:** 100% brightness

Use conditional logic to check time and adjust brightness accordingly.

### SmartThings

Create routine:
1. **IF** "Closet Door Sensor" opens
2. **THEN** Turn on "Closet Light" to 100%

For day/night variation, create two routines with time conditions.

### Apple HomeKit

1. Open Home app → Automation
2. **When:** Closet door sensor detects open
3. **Time:** Anytime (or add time condition)
4. **Do:** Turn on Closet Light
5. Optional: Add "Convert to Shortcut" for brightness control

### Alexa

Create routine:
1. **When:** "Closet Door Sensor" opens
2. **Add condition:** Time between sunrise and sunset (optional)
3. **Action:** Turn on "Closet Light" to 100%

### Google Home

Create automation:
1. **Starter:** "Closet Door Sensor" opens
2. **Condition:** Time of day (optional)
3. **Action:** Turn on "Closet Light"

## Auto turn-off when door closes

Complete the automation cycle by turning lights off when the door closes:

### Simple auto-off

Create automation with these elements:
- **Trigger:** Closet door sensor changes to "closed" for 2 minutes
- **Action:** Turn off closet light

### Why the delay?

**Without delay:** Lights turn off immediately when door closes
- Problem: Door swings closed while you're still in closet
- Problem: Multiple in/out trips cause rapid toggling

**With 2-minute delay:** Buffer time for normal use
- Allows door to close naturally
- Prevents annoying on/off cycles
- Still energy efficient

---

**Related automations:**
- [Disable automations when door closed](/automation/contact/disable-on-door-close/)

[← Back to contact sensor automations](/automation/contact/) | [View all automations →](/automation/)
