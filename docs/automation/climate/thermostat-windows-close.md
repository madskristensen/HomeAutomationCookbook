---
layout: default
title: Resume Thermostat When All Windows Close - Climate Control
description: Automatically resume heating or cooling when all windows and doors are closed. Smart climate control that adapts to your behavior.
keywords: thermostat resume automation, windows closed automation, HVAC restart, climate control automation, automatic thermostat, restore climate control, smart HVAC
---

# Start thermostat when windows and doors are closed

Once all windows and doors are closed, it's time to resume climate control. This automation restores your HVAC system to continue heating or cooling your home.

## Use cases

* **After Airing Out** - All windows and doors have been closed after bringing in fresh air
* **Resume Normal Comfort** - Restore temperature control automatically
* **Energy Optimization** - Don't waste time with HVAC off when windows are closed
* **Seamless Experience** - Climate control adapts without manual intervention
* **Return from Nice Weather** - Automatically resume when outdoor conditions change

## Products needed

### Essential

* **Smart Thermostat** - WiFi or Zigbee enabled
  - Popular brands: Nest, Ecobee, Honeywell, Sensi
  - Key features: API control, mode restoration capability
  
* **Contact Sensors** - On all windows and doors being monitored
  - Must match the sensors used in "stop thermostat" automation
  - Popular brands: Aqara, Wyze, SmartThings, Ring
  - Coverage: All windows and doors that trigger HVAC shutdown

### Optional enhancements

* **Temperature Sensor** - Verify indoor temp before resuming (safety check)
* **Variable/Helper** - Store previous thermostat state for accurate restoration

## Basic automation setup

### Triggers
* Any window or door closes

### Conditions
* ALL windows and doors are closed (critical condition)
* Thermostat is currently off
* Optional: Indoor temperature outside comfortable range

### Actions
* Turn on thermostat
* Restore previous mode (heat/cool/auto)
* Optional: Restore previous temperature setpoint
* Optional: Send notification "Climate control resumed"

## Platform-specific examples

### Home Assistant

**Simple version:**

Create automation with these elements:
- **Trigger:** Any window or door closes
- **Conditions:**
  - ALL windows and doors must be closed (check each sensor individually)
  - Thermostat is currently "off"
- **Action:** Set thermostat HVAC mode to "heat_cool" (or "heat", "cool", "auto")

**Advanced version with state restoration:**

Instead of hardcoding mode:
- Restore thermostat to previously saved mode from helper variable
- Send notification: "Climate control resumed - all windows closed"

**Using group for all sensors:**

Create binary sensor group called "All Windows and Doors":
- Contains all window and door contact sensors
- Simplifies automation trigger and conditions
- **Trigger:** When group state changes to "off" (all closed)
- **Condition:** Thermostat is "off"
- **Action:** Restore thermostat to saved previous mode

### SmartThings

Create routine:
1. **IF** Living room window closes
2. **AND** ALL other windows/doors are closed (add condition for each)
3. **AND** Thermostat mode is "Off"
4. **THEN** Set thermostat mode to "Auto" (or saved previous mode)

### Apple HomeKit

1. Create automation in Home app
2. **When:** Any window or door closes
3. **Conditions:** 
   - All windows are closed
   - All doors are closed
   - Thermostat is off
4. **Do:** Turn on thermostat to Auto mode

### Alexa

Create routine:
1. **When:** Smart Home sensor closes (select window sensor)
2. **Add condition:** All other windows/doors closed (check each)
3. **Add condition:** Thermostat mode is "Off"
4. **Action:** Set thermostat to Auto mode

### Google Home

Create automation:
1. **Starter:** Window sensor closes
2. **Condition:** All windows and doors are closed
3. **Action:** Set thermostat to Heat-Cool mode

## Advanced features

### Save and restore complete state

Store not just mode, but complete thermostat state using scene creation:

**When stopping thermostat:**
- Create scene snapshot of thermostat (saves mode, temperature, fan, all settings)
- Turn off thermostat

**When resuming:**
- Activate saved scene
- Restores: HVAC mode, temperature setpoint, fan mode, all custom settings

### Delay before resuming

Wait a few minutes before resuming to ensure windows stay closed:

Add "for 2 minutes" delay to trigger - ensures windows remain closed before resuming

### Temperature-based resume

Only resume if indoor temperature needs adjustment:
- **Winter:** Resume heating if temperature drops below 68°F
- **Summer:** Resume cooling if temperature rises above 75°F

Use conditional logic checking indoor temperature and thermostat mode.

### Smart scheduling

Don't resume during times when HVAC would normally be off:

Add time condition: Only resume between 6 AM and 11 PM (not during sleep hours when thermostat would be in eco mode)

## Troubleshooting

### Issue: Thermostat doesn't resume

**Causes:**
- Not all windows/doors actually closed
- Missing sensor in condition check
- Previous state not saved correctly
- Automation disabled or has errors
- Platform limitation on "all closed" detection

**Solutions:**
✅ Verify ALL sensors report closed state in app
✅ Check automation conditions - ensure every window/door sensor is listed
✅ Review automation logs - see which condition is failing
✅ Test state restoration - manually turn off thermostat and trigger automation
✅ Use group sensor (Home Assistant) or virtual sensor to simplify "all closed" check
✅ Add notification showing which sensors prevented trigger

### Issue: Wrong mode restored

**Causes:**
- Previous state not saved when shutting down
- State variable not created or misconfigured
- Default mode used instead of saved mode
- Seasonal mode change (heat vs cool) not accounted for

**Check:**
- ✅ Verify "stop thermostat" automation saves state before turning off
- ✅ Check helper/variable entity exists and updates correctly
- ✅ Review saved state value in automation logs
- ✅ Test full cycle: open window → close window → verify correct mode

**Fix:**
- Create input_text helper to store previous mode
- Save complete thermostat scene instead of just mode
- Add fallback: If no saved state, use "auto" mode
- Consider seasonal logic: Default to "heat" in winter, "cool" in summer

### Issue: Thermostat resumes too quickly

**Causes:**
- Trigger fires immediately when any window closes
- Don't account for someone closing/reopening windows
- No delay to verify windows stay closed
- False triggers from sensor fluctuations

**Solutions:**
✅ Add "for: 2 minutes" delay to trigger - ensure windows stay closed
✅ Increase delay to 5 minutes during nice weather (encourage natural ventilation)
✅ Don't resume if another window opened within 5 minutes
✅ Add temperature check: Only resume if temp outside comfortable range
✅ Consider time of day: Longer delays during pleasant weather hours

---

**Related automations:**
- [Stop thermostat when windows open](/automation/climate/thermostat-windows-open/)
- [Smart window open/close notifications](/automation/climate/window-notifications/)
- [Morning routine automation](/automation/presence/morning-routine/)

[← Back to climate automations](/automation/climate/) | [View all automations →](/automation/)
