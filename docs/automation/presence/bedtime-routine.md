---
layout: default
title: Bedtime Routine Automation - Smart Home Night Mode
description: Automate your bedtime routine with lights off, doors locked, and thermostat adjusted. Complete guide for nighttime smart home automation.
keywords: bedtime routine automation, night mode automation, smart home bedtime, automatic bedtime routine, good night automation
---

# Turn on all lights when going to bed

This automation is a real time-saver that can be customized for more than just bedtime. One command prepares your entire home for sleep.

## Use cases

* **Bedtime** - Turn off lights throughout house
* **One-button routine** - Single trigger for multiple actions
* **Voice command** - "Good night" to Alexa/Google/Siri
* **Scheduled** - Automatic at set time
* **Button press** - Physical bedside button

## Products needed

* **Smart lights** - Throughout house
* **Smart button** (optional) - Bedside trigger
* **Smart locks** - Auto-lock doors
* **Smart thermostat** - Temperature adjustment

## Basic automation setup

### Triggers
* Time is 10:00 PM
* OR button is pressed
* OR voice command "Good night"

### Conditions
* None (immediate execution desired)

### Actions
* Turn off all main lights in house
* Keep nightlights on (optional)
* Put house in Night Mode

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Triggers:**
  - Time is 10:00 PM
  - OR bedside button pressed
- **Actions:**
  - Turn off main lights in living room, kitchen, and office
  - Turn on nightlights (bedroom and bathroom) at 10% brightness
  - Set house mode to "Night"

### SmartThings

Create routine:
1. **WHEN** Time is 10:00 PM OR button pressed
2. **THEN** 
   - Change mode to "Night"
   - Turn off main lights
   - Keep nightlights on

### Apple HomeKit

Create "Good Night" scene:
1. Turn off main lights
2. Set nightlights to 10%
3. Lock doors
4. Set thermostat

Trigger via:
- Voice: "Hey Siri, good night"
- Button automation
- Time automation

### Alexa

Create routine:
1. **WHEN** You say "Good night"
2. **ALEXA WILL:**
   - Turn off lights (select rooms)
   - Lock doors
   - Set thermostat
   - Play white noise (optional)

### Google Home

Create routine:
1. **WHEN** I say "Good night"
2. **ASSISTANT WILL:**
   - Adjust lights and plugs
   - Lock doors
   - Set thermostat
   - Play sleep sounds

## Night mode actions

### Lighting
* **Turn off:**
  - Living room
  - Kitchen
  - Office
  - Hallway main lights
  
* **Keep on (dim):**
  - Bedroom nightlight (10%)
  - Bathroom nightlight (10%)
  - Hallway nightlight (5%)

### Security
* **Lock all doors:**
  - Front door
  - Back door
  - Side doors
  - Garage door
  
* **Close garage door** - If open

* **Arm security:**
  - Motion sensors
  - Cameras (enable night mode)
  - Perimeter sensors

### Climate
* **Adjust thermostat:**
  - Lower to sleeping temperature
  - Heating: 65°F (18°C)
  - Cooling: 70°F (21°C)
  
* **Enable DND mode** - Quiet smart speakers

### Cameras
* **Set privacy mode** - Indoor cameras
* **Enable night vision** - Outdoor cameras
* **Reduce sensitivity** - Prevent alerts from normal movement

### Appliances
* **Turn off non-essentials:**
  - Coffee maker
  - Fans (except bedroom)
  - Entertainment systems
  - Office equipment

## Advanced features

### Gradual dimming (15 minutes before bedtime)

Create automation that gradually dims lights before bedtime:
- **Trigger:** Time is 9:45 PM (15 minutes before bedtime)
- **Action:** Dim living room lights to 30% over 15 minute transition

### Sleep tracking integration

If using sleep tracker (Apple Watch, Fitbit, etc.):

Create trigger: When sleep status changes to "sleeping"

### Reminder checks

Before activating Night Mode, verify:
- All windows closed
- Appliances off
- Doors locked
- Garage closed

Send notification if any issues.

### Kids bedtime vs. adult bedtime

**Kids Bedtime (8:30 PM):**
- Dim kids' room lights
- Turn off playroom
- Start white noise
- Keep hallway lights

**Adult Bedtime (10:30 PM):**
- Full house Night Mode
- All lights off (except nightlights)
- Lock everything
- Lower thermostat

## Safety considerations

**Always Keep:**
- Path lighting (nightlights)
- Emergency exit lighting
- Quick access to manual controls
- Physical keys accessible

**Smart speaker settings:**
- Reduce volume at night
- Or enable DND completely
- Allow emergency phrases through

## Troubleshooting

### Lights don't turn off

**Check:**
- Automation is enabled
- Lights are connected
- No competing automations
- Switch positions

### Nightlights too bright/dim

**Adjust brightness:**
- Test different percentages
- 5-15% typical range
- Warmer color temperature better

### Locks don't engage

**Verify:**
- Lock battery level
- Lock is in range
- Automation includes lock command
- Check lock status in app

---

**Related automations:**
- [Morning routine](/automation/presence/morning-routine/)
- [Set away mode](/automation/presence/away-mode/)
- [Bathroom night light](/automation/motion/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/presence/">← Back to Presence Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
