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
    <h4>Home Assistant</h4>
    <ol>
      <li>Use sun.sun entity for sunset/sunrise</li>
      <li>Trigger: sun.sun goes below horizon (offset: -01:00:00 for hour before)</li>
      <li>Action: Turn on outdoor light group</li>
      <li>Second automation: sun rises → Turn off outdoor lights</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Create routine with sunset trigger</li>
      <li>IF: Time is at sunset (or offset)</li>
      <li>THEN: Turn on outdoor lights</li>
      <li>Second routine for sunrise turn-off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Simple Automation Rules or Rule Machine</li>
      <li>Trigger: Sunset with optional offset</li>
      <li>Action: Turn on outdoor light group</li>
      <li>Create paired rule for sunrise</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>Create automation with sunset trigger</li>
      <li>When: Sunset (with offset if desired)</li>
      <li>Do: Turn on outdoor lights scene</li>
      <li>Repeat for sunrise turn-off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>Create routine with schedule trigger</li>
      <li>At: Sunset</li>
      <li>Action: Turn on outdoor light group</li>
      <li>Separate routine for sunrise</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Create scheduled routine</li>
      <li>Starter: Sunset</li>
      <li>Action: Turn on outdoor lights</li>
      <li>Create companion sunrise routine</li>
    </ol>
  </div>
</div>

## Advanced features

### Lux-based control

More accurate than time-based control:

**Setup:**
1. Install lux/illumination sensor outdoors (shaded from direct light)
2. Trigger when lux drops below threshold (150-250 typical for "dusk")
3. Turn off when lux rises above threshold (300-500 typical for "dawn")

**Benefits:**
- Accounts for cloudy days (earlier dusk)
- Seasonal variations handled automatically
- More natural transition
- Works with actual light conditions

### Time-limited operation

Keep lights on for specific hours only:

**Pattern 1: Dusk to Specific Time**
- Turn on at sunset
- Turn off at 11 PM
- Saves energy overnight

**Pattern 2: Specific Window**
- Turn on at sunset
- Turn off at midnight
- Turn on at 6 AM
- Turn off at sunrise

### Holiday light scheduling

Special handling for seasonal decorations:

**Date-Based Conditions:**
- Only activate November 15 through January 5
- Different schedule for Halloween decorations
- Special patterns for holidays

**Easy Enable/Disable:**
- Create "Holiday Lights" virtual switch
- Add as condition to automation
- Toggle switch to enable/disable season

### Motion-enhanced lighting

Combine scheduled and motion lighting:

**Dim Baseline + Bright on Motion:**
- Scheduled: Outdoor lights at 30%
- Motion: Increase to 100% for 5 minutes
- Return to 30% when motion clears

**Entry Path Lighting:**
- Driveway sensor detects car
- Path lights illuminate at 100%
- Returns to normal after 10 minutes

### Multiple zones

Different areas, different schedules:

**Front Yard:**
- On at sunset
- Full brightness
- Off at 11 PM

**Backyard:**
- On at sunset
- Lower brightness
- Off at 10 PM

**Pathway:**
- On at sunset
- Dim level only
- All night

## Troubleshooting

### Issue: Lights turn on at wrong time

**Causes:**
- Incorrect time zone in platform
- Sunset offset not set correctly
- Daylight saving time issues

**Solutions:**
✅ Verify time zone settings
✅ Check sunset time is calculated correctly
✅ Test with manual trigger first
✅ Use lux sensor for more accuracy

### Issue: Lux sensor triggers inconsistently

**Causes:**
- Sensor placement in direct sunlight
- Shadows from trees/buildings
- Sensor behind glass or window

**Solutions:**
✅ Place in north-facing location (northern hemisphere)
✅ Avoid direct sunlight on sensor
✅ Position in open area representing general light level
✅ Adjust threshold values based on testing

### Issue: Lights don't turn off in morning

**Causes:**
- Sunrise automation not created
- Conflicting automation turning them on
- Manual override stuck on

**Solutions:**
✅ Create explicit sunrise off automation
✅ Check for conflicting rules
✅ Add failsafe: Turn off if on past 8 AM
✅ Verify no manual override active

### Issue: Holiday lights on outside of season

**Causes:**
- Date condition not set
- Virtual switch left on
- Automation not updated

**Solutions:**
✅ Add date range condition
✅ Use virtual switch for easy enable/disable
✅ Create calendar reminder to update
✅ Use separate automation for holiday lights

## Best practices

### Light selection

**Good Outdoor Choices:**
- LED for energy efficiency
- Warm white (2700-3000K) for ambiance
- Weatherproof rated (IP44 or higher)
- Dimmable for flexibility

**Placement:**
- Entry points illuminated
- Pathways visible
- Not aimed at neighbor windows
- Avoid light pollution upward

### Energy efficiency

**Optimize Runtime:**
- Don't run all night if not needed
- Use lower brightness after midnight
- Motion-activated for less-used areas
- LED lights consume minimal power

**Smart Scheduling:**
- Off during late night hours
- Dimmed after household bedtime
- Full brightness only when needed

### Neighbor considerations

**Be Courteous:**
- Direct light downward
- Avoid shining into neighbor windows
- Consider dimming after 10 PM
- Use warm colors (less intrusive)

---

**Related automations:**
- [Away lights](/automation/security/away-lights/)
- [Motion detection lights](/automation/motion/lights-on-motion/)
- [Dashboards](/automation/misc/dashboards/)

<div class="page-navigation">
  <a href="/automation/misc/">← Back to Misc Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
