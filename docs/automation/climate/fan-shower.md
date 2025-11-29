---
layout: default
title: Turn On Bathroom Fan When Starting Shower - Climate Automation
description: Automatically turn on your bathroom fan when starting a shower. Guide covers multiple trigger methods including lights, humidity sensors, and door contacts.
keywords: bathroom fan automation, shower fan control, humidity sensor automation, automatic fan, bathroom ventilation, smart fan switch, prevent mirror fog, mold prevention
---

# Turn on bathroom fan when starting shower

Remembering to turn on the ceiling fan when taking a shower early in the morning isn't always easy. Automate it to prevent mirror fog, reduce humidity, and improve air quality without thinking about it.

## Use cases

* **Morning Shower** - Automatically turn on fan when starting your morning shower
* **Prevent Mirror Fog** - Keep bathroom mirrors clear during showers
* **Humidity Control** - Reduce excess moisture to prevent mold and mildew
* **Bathroom Ventilation** - Improve air quality automatically
* **Multi-User Households** - Everyone gets fan benefits without remembering

## Products needed

### Essential

* **Smart Fan Switch** - WiFi or Zigbee ceiling fan control
  - Popular brands: Lutron, GE, Leviton, Inovelli
  - Key features: Works with existing fan, load rating sufficient for fan motor

**PLUS one of these trigger options:**

* **Option 1: Smart Light Switch** - Trigger when shower lights turn on
  - Easiest method if you have smart shower lights
  
* **Option 2: Contact Sensor** - Trigger when shower door opens
  - Best for glass shower enclosures with door
  
* **Option 3: Humidity Sensor** - Trigger when humidity rises
  - Most accurate but requires sensor placement
  - Options: Aqara, Sonoff, Zigbee sensors

### Optional enhancements

* **Multi-Sensor** - Combines temperature, humidity, and motion for advanced control
* **Smart Speaker** - Announce "Fan turned on" or play shower music

## Basic automation setup

### Triggers (choose one method)

**Method 1: Light-based**
* Shower lights turn on

**Method 2: Door sensor**
* Shower door opens (contact sensor)

**Method 3: Humidity-based**
* Bathroom humidity rises above 75%

### Conditions (optional)

* **Time-Based:** Only between 5 AM and 11 PM (quiet hours at night)
* **Home Mode:** Only when someone is home

### Actions

* Turn on bathroom fan switch
* Optional: Set fan to specific speed if multi-speed fan
* Optional: Send notification "Bathroom fan activated"

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Shower lights turn on
- **Condition:** Time is between 5 AM and 11 PM
- **Action:** Turn on bathroom fan switch

**Humidity-based example:**

Create automation with these elements:
- **Trigger:** Bathroom humidity rises above 75%
- **Action:** Turn on bathroom fan

### SmartThings

Create routine:
1. **IF** Shower lights turn on
2. **AND** Time is between 5:00 AM and 11:00 PM
3. **THEN** Turn on bathroom fan switch

### Apple HomeKit

1. Create automation in Home app
2. **When:** Shower light turns on
3. **Conditions:** Time is between 5:00 AM and 11:00 PM
4. **Do:** Turn on bathroom fan

### Alexa

Create routine:
1. **When:** Smart Home device (shower light) turns on
2. **Add condition:** Time between 5:00 AM - 11:00 PM
3. **Action:** Turn on bathroom fan

### Google Home

Create automation:
1. **Starter:** Shower light turns on
2. **Condition:** Time between 5:00 AM - 11:00 PM
3. **Action:** Turn on bathroom fan

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

[← Back to climate automations](/automation/climate/) | [View all automations →](/automation/)
