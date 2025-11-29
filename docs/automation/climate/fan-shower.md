---
layout: default
title: Turn On Bathroom Fan When Starting Shower - Climate Automation
description: Automatically turn on your bathroom fan when starting a shower. Guide covers multiple trigger methods including lights, humidity sensors, and door contacts.
keywords: bathroom fan automation, shower fan control, humidity sensor automation, automatic fan, bathroom ventilation, smart fan switch, prevent mirror fog, mold prevention
---

# Turn on bathroom fan when starting shower

Remembering to turn on the ceiling fan when taking a shower early in the morning isn't always easy. Automate it to prevent mirror fog, reduce humidity, and improve air quality without thinking about it.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Convenience & Comfort</h4>
    <ul>
      <li><strong>Morning Shower</strong> - Automatically turn on fan when starting your morning shower</li>
      <li><strong>Prevent Mirror Fog</strong> - Keep bathroom mirrors clear during showers</li>
      <li><strong>Multi-User Households</strong> - Everyone gets fan benefits without remembering</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Health & Safety</h4>
    <ul>
      <li><strong>Humidity Control</strong> - Reduce excess moisture to prevent mold and mildew</li>
      <li><strong>Bathroom Ventilation</strong> - Improve air quality automatically</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Fan Switch</strong>
      <div class="product-details">
        Popular brands: Lutron, GE, Leviton, Inovelli<br>
        WiFi or Zigbee • Works with existing fan • Load rating sufficient for fan motor
      </div>
    </div>
    
    <div class="product-item">
      <strong>Trigger Option (choose one)</strong>
      <div class="product-details">
        <strong>Smart Light Switch:</strong> Trigger when shower lights turn on (easiest method)<br>
        <strong>Contact Sensor:</strong> Trigger when shower door opens (best for glass enclosures)<br>
        <strong>Humidity Sensor:</strong> Trigger when humidity rises (most accurate - Aqara, Sonoff, Zigbee)
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Multi-Sensor</strong>
      <div class="product-details">
        Combines temperature, humidity, and motion for advanced control
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Speaker</strong>
      <div class="product-details">
        Announce "Fan turned on" or play shower music
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF shower lights turn on
THEN turn on bathroom fan</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers (choose one method)</h4>
    <strong>Method 1 - Light-based:</strong> Shower lights turn on<br>
    <strong>Method 2 - Door sensor:</strong> Shower door opens (contact sensor)<br>
    <strong>Method 3 - Humidity-based:</strong> Bathroom humidity rises above 75%
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>Time-Based:</strong> Only between 5 AM and 11 PM (quiet hours at night)<br>
    <strong>Home Mode:</strong> Only when someone is home
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on bathroom fan switch</li>
      <li>Optional: Set fan to specific speed if multi-speed fan</li>
      <li>Optional: Send notification "Bathroom fan activated"</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Shower lights turn on</li>
      <li>Condition: Time is between 5 AM and 11 PM</li>
      <li>Action: Turn on bathroom fan switch</li>
      <li>Humidity option: Trigger when humidity rises above 75%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF Shower lights turn on</li>
      <li>AND Time is between 5:00 AM and 11:00 PM</li>
      <li>THEN Turn on bathroom fan switch</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Shower light turns on</li>
      <li>Conditions: Time is between 5:00 AM and 11:00 PM</li>
      <li>Do: Turn on bathroom fan</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: Shower light turns on</li>
      <li>Condition: Time between 5:00 AM - 11:00 PM</li>
      <li>Action: Turn on bathroom fan</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: Shower light turns on</li>
      <li>Condition: Time between 5:00 AM - 11:00 PM</li>
      <li>Action: Turn on bathroom fan</li>
    </ol>
  </div>
</div>

## Advanced features

### Automatic fan shutoff

Turn off the fan automatically after the shower ends:

Create automation with these elements:
- **Trigger:** Shower lights turn off for 10 minutes
- **Action:** Turn off bathroom fan

**Humidity-based shutoff:**

Turn off when humidity returns to normal:
- **Trigger:** Bathroom humidity drops below 60% for 5 minutes
- **Condition:** Fan is currently on
- **Action:** Turn off bathroom fan

### Bonus automations

Since your smart home now knows when you're showering:

* **Play Music** - Start shower playlist on bathroom speaker
* **Flash Lights** - Alert you when doorbell rings (can't hear over shower)
* **Lock Front Door** - Secure home while you're in the shower
* **Adjust Thermostat** - Increase bathroom temperature slightly for comfort

## Troubleshooting

### Issue: Fan doesn't turn on

**Causes:**
- Smart fan switch not responding
- Trigger not detecting shower start
- Automation disabled or has errors
- Fan physical switch is off

**Solutions:**
✅ Test fan switch manually through app - verify it controls fan
✅ Check automation triggers - simulate shower start and watch logs
✅ Verify automation is enabled in your platform
✅ Ensure physical fan switch (if separate) is in "on" position
✅ Check fan switch load rating matches fan motor requirements

### Issue: Fan turns on at wrong times

**Causes:**
- Multiple triggers firing unexpectedly
- Humidity sensor triggered by other sources (hot bath, steam from cooking)
- Time conditions not set properly
- Contact sensor detecting wrong door/window

**Check:**
- ✅ Review automation logs to see what triggered activation
- ✅ Add time-based conditions to limit activation hours
- ✅ Increase humidity threshold if too sensitive (try 80% instead of 75%)
- ✅ Verify contact sensor is only on shower door, not bathroom door

**Fix:**
- Add delay: Only trigger if condition persists for 2-3 minutes
- Use multiple conditions: Light ON + Humidity rising + Door closed
- Set proper time restrictions: Only during typical shower hours

### Issue: Fan doesn't turn off

**Causes:**
- Auto-off automation not created or not working
- Humidity not dropping (ventilation issue)
- Physical switch turned on manually (bypassing automation)

**Solutions:**
✅ Create separate automation for fan shutoff (see Advanced Features)
✅ Increase shutoff delay if humidity drops slowly (15-20 minutes)
✅ Check actual bathroom ventilation - fan may need cleaning or is undersized
✅ Add manual override: Physical button press overrides automation
✅ Set maximum run time: Turn off after 30 minutes regardless

---

**Related automations:**
- [Play music when shower starts](/automation/media/shower-music/)
- [Morning routine automation](/automation/presence/morning-routine/)
- [Maintain room temperature with smart heater](/automation/climate/room-heater-maintain-temp/)

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
