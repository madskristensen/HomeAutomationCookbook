---
layout: default
title: Activate Air Purifier When Air Quality Drops - Health Automation
description: Automatically run your air purifier when indoor air quality drops below healthy levels. Monitor AQI and PM2.5 for cleaner air.
keywords: air quality automation, air purifier control, AQI sensor automation, PM2.5 automation, indoor air quality, automatic air purifier, health automation, allergy automation
---

# Clean the air when air quality drops

Indoor air quality fluctuates throughout the day from cooking, outdoor pollution, pet dander, and more. Automate air purification when quality drops below healthy thresholds for better health and comfort.

## Use cases

* **Cooking Smoke** - Air quality drops when cooking creates smoke or strong odors
* **Seasonal Allergies** - Outdoor pollen affecting indoor air quality
* **Poor Outdoor AQI** - Wildfire smoke or pollution entering home
* **Pet Odors** - Dander and smells accumulating in living spaces
* **Health Maintenance** - Proactive air quality management for respiratory health

## Products needed

### Essential

**Option 1: Smart air purifier**
* **Air Quality Sensor** - Measures AQI or PM2.5
  - Popular brands: Awair, IQAir, Aqara, PurpleAir
  - Key features: PM2.5 detection, WiFi connectivity
  
* **Smart Air Purifier** - WiFi-enabled purifier
  - Brands: Coway, Levoit, Dyson, Winix
  - OR Regular purifier on **Smart Plug** (simpler option)

**Option 2: HVAC-based**
* **Air Quality Sensor**
* **Smart Thermostat** with air filter/circulation mode
  - Brands: Ecobee, Honeywell

### Optional enhancements

* **Multiple Sensors** - Track air quality in different rooms
* **Outdoor Air Quality Monitor** - Compare indoor vs outdoor
* **Smart Notifications** - Alert when air quality poor

## Basic automation setup

### Triggers
* Air quality (AQI) drops below 35
* OR PM2.5 concentration above 50 μg/m³
* OR VOC (Volatile Organic Compounds) exceeds threshold

### Conditions (optional)
* None - air quality is health-critical and should be addressed immediately
* Optional: Only during occupied hours

### Actions
* Turn on air purifier at high speed
* OR activate HVAC fan with filter
* Optional: Close smart windows/vents
* Optional: Send notification with current air quality reading

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Air quality sensor drops below 35 AQI
- **Action:**
  - Turn on air purifier fan at 100% (high speed)
  - Send notification: "Air quality poor ([current AQI]) - Purifier activated"

**Using PM2.5 instead:**

Create automation with these elements:
- **Trigger:** PM2.5 sensor rises above 50 μg/m³
- **Action:** Turn on air purifier smart plug

**Multi-level response:**

Create two separate automations:

**Moderate quality (AQI 35-50):**
- **Trigger:** AQI between 35 and 50
- **Action:** Turn on purifier at 50% speed (medium)

**Poor quality (AQI below 35):**
- **Trigger:** AQI below 35
- **Action:** Turn on purifier at 100% speed (high)

### SmartThings

Create routine:
1. **IF** Air quality sensor reports AQI below 35
2. **THEN** Turn on air purifier smart plug
3. **THEN** Send notification "Air quality poor - purifier activated"

### Apple HomeKit

1. Create automation in Home app
2. **When:** Air quality sensor detects poor air quality
3. **Conditions:** AQI below threshold (if sensor supports)
4. **Do:** Turn on air purifier (via smart plug or direct control)

### Alexa

Create routine:
1. **When:** Smart Home sensor detects value (air quality sensor)
2. **Add condition:** Value below 35 AQI
3. **Action:** Turn on air purifier smart plug
4. **Action:** Send notification to phone

### Google Home

Create automation:
1. **Starter:** Air quality sensor detects poor quality
2. **Action:** Turn on air purifier
3. **Action:** Announce "Air quality low, purifier activated"

## Advanced features

### Automatic purifier shutoff

Turn off when air quality improves:

Create automation with these elements:
- **Trigger:** Air quality rises above 50 AQI for 30 minutes
- **Condition:** Purifier is currently on
- **Action:**
  - Turn off purifier
  - Send notification: "Air quality improved ([current AQI]) - Purifier turned off"

### Graduated speed control

Adjust purifier speed based on air quality level:

Create automation triggered by air quality sensor state change:
- **Good air (AQI above 50):** Set fan to 25% (low/auto)
- **Moderate (AQI 35-50):** Set fan to 50% (medium)
- **Unhealthy (AQI below 35):** Set fan to 100% (high)

Use conditional logic to check current AQI and set appropriate fan speed.

### No purifier? Alternative actions

If you don't have an air purifier:
- Send mobile notification: "Air quality poor ([current AQI]). Consider opening windows or improving ventilation."
- Create persistent notification on dashboard with current AQI and suggestion to check outdoor air quality before opening windows

## Air quality levels reference

### AQI scale

**Good (0-50 AQI):**
- No action needed
- Air quality satisfactory

**Moderate (51-100):**
- Turn on purifier at low speed
- Sensitive individuals may experience minor effects

**Unhealthy for Sensitive Groups (101-150):**
- Purifier on medium to high
- People with respiratory conditions should limit outdoor activity

**Unhealthy (151-200):**
- Purifier on maximum
- Notify household members
- Everyone may experience health effects

**Very Unhealthy (201-300):**
- Purifier maximum
- Urgent notification
- Health warnings for everyone

**Hazardous (301+):**
- Purifier maximum
- Emergency notification
- Seal windows/doors
- Consider evacuation if outdoor air (wildfire)

## Troubleshooting

### Issue: Purifier doesn't turn on

**Causes:**
- Air quality sensor not reporting correctly
- Threshold too low (never reaches trigger point)
- Smart plug or purifier not responding
- Automation disabled or has errors

**Solutions:**
✅ Check air quality sensor battery and connectivity
✅ View current sensor reading in app - is it updating?
✅ Adjust threshold based on typical readings (try 45-50 instead of 35)
✅ Test purifier control manually - verify smart plug works
✅ Check automation logs to see if triggers are firing
✅ Verify automation is enabled

### Issue: Purifier runs constantly

**Causes:**
- Air quality sensor placed poorly (near kitchen, litter box, etc.)
- Outdoor air quality consistently poor
- Purifier not actually improving air (filter needs replacement)
- Threshold set too high (always triggers)
- No shutoff automation created

**Check:**
- ✅ Review sensor placement - away from heat, humidity, direct sources
- ✅ Check outdoor AQI - if outdoor is poor, indoor will be affected
- ✅ Inspect purifier filter - replace if dirty or old
- ✅ Monitor air quality trends - is it improving when purifier runs?
- ✅ Create companion shutoff automation (see Advanced Features above)

**Fix:**
- Move sensor to central location away from direct pollution sources
- Lower threshold (trigger at 30 instead of 35)
- Add time delay: Only turn on if quality stays poor for 5+ minutes
- Set maximum run time: Turn off after 2 hours, reassess air quality
- Add shutoff automation with 30-minute "quality stable" delay

### Issue: False triggers from cooking

**Causes:**
- Sensor too close to kitchen
- Cooking creates brief air quality spikes
- No delay to differentiate temporary vs sustained poor quality

**Solutions:**
✅ Move sensor away from kitchen or add delay before triggering
✅ Add condition: Only trigger between certain hours (not dinner time)
✅ Use "for: 5 minutes" delay to ignore brief spikes
✅ Install separate kitchen hood fan automation
✅ Add condition: Don't trigger if stove is in use (if smart)
✅ Use higher threshold for cooking hours (trigger at 30 instead of 35)

---

**Related automations:**
- [Smart window open/close notifications](/automation/climate/window-notifications/)
- [Stop thermostat when windows open](/automation/climate/thermostat-windows-open/)
- [Away mode automation](/automation/presence/away-mode/)

[← Back to climate automations](/automation/climate/) | [View all automations →](/automation/)
