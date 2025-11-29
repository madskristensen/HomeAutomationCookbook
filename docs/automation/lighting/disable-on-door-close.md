---
layout: default
title: Disable Automations When Door is Closed - Smart Override System
description: Learn how to prevent motion sensor lights from turning off when bathroom or bedroom doors are closed. Complete guide with door sensor override logic.
keywords: disable automation door closed, bathroom door sensor, automation override, door sensor logic, prevent lights turning off
---

# Disable automations when door is closed

Prevent frustration when motion-based lighting turns off while you're sitting still in the bathroom or bedroom. This automation uses a door sensor to intelligently override motion timeout behavior.

<div class="info-box">
  <strong>⚠️ The Problem: Motion Sensors Can't Detect Stationary People</strong>
  <ul>
    <li>Sitting on toilet</li>
    <li>Taking a shower</li>
    <li>Lying in bed reading</li>
    <li>Working at desk</li>
    <li><strong>Result:</strong> Lights turn off unexpectedly, leaving you in the dark</li>
  </ul>
</div>

<div class="info-box">
  <strong>✅ The Solution: Door Sensor Override</strong>
  <ul>
    <li><strong>Door closed</strong> = Someone is inside, keep lights on</li>
    <li><strong>Door open</strong> = Room is empty (after motion timeout), safe to turn off lights</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Private Spaces</h4>
    <ul>
      <li><strong>Bathroom</strong> - People sitting still on toilet or in shower</li>
      <li><strong>Bedroom</strong> - Guest room during naps or sleep</li>
      <li><strong>Reading Nook</strong> - Sitting still while reading</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Work & Entertainment</h4>
    <ul>
      <li><strong>Home Office</strong> - Working at computer without much movement</li>
      <li><strong>Media Room</strong> - Watching movies in reclined position</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Contact Sensor</strong>
      <div class="product-details">
        Mounted on door and frame
      </div>
    </div>
    
    <div class="product-item">
      <strong>Existing Motion Sensor</strong>
      <div class="product-details">
        Already installed for lights
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Light</strong>
      <div class="product-details">
        Switch or bulb
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💻 Platform Requirements</strong>
  <ul>
    <li><strong>Full Support:</strong> Home Assistant, SmartThings (with SharpTools), Hubitat, HomeSeer - These platforms support variables or virtual switches needed for this automation</li>
    <li><strong>Limited Support:</strong> Alexa, Google Home (use workarounds), Apple HomeKit (requires Homebridge for full functionality)</li>
  </ul>
</div>

## Automation setup

<div class="setup-steps">
  <div class="setup-step">
    <h4>Scenario 1: Bathroom (Keep Lights On When Door Closed)</h4>
    <p><strong>Original automation (problem):</strong> Trigger: No motion for 5 minutes → Action: Turn off bathroom light → <em>Issue: Turns off while someone is sitting still inside</em></p>
    <p><strong>Improved automation (solution):</strong></p>
  </div>
  
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>No motion detected for 5 minutes</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>Door is OPEN (not closed)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn off bathroom light</li>
    </ul>
    <p><strong>Logic:</strong> Only turn off lights if: (1) No motion detected for 5 minutes AND (2) Door is open (meaning no one is inside)</p>
  </div>
  
  <div class="setup-step">
    <h4>Scenario 2: Guest Room (Delay After Entry)</h4>
    <p>Prevent lights from turning on automatically when guests are resting:</p>
  </div>
  
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Guest room motion detected</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>Door has been open for 5+ minutes</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on guest room light</li>
    </ul>
    <p><strong>Logic:</strong> If guest leaves room and returns within 5 minutes, lights don't turn on automatically. Helpful for naps, early bedtimes, and privacy.</p>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Bathroom motion sensor no motion for 5 minutes</li>
      <li>Condition: Bathroom door sensor is "open"</li>
      <li>Action: Turn off bathroom light</li>
      <li>Note: Adjust based on your sensor's open/closed values</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings (with SharpTools)</h4>
    <ol>
      <li>Create rule in SharpTools</li>
      <li>Trigger: Motion inactive for 5 minutes</li>
      <li>Condition: Door sensor is "open"</li>
      <li>Action: Turn off light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat (Rule Machine)</h4>
    <ol>
      <li>Create new rule</li>
      <li>Trigger: Motion inactive (canceled) for 5 minutes</li>
      <li>Required Expression: Door contact is open</li>
      <li>Actions to Run: Off: Light</li>
    </ol>
  </div>
</div>

## Advanced implementations

### Manual disable mode with button

Add a physical button to manually disable all automations in a room:
- **Trigger:** Disable button pressed
- **Action:** Toggle automation disabled mode

Then add condition to all automations:
- **Condition:** Automation disabled mode is OFF

This allows manual override when needed.

### Visual indicator

Use LED strip or smart bulb to show automation status:
- **When disabled:** Set status light to red
- **When enabled:** Set status light to green
- **Trigger:** Automation disabled mode changes

Provides visual feedback of automation state.

### Time-based auto-resume

Automatically re-enable automations after a set period:
- **Trigger:** Automation disabled mode has been ON for 2 hours
- **Action:** Turn off disabled mode (re-enable automations)

Prevents accidentally leaving automations disabled permanently.

## Troubleshooting

### Lights still turn off when door closed

**Check:**
- Door sensor state in app (is "closed" showing as 'on' or 'off'?)
- Condition logic matches your sensor's behavior
- Automation is actually using the condition

**Fix:** Reverse the door state condition if needed. If your sensor shows 'on' when closed, use 'on' in the condition instead of 'off'.

### Door sensor not reliable

**Causes:**
- Sensor too far from magnet
- Battery low
- Door doesn't close fully

**Solutions:**
- Reposition for better alignment
- Replace battery
- Adjust door latch/strike plate
- Use tilt sensor instead of contact sensor

---

**Related automations:**
- [Toggle lights on door open](/automation/lighting/toggle-lights-door/)
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
