---
layout: default
title: Dim Lights When TV Turns On - Theater Mode Automation
description: Automatically dim lights when TV turns on for better viewing experience. Complete guide with power monitoring and smart TV integration.
keywords: TV lighting automation, dim lights TV, theater mode automation, movie lighting, automatic TV lights, smart TV automation, cinema mode
---

# Dim lights when TV turns on

Enhance movie watching by automatically dimming lights when the TV turns on. Create the perfect viewing atmosphere without fumbling for light switches.

## Use cases

* **Movie Watching** - Optimize lighting for better screen visibility
* **TV Show Viewing** - Reduce glare and eye strain
* **Gaming** - Create immersive gaming environment
* **Afternoon Viewing** - Close blinds when sun hits screen
* **Theater Experience** - Automatic cinema mode in your living room

## Products needed

### Essential

**Option 1: Power monitoring (most universal)**
* **Smart Plug with Power Monitoring** - Measure TV power consumption
  - Popular brands: TP-Link Kasa, Shelly, Zigbee power monitoring plugs
  - Key features: Real-time power measurement, relay control
  
**Option 2: Smart TV integration (more reliable)**
* **Smart TV** with platform integration
  - Compatible: Chromecast, Fire TV, Roku, Apple TV, Samsung, LG
  - Platform integration: Home Assistant, SmartThings

**Plus:**
* **Smart Lights or Light Switches** - Dimmable lights
  - Popular brands: Philips Hue, LIFX, Lutron, Inovelli
* **Smart Blinds** (optional) - For daytime glare control

### Optional enhancements

* **RGB Bias Lighting** - Colored LED strip behind TV
* **Motion Sensor** - Pause dimming if someone walking around
* **Voice Control** - Manual theater mode activation

## Basic automation setup

### Using power monitor

**Triggers:**
* Smart plug power consumption rises above 50 watts (TV turns on)

**Conditions:**
* Time between sunset and sunrise (optional - different daytime behavior)
* OR anytime for consistent behavior

**Actions:**
* Dim lights to 10%
* OR turn lights off completely
* Optional: Close blinds/curtains

### Using smart TV

**Triggers:**
* TV turns on
* OR specific app opens (Netflix, Disney+, etc.)

**Conditions:**
* Time is between 6 PM and midnight (movie hours)
* Optional: Only for video apps (not menu/settings)

**Actions:**
* Dim lights to 10-20%
* Close blinds if daytime

## Platform-specific examples

### Home Assistant

**Power monitoring method:**

Create automation with these elements:
- **Trigger:** TV plug power consumption rises above 50W for 5 seconds
- **Condition:** Time is after sunset and before sunrise
- **Actions:**
  - Dim living room lights to 10% brightness
  - Use 2-second smooth transition

**Smart TV integration:**

Create automation with these elements:
- **Trigger:** TV media player state changes to 'playing'
- **Condition:** Time is between 6 PM and midnight
- **Actions:**
  - Dim living room lights to 15% brightness with 3-second transition
  - Close living room blinds

**Reverse automation (lights on when TV off):**

Create automation to restore lights:
- **Trigger:** TV plug power drops below 10W for 2 minutes
- **Condition:** TV mode is currently active
- **Actions:**
  - Restore lights to 50% brightness
  - Deactivate TV mode flag

### SmartThings

Create routine using power monitoring:
1. **IF** TV smart plug power above 50W for 5 seconds
2. **AND** Time is after sunset
3. **THEN** Set living room lights to 10%
4. **THEN** Close blinds

### Apple HomeKit

1. Create automation in Home app
2. **When:** TV (power monitor) power above 50W
3. **Conditions:** Time after sunset
4. **Do:** 
   - Dim lights to 10%
   - Close blinds

### Alexa

Create routine:
1. **When:** Smart Home device (TV plug) power above 50W
2. **Add condition:** Time after 6:00 PM
3. **Action:** Set lights to 10% brightness
4. **Action:** Close smart blinds

### Google Home

Create automation:
1. **Starter:** TV smart plug power above 50 watts
2. **Condition:** Time after 6:00 PM
3. **Action:** Dim living room lights to 10%

## Advanced features

### Content-aware lighting

Different content types get different lighting:

Create automation triggered by TV app changes with conditional logic:
- **Movie mode (Netflix, Disney+, Plex):** 5% brightness, warm white, close blinds
- **TV show mode (Hulu, YouTube TV):** 15% brightness
- **Gaming mode (HDMI inputs):** 25% brightness, activate RGB bias lighting with dynamic effect
- **Sports mode (ESPN):** 30% brightness

Use app name or input source to determine content type and adjust accordingly.

### Daytime glare control

Different behavior for daytime vs nighttime:

Create two automations:

**Daytime (sunrise to sunset):**
- Close blinds to reduce glare
- Keep lights at 40% (more light needed during day)

**Nighttime (after sunset):**
- Dim lights significantly to 10%
- Blinds already closed or less critical

### Bias lighting synchronization

Sync LED strip behind TV:
- Dim main room lights to 5%
- Activate TV backlight LED strip at 50% brightness
- Set warm white/orange color (RGB: 255, 140, 60)

### Pause dimming for movement

Don't dim if people are moving around:

Add condition: No motion detected in last 5 minutes before dimming lights

## Troubleshooting

### Issue: Lights dim when TV menu on

**Causes:**
- Power monitoring can't differentiate between menu and playback
- Trigger threshold too low
- No delay to ensure actually watching content

**Solutions:**
✅ Increase power threshold (try 80W instead of 50W)
✅ Add longer delay (30 seconds) before dimming
✅ Use smart TV integration instead - detect 'playing' state
✅ Add condition: Only between certain hours (6 PM - midnight)
✅ Use app-specific triggers (Netflix/Disney+ only)

### Issue: Lights don't restore when TV off

**Causes:**
- Power drops gradually, not instantly
- No reverse automation created
- Previous brightness not saved
- TV on standby still drawing power

**Check:**
- ✅ Create separate "restore lights" automation (shown in examples)
- ✅ Use lower power threshold for "off" detection (below 10W)
- ✅ Add 2-minute delay to ensure TV actually off (not just paused)
- ✅ Save previous light state before dimming
- ✅ Test actual TV power consumption when off (may be 5-15W)

**Fix with state saving:**
- When dimming: Create scene snapshot of current light state, then dim
- When restoring: Activate saved scene to restore exact previous brightness

### Issue: Smart TV state inaccurate

**Causes:**
- TV integration losing connection
- TV firmware outdated
- Network issues
- Platform doesn't support TV model well

**Solutions:**
✅ Update TV firmware to latest version
✅ Check TV integration in platform (reconnect if needed)
✅ Use power monitoring as backup method
✅ Restart hub/integration
✅ Check TV is on same network as hub
✅ Use Cast device (Chromecast) instead of TV direct integration

---

**Related automations:**
- [Away mode automation](/automation/presence/away-mode/)
- [Bedtime routine automation](/automation/presence/bedtime-routine/)
- [Speaker volume presets](/automation/media/speaker-volume-presets/)

<div class="page-navigation">
  <a href="/automation/media/">← Back to Media Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
