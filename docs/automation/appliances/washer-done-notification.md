---
layout: default
title: Washer Done Notification - Power Monitoring Method
description: Get notified when the washing machine finishes. Use power monitoring to detect cycle completion automatically.
keywords: washer done alert, laundry notification, power monitoring washer, washing machine automation, laundry done alert, appliance monitoring, smart laundry
---

# Notify me when the washer is done

Don't forget wet clothes in the washer. Get notified when the cycle completes so you can transfer to the dryer promptly and avoid mildew.

## Use cases

* **Transfer to Dryer Promptly** - Be reminded when washer finishes
* **Start Next Load** - Know when machine is available
* **Avoid Forgetting Clothes** - No more wet clothes sitting for hours
* **Laundry Flow** - Keep laundry moving efficiently
* **Multi-Tasking** - Get alerted while doing other things

## Products needed

### Essential

**Option 1: Power Monitoring (Recommended)**
* **Power Metering Smart Plug** - Measures washer electricity usage
  - Popular brands: TP-Link Kasa, Shelly, Zigbee power monitoring plugs
  - Key features: Real-time wattage measurement, 15A rating minimum
  - Plug washer into smart plug

**Option 2: Contact Sensor (Alternative)**
* **Contact Sensor** on washer door
* **Multi-Sensor** with vibration detection

### Optional Enhancements

* **Smart Light** in laundry room for visual alert
* **Dashboard Tile** showing washer status
* **Voice Announcement** on smart speaker

## Automation setup - Power monitoring

This is the most reliable method for front-load and top-load washers.

### Step 1: Learn power consumption pattern

1. Plug washer into power monitoring plug
2. Run a full cycle
3. Note the power levels:
   - **Idle:** < 5 watts (or 0W)
   - **Running:** 100-500 watts (varies by cycle phase)
   - **Done:** < 5 watts

Washing machines cycle through different phases (fill, agitate, spin) with varying power use. The key is detecting when power drops and STAYS low.

### Step 2: Create start detection

**Triggers:**
* Power consumption rises above 50 watts (washer starts)

**Actions:**
* Set variable "washer_running" to true
* OR turn on virtual switch
* Optional: Start timer

### Step 3: Create done notification

**Triggers:**
* Power consumption drops below 10 watts for 3 minutes

**Conditions:**
* Variable "washer_running" is true (confirms washer was actually running)

**Actions:**
* Send notification: "Washer is done!"
* Set variable "washer_running" to false
* Flash laundry room light (optional)
* Update dashboard tile

## Platform-Specific Examples

### Home Assistant

**Create Helper Boolean:**

Create a boolean helper (toggle) named "washer_running" with initial value off. This tracks whether the washer is currently running a cycle.

**Automation - Detect washer start:**

Create automation with these elements:
- **Trigger:** Washer plug power consumption rises above 50W
- **Action:** Turn on "washer_running" boolean helper

**Automation - Detect washer done:**

Create automation with these elements:
- **Trigger:** Washer plug power drops below 10W for 3 minutes
- **Condition:** "washer_running" boolean is on
- **Action 1:** Send notification "Washer is done! Transfer clothes to dryer."
- **Action 2:** Turn off "washer_running" boolean
- **Action 3 (optional):** Flash laundry room light for visual alert

### SmartThings

Create two routines:

**Routine 1: Washer Start**
1. **IF** Washer plug power above 50W
2. **THEN** Turn on virtual switch "Washer Running"

**Routine 2: Washer Done**
1. **IF** Washer plug power below 10W for 3 minutes
2. **AND** Virtual switch "Washer Running" is on
3. **THEN** Send notification "Washer is done"
4. **THEN** Turn off virtual switch
5. **THEN** Flash laundry room light

### Apple HomeKit

HomeKit has limited power monitoring automation. Use workaround:
1. Use Home Assistant or Hubitat for logic
2. Expose notification to HomeKit
3. OR use IFTTT for notification trigger

### Alexa

Create routines:

**Routine 1: Start Detection**
1. **When:** Washer plug power above 50W
2. **Action:** Turn on virtual switch "Washer Running"

**Routine 2: Done Notification**
1. **When:** Washer plug power below 10W
2. **Add condition:** Virtual switch "Washer Running" is on
3. **Action:** Send notification to phone
4. **Action:** Alexa announces "The washer is done"

### Google Home

Limited native support. Use Home Assistant or IFTTT for power monitoring logic.

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
- [Away mode automation](/automation/presence/away-mode/)

[← Back to appliance automations](/automation/appliances/) | [View all automations →](/automation/)
