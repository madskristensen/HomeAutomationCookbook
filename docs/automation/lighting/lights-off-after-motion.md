---
layout: default
title: Turn Off Lights After Motion Stops - Smart Home Automation
description: Automatically turn off lights when no motion is detected. Complete guide with timing strategies, conditions, and platform examples for motion-based light control.
keywords: motion sensor lights off, automatic light shutoff, occupancy detection, smart lighting automation, turn off lights automatically
---

# Turn off lights after motion stops

While modern LED lights use minimal power, automatically turning off lights when a room is unoccupied creates a satisfying smart home experience and ensures energy isn't wasted. This automation completes the motion detection lighting cycle.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Quick Access Spaces</h4>
    <ul>
      <li><strong>Bathroom</strong> - Turn off lights 5 minutes after no motion detected</li>
      <li><strong>Closets</strong> - Turn off immediately after 1 minute (quick access areas)</li>
      <li><strong>Garage</strong> - Turn off after 3-5 minutes of no activity</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Living & Work Spaces</h4>
    <ul>
      <li><strong>Living Areas</strong> - Turn off lights 2 minutes after no motion at nighttime</li>
      <li><strong>Home Office</strong> - Longer delay (10 minutes) for stationary work</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        Same sensor used for turning lights on<br>
        Should detect motion continuously, not just entry<br>
        Battery life consideration: some sensors report too frequently
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Light Switch or Bulb</strong>
      <div class="product-details">
        Connected to your automation platform
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Outdoor Tip</strong>
  <ul>
    <li>Use weather-rated sensors (IP65+) or protect from elements</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF no motion detected for 5 minutes
THEN turn off lights</div>

<div class="info-box">
  <strong>⏱️ Timing Strategies by Room Type</strong>
  <ul>
    <li><strong>Quick Access (1-2 min):</strong> Closets, pantry, laundry room, hallways - Brief visits, quick in and out</li>
    <li><strong>Living Spaces (3-5 min):</strong> Living room, dining room, kitchen, home gym - May have brief stationary moments, but generally active</li>
    <li><strong>Work/Relaxation (5-10 min):</strong> Home office, reading nook, craft room, bathroom - People often sit still for extended periods</li>
    <li><strong>Bathroom Special:</strong> Use door sensor override (don't turn off if door closed), OR extended delay (10-15 min), OR multiple sensors</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Motion no longer detected for X minutes</li>
      <li>Fast-access areas: 1-2 minutes</li>
      <li>Living spaces: 3-5 minutes</li>
      <li>Work areas: 5-10 minutes</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Time-based:</strong> Different delays for day vs. night<br>
    <strong>Door status:</strong> Don't turn off if bathroom door is closed (someone may be sitting still)<br>
    <strong>Additional sensors:</strong> Check other sensors in room for activity
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn off light switch/bulb</li>
      <li>Can include gradual dimming before turning off (advanced)</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
      <h4>Home Assistant</h4>
    </div>
    <ol>
      <li>Trigger: Bathroom motion sensor no motion for 5 minutes</li>
      <li>Condition: Bathroom door sensor shows door is open (not in use)</li>
      <li>Action: Turn off bathroom light</li>
      <li>Advanced: Dim to 50% after 3 min, wait 30 sec, check motion, then off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <ol>
      <li>IF: Motion sensor no motion for 5 minutes</li>
      <li>AND: Door sensor is open</li>
      <li>THEN: Turn off light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <ol>
      <li>Use Motion Lighting app or Rule Machine</li>
      <li>Trigger: Motion inactive for 5 minutes</li>
      <li>Condition: Door contact is open</li>
      <li>Action: Turn off light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <ol>
      <li>When: Motion stops</li>
      <li>Wait for: 5 minutes</li>
      <li>If: Bathroom door is open</li>
      <li>Do: Turn off bathroom light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa</h4>
    </div>
    <ol>
      <li>When: Motion sensor detects no motion for 5 minutes</li>
      <li>Condition: Door contact is open</li>
      <li>Action: Turn off light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <ol>
      <li>Starter: Motion no motion for 5 minutes</li>
      <li>Condition: Door sensor is open</li>
      <li>Action: Turn off light</li>
    </ol>
  </div>
</div>

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
- [Turn on lights when motion detected](/automation/lighting/lights-on-motion/)
- [Bathroom night light automation](/automation/lighting/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
