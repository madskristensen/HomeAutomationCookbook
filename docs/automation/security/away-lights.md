---
layout: default
title: Away Lights Automation - Make Your Home Look Occupied
description: Deter break-ins and package theft by making your home look occupied with strategic away lighting automation. Complete setup guide.
keywords: away lights, security lighting, home occupied simulation, break-in prevention, package theft prevention, smart home security
---

# Turn on away lights

Turning on a few strategic lights in the house can make it look like you are home and deter potential thieves from breaking in or stealing packages from the porch. If your smart electric fireplace is also on, you can make it look even more convincing.

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
    <h4>Home Assistant</h4>
    <ol>
      <li>Create "Away Lights" scene with desired lights</li>
      <li>Automation 1: Trigger on mode change to "Away" + sun below horizon + before 11 PM → Activate scene</li>
      <li>Automation 2: Trigger at 11 PM + mode is "Away" → Turn off all lights</li>
      <li>Use sun.sun entity for sunset detection</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Create "Away Lights" scene in app</li>
      <li>Routine 1: IF Mode is Away AND Time is sunset to 11 PM → THEN Activate Away Lights scene</li>
      <li>Routine 2: IF Time is 11 PM AND Mode is Away → THEN Turn off all lights</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Create group "Away Lights" with selected devices</li>
      <li>Use Rule Machine for complex time + mode logic</li>
      <li>Trigger: Mode changes to Away OR sunset occurs</li>
      <li>Conditions: Mode is Away AND time before 11 PM AND after sunset</li>
      <li>Action: Turn on Away Lights group</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>Create "Away Lights" scene</li>
      <li>Automation: When last person leaves + sunset to 11 PM → Activate scene</li>
      <li>Automation: At 11 PM when no one home → Turn off lights</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>Create "Away Lights" routine with device group</li>
      <li>Trigger: When mode changes to Away AND after sunset</li>
      <li>Action: Turn on Away Lights devices</li>
      <li>Separate routine for 11 PM turn-off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Create device group for away lights</li>
      <li>Starter: When everyone leaves + after sunset</li>
      <li>Action: Turn on away lights group</li>
      <li>Scheduled routine at 11 PM to turn off</li>
    </ol>
  </div>
</div>

## Advanced features

### Randomized lighting patterns

Make the pattern less predictable and more realistic:

**Staggered Timing:**
- Living room on at sunset
- Kitchen on 15 minutes later
- Bedroom on 30 minutes later
- Random 5-10 minute variations each day

**Random Delays:**
Use random delay functions (if available) to vary timing by a few minutes each day.

### Vacation mode enhancement

During extended absences, enhance the pattern:

**Multiple Rooms:**
- Rotate which rooms are lit throughout evening
- Kitchen early (dinner time simulation)
- Living room later (TV time)
- Brief bathroom light usage

**Blind/Shade Movement:**
- Open in morning
- Close at dusk
- Adds realism to occupied appearance

### TV simulator integration

Add a TV simulator for realistic glow:

**Options:**
- FakeTV device (dedicated product)
- Smart LED strip programmed for TV patterns
- Colored smart bulb with random color scenes

**Placement:**
- Position where TV glow would be visible from outside
- Behind furniture or in corner
- Visible through front-facing windows

### Motion-activated exterior

Combine away lights with motion-triggered outdoor lighting:

**Setup:**
- Exterior motion sensors
- Bright outdoor lights
- Triggered when motion detected
- Stays on for 5-10 minutes

**Benefits:**
- Startles potential intruders
- Illuminates anyone approaching
- Activates camera recording

## Troubleshooting

### Issue: Lights come on during daytime

**Causes:**
- Sunset condition not working
- Time zone incorrectly set
- Missing condition check

**Solutions:**
✅ Verify sunset trigger or condition is active
✅ Check platform time zone settings
✅ Add explicit "after sunset" condition
✅ Use lux sensor as alternative to sunset

### Issue: Lights don't turn off at scheduled time

**Causes:**
- Automation scheduled wrong
- Time condition conflict
- Mode changed unexpectedly

**Solutions:**
✅ Check 11 PM automation trigger
✅ Verify mode is still "Away"
✅ Check for conflicting automations
✅ Add logging to troubleshoot

### Issue: Pattern looks too predictable

**Causes:**
- Same lights, same time every day
- Obvious on/off pattern
- No variation

**Solutions:**
✅ Add random time offsets (5-15 minutes)
✅ Rotate which rooms are used
✅ Include occasional TV simulator or fireplace
✅ Vary turn-off time slightly

### Issue: Lights come on when arriving home

**Causes:**
- Delay between arrival and mode change
- Away mode not transitioning quickly
- Automation still processing

**Solutions:**
✅ Ensure Home mode triggers immediately on arrival
✅ Add condition: only if mode is still Away
✅ Add small delay before activating away lights
✅ Check that mode automation runs before light automation

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
