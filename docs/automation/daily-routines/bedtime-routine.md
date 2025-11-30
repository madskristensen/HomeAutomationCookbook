---
layout: automation
title: Bedtime Routine Automation - Smart Home Night Mode
description: Automate your bedtime routine with lights off, doors locked, and thermostat adjusted. Complete guide for nighttime smart home automation.
keywords: bedtime routine automation, night mode automation, smart home bedtime, automatic bedtime routine, good night automation
---

# Turn on all lights when going to bed

As the day winds down, the house should wind down with it. A single command - spoken, tapped, or triggered by a button at the bedside - sends the home into its nightly rest. Lights extinguish room by room, locks confirm their hold, the thermostat settles into its sleeping temperature. You can close your eyes knowing that everything has been tended to.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Trigger Methods</h4>
    <ul>
      <li><strong>Bedtime</strong> - Turn off lights throughout house</li>
      <li><strong>Voice Command</strong> - "Good night" to Alexa/Google/Siri</li>
      <li><strong>Button Press</strong> - Physical bedside button</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Automation Styles</h4>
    <ul>
      <li><strong>One-Button Routine</strong> - Single trigger for multiple actions</li>
      <li><strong>Scheduled</strong> - Automatic at set time</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Lights</strong>
      <div class="product-details">
        Throughout house for automation control
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Button</strong>
      <div class="product-details">
        Bedside trigger for one-press routine
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Locks</strong>
      <div class="product-details">
        Auto-lock doors at bedtime
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Thermostat</strong>
      <div class="product-details">
        Temperature adjustment for sleep
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF bedtime button pressed (or time is 10:30 PM)
THEN turn off all downstairs lights
AND lock doors
AND set thermostat to sleep mode</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Time is 10:00 PM</li>
      <li>OR button is pressed</li>
      <li>OR voice command "Good night"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <p>None (immediate execution desired)</p>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn off all main lights in house</li>
      <li>Keep nightlights on (optional)</li>
      <li>Put house in Night Mode</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
      <h4>Home Assistant</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Time is 10:00 PM OR bedside button pressed</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Turn off main lights, nightlights to 10%, set mode to "Night"</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">WHEN</span>
        <span class="step-content">Time is 10:00 PM OR button pressed</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Change mode to "Night", turn off main lights</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Time is 10:00 PM OR button pressed</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Change mode to "Night" → Turn off main lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Mode Manager + Rule Machine for mode-based actions
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Scene</span>
        <span class="step-content">"Good Night" - turn off main lights, nightlights to 10%</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Voice "Hey Siri, good night" or button/time automation</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">You say "Good night"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Turn off lights, lock doors, set thermostat</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">I say "Good night"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Adjust lights, lock doors, set thermostat</span>
      </div>
    </div>
  </div>
</div>

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
- [Morning routine](/automation/daily-routines/morning-routine/)
- [Set away mode](/automation/daily-routines/away-mode/)
- [Bathroom night light](/automation/lighting/bathroom-night-light/)

<div class="page-navigation">
  <a href="/automation/daily-routines/">← Back to Daily Routines</a>
  <a href="/automation/">View All Automations →</a>
</div>
