---
layout: automation
title: Washer Done Notification - Power Monitoring Method
description: Get notified when the washing machine finishes. Use power monitoring to detect cycle completion automatically.
keywords: washer done alert, laundry notification, power monitoring washer, washing machine automation, laundry done alert, appliance monitoring, smart laundry
---

# Notify me when the washer is done

Wet laundry, left too long in the drum, develops that unmistakable musty smell - the quiet punishment for forgetting. A power monitor watches the washing machine, and when the drum falls still, a gentle reminder finds you wherever you are. The clothes make it to the dryer in time. The mildew never comes.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Efficiency</h4>
    <ul>
      <li><strong>Transfer to Dryer Promptly</strong> - Be reminded when washer finishes</li>
      <li><strong>Start Next Load</strong> - Know when machine is available</li>
      <li><strong>Laundry Flow</strong> - Keep laundry moving efficiently</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Convenience</h4>
    <ul>
      <li><strong>Avoid Forgetting Clothes</strong> - No more wet clothes sitting for hours</li>
      <li><strong>Multi-Tasking</strong> - Get alerted while doing other things</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment - Option 1: Power Monitoring (Recommended)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Power Metering Smart Plug</strong>
      <div class="product-details">
        Popular brands: TP-Link Kasa, Shelly, Zigbee power monitoring plugs<br>
        Real-time wattage measurement • 15A rating minimum • Plug washer into smart plug
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Essential Equipment - Option 2: Contact Sensor (Alternative)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Contact Sensor or Multi-Sensor</strong>
      <div class="product-details">
        Contact sensor on washer door OR Multi-sensor with vibration detection
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
      <strong>Voice Announcement</strong>
      <div class="product-details">
        On smart speaker for audio notification
      </div>
    </div>
  </div>
</div>

## Automation setup - Power monitoring

<div class="automation-example">IF washer power < 10W for 3 minutes
AND washer was running
THEN send notification \"Washer done - move to dryer!\"
AND set washer_running to false</div>

<div class="info-box">
  <strong>💡 Learn Power Consumption Pattern First</strong>
  <ul>
    <li>Plug washer into power monitoring plug</li>
    <li>Run a full cycle and note the power levels:
      <ul>
        <li><strong>Idle:</strong> < 5 watts (or 0W)</li>
        <li><strong>Running:</strong> 100-500 watts (varies by cycle phase)</li>
        <li><strong>Done:</strong> < 5 watts</li>
      </ul>
    </li>
    <li>Key insight: Washing machines cycle through different phases (fill, agitate, spin) with varying power use. Detect when power drops and STAYS low.</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Step 1: Detect Washer Start</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Power consumption rises above 50 watts (washer starts)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Set variable "washer_running" to true</li>
      <li>OR turn on virtual switch</li>
      <li>Optional: Start timer</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 2: Detect Washer Done</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Power consumption drops below 10 watts for 3 minutes</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Variable "washer_running" is true (confirms washer was actually running)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Washer is done!"</li>
      <li>Set variable "washer_running" to false</li>
      <li>Flash laundry room light (optional)</li>
      <li>Update dashboard tile</li>
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
        <span class="step-label">Start</span>
        <span class="step-content">Power > 50W → Turn on "washer_running" helper</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Done</span>
        <span class="step-content">Power < 10W for 3 min AND helper on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Notify, Turn off helper, Flash light</span>
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
        <span class="step-label">Start</span>
        <span class="step-content">Power > 50W → Virtual switch on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Done</span>
        <span class="step-content">Power < 10W for 3 min AND switch on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Notify, Switch off, Flash light</span>
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
        <span class="step-label">Start</span>
        <span class="step-content">Power > 50W → Virtual switch on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Done</span>
        <span class="step-content">Power < 10W for 3 min AND switch on → Notify</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with power monitoring plug
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
        <span class="step-content">Limited power monitoring support</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Workaround</span>
        <span class="step-content">Use Home Assistant or Hubitat for logic</span>
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
        <span class="step-label">Start</span>
        <span class="step-content">Power > 50W → Virtual switch on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Done</span>
        <span class="step-content">Power < 10W AND switch on</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Notify phone, Alexa announces</span>
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
        <span class="step-content">Limited native support</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Workaround</span>
        <span class="step-content">Use Home Assistant for power monitoring</span>
      </div>
    </div>
  </div>
</div>

## Automation setup - Door sensor (alternative)

Less reliable but works if power monitoring not available:

**Triggers:**
* Washer door closes

**Actions:**
* Set variable "washer_may_be_running" to true

**Then create second automation:**

**Triggers:**
* No vibration detected for 5 minutes (if using multi-sensor)
* OR door closed for 60 minutes (basic timer method)

**Conditions:**
* Variable "washer_may_be_running" is true
* Washer door is still closed

**Actions:**
* Send notification: "Washer appears done"
* Set variable to false

## Advanced features

### Escalating reminders

Don't let clothes sit too long:

Create three automations for progressive alerts:
1. **First notification (immediate):** When power drops below 10W for 3 minutes, send "Washer done" notification and set "washer_needs_emptying" flag
2. **Reminder (30 min later):** If "washer_needs_emptying" still on after 30 minutes, send high-priority "REMINDER: Washer still needs emptying!"
3. **Urgent (2 hours later):** If flag still on after 2 hours, send urgent "Clothes in washer for 2+ hours - mildew risk!"

### Dashboard integration

Show status tile:

Create template binary sensor with these states:
- **Running:** Blue washing machine icon (when washer_running is on)
- **Done - needs attention:** Red alert icon (when washer_needs_emptying is on)
- **Empty:** Gray off icon (when both are off)

### Reset when door opens

Automatically reset when clothes removed:

Create automation with these elements:
- **Trigger:** Washer door sensor opens
- **Condition:** "washer_needs_emptying" flag is on
- **Action:** Turn off "washer_needs_emptying" flag

## Troubleshooting

### Issue: False "Done" Notifications During Cycle

**Causes:**
- Power drops briefly between cycle phases
- Threshold too high (triggering during low-power phases)
- Delay too short

**Solutions:**
✅ Increase delay to 5 minutes instead of 3
✅ Lower threshold (5W instead of 10W)
✅ Monitor full wash cycle to understand power pattern
✅ Use template trigger that requires sustained low power for 5 minutes

### Issue: No notification when done

**Causes:**
- Washer never detected as "starting"
- Power threshold incorrect
- Washer uses very little standby power
- Smart plug lost connection

**Check:**
- ✅ Verify washer_running variable was set to true
- ✅ Check automation logs - which step is failing?
- ✅ Monitor power consumption during actual cycle
- ✅ Test smart plug connectivity
- ✅ Verify sensor.washer_plug_power entity exists and updates

**Fix:**
- Adjust start detection threshold based on actual usage
- Add debugging notifications at each step
- Verify smart plug can handle washer load (15A minimum)

### Issue: Notification even when washer not used

**Causes:**
- Washer running variable stuck "on"
- Power monitoring detecting other devices
- Plug measuring wrong outlet

**Solutions:**
✅ Add auto-reset: Turn off variable after 3 hours max
✅ Verify only washer plugged into smart plug
✅ Add manual reset button on dashboard
✅ Check for power spikes from other sources
✅ Add auto-reset automation: If "washer_running" stays on for 3 hours, automatically turn it off

---

**Related automations:**
- [Dryer done notification](/automation/appliances/dryer-done-notification/)
- [Dishwasher done notification](/automation/appliances/dishwasher-done-notification/)
- [Away mode automation](/automation/daily-routines/away-mode/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliance Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
