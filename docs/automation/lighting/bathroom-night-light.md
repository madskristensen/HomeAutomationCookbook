---
layout: default
title: Bathroom Night Light Automation - Low Brightness Motion Lighting
description: Create a gentle nighttime bathroom lighting automation that turns on lights at low brightness when motion is detected at night. Perfect for nighttime navigation.
keywords: bathroom night light, nighttime motion lighting, low brightness automation, smart bathroom lighting, motion sensor dimming, night mode lighting
---

# Turn on bathroom light at low dim at night

This simple yet valuable automation provides gentle lighting for nighttime bathroom visits. It prevents harsh bright lights from disrupting your sleep cycle while providing enough illumination for safe navigation.

<div class="info-box">
  <strong>🌙 Why This Automation Matters</strong>
  <ul>
    <li><strong>Sleep Quality:</strong> Bright lights suppress melatonin production. Low-light maintains sleep readiness and makes it easier to fall back asleep.</li>
    <li><strong>Safety:</strong> No stumbling in the dark. Safe navigation for all ages, reduces fall risk for elderly. Kids can navigate independently.</li>
    <li><strong>Family-Friendly:</strong> Whole household benefits. Great for overnight guests. Works for everyone automatically with no explanation needed.</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Nighttime Navigation</h4>
    <ul>
      <li><strong>Middle of Night Bathroom Trips</strong> - Common for everyone</li>
      <li><strong>Nighttime Hallway Navigation</strong> - Safe path to bathroom</li>
      <li><strong>Kids Walking to Parents' Bedroom</strong> - Safe independent movement</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Early Morning & Kitchen</h4>
    <ul>
      <li><strong>Getting Water from Kitchen</strong> - Any nighttime navigation</li>
      <li><strong>Early Morning Routine</strong> - Before sunrise gentle lighting</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        Battery-powered (easier installation) or Wired (no battery changes needed)<br>
        Placement: Bathroom entry or hallway
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Light Switch or Bulb</strong>
      <div class="product-details">
        Must support dimming • Check minimum brightness (some only go to 10%)<br>
        Color temperature control helpful (warm white better at night)
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Lux Sensor</strong>
      <div class="product-details">
        Only activate if dark enough
      </div>
    </div>
    
    <div class="product-item">
      <strong>Multiple Motion Sensors</strong>
      <div class="product-details">
        For larger spaces
      </div>
    </div>
    
    <div class="product-item">
      <strong>Color Bulbs</strong>
      <div class="product-details">
        Can use red/amber for minimal sleep disruption
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF motion detected in bathroom
AND time between 10:00 PM - 6:00 AM
THEN turn on light to 10% warm white</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Motion detected by sensor</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>Home is in "Night Mode" OR time is between 10 PM and 6 AM</li>
      <li>Room is dark (lux sensor below threshold - optional)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on light switch/bulb at 10% brightness</li>
      <li>Set color temperature to warm white (2700K) if supported</li>
      <li>Optional: Set color to red or amber for minimal disruption</li>
    </ul>
  </div>
</div>

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

See [Presence & Modes Automations](/automation/daily-routines/) for detailed Night Mode setup.

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

### Hubitat

Use Motion Lighting app or Rule Machine:
1. **Trigger:** Motion sensor active
2. **Condition:** Mode is "Night" OR time between 10 PM and 6 AM
3. **Action:** Turn on bathroom light at 10% brightness
4. **Optional:** Set color temperature to warm white (2700K) if supported

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

See [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/) for complete details.

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

### Lights still too bright

**Try:**
- Reduce to 5% or lower
- Use red/amber color if supported
- Add dimming film to bulb (diffuses light)
- Use nightlight instead for minimal illumination

### Lights too dim for safety

**Try:**
- Increase to 15-20%
- Use warmer but brighter setting
- Add additional lighting in critical areas
- Motion-sensitive nightlights as backup

### Delay before lights come on

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
- [Turn on lights when motion detected](/automation/lighting/lights-on-motion/)
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/)
- [Night mode setup](/automation/daily-routines/night-mode/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
