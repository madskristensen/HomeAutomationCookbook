---
layout: default
title: Driveway Welcome Wave - Smart Arrival Lighting Automation
description: Create a stunning ripple lighting effect from street to front door when you arrive home. Step-by-step guide for driveway welcome lighting automation.
keywords: driveway lights, arrival lighting, welcome home lights, ripple effect lights, smart outdoor lighting, pathway lights automation, garage arrival lights
---

# Driveway welcome wave

Create a stunning visual welcome when you arrive home by having lights ripple from the street toward your front door. This choreographed lighting sequence creates an impressive pathway effect that guides you home while adding security and curb appeal.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Daily arrivals</h4>
    <ul>
      <li><strong>Evening homecoming</strong> - Lights guide you from street to door after dark</li>
      <li><strong>Late night returns</strong> - Safe, well-lit path to your entrance</li>
      <li><strong>Guest arrivals</strong> - Impressive welcome for visitors</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Security and ambiance</h4>
    <ul>
      <li><strong>Deterrent effect</strong> - Active lighting discourages intruders</li>
      <li><strong>Pathway visibility</strong> - Clearly illuminated walkway prevents trips</li>
      <li><strong>Curb appeal</strong> - Dramatic effect impresses neighbors and guests</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart outdoor lights</strong>
      <div class="product-details">
        Popular brands: Philips Hue Outdoor, LIFX, Ring Smart Lighting, Govee<br>
        Multiple zones: Street/driveway entrance, pathway, gate area, front door
      </div>
    </div>
    
    <div class="product-item">
      <strong>Arrival detection</strong>
      <div class="product-details">
        Options: GPS geofencing, driveway motion sensor, garage door sensor, or car presence sensor<br>
        Platforms: Home Assistant, SmartThings, Hubitat with presence detection
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Driveway motion sensor</strong>
      <div class="product-details">
        Detects car approaching before reaching garage for earlier trigger
      </div>
    </div>
    
    <div class="product-item">
      <strong>Color-capable lights</strong>
      <div class="product-details">
        Add color effects like warm amber wave or holiday themes
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Light zone planning tip</strong>
  <ul>
    <li>Zone 1: Street/driveway entrance lights</li>
    <li>Zone 2: Mid-driveway or pathway lights</li>
    <li>Zone 3: Gate or garage area lights</li>
    <li>Zone 4: Front porch and door lights</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF car detected in driveway OR geofence arrival
AND time is after sunset
THEN turn on street lights
WAIT 1 second
THEN turn on pathway lights
WAIT 1 second
THEN turn on gate lights
WAIT 1 second
THEN turn on front door lights</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Driveway motion sensor detects vehicle</li>
      <li>OR phone GPS enters home zone</li>
      <li>OR garage door begins opening</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Time-based:</strong> Only after sunset or before sunrise<br>
    <strong>Mode:</strong> Only when arriving (not when already home)<br>
    <strong>Cooldown:</strong> Don't repeat within 10 minutes
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on Zone 1 (street) lights to 100%</li>
      <li>Wait 1-2 seconds</li>
      <li>Turn on Zone 2 (pathway) lights to 100%</li>
      <li>Wait 1-2 seconds</li>
      <li>Turn on Zone 3 (gate) lights to 100%</li>
      <li>Wait 1-2 seconds</li>
      <li>Turn on Zone 4 (front door) lights to 100%</li>
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
        <span class="step-content">Person enters home zone OR driveway motion detected</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Sun is below horizon</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Run script with sequential light activation and delays</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use a script with delay actions between each light zone
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
        <span class="step-content">Member arrives at home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Time is between sunset and sunrise</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Activate welcome wave scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create scene with timed light sequences using SmartThings Routines
        </div>
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
        <span class="step-content">Presence sensor arrives OR motion on driveway</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Mode is Night or time after sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Run Rule Machine sequence with delays</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine for complex sequencing with wait actions
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
        <span class="step-content">First person arrives home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">After sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Activate welcome wave scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use Shortcuts app for advanced sequencing with delays
        </div>
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
        <span class="step-content">Location: You arrive home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Between sunset and sunrise</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on lights with wait actions between each zone</span>
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
        <span class="step-label">Starter</span>
        <span class="step-content">When first person arrives home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">After sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Activate arrival lighting scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> May need third-party app for sequential delays
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Color wave effect</h3>
    <p>Add color transitions for extra visual impact:</p>
    <ul>
      <li>Warm amber wave from street to door</li>
      <li>Cool white to warm white transition</li>
      <li>Holiday colors for seasonal themes</li>
      <li>Family member-specific colors (Dad = blue, Mom = purple)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Speed variations</h3>
    <p>Adjust timing based on context:</p>
    <ul>
      <li><strong>Normal arrival:</strong> 1-2 second delays between zones</li>
      <li><strong>Quick entry:</strong> 0.5 second delays</li>
      <li><strong>Dramatic effect:</strong> 3-4 second delays</li>
      <li><strong>Guest mode:</strong> Slower, more impressive wave</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Per-person customization</h3>
    <p>Different effects for different family members:</p>
    <ul>
      <li>Track which phone triggered arrival</li>
      <li>Assign different colors or brightness per person</li>
      <li>Kids get fun colors, adults get warm white</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights activate too late</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Already at the door before lights start rippling.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use GPS geofence trigger further from home (200-300m radius)</li>
        <li>Add driveway motion sensor for earlier detection</li>
        <li>Trigger on garage door opening instead of arrival</li>
        <li>Use faster local processing (Zigbee/Z-Wave vs cloud)</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Sequence feels disjointed</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lights don't flow smoothly from zone to zone.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reduce delay time between zones (try 0.5-1 second)</li>
        <li>Ensure all lights are on same protocol for consistent timing</li>
        <li>Add transition time to lights so they fade on gradually</li>
        <li>Test and adjust timing to match your walking pace</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Triggers for other family members</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Wave activates when already home and someone else arrives.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add condition: Only if home mode was "Away"</li>
        <li>Add cooldown period (don't repeat within 30 minutes)</li>
        <li>Track if first person arriving (not subsequent arrivals)</li>
        <li>Use car-specific detection if possible</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="best-practice-card">
  <h3>Light zone planning</h3>
  <ol>
    <li>Map out your driveway and pathway into 3-5 distinct zones</li>
    <li>Ensure zones follow natural walking/driving path</li>
    <li>Position lights to illuminate walkway, not just be decorative</li>
    <li>Consider both car and pedestrian arrival paths</li>
    <li>Test timing by walking the path while watching lights</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>Too many zones</strong> - 3-5 zones is ideal, more becomes chaotic</li>
    <li><strong>Delays too long</strong> - You'll arrive before the wave finishes</li>
    <li><strong>Bright flash</strong> - Use gradual transitions, not instant on</li>
    <li><strong>Daytime activation</strong> - Wastes energy and isn't visible anyway</li>
  </ul>
</div>

---

**Related automations:**
- [Outdoor night lights](/automation/lighting/outdoor-night-lights/)
- [Welcome home music](/automation/entertainment/welcome-home-music/)
- [Unlock door on arrival](/automation/daily-routines/unlock-door-arrival/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
