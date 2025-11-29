---
layout: default
title: Bathroom Night Light Automation - Low Brightness Motion Lighting
description: Create a gentle nighttime bathroom lighting automation that turns on lights at low brightness when motion is detected at night. Perfect for nighttime navigation.
keywords: bathroom night light, nighttime motion lighting, low brightness automation, smart bathroom lighting, motion sensor dimming, night mode lighting
---

# Turn on bathroom light at low dim at night

This simple yet valuable automation provides gentle lighting for nighttime bathroom visits. It prevents harsh bright lights from disrupting your sleep cycle while providing enough illumination for safe navigation.

## Why this automation matters

**Sleep quality benefits:**
- Bright lights suppress melatonin production
- Low-light maintains sleep readiness
- Easier to fall back asleep
- Less disruptive to sleep patterns

**Safety benefits:**
- No stumbling in the dark
- Safe navigation for all ages
- Reduces fall risk for elderly
- Kids can navigate independently

**Family-friendly:**
- Whole household benefits
- Great for overnight guests
- Works for everyone automatically
- No explanation needed

## Use cases

* **Middle of night bathroom trips** - Common for everyone
* **Nighttime hallway navigation** - Safe path to bathroom
* **Kids walking to parents' bedroom** - Safe independent movement
* **Getting water from kitchen** - Any nighttime navigation
* **Early morning routine** - Before sunrise gentle lighting

## Products needed

### Essential equipment

* **Motion sensor**
  - Battery-powered: Easier installation
  - Wired: No battery changes needed
  - Placement: Bathroom entry or hallway
  
* **Smart light switch or bulb**
  - Must support dimming
  - Check minimum brightness (some only go to 10%)
  - Color temperature control helpful (warm white better at night)

### Optional enhancements

* **Lux sensor** - Only activate if dark enough
* **Multiple motion sensors** - For larger spaces
* **Smart dimmer** - Better dimming control
* **Color bulbs** - Can use red/amber for minimal sleep disruption

## Basic automation setup

### Triggers
* Motion detected by sensor

### Conditions (optional)
* Home is in "Night Mode"
* OR time is between 10 PM and 6 AM
* AND room is dark (lux sensor below threshold - optional)

### Actions
* Turn on light switch/bulb at 10% brightness
* Set color temperature to warm white (2700K) if supported
* Optional: Set color to red or amber for minimal disruption

## Creating "Night Mode"

Night Mode is a home state that indicates sleeping hours. Set it up using:

**Option 1: Time-based**
- IF time is 10:00 PM
- THEN set house to Night Mode

**Option 2: Manual trigger**
- IF "Good Night" voice command
- OR bedtime button pressed
- THEN set house to Night Mode

**Option 3: Presence-based**
- IF last person goes to bedroom
- AND time is after 9:00 PM
- THEN set house to Night Mode

See [Presence & Modes Automations](/automation/presence/) for detailed Night Mode setup.

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Motion sensor detects movement
- **Condition:** House mode is "Night" OR time between 10 PM and 6 AM
- **Action:** Turn on bathroom light at 10% brightness with warm white (2700K) color temperature

### Advanced: Multiple brightness levels by time

Adjust brightness based on time of night:
- **Deep night (11 PM - 5 AM):** 5% brightness, very warm (2200K)
- **Early morning (5 AM - 7 AM):** 20% brightness, warm (2700K)
- **Late evening (9 PM - 11 PM):** 15% brightness, warm white

Use conditional logic to check current time and set appropriate brightness level.

### SmartThings

Create routine:
1. **IF** "Bathroom Motion Sensor" detects motion
2. **AND** Location mode is "Night"
3. **THEN** Set "Bathroom Light" to 10% brightness

### Apple HomeKit

1. Create automation in Home app
2. **When:** Bathroom motion sensor detects motion
3. **Time:** Between 10 PM and 6 AM
4. **Do:** Turn on bathroom light at 10%
5. **Optional:** Convert to Shortcut for color temperature control

### Alexa

Create routine:
1. **When:** "Bathroom Motion Sensor" detects motion
2. **Add condition:** Time between 10:00 PM and 6:00 AM
3. **Alexa will:** Smart Home → Turn on "Bathroom Light" to 10%

### Google Home

Create automation:
1. **Starter:** "Bathroom Motion Sensor" detects motion
2. **Condition:** Between 10 PM and 6 AM
3. **Action:** Set "Bathroom Light" brightness to 10%

## Pro tips

### Strategic sensor placement

The motion sensor doesn't have to be in the room you want to light up!

**Example: Separate toilet room**

In my bathroom with a separate toilet room:
- Motion sensor is in main bathroom
- Lights triggered: Both main bathroom AND toilet room
- **Benefit:** Lights come on BEFORE entering toilet room
- Path is lit up in advance

**Other strategic placements:**
- Bedroom sensor → Bathroom lights
- Hallway sensor → Multiple room lights
- Stairway sensor → Upstairs bathroom

### Brightness levels by location

Different rooms may need different nighttime brightness:

**Very Low (5-8%):**
- Bedroom
- Baby's room
- Reading area

**Low (10-15%):**
- Bathroom
- Toilet room
- Bedroom hallway

**Medium-Low (15-25%):**
- Main hallway
- Kitchen
- Stairs (safety priority)

### Color temperature guidelines

**Warm White (2200-2700K):**
- Minimal melatonin suppression
- Comfortable orange/amber glow
- Best for sleep maintenance

**Ultra Warm/Red (1800K or Red):**
- Even less sleep disruption
- Takes time to adjust (seems very dim)
- Best for frequent night wakers

**Avoid:**
- Cool white (4000K+) - suppresses melatonin
- Blue tones - very disruptive to sleep
- Bright white - defeats the purpose

## Auto turn-off integration

Combine with motion-stop automation for complete cycle:
- **Trigger:** Motion sensor shows no motion for 5 minutes
- **Condition:** House mode is "Night"
- **Action:** Turn off bathroom light

See [Turn off lights after motion stops](/automation/motion/lights-off-after-motion/) for complete details.

## Extending to other rooms

Apply the same pattern throughout your home:

### Hallways
- 15% brightness
- Warm white (2200K)

### Kitchen
- 20% brightness
- Warm (2700K)

### Stairs (safety priority)
- 25% brightness (brighter for safety)
- Warm (2700K)

### Kids' rooms
- 8% brightness (very low)
- Warm white (2200K)

## Advanced: Personal preferences

### Per-person brightness

Use presence detection to adjust brightness by person:
- **Parent 1 home:** 5% brightness (very dim preference)
- **Parent 2 home:** 15% brightness (slightly brighter preference)
- **Guests/others:** 10% brightness (default)

Use conditional logic to check which person is home and set their preferred brightness.

### Gradual brightening

Lights start very dim and gradually increase:
1. Start at 5% brightness
2. Wait 3 seconds
3. Check if motion still detected
4. If yes, increase to 10% with 2-second transition

This prevents sudden brightness changes that disrupt sleep.

## Troubleshooting

### Lights Still Too Bright

**Try:**
- Reduce to 5% or lower
- Use red/amber color if supported
- Add dimming film to bulb (diffuses light)
- Use nightlight instead for minimal illumination

### Lights Too Dim for Safety

**Try:**
- Increase to 15-20%
- Use warmer but brighter setting
- Add additional lighting in critical areas
- Motion-sensitive nightlights as backup

### Delay Before Lights Come On

**Causes:**
- Cloud processing
- Sensor placement
- Weak wireless signal

**Solutions:**
- Ensure local automation processing
- Move sensor closer to entry point
- Add Zigbee/Z-Wave repeaters
- Optimize automation logic

---

**Related automations:**
- [Turn on lights when motion detected](/automation/motion/lights-on-motion/)
- [Turn off lights after motion stops](/automation/motion/lights-off-after-motion/)
- [Night mode setup](/automation/presence/night-mode/)

[← Back to motion detection automations](/automation/motion/) | [View all automations →](/automation/)
