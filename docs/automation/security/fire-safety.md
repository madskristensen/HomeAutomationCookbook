---
layout: automation
title: Fire Safety Emergency Response - Smart Home Automation
description: Automated fire emergency response when smoke detector sounds. Lights on, doors unlocked, irrigation started, notifications sent.
keywords: fire safety automation, smoke detector, emergency response, smart home safety, fire evacuation, home emergency, smoke alarm automation
---

# Get safely out of the house in case of fire

When smoke fills a house at 3 a.m., every second matters. In darkness, disoriented and alarmed, a family needs light to find their way, doors that open without fumbling, and a path clear to safety. This automation transforms the moment a smoke detector sounds into a coordinated response - lights blazing on, locks releasing, notifications flying to phones - giving everyone the best chance to get out safely.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Fire Emergency</h4>
    <ul>
      <li><strong>Smoke Detector Goes Off</strong> - Immediate emergency response</li>
      <li><strong>Nighttime Evacuation</strong> - All lights turn on for safe exit</li>
      <li><strong>Door Unlock</strong> - Quick escape without fumbling for locks</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Break-in Detection</h4>
    <ul>
      <li><strong>Window Breaks</strong> - Alert and response to glass break sound</li>
      <li><strong>Nighttime Intrusion</strong> - Lights and notifications activate</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Smoke Detector or Detection Method</strong>
      <div class="product-details">
        Options:<br>
        • Native smart detector: Nest Protect, First Alert Onelink<br>
        • Sound listener: Amazon Echo Guard feature, dedicated listeners<br>
        • Wired relay: Attached to existing smoke detector wiring
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Lights</strong>
      <div class="product-details">
        Whole-house smart lights for full illumination during emergency
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Door Lock</strong>
      <div class="product-details">
        Auto-unlock for quick escape
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Irrigation System</strong>
      <div class="product-details">
        Wet exterior to prevent fire spread (Rachio, RainMachine, etc.)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Glass Break Sensor</strong>
      <div class="product-details">
        Ring Glass Break, Aqara, SmartThings sensors
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>🔊 Smoke Detection Without Smart Detectors</strong>
  <p>If you don't have a smart smoke detector, there are alternatives you can use to make your existing detector smart:</p>
  <ul>
    <li><strong>Wired relays:</strong> Attach to existing smoke detector wiring, acts like an open/closed sensor when alarm sounds</li>
    <li><strong>Sound listeners:</strong> Devices that pick up the specific sound pattern of smoke detectors and send signals to your smart home</li>
    <li><strong>Amazon Echo Guard:</strong> Built into Echo devices, can detect smoke alarm sounds through its Guard feature</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF smoke detector goes off
THEN turn on all lights
AND unlock all doors
AND start outdoor irrigation
AND send notifications</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Smoke detector goes off (state changes to "smoke detected")</li>
      <li>OR Sound listener detects smoke alarm pattern</li>
      <li>OR Wired relay sensor changes state</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>None - this should always run when triggered</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on lights in the whole house (100% brightness)</li>
      <li>Unlock all doors</li>
      <li>Start the outdoor irrigation (if available)</li>
      <li>Send critical notifications to all family members</li>
      <li>Optional: Announce evacuation message on smart speakers</li>
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
        <span class="step-content">Smoke detector state changes to "on" or "smoke"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">None (always run)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">All lights 100% + Unlock doors + Start irrigation + Critical notifications</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Optional:</strong> TTS announcement "Fire alarm activated, evacuate immediately"
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
        <span class="step-content">Smoke detector detects smoke</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on all lights + Unlock doors + Start irrigation</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use SHM (SmartThings Home Monitor) for enhanced integration
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
        <span class="step-content">Smoke sensor active</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">All lights on + Doors unlocked + Irrigation on + Push notifications</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine or HSM (Hubitat Safety Monitor)
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
        <span class="step-content">Smoke detected by HomeKit smoke sensor</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on all lights + Unlock doors</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Limited irrigation control, notifications automatic
        </div>
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
        <span class="step-label">Setup</span>
        <span class="step-content">Enable Guard feature in Alexa app</span>
      </div>
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Guard detects emergency</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on all lights, Smart Alerts sends notifications</span>
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
        <span class="step-content">Smoke alarm activates (Nest Protect native)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on lights, send notifications</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Nest integrates with Works with Google devices
        </div>
      </div>
    </div>
  </div>
</div>

## Glass break detection setup

A variation of fire safety is detecting window break sounds:

<div class="automation-example">IF glass break detected
AND time is nighttime OR home is in Away mode
THEN turn on all lights
AND send critical alert
AND start recording cameras</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Glass break sensor detects breaking glass</li>
      <li>OR Sound listener detects glass break pattern</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>Time is between 10 PM and 6 AM</li>
      <li>OR Home is in Away mode</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on all interior and exterior lights</li>
      <li>Send high-priority notification with location</li>
      <li>Start camera recording</li>
      <li>Optional: Sound audible alarm</li>
      <li>Optional: Announce warning message</li>
    </ul>
  </div>
</div>

## Advanced features

### Zone-based evacuation lighting

Create lit paths to exits:

**Implementation:**
- Identify primary and secondary exit paths
- Light those paths at maximum brightness
- Include stairway and hallway lights
- Exterior lights illuminate exit points

**Automation Logic:**
1. Fire detected → All path lights to 100%
2. Exterior lights on to illuminate exits
3. Smart bulbs flash in exit direction (if supported)

<div class="feature-grid">
  <div class="feature-card">
    <h3>Smoke detector by room</h3>
    <p>Different response based on fire location:</p>
    <ul>
      <li><strong>Kitchen:</strong> Add 30-second delay (may be cooking), verify first</li>
      <li><strong>Bedroom:</strong> Immediate full response, no delay</li>
      <li><strong>Garage:</strong> Specific response, alert with location</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Irrigation for fire containment</h3>
    <p>Strategic irrigation activation:</p>
    <ul>
      <li>Activate zones closest to house</li>
      <li>Wet perimeter to slow fire spread</li>
      <li>Run 10-15 minutes, auto shutoff after 30</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Multi-alarm verification</h3>
    <p>Reduce false positives:</p>
    <ul>
      <li><strong>Single detector:</strong> Send alert, wait 30 seconds</li>
      <li><strong>Two+ detectors:</strong> Full emergency response</li>
      <li><strong>Continued alarm:</strong> Full response after delay</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Post-event automation</h3>
    <p>After emergency is handled:</p>
    <ul>
      <li>When smoke clears, wait 15 minutes</li>
      <li>Send "All clear" notification</li>
      <li>Return lights to previous state</li>
      <li>Relock doors (after verification)</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>False alarms from cooking</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Kitchen smoke detector too sensitive to steam or cooking smoke.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add delay for kitchen detector only</li>
        <li>Send verification alert before full response</li>
        <li>Use "photoelectric" type detector</li>
        <li>Relocate kitchen detector away from stove</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Doors don't unlock</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lock battery low or connectivity issue.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check lock battery regularly</li>
        <li>Verify lock responds to commands</li>
        <li>Test automation monthly</li>
        <li>Add lock to automation actions</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Notifications don't arrive</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Phone in Do Not Disturb or critical alerts not enabled.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use "critical" notification flags</li>
        <li>Enable emergency bypass in settings</li>
        <li>Test notifications during setup</li>
        <li>Use multiple notification methods</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Automation doesn't trigger</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Smoke detector not integrated or wrong trigger configured.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify smoke detector appears in smart home</li>
        <li>Check detector status and connectivity</li>
        <li>Test with manual trigger (test button)</li>
        <li>Review automation logs for errors</li>
      </ul>
    </div>
  </div>
</div>

## Safety considerations

### Test regularly

**Monthly:**
- Test smoke detectors
- Verify automation triggers
- Check all lights respond
- Test door unlocks
- Verify notifications arrive

**Annually:**
- Replace batteries
- Review evacuation plan
- Update family on procedures
- Test irrigation response

### Manual overrides

**Always Ensure:**
- Physical escape routes available
- Manual door locks work
- Physical light switches function
- Don't rely solely on automation

### Fire safety basics

**Remember:**
- Automation assists, doesn't replace safety planning
- Have multiple escape routes
- Practice fire drills with family
- Know when to evacuate vs. fight fire
- Call 911 first

---

**Related automations:**
- [Away lights](/automation/security/away-lights/)
- [Fake dog deterrent](/automation/security/fake-dog-deterrent/)
- [Away mode](/automation/daily-routines/away-mode/)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
