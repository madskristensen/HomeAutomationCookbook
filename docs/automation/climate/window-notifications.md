---
layout: default
title: Smart Window Open/Close Notifications for Energy Savings
description: Get notified when outdoor temperature is ideal for opening or closing windows. Save energy by using free heating or cooling.
keywords: window notification automation, energy saving alerts, when to open windows, temperature notification, smart thermostat notifications, free heating, free cooling, natural ventilation
---

# Notify when to open or close windows

Save energy by using outdoor air for heating or cooling instead of running HVAC. Get smart notifications when outdoor temperature is perfect for opening or closing windows.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Energy Savings</h4>
    <ul>
      <li><strong>Free Heating</strong> - Warm winter days when outside air warmer than heating setpoint</li>
      <li><strong>Free Cooling</strong> - Cool summer nights when outside air cooler than cooling setpoint</li>
      <li><strong>Energy Savings</strong> - Take advantage of nice weather instead of running HVAC</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Comfort & Awareness</h4>
    <ul>
      <li><strong>Optimal Ventilation</strong> - Know the best times to air out your home</li>
      <li><strong>Weather Awareness</strong> - Stay informed about ideal conditions</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Indoor Temperature Sensor</strong>
      <div class="product-details">
        Can use smart thermostat's sensor or standalone temperature sensors
      </div>
    </div>
    
    <div class="product-item">
      <strong>Outdoor Temperature Sensor</strong>
      <div class="product-details">
        Popular brands: Ambient Weather, Ecowitt, Aqara outdoor sensor<br>
        Weather station integration (Weather Underground, OpenWeatherMap) OR physical outdoor sensor
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Home Platform</strong>
      <div class="product-details">
        For notifications and logic: Home Assistant, SmartThings, Hubitat, etc.
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Contact Sensors</strong>
      <div class="product-details">
        Track which windows are currently open/closed
      </div>
    </div>
    
    <div class="product-item">
      <strong>Weather Forecast Integration</strong>
      <div class="product-details">
        Predict upcoming conditions for better planning
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF outside temp > inside temp + 5°F (in heating season)
THEN send notification "Open windows for free heating!"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>For Heating Season (Winter)</h4>
    <strong>Trigger:</strong> Outside temp rises above thermostat heating setpoint<br>
    <strong>Conditions:</strong> Windows currently closed • House in heating mode • Daytime hours (optional)<br>
    <strong>Action:</strong> Send notification "Outside is warmer than inside! Open windows to save energy."
  </div>
  
  <div class="setup-step">
    <h4>For Cooling Season (Summer)</h4>
    <strong>Trigger:</strong> Outside temp drops below thermostat cooling setpoint<br>
    <strong>Conditions:</strong> Windows currently closed • House in cooling mode • Evening/night time (optional)<br>
    <strong>Action:</strong> Send notification "Outside is cooler than inside! Open windows to save energy."
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Outside temp rises above heating setpoint</li>
      <li>Condition: Windows closed, heating mode, daytime</li>
      <li>Action: Send notification with current temps</li>
      <li>Option: Add temperature difference threshold (5°F min)</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF Outdoor temp sensor > thermostat setpoint</li>
      <li>AND All windows are closed</li>
      <li>THEN Send notification "Open windows for free heating"</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Rule Machine with temperature comparison</li>
      <li>Trigger: Outdoor temp rises above indoor temp + 5°F</li>
      <li>Condition: Windows closed, heating season</li>
      <li>Action: Send notification "Open windows for free heating"</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>Limited native temperature comparison</li>
      <li>Use Home Assistant or similar hub for logic</li>
      <li>Create notification through external service</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: Outdoor temperature changes</li>
      <li>Condition: Outdoor temp > Indoor temp by 5°</li>
      <li>Action: Send notification to phone</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Limited native support for complex temp comparisons</li>
      <li>Use IFTTT for notifications</li>
      <li>Or Home Assistant for logic</li>
    </ol>
  </div>
</div>

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
