---
layout: default
title: Automation Recipes
---

# Automation recipes

This is the main section with dozens of practical automation recipes for your smart home. These automations have been tested and refined over years to be as accurate and easy to set up as possible.

## Categories

### 💡 [Lighting](/automation/lighting/)

Automatic lighting is the foundation of a smart home. Learn how to:
- Turn on lights when motion is detected
- Turn off lights after motion stops
- Toggle lights on door open/close
- Outdoor lights at sunset

[Explore Lighting Automations →](/automation/lighting/)

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
- Automatic blinds at sunset and sunrise
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
- Water leak detection and response
- Garage door monitoring

[Explore Security Automations →](/automation/security/)

---

### 🖥️ [Dashboards](/automation/dashboards/)

Visual control and status for your smart home:
- Garbage day reminders
- Status tiles instead of notifications
- Music controls

[Explore Dashboard Automations →](/automation/dashboards/)

---

### 🔔 [Notifications and reminders](/automation/notifications/)

Stay informed with smart alerts and reminders:
- Low battery alerts
- Doorbell notifications
- Family-friendly reminders
- Baby sleep mode

[Explore Notification Automations →](/automation/notifications/)

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

[← Back to Home](/) | [Start with Lighting →](/automation/lighting/)

