---
layout: default
title: Resume Thermostat When All Windows Close - Climate Control
description: Automatically resume heating or cooling when all windows and doors are closed. Smart climate control that adapts to your behavior.
keywords: thermostat resume automation, windows closed automation, HVAC restart, climate control automation, automatic thermostat, restore climate control, smart HVAC
---

# Start thermostat when windows and doors are closed

Once all windows and doors are closed, it's time to resume climate control. This automation restores your HVAC system to continue heating or cooling your home.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Automatic Comfort</h4>
    <ul>
      <li><strong>After Airing Out</strong> - All windows and doors have been closed after bringing in fresh air</li>
      <li><strong>Resume Normal Comfort</strong> - Restore temperature control automatically</li>
      <li><strong>Seamless Experience</strong> - Climate control adapts without manual intervention</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Efficiency</h4>
    <ul>
      <li><strong>Energy Optimization</strong> - Don't waste time with HVAC off when windows are closed</li>
      <li><strong>Return from Nice Weather</strong> - Automatically resume when outdoor conditions change</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Thermostat</strong>
      <div class="product-details">
        Popular brands: Nest, Ecobee, Honeywell, Sensi<br>
        WiFi or Zigbee enabled • API control • Mode restoration capability
      </div>
    </div>
    
    <div class="product-item">
      <strong>Contact Sensors</strong>
      <div class="product-details">
        Popular brands: Aqara, Wyze, SmartThings, Ring<br>
        Must match sensors used in "stop thermostat" automation • Cover all monitored windows/doors
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Temperature Sensor</strong>
      <div class="product-details">
        Verify indoor temp before resuming (safety check)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Variable/Helper</strong>
      <div class="product-details">
        Store previous thermostat state for accurate restoration
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF all windows closed
THEN restore thermostat to previous mode
AND send notification "Climate control resumed"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Any window or door closes</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>ALL windows and doors are closed:</strong> Critical condition<br>
    <strong>Thermostat is currently off</strong><br>
    <strong>Optional:</strong> Indoor temperature outside comfortable range
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on thermostat</li>
      <li>Restore previous mode (heat/cool/auto)</li>
      <li>Optional: Restore previous temperature setpoint</li>
      <li>Optional: Send notification "Climate control resumed"</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Any window or door closes</li>
      <li>Condition: ALL windows/doors closed AND thermostat is "off"</li>
      <li>Action: Restore thermostat to saved previous mode</li>
      <li>Tip: Use group sensor for simplified "all closed" check</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF Living room window closes</li>
      <li>AND ALL other windows/doors are closed</li>
      <li>AND Thermostat mode is "Off"</li>
      <li>THEN Set thermostat mode to "Auto"</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Any window or door closes</li>
      <li>Conditions: All windows/doors closed, Thermostat is off</li>
      <li>Do: Turn on thermostat to Auto mode</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: Smart Home sensor closes</li>
      <li>Condition: All other windows/doors closed, Thermostat "Off"</li>
      <li>Action: Set thermostat to Auto mode</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: Window sensor closes</li>
      <li>Condition: All windows and doors are closed</li>
      <li>Action: Set thermostat to Heat-Cool mode</li>
    </ol>
  </div>
</div>

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

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
