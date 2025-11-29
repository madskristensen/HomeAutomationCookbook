---
layout: default
title: Maintain Room Temperature with Smart Heater - Zone Heating
description: Use a smart plug and temperature sensor to maintain comfortable temperature in cold rooms. Complete guide with safety considerations.
keywords: room heater automation, zone heating automation, space heater control, temperature sensor automation, smart plug heater, supplemental heating, cold room heating
---

# Maintain temperature using a room heater

In colder rooms, add supplemental heating to maintain comfortable temperature automatically. Perfect for rooms that stay consistently cold or need different temperatures than the rest of the house.

## Use cases

* **Cold Bedroom** - Room gets too cold during the night
* **Kids' Room Warmer** - Children want warmer bedroom than rest of house
* **Garage Office** - Converted workspace needs extra heat
* **Basement Room** - Lower levels stay consistently cold
* **Guest Room** - Maintain comfortable temperature only when occupied

## Products needed

### Essential

* **Temperature Sensor** - Room-specific temperature monitoring
  - Popular brands: Aqara, Sonoff, SmartThings, Zigbee sensors
  - Key features: Accurate temperature, fast updates, good battery life
  
* **Room Heater** - Electric space heater
  - Must have simple on/off switch (stays in "on" position when power applied)
  - Certified safety: UL, ETL, or CE certification required
  - Features: Tip-over protection, overheat protection
  
* **Smart Plug** - Control power to heater
  - Popular brands: TP-Link Kasa, Wyze, Zigbee plugs
  - Requirements: Must handle heater wattage (usually 1500W)
  - Features: Power monitoring recommended

### Optional enhancements

* **Contact Sensor** - On window for safety (prevent running with window open)
* **Presence Sensor** - Only heat when room is occupied
* **Smart Outlet** - In-wall alternative to smart plug

## Basic automation setup

### Part 1: Turn on heater when cold

**Triggers:**
* Room temperature drops below 68°F (20°C)

**Conditions:**
* Window is closed (safety - critical condition)
* Time is between 6 PM and 8 AM (typical heating hours)

**Actions:**
* Turn on smart plug with room heater

### Part 2: Turn off heater when warm

**Triggers:**
* Room temperature rises above 70°F (21°C)

**Conditions:**
* None (always turn off when warm enough)

**Actions:**
* Turn off smart plug with room heater

## Platform-specific examples

### Home Assistant

**Turn on when cold:**

Create automation with these elements:
- **Trigger:** Bedroom temperature drops below 68°F for 5 minutes
- **Conditions:**
  - Window is closed (critical safety check)
  - Time is between 6 PM and 8 AM (typical cold hours)
- **Action:** Turn on heater smart plug

**Turn off when warm:**

Create automation with these elements:
- **Trigger:** Bedroom temperature rises above 70°F for 2 minutes
- **Action:** Turn off heater smart plug

**With power monitoring safety:**

Create safety automation:
- **Trigger:** Heater plug has been on for 8 hours continuously
- **Actions:**
  - Turn off heater plug
  - Send notification: "Bedroom heater auto shut-off after 8 hours" as safety alert

### SmartThings

Create routine for turning on:
1. **IF** Bedroom temperature sensor reports below 68°F
2. **AND** Bedroom window is closed
3. **AND** Time is between 6:00 PM and 8:00 AM
4. **THEN** Turn on bedroom heater smart plug

Create routine for turning off:
1. **IF** Bedroom temperature sensor reports above 70°F
2. **THEN** Turn off bedroom heater smart plug

### Apple HomeKit

**Turn On Automation:**
1. Create automation in Home app
2. **When:** Bedroom temperature falls below 68°F
3. **Conditions:** 
   - Window is closed
   - Time between 6:00 PM - 8:00 AM
4. **Do:** Turn on heater smart plug

**Turn Off Automation:**
1. **When:** Bedroom temperature rises above 70°F
2. **Do:** Turn off heater smart plug

### Alexa

Create routine for turning on:
1. **When:** Smart Home sensor detects temperature below 68°F
2. **Add condition:** Window sensor is closed
3. **Add condition:** Time between 6:00 PM - 8:00 AM
4. **Action:** Turn on heater smart plug

### Google Home

Create automation for turning on:
1. **Starter:** Temperature sensor below 68°F
2. **Condition:** Window closed and time between 6 PM - 8 AM
3. **Action:** Turn on heater smart plug

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

[← Back to climate automations](/automation/climate/) | [View all automations →](/automation/)
