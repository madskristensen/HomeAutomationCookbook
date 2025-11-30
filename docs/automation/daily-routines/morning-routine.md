---
layout: automation
title: Morning Routine Automation - Wake Up Smart Home
description: Automate your morning routine with lights, coffee, music, and thermostat. Complete guide for morning automation with all major smart home platforms.
keywords: morning routine automation, wake up automation, smart home morning, automatic morning routine, morning lights automation
---

# Turn on all lights when you get up in the morning

The day begins before you are fully awake - lights rising gently, the coffee maker stirring to life, the thermostat nudging the house toward waking temperature. By the time your feet touch the floor, the home has already begun preparing itself, greeting you with warmth and light rather than darkness and cold.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Trigger Methods</h4>
    <ul>
      <li><strong>Weekday Mornings</strong> - Consistent wake-up routine</li>
      <li><strong>Motion-Triggered</strong> - Lights when you get out of bed</li>
      <li><strong>Time-Based</strong> - Scheduled wake-up time</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Activation Options</h4>
    <ul>
      <li><strong>Voice-Activated</strong> - "Good morning" routine</li>
      <li><strong>Button-Triggered</strong> - Bedside button press</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Lights</strong>
      <div class="product-details">
        Throughout house for automated morning routine
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        In bedroom or bathroom to detect wake-up
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Button</strong>
      <div class="product-details">
        Bedside trigger for one-press routine
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Thermostat</strong>
      <div class="product-details">
        Climate control for comfort
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Plugs</strong>
      <div class="product-details">
        For coffee maker and other appliances
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF time is 6:30 AM on weekdays
THEN turn on bedroom lights to 30%
AND start coffee maker
AND read morning briefing</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Time is between 6:00 AM and 9:00 AM</li>
      <li>AND motion detected in bedroom</li>
      <li>OR button pressed</li>
      <li>OR voice command "Good morning"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>House is in Night Mode</li>
      <li>Time is between 6:00 AM and 10:00 AM</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on main lights in house</li>
      <li>Put house in Home Mode</li>
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
        <span class="step-content">Bedroom motion sensor detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">House mode is "Night" AND Time is 6 AM - 10 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set mode to "Home", turn on morning lights</span>
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
        <span class="step-content">Motion in bedroom AND Time 6 AM - 10 AM AND Mode "Night"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Change mode to "Home" AND Turn on morning lights</span>
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
        <span class="step-content">Bedroom motion sensor active</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Mode is "Night" AND Time 6 AM - 10 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Change mode to "Day" + Turn on morning lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Mode Manager or Rule Machine
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
        <span class="step-content">Motion detected in bedroom</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Time</span>
        <span class="step-content">Between 6 AM and 10 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Activate "Good Morning" scene</span>
      </div>
    </div>
  </div>
</div>

## Morning (Home) mode actions

### Lighting
* **Kitchen** - 100% brightness
* **Bathroom** - 100% brightness
* **Hallway** - 80% brightness
* **Living room** - 60% (gentle)
* **Bedroom** - Keep off or 20%

### Climate
* **Increase thermostat** - 70°F (21°C)
* **Turn on bathroom fan** - If humid
* **Open smart blinds** - Let in sunlight

### Kitchen
* **Start coffee maker** - Via smart plug
* **Display weather** - On smart display
* **Turn on news** - Smart speaker (optional)

### Security
* **Disarm interior sensors**
* **Disable night cameras** - Interior only
* **Unlock certain doors** - If needed

### Announcements
* **Weather forecast**
* **Calendar events for today**
* **Commute time**
* **Reminders**

## Advanced morning routine

### Gradual wake-up (30 minutes before alarm)

Create automation that gradually increases bedroom light brightness:
- Start at 1% brightness at wake time (e.g., 6:00 AM)
- Gradually increase over 30 minutes
- Use repeat loop: wait 1 minute, increase brightness by 3%, repeat 30 times
- Final brightness reaches ~90% by end

### Weekday vs. weekend

**Weekday routine:**
- Earlier wake time
- News briefing
- Commute information

**Weekend routine:**
- Later wake time
- Music instead of news
- Relaxed lighting

## Related actions

See also:
- [Bedtime Routine](/automation/daily-routines/bedtime-routine/) - Evening counterpart
- [Set Away Mode](/automation/daily-routines/away-mode/) - Leaving home

<div class="page-navigation">
  <a href="/automation/daily-routines/">← Back to Daily Routines</a>
  <a href="/automation/">View All Automations →</a>
</div>
