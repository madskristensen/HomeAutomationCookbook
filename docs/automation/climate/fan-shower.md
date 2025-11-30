---
layout: automation
title: Turn On Bathroom Fan When Starting Shower - Climate Automation
description: Automatically turn on your bathroom fan when starting a shower. Guide covers multiple trigger methods including lights, humidity sensors, and door contacts.
keywords: bathroom fan automation, shower fan control, humidity sensor automation, automatic fan, bathroom ventilation, smart fan switch, prevent mirror fog, mold prevention
---

# Turn on bathroom fan when starting shower

In the quiet rush of a morning shower, who remembers the ceiling fan? Yet steam rises, mirrors fog, and moisture settles into walls and grout where it does not belong. This automation remembers for you - the fan awakens as the water runs, drawing humid air away before it can do any harm.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Convenience & Comfort</h4>
    <ul>
      <li><strong>Morning Shower</strong> - Automatically turn on fan when starting your morning shower</li>
      <li><strong>Prevent Mirror Fog</strong> - Keep bathroom mirrors clear during showers</li>
      <li><strong>Multi-User Households</strong> - Everyone gets fan benefits without remembering</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Health & Safety</h4>
    <ul>
      <li><strong>Humidity Control</strong> - Reduce excess moisture to prevent mold and mildew</li>
      <li><strong>Bathroom Ventilation</strong> - Improve air quality automatically</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Fan Switch</strong>
      <div class="product-details">
        Popular brands: Lutron, GE, Leviton, Inovelli<br>
        WiFi or Zigbee • Works with existing fan • Load rating sufficient for fan motor
      </div>
    </div>
    
    <div class="product-item">
      <strong>Trigger Option (choose one)</strong>
      <div class="product-details">
        <strong>Smart Light Switch:</strong> Trigger when shower lights turn on (easiest method)<br>
        <strong>Contact Sensor:</strong> Trigger when shower door opens (best for glass enclosures)<br>
        <strong>Humidity Sensor:</strong> Trigger when humidity rises (most accurate - Aqara, Sonoff, Zigbee)
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Multi-Sensor</strong>
      <div class="product-details">
        Combines temperature, humidity, and motion for advanced control
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Speaker</strong>
      <div class="product-details">
        Announce "Fan turned on" or play shower music
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF shower lights turn on
THEN turn on bathroom fan</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers (choose one method)</h4>
    <strong>Method 1 - Light-based:</strong> Shower lights turn on<br>
    <strong>Method 2 - Door sensor:</strong> Shower door opens (contact sensor)<br>
    <strong>Method 3 - Humidity-based:</strong> Bathroom humidity rises above 75%
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>Time-Based:</strong> Only between 5 AM and 11 PM (quiet hours at night)<br>
    <strong>Home Mode:</strong> Only when someone is home
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on bathroom fan switch</li>
      <li>Optional: Set fan to specific speed if multi-speed fan</li>
      <li>Optional: Send notification "Bathroom fan activated"</li>
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
        <span class="step-content">Shower lights turn on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time is between 5 AM and 11 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom fan switch</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Alt trigger:</strong> Humidity rises above 75%
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
        <span class="step-content">Shower lights turn on AND Time is 5 AM - 11 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on bathroom fan switch</span>
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
        <span class="step-content">Shower light turns on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time 5 AM - 11 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom fan</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Simple Automation Rules or Rule Machine
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
        <span class="step-content">Shower light turns on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time is between 5:00 AM and 11:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on bathroom fan</span>
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
        <span class="step-content">Shower light turns on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 5:00 AM - 11:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom fan</span>
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
        <span class="step-content">Shower light turns on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 5:00 AM - 11:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom fan</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Automatic fan shutoff</h3>
    <p>Turn off the fan automatically after the shower ends:</p>
    <ul>
      <li><strong>Trigger:</strong> Shower lights turn off for 10 minutes</li>
      <li><strong>Action:</strong> Turn off bathroom fan</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Humidity-based shutoff</h3>
    <p>Turn off when humidity returns to normal:</p>
    <ul>
      <li><strong>Trigger:</strong> Humidity drops below 60% for 5 min</li>
      <li><strong>Condition:</strong> Fan is currently on</li>
      <li><strong>Action:</strong> Turn off bathroom fan</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Bonus automations</h3>
    <p>Since your smart home now knows when you're showering:</p>
    <ul>
      <li><strong>Play Music:</strong> Start shower playlist on speaker</li>
      <li><strong>Flash Lights:</strong> Alert when doorbell rings</li>
      <li><strong>Lock Front Door:</strong> Secure home while showering</li>
      <li><strong>Adjust Thermostat:</strong> Increase bathroom temp</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Fan doesn't turn on</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Smart fan switch not responding or automation disabled.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Test fan switch manually through app</li>
        <li>Check automation triggers - simulate shower start</li>
        <li>Verify automation is enabled in your platform</li>
        <li>Ensure physical fan switch is in "on" position</li>
        <li>Check fan switch load rating matches fan motor</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Fan turns on at wrong times</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Multiple triggers firing or humidity sensor triggered by other sources.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Review automation logs to see what triggered</li>
        <li>Add time-based conditions to limit hours</li>
        <li>Increase humidity threshold (try 80% instead of 75%)</li>
        <li>Add delay: Only trigger if condition persists for 2-3 min</li>
        <li>Use multiple conditions: Light ON + Humidity rising</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Fan doesn't turn off</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Auto-off automation not created or humidity not dropping.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Create separate automation for fan shutoff</li>
        <li>Increase shutoff delay if humidity drops slowly</li>
        <li>Check bathroom ventilation - fan may need cleaning</li>
        <li>Add manual override button</li>
        <li>Set maximum run time: Off after 30 minutes regardless</li>
      </ul>
    </div>
  </div>
</div>

---

**Related automations:**
- [Play music when shower starts](/automation/entertainment/shower-music/)
- [Morning routine automation](/automation/daily-routines/morning-routine/)
- [Maintain room temperature with smart heater](/automation/climate/room-heater-maintain-temp/)

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
