---
layout: automation
title: Garage Door Left Open Notification - Smart Home Safety
description: Get alerted when your garage door is left open too long. Automatic notifications and optional auto-close for security and weather protection.
keywords: garage door notification, garage door left open, smart garage, garage door sensor, garage door automation, auto close garage, garage security
---

# Garage door left open notification

An open garage door is a security risk and can let in weather, pests, or unwanted visitors. This automation notifies you when the garage door has been open too long and optionally closes it automatically.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Security and safety</h4>
    <ul>
      <li><strong>Forgot to close</strong> - Get reminded after leaving</li>
      <li><strong>Kids left it open</strong> - Know when door is forgotten</li>
      <li><strong>Night security</strong> - Alert if open after bedtime</li>
      <li><strong>Away from home</strong> - Close remotely from anywhere</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Protection</h4>
    <ul>
      <li><strong>Weather protection</strong> - Close before rain or snow</li>
      <li><strong>Temperature control</strong> - Don't heat/cool the outdoors</li>
      <li><strong>Pest prevention</strong> - Keep animals out of garage</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Garage door sensor</strong>
      <div class="product-details">
        Options: Smart garage controller (Chamberlain myQ, Tailwind, Meross), tilt sensor, or contact sensor on door<br>
        Must report open/closed state to smart home platform
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart garage door controller</strong>
      <div class="product-details">
        Brands: Chamberlain myQ, Tailwind iQ3, Meross, Ratgdo<br>
        Enables remote open/close and status monitoring
      </div>
    </div>
    
    <div class="product-item">
      <strong>Camera</strong>
      <div class="product-details">
        Visual confirmation of garage status and contents
      </div>
    </div>
    
    <div class="product-item">
      <strong>Motion sensor</strong>
      <div class="product-details">
        Detect activity in garage for smarter auto-close timing
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Choosing a garage door sensor</strong>
  <ul>
    <li><strong>Smart controller:</strong> Best option - controls door AND reports status</li>
    <li><strong>Tilt sensor:</strong> Detects when door tilts (opens) - easy install</li>
    <li><strong>Contact sensor:</strong> Mount on door frame and door - reports open/closed</li>
    <li><strong>Existing opener:</strong> Some openers have built-in WiFi (check for myQ compatibility)</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF garage door open for 10 minutes
AND nobody is in garage (optional)
THEN send notification "Garage door still open"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation 1: Open too long notification</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Garage door state is "open" for 10 minutes</li>
    </ul>
    <h4>Conditions (optional)</h4>
    <ul>
      <li>No motion detected in garage for 5 minutes</li>
      <li>Home mode is not "Away" (separate automation for away)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Garage door has been open for 10 minutes"</li>
      <li>Include action button to close door remotely</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Automation 2: Open at night alert</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 10:00 PM (or bedtime)</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Garage door is open</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send high-priority notification: "Garage door still open at bedtime!"</li>
      <li>Optional: Auto-close after 2 minute warning</li>
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
        <span class="step-content">Garage door open for 10 minutes (use for: minutes: 10)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Optional motion check</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">notify.mobile_app with actionable notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Include action to close door directly from notification
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
        <span class="step-content">Garage door is open for 10 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Send notification to all members</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use Smart Home Monitor for additional alerts
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
        <span class="step-content">Garage door open for 10 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send push notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with delayed trigger
          <br>
          <strong>Optional:</strong> Use HSM for security integration
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
        <span class="step-content">Garage door is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Add time condition if needed</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> May need Home+ app for duration triggers
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
        <span class="step-label">When</span>
        <span class="step-content">Garage door is open (if supported)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Wait</span>
        <span class="step-content">10 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send notification, announce on Echo</span>
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
        <span class="step-label">Limitation</span>
        <span class="step-content">Limited native support for duration triggers</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Workaround</span>
        <span class="step-content">Use Home Assistant or IFTTT integration</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Can announce status on speakers
        </div>
      </div>
    </div>
  </div>
</div>

## Auto-close options

<div class="feature-grid">
  <div class="feature-card">
    <h3>Time-based auto-close</h3>
    <p>Automatically close after set time:</p>
    <ul>
      <li><strong>Trigger:</strong> Door open for 15 minutes</li>
      <li><strong>Condition:</strong> No motion in garage for 5 minutes</li>
      <li><strong>Actions:</strong> Send warning, wait 2 min, close door, confirm</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Departure auto-close</h3>
    <p>Close when leaving home:</p>
    <ul>
      <li><strong>Trigger:</strong> Last person leaves home (geofence)</li>
      <li><strong>Condition:</strong> Garage door is open</li>
      <li><strong>Actions:</strong> Wait 2 min, close door, send notification</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Bedtime auto-close</h3>
    <p>Part of night routine:</p>
    <ul>
      <li><strong>Trigger:</strong> Night mode OR time is 10:30 PM</li>
      <li><strong>Condition:</strong> Garage door is open</li>
      <li><strong>Actions:</strong> Send notification, close door</li>
    </ul>
  </div>
</div>

<div class="warning-card">
  <h3>Safety warning for auto-close</h3>
  <ul>
    <li>Ensure garage door has proper safety sensors (photo-eye)</li>
    <li>Never auto-close if people or vehicles might be moving through</li>
    <li>Always send warning notification before closing</li>
    <li>Consider adding a motion sensor for extra safety</li>
  </ul>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Escalating notifications</h3>
    <p>Progressive alerts if door stays open:</p>
    <ul>
      <li><strong>10 minutes:</strong> Standard notification</li>
      <li><strong>30 minutes:</strong> Reminder with close option</li>
      <li><strong>1 hour:</strong> High priority alert</li>
      <li><strong>2 hours:</strong> Alert other family members</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Weather-aware closing</h3>
    <p>Close before bad weather:</p>
    <ul>
      <li><strong>Trigger:</strong> Rain starting within 30 minutes</li>
      <li><strong>Condition:</strong> Garage door is open</li>
      <li><strong>Action:</strong> Send notification to consider closing</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Dashboard status tile</h3>
    <p>Always know garage status:</p>
    <ul>
      <li>Color coding: green (closed), red (open)</li>
      <li>Show time since opened if currently open</li>
      <li>Quick action button to close</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Voice announcements</h3>
    <p>Audio reminders throughout home:</p>
    <ul>
      <li><strong>Trigger:</strong> Door open for 10 minutes</li>
      <li><strong>Action:</strong> Announce on all speakers</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Quiet hours exception</h3>
    <p>Different behavior at night:</p>
    <ul>
      <li><strong>Daytime:</strong> Notification only after 10 min</li>
      <li><strong>Nighttime:</strong> Immediate + auto-close after 5 min</li>
      <li><strong>Away mode:</strong> Immediate + auto-close after 2 min</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Sensor shows wrong state</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Tilt sensor mounted incorrectly or contact sensor misaligned.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify sensor mounting - tilt sensors need proper angle</li>
        <li>Check magnet/sensor gap for contact sensors (< 1 inch)</li>
        <li>Replace battery</li>
        <li>Test sensor manually by opening/closing door</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Notifications not arriving</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Phone notification permissions or automation disabled.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check notification permissions for smart home app</li>
        <li>Verify automation is enabled and error-free</li>
        <li>Test with manual trigger</li>
        <li>Add app to Do Not Disturb exceptions</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Auto-close not working</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Smart controller offline or safety sensors blocked.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Test manual close via app</li>
        <li>Check safety sensor alignment (floor level)</li>
        <li>Verify controller is online and connected</li>
        <li>Check automation logs for condition failures</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Too many notifications</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Delay too short or no cooldown between notifications.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Increase delay time (10-15 minutes)</li>
        <li>Add condition: only if door was closed within last hour</li>
        <li>Add notification cooldown (1 per hour max)</li>
        <li>Use escalating notifications instead of repeated same message</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

### Finding the right delay time

**Consider your habits:**
- Loading/unloading car: 5-10 minutes typical
- Doing garage work: 30+ minutes
- Quick grab from garage: 1-2 minutes

**Recommended settings:**
- **Standard alert:** 10-15 minutes
- **Auto-close:** 20-30 minutes minimum
- **Night mode:** 5 minutes
- **Away mode:** 2-5 minutes

### Safety first

**Always verify:**
- Safety sensors working properly
- Warning before auto-close
- Manual override accessible
- Family aware of automation

**Never auto-close without:**
- Motion sensor verification OR
- Significant delay (15+ minutes) OR
- Warning notification first

### Multiple garage doors

Create separate automations per door:

- Different notification sounds or messages
- Different timing based on use (main vs. rarely used)
- Separate status tiles on dashboard

---

**Related automations:**
- [Away mode automation](/automation/daily-routines/away-mode/)
- [Bedtime routine](/automation/daily-routines/bedtime-routine/)
- [Doorbell notification](/automation/notifications/doorbell-notification.html)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
