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
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Motion sensor state changes to "on"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Light level (lux) is below 100</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Night (10 PM - 6 AM):</strong> Set brightness to 10%
        </div>
        <div class="step-variant">
          <strong>Day (6 AM - 10 PM):</strong> Set brightness to 100%
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">IF</span>
        <span class="step-content">Motion is detected on sensor</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Time is between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on light to 10%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create second routine for daytime with 100% brightness
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Motion sensor active</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Mode is "Night" or time between 10 PM - 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set light to 10%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine or Simple Automation Rules
          <br/>
          <strong>Note:</strong> Create separate rule for daytime at 100%
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Motion sensor detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Time</span>
        <span class="step-content">Between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on bathroom light at 10%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Repeat for daytime hours at 100%
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Amazon Alexa logo">
      <h4>Alexa</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Motion sensor detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on light to 10%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create second routine for daytime with 100% brightness
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Motion sensor detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 10 PM - 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set light to 10%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create second routine for daytime with 100% brightness
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Multiple brightness levels</h3>
    <p>Create different levels throughout the night:</p>
    <div class="brightness-schedule">
      <div class="brightness-item">
        <span class="time-badge">9 PM - 11 PM</span>
        <span class="brightness-level">30%</span>
        <span class="brightness-desc">Still awake, need moderate light</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">11 PM - 5 AM</span>
        <span class="brightness-level">10%</span>
        <span class="brightness-desc">Minimal disturbance</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">5 AM - 7 AM</span>
        <span class="brightness-level">20%</span>
        <span class="brightness-desc">Gentle wake-up</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">7 AM - 9 PM</span>
        <span class="brightness-level">100%</span>
        <span class="brightness-desc">Full brightness</span>
      </div>
    </div>
  </div>
  
  <div class="feature-card">
    <h3>Lux-based activation</h3>
    <p>Only turn on lights if the room is actually dark:</p>
    <ul>
      <li>Add a condition that light level must be below a certain threshold (e.g., 100 lux)</li>
      <li>This prevents lights from turning on during daytime when natural light is sufficient</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Zone-based motion</h3>
    <p>For larger rooms, use multiple motion sensors to track which area someone is in and only light that zone.</p>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn on too slowly</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Delay between motion detection and lights turning on causes you to reach for the switch.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check sensor placement - should detect motion before entering room</li>
        <li>Reduce automation processing time - use local control instead of cloud</li>
        <li>Use faster communication protocols (Zigbee/Z-Wave vs WiFi)</li>
        <li>Optimize automation logic to minimize conditions</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn on when not needed</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lights activate from pets, sunlight reflections, or other false triggers.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Adjust motion sensor sensitivity</li>
        <li>Add lux sensor condition to prevent daytime activation</li>
        <li>Use pet-immune motion sensors</li>
        <li>Position sensor away from windows and heat sources</li>
        <li>Add time-based conditions</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Inconsistent performance</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sometimes works, sometimes doesn't.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check sensor battery levels</li>
        <li>Verify wireless signal strength (Zigbee/Z-Wave mesh)</li>
        <li>Replace batteries before completely dead</li>
        <li>Add repeaters/extenders for distant sensors</li>
        <li>Check for interference from other devices</li>
      </ul>
    </div>
  </div>
</div>

## Sensor placement best practices

<div class="placement-grid">
  <div class="placement-card">
    <h3>Height</h3>
    <ul>
      <li><strong>Optimal:</strong> 6-8 feet high for best coverage</li>
      <li><strong>Corners:</strong> Good for monitoring entire room</li>
      <li><strong>Entry points:</strong> Near doors for immediate detection</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Angle</h3>
    <ul>
      <li><strong>Ceiling mount:</strong> Wide coverage, detects all motion</li>
      <li><strong>Wall mount:</strong> Directional, catches people entering</li>
      <li><strong>Corner mount:</strong> 90° coverage, good for hallways</li>
    </ul>
  </div>
</div>

<div class="best-practice-card">
  <h3>Coverage testing</h3>
  <ol>
    <li>Mount sensor temporarily with tape</li>
    <li>Walk through room at different paths</li>
    <li>Verify all entry points are covered</li>
    <li>Check for dead zones</li>
    <li>Adjust position or add additional sensors</li>
    <li>Permanently mount once confirmed</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>Near windows</strong> - Sunlight and outdoor motion cause false triggers</li>
    <li><strong>Near heating/AC vents</strong> - Temperature changes trigger sensors</li>
    <li><strong>Pointed at moving objects</strong> - Ceiling fans, curtains, pets</li>
    <li><strong>Behind furniture</strong> - Blocks detection zone</li>
  </ul>
</div>

---

**Related automations:**
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/)
- [Nighttime bathroom lighting](/automation/lighting/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
