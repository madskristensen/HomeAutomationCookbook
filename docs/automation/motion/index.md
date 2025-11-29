---
layout: default
title: Motion Detection Automations - Smart Home Lighting Guide
description: Master motion sensor automations for smart home lighting. Learn to turn lights on/off automatically, create nighttime modes, and optimize motion detection.
keywords: motion sensor automation, automatic lighting, PIR sensor, occupancy detection, smart home motion, motion activated lights
---

# Motion Detection Automations

Motion detection is one of the most powerful tools in a home automator's arsenal. Motion sensors come in many varieties and can be customized to fit any scenario. Proper use of motion detection to turn on lights, music, and more will seem like magic to guests and make your life easier.

<div class="category-intro" markdown="1">

## Why Motion Detection?

- ✨ **Hands-Free Lighting** - Lights turn on automatically as you enter any room
- 🔋 **Energy Savings** - Lights turn off when rooms are unoccupied
- 🌙 **Safety at Night** - Never stumble in the dark again
- 🎯 **True Automation** - Works without any input from you
- 💡 **Versatile** - Beyond lights: music, notifications, security alerts
- 🏃 **Fast Response** - Modern sensors detect motion in milliseconds

</div>

## 🌟 Essential Automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

#### [Turn On Lights When Motion is Detected](/automation/motion/lights-on-motion/)

The most common and useful automation. Automatically turn on lights when entering a room.

**Best for:** Bathrooms, hallways, closets, entryways, outdoor areas

<p><a href="/automation/motion/lights-on-motion/" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

#### [Turn Off Lights After Motion Stops](/automation/motion/lights-off-after-motion/)

Complete the cycle by turning lights off when a room is no longer occupied.

**Best for:** All rooms with motion sensors, energy savings

<p><a href="/automation/motion/lights-off-after-motion/" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Quick Start Guide

### 1. Choose Your Motion Sensor

**Indoor Sensors:**
- Philips Hue Motion Sensor (includes lux sensor)
- Aqara Motion Sensor (compact, long battery life)
- SmartThings Motion Sensor
- Wyze Motion Sensor (budget-friendly)

**Outdoor Sensors:**
- Ring Motion Sensor (weather-resistant)
- Aqara Motion Sensor P1 (IP65 rated)
- Philips Hue Outdoor Motion
- Any sensor in weatherproof enclosure

### 2. Select Communication Protocol

**Zigbee:**
- ✅ Low power, long battery life
- ✅ Mesh network, reliable
- ✅ Fast response time
- ❌ Requires hub

**Z-Wave:**
- ✅ Very reliable, no interference
- ✅ Long range
- ❌ More expensive
- ❌ Requires hub

**WiFi:**
- ✅ No hub needed
- ✅ Easy setup
- ❌ Higher power consumption
- ❌ Can congest network

**Bluetooth:**
- ✅ Low power
- ✅ No hub for some platforms
- ❌ Limited range
- ❌ No mesh

### 3. Plan Your Installation

**Coverage Mapping:**
1. Identify all areas needing automation
2. Mark entry points on floor plan
3. Note furniture and obstacles
4. Plan sensor placement for full coverage

**Sensor Placement Guidelines:**
- **Height:** 6-8 feet for optimal coverage
- **Angle:** Point toward entry/movement paths
- **Avoid:** Windows, heat sources, moving objects
- **Test:** Verify coverage before permanent mounting

### 4. Create Your First Automation

Start simple:
1. **Trigger:** Motion detected
2. **Action:** Turn on light at 100%
3. **Test:** Walk through several times
4. **Refine:** Add conditions, adjust timing

Then enhance:
- Add time-based brightness
- Include auto-off timer
- Add lux sensor conditions
- Expand to more rooms

---

## Motion Sensor Types

### Passive Infrared (PIR)

**How it works:** Detects changes in infrared radiation (body heat)

**Pros:**
- Most common and affordable
- Reliable for human detection
- Long battery life
- Wide detection angle

**Cons:**
- Can miss stationary people
- Affected by temperature changes
- May detect pets

**Best for:** General room occupancy, entry detection

### Microwave/Radar

**How it works:** Emits microwave signals and detects reflection changes

**Pros:**
- Can detect through walls/objects
- Senses smaller movements
- Not affected by temperature

**Cons:**
- More expensive
- Higher power consumption
- Can trigger through walls (may be unwanted)

**Best for:** Larger spaces, high-accuracy needs

### Dual-Technology

**How it works:** Combines PIR + microwave for accuracy

**Pros:**
- Fewer false triggers
- Very reliable
- Best accuracy

**Cons:**
- Most expensive
- Shorter battery life

**Best for:** Critical applications, security

### mmWave

**How it works:** High-frequency radar detection

**Pros:**
- Detects breathing, micro-movements
- True presence detection (not just motion)
- Can detect stationary people

**Cons:**
- Expensive
- Requires tuning
- May be too sensitive

**Best for:** Offices, workspaces where people sit still

---

## Common Challenges & Solutions

### Challenge: False Triggers

**Causes:**
- Pets triggering sensor
- Sunlight through windows
- Heat from vents
- Tree branches/shadows

**Solutions:**
✅ Pet-immune sensors (ignore small animals)
✅ Adjust sensor sensitivity
✅ Reposition away from windows
✅ Add lux sensor condition (only in dark)
✅ Time-based conditions

### Challenge: Missed Detection

**Causes:**
- Dead zones in coverage
- Sensor positioned wrong
- Person sitting very still
- Sensor battery low

**Solutions:**
✅ Add additional sensors
✅ Use mmWave for stationary detection
✅ Increase sensor sensitivity
✅ Regular battery maintenance
✅ Test coverage thoroughly

### Challenge: Lights Turn Off While Occupied

**Causes:**
- Timeout too short
- Single sensor can't see entire room
- Activity doesn't generate motion

**Solutions:**
✅ Increase timeout duration
✅ Add multiple sensors
✅ Use door sensor override
✅ Add manual extension button
✅ Consider presence sensors

### Challenge: Slow Response Time

**Causes:**
- Cloud processing delays
- Weak wireless signal
- Sensor sleep cycle
- Complex automation logic

**Solutions:**
✅ Use local automation processing
✅ Add Zigbee/Z-Wave repeaters
✅ Simplify automation conditions
✅ Update firmware
✅ Position sensor to detect entry earlier

---

## Best Practices

### Testing & Optimization

**Initial Setup:**
1. Mount temporarily with tape
2. Test all walking paths
3. Check different times of day
4. Verify with multiple people
5. Adjust as needed
6. Permanent installation

**Ongoing Maintenance:**
- Replace batteries annually (or before depletion)
- Clean sensor lens quarterly
- Verify operation monthly
- Update firmware when available
- Adjust for seasonal changes (if outdoor)

### Room-by-Room Strategy

**Start Small:**
1. Choose one high-traffic room
2. Implement basic automation
3. Test and refine for 1-2 weeks
4. Once working well, expand to next room
5. Learn and improve with each room

**Don't Rush:**
- One room at a time
- Perfect before expanding
- Learn what works for your household
- Build confidence in system

### Family Acceptance

**Make It Work for Everyone:**
- Get feedback from all household members
- Adjust to natural behavior patterns
- Provide manual overrides
- Keep physical switches functional
- Iterate based on real usage

**Guest-Friendly:**
- Automations should "just work"
- No explanation needed
- Physical switches as backup
- Predictable behavior

---

## Advanced Techniques

### Multi-Sensor Logic

Combine multiple sensor types for better accuracy:

```yaml
trigger:
  - platform: state
    entity_id: binary_sensor.motion_1
    to: 'on'
  - platform: state
    entity_id: binary_sensor.motion_2
    to: 'on'
condition:
  # Only if either sensor active OR lux is low
  - condition: or
    conditions:
      - condition: numeric_state
        entity_id: sensor.lux
        below: 100
      - condition: state
        entity_id: binary_sensor.motion_1
        state: 'on'
```

### Zone-Based Lighting

Different areas of large room get different lighting:

- Entry zone: Full brightness
- Seating zone: Medium brightness
- Reading nook: Warm, focused light
- TV area: Dim ambient light

### Adaptive Brightness

Adjust brightness based on:
- Time of day (gradual changes)
- Natural light levels (lux sensor)
- Activity type (watching TV vs. reading)
- Personal preferences (per-person detection)

### Activity Detection

Use motion patterns to detect activity:
- Rapid movement: Cleaning, playing
- Slow movement: Reading, relaxing
- No movement: Sleeping, away

Adjust automations based on detected activity.

---

**Get Started:**
- [Turn On Lights When Motion Detected →](/automation/motion/lights-on-motion/)
- [Turn Off Lights After Motion Stops →](/automation/motion/lights-off-after-motion/)
- [Bathroom Night Light →](/automation/motion/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/">← Back to All Automations</a>
  <a href="/automation/contact/">Next: Contact Sensors →</a>
</div>
