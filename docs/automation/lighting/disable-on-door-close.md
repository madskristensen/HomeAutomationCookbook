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
        <span class="step-content">Bathroom door sensor is "open"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off bathroom light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Adjust based on your sensor's open/closed values
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
        <span class="step-label">Trigger</span>
        <span class="step-content">Motion inactive for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door sensor is "open"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use SharpTools for advanced conditions
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
        <span class="step-content">Motion inactive (canceled) for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Expression</span>
        <span class="step-content">Door contact is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine for complex logic
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Manual disable mode</h3>
    <p>Add a physical button to manually disable all automations in a room:</p>
    <ul>
      <li><strong>Trigger:</strong> Disable button pressed</li>
      <li><strong>Action:</strong> Toggle automation disabled mode</li>
      <li><strong>Condition:</strong> Add to all automations: mode is OFF</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Visual indicator</h3>
    <p>Use LED strip or smart bulb to show automation status:</p>
    <ul>
      <li><strong>When disabled:</strong> Set status light to red</li>
      <li><strong>When enabled:</strong> Set status light to green</li>
      <li><strong>Trigger:</strong> Automation mode changes</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Time-based auto-resume</h3>
    <p>Automatically re-enable automations after a set period:</p>
    <ul>
      <li><strong>Trigger:</strong> Disabled mode has been ON for 2 hours</li>
      <li><strong>Action:</strong> Turn off disabled mode (re-enable)</li>
      <li>Prevents accidentally leaving automations disabled</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights still turn off when door closed</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Condition logic may not match your sensor's behavior.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check door sensor state in app (is "closed" showing as 'on' or 'off'?)</li>
        <li>Verify condition logic matches your sensor's behavior</li>
        <li>Confirm automation is actually using the condition</li>
        <li>Reverse the door state condition if needed</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Door sensor not reliable</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sensor too far from magnet, battery low, or door doesn't close fully.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reposition for better alignment</li>
        <li>Replace battery</li>
        <li>Adjust door latch/strike plate</li>
        <li>Use tilt sensor instead of contact sensor</li>
      </ul>
    </div>
  </div>
</div>

---

**Related automations:**
- [Toggle lights on door open](/automation/lighting/toggle-lights-door/)
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
