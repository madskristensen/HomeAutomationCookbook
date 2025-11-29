---
layout: default
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
    <ol>
      <li>Trigger: Garage door open for 10 minutes (use for: minutes: 10)</li>
      <li>Condition: Optional motion check</li>
      <li>Action: notify.mobile_app with actionable notification</li>
      <li>Include action to close door directly from notification</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <ol>
      <li>IF Garage door is open for 10 minutes</li>
      <li>THEN Send notification to all members</li>
      <li>Use Smart Home Monitor for additional alerts</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <ol>
      <li>Use Rule Machine with delayed trigger</li>
      <li>Trigger: Garage door open for 10 minutes</li>
      <li>Action: Send push notification</li>
      <li>Optional: Use HSM for security integration</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <ol>
      <li>Create automation: Garage door is open</li>
      <li>Add time condition if needed</li>
      <li>Action: Send notification</li>
      <li>Note: May need Home+ app for duration triggers</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa</h4>
    </div>
    <ol>
      <li>Routine: When garage door is open (if supported)</li>
      <li>Wait: 10 minutes</li>
      <li>Action: Send notification, announce on Echo</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <ol>
      <li>Limited native support for duration triggers</li>
      <li>Use third-party integration (Home Assistant, IFTTT)</li>
      <li>Can announce status on speakers</li>
    </ol>
  </div>
</div>

## Auto-close options

### Time-based auto-close

Automatically close after set time:

**Setup:**
- **Trigger:** Garage door open for 15 minutes
- **Condition:** No motion in garage for 5 minutes
- **Actions:**
  1. Send warning notification: "Closing garage door in 2 minutes"
  2. Wait 2 minutes
  3. Check if door still open (someone may have closed manually)
  4. Close garage door
  5. Send confirmation: "Garage door closed automatically"

### Departure auto-close

Close when leaving home:

- **Trigger:** Last person leaves home (geofence exit)
- **Condition:** Garage door is open
- **Actions:**
  1. Wait 2 minutes (allows time to return if forgot something)
  2. Close garage door
  3. Send notification: "Garage door closed - you left home"

### Bedtime auto-close

Part of night routine:

- **Trigger:** Home mode changes to "Night" OR time is 10:30 PM
- **Condition:** Garage door is open
- **Actions:**
  1. Send notification: "Closing garage door for the night"
  2. Close garage door

<div class="info-box">
  <strong>⚠️ Safety warning for auto-close</strong>
  <ul>
    <li>Ensure garage door has proper safety sensors (photo-eye)</li>
    <li>Never auto-close if people or vehicles might be moving through</li>
    <li>Always send warning notification before closing</li>
    <li>Consider adding a motion sensor for extra safety</li>
    <li>Test that safety reversal works properly</li>
  </ul>
</div>

## Advanced features

### Escalating notifications

Progressive alerts if door stays open:

1. **10 minutes:** Standard notification
2. **30 minutes:** Reminder notification with close option
3. **1 hour:** High priority alert
4. **2 hours:** Alert other family members

### Weather-aware closing

Close before bad weather:

- **Trigger:** Weather service reports rain starting within 30 minutes
- **Condition:** Garage door is open
- **Action:** Send notification: "Rain coming - consider closing garage door"

### Dashboard status tile

Always know garage status:

- Create sensor card showing current state
- Color coding: green (closed), red (open)
- Show time since opened if currently open
- Quick action button to close

### Voice announcements

Audio reminders throughout home:

- **Trigger:** Garage door open for 10 minutes
- **Action:** Announce on all speakers: "Just a reminder, the garage door is still open"

### Quiet hours exception

Different behavior at night:

- **Daytime (6 AM - 10 PM):** Notification only after 10 minutes
- **Nighttime (10 PM - 6 AM):** Immediate notification + auto-close after 5 minutes
- **Away mode:** Immediate notification + auto-close after 2 minutes

## Troubleshooting

### Issue: Sensor shows wrong state

**Causes:**
- Tilt sensor mounted incorrectly
- Contact sensor misaligned
- Sensor battery dead
- Wireless interference

**Solutions:**
✅ Verify sensor mounting - tilt sensors need proper angle
✅ Check magnet/sensor gap for contact sensors (< 1 inch)
✅ Replace battery
✅ Test sensor manually by opening/closing door
✅ Move sensor if wireless signal is weak

### Issue: Notifications not arriving

**Causes:**
- Phone notification permissions
- Automation disabled
- Network connectivity
- Do Not Disturb mode blocking

**Solutions:**
✅ Check notification permissions for smart home app
✅ Verify automation is enabled and error-free
✅ Test with manual trigger
✅ Add app to Do Not Disturb exceptions
✅ Check hub connectivity

### Issue: Auto-close not working

**Causes:**
- Smart controller offline
- Safety sensors blocked
- Opener not responding
- Automation condition not met

**Solutions:**
✅ Test manual close via app
✅ Check safety sensor alignment (usually at floor level)
✅ Verify controller is online and connected
✅ Check automation logs for condition failures
✅ Ensure opener is in "smart" mode if applicable

### Issue: Too many notifications

**Causes:**
- Delay too short
- Door briefly opened multiple times
- No cooldown between notifications

**Solutions:**
✅ Increase delay time (10-15 minutes)
✅ Add condition: only if door was closed within last hour
✅ Add notification cooldown (1 per hour max)
✅ Use escalating notifications instead of repeated same message

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
