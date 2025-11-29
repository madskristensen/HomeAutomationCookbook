---
layout: default
title: Outdoor Night Lights Automation - Smart Exterior Lighting
description: Automatically turn on outdoor lights at dusk for safety, aesthetics, and convenience. Complete setup guide with sunset/lux sensor options.
keywords: outdoor lights automation, sunset lights, dusk lighting, exterior lighting, holiday lights, smart outdoor lights, curb appeal
---

# Turn on outdoor night lights

Having lights on around the outside of your house is great for several reasons. It lights up the way when you walk outside, it lights up the driveway, it deters trespassing, and it looks great.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Daily Lighting</h4>
    <ul>
      <li><strong>Driveway Illumination</strong> - Light the way when coming home after dark</li>
      <li><strong>Pathway Safety</strong> - Prevent trips and falls on walkways</li>
      <li><strong>Curb Appeal</strong> - Your home looks welcoming and well-maintained</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Special Occasions</h4>
    <ul>
      <li><strong>Holiday Lights</strong> - Automatically control seasonal decorations</li>
      <li><strong>Landscape Lighting</strong> - Showcase landscaping features</li>
      <li><strong>Security Deterrence</strong> - Well-lit homes discourage trespassing</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Lights (any type)</strong>
      <div class="product-details">
        Options:<br>
        • Smart outdoor light fixtures<br>
        • Smart plugs for existing lights or holiday lights<br>
        • Smart light switches controlling outdoor circuits<br>
        • Smart bulbs in weatherproof fixtures
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Illumination/Lux Sensor</strong>
      <div class="product-details">
        Measures actual light levels instead of relying on sunset time<br>
        More accurate for cloudy days and seasonal variations
      </div>
    </div>
    
    <div class="product-item">
      <strong>Motion Sensors</strong>
      <div class="product-details">
        For motion-activated exterior lighting in addition to scheduled
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Sunset vs. Lux Sensor</strong>
  <p>Using sunset/sunrise times will be good enough for most cases, but not all. The amount of light varies significantly based on the time of year and current weather conditions. Using an illumination sensor that measures how light it is greatly improves the precision.</p>
</div>

## Basic automation setup

<div class="automation-example">IF time is one hour before sunset
THEN turn on outdoor lights</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation 1: Turn on at dusk</h4>
    <h4>Triggers</h4>
    <ul>
      <li>An hour before sunset</li>
      <li>OR Sunset time</li>
      <li>OR Lux drops below 200 (if using lux sensor)</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>None (always turn on at dusk)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Turn on outdoor lights</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Automation 2: Turn off at dawn</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Sunrise time</li>
      <li>OR Lux rises above 300 (if using lux sensor)</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>None</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Turn off outdoor lights</li>
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
        <span class="step-content">sun.sun goes below horizon (offset: -01:00:00 for hour before)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on outdoor light group</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create second automation: sun rises → Turn off outdoor lights
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
        <span class="step-content">Time is at sunset (or offset)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on outdoor lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create second routine for sunrise turn-off
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
        <span class="step-content">Sunset with optional offset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on outdoor light group</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Simple Automation Rules or Rule Machine
          <br>
          <strong>Note:</strong> Create paired rule for sunrise
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
        <span class="step-content">Sunset (with offset if desired)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on outdoor lights scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Repeat for sunrise turn-off
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
        <span class="step-content">Sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on outdoor light group</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Separate routine for sunrise
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
        <span class="step-content">Sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on outdoor lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create companion sunrise routine
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Lux-based control</h3>
    <p>More accurate than time-based control:</p>
    <ul>
      <li>Install lux sensor outdoors (shaded from direct light)</li>
      <li>Trigger when lux drops below 150-250 (dusk)</li>
      <li>Turn off when lux rises above 300-500 (dawn)</li>
      <li>Accounts for cloudy days and seasonal variations</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Time-limited operation</h3>
    <p>Keep lights on for specific hours only:</p>
    <ul>
      <li><strong>Dusk to specific time:</strong> On at sunset, off at 11 PM</li>
      <li><strong>Specific window:</strong> On at sunset, off at midnight, on at 6 AM, off at sunrise</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Holiday light scheduling</h3>
    <p>Special handling for seasonal decorations:</p>
    <ul>
      <li>Add date-based conditions (Nov 15 - Jan 5)</li>
      <li>Create "Holiday Lights" virtual switch</li>
      <li>Toggle switch to enable/disable season</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Motion-enhanced lighting</h3>
    <p>Combine scheduled and motion lighting:</p>
    <ul>
      <li><strong>Dim baseline:</strong> Scheduled at 30%</li>
      <li><strong>Motion detected:</strong> Increase to 100% for 5 minutes</li>
      <li><strong>Entry path:</strong> Driveway sensor triggers path lights</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Multiple zones</h3>
    <p>Different areas, different schedules:</p>
    <ul>
      <li><strong>Front yard:</strong> Full brightness, off at 11 PM</li>
      <li><strong>Backyard:</strong> Lower brightness, off at 10 PM</li>
      <li><strong>Pathway:</strong> Dim level, all night</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn on at wrong time</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Incorrect time zone, sunset offset, or daylight saving issues.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify time zone settings</li>
        <li>Check sunset time is calculated correctly</li>
        <li>Test with manual trigger first</li>
        <li>Use lux sensor for more accuracy</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lux sensor triggers inconsistently</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sensor placement in direct sunlight or shadows from trees/buildings.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Place in north-facing location (northern hemisphere)</li>
        <li>Avoid direct sunlight on sensor</li>
        <li>Position in open area representing general light level</li>
        <li>Adjust threshold values based on testing</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights don't turn off in morning</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sunrise automation not created or conflicting rules.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Create explicit sunrise off automation</li>
        <li>Check for conflicting rules</li>
        <li>Add failsafe: Turn off if on past 8 AM</li>
        <li>Verify no manual override active</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Holiday lights on outside of season</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Date condition not set or virtual switch left on.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add date range condition</li>
        <li>Use virtual switch for easy enable/disable</li>
        <li>Create calendar reminder to update</li>
        <li>Use separate automation for holiday lights</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="placement-grid">
  <div class="placement-card">
    <h3>Light selection</h3>
    <ul>
      <li><strong>LED:</strong> Energy efficient</li>
      <li><strong>Warm white (2700-3000K):</strong> For ambiance</li>
      <li><strong>IP44+ rated:</strong> Weatherproof</li>
      <li><strong>Dimmable:</strong> Flexibility for different scenarios</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Placement</h3>
    <ul>
      <li>Entry points illuminated</li>
      <li>Pathways visible</li>
      <li>Not aimed at neighbor windows</li>
      <li>Avoid light pollution upward</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Energy efficiency</h3>
    <p>Optimize runtime for savings:</p>
    <ul>
      <li>Don't run all night if not needed</li>
      <li>Use lower brightness after midnight</li>
      <li>Motion-activated for less-used areas</li>
      <li>LED lights consume minimal power</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Neighbor considerations</h3>
    <p>Be courteous with outdoor lighting:</p>
    <ul>
      <li>Direct light downward</li>
      <li>Avoid shining into neighbor windows</li>
      <li>Consider dimming after 10 PM</li>
      <li>Use warm colors (less intrusive)</li>
    </ul>
  </div>
</div>

---

**Related automations:**
- [Away lights](/automation/security/away-lights/)
- [Motion detection lights](/automation/lighting/lights-on-motion/)
- [Dashboards](/automation/notifications/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting</a>
  <a href="/automation/">View All Automations →</a>
</div>
