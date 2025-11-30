---
layout: automation
title: Pause HVAC When Window Opens - Smart Climate Automation
description: Automatically pause heating or cooling when a window or door opens. Save energy and get a visual reminder with a blinking light.
keywords: window open HVAC, pause air conditioning, smart thermostat window, energy saving automation, window sensor thermostat, climate automation, HVAC efficiency
---

# Pause HVAC when window opens

Stop wasting energy heating or cooling the outdoors. This automation automatically pauses your HVAC system when a window or patio door opens and provides a visual reminder with a blinking light so you know to close it.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Energy savings</h4>
    <ul>
      <li><strong>Fresh air breaks</strong> - Open windows without wasting energy</li>
      <li><strong>Kids leaving doors open</strong> - Auto-pause prevents waste</li>
      <li><strong>Patio entertaining</strong> - Don't cool the backyard</li>
      <li><strong>Forgotten windows</strong> - System adapts automatically</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Visual reminders</h4>
    <ul>
      <li><strong>Blinking light signal</strong> - Know a window is open at a glance</li>
      <li><strong>Kitchen indicator</strong> - See status while cooking</li>
      <li><strong>Entry reminder</strong> - Notice when leaving</li>
      <li><strong>Night check</strong> - Quick visual scan before bed</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Window/door contact sensors</strong>
      <div class="product-details">
        Popular brands: Aqara, SmartThings, Eve, Wyze<br>
        Place on each window and exterior door you want to monitor
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart thermostat</strong>
      <div class="product-details">
        Brands: Ecobee, Nest, Honeywell Home, Emerson Sensi<br>
        Must support remote control via smart home platform
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart light for indicator</strong>
      <div class="product-details">
        Any color-capable smart bulb for visual "window open" indicator<br>
        Brands: Philips Hue, LIFX, Wyze Bulb Color
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart speaker</strong>
      <div class="product-details">
        For voice announcements when windows open/close
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Energy savings tip</strong>
  <ul>
    <li>This automation can save 10-25% on HVAC costs during temperate months</li>
    <li>Even 10 minutes of open window with HVAC running wastes significant energy</li>
    <li>The visual indicator helps develop better habits over time</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF any window or patio door opens
AND HVAC is currently running (heating or cooling)
THEN pause HVAC (set to "off" or "eco" mode)
AND start blinking indicator light (on/off every 2 seconds)
AND send notification "Window open - HVAC paused"

IF all windows and doors are closed
AND HVAC was paused due to open window
THEN resume previous HVAC mode
AND stop indicator light blinking
AND send notification "All closed - HVAC resumed"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Any window contact sensor changes to "open"</li>
      <li>OR any patio door contact sensor changes to "open"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>HVAC status:</strong> Thermostat is actively heating or cooling<br>
    <strong>Temperature:</strong> Outside temp differs significantly from inside (optional)<br>
    <strong>Duration:</strong> Add 30-second delay before pausing (avoids quick open/close)
  </div>
  
  <div class="setup-step">
    <h4>Actions when window opens</h4>
    <ul>
      <li>Save current thermostat mode (for later restore)</li>
      <li>Set thermostat to "off" or "eco" mode</li>
      <li>Start indicator light blinking pattern</li>
      <li>Send notification: "Living room window open - HVAC paused"</li>
      <li>Optional: Announce on smart speaker</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions when all windows close</h4>
    <ul>
      <li>Restore thermostat to previous mode</li>
      <li>Turn off indicator light (or return to normal)</li>
      <li>Send notification: "All windows closed - HVAC resumed"</li>
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
        <span class="step-content">Any sensor in "windows" group changes to "on" (open)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">climate.thermostat hvac_action is "heating" or "cooling"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Save state, set HVAC off, start light flash script</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use input_select to store previous HVAC mode for restoration
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
        <span class="step-content">Any contact sensor opens (create group)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Thermostat is running</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Set thermostat to Off, turn on indicator light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create separate routine for when all sensors close
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
        <span class="step-content">Contact sensor group any member opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Thermostat operating state is heating/cooling</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set thermostat off, activate indicator blink</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with variable to store previous mode
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
        <span class="step-content">Any window/door sensor opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Thermostat is heating or cooling</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn off thermostat, turn on indicator</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create automation for each sensor or use Shortcuts for group logic
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
        <span class="step-content">Contact sensor opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set thermostat to off, turn on indicator light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Create routine for each sensor or use virtual group device
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
        <span class="step-label">Starter</span>
        <span class="step-content">Contact sensor opens (if supported)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off thermostat, turn on light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Limited sensor support - may need Home Assistant or IFTTT
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Blinking indicator patterns</h3>
    <p>Different signals for different situations:</p>
    <ul>
      <li><strong>Slow blink (2 sec):</strong> One window open</li>
      <li><strong>Fast blink (0.5 sec):</strong> Multiple windows open</li>
      <li><strong>Color change:</strong> Blue = winter (heating paused), Red = summer (cooling paused)</li>
      <li><strong>Brightness:</strong> Dim during day, brighter at night</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Smart delay logic</h3>
    <p>Avoid constant on/off cycling:</p>
    <ul>
      <li><strong>30-second delay:</strong> Wait before pausing HVAC</li>
      <li><strong>Grace period:</strong> Don't resume if another window opens within 1 minute</li>
      <li><strong>Cooldown:</strong> Don't pause again within 5 minutes of resuming</li>
      <li><strong>Quick access exception:</strong> Don't pause for &lt;30 second door opens</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Temperature-aware</h3>
    <p>Only pause when it matters:</p>
    <ul>
      <li>Skip pause if outside temp is comfortable (65-75°F / 18-24°C)</li>
      <li>Immediate pause if outside temp is extreme</li>
      <li>Consider humidity differences</li>
      <li>Factor in sunny vs. shady side of house</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>HVAC keeps cycling on and off</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Frequent short window openings cause constant HVAC toggling.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add 30-60 second delay before pausing HVAC</li>
        <li>Add 2-minute delay before resuming HVAC</li>
        <li>Ignore windows that open for less than 30 seconds</li>
        <li>Add cooldown period between state changes</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>HVAC doesn't resume after closing</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Windows closed but HVAC stays off.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify all sensors are reporting correctly</li>
        <li>Check that "resume" automation is enabled</li>
        <li>Ensure previous mode was properly saved</li>
        <li>Add fallback timer to resume after 1 hour regardless</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Indicator light annoying at night</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Blinking light too bright or distracting when sleeping.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reduce brightness of indicator at night (10% vs 50%)</li>
        <li>Use slower blink rate at night</li>
        <li>Switch to solid on instead of blinking after 10 PM</li>
        <li>Use indicator in non-bedroom area only</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Too many notifications</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Getting notification for every window open/close.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Only notify on first open and final close</li>
        <li>Use visual indicator instead of phone notifications</li>
        <li>Batch notifications (summarize every 5 minutes)</li>
        <li>Only notify if window open for more than 5 minutes</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="best-practice-card">
  <h3>Setting up window HVAC pause</h3>
  <ol>
    <li>Install contact sensors on all windows and exterior doors</li>
    <li>Create a sensor group for easier automation</li>
    <li>Add delay before pausing to avoid quick open/close triggers</li>
    <li>Store previous HVAC mode for proper restoration</li>
    <li>Choose indicator light location visible from main areas</li>
    <li>Test thoroughly before relying on automation</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>No delay</strong> - Quick door opens will constantly toggle HVAC</li>
    <li><strong>No restoration</strong> - Forgetting to resume HVAC after windows close</li>
    <li><strong>Too sensitive</strong> - Every brief door opening shouldn't trigger</li>
    <li><strong>Bedroom indicator</strong> - Blinking lights disrupt sleep</li>
  </ul>
</div>

---

**Related automations:**
- [Thermostat - windows open](/automation/climate/thermostat-windows-open/)
- [Thermostat - windows close](/automation/climate/thermostat-windows-close/)
- [Window notifications](/automation/climate/window-notifications/)

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
