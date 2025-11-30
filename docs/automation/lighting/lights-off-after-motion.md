---
layout: automation
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
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Bathroom motion sensor no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Bathroom door sensor shows door is open (not in use)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off bathroom light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Advanced:</strong> Dim to 50% after 3 min, wait 30 sec, check motion, then off
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
        <span class="step-content">Motion sensor no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Door sensor is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn off light</span>
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
        <span class="step-content">Motion inactive for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door contact is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Motion Lighting app or Rule Machine
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
        <span class="step-content">Motion stops</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Wait</span>
        <span class="step-content">5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">If</span>
        <span class="step-content">Bathroom door is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn off bathroom light</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Motion sensor detects no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door contact is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
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
        <span class="step-content">Motion no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door sensor is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Day vs. night timing</h3>
    <p>Create separate automations with different delay times:</p>
    <ul>
      <li><strong>Daytime:</strong> Shorter delays (2-3 minutes), more active movement</li>
      <li><strong>Nighttime:</strong> Longer delays (5-10 minutes), slower movement</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Multiple sensor logic</h3>
    <p>For larger rooms, use multiple sensors to ensure no one is present:</p>
    <ul>
      <li>All motion sensors must show "no motion" before turning off</li>
      <li>Set appropriate delay (e.g., 5 minutes)</li>
      <li>Prevents false shutoffs in sensor blind spots</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Activity-based override</h3>
    <p>Don't turn off lights if other activity detected:</p>
    <ul>
      <li>TV is on in the room</li>
      <li>Music is playing</li>
      <li>Computer is active</li>
      <li>Smart plug shows power usage</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn off while room is occupied</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Person sitting very still, motion sensor dead zone, or delay too short.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add door sensor - don't turn off if door closed</li>
        <li>Use longer delay (5-10 minutes instead of 2-3)</li>
        <li>Add additional motion sensors for full coverage</li>
        <li>Use occupancy sensors instead of motion</li>
        <li>Add manual override button to extend time</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights stay on too long after leaving</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Delay too long or sensor sees movement outside room (hallway traffic).
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reduce delay time</li>
        <li>Reposition sensor to focus on room interior only</li>
        <li>Add door sensor - turn off immediately when door closes</li>
        <li>Use presence detection for faster response</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Inconsistent behavior</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sometimes works, sometimes doesn't respond at all.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Replace batteries before fully depleted</li>
        <li>Add Zigbee/Z-Wave repeaters</li>
        <li>Check sensor configuration</li>
        <li>Update firmware</li>
        <li>Test sensor range and coverage</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="placement-grid">
  <div class="placement-card">
    <h3>Testing your delays</h3>
    <ul>
      <li><strong>Start conservative:</strong> 10 minute delay initially</li>
      <li><strong>Monitor:</strong> Watch for false shutoffs over several days</li>
      <li><strong>Gradually reduce:</strong> Find the sweet spot</li>
      <li><strong>Room-specific:</strong> Different delay per room type</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Sensor coverage verification</h3>
    <ul>
      <li>Walk through room at different paths</li>
      <li>Stand still in each area for 2 minutes</li>
      <li>Verify motion sensor still "sees" you</li>
      <li>Add sensors to eliminate dead zones</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Manual override options</h3>
    <p>Always provide a way to override automation:</p>
    <ul>
      <li><strong>Physical switch:</strong> Manual operation keeps lights on indefinitely</li>
      <li><strong>Voice command:</strong> "Keep bathroom lights on" for 30 min override</li>
      <li><strong>Dashboard button:</strong> Toggle to disable/enable automation</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Energy savings</h3>
    <p>While LED bulbs use minimal power, automatic shutoff still provides benefits:</p>
    <ul>
      <li>10W LED × 2 hours/day = 7.3 kWh/year per bulb</li>
      <li>Halogen/incandescent: 60W bulbs save 10x more</li>
      <li>Commercial spaces: significant savings</li>
      <li>Environmental impact: reduced energy generation</li>
    </ul>
  </div>
</div>

---

**Related automations:**
- [Turn on lights when motion detected](/automation/lighting/lights-on-motion/)
- [Bathroom night light automation](/automation/lighting/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
