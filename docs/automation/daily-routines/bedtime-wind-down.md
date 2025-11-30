---
layout: automation
title: Family Bedtime Wind-Down Automation - Smart Home Sleep Routine
description: Gradually dim lights, cool the house, and quiet notifications 30 minutes before bedtime. Easy cancel option for flexible sleep schedules.
keywords: bedtime automation, sleep routine, wind-down mode, evening routine, smart home bedtime, lights dim automation, sleep preparation, family bedtime
---

# Family bedtime wind-down

Sleep comes easier when the body has been gently prepared for it. Thirty minutes before bedtime, the house begins a slow exhale - lights dimming by degrees, the air cooling, notifications falling silent. It is a signal to everyone that the day is ending, that rest is near, that the time for screens and activity is drawing to a close.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Sleep preparation</h4>
    <ul>
      <li><strong>Gradual transition</strong> - Body naturally prepares for sleep</li>
      <li><strong>Consistent routine</strong> - Same wind-down every night</li>
      <li><strong>Family coordination</strong> - Everyone gets the signal it's bedtime</li>
      <li><strong>Better sleep quality</strong> - Reduced light exposure before bed</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Flexibility built-in</h4>
    <ul>
      <li><strong>Easy cancel</strong> - One tap to stay up for movie night</li>
      <li><strong>Weekend adjustment</strong> - Different schedule for weekends</li>
      <li><strong>Guest mode</strong> - Disable when entertaining</li>
      <li><strong>Vacation mode</strong> - Skip during holidays</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart lights with dimming</strong>
      <div class="product-details">
        Popular brands: Philips Hue, LIFX, Lutron, Inovelli<br>
        Must support gradual dimming and warm color temperatures
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart thermostat</strong>
      <div class="product-details">
        Brands: Ecobee, Nest, Honeywell Home<br>
        For automatic temperature adjustment before bed
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart speakers</strong>
      <div class="product-details">
        For bedtime announcement and easy voice cancellation
      </div>
    </div>
    
    <div class="product-item">
      <strong>Phone focus modes</strong>
      <div class="product-details">
        iOS Focus Mode or Android Digital Wellbeing for notification silencing
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart blinds/curtains</strong>
      <div class="product-details">
        Automatically close for privacy and light blocking
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Sleep science tip</strong>
  <ul>
    <li>Warm light (2700K or lower) helps trigger melatonin production</li>
    <li>Gradual dimming over 30 minutes mimics natural sunset</li>
    <li>Cooler room temperature (65-68°F / 18-20°C) promotes better sleep</li>
    <li>Reducing screen brightness and notifications reduces mental stimulation</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">AT 30 minutes before bedtime (e.g., 9:30 PM)
THEN announce "Bedtime wind-down starting"
AND start dimming living room lights from current level to 20% over 30 minutes
AND set thermostat to sleep temperature (68°F / 20°C)
AND activate phone Do Not Disturb mode
AND close bedroom blinds

AT bedtime (e.g., 10:00 PM)
THEN turn off all lights except nightlights
AND announce "Goodnight"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Time is 30 minutes before scheduled bedtime</li>
      <li>OR voice command "Start bedtime wind-down"</li>
      <li>OR button press on bedside table</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>Day of week:</strong> Different times for weekdays vs. weekends<br>
    <strong>Home mode:</strong> Skip if in "Guest" or "Party" mode<br>
    <strong>Vacation:</strong> Skip if vacation mode is active
  </div>
  
  <div class="setup-step">
    <h4>Actions (30 min before)</h4>
    <ul>
      <li>Send notification: "Bedtime wind-down starting - tap to cancel"</li>
      <li>Announce on speakers: "Bedtime wind-down starting"</li>
      <li>Start gradual dimming of living room lights to 20%</li>
      <li>Shift light color to warm (2700K)</li>
      <li>Set thermostat to sleep temperature</li>
      <li>Close bedroom blinds/curtains</li>
      <li>Enable phone Do Not Disturb (via Focus mode trigger)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions (at bedtime)</h4>
    <ul>
      <li>Turn off all lights except hallway/bathroom nightlights</li>
      <li>Lock front door if not already locked</li>
      <li>Arm security system in "Night" mode</li>
      <li>Announce "Goodnight" on bedroom speaker</li>
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
        <span class="step-content">Time trigger at 9:30 PM (weekdays) or 10:30 PM (weekends)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">input_boolean.vacation_mode is off</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Call script.bedtime_wind_down with gradual transitions</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use transition parameter on light.turn_on for gradual dimming over 1800 seconds (30 min)
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
        <span class="step-content">Time is 9:30 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Mode is not "Guest" or "Vacation"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Activate "Wind-Down" scene, adjust thermostat, notify</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create separate routine for actual bedtime (10 PM)
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
        <span class="step-content">Time is 9:30 PM on weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Mode is "Home" (not Guest/Vacation)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Activate wind-down scene, set thermostat, dim lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine for complex scheduling with different weekend times
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
        <span class="step-content">Time is 9:30 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Someone is home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Activate "Wind-Down" scene, close blinds, adjust thermostat</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use iOS Focus Mode integration for phone DND
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
        <span class="step-content">Time is 9:30 PM every day</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Dim lights, announce, adjust thermostat, enable DND</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Say "Alexa, cancel bedtime" to stop the routine
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
        <span class="step-label">Starter</span>
        <span class="step-content">Time is 9:30 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Dim lights, adjust thermostat, broadcast bedtime message</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use "bedtime" scheduled routine for built-in features
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Easy cancel options</h3>
    <p>Multiple ways to skip wind-down:</p>
    <ul>
      <li><strong>Voice:</strong> "Cancel bedtime" or "Skip wind-down"</li>
      <li><strong>Notification:</strong> Tap actionable notification to cancel</li>
      <li><strong>Button:</strong> Physical button by couch to postpone</li>
      <li><strong>Time extension:</strong> "Delay bedtime 1 hour"</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Adaptive scheduling</h3>
    <p>Adjust based on context:</p>
    <ul>
      <li><strong>Weekday vs. weekend:</strong> Different bedtimes</li>
      <li><strong>Seasonal:</strong> Earlier in winter, later in summer</li>
      <li><strong>Work schedule:</strong> Adjust based on calendar</li>
      <li><strong>Guest mode:</strong> Auto-disable when entertaining</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Gradual light dimming</h3>
    <p>Create natural sunset effect:</p>
    <ul>
      <li>30 min: Start at current brightness</li>
      <li>20 min: Dim to 60%, shift to warm (3000K)</li>
      <li>10 min: Dim to 30%, warmer (2700K)</li>
      <li>0 min: Dim to 10%, very warm (2200K)</li>
      <li>Bedtime: Lights off except nightlights</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Wind-down starts during activities</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lights dim while watching a movie or having guests.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add condition: TV is off or media player not playing</li>
        <li>Create "Guest Mode" that disables wind-down</li>
        <li>Add easy cancel button on coffee table</li>
        <li>Use presence to detect if guests are present</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Family on different schedules</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Parents want to stay up after kids' bedtime.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Create separate "Kids wind-down" for children's rooms only</li>
        <li>Only affect common areas at later time</li>
        <li>Use per-room automations based on occupancy</li>
        <li>Trigger adult wind-down manually or later</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Phone DND not activating</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Phone notifications still coming through during wind-down.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify Focus Mode/DND shortcut is properly configured</li>
        <li>Use scheduled Focus Mode on phone as backup</li>
        <li>Grant automation app permission to control DND</li>
        <li>Check that automation has access to iPhone/Android Focus</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights jump instead of gradual dim</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lights change brightness in steps rather than smoothly.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use transition parameter in light commands (e.g., 1800 seconds)</li>
        <li>Ensure lights support gradual dimming</li>
        <li>Some platforms need scripted step-by-step dimming</li>
        <li>Use lights designed for gradual transitions (Hue, LIFX)</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="best-practice-card">
  <h3>Creating effective wind-down</h3>
  <ol>
    <li>Start 30 minutes before desired sleep time</li>
    <li>Use gradual transitions, not sudden changes</li>
    <li>Include easy cancellation method</li>
    <li>Make voice commands intuitive: "Cancel bedtime"</li>
    <li>Don't affect all rooms - leave kitchen accessible</li>
    <li>Include announcement so family knows it's starting</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>Sudden darkness</strong> - Always use gradual dimming</li>
    <li><strong>No cancel option</strong> - People need flexibility</li>
    <li><strong>All rooms at once</strong> - Someone might need the kitchen</li>
    <li><strong>Locking thermostat</strong> - Allow manual override if too cold/hot</li>
    <li><strong>Ignoring guests</strong> - Always have guest mode option</li>
  </ul>
</div>

---

**Related automations:**
- [Bedtime routine](/automation/daily-routines/bedtime-routine/)
- [Morning routine](/automation/daily-routines/morning-routine/)
- [Wake-up lights](/automation/lighting/wake-up-lights/)

<div class="page-navigation">
  <a href="/automation/daily-routines/">← Back to Daily Routines</a>
  <a href="/automation/">View All Automations →</a>
</div>
