---
layout: default
title: Dishwasher Done Notification - Temperature Method
description: Get notified when dishwasher finishes using temperature detection from drying cycle. Alternative method to power monitoring.
keywords: dishwasher done alert, temperature sensor dishwasher, completion notification, dishwasher automation, drying cycle detection, appliance monitoring
---

# Notify me when the dishwasher is done

Get alerted when dishes are clean and ready to be put away. This clever temperature-based method detects the heat from the drying cycle.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Efficiency</h4>
    <ul>
      <li><strong>Prompt Dish Removal</strong> - Empty dishwasher right when cycle ends</li>
      <li><strong>Kitchen Cleanup</strong> - Know when you can run another load</li>
      <li><strong>Track Dish Status</strong> - Dashboard showing clean/dirty</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Convenience</h4>
    <ul>
      <li><strong>Prevent Dishes Sitting</strong> - Don't let clean dishes sit too long</li>
      <li><strong>Multi-Tasking</strong> - Get alerted while doing other things</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment - Option 1: Temperature Sensor (Clever!)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Multi-Purpose Sensor or Temperature Sensor</strong>
      <div class="product-details">
        Popular brands: Aeotec, SmartThings, Zigbee multi-sensors<br>
        Temperature detection • Contact/tilt sensor • Mount on side or top of dishwasher door<br>
        <em>Detects heat from drying cycle - very clever and reliable!</em>
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Essential Equipment - Option 2: Power Monitoring (Traditional)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Power Metering Smart Plug</strong>
      <div class="product-details">
        15A rated minimum • Plug dishwasher into smart plug<br>
        Use same technique as washer automation
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Dashboard Tile</strong>
      <div class="product-details">
        Showing clean/dirty status
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Light</strong>
      <div class="product-details">
        In kitchen for visual alert
      </div>
    </div>
    
    <div class="product-item">
      <strong>Voice Announcement</strong>
      <div class="product-details">
        Via smart speaker when dishes are clean
      </div>
    </div>
  </div>
</div>

## Automation setup - Temperature method

<div class="automation-example">IF temperature > 90°F
AND door closed for 60 minutes
AND dishwasher running
THEN send notification "Dishwasher done!"
AND set dishwasher_clean to true</div>

<div class="info-box">
  <strong>💡 Sensor Placement & Temperature Patterns</strong>
  <ul>
    <li><strong>Mounting:</strong> On side or top of dishwasher door. Position to detect heat from drying cycle vent. May require experimentation to find best spot (usually near top of door or side vent).</li>
    <li><strong>Contact Sensor:</strong> Register as "tilt sensor" or "garage door sensor" so it only triggers "open" when door is fully horizontal (open), not just cracked.</li>
    <li><strong>Temperature Pattern:</strong> Normal: 68-75°F (room temp) • Drying cycle: 90-120°F • After cycle: Gradually cools over 30-60 minutes</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation: Detect Dishwasher Done</h4>
    
    <h4>Triggers</h4>
    <ul>
      <li>Temperature rises above 90°F (32°C)</li>
    </ul>
    
    <h4>Conditions</h4>
    <ul>
      <li>Contact/tilt sensor has been closed for 60 minutes (ensures it's the drying cycle, not just running/wash cycle)</li>
      <li>Dishwasher in use (based on time of day or manual indicator)</li>
    </ul>
    
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Dishwasher is done!"</li>
      <li>Turn on dashboard tile showing "clean"</li>
      <li>Optional: Flash kitchen light</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Auto-Reset: Door Opens</h4>
    
    <h4>Triggers</h4>
    <ul>
      <li>Contact/tilt sensor opens (door opened)</li>
    </ul>
    
    <h4>Actions</h4>
    <ul>
      <li>Turn off dashboard tile</li>
      <li>Reset variable</li>
      <li>Assumes dishwasher emptied when door opened</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Create two boolean helpers: "dishwasher_running" and "dishwasher_clean"</li>
      <li>Start: Door closes → Turn on "dishwasher_running"</li>
      <li>Done: Temp > 90°F AND door closed 60min AND running</li>
      <li>Actions: Notify, Turn off running, Turn on clean</li>
      <li>Reset: Door opens → Turn off both booleans</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Routine 1: Temp > 90°F AND door closed 60+ min</li>
      <li>Actions: Notify, Turn on virtual switch "Dishwasher Clean"</li>
      <li>Routine 2: Door opens → Turn off virtual switch</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Rule Machine with temperature sensor</li>
      <li>Start: Door closes → Set "running" variable</li>
      <li>Done: Temp > 90°F AND door closed 60min → Notify</li>
      <li>Reset: Door opens → Clear variables</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Temperature sensor above 90°F</li>
      <li>Conditions: Contact sensor closed for 60+ minutes</li>
      <li>Do: Send notification</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: Temperature sensor value above 90°F</li>
      <li>Condition: Contact sensor closed</li>
      <li>Actions: Send notification, Alexa announces "dishwasher is done"</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Limited native support for temperature triggers</li>
      <li>Use Home Assistant or IFTTT for logic</li>
    </ol>
  </div>
</div>

## Power monitoring method

If temperature method doesn't work, use power monitoring:

**Setup:**
1. Plug dishwasher into power monitoring smart plug
2. Monitor power consumption during full cycle
3. Note idle (<10W), running (500-1500W), and done (<10W) levels

**Automation:**
- Start detection: Power above 100W
- Done detection: Power below 20W for 5 minutes after running

See [Washer Done Notification](/automation/appliances/washer-done-notification/) for detailed power monitoring setup.

## Advanced features

### Clean/dirty dashboard

Visual indicator on dashboard:

Create template sensor that displays:
- **"Clean - Ready to Empty"** with alert icon (when dishwasher_clean is on)
- **"Running"** with running icon (when dishwasher_running is on)
- **"Dirty - Ready for Dishes"** with off icon (when both are off)

### Manual status control

Add buttons to manually set clean/dirty:

Create two scripts:
1. **Mark Dishwasher Dirty:** Turn off both dishwasher_clean and dishwasher_running booleans
2. **Mark Dishwasher Clean:** Turn on dishwasher_clean, turn off dishwasher_running

## Troubleshooting

### Issue: Temperature never rises enough

**Causes:**
- Sensor not positioned near heat vent
- Dishwasher doesn't have heated dry
- Sensor too far from heat source
- Threshold too high

**Solutions:**
✅ Reposition sensor closer to drying vent/exhaust
✅ Lower temperature threshold (try 85°F instead of 90°F)
✅ Check if dishwasher has heated dry option enabled
✅ Test with thermometer to find hottest spot on door
✅ Use power monitoring method instead

### Issue: False notifications

**Causes:**
- Temperature rises from nearby heat source (oven, sun)
- Door opened mid-cycle
- Minimum closed time too short

**Check:**
- ✅ Increase required door closed time (90 minutes instead of 60)
- ✅ Position sensor away from other heat sources
- ✅ Add time-based condition (only during typical dishwasher hours)
- ✅ Combine with other detection methods

**Fix:**

Add conditions to automation:
- Only trigger during typical dishwasher hours (after meals: 7-9am or 7-11pm)
- Require door closed for 90 minutes instead of 60

### Issue: No notification when done

**Causes:**
- Sensor battery dead
- Sensor fell off dishwasher
- Door opened before drying cycle started
- Temperature threshold never reached

**Solutions:**
✅ Check sensor battery level
✅ Verify sensor still attached securely
✅ Monitor temperature during actual cycle
✅ Adjust threshold based on actual readings
✅ Switch to power monitoring method if temperature unreliable

---

**Related automations:**
- [Washer done notification](/automation/appliances/washer-done-notification/)
- [Dryer done notification](/automation/appliances/dryer-done-notification/)
- [Morning routine automation](/automation/presence/morning-routine/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliance Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
