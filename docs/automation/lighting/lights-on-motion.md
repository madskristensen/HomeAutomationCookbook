---
layout: default
title: Turn On Lights When Motion is Detected - Smart Home Automation Guide
description: Learn how to automatically turn on lights when motion is detected. Step-by-step guide for motion sensor lighting automation with examples for all smart home platforms.
keywords: motion sensor, automatic lights, smart home lighting, motion detection, home automation, smart lights
---

# Turn on lights when motion is detected

Automatically turning on lights when motion is detected is one of the most popular and useful smart home automations. It solves the everyday problem of fumbling for light switches in the dark and creates a seamless, effortless lighting experience.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Indoor Automation</h4>
    <ul>
      <li><strong>Nighttime Navigation</strong> - Bathroom lights turn on at low brightness when you get up at night</li>
      <li><strong>Home Office</strong> - Lights automatically turn on when you enter your workspace</li>
      <li><strong>Hallways</strong> - Lights turn on as you move through the house</li>
      <li><strong>Closets</strong> - No more fumbling for switches in dark spaces</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Outdoor Automation</h4>
    <ul>
      <li><strong>Garden Shed</strong> - Motion sensor triggers light when you enter</li>
      <li><strong>Porch Light</strong> - Automatically lights up for guests and delivery drivers</li>
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
        Popular brands: Philips Hue, Aqara, SmartThings, Wyze<br>
        Indoor: Standard motion sensors • Outdoor: Weatherproof IP65+ rated sensors
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Light Switch or Bulb</strong>
      <div class="product-details">
        Switches: Lutron, GE, Inovelli, Leviton<br>
        Bulbs: Philips Hue, LIFX, Wyze, Sengled
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Outdoor Motion Sensing Tip</strong>
  <ul>
    <li>Use sensors specifically rated for outdoor use (IP65 or higher)</li>
    <li>OR protect indoor sensors with weatherproof enclosures</li>
    <li>OR place sensors under eaves to avoid direct water exposure</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF motion detected
THEN turn on lights to 100%</div>

<div class="info-box">
  <strong>🌞 Day vs. Night Dimming Enhancement</strong>
  <ul>
    <li><strong>Daytime:</strong> Brightness 100% OR skip turning on if room has natural light (use lux sensor)</li>
    <li><strong>Nighttime (9 PM - 11 PM):</strong> Medium brightness 50%</li>
    <li><strong>Deep Night (11 PM - 6 AM):</strong> Low brightness 10-20% with warm color temperature</li>
    <li><strong>Early Morning (6 AM - 9 AM):</strong> Full brightness 100%</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Motion detected by sensor</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Time-based:</strong> Different behavior for day vs. night<br>
    <strong>Lux sensor:</strong> Only activate if room is dark (below certain lux level)<br>
    <strong>Home mode:</strong> Only when home is occupied
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on light switch or bulb</li>
      <li>Set to preferred brightness level (dimming percentage)</li>
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
      <li>Trigger: Motion sensor state changes to "on"</li>
      <li>Condition: Light level (lux) is below 100</li>
      <li>Action: Turn on bathroom light</li>
      <li>If time 10 PM - 6 AM: Set brightness to 10%</li>
      <li>If time 6 AM - 10 PM: Set brightness to 100%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <ol>
      <li>IF: Motion is detected on sensor</li>
      <li>AND: Time is between 10 PM and 6 AM</li>
      <li>THEN: Turn on light to 10%</li>
      <li>Create second routine for daytime with 100% brightness</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <ol>
      <li>Use Rule Machine or Simple Automation Rules</li>
      <li>Trigger: Motion sensor active</li>
      <li>Condition: Mode is "Night" or time between 10 PM - 6 AM</li>
      <li>Action: Set light to 10%</li>
      <li>Create separate rule for daytime at 100%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <ol>
      <li>When: Motion sensor detects motion</li>
      <li>Time: Between 10 PM and 6 AM</li>
      <li>Do: Turn on bathroom light at 10%</li>
      <li>Repeat for daytime hours at 100%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Amazon Alexa logo">
      <h4>Alexa</h4>
    </div>
    <ol>
      <li>When: Motion sensor detects motion</li>
      <li>Condition: Between 10 PM and 6 AM</li>
      <li>Action: Turn on light to 10%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <ol>
      <li>When: Motion sensor detects motion</li>
      <li>Condition: Time between 10 PM - 6 AM</li>
      <li>Action: Set light to 10%</li>
    </ol>
  </div>
</div>

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
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/)
- [Nighttime bathroom lighting](/automation/lighting/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
