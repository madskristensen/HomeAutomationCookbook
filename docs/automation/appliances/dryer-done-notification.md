---
layout: default
title: Dryer Done Notification - Vibration Sensor Method
description: Get notified when dryer finishes using vibration detection. Clever method using multi-purpose sensor.
keywords: dryer done alert, vibration sensor dryer, laundry completion alert, dryer automation, vibration detection, appliance monitoring, smart laundry
---

# Notify me when the dryer is done

Get alerted when the dryer finishes so you can remove clothes promptly and reduce wrinkles. This clever vibration sensor method works even with 240V dryers.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Efficiency</h4>
    <ul>
      <li><strong>Prompt Clothes Removal</strong> - Empty dryer right when cycle ends to reduce wrinkles</li>
      <li><strong>Start Next Load</strong> - Know when dryer is available for next batch</li>
      <li><strong>Laundry Flow</strong> - Keep laundry moving efficiently from washer to dryer to folding</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Convenience</h4>
    <ul>
      <li><strong>Save Time</strong> - No more checking if dryer is done</li>
      <li><strong>Reduce Re-Drying</strong> - Clothes won't sit and get wrinkled</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment - Option 1: Multi-Sensor (Recommended for 240V dryers)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Multi-Purpose Sensor</strong>
      <div class="product-details">
        Popular brands: SmartThings, Aeotec, Zigbee multi-sensors<br>
        Vibration detection • Door contact sensor • Battery powered • Attach to dryer door
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Essential Equipment - Option 2: Power Monitoring (If standard 120V outlet)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Power Metering Smart Plug</strong>
      <div class="product-details">
        15A rated minimum • Only works if dryer uses standard outlet (rare)<br>
        <em>Note: Most dryers use 240V hardwired connection</em>
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Light</strong>
      <div class="product-details">
        In laundry room for visual alert when done
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dashboard Tile</strong>
      <div class="product-details">
        Showing dryer status and escalating reminders
      </div>
    </div>
  </div>
</div>

## Automation setup - Multi-sensor method

<div class="automation-example">IF vibration stops for 5 minutes
AND door closed
AND dryer was running
THEN send notification "Dryer done - remove clothes!"
AND set dryer_running to false</div>

<div class="info-box">
  <strong>💡 Multi-Sensor Requirements & Placement</strong>
  <ul>
    <li><strong>Platform:</strong> Home Assistant, SmartThings (with WebCoRE/SharpTools), or Hubitat with variables/virtual switches</li>
    <li><strong>Sensor:</strong> Multi-sensor with both vibration and contact detection</li>
    <li><strong>Mounting:</strong> On dryer door (top or side works best). Should sense vibration when drum spinning and detect door opening/closing. Secure firmly with adhesive or tape.</li>
    <li><strong>Testing:</strong> Run a dryer cycle. Verify vibration detected throughout cycle, notification when cycle ends, and door opening resets system.</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Step 1: Detect Dryer Running</h4>
    
    <h4>Triggers</h4>
    <ul>
      <li>Multi-purpose sensor vibration changes to Active or Inactive (any vibration change)</li>
    </ul>
    
    <h4>Conditions</h4>
    <ul>
      <li>Contact sensor is closed (door closed)</li>
      <li>Vibration has stayed active for 5 minutes (not just bump/slam)</li>
    </ul>
    
    <h4>Actions</h4>
    <ul>
      <li>Turn on variable/virtual switch "dryer_running"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 2: Detect Dryer Done</h4>
    
    <h4>Triggers</h4>
    <ul>
      <li>Vibration becomes Inactive (stops vibrating)</li>
    </ul>
    
    <h4>Conditions</h4>
    <ul>
      <li>Contact sensor is closed (door still closed)</li>
      <li>Variable "dryer_running" is true</li>
      <li>Vibration inactive for 5 minutes (confirms actually done)</li>
    </ul>
    
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Dryer is done!"</li>
      <li>Set variable "dryer_running" to false</li>
      <li>Flash laundry room light (optional)</li>
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
      <li>Create two boolean helpers: "dryer_running" and "dryer_needs_emptying"</li>
      <li>Start: Vibration changes AND door closed AND active 5min</li>
      <li>Done: Vibration inactive 5min AND door closed AND running</li>
      <li>Actions: Notify, Turn off running, Turn on needs_emptying, Flash light</li>
      <li>Reset: Door opens → Turn off both booleans</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <ol>
      <li>Use WebCoRE or SharpTools for complex logic</li>
      <li>Start: Vibration changes AND door closed AND active 5min → Virtual switch on</li>
      <li>Done: Vibration inactive 5min AND door closed AND switch on</li>
      <li>Actions: Notify, Switch off, Flash light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <ol>
      <li>Create virtual switch "Dryer Running"</li>
      <li>Use Rule Machine with vibration sensor</li>
      <li>Start: Vibration active 5min AND door closed → Switch on</li>
      <li>Done: Vibration inactive 5min AND switch on → Notify, Switch off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <ol>
      <li>Cannot directly handle complex vibration+contact logic</li>
      <li>Use Home Assistant or Hubitat as bridge</li>
      <li>Expose notification trigger to HomeKit</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa / Google Home</h4>
    </div>
    <ol>
      <li>Limited support for complex vibration+contact logic</li>
      <li>Use Home Assistant or SmartThings for automation</li>
      <li>Trigger Alexa/Google actions from primary platform</li>
    </ol>
  </div>
</div>

## Advanced features

### Escalating reminders

Remind if clothes left in dryer:

Create two reminder automations:
1. **30 min reminder:** If "dryer_needs_emptying" on for 30 minutes, send "REMINDER: Dryer clothes waiting for 30 minutes!"
2. **2 hour urgent:** If still on after 2 hours, send high-priority "URGENT: Dryer clothes sitting for 2 hours - wrinkles!"

### Dashboard status

Visual indicator:

Create template binary sensor with these states:
- **Running:** Blue tumble dryer icon (when dryer_running is on)
- **Done - needs attention:** Red alert icon (when dryer_needs_emptying is on)
- **Empty:** Gray off icon (when both are off)

### Track cycle duration

Measure how long dryer runs:

Create automation that sends notification when dryer finishes, including the total cycle duration calculated from when "dryer_running" was turned on.

## Troubleshooting

### Issue: False "Done" Notifications

**Causes:**
- Dryer paused temporarily (door opened mid-cycle)
- Vibration sensor too sensitive (detecting other vibrations)
- Delay too short (drum spins intermittently)
- Kids bumping dryer

**Solutions:**
✅ Increase vibration inactive delay to 8-10 minutes
✅ Require door closed condition throughout
✅ Position sensor away from external vibration sources
✅ Add condition: Dryer must have been running for minimum 15 minutes
✅ Test sensor placement - may need adjustment

Add condition to automation: Dryer must have been in "running" state for at least 15 minutes before done notification can trigger.

### Issue: No notification when dryer finishes

**Causes:**
- Sensor not detecting vibration
- Sensor battery dead
- Door opened before cycle ended
- Sensor fell off dryer
- "Dryer running" never set to true

**Check:**
- ✅ Verify sensor battery level
- ✅ Test vibration sensor manually (shake it, check state)
- ✅ Check sensor is securely attached to dryer
- ✅ Review automation logs - which condition failed?
- ✅ Monitor sensor during actual dryer cycle
- ✅ Verify dryer_running variable was set to true

**Fix:**
- Reposition sensor if vibration not detected
- Use stronger adhesive or mounting method
- Replace battery if low
- Add debug notifications at each automation step

### Issue: Vibration detected when dryer not running

**Causes:**
- Washer vibration affecting dryer sensor
- Other appliances causing vibration
- Sensor too sensitive
- Kids playing near laundry area

**Solutions:**
✅ Increase required vibration duration (10 minutes instead of 5)
✅ Add time-based condition (only during typical dryer hours)
✅ Position sensor to minimize external vibration
✅ Combine with other triggers (e.g., laundry room door closed)
✅ Add manual override to disable automation temporarily

Add conditions to automation:
- Only trigger during typical laundry hours (7am-10pm)
- Require vibration sustained for 10 minutes instead of 5

## Alternative: Power monitoring method

If your dryer uses a standard 120V outlet (rare), you can use the same power monitoring method as the washer automation.

**Setup:**
- Plug dryer into 15A+ rated smart plug with power monitoring
- Detect start: Power above 200W
- Detect done: Power below 20W for 5 minutes

*Note: Most dryers use 240V hardwired connections and cannot use smart plugs.*

---

**Related automations:**
- [Washer done notification](/automation/appliances/washer-done-notification/)
- [Dishwasher done notification](/automation/appliances/dishwasher-done-notification/)
- [Away mode automation](/automation/daily-routines/away-mode/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliance Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
