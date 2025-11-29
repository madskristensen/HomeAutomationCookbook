---
layout: default
title: Maintain Room Temperature with Smart Heater - Zone Heating
description: Use a smart plug and temperature sensor to maintain comfortable temperature in cold rooms. Complete guide with safety considerations.
keywords: room heater automation, zone heating automation, space heater control, temperature sensor automation, smart plug heater, supplemental heating, cold room heating
---

# Maintain temperature using a room heater

In colder rooms, add supplemental heating to maintain comfortable temperature automatically. Perfect for rooms that stay consistently cold or need different temperatures than the rest of the house.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Bedrooms & Living</h4>
    <ul>
      <li><strong>Cold Bedroom</strong> - Room gets too cold during the night</li>
      <li><strong>Kids' Room Warmer</strong> - Children want warmer bedroom than rest of house</li>
      <li><strong>Guest Room</strong> - Maintain comfortable temperature only when occupied</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Workspaces</h4>
    <ul>
      <li><strong>Garage Office</strong> - Converted workspace needs extra heat</li>
      <li><strong>Basement Room</strong> - Lower levels stay consistently cold</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Temperature Sensor</strong>
      <div class="product-details">
        Popular brands: Aqara, Sonoff, SmartThings, Zigbee sensors<br>
        Accurate temperature • Fast updates • Good battery life
      </div>
    </div>
    
    <div class="product-item">
      <strong>Room Heater</strong>
      <div class="product-details">
        Electric space heater with simple on/off switch<br>
        UL, ETL, or CE certified • Tip-over protection • Overheat protection
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Plug</strong>
      <div class="product-details">
        Popular brands: TP-Link Kasa, Wyze, Zigbee plugs<br>
        Must handle 1500W heater • Power monitoring recommended
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Contact Sensor</strong>
      <div class="product-details">
        On window for safety (prevent running with window open)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Presence Sensor</strong>
      <div class="product-details">
        Only heat when room is occupied
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF room temperature < 68°F
THEN turn on space heater
ELSE IF temperature > 70°F
THEN turn off space heater</div>

<div class="info-box">
  <strong>⚠️ Critical Safety</strong>
  <ul>
    <li>Never operate heater with window open</li>
    <li>Use only certified heaters (UL, ETL, CE)</li>
    <li>Ensure 3 feet clearance on all sides</li>
    <li>Implement maximum runtime shutoff (8 hours)</li>
    <li>Always check window sensor in conditions</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Part 1: Turn On When Cold</h4>
    <strong>Trigger:</strong> Room temperature drops below 68°F (20°C)<br>
    <strong>Conditions:</strong> Window is closed (CRITICAL) • Time between 6 PM - 8 AM<br>
    <strong>Action:</strong> Turn on smart plug with room heater
  </div>
  
  <div class="setup-step">
    <h4>Part 2: Turn Off When Warm</h4>
    <strong>Trigger:</strong> Room temperature rises above 70°F (21°C)<br>
    <strong>Conditions:</strong> None (always turn off when warm enough)<br>
    <strong>Action:</strong> Turn off smart plug with room heater
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Bedroom temp below 68°F for 5 min</li>
      <li>Condition: Window closed AND time 6 PM - 8 AM</li>
      <li>Action: Turn on heater smart plug</li>
      <li>Trigger 2: Temp above 70°F for 2 min</li>
      <li>Action 2: Turn off heater plug</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF Bedroom temp sensor below 68°F</li>
      <li>AND Bedroom window is closed</li>
      <li>AND Time is 6:00 PM - 8:00 AM</li>
      <li>THEN Turn on bedroom heater plug</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Bedroom temperature falls below 68°F</li>
      <li>Conditions: Window closed, Time 6 PM - 8 AM</li>
      <li>Do: Turn on heater smart plug</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: Temperature sensor below 68°F</li>
      <li>Condition: Window closed, Time 6 PM - 8 AM</li>
      <li>Action: Turn on heater smart plug</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: Temperature sensor below 68°F</li>
      <li>Condition: Window closed, Time 6 PM - 8 AM</li>
      <li>Action: Turn on heater smart plug</li>
    </ol>
  </div>
</div>

## Advanced features

### Presence-based heating

Only run heater when room is occupied:

Create automation with these elements:
- **Trigger:** Bedroom temperature below 68°F
- **Conditions:**
  - Window is closed
  - Room is occupied (motion sensor active OR presence sensor detects person)
- **Action:** Turn on heater

### Pre-warm before bedtime

Start heating room before typical bedtime:

Create automation with these elements:
- **Trigger:** Time is 9:00 PM
- **Conditions:**
  - Bedroom temperature below 68°F
  - Window is closed
- **Action:** Turn on heater

### Smart scheduling

Different temperatures for different times:

Create automation triggered by temperature change:
- **Bedtime (10 PM - 7 AM):** Keep warm 68-70°F
  - If temp below 68°F AND window closed: Turn on heater
- **When warm enough (above 70°F):** Turn off heater

Use conditional logic based on time of day and current temperature.

### Power failure recovery

Don't automatically restart heater after power outage:

Create automation triggered when system starts/restarts:
- **Action:** Turn off heater smart plug (ensures safe state after power restoration)

## Safety considerations

### ⚠️ Critical Safety Rules

**1. Never operate heater with window open**
- Risk of carbon monoxide (for fuel-based heaters)
- Massive energy waste
- Always check window sensor in automation conditions

**2. Use certified heaters only**
- Look for UL, ETL, or CE certification
- Must have tip-over protection
- Must have overheat protection
- Avoid old or damaged heaters

**3. Don't cover heater**
- Ensure 3 feet clearance on all sides
- Never place under desks or in closets
- Keep away from curtains, bedding, furniture

**4. Monitor for faults**
- Send alert if heater runs more than 8 hours continuously
- Track power consumption to detect issues
- Stop automation if unusual behavior detected

**5. Power monitoring recommended**
- Track watts to detect issues (normal: 1500W, problem: significantly different)
- Alert if power consumption abnormal
- Automatic shutoff if power exceeds safe levels

### Recommended safety automations

**Window open safety:**
Create emergency shutoff automation:
- **Trigger:** Bedroom window opens
- **Condition:** Heater is currently on
- **Actions:**
  - Turn off heater immediately
  - Send safety alert notification: "SAFETY: Heater turned off - window opened"

**Maximum Runtime:**
Always implement maximum runtime shutoff (shown in examples above).

**Away Mode:**
Turn off all heaters when house is in Away mode.

## Troubleshooting

### Issue: Room never reaches target temperature

**Causes:**
- Heater undersized for room
- Room has poor insulation
- Outdoor temperature extremely cold
- Heater on smart plug that can't supply enough power
- Temperature sensor placement incorrect

**Solutions:**
✅ Calculate room heating requirements (typically 10W per sq ft)
✅ Check heater wattage matches or exceeds room needs
✅ Verify smart plug rated for heater wattage (usually need 15A/1800W capacity)
✅ Improve room insulation (door draft stopper, window sealing)
✅ Lower target temperature expectations in extreme cold
✅ Move temperature sensor away from heater, windows, doors
✅ Consider larger heater or multiple heaters

### Issue: Heater cycles on/off too frequently

**Causes:**
- Temperature thresholds too close together (68°F off, 69°F on)
- Temperature sensor too close to heater
- Rapid temperature fluctuations in room
- No delay in automation triggers

**Check:**
- ✅ Increase temperature deadband (66°F on, 70°F off = 4° difference)
- ✅ Move sensor away from heater - at least 6-10 feet
- ✅ Add "for: 5 minutes" delay to both on and off triggers
- ✅ Use slower-responding sensor position (avoid direct airflow)

**Fix:**
Modify trigger with:
- Lower threshold: Turn on at 66°F instead of 68°F
- Add 5 minute delay: Temperature must stay below threshold for 5 minutes before turning on

### Issue: Smart plug turns off unexpectedly

**Causes:**
- Smart plug overheating
- Heater drawing too much power
- Smart plug not rated for heater
- Network connectivity issues
- Automation or safety feature triggering

**Solutions:**
✅ Verify smart plug specifications: Must support 15A / 1500-1800W
✅ Check for overheating: Touch plug after running - should be warm not hot
✅ Use in-wall smart outlet instead of plug (better heat dissipation)
✅ Review automation logs: Check what turned off the plug
✅ Check heater actual wattage (use kill-a-watt meter)
✅ Don't daisy-chain plugs or use extension cords
✅ Replace smart plug if overheating or failing

---

**Related automations:**
- [Stop thermostat when windows open](/automation/climate/thermostat-windows-open/)
- [Turn on bathroom fan when starting shower](/automation/climate/fan-shower/)
- [Bedtime routine automation](/automation/presence/bedtime-routine/)

<div class="page-navigation">
  <a href="/automation/climate/">← Back to Climate Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
