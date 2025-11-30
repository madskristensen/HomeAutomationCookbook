---
layout: automation
title: Start Robot Vacuum When Everyone Leaves
description: Automatically start your robot vacuum when the house is empty. Clean while away without lifting a finger.
keywords: robot vacuum automation, auto start vacuum, vacuum when away, automatic vacuum cleaning, smart vacuum, presence detection vacuum, away mode cleaning
---

# Start the robot vacuum when everybody leaves

Robot vacuums are great, but even better when they clean while you're away. Automate daily cleaning to happen when no one is home to disturb or be disturbed.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Automated Cleaning</h4>
    <ul>
      <li><strong>Clean During Work Hours</strong> - House cleaned while away at work</li>
      <li><strong>No Disturbance</strong> - No one home to be bothered by vacuum noise</li>
      <li><strong>Daily Cleaning</strong> - Automatic consistent cleaning schedule</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Convenience</h4>
    <ul>
      <li><strong>Pet Hair Management</strong> - Keep up with pet shedding automatically</li>
      <li><strong>Guest Ready</strong> - House always clean when you return</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>WiFi-Enabled Robot Vacuum</strong>
      <div class="product-details">
        Popular brands: Roomba, Roborock, Eufy, Shark, Neato<br>
        WiFi connectivity • App control • Scheduling override
      </div>
    </div>
    
    <div class="product-item">
      <strong>Presence Detection</strong>
      <div class="product-details">
        Phone app location services, GPS-based (Home Assistant, SmartThings, Life360)<br>
        OR door lock status + motion sensors
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Contact Sensors</strong>
      <div class="product-details">
        On doors to ensure all closed before starting
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Notifications</strong>
      <div class="product-details">
        Alert if vacuum gets stuck or has errors
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF everyone leaves home
AND time between 9:00 AM - 5:00 PM
THEN start robot vacuum</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Home goes into Away Mode</li>
      <li>(Last person leaves house based on presence detection)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Time is between 9 AM - 6 PM:</strong> Vacuum during daytime only<br>
    <strong>House in Away Mode for 15 min:</strong> Ensure everyone actually left<br>
    <strong>Optional:</strong> Day of week (e.g., only weekdays)
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Start robot vacuum cleaning cycle</li>
      <li>OR trigger vacuum's existing schedule</li>
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
        <span class="step-content">Home mode 'Away' for 15 min</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time 9am-6pm, weekdays, vacuum docked</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Start robot vacuum cleaning cycle</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Stop:</strong> When home → Send vacuum to dock
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
        <span class="step-content">Home mode "Away" for 15 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Time 9 AM - 6 PM, Mon-Fri</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Start robot vacuum</span>
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
        <span class="step-content">Mode changes to "Away" for 15 min</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time 9am-6pm, weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Start vacuum cleaning cycle</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Mode Manager with vacuum integration
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
        <span class="step-content">Time 9 AM - 6 PM, Weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Start vacuum (if HomeKit supported)</span>
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
        <span class="step-content">Last person leaves (location)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time 9 AM - 6 PM, Weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Start vacuum</span>
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
        <span class="step-content">Last person leaves home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time 9 AM - 6 PM, weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Start robot vacuum</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

### Room-by-room daily schedule

Different rooms on different days:

Create automation that triggers when away for 15 minutes during daytime (9am-6pm), then uses day-based logic:
- **Monday:** Clean kitchen & dining room (segment IDs 1, 2)
- **Tuesday:** Clean living room (segment 3)
- **Wednesday:** Clean bedrooms (segments 4, 5)
- **Thursday:** Clean hallways (segment 6)
- **Friday:** Full house cleaning (all rooms)

*Note: Requires vacuum model supporting room-specific cleaning commands*

### Pre-cleaning notification

Remind to tidy up before vacuum starts:

Create automation with these elements:
- **Trigger:** Home mode changes to 'Away' for 5 minutes
- **Condition:** Time between 9am-6pm
- **Action:** Send notification "Vacuum will start in 10 minutes. Tidy floors if needed!"

### Stuck vacuum alert

Get notified if vacuum has problems:

Create automation with these elements:
- **Trigger:** Vacuum state changes to 'error'
- **Action:** Send high-priority notification "Robot vacuum is stuck or has an error!"

### Battery-based smart start

Only start if battery sufficient:

Add condition to automation: Vacuum battery level must be above 50% before starting cleaning cycle.

## Safety considerations

### Pre-checks before starting

Ensure conditions are safe:

Add conditions to automation:
- All doors closed (prevent vacuum getting stuck in closets - check bedroom closet door, utility room door)
- No maintenance needed (vacuum is docked AND bin is not full)

### Stop conditions

Automatically stop vacuum if:

Create automation with these elements:
- **Trigger:** Any person arrives home (group.all_persons changes to 'home')
- **Condition:** Vacuum is currently cleaning
- **Action:** Send vacuum to dock (return to base)

## Troubleshooting

### Issue: Vacuum starts when someone is still home

**Causes:**
- Presence detection too fast/inaccurate
- Phone GPS delay
- One person left but others home
- Away mode triggered prematurely

**Solutions:**
✅ Increase away delay to 20-30 minutes
✅ Use "all persons away" not "any person away"
✅ Combine presence with door lock status
✅ Add motion sensor check - no motion for 15+ minutes
✅ Use more reliable presence detection (Life360, multiple methods)

Add multiple detection methods to conditions:
- All persons away for 15+ minutes
- AND no motion detected for 15+ minutes
- AND front door locked

### Issue: Vacuum gets stuck

**Causes:**
- Doors left open (closets, bathrooms)
- Obstacles not cleared (shoes, toys, cables)
- Low battery starting cycle
- Virtual barriers not set

**Solutions:**
✅ Add notification before start: "Tidy floors in 10 minutes"
✅ Check battery level before starting (>50%)
✅ Set virtual barriers in vacuum app
✅ Add door sensors - only start if problem doors closed
✅ Implement stuck detection and notification (shown above)

### Issue: Vacuum doesn't start

**Causes:**
- Vacuum already running or has error
- Battery too low
- Maintenance needed (bin full, filter)
- Integration not working

**Check:**
- ✅ Verify vacuum shows as "docked" before automation triggers
- ✅ Check vacuum battery level
- ✅ Empty bin and clean filter
- ✅ Test manual start via app
- ✅ Review automation logs
- ✅ Check vacuum WiFi connection

Add diagnostics to automation:
- If vacuum is docked, start cleaning
- Otherwise, send notification with current vacuum state and battery level

---

**Related automations:**
- [Away mode automation](/automation/daily-routines/away-mode/)
- [Morning routine automation](/automation/daily-routines/morning-routine/)
- [Washer done notification](/automation/appliances/washer-done-notification/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliance Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
