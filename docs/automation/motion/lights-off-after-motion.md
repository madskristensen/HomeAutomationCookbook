---
layout: default
title: Turn Off Lights After Motion Stops - Smart Home Automation
description: Automatically turn off lights when no motion is detected. Complete guide with timing strategies, conditions, and platform examples for motion-based light control.
keywords: motion sensor lights off, automatic light shutoff, occupancy detection, smart lighting automation, turn off lights automatically
---

# Turn off lights after motion stops

While modern LED lights use minimal power, automatically turning off lights when a room is unoccupied creates a satisfying smart home experience and ensures energy isn't wasted. This automation completes the motion detection lighting cycle.

## Use cases

* **Bathroom** - Turn off lights 5 minutes after no motion detected
* **Living areas** - Turn off lights 2 minutes after no motion at nighttime
* **Closets** - Turn off immediately after 1 minute (quick access areas)
* **Garage** - Turn off after 3-5 minutes of no activity
* **Home office** - Longer delay (10 minutes) for stationary work

## Products needed

* **Motion sensor** - Same sensor used for turning lights on
  - Should detect motion continuously, not just entry
  - Battery life consideration: some sensors report too frequently
* **Smart light switch or bulb** - Connected to your automation platform

> **💡 Outdoor tip:** Use weather-rated sensors (IP65+) or protect from elements

## Basic automation setup

### Triggers
* Motion no longer detected for X minutes
  - Fast-access areas: 1-2 minutes
  - Living spaces: 3-5 minutes
  - Work areas: 5-10 minutes

### Conditions (optional)
* **Time-based:** Different delays for day vs. night
* **Door status:** Don't turn off if bathroom door is closed (someone may be sitting still)
* **Additional sensors:** Check other sensors in room for activity

### Actions
* Turn off light switch/bulb
* Can include gradual dimming before turning off (advanced)

## Timing strategies by room type

### Quick access spaces (1-2 minutes)
- Closets
- Pantry
- Laundry room (if no appliances running)
- Hallways

**Reasoning:** Brief visits, quick in and out

### Living spaces (3-5 minutes)
- Living room
- Dining room  
- Kitchen
- Home gym

**Reasoning:** May have brief stationary moments, but generally active

### Work/relaxation spaces (5-10 minutes)
- Home office
- Reading nook
- Craft room
- Bathroom (see special considerations)

**Reasoning:** People often sit still for extended periods

### Special considerations: bathrooms

Bathrooms require extra logic to prevent lights turning off while occupied:

**Option 1: Door sensor override**
- If door is closed → Don't turn off lights
- Even if no motion detected

**Option 2: Extended delay**
- Use 10-15 minute delay
- Less likely to turn off while showering/bathing

**Option 3: Multiple sensors**
- Motion sensor for general bathroom
- Separate sensor inside shower/toilet area
- If either detects motion → Keep lights on

## Platform-specific examples

### Home Assistant

Create an automation with these elements:
- **Trigger:** Bathroom motion sensor shows no motion for 5 minutes
- **Condition:** Bathroom door sensor shows door is open (not in use)
- **Action:** Turn off bathroom light

### Advanced: Gradual dimming

Create a more sophisticated automation:
- **Trigger:** Living room motion sensor shows no motion for 3 minutes
- **Actions:**
  1. Dim lights to 50% as a warning
  2. Wait 30 seconds
  3. Check if motion has resumed
  4. If still no motion, turn off lights completely

### SmartThings

Create routine:
1. **IF** "Bathroom Motion Sensor" no motion for 5 minutes
2. **AND** "Bathroom Door Sensor" is open
3. **THEN** Turn off "Bathroom Light"

### Apple HomeKit

1. Create automation: When motion stops
2. Wait for: 5 minutes
3. If: Bathroom door is open
4. Do: Turn off bathroom light

### Alexa

Create routine:
1. When: "Bathroom Motion Sensor" detects no motion for 5 minutes
2. Add condition: "Bathroom Door Contact" is open
3. Action: Turn off "Bathroom Light"

### Google Home

Create automation:
1. Starter: "Bathroom Motion" no motion for 5 minutes
2. Condition: "Door sensor" is open
3. Action: Turn off "Bathroom Light"

## Advanced techniques

### Day vs. night timing

**Daytime:**
- Shorter delays (2-3 minutes)
- People more active during the day
- Quicker room-to-room movement

**Nighttime:**
- Longer delays (5-10 minutes)
- Moving more slowly
- May sit still more often

Create separate automations for day and night with different delay times.

### Multiple sensor logic

For larger rooms, use multiple sensors to ensure no one is present:
- All motion sensors must show "no motion" before turning off lights
- Set appropriate delay (e.g., 5 minutes)
- Prevents false shutoffs when someone is in sensor blind spot

### Activity-based override

Don't turn off lights if other activity detected:

**Conditions to keep lights on:**
- TV is on in the room
- Music is playing
- Device charging (phone on wireless charger)
- Computer is active
- Smart plug shows power usage (someone using appliance)

## Common problems and solutions

### Problem: Lights turn off while room is occupied

**Why it happens:**
- Person sitting very still
- Motion sensor dead zone
- Single sensor can't see entire room
- Delay too short for activity type

**Solutions:**
1. ✅ Add door sensor - don't turn off if door closed
2. ✅ Use longer delay (5-10 minutes instead of 2-3)
3. ✅ Add additional motion sensors for full coverage
4. ✅ Use occupancy sensors instead of motion (if available)
5. ✅ Add manual override button to extend time
6. ✅ Use other sensors as indicators (chair pressure sensor, desk occupancy)

### Problem: Lights stay on too long after leaving

**Why it happens:**
- Delay is too long for room type
- Sensor placed where it sees movement outside room (hallway traffic)

**Solutions:**
1. ✅ Reduce delay time
2. ✅ Reposition sensor to focus on room interior only
3. ✅ Add door sensor - turn off immediately when door closes
4. ✅ Use presence detection for faster response

### Problem: Inconsistent behavior

**Why it happens:**
- Battery low in sensor
- Weak wireless signal
- Sensor needs recalibration
- Interference from other devices

**Solutions:**
1. ✅ Replace batteries before fully depleted
2. ✅ Add Zigbee/Z-Wave repeaters
3. ✅ Check sensor configuration
4. ✅ Update firmware
5. ✅ Test sensor range and coverage

## Best practices

### Testing your delays

1. Set initial delay conservatively long (10 minutes)
2. Monitor for false shutoffs over several days
3. Gradually reduce delay time
4. Find the sweet spot where:
   - Lights don't turn off when occupied
   - Lights don't stay on unnecessarily long
5. Different delay per room type

### Sensor coverage verification

**Walk test:**
1. Turn lights on via motion
2. Move to different areas of room
3. Stand still in each area for 2 minutes
4. Verify motion sensor still "sees" you
5. Identify dead zones
6. Add sensors or reposition to eliminate dead zones

### Manual override options

Always provide a way to override automation:

**Physical switch:**
- Manual switch operation keeps lights on indefinitely
- Automation resumes on next activation

**Voice command:**
- "Keep bathroom lights on"
- Sets temporary override for 30 minutes

**Dashboard button:**
- "Disable motion automation" toggle
- Resume automatically after set time or manually

## Energy savings

While LED bulbs use minimal power, automatic shutoff still provides benefits:

**Energy savings examples:**
- 10W LED × 2 hours/day unnecessary use = 7.3 kWh/year
- Multiplied by 10 lights = 73 kWh/year
- At $0.13/kWh = $9.50/year savings
- Plus reduced bulb replacement costs

**Larger impact:**
- Halogen/incandescent: 60W bulbs save 10x more
- Commercial spaces: significant savings
- Environmental impact: reduced energy generation

---

**Related automations:**
- [Turn on lights when motion detected](/automation/motion/lights-on-motion/)
- [Bathroom night light automation](/automation/motion/bathroom-night-light/)

[← Back to motion detection automations](/automation/motion/) | [View all automations →](/automation/)
