---
layout: default
title: Dryer Done Notification - Vibration Sensor Method
description: Get notified when dryer finishes using vibration detection. Clever method using multi-purpose sensor.
keywords: dryer done alert, vibration sensor dryer, laundry completion alert, dryer automation, vibration detection, appliance monitoring, smart laundry
---

# Notify me when the dryer is done

Get alerted when the dryer finishes so you can remove clothes promptly and reduce wrinkles. This clever vibration sensor method works even with 240V dryers.

## Use cases

* **Prompt Clothes Removal** - Empty dryer right when cycle ends to reduce wrinkles
* **Start Next Load** - Know when dryer is available for next batch
* **Laundry Flow** - Keep laundry moving efficiently from washer to dryer to folding
* **Save Time** - No more checking if dryer is done
* **Reduce Re-Drying** - Clothes won't sit and get wrinkled

## Products needed

### Essential

**Option 1: Multi-Sensor Method (Recommended for 240V dryers)**
* **Multi-Purpose Sensor** with vibration and contact detection
  - Popular brands: SmartThings, Aeotec, Zigbee multi-sensors
  - Key features: Vibration detection, door contact sensor, battery powered
  - Attach to dryer door

**Option 2: Power Monitoring (If standard 120V outlet)**
* **Power Metering Smart Plug** - 15A rated minimum
  - Only works if dryer uses standard outlet (rare)
  - Most dryers use 240V hardwired connection

### Optional Enhancements

* **Smart Light** in laundry room for visual alert
* **Dashboard Tile** showing dryer status
* **Escalating Reminders** if clothes not removed

## Automation setup - Multi-sensor method

This method has been used successfully for years and is very accurate. It detects the vibration of the drum spinning.

### Requirements

* Smart home platform with variables/virtual switches
* Works with: Home Assistant, SmartThings (with WebCoRE or SharpTools), Hubitat
* Multi-sensor with both vibration and contact detection

### Sensor placement

**Where to Mount:**
* On dryer door (top or side works best)
* Should sense vibration when drum spinning
* Should detect door opening/closing
* Secure firmly with adhesive or tape

**Testing:**
* Run a dryer cycle
* Verify vibration detected throughout cycle
* Confirm notification when cycle ends
* Test door opening resets system

### Step 1: Detect dryer running

**Triggers:**
* Multi-purpose sensor vibration changes to Active or Inactive (any vibration change)

**Conditions:**
* Contact sensor is closed (door closed)
* AND vibration has stayed active for 5 minutes (not just bump/slam)

**Actions:**
* Turn on variable/virtual switch "dryer_running"

### Step 2: Detect dryer done

**Triggers:**
* Vibration becomes Inactive (stops vibrating)

**Conditions:**
* Contact sensor is closed (door still closed)
* AND variable "dryer_running" is true
* AND vibration inactive for 5 minutes (confirms actually done)

**Actions:**
* Send notification: "Dryer is done!"
* Set variable "dryer_running" to false
* Flash laundry room light (optional)

## Platform-Specific Examples

### Home Assistant

**Create Helper Boolean:**

Create two boolean helpers:
1. "dryer_running" - tracks if dryer is currently running
2. "dryer_needs_emptying" - tracks if dryer is done and needs attention

**Automation - Detect dryer start:**

Create automation with these elements:
- **Trigger:** Dryer vibration sensor state changes
- **Conditions:** Door contact is closed AND vibration has been active for 5 minutes
- **Action:** Turn on "dryer_running" boolean

**Automation - Detect dryer done:**

Create automation with these elements:
- **Trigger:** Vibration sensor becomes inactive for 5 minutes
- **Conditions:** Door still closed AND "dryer_running" is on
- **Action 1:** Send notification "Dryer is done! Remove clothes to prevent wrinkles."
- **Action 2:** Turn off "dryer_running" boolean
- **Action 3:** Turn on "dryer_needs_emptying" boolean
- **Action 4 (optional):** Flash laundry room light

**Reset when door opens:**

Create automation with these elements:
- **Trigger:** Door contact sensor opens
- **Action:** Turn off both "dryer_running" and "dryer_needs_emptying" booleans

### SmartThings

Use WebCoRE or SharpTools for complex logic:

**Piston/Rule Logic:**

1. IF vibration sensor changes state
2. AND door contact is closed
3. AND vibration has been active for 5 minutes
4. THEN turn on virtual switch "Dryer Running"

5. IF vibration becomes inactive for 5 minutes
6. AND door is still closed
7. AND "Dryer Running" switch is on
8. THEN send notification
9. AND turn off "Dryer Running" switch
10. AND flash laundry light

### Apple HomeKit

HomeKit cannot directly handle this complex logic. Use Home Assistant or Hubitat as bridge and expose notification trigger to HomeKit.

### Alexa/Google Home

Limited support for complex vibration+contact logic. Use Home Assistant or SmartThings for automation logic, then trigger Alexa/Google actions.

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
- [Away mode automation](/automation/presence/away-mode/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliance Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
