---
layout: default
title: Automation Recipes
---

# Automation recipes

This is the main section with dozens of practical automation recipes for your smart home. These automations have been tested and refined over years to be as accurate and easy to set up as possible.

<div class="platform-compatibility">
  <p><strong>Platform agnostic:</strong> All recipes work with</p>
  <div class="platform-logos">
    <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant" title="Home Assistant" class="platform-logo">
    <img src="/assets/img/logos/hubitat.png" alt="Hubitat" title="Hubitat" class="platform-logo">
    <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit" title="Apple HomeKit" class="platform-logo">
    <img src="/assets/img/logos/smartthings.png" alt="SmartThings" title="SmartThings" class="platform-logo">
    <img src="/assets/img/logos/google.png" alt="Google Home" title="Google Home" class="platform-logo">
    <img src="/assets/img/logos/alexa.png" alt="Alexa" title="Alexa" class="platform-logo">
  </div>
</div>

## Categories

All automations are organized by what they accomplish, making it easy to find solutions for your specific needs.

### [Lighting](/automation/lighting/)

Automatic lighting that responds to your presence and needs:
- Turn on lights when motion is detected
- Toggle lights when doors open
- Nighttime low-brightness lighting
- Outdoor lights at sunset

[Explore Lighting Automations →](/automation/lighting/)

---

### [Daily routines](/automation/daily-routines/)

Automate your daily rhythm for effortless living:
- Away mode when everyone leaves
- Morning wake-up routines
- Bedtime wind-down automation
- Unlock door on arrival

[Explore Daily Routine Automations →](/automation/daily-routines/)

---

### [Climate and comfort](/automation/climate/)

Control temperature, humidity, and air quality:
- Turn on fan when shower starts
- Pause thermostat when windows open
- Automatic blinds at sunset and sunrise
- Air quality monitoring and control

[Explore Climate Automations →](/automation/climate/)

---

### [Entertainment](/automation/entertainment/)

Music and media control for your lifestyle:
- Dim lights when TV turns on
- Play music when you start shower
- Control music with physical switches
- Speaker volume presets

[Explore Entertainment Automations →](/automation/entertainment/)

---

### [Appliances](/automation/appliances/)

Smart appliance notifications and control:
- Washer and dryer completion alerts
- Dishwasher done notifications
- Robot vacuum scheduling
- Coffee maker automation

[Explore Appliance Automations →](/automation/appliances/)

---

### [Safety and security](/automation/security/)

Protect your home and family:
- Away lighting patterns to deter intruders
- Fire emergency response
- Water leak detection and response
- Garage door monitoring

[Explore Safety Automations →](/automation/security/)

---

### [Notifications and alerts](/automation/notifications/)

Stay informed without notification fatigue:
- Low battery alerts for all devices
- Dashboard status tiles
- Doorbell notifications
- Family reminders (teeth brushing, garbage day)

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

