---
layout: automation
title: Auto-Close Garage When Left Open - Smart Home Security
description: Automatically close your garage door when left open and nobody's home. Get a photo notification for peace of mind with this smart garage automation.
keywords: auto close garage, garage door automation, smart garage, garage security, garage left open, automatic garage close, garage notification photo
---

# Auto-close garage when forgotten

You are halfway to work when the doubt creeps in: did I close the garage? With this automation, you need not turn around to check. If the door stands open after everyone has gone, the house takes care of it - lowering the door and sending a photo as proof, so you can carry on with your day in peace.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Security scenarios</h4>
    <ul>
      <li><strong>Forgot to close</strong> - Auto-closes after you drive away</li>
      <li><strong>Kids left it open</strong> - Closes automatically when family leaves</li>
      <li><strong>Running late</strong> - Don't worry about going back to check</li>
      <li><strong>Package protection</strong> - Keep deliveries safe from theft</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Peace of mind</h4>
    <ul>
      <li><strong>Photo confirmation</strong> - See that it actually closed</li>
      <li><strong>Weather protection</strong> - Keep rain and snow out</li>
      <li><strong>Energy savings</strong> - Don't heat or cool the outdoors</li>
      <li><strong>Pest prevention</strong> - Keep animals out of garage</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart garage door controller</strong>
      <div class="product-details">
        Popular brands: Chamberlain myQ, Tailwind iQ3, Meross, Ratgdo<br>
        Must support remote open/close and status reporting
      </div>
    </div>
    
    <div class="product-item">
      <strong>Presence detection</strong>
      <div class="product-details">
        Options: Phone GPS/geofencing, smart home presence sensors, Life360<br>
        Must accurately detect when all family members have left
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Garage camera</strong>
      <div class="product-details">
        Brands: Wyze, Blink, Ring, Arlo, Reolink<br>
        Provides photo/video confirmation of garage status
      </div>
    </div>
    
    <div class="product-item">
      <strong>Motion sensor in garage</strong>
      <div class="product-details">
        Prevents closing if someone is still in the garage working
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Safety first</strong>
  <ul>
    <li>Ensure your garage door has working safety sensors (photo-eyes)</li>
    <li>Always send a warning notification before auto-closing</li>
    <li>Add a motion sensor to detect if someone is in the garage</li>
    <li>Consider a short delay to allow for cancellation</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF garage door is open
AND nobody is home (all phones away)
AND garage door has been open for 5+ minutes
AND no motion in garage for 2 minutes
THEN send notification "Closing garage in 2 minutes"
WAIT 2 minutes
THEN close garage door
THEN take camera snapshot
THEN send notification with photo "Garage closed"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Home mode changes to "Away" (last person left)</li>
      <li>OR garage door open for 5 minutes while nobody home</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Presence:</strong> All family members away from home<br>
    <strong>Garage status:</strong> Garage door is currently open<br>
    <strong>Motion:</strong> No motion detected in garage for 2+ minutes<br>
    <strong>Safety:</strong> No obstruction detected by door sensors
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Send warning notification: "Garage still open. Closing in 2 minutes."</li>
      <li>Wait 2 minutes (allows manual cancellation)</li>
      <li>Close garage door</li>
      <li>Wait 30 seconds for door to fully close</li>
      <li>Take snapshot from garage camera</li>
      <li>Send confirmation notification with photo</li>
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
        <span class="step-content">Zone.home person count = 0 for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">cover.garage_door is open AND no motion for 2 min</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Notify, delay, close cover, snapshot, notify with image</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use actionable notification with "Cancel" button during warning delay
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
        <span class="step-content">Everyone leaves (location mode: Away)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Garage door is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Notify, wait 2 min, close garage, send confirmation</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use Smart Home Monitor for additional security integration
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
        <span class="step-content">Mode changes to Away</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Garage door is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send notification, delay 2 min, close door</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine for complex logic with delays
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
        <span class="step-content">Last person leaves home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Garage door is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Close garage door, send notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use Shortcuts app for delays and photo capture
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
        <span class="step-content">Location: Everyone leaves</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Garage door sensor reports open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Wait 2 min, close garage, send notification</span>
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
        <span class="step-content">Everyone leaves home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Garage door is open (if supported)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Close garage via connected controller</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> May need Home Assistant or IFTTT for full automation
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Photo confirmation</h3>
    <p>Visual verification that garage is actually closed:</p>
    <ul>
      <li>Take snapshot after door closes</li>
      <li>Include timestamp on image</li>
      <li>Show "before and after" comparison</li>
      <li>Store images for security records</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Cancellation option</h3>
    <p>Allow manual override:</p>
    <ul>
      <li>Actionable notification with "Cancel" button</li>
      <li>2-minute delay before closing</li>
      <li>Voice command to cancel: "Don't close garage"</li>
      <li>Manual override if you're coming right back</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Context-aware behavior</h3>
    <p>Smarter decision making:</p>
    <ul>
      <li><strong>Quick trips:</strong> Wait longer if you just left (might return)</li>
      <li><strong>Work hours:</strong> Close immediately on weekday mornings</li>
      <li><strong>Weather:</strong> Close immediately if rain is starting</li>
      <li><strong>Time of day:</strong> Shorter delay at night for security</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Door closes when someone's in garage</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Presence detection missed someone still in the garage.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add motion sensor in garage as safety condition</li>
        <li>Require no motion for 5+ minutes before closing</li>
        <li>Add longer delay before auto-close (5-10 minutes)</li>
        <li>Use multiple presence detection methods</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>False "away" detection</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> System thinks everyone left when someone is still home.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use multiple presence methods (GPS + WiFi + Bluetooth)</li>
        <li>Increase geofence radius to reduce false departures</li>
        <li>Add delay before declaring "away" (5-10 minutes)</li>
        <li>Track all family members' phones</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Door won't close remotely</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Automation triggers but garage door doesn't close.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check safety sensors (photo-eyes) aren't blocked</li>
        <li>Verify smart controller is online and connected</li>
        <li>Test manual close from app first</li>
        <li>Check for obstruction in door path</li>
        <li>Verify garage door opener is powered on</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Photo notification not arriving</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Door closes but no photo confirmation received.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify camera is online and accessible</li>
        <li>Check notification permissions on phone</li>
        <li>Add delay between door close and snapshot (30 seconds)</li>
        <li>Verify camera snapshot service is configured correctly</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="best-practice-card">
  <h3>Setting up auto-close safely</h3>
  <ol>
    <li>Always verify garage door safety sensors work properly</li>
    <li>Add motion sensor in garage as backup safety check</li>
    <li>Include warning notification before closing</li>
    <li>Add 2+ minute delay for cancellation opportunity</li>
    <li>Send confirmation with photo after closing</li>
    <li>Test automation thoroughly before relying on it</li>
  </ol>
</div>

<div class="warning-card">
  <h3>Safety warnings</h3>
  <ul>
    <li><strong>Never bypass safety sensors</strong> - They prevent injury and damage</li>
    <li><strong>Add motion detection</strong> - Prevent closing on people or pets</li>
    <li><strong>Include delays</strong> - Allow time to cancel if needed</li>
    <li><strong>Test regularly</strong> - Ensure automation works when needed</li>
    <li><strong>Inform family</strong> - Everyone should know about auto-close feature</li>
  </ul>
</div>

---

**Related automations:**
- [Garage door notification](/automation/security/garage-door-notification/)
- [Away mode](/automation/daily-routines/away-mode/)
- [Doorbell notification](/automation/notifications/doorbell-notification/)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
