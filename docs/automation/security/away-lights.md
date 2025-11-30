---
layout: automation
title: Away Lights Automation - Make Your Home Look Occupied
description: Deter break-ins and package theft by making your home look occupied with strategic away lighting automation. Complete setup guide.
keywords: away lights, security lighting, home occupied simulation, break-in prevention, package theft prevention, smart home security
---

# Turn on away lights

An empty house, to the wrong kind of observer, announces opportunity. But a house with lights shifting from room to room - a lamp on in the living room, later replaced by a glow from upstairs - tells a different story. The house looks lived in, and that simple appearance is often enough to send trouble looking elsewhere.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Security</h4>
    <ul>
      <li><strong>Deter Break-ins</strong> - Make it look like someone is home</li>
      <li><strong>Package Theft Prevention</strong> - Discourage porch pirates</li>
      <li><strong>Vacation Security</strong> - Maintain occupied appearance during trips</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Peace of Mind</h4>
    <ul>
      <li><strong>Extended Absences</strong> - Feel secure during business trips</li>
      <li><strong>Evening Events</strong> - Come home to a lit house</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Light Switches or Bulbs</strong>
      <div class="product-details">
        Strategic placement in visible rooms<br>
        Switches: Lutron, GE, Inovelli, Leviton<br>
        Bulbs: Philips Hue, LIFX, Wyze, Sengled
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Electric Fireplace</strong>
      <div class="product-details">
        Adds convincing warmth and movement visible from outside
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart TV Simulator</strong>
      <div class="product-details">
        LED device that mimics TV glow patterns
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Blinds/Shades</strong>
      <div class="product-details">
        Automated movement adds to lived-in appearance
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Strategic Light Selection</strong>
  <ul>
    <li>Choose lights visible from the street or driveway</li>
    <li>Living room, kitchen, and one bedroom work well</li>
    <li>Avoid turning on ALL lights - looks unnatural</li>
    <li>Consider what a person home alone would use</li>
  </ul>
</div>

## Basic automation setup

Away lights is a great candidate for a scene or lighting group if your smart home platform supports them. Create an "Away Lights" scene with your strategic lights configured.

<div class="automation-example">IF home goes into Away mode
AND time is between sunset and 11 PM
THEN turn on away lights scene</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation 1: Turn on away lights</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Home goes into Away mode</li>
      <li>OR Time is between sunset and 11 PM (check if already in Away mode)</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Home is in Away mode</li>
      <li>Time is between sunset and 11 PM</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Turn on indoor lights (living room, kitchen)</li>
      <li>Turn on electric fireplace (optional)</li>
      <li>OR Execute scene that turns on the away lights</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Automation 2: Turn off at bedtime</h4>
    <p>At 11 PM, or whatever your normal bedtime is, turn off the away lights:</p>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 11:00 PM</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Home is in Away mode</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Turn off indoor lights</li>
      <li>Turn off electric fireplace</li>
      <li>OR Execute a scene that turns off all lights</li>
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
        <span class="step-content">Mode changes to "Away" + sun below horizon + before 11 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Activate "Away Lights" scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Create scene with desired lights, use sun.sun for sunset
          <br>
          <strong>Note:</strong> Create separate 11 PM automation to turn off all lights
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
        <span class="step-content">Mode is Away AND Time is sunset to 11 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Activate Away Lights scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create second routine for 11 PM turn-off
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
        <span class="step-content">Mode changes to Away OR sunset occurs</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Mode is Away AND time before 11 PM AND after sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on Away Lights group</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Create group with selected devices, use Rule Machine
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
        <span class="step-content">Last person leaves + sunset to 11 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Activate "Away Lights" scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create separate 11 PM automation to turn off
        </div>
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
        <span class="step-content">Mode changes to Away AND after sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on Away Lights devices</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Separate routine for 11 PM turn-off
        </div>
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
        <span class="step-content">Everyone leaves + after sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on away lights group</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Scheduled routine at 11 PM to turn off
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Randomized lighting patterns</h3>
    <p>Make the pattern less predictable and more realistic:</p>
    <ul>
      <li><strong>Staggered timing:</strong> Living room at sunset, kitchen 15 min later</li>
      <li><strong>Random delays:</strong> 5-10 minute variations each day</li>
      <li><strong>Room rotation:</strong> Different rooms on different nights</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Vacation mode enhancement</h3>
    <p>During extended absences, enhance the pattern:</p>
    <ul>
      <li><strong>Multiple rooms:</strong> Rotate throughout evening</li>
      <li><strong>Dinner simulation:</strong> Kitchen early, living room later</li>
      <li><strong>Blind movement:</strong> Open in morning, close at dusk</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>TV simulator integration</h3>
    <p>Add realistic glow for enhanced effect:</p>
    <ul>
      <li>FakeTV device or smart LED strip</li>
      <li>Position where visible from outside</li>
      <li>Colored smart bulb with random color scenes</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Motion-activated exterior</h3>
    <p>Combine with motion-triggered outdoor lighting:</p>
    <ul>
      <li>Exterior motion sensors trigger bright lights</li>
      <li>Stays on for 5-10 minutes</li>
      <li>Startles potential intruders and activates cameras</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights come on during daytime</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sunset condition not working or time zone incorrectly set.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify sunset trigger or condition is active</li>
        <li>Check platform time zone settings</li>
        <li>Add explicit "after sunset" condition</li>
        <li>Use lux sensor as alternative to sunset</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights don't turn off at scheduled time</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Automation scheduled wrong or mode changed unexpectedly.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check 11 PM automation trigger</li>
        <li>Verify mode is still "Away"</li>
        <li>Check for conflicting automations</li>
        <li>Add logging to troubleshoot</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Pattern looks too predictable</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Same lights, same time every day with no variation.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add random time offsets (5-15 minutes)</li>
        <li>Rotate which rooms are used</li>
        <li>Include occasional TV simulator or fireplace</li>
        <li>Vary turn-off time slightly</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

### Light selection

**Good Choices:**
✅ Living room - visible from street
✅ Kitchen - common evening activity area
✅ One bedroom - suggests someone home
✅ Entry/foyer - normal usage pattern

**Avoid:**
❌ Every room lit - looks suspicious
❌ Outdoor lights only - no interior activity
❌ Basement/attic - unusual pattern
❌ Bathroom only - strange choice

### Timing considerations

**Natural Patterns:**
- Lights on after sunset
- Activity in kitchen 5-8 PM (dinner)
- Living room 7-11 PM (relaxing)
- Bedroom 10-11 PM (winding down)
- All off by 11 PM (sleep)

**Avoid:**
- Lights on 24/7
- Exact same time every day
- Lights on before sunset
- Lights off at unusual times

### Security layering

**Combine With:**
- Motion-activated exterior lights
- Camera recording
- Smart door locks
- Alarm system
- Neighbor alerts

---

**Related automations:**
- [Away mode automation](/automation/daily-routines/away-mode/)
- [Fire safety response](/automation/security/fire-safety/)
- [Outdoor night lights](/automation/lighting/outdoor-night-lights/)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
