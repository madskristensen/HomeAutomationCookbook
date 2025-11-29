---
layout: default
title: Disable Automations When Door is Closed - Smart Override System
description: Learn how to prevent motion sensor lights from turning off when bathroom or bedroom doors are closed. Complete guide with door sensor override logic.
keywords: disable automation door closed, bathroom door sensor, automation override, door sensor logic, prevent lights turning off
---

# Disable automations when door is closed

Prevent frustration when motion-based lighting turns off while you're sitting still in the bathroom or bedroom. This automation uses a door sensor to intelligently override motion timeout behavior.

## The problem

**Motion sensors can't detect stationary people:**
- Sitting on toilet
- Taking a shower
- Lying in bed reading
- Working at desk

**Result:** Lights turn off unexpectedly, leaving you in the dark.

## The solution

Use a door sensor to override the auto-off behavior:
- **Door closed** = Someone is inside, keep lights on
- **Door open** = Room is empty (after motion timeout), safe to turn off lights

## Use cases

* **Bathroom** - People sitting still on toilet or in shower
* **Bedroom** - Guest room during naps or sleep
* **Home office** - Working at computer without much movement
* **Media room** - Watching movies in reclined position
* **Reading nook** - Sitting still while reading

## Products needed

* **Contact sensor** - Mounted on door and frame
* **Existing motion sensor** - Already installed for lights
* **Smart light** - Switch or bulb

### Platform requirements

This automation requires **variables or virtual switches**, supported by:

- ✅ Home Assistant
- ✅ SmartThings (with SharpTools or custom)
- ✅ Hubitat
- ✅ HomeSeer
- ⚠️ Alexa (limited - use workarounds)
- ⚠️ Google Home (limited - use workarounds)
- ⚠️ Apple HomeKit (requires Homebridge for full functionality)

## Automation setup

### Scenario 1: Bathroom (keep lights on when door closed)

Modify your existing "turn off lights after motion stops" automation:

#### Original automation (problem)
- **Trigger:** No motion for 5 minutes
- **Action:** Turn off bathroom light
- **Issue:** Turns off while someone is sitting still inside

#### Improved automation (solution)
- **Trigger:** No motion for 5 minutes
- **Condition:** Door is OPEN (not closed)
- **Action:** Turn off bathroom light

**Logic:** Only turn off lights if:
1. No motion detected for 5 minutes AND
2. Door is open (meaning no one is inside)

### Scenario 2: Guest room (delay after entry)

Prevent lights from turning on automatically when guests are resting:
- **Trigger:** Guest room motion detected
- **Condition:** Door has been open for 5+ minutes
- **Action:** Turn on guest room light

**Logic:** If guest leaves room and returns within 5 minutes, lights don't turn on automatically. Helpful for:
- Naps
- Early bedtimes
- Privacy

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Bathroom motion sensor shows no motion for 5 minutes
- **Condition:** Bathroom door sensor is "open" (adjust based on your sensor's open/closed values)
- **Action:** Turn off bathroom light

### SmartThings (with SharpTools)

1. Create rule in SharpTools
2. **Trigger:** Motion inactive for 5 minutes
3. **Condition:** Door sensor is "open"
4. **Action:** Turn off light

### Hubitat (Rule Machine)

1. Create new rule
2. **Trigger:** Motion inactive (canceled) for 5 minutes
3. **Required Expression:** Door contact is open
4. **Actions to Run:** Off: Light

## Advanced implementations

### Manual disable mode with button

Add a physical button to manually disable all automations in a room:
- **Trigger:** Disable button pressed
- **Action:** Toggle automation disabled mode

Then add condition to all automations:
- **Condition:** Automation disabled mode is OFF

This allows manual override when needed.

### Visual indicator

Use LED strip or smart bulb to show automation status:
- **When disabled:** Set status light to red
- **When enabled:** Set status light to green
- **Trigger:** Automation disabled mode changes

Provides visual feedback of automation state.

### Time-based auto-resume

Automatically re-enable automations after a set period:
- **Trigger:** Automation disabled mode has been ON for 2 hours
- **Action:** Turn off disabled mode (re-enable automations)

Prevents accidentally leaving automations disabled permanently.

## Troubleshooting

### Lights still turn off when door closed

**Check:**
- Door sensor state in app (is "closed" showing as 'on' or 'off'?)
- Condition logic matches your sensor's behavior
- Automation is actually using the condition

**Fix:** Reverse the door state condition if needed. If your sensor shows 'on' when closed, use 'on' in the condition instead of 'off'.

### Door sensor not reliable

**Causes:**
- Sensor too far from magnet
- Battery low
- Door doesn't close fully

**Solutions:**
- Reposition for better alignment
- Replace battery
- Adjust door latch/strike plate
- Use tilt sensor instead of contact sensor

---

**Related automations:**
- [Toggle lights on door open](/automation/contact/toggle-lights-door/)
- [Turn off lights after motion stops](/automation/motion/lights-off-after-motion/)

[← Back to contact sensor automations](/automation/contact/) | [View all automations →](/automation/)
