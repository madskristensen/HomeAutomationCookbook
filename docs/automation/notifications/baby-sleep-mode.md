---
layout: automation
title: Stop Automations When Baby Sleeps - Quiet Mode Automation
description: Disable automations in baby's room when they're sleeping. Detect sleep using white noise machine or monitor with power monitoring.
keywords: baby sleep automation, nursery automation, quiet mode, sleep detection, power monitoring, white noise automation, baby monitor detection
---

# Stop automations when baby sleeps

Nothing is worse than putting the baby to sleep, just for the automated lights to come on and wake her up. There are ways we can detect if the baby is asleep and then disable any automation from disturbing her.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Baby & Nursery</h4>
    <ul>
      <li><strong>Nap Time</strong> - Disable nursery automations during sleep</li>
      <li><strong>Nighttime Sleep</strong> - Keep room dark and quiet all night</li>
      <li><strong>Smart Quiet Mode</strong> - House knows baby is sleeping</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Adults & Others</h4>
    <ul>
      <li><strong>Afternoon Nap</strong> - Disable bedroom automations during rest</li>
      <li><strong>Work From Home</strong> - Quiet mode for important calls</li>
      <li><strong>Guest Sleeping</strong> - Respect guest room quiet time</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>White Noise Machine or Baby Monitor</strong>
      <div class="product-details">
        Any device that runs while baby sleeps<br>
        The device acts as the "sleep indicator"
      </div>
    </div>
    
    <div class="product-item">
      <strong>Power Metering Smart Plug</strong>
      <div class="product-details">
        TP-Link Kasa, Shelly, or any plug with power monitoring<br>
        Detects when sleep device is running
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 How It Works</strong>
  <p>Plug the white noise machine or baby monitor into the smart plug. When the baby goes down for sleep, turn on the white noise or monitor. This will draw power, which you monitor using the smart plug. When power consumption rises, you know baby is sleeping.</p>
</div>

## Logic

<div class="automation-example">IF plug power rises above 5 watts
THEN set "baby sleeping" to true
AND disable nursery automations</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Step 1: Detect Sleep Start</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Plug's power consumption rises above 5 watts</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>None</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Flip virtual switch "Baby Sleeping" to on</li>
      <li>OR Set variable "baby_sleeping" to true</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 2: Detect Sleep End</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Plug's power consumption drops below 2 watts for 2 minutes</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>"Baby Sleeping" is currently on</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Turn off "Baby Sleeping" virtual switch</li>
      <li>OR Set variable "baby_sleeping" to false</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 3: Use in Other Automations</h4>
    <p>Add a condition to your nursery automations:</p>
    <ul>
      <li><strong>Condition:</strong> "Baby Sleeping" is OFF</li>
      <li>This prevents the automation from running when baby is asleep</li>
    </ul>
  </div>
</div>

## Advanced features

### Room-specific quiet mode

Expand beyond just the nursery:

**Affected Automations:**
- Motion lights in nursery (disabled)
- Motion lights in adjacent hallway (dimmed to 10%)
- Doorbell chime volume (reduced)
- Smart speaker volume (lowered)

**Logic:**
When "Baby Sleeping" is on:
- Nursery motion lights: Disabled completely
- Hallway lights: 10% if triggered
- Whole-house speaker volume: 30%

### Time-based expectations

Combine with time for smarter behavior:

**Nighttime Sleep (7 PM - 7 AM):**
- Longer expected sleep duration
- More aggressive quiet mode
- No automations in nursery

**Naptime (10 AM - 5 PM):**
- Shorter expected duration
- Modified quiet mode
- Some automations may proceed quietly

### Wake detection

Detect when baby wakes up before you turn off the monitor:

**Sound Detection:**
- Use smart speaker with sound detection
- Crying sound triggers "baby awake" even before monitor off

**Motion Detection:**
- Camera or sensor in nursery
- Motion during expected sleep time = possible wake

### Dashboard integration

Visual status for caregivers:

**Dashboard Tile:**
- Green: Baby awake, normal automation
- Red: Baby sleeping, quiet mode active
- Shows time sleeping started
- Manual override button

### Multi-child support

Track multiple children:

**Setup:**
- Separate monitor/plug for each child
- Separate virtual switch for each
- Combined "Any Child Sleeping" switch for house-wide rules

**Logic:**
- Individual room rules per child
- Global quiet mode if ANY child sleeping
- Different automation rules per room

## Failure modes

### Issue: False "sleeping" detection

**Causes:**
- Power threshold too low
- Device has standby power draw
- Interference from other devices

**Solutions:**
✅ Measure actual power consumption of device
✅ Increase power threshold slightly
✅ Add time requirement (power > 5W for 1 minute)
✅ Verify only sleep device is on plug

### Issue: Automations still trigger during sleep

**Causes:**
- Condition not added to automation
- Condition logic incorrect
- Virtual switch not updating

**Solutions:**
✅ Verify condition is added to each affected automation
✅ Check condition logic (should be "Baby Sleeping is OFF")
✅ Test virtual switch manually
✅ Review automation logs

### Issue: Sleep mode doesn't end when monitor turned off

**Causes:**
- Power threshold too low for "off" detection
- Monitor has standby power
- Delay too short

**Solutions:**
✅ Lower the "off" power threshold (try 1W)
✅ Increase delay before declaring sleep over
✅ Check if monitor has true standby power draw
✅ Add manual override option

### Issue: Variable/switch state gets stuck

**Causes:**
- Power monitoring glitch
- Automation error
- Network connectivity issue

**Solutions:**
✅ Add auto-reset after max time (8 hours for night, 3 hours for nap)
✅ Create manual reset button on dashboard
✅ Check plug connectivity
✅ Add backup time-based reset

## Best practices

### Choose the right indicator device

**Good Choices:**
✅ White noise machine (clear on/off power difference)
✅ Baby video monitor (consistent power draw when on)
✅ Dedicated nursery lamp (turn on for sleep time)

**Avoid:**
❌ Devices with variable power (brightness dimming)
❌ Devices with high standby power
❌ Devices that cycle on/off during use

### Calibrate power thresholds

**Process:**
1. Plug device into power monitoring plug
2. Record power when device is OFF (standby)
3. Record power when device is ON (running)
4. Set "on" threshold above standby but below running
5. Set "off" threshold below "on" threshold

**Example:**
- Standby: 0.5W
- Running: 8W
- On threshold: 5W
- Off threshold: 2W

### Gradual quiet mode

**Smooth Transitions:**
- Don't abruptly cut all sound
- Lower volumes gradually
- Allow some quiet activities

**Priority Levels:**
1. Nursery: Complete quiet mode
2. Adjacent rooms: Reduced volume/brightness
3. Rest of house: Normal with volume limits

---

## Related recipes
- [Lights off after motion](/automation/lighting/lights-off-after-motion/)
- [Bedtime routine](/automation/daily-routines/bedtime-routine/)
- [Teeth brushing reminder](/automation/notifications/teeth-brushing-reminder/)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
