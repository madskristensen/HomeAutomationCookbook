---
layout: default
title: Automation Recipes
---

# Automation recipes

This is the main section with dozens of practical automation recipes for your smart home. These automations have been tested and refined over years to be as accurate and easy to set up as possible.

## Categories

### 🚶 [Motion Detection](/automation/motion/)

Motion sensors are powerful automation tools. Learn how to:
- Turn on lights when motion is detected
- Turn off lights after motion stops
- Create nighttime low-light automations

[Explore Motion Automations →](/automation/motion/)

---

### 🚪 [Contact (door/window) sensors](/automation/contact/)

Versatile sensors that enable many useful automations:
- Toggle lights when doors open
- Disable automations when doors close
- Security and safety alerts

[Explore Contact Sensor Automations →](/automation/contact/)

---

### 📍 [Presence and modes](/automation/presence/)

Location-based and mode-driven automations:
- Set Away Mode when everybody leaves
- Unlock door when you arrive home
- Morning and bedtime routines
- Guest and vacation modes

[Explore Presence Automations →](/automation/presence/)

---

### 🌡️ [Climate](/automation/climate/)

Control temperature, humidity, and air quality:
- Turn on fan when shower starts
- Control thermostat with window sensors
- Maintain temperature with room heaters
- Air quality monitoring and control

[Explore Climate Automations →](/automation/climate/)

---

### 🎵 [Media](/automation/media/)

Music and entertainment control:
- Play music when you start shower
- Control music with physical switches
- Speaker volume presets
- Dim lights when TV turns on

[Explore Media Automations →](/automation/media/)

---

### 🧺 [Appliances](/automation/appliances/)

Smart appliance notifications and control:
- Washer and dryer completion alerts
- Dishwasher done notifications
- Robot vacuum scheduling
- Coffee maker automation

[Explore Appliance Automations →](/automation/appliances/)

---

### 🔒 [Security and Safety](/automation/security/)

Protect your home and family:
- Away lighting patterns
- Fire emergency response
- Door and window monitoring

[Explore Security Automations →](/automation/security/)

---

### 🖥️ [Dashboards](/automation/dashboards/)

Visual control and status for your smart home:
- Garbage day reminders
- Status tiles instead of notifications
- Music controls

[Explore Dashboard Automations →](/automation/dashboards/)

---

### 🎯 [Miscellaneous](/automation/misc/)

Additional helpful automations:
- Outdoor night lights
- Doorbell notifications
- Baby sleep mode
- And more!

[Explore Misc Automations →](/automation/misc/)

---

## Getting started with automations

### 1. Start simple
Begin with a single trigger and single action. Test thoroughly before adding complexity.

### 2. Add conditions
Enhance automations with time of day, presence detection, or sensor state conditions.

### 3. Test thoroughly
Run automations in "test mode" before enabling permanently. Monitor for a few days.

### 4. Document
Name automations clearly and add descriptions for future reference.

### 5. Iterate
Gather feedback from household members and refine based on real-world usage.

## Automation patterns

### If/Then/Else
```
IF motion detected
THEN turn on light
ELSE (after 5 min) turn off light
```

### Multiple conditions
```
IF (motion detected) AND (lux < 100) AND (time after sunset)
THEN turn on light
```

### Time-based
```
EVERY weekday at 7:00 AM
DO run morning routine
```

## Best practices

✅ **Keep It Simple** - Simple automations are reliable automations
✅ **Include Delays** - Avoid rapid on/off toggling
✅ **Plan Fallbacks** - What if a sensor fails?
✅ **Test Edge Cases** - What happens at midnight? During power outage?
✅ **Get Feedback** - Ask family members how automations work for them

---

[← Back to Home](/) | [Start with Motion Detection →](/automation/motion/)

