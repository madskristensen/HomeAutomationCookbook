---
layout: default
title: Dishwasher Done Notification - Temperature Method
description: Get notified when dishwasher finishes using temperature detection from drying cycle. Alternative method to power monitoring.
keywords: dishwasher done alert, temperature sensor dishwasher, completion notification, dishwasher automation, drying cycle detection, appliance monitoring
---

# Notify me when the dishwasher is done

Get alerted when dishes are clean and ready to be put away. This clever temperature-based method detects the heat from the drying cycle.

## Use cases

* **Prompt Dish Removal** - Empty dishwasher right when cycle ends
* **Kitchen Cleanup** - Know when you can run another load
* **Prevent Dishes Sitting** - Don't let clean dishes sit too long
* **Multi-Tasking** - Get alerted while doing other things
* **Track Dish Status** - Dashboard showing clean/dirty

## Products needed

### Essential

**Option 1: Temperature Sensor Method (Clever!)**
* **Multi-Purpose Sensor** with temperature and contact
  - Popular brands: Aeotec, SmartThings, Zigbee multi-sensors
  - OR standalone temperature sensor with tilt sensor
  - Mount on side or top of dishwasher door
  - Key features: Temperature detection, contact/tilt sensor

**Option 2: Power Monitoring (Traditional)**
* **Power Metering Smart Plug** - 15A rated minimum
  - Use same technique as washer automation
  - Plug dishwasher into smart plug

### Optional Enhancements

* **Dashboard Tile** showing clean/dirty status
* **Smart Light** for visual alert
* **Voice Announcement** via smart speaker

## Automation setup - Temperature method

This uses the heat from the drying cycle as the trigger - very clever and reliable!

### Sensor placement

**Where to Mount:**
* On side or top of dishwasher door
* Position to detect heat from drying cycle vent
* May require experimentation to find best spot
* Usually near top of door or side vent

**If using contact sensor:**
Register as "tilt sensor" or "garage door sensor" so it only triggers "open" when door is fully horizontal (open), not just cracked.

### Temperature patterns

Dishwashers heat up significantly during drying:
- **Normal temperature:** 68-75°F (room temp)
- **Drying cycle:** 90-120°F
- **After cycle:** Gradually cools over 30-60 minutes

### Automation logic

**Triggers:**
* Temperature rises above 90°F (32°C)

**Conditions:**
* Contact/tilt sensor has been closed for 60 minutes
  - Ensures it's the drying cycle, not just running/wash cycle
* Dishwasher in use (based on time of day or manual indicator)

**Actions:**
* Send notification: "Dishwasher is done!"
* Turn on dashboard tile showing "clean"
* Optional: Flash kitchen light

### Auto-reset dashboard tile

**Triggers:**
* Contact/tilt sensor opens (door opened)

**Actions:**
* Turn off dashboard tile
* Reset variable
* Assumes dishwasher emptied when door opened

## Platform-Specific Examples

### Home Assistant

**Create Helper Booleans:**

Create two boolean helpers:
1. "dishwasher_running" - tracks if dishwasher is currently running
2. "dishwasher_clean" - tracks if dishwasher finished and dishes are clean

**Automation - Detect dishwasher start:**

Create automation with these elements:
- **Trigger:** Dishwasher door closes
- **Condition:** "dishwasher_running" is currently off (not already marked as running)
- **Action:** Turn on "dishwasher_running" boolean

**Automation - Detect dishwasher done (temperature):**

Create automation with these elements:
- **Trigger:** Temperature sensor rises above 90°F
- **Conditions:** Door has been closed for at least 60 minutes AND "dishwasher_running" is on
- **Action 1:** Send notification "Dishwasher is done - dishes are clean!"
- **Action 2:** Turn off "dishwasher_running" boolean
- **Action 3:** Turn on "dishwasher_clean" boolean

**Reset when door opens:**

Create automation with these elements:
- **Trigger:** Dishwasher door opens
- **Action:** Turn off both "dishwasher_running" and "dishwasher_clean" booleans

### SmartThings

Create routines:

**Routine 1: Dishwasher Done**
1. **IF** Dishwasher temperature sensor above 90°F
2. **AND** Door contact closed for 60+ minutes
3. **THEN** Send notification "Dishwasher is done"
4. **THEN** Turn on virtual switch "Dishwasher Clean"

**Routine 2: Reset on Door Open**
1. **IF** Dishwasher door opens
2. **THEN** Turn off virtual switch "Dishwasher Clean"

### Apple HomeKit

1. Create automation in Home app
2. **When:** Temperature sensor above 90°F
3. **Conditions:** Contact sensor closed for 60+ minutes
4. **Do:** Send notification

### Alexa

Create routine:
1. **When:** Temperature sensor value above 90°F
2. **Add condition:** Contact sensor closed
3. **Action:** Send notification to phone
4. **Action:** Alexa announces "The dishwasher is done"

### Google Home

Limited native support for temperature triggers. Use Home Assistant or IFTTT for logic.

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
