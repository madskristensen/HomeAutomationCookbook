---
layout: automation
title: Activate Air Purifier When Air Quality Drops - Health Automation
description: Automatically run your air purifier when indoor air quality drops below healthy levels. Monitor AQI and PM2.5 for cleaner air.
keywords: air quality automation, air purifier control, AQI sensor automation, PM2.5 automation, indoor air quality, automatic air purifier, health automation, allergy automation
---

# Clean the air when air quality drops

Indoor air quality fluctuates throughout the day from cooking, outdoor pollution, pet dander, and more. Automate air purification when quality drops below healthy thresholds for better health and comfort.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Indoor Sources</h4>
    <ul>
      <li><strong>Cooking Smoke</strong> - Air quality drops when cooking creates smoke or strong odors</li>
      <li><strong>Pet Odors</strong> - Dander and smells accumulating in living spaces</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>External Factors</h4>
    <ul>
      <li><strong>Seasonal Allergies</strong> - Outdoor pollen affecting indoor air quality</li>
      <li><strong>Poor Outdoor AQI</strong> - Wildfire smoke or pollution entering home</li>
      <li><strong>Health Maintenance</strong> - Proactive air quality management for respiratory health</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment - Option 1: Smart Air Purifier</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Air Quality Sensor</strong>
      <div class="product-details">
        Popular brands: Awair, IQAir, Aqara, PurpleAir<br>
        PM2.5 detection • WiFi connectivity • Measures AQI or PM2.5
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Air Purifier</strong>
      <div class="product-details">
        Brands: Coway, Levoit, Dyson, Winix<br>
        WiFi-enabled OR regular purifier on smart plug (simpler option)
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Essential Equipment - Option 2: HVAC-Based</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Air Quality Sensor + Smart Thermostat</strong>
      <div class="product-details">
        Brands: Ecobee, Honeywell<br>
        Smart thermostat with air filter/circulation mode
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Multiple Sensors</strong>
      <div class="product-details">
        Track air quality in different rooms
      </div>
    </div>
    
    <div class="product-item">
      <strong>Outdoor Air Quality Monitor</strong>
      <div class="product-details">
        Compare indoor vs outdoor conditions
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF air quality poor (AQI > 100)
THEN turn on air purifier to high
AND send notification "Poor air quality detected"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Air quality (AQI) drops below 35</li>
      <li>OR PM2.5 concentration above 50 μg/m³</li>
      <li>OR VOC (Volatile Organic Compounds) exceeds threshold</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>Note:</strong> Air quality is health-critical and should be addressed immediately<br>
    <strong>Optional:</strong> Only during occupied hours
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on air purifier at high speed</li>
      <li>OR activate HVAC fan with filter</li>
      <li>Optional: Close smart windows/vents</li>
      <li>Optional: Send notification with current air quality reading</li>
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
        <span class="step-label">Trigger</span>
        <span class="step-content">Air quality sensor drops below 35 AQI</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on air purifier at 100%, send notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Alternative:</strong> Use PM2.5 sensor above 50 μg/m³
        </div>
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
        <span class="step-label">IF</span>
        <span class="step-content">Air quality sensor reports AQI below 35</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on air purifier smart plug, send notification</span>
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
        <span class="step-label">Trigger</span>
        <span class="step-content">AQI sensor drops below 35</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on air purifier at high, send notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with air quality device
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
        <span class="step-label">When</span>
        <span class="step-content">Air quality sensor detects poor air quality</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">AQI below threshold (if supported)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on air purifier</span>
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
        <span class="step-label">When</span>
        <span class="step-content">Air quality sensor value below 35 AQI</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on air purifier, send notification</span>
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
        <span class="step-label">Starter</span>
        <span class="step-content">Air quality sensor detects poor quality</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on air purifier, announce status</span>
      </div>
    </div>
  </div>
</div>

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
- [Away mode automation](/automation/daily-routines/away-mode/)

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
