---
layout: automation
title: Gradual Wake-Up Lighting - Sunrise Simulation Alarm
description: Wake up gently with gradually brightening lights that simulate sunrise. A natural alternative to jarring alarms that improves your morning routine.
keywords: wake up lights, sunrise alarm, gradual lighting, morning light automation, sleep automation, circadian lighting, gentle wake up
---

# Gradual wake-up lighting

Waking up to a blaring alarm in a dark room can leave you feeling groggy and disoriented. Gradual wake-up lighting simulates a natural sunrise, slowly brightening your bedroom over 15-30 minutes to help you wake more naturally and start your day feeling refreshed.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Better mornings</h4>
    <ul>
      <li><strong>Dark winter mornings</strong> - Wake up before natural sunrise</li>
      <li><strong>Deep sleepers</strong> - Light helps transition from sleep gradually</li>
      <li><strong>Light sleepers nearby</strong> - Partner stays asleep while you wake</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Health and wellness</h4>
    <ul>
      <li><strong>Circadian rhythm</strong> - Light cues help regulate sleep cycle</li>
      <li><strong>Seasonal affective disorder</strong> - Morning light exposure helps mood</li>
      <li><strong>Gentle transition</strong> - Less stressful than sudden alarm</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Dimmable smart bulb or light strip</strong>
      <div class="product-details">
        Brands: Philips Hue, LIFX, Sengled, Wyze, Govee<br>
        Features: Dimming from 1-100%, color temperature adjustment (warm to cool white)<br>
        Placement: Bedside lamp, ceiling light, or light strip behind headboard
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Color-changing bulb</strong>
      <div class="product-details">
        Start with warm red/orange, transition to cool white<br>
        More closely simulates actual sunrise colors
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart blinds</strong>
      <div class="product-details">
        Coordinate with natural light by opening blinds as lights brighten<br>
        Brands: Ikea Fyrtur, Somfy, Lutron Serena
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart speaker</strong>
      <div class="product-details">
        Add gentle audio (birds, soft music) at end of wake cycle<br>
        Announce weather and schedule when fully awake
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Bulb placement tips</strong>
  <ul>
    <li><strong>Bedside:</strong> Closest to eyes, most effective</li>
    <li><strong>Ceiling:</strong> Fills room but less direct on face</li>
    <li><strong>Light strip behind headboard:</strong> Indirect, diffused light</li>
    <li><strong>Multiple locations:</strong> Combine for best effect</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">AT 6:00 AM on weekdays
START light at 1% warm white
OVER 30 minutes gradually increase to 100% cool white
AT 6:30 AM play gentle wake-up sound</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation: Gradual wake-up</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 30 minutes before desired wake time</li>
      <li>Example: 6:00 AM for 6:30 AM wake time</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Day is weekday (Mon-Fri) - or create separate weekend schedule</li>
      <li>Optional: Vacation mode is off</li>
      <li>Optional: Someone is in bed (presence sensor)</li>
    </ul>
    <h4>Actions (sequence over 30 minutes)</h4>
    <ul>
      <li>Set light to 1% brightness, warm white (2700K)</li>
      <li>Gradually increase to 25% over 10 minutes</li>
      <li>Gradually increase to 50% over next 10 minutes, shift to neutral (3500K)</li>
      <li>Gradually increase to 100% over final 10 minutes, shift to cool white (5000K)</li>
      <li>At end: Play gentle alarm sound or announcement</li>
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
        <span class="step-content">Time is 6:00 AM on weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">light.turn_on with transition: 1800 (30 min), brightness: 255</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use script with multiple steps for color temperature changes
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
        <span class="step-content">Time is 6:00 AM, Mon-Fri</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Set light level to 1%, then gradually increase</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> May need multiple timed routines for gradual effect
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
        <span class="step-content">Time is 6:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Day is weekday</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Fade light to 100% over 30 minutes</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with dimmer action and transition time
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
        <span class="step-content">Time is 6:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Weekdays only</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Set scene with transition</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Create "Sunrise" scene, may need Shortcuts for long transitions
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
        <span class="step-content">Schedule: 6:00 AM, Mon-Fri</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on light to 5%, wait 5 min, set to 15%, etc.</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use wait actions between brightness steps
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
        <span class="step-content">6:00 AM on weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Adjust lights with gentle wake feature</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Works well with compatible lights like Philips Hue
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Sunrise color simulation</h3>
    <p>Mimic natural sunrise colors:</p>
    <ul>
      <li><strong>0-10 min:</strong> Deep red/orange (1800K), 1-10%</li>
      <li><strong>10-20 min:</strong> Warm orange/yellow (2700K), 10-40%</li>
      <li><strong>20-30 min:</strong> Neutral white (4000K), 40-70%</li>
      <li><strong>30+ min:</strong> Cool daylight (5500K), 70-100%</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Alarm integration</h3>
    <p>Sync with phone or smart speaker alarm:</p>
    <ul>
      <li>Start light 30 min before alarm rings</li>
      <li>At alarm time, announce weather and calendar</li>
      <li>Play gentle music or nature sounds</li>
      <li>Pause if snooze is pressed</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Weekend flexibility</h3>
    <p>Different schedule for non-work days:</p>
    <ul>
      <li>Later start time (8:00 AM vs. 6:00 AM)</li>
      <li>Longer transition (45 min instead of 30)</li>
      <li>Option to disable entirely on weekends</li>
      <li>Holiday calendar integration</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Partner-friendly mode</h3>
    <p>Wake one person without disturbing the other:</p>
    <ul>
      <li>Use bedside lamp on one side only</li>
      <li>Lower maximum brightness (50% instead of 100%)</li>
      <li>Direct light away from sleeping partner</li>
      <li>Add gentle vibrating alarm under pillow</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Smart blinds coordination</h3>
    <p>Combine artificial and natural light:</p>
    <ul>
      <li>Begin opening blinds at mid-point of wake cycle</li>
      <li>Full open when lights reach 100%</li>
      <li>In summer, may need less artificial light</li>
      <li>In winter, artificial light compensates for late sunrise</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights are too bright too fast</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Transition feels jarring, not gradual enough.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Increase transition time (try 45-60 minutes)</li>
        <li>Start at lower brightness (1% instead of 5%)</li>
        <li>Use bulb behind diffuser for softer light</li>
        <li>Position light to bounce off wall instead of direct</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Bulb doesn't dim low enough</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Minimum brightness still too bright to start.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Choose bulb with good low-end dimming (Philips Hue excels here)</li>
        <li>Use lower wattage bulb</li>
        <li>Add dimmer shade or diffuser</li>
        <li>Point light away from bed initially</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Transition not smooth</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Light jumps in steps instead of smooth fade.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check bulb supports transition time in platform</li>
        <li>Use longer transition command if supported</li>
        <li>Create more intermediate steps in automation</li>
        <li>Some platforms handle transitions better than others</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Wakes partner too early</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Light disturbs partner who wakes later.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Use bedside lamp only on your side</li>
        <li>Lower maximum brightness</li>
        <li>Position light to face away from partner</li>
        <li>Consider eye mask for partner</li>
        <li>Use smart blinds on one side of room only</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

### Timing recommendations

**Wake-up transition duration:**
- **Minimum:** 15 minutes (noticeable but quick)
- **Recommended:** 30 minutes (natural feeling)
- **Extended:** 45-60 minutes (very gradual, deep sleepers)

**Start time calculation:**
- Desired wake time minus transition duration
- Example: Wake at 6:30 AM with 30-min transition = Start at 6:00 AM

### Light placement

**Most effective positions:**
- Bedside table lamp facing slightly toward headboard
- Light strip behind headboard (diffused, indirect)
- Ceiling fixture with dimmer (fills room evenly)

**Less effective:**
- Light behind you (can't see it while lying in bed)
- Light in hallway (too far, limited effect)
- Covered or obstructed positions

### Bulb selection

**Key features:**
- Wide dimming range (1% to 100%)
- Adjustable color temperature (2700K to 5500K)
- Reliable transition time support
- Quiet operation (some bulbs buzz at low levels)

**Recommended bulbs:**
- Philips Hue (excellent low-end dimming)
- LIFX (great color range, no hub needed)
- Sengled (budget-friendly option)

### Schedule management

**Weekday vs. weekend:**
- Separate automations for different schedules
- Or use day-of-week conditions
- Consider holidays and vacation mode

**Flexibility:**
- Voice command to skip tomorrow's wake-up
- Dashboard toggle for quick disable
- Alarm clock sync if possible

---

**Related automations:**
- [Morning routine automation](/automation/daily-routines/morning-routine.html)
- [Bedtime routine automation](/automation/daily-routines/bedtime-routine.html)
- [Blinds at sunset/sunrise](/automation/climate/blinds-sunset-sunrise.html)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
