---
layout: default
title: Package Delivery Detection - Smart Home Notification
description: Get notified when packages are delivered to your door without needing a smart doorbell. Use motion sensors and cameras for reliable delivery alerts.
keywords: package delivery notification, delivery alert, porch package detection, smart home delivery, motion sensor package, front door delivery notification
---

# Package delivery detection

Know when packages arrive at your door even without a smart doorbell. This automation uses motion sensors and optional cameras to detect deliveries and send you instant notifications, helping prevent package theft and letting you retrieve deliveries promptly.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Security and awareness</h4>
    <ul>
      <li><strong>Prevent theft</strong> - Retrieve packages quickly before porch pirates strike</li>
      <li><strong>Working from home</strong> - Know when to grab packages without watching the door</li>
      <li><strong>Away from home</strong> - Get notified to arrange pickup or ask neighbor to collect</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Convenience</h4>
    <ul>
      <li><strong>Expecting important delivery</strong> - Immediate notification for time-sensitive packages</li>
      <li><strong>Multiple deliveries</strong> - Track when each carrier arrives</li>
      <li><strong>Apartment living</strong> - Know when lobby deliveries arrive</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Outdoor motion sensor</strong>
      <div class="product-details">
        Popular brands: Philips Hue Outdoor, Aqara (with weatherproof case), Ring Motion Sensor<br>
        Requirements: Weatherproof (IP65+), reliable detection range for porch area
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Outdoor camera</strong>
      <div class="product-details">
        Brands: Wyze, Ring, Arlo, Eufy, Reolink<br>
        Capture snapshot with notification for visual confirmation
      </div>
    </div>
    
    <div class="product-item">
      <strong>Pressure mat or step sensor</strong>
      <div class="product-details">
        Place under doormat for more precise detection<br>
        Only triggers when someone steps on porch
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart lock</strong>
      <div class="product-details">
        Know if door was opened (you) vs. just motion (delivery person)
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Motion sensor vs. smart doorbell</strong>
  <ul>
    <li><strong>Motion sensor approach:</strong> Works for deliveries that don't ring doorbell (most carriers)</li>
    <li><strong>Lower cost:</strong> Motion sensor typically cheaper than smart doorbell</li>
    <li><strong>Privacy:</strong> No camera required if you prefer minimal surveillance</li>
    <li><strong>Complement doorbell:</strong> Use both for complete coverage</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF motion detected on porch
AND front door not opened in last 30 seconds
AND time is during delivery hours (8 AM - 8 PM)
THEN send notification "Possible package delivery"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Motion detected on porch/front door sensor</li>
      <li>OR Camera detects person (if using AI detection)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>Front door was not opened in last 30-60 seconds (not you coming/going)</li>
      <li>Time is between 8 AM and 8 PM (typical delivery hours)</li>
      <li>Optional: Doorbell was not pressed (delivery person didn't ring)</li>
      <li>Optional: Smart lock was not used recently</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Motion at front door - possible delivery"</li>
      <li>Optional: Attach camera snapshot</li>
      <li>Optional: Start recording on porch camera</li>
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
        <span class="step-content">Porch motion sensor changes to "on"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door not opened in last 60 sec + time 8am-8pm</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">notify.mobile_app with camera snapshot attachment</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use template to check door last changed time
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
        <span class="step-content">Motion detected AND Time 8am-8pm</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Front door closed (was not recently opened)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Send push notification</span>
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
        <span class="step-content">Door inactive 60+ sec + time restriction</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send push notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine for complex time conditions
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
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 8 AM and 8 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Send notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Limited ability to check door state in native automations
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
        <span class="step-content">Motion sensor detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 8 AM and 8 PM</span>
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
        <span class="step-label">When</span>
        <span class="step-content">Motion detected by compatible sensor</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time restriction 8 AM - 8 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send notification or announce</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Camera snapshot with notification</h3>
    <p>Visual confirmation of who's at the door:</p>
    <ul>
      <li>Capture snapshot when motion triggers</li>
      <li>Attach image to push notification</li>
      <li>See if it's delivery person, neighbor, or solicitor</li>
      <li>Provides evidence if package is stolen</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>AI person detection</h3>
    <p>Reduce false alerts from animals and cars:</p>
    <ul>
      <li>Use camera AI to detect human presence</li>
      <li>Filter out pets, leaves, shadows</li>
      <li>More accurate than basic motion sensing</li>
      <li>Available on: Frigate, Wyze, Ring, Google Nest</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Delivery service integration</h3>
    <p>Combine with carrier tracking:</p>
    <ul>
      <li>Enable notifications only on expected delivery days</li>
      <li>Match motion alert with tracking "delivered" status</li>
      <li>Use Informed Delivery, UPS My Choice, FedEx Delivery Manager</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Repeated motion detection</h3>
    <p>Distinguish delivery from passersby:</p>
    <ul>
      <li><strong>Single brief motion:</strong> Someone walking by - lower priority</li>
      <li><strong>Motion, pause, motion:</strong> Likely package drop-off - higher priority</li>
      <li>Delivery pattern: approach, stop, leave</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Package area monitoring</h3>
    <p>Continue monitoring after delivery:</p>
    <ul>
      <li>If motion detected after initial delivery alert</li>
      <li>Could be another delivery or theft attempt</li>
      <li>Higher alert priority: "Motion near package"</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Too many false alerts</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Motion sensor triggers from cars, animals, wind-blown items.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Adjust sensor sensitivity</li>
        <li>Reposition to focus on porch area only</li>
        <li>Use camera with AI person detection</li>
        <li>Add pet-immune motion sensor</li>
        <li>Use narrower detection zone</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Missing deliveries</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sensor not detecting delivery person.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check sensor coverage area</li>
        <li>Test sensor with walk-through</li>
        <li>Verify sensor battery/connectivity</li>
        <li>Add second sensor for better coverage</li>
        <li>Check for obstructions in detection zone</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Alerts when I come home</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Getting alerted by your own motion when arriving/departing.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add condition: door not opened recently</li>
        <li>Add condition: smart lock not used</li>
        <li>Use presence detection to suppress when arriving</li>
        <li>Exclude alerts when garage door opens</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Late night false alarms</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Motion from animals or passersby at odd hours.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Restrict to delivery hours (8 AM - 8 PM)</li>
        <li>Use different notification for after-hours (security focus)</li>
        <li>Reduce sensitivity at night</li>
        <li>Only alert if motion persists for several seconds</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

### Sensor placement

**Optimal positions:**
- Under porch roof (protected from weather)
- Aimed at typical package drop zone
- Avoiding direct sunlight (causes false triggers)
- 6-8 feet high for best coverage

**Coverage area:**
- Focus on delivery zone, not sidewalk
- Include path delivery person takes
- Minimize detection of street traffic

### Notification management

**Keep alerts useful:**
- Include location: "Front porch motion"
- Attach camera snapshot when available
- Different sound for delivery vs. security alerts

**Reduce notification fatigue:**
- Restrict to delivery hours
- Add cooldown (ignore repeat triggers within 5 minutes)
- Use different notification levels based on confidence

### Privacy considerations

**If using camera:**
- Position to capture porch, not public sidewalk
- Check local laws on recording public areas
- Consider camera with local storage vs. cloud
- Notify visitors (signs or announcements)

---

**Related automations:**
- [Doorbell notification](/automation/notifications/doorbell-notification.html)
- [Away mode automation](/automation/daily-routines/away-mode.html)
- [Motion detection lights](/automation/lighting/lights-on-motion.html)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
