---
layout: default
title: Smart Window Open/Close Notifications for Energy Savings
description: Get notified when outdoor temperature is ideal for opening or closing windows. Save energy by using free heating or cooling.
keywords: window notification automation, energy saving alerts, when to open windows, temperature notification, smart thermostat notifications, free heating, free cooling, natural ventilation
---

# Notify when to open or close windows

Save energy by using outdoor air for heating or cooling instead of running HVAC. Get smart notifications when outdoor temperature is perfect for opening or closing windows.

## Use cases

* **Free Heating** - Warm winter days - outside air warmer than your heating setpoint
* **Free Cooling** - Cool summer nights - outside air cooler than your cooling setpoint
* **Energy Savings** - Take advantage of nice weather instead of running HVAC
* **Optimal Ventilation** - Know the best times to air out your home
* **Weather Awareness** - Stay informed about ideal conditions

## Products needed

### Essential

* **Indoor Temperature Sensor** - Monitor current indoor temperature
  - Can use smart thermostat's sensor
  - Or standalone temperature sensors
  
* **Outdoor Temperature Sensor** - Monitor outdoor conditions
  - Weather station integration (Weather Underground, OpenWeatherMap)
  - OR physical outdoor sensor
  - Popular brands: Ambient Weather, Ecowitt, Aqara outdoor sensor
  
* **Smart Home Platform** - For notifications and logic
  - Home Assistant, SmartThings, Hubitat, etc.

### Optional enhancements

* **Contact Sensors** - Track which windows are currently open/closed
* **Weather Forecast Integration** - Predict upcoming conditions
* **Dashboard Widget** - Visual indicator of optimal window status

## Basic automation setup

### For heating season (winter)

**Triggers:**
* Outside temperature rises above thermostat heating setpoint
* Example: Outside is 72°F, thermostat set to 70°F

**Conditions:**
* Windows are currently closed
* House is in heating mode
* Time is during daylight hours (optional)

**Actions:**
* Send notification: "Outside is warmer than inside! Open windows to save energy."

### For cooling season (summer)

**Triggers:**
* Outside temperature drops below thermostat cooling setpoint
* Example: Outside is 68°F, thermostat set to 72°F

**Conditions:**
* Windows are currently closed
* House is in cooling mode
* Time is typically evening/night (optional)

**Actions:**
* Send notification: "Outside is cooler than inside! Open windows to save energy."

## Platform-specific examples

### Home Assistant

**Notify to open windows (winter - free heating):**

Create automation with these elements:
- **Trigger:** Outside temperature rises above thermostat heating setpoint
- **Conditions:**
  - All windows are closed
  - Thermostat in heating mode
  - Daytime (between sunrise and sunset)
- **Action:** Send notification: "Outside is [temp]°F, inside is [temp]°F. Open windows for free heating!"

**Notify to open windows (summer - free cooling):**

Create automation with these elements:
- **Trigger:** Outside temperature drops below thermostat cooling setpoint for 15 minutes
- **Conditions:**
  - All windows are closed
  - Thermostat in cooling mode
  - Evening/night (after sunset)
- **Action:** Send notification with actionable button: "Open windows for free cooling" with "Done - Windows Opened" action

**With temperature difference threshold:**

Only notify when significant temperature difference (5°F or more):
- Check absolute difference between outdoor and indoor temperature
- Verify conditions are favorable (outside warmer in winter OR cooler in summer)
- Send notification showing exact temperature difference

### SmartThings

Create routine:
1. **IF** Outdoor temperature sensor is greater than thermostat setpoint
2. **AND** All windows are closed
3. **THEN** Send notification "Outside warmer - open windows for free heating"

### Apple HomeKit

HomeKit has limited temperature comparison logic. Workaround:
1. Use Home Assistant or similar hub for logic
2. Create notification through external service
3. OR use manual checking via dashboard

### Alexa

Create routine with temperature comparison:
1. **When:** Outdoor temperature changes
2. **Add condition:** Outdoor temp > Indoor temp by 5° (heating season)
3. **Action:** Send notification to phone

### Google Home

Limited native support for complex temperature comparisons. Use integration with:
- IFTTT for notifications
- Home Assistant for logic
- Manual dashboard checking

## Advanced features

### Notify to close windows

Alert when outdoor temperature is no longer favorable:

Create automation with these elements:
- **Trigger:** Outside temperature drops 5°F below inside temperature
- **Condition:** At least one window is open AND in heating season
- **Action:** Send notification: "Getting cold outside ([temp]°F). Time to close windows and resume heating."

### Weather forecast integration

Predict optimal window times using forecast data:

Create automation triggered at 5 PM:
- Check evening forecast temperature
- If forecast shows cool evening (below 65°F) AND currently warm inside (above 72°F)
- Send notification: "Forecast shows cool evening. Good night to open windows!"

### Include estimated savings

Calculate potential savings:

Include message in notification: "Open windows now - save ~$0.50/hour vs running AC!"

### Rain alert for open windows

Warn before rain if windows open:

Create automation with these elements:
- **Trigger:** Weather forecast changes
- **Condition:** Rain predicted in next period AND windows are open
- **Action:** Send high-priority notification: "Rain expected soon - close windows!"

## Troubleshooting

### Issue: Too many notifications

**Causes:**
- Temperature constantly fluctuating around threshold
- Notifications sent every time temp changes
- No cooldown period between notifications
- Both heating and cooling alerts active simultaneously

**Solutions:**
✅ Add "for: 15 minutes" delay to trigger - ensure temperature stable
✅ Increase temperature difference threshold (5°F instead of 2°F)
✅ Send maximum one notification per 2-hour period
✅ Only notify during specific hours (morning, evening)
✅ Add actionable notification - dismiss or snooze for certain period
✅ Use notification cooldown automation

**Cooldown example:**
Add condition: Only send notification if previous notification was sent more than 2 hours ago (check automation's last triggered time)

### Issue: Notifications not helpful

**Causes:**
- Notification sent at inconvenient times (middle of night, at work)
- Temperature difference too small to matter
- Outdoor conditions not actually comfortable (humidity, wind)
- Windows already open

**Check:**
- ✅ Add time restrictions: Only notify 7 AM-10 PM
- ✅ Only notify when home (presence detection)
- ✅ Check window sensors - don't notify if windows already open
- ✅ Increase minimum temperature difference (5-8°F minimum)
- ✅ Include humidity in decision (high humidity makes cooling less effective)

**Fix:**
Add multiple conditions:
- Only notify during awake hours (7 AM - 10 PM)
- Only when someone is home (check home mode)
- Significant temp difference (5°F minimum)
- Not too humid (outdoor humidity below 70%)

### Issue: Outdoor temperature sensor inaccurate

**Causes:**
- Weather integration using wrong location
- Outdoor sensor in direct sunlight
- Sensor too close to house (heat radiance)
- Weather service data delayed or inaccurate

**Solutions:**
✅ Verify weather integration location (check lat/long coordinates)
✅ Use multiple weather sources and average them
✅ Mount physical sensor in shaded area, away from walls
✅ Compare multiple weather services (OpenWeatherMap, Weather Underground, local station)
✅ Add calibration offset if sensor consistently off
✅ Use nearest weather station data instead of forecast

---

**Related automations:**
- [Stop thermostat when windows open](/automation/climate/thermostat-windows-open/)
- [Resume thermostat when all windows close](/automation/climate/thermostat-windows-close/)
- [Activate air purifier when air quality drops](/automation/climate/air-quality-purifier/)

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
