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

<div class="platform-grid">
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
      <h4>Home Assistant</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Motion sensor detects movement</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">House mode is "Night" OR time between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom light at 10% brightness</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Set warm white (2700K) color temperature for minimal sleep disruption
        </div>
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
        <span class="step-label">IF</span>
        <span class="step-content">"Bathroom Motion Sensor" detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Location mode is "Night"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Set "Bathroom Light" to 10% brightness</span>
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
        <span class="step-content">Motion sensor active</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Mode is "Night" OR time 10 PM - 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on bathroom light at 10%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Motion Lighting app or Rule Machine
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
        <span class="step-label">When</span>
        <span class="step-content">Bathroom motion sensor detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Time</span>
        <span class="step-content">Between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on bathroom light at 10%</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Amazon Alexa logo">
      <h4>Alexa</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">"Bathroom Motion Sensor" detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on "Bathroom Light" to 10%</span>
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
        <span class="step-content">"Bathroom Motion Sensor" detects motion</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Between 10 PM and 6 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set "Bathroom Light" brightness to 10%</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Multiple brightness levels</h3>
    <p>Adjust brightness based on time of night:</p>
    <div class="brightness-schedule">
      <div class="brightness-item">
        <span class="time-badge">9 PM - 11 PM</span>
        <span class="brightness-level">15%</span>
        <span class="brightness-desc">Still awake, moderate light</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">11 PM - 5 AM</span>
        <span class="brightness-level">5%</span>
        <span class="brightness-desc">Deep night, very warm (2200K)</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">5 AM - 7 AM</span>
        <span class="brightness-level">20%</span>
        <span class="brightness-desc">Early morning, warm (2700K)</span>
      </div>
    </div>
  </div>
  
  <div class="feature-card">
    <h3>Strategic sensor placement</h3>
    <p>The motion sensor doesn't have to be in the room you want to light up:</p>
    <ul>
      <li><strong>Separate toilet room:</strong> Sensor in main bathroom triggers both lights</li>
      <li><strong>Bedroom sensor</strong> triggers bathroom lights</li>
      <li><strong>Hallway sensor</strong> triggers multiple room lights</li>
      <li><strong>Stairway sensor</strong> triggers upstairs bathroom</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Color temperature guidelines</h3>
    <p>Choose appropriate color for minimal sleep disruption:</p>
    <ul>
      <li><strong>Warm White (2200-2700K):</strong> Minimal melatonin suppression</li>
      <li><strong>Ultra Warm/Red (1800K):</strong> Even less sleep disruption</li>
      <li><strong>Avoid Cool White (4000K+):</strong> Suppresses melatonin, disrupts sleep</li>
    </ul>
  </div>
</div>

<div class="placement-grid">
  <div class="placement-card">
    <h3>Brightness by location</h3>
    <ul>
      <li><strong>Very Low (5-8%):</strong> Bedroom, baby's room</li>
      <li><strong>Low (10-15%):</strong> Bathroom, toilet room</li>
      <li><strong>Medium-Low (15-25%):</strong> Hallway, kitchen, stairs</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Extending to other rooms</h3>
    <ul>
      <li><strong>Hallways:</strong> 15%, warm white (2200K)</li>
      <li><strong>Kitchen:</strong> 20%, warm (2700K)</li>
      <li><strong>Stairs:</strong> 25%, safety priority</li>
      <li><strong>Kids' rooms:</strong> 8%, very low</li>
    </ul>
  </div>
</div>

<div class="best-practice-card">
  <h3>Auto turn-off integration</h3>
  <ol>
    <li>Trigger: Motion sensor shows no motion for 5 minutes</li>
    <li>Condition: House mode is "Night"</li>
    <li>Action: Turn off bathroom light</li>
  </ol>
</div>

See [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/) for complete details.

<div class="feature-grid">
  <div class="feature-card">
    <h3>Per-person brightness</h3>
    <p>Use presence detection to adjust brightness by person:</p>
    <ul>
      <li><strong>Parent 1 home:</strong> 5% brightness (very dim preference)</li>
      <li><strong>Parent 2 home:</strong> 15% brightness (slightly brighter preference)</li>
      <li><strong>Guests/others:</strong> 10% brightness (default)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Gradual brightening</h3>
    <p>Lights start very dim and gradually increase:</p>
    <ol>
      <li>Start at 5% brightness</li>
      <li>Wait 3 seconds</li>
      <li>Check if motion still detected</li>
      <li>If yes, increase to 10% with 2-second transition</li>
    </ol>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights still too bright</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Even at lowest setting, lights are too bright for comfortable sleep.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reduce to 5% or lower if bulb supports it</li>
        <li>Use red/amber color if supported</li>
        <li>Add dimming film to bulb (diffuses light)</li>
        <li>Use dedicated nightlight instead</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights too dim for safety</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lighting is not sufficient for safe navigation.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Increase to 15-20%</li>
        <li>Use warmer but brighter setting</li>
        <li>Add additional lighting in critical areas</li>
        <li>Motion-sensitive nightlights as backup</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Delay before lights come on</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Noticeable delay between motion detection and lights turning on.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Ensure local automation processing</li>
        <li>Move sensor closer to entry point</li>
        <li>Add Zigbee/Z-Wave repeaters</li>
        <li>Optimize automation logic</li>
      </ul>
    </div>
  </div>
</div>

---

**Related automations:**
- [Turn on lights when motion detected](/automation/lighting/lights-on-motion/)
- [Turn off lights after motion stops](/automation/lighting/lights-off-after-motion/)
- [Night mode setup](/automation/daily-routines/night-mode/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
