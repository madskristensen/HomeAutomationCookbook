---
layout: automation
title: Stove or Oven Left On Alert - Smart Home Safety
description: Get notified when your stove or oven is left on too long. Prevent fire hazards and improve safety with cooking appliance monitoring.
keywords: stove left on alert, oven notification, cooking safety, smart stove monitoring, kitchen fire prevention, appliance safety automation
---

# Stove or oven left on alert

The burner left glowing after dinner, the oven forgotten once the casserole came out - small oversights that can become dangerous ones. A power monitor watches the kitchen, noting when the stove has been running longer than it should. A quiet alert arrives, interrupting your evening show or reaching you across town, before worry turns to hazard.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Safety and prevention</h4>
    <ul>
      <li><strong>Fire prevention</strong> - Catch forgotten burners before they become hazards</li>
      <li><strong>Elderly care</strong> - Help aging parents stay safe while cooking</li>
      <li><strong>Busy households</strong> - Catch distractions that lead to forgotten appliances</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Awareness</h4>
    <ul>
      <li><strong>Left home with stove on</strong> - Get alerted after leaving</li>
      <li><strong>Long cooking times</strong> - Reminder for slow-cooked items</li>
      <li><strong>Kids home alone</strong> - Know if appliances are being used</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment (choose one method)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Method 1: Smart plug with power monitoring</strong>
      <div class="product-details">
        Brands: TP-Link Kasa, Emporia, Zooz, Shelly<br>
        Works for: Electric stoves/ovens plugged into outlet<br>
        Detects power draw indicating appliance is on
      </div>
    </div>
    
    <div class="product-item">
      <strong>Method 2: Stove guard sensor</strong>
      <div class="product-details">
        Brands: iGuardStove, FireAvert, Wallflower<br>
        Purpose-built stove monitoring devices<br>
        Some can actually shut off power automatically
      </div>
    </div>
    
    <div class="product-item">
      <strong>Method 3: Temperature sensor on stovetop</strong>
      <div class="product-details">
        Brands: Aqara, SmartThings Multipurpose<br>
        Detects elevated temperature when burners are on<br>
        Works for gas and electric stoves
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Motion sensor in kitchen</strong>
      <div class="product-details">
        Differentiate between cooking and forgotten stove
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart speaker</strong>
      <div class="product-details">
        Announce alerts audibly in the home
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart smoke detector</strong>
      <div class="product-details">
        Nest Protect, First Alert Onelink<br>
        Complementary fire safety
      </div>
    </div>
  </div>
</div>

<div class="warning-card">
  <h3>Important safety notes</h3>
  <ul>
    <li><strong>Don't plug gas appliances into smart plugs</strong> - Cutting power won't stop gas flow</li>
    <li><strong>Check plug rating</strong> - Ovens draw high current; ensure plug is rated for load</li>
    <li><strong>Hard-wired appliances</strong> - Need electrician to install monitoring solutions</li>
    <li><strong>This is a supplement</strong> - Not a replacement for smoke detectors and fire safety</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF stove/oven power draw > 100W for 30 minutes
AND no motion in kitchen for 15 minutes
THEN send notification "Stove may be left on unattended"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation 1: Long cooking alert</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Stove power consumption above 100W for 60 minutes</li>
      <li>OR Temperature sensor above 100°F for 60 minutes</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Optional: No motion in kitchen for 15 minutes</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Stove has been on for 1 hour"</li>
      <li>Optional: Announce on kitchen speaker</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Automation 2: Left home with stove on</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Everyone leaves home (away mode activates)</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Stove power consumption above 100W</li>
      <li>OR Stove temperature elevated</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send high-priority notification: "WARNING: Stove is still on and nobody is home!"</li>
      <li>Optional: Turn off smart plug if electric stove</li>
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
        <span class="step-content">Power sensor > 100W for 60 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Kitchen motion inactive 15+ minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">notify.mobile_app + tts.speak on kitchen speaker</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Create separate critical automation for "away + stove on"
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
        <span class="step-content">Power meter > 100W for 60 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">No motion in kitchen for 15 minutes</span>
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
        <span class="step-content">Power meter reports > 100W for 60 min</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Kitchen motion inactive</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send push notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with power trigger capabilities
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
        <span class="step-label">Limitation</span>
        <span class="step-content">Limited power monitoring support natively</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Workaround</span>
        <span class="step-content">Use Eve Energy plug with Eve app automations</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Alternative:</strong> Use temperature sensor as trigger
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
        <span class="step-label">Limitation</span>
        <span class="step-content">No native power level triggers</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Workaround</span>
        <span class="step-content">Use with smart plug that has own app + IFTTT</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Announce on Echo devices</span>
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
        <span class="step-content">Limited power monitoring automation</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Workaround</span>
        <span class="step-content">Use Home Assistant or third-party integration</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Can announce on Nest speakers via integration
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Tiered alerts based on duration</h3>
    <p>Escalating notifications for extended cooking:</p>
    <ul>
      <li><strong>60 minutes:</strong> "Stove has been on for 1 hour"</li>
      <li><strong>90 minutes:</strong> "Stove still on - is everything OK?"</li>
      <li><strong>120 minutes:</strong> High priority: "Stove on for 2 hours!"</li>
      <li><strong>180 minutes:</strong> Critical: Alert all family members</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Motion-aware alerting</h3>
    <p>Only alert when stove appears unattended:</p>
    <ul>
      <li>Track kitchen motion sensor activity</li>
      <li>If motion detected, assume cooking is active</li>
      <li>Alert only when no motion for 15+ minutes</li>
      <li>Reduces false alarms during active cooking</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Auto-shutoff for electric appliances</h3>
    <p>Automatically cut power in dangerous situations:</p>
    <ul>
      <li>Only for electric stoves plugged into smart plug</li>
      <li>Trigger: Away mode + stove on for 10 minutes</li>
      <li>Send confirmation notification</li>
      <li><strong>Caution:</strong> May require re-igniting oven after restoration</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Bedtime stove check</h3>
    <p>Part of bedtime routine:</p>
    <ul>
      <li>Trigger: Bedtime mode activates OR time is 10 PM</li>
      <li>Condition: Stove power above threshold</li>
      <li>Action: "Stove is still on at bedtime!"</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Guest cooking notification</h3>
    <p>Know when guests use the kitchen:</p>
    <ul>
      <li>Trigger: Stove turns on while in vacation mode</li>
      <li>Action: Alert homeowner</li>
      <li>Useful for Airbnb hosts or house sitters</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Alerts during normal cooking</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Getting alerts while actively cooking long recipes.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Increase time threshold (90 minutes instead of 60)</li>
        <li>Add motion sensor condition - only alert if unattended</li>
        <li>Add snooze option: "I'm cooking - remind me in 2 hours"</li>
        <li>Create "slow cooking" mode that extends thresholds</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Power monitoring not accurate</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Smart plug reports inconsistent power readings.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check smart plug current rating vs. appliance draw</li>
        <li>Calibrate threshold by testing when stove is on vs. off</li>
        <li>Use average power over 5 minutes instead of instant</li>
        <li>Try different smart plug with better power monitoring</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Gas stove monitoring challenges</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Can't use power monitoring for gas appliances.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use temperature sensor near burners</li>
        <li>Use dedicated stove guard device (iGuardStove)</li>
        <li>Monitor gas flow if gas company offers smart meter</li>
        <li>Motion sensor + time-based heuristics</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Hard-wired appliance</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Stove is hard-wired, can't use smart plug.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use temperature sensor method</li>
        <li>Install dedicated stove guard device</li>
        <li>Consider CT clamp on circuit (requires electrician)</li>
        <li>Use whole-home energy monitor (Sense, Emporia Vue)</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

### Setting appropriate thresholds

**Time thresholds:**
- **Standard alert:** 60-90 minutes (catches forgotten appliances)
- **Slow cooking:** 3-4 hours (for roasts, slow braises)
- **Oven preheating:** Ignore first 15 minutes

**Power thresholds:**
- **Electric burner on:** Usually 500W-2000W per burner
- **Electric oven on:** Usually 1500W-5000W
- **Standby/clock only:** Under 10W
- **Set threshold at:** 100W (catches any active heating element)

### Combining with motion detection

**Reduce false alerts:**
- Only alert if no kitchen motion for 15+ minutes
- Reset timer if motion detected
- Assume active cooking while motion present

**Motion placement:**
- Position to see cooking area
- Avoid triggering from nearby rooms
- Consider multiple sensors for large kitchens

### Safety integration

**Complement with:**
- Smoke detectors (smart preferably)
- Carbon monoxide detectors
- Fire extinguisher in accessible location
- Emergency auto-shutoff for electric appliances

---

**Related automations:**
- [Fire safety response](/automation/security/fire-safety.html)
- [Away mode automation](/automation/daily-routines/away-mode.html)
- [Bedtime routine](/automation/daily-routines/bedtime-routine.html)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
