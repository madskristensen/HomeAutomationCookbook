---
layout: default
title: Morning Routine Automation - Wake Up Smart Home
description: Automate your morning routine with lights, coffee, music, and thermostat. Complete guide for morning automation with all major smart home platforms.
keywords: morning routine automation, wake up automation, smart home morning, automatic morning routine, morning lights automation
---

# Turn on all lights when you get up in the morning

Start your day right with an automated morning routine that prepares your home for the day ahead. From gradual lighting to starting the coffee maker, this automation creates a consistent, pleasant wake-up experience.

## Use cases

* **Weekday mornings** - Consistent wake-up routine
* **Motion-triggered** - Lights when you get out of bed
* **Time-based** - Scheduled wake-up time
* **Voice-activated** - "Good morning" routine
* **Button-triggered** - Bedside button press

## Products needed

* **Smart lights** - Throughout house
* **Motion sensor** (optional) - Bedroom or bathroom
* **Smart button** (optional) - Bedside trigger
* **Smart thermostat** - Climate control
* **Smart plugs** - Coffee maker, etc.

## Basic automation setup

### Triggers
* Time is between 6:00 AM and 9:00 AM
* AND motion detected in bedroom
* OR button pressed
* OR voice command "Good morning"

### Conditions
* House is in Night Mode
* Time is between 6:00 AM and 10:00 AM

### Actions
* Turn on main lights in house
* Put house in Home Mode

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Bedroom motion sensor detects motion
- **Conditions:**
  - House mode is "Night"
  - Time is between 6 AM and 10 AM
- **Actions:**
  - Set house mode to "Home"
  - Turn on lights in kitchen, bathroom, and hallway at 100% brightness

### SmartThings

Create routine:
1. **IF** Motion in bedroom
2. **AND** Time between 6 AM - 10 AM  
3. **AND** Mode is "Night"
4. **THEN** Change mode to "Home"
5. **AND** Turn on morning lights

### Apple HomeKit

Create automation:
1. **When:** Motion detected in bedroom
2. **Time:** Between 6 AM and 10 AM
3. **Do:** Activate "Good Morning" scene

## Morning (Home) mode actions

### Lighting
* **Kitchen** - 100% brightness
* **Bathroom** - 100% brightness
* **Hallway** - 80% brightness
* **Living room** - 60% (gentle)
* **Bedroom** - Keep off or 20%

### Climate
* **Increase thermostat** - 70°F (21°C)
* **Turn on bathroom fan** - If humid
* **Open smart blinds** - Let in sunlight

### Kitchen
* **Start coffee maker** - Via smart plug
* **Display weather** - On smart display
* **Turn on news** - Smart speaker (optional)

### Security
* **Disarm interior sensors**
* **Disable night cameras** - Interior only
* **Unlock certain doors** - If needed

### Announcements
* **Weather forecast**
* **Calendar events for today**
* **Commute time**
* **Reminders**

## Advanced morning routine

### Gradual wake-up (30 minutes before alarm)

Create automation that gradually increases bedroom light brightness:
- Start at 1% brightness at wake time (e.g., 6:00 AM)
- Gradually increase over 30 minutes
- Use repeat loop: wait 1 minute, increase brightness by 3%, repeat 30 times
- Final brightness reaches ~90% by end

### Weekday vs. weekend

**Weekday routine:**
- Earlier wake time
- News briefing
- Commute information

**Weekend routine:**
- Later wake time
- Music instead of news
- Relaxed lighting

## Related actions

See also:
- [Bedtime Routine](/automation/presence/bedtime-routine/) - Evening counterpart
- [Set Away Mode](/automation/presence/away-mode/) - Leaving home

[← Back to Presence & Modes](/automation/presence/) | [View All Automations →](/automation/)
