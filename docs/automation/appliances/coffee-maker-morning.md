---
layout: default
title: Automatic Coffee Maker in the Morning
description: Wake up to freshly brewed coffee automatically. Smart plug method for starting coffee maker on schedule.
keywords: coffee maker automation, automatic coffee morning, morning coffee routine, smart plug coffee, scheduled coffee, wake up coffee, automatic brewing
---

# Start coffee maker in the morning

Wake up to freshly brewed coffee automatically. Start your day right with coffee ready when you need it, without stumbling to the kitchen first.

## Use cases

* **Morning Coffee Ready** - Coffee brewing when alarm goes off
* **Automatic Weekday Brewing** - Consistent work morning routine
* **Wake-Up Motivation** - Smell of coffee helps you get up
* **When Shower Ends** - Time coffee to finish as you're ready
* **Guest Accommodation** - Auto-brew when guests staying over

## Products needed

### Essential

* **Smart Plug or Smart Outlet** - Control power to coffee maker
  - Popular brands: TP-Link Kasa, Wyze, Wemo, Zigbee plugs
  - Key features: Schedule capability, reliable automation
  
* **Compatible Coffee Maker** - Must start automatically when power applied
  - **Critical:** Won't work if button must be pressed after power on
  - Simple/old coffee makers work best
  - Some programmable models work

### Optional Enhancements

* **Motion Sensor** - Start coffee when you wake up/move around
* **Smart Lights** - Coordinate with morning routine
* **Grinder** on separate smart plug for fresh-ground beans

## Setup requirements

### Test coffee maker compatibility

**Before automating, verify your coffee maker will work:**

1. Fill coffee maker with water and grounds
2. Turn coffee maker switch to "on" position  
3. Unplug it
4. Plug it back in
5. **Does it start brewing?** 
   - ✅ **YES** = Compatible! Automation will work
   - ❌ **NO** = Not compatible (requires button press)

**Compatible Coffee Maker Types:**
- Old/simple coffee makers with physical on/off switch
- Some programmable models that remember settings
- Basic drip coffee makers

**Not Compatible:**
- Coffee makers requiring button press after power on
- Models with touchscreen that resets on power loss
- Most pod-based machines (Keurig, Nespresso)

## Basic automation setup

### Night before preparation

**Every night:**
1. Fill coffee maker with water and grounds
2. Turn coffee maker switch to "on" position
3. Press physical button on smart plug to turn it OFF
4. (Turning plug off signals the automation coffee maker is ready)

### Morning automation

**Triggers:**
* 7:00 AM Monday-Friday
* OR when shower turns on
* OR when bedroom motion detected

**Conditions:**
* Smart plug is currently OFF
  - This confirms coffee maker is loaded and ready
  - Prevents turning on empty coffee maker

**Actions:**
* Turn on smart plug
* Coffee starts brewing!
* Optional: Send notification "Coffee brewing"

## Platform-Specific Examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Time is 7:00 AM
- **Conditions:** Weekdays only (Mon-Fri) AND coffee maker plug is OFF (confirms loaded and ready)
- **Action 1:** Turn on coffee maker smart plug
- **Action 2:** Send notification "Good morning! Coffee is brewing ☕"

**Triggered by shower:**

Create automation with these elements:
- **Trigger:** Bathroom shower light turns on
- **Conditions:** Morning hours (6am-10am) AND weekdays AND coffee maker plug is OFF
- **Action:** Turn on coffee maker plug

**Triggered by motion:**

Create automation with these elements:
- **Trigger:** Bedroom motion sensor activates
- **Conditions:** Morning hours (6am-9am) AND weekdays AND coffee maker plug is OFF
- **Action:** Turn on coffee maker plug

### Automatic safety shutoff

**Critical for safety:**

Create automation with these elements:
- **Trigger:** Coffee maker plug has been ON for 30 minutes
- **Action 1:** Turn off coffee maker plug
- **Action 2:** Send notification "Coffee maker auto shut-off (30 min safety timer)"

### SmartThings

Create routine:
1. **IF** Time is 7:00 AM
2. **AND** Day is Monday through Friday
3. **AND** Coffee maker plug is OFF (confirms loaded)
4. **THEN** Turn on coffee maker plug

Create safety routine:
1. **IF** Coffee maker plug has been ON for 30 minutes
2. **THEN** Turn off coffee maker plug

### Apple HomeKit

1. Create automation in Home app
2. **When:** Time is 7:00 AM
3. **Conditions:** Weekdays only
4. **Do:** Turn on coffee maker smart plug

(Note: Can't check if plug is off as condition in HomeKit)

Create second automation for shutoff:
1. **When:** Coffee maker plug turns on
2. **Wait:** 30 minutes
3. **Do:** Turn off coffee maker plug

### Alexa

Create routine:
1. **When:** Schedule (7:00 AM weekdays)
2. **Action:** Turn on coffee maker smart plug

Safety routine:
1. **When:** Coffee maker plug has been on for 30 minutes
2. **Action:** Turn off coffee maker plug

### Google Home

Create automation:
1. **Starter:** Time is 7:00 AM on weekdays
2. **Action:** Turn on coffee maker plug

## Advanced features

### Voice-activated coffee

Make coffee on demand:

Create automation triggered by voice command (e.g., Alexa actionable notification) that turns on coffee maker plug if it's currently off (loaded and ready).

Say: "Alexa, start coffee"

### Pre-warm before arrival

Start coffee when arriving home:

Create automation with these elements:
- **Trigger:** Person arrives home
- **Conditions:** Morning hours (6am-10am) AND coffee maker plug is OFF
- **Action:** Turn on coffee maker plug

### Multi-stage morning

Coordinate with other morning routines:

Create automation that runs at wake-up time:
1. Turn on coffee maker plug
2. Gradually increase bedroom light brightness (start at 10%, transition over 60 seconds)
3. Wait 5 minutes
4. Brighten lights to 100% over 30 seconds

## Alternative triggers

### Smart alarm clock integration

Start coffee when alarm dismissed:

If using phone alarm with Home Assistant, trigger coffee maker when mobile app sends alarm dismissed event.

### Presence + time

Only brew if someone home:

Add conditions to automation:
- At least one person is home
- Time is between 6am and 9am

### Weather-based

Skip on very hot days:

Add condition: Only brew if outdoor temperature is below 75°F (don't brew hot coffee when already hot outside)

## Troubleshooting

### Issue: Coffee maker doesn't start

**Causes:**
- Coffee maker incompatible (requires button press)
- Smart plug didn't turn on
- Coffee maker switch not in "on" position
- Automation didn't trigger

**Solutions:**
✅ Re-test coffee maker compatibility (unplug/plug test)
✅ Verify smart plug turns on via app manually
✅ Check coffee maker physical switch is "on"
✅ Review automation logs to see if it triggered
✅ Ensure coffee maker switch wasn't accidentally turned off
✅ Try different coffee maker model if current one incompatible

### Issue: Empty coffee maker turns on

**Causes:**
- Forgot to prepare coffee maker night before
- Smart plug already on (not turned off in prep)
- Automation has no check for "ready" state
- Weekend automation triggered

**Solutions:**
✅ Add condition: Smart plug must be OFF before turning on
✅ Create reminder notification evening before: "Prepare coffee maker"
✅ Add weekday-only condition if don't want weekend coffee
✅ Visual reminder (dashboard tile) showing coffee maker status

Create evening reminder automation:
- **Trigger:** Time is 9:00 PM
- **Condition:** Weeknights (Sun-Thu, night before weekdays)
- **Action:** Send notification "Reminder: Prepare coffee maker for tomorrow morning"

### Issue: Coffee burns or overheats

**Causes:**
- No automatic shutoff implemented
- Coffee maker left on too long
- Heating plate continues heating
- Safety timer not working

**Solutions:**
✅ **Always implement 30-minute auto-shutoff** (shown in examples)
✅ Use coffee maker with auto-shutoff feature
✅ Add notification when shutting off
✅ Test smart plug reliability
✅ Use thermal carafe coffee maker (no heating plate)
✅ Monitor with power monitoring plug (detect malfunction)

Create emergency shutoff automation:
- **Trigger:** Coffee maker plug has been ON for 45 minutes (maximum safe time)
- **Action 1:** Turn off coffee maker plug
- **Action 2:** Send high-priority notification "SAFETY: Coffee maker auto shut-off"

## Safety best practices

### ⚠️ Important Safety Rules

1. **Always use auto-shutoff automation** (30-45 minutes maximum)
2. **Never automate coffee maker without testing compatibility first**
3. **Use smart plug rated for coffee maker wattage** (typically 800-1200W)
4. **Don't leave house with coffee maker automating** (first few times)
5. **Clean coffee maker regularly** to prevent fire hazard
6. **Replace old coffee makers** - worn heating elements dangerous

### Recommended features

✅ Coffee maker with built-in auto-shutoff
✅ Smart plug with power monitoring (detect malfunctions)
✅ Multiple shutoff methods (time-based + power-based)
✅ Notifications when coffee maker turns on/off
✅ Manual override easily accessible

---

**Related automations:**
- [Morning routine automation](/automation/presence/morning-routine/)
- [Play music when shower starts](/automation/media/shower-music/)
- [Turn on bathroom fan when starting shower](/automation/climate/fan-shower/)

[← Back to appliance automations](/automation/appliances/) | [View all automations →](/automation/)
