---
layout: automation
title: Automatic Coffee Maker in the Morning
description: Wake up to freshly brewed coffee automatically. Smart plug method for starting coffee maker on schedule.
keywords: coffee maker automation, automatic coffee morning, morning coffee routine, smart plug coffee, scheduled coffee, wake up coffee, automatic brewing
---

# Start coffee maker in the morning

There is something deeply civilized about waking to the smell of fresh coffee - not fumbling bleary-eyed to start the machine, but finding it already brewed, patiently waiting. A simple smart plug and a bit of timing turn morning chaos into morning ritual.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Morning Convenience</h4>
    <ul>
      <li><strong>Morning Coffee Ready</strong> - Coffee brewing when alarm goes off</li>
      <li><strong>Automatic Weekday Brewing</strong> - Consistent work morning routine</li>
      <li><strong>When Shower Ends</strong> - Time coffee to finish as you're ready</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Lifestyle Benefits</h4>
    <ul>
      <li><strong>Wake-Up Motivation</strong> - Smell of coffee helps you get up</li>
      <li><strong>Guest Accommodation</strong> - Auto-brew when guests staying over</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Plug or Smart Outlet</strong>
      <div class="product-details">
        Popular brands: TP-Link Kasa, Wyze, Wemo, Zigbee plugs<br>
        Schedule capability • Reliable automation
      </div>
    </div>
    
    <div class="product-item">
      <strong>Compatible Coffee Maker</strong>
      <div class="product-details">
        Must start automatically when power applied<br>
        Simple/old coffee makers work best • Some programmable models work<br>
        <strong>Critical:</strong> Won't work if button must be pressed after power on
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        Start coffee when you wake up/move around
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Grinder</strong>
      <div class="product-details">
        On separate smart plug for fresh-ground beans
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>✅ Test Coffee Maker Compatibility</strong>
  <ul>
    <li>Fill coffee maker with water and grounds</li>
    <li>Turn coffee maker switch to "on" position</li>
    <li>Unplug it, then plug it back in</li>
    <li>Does it start brewing? YES = Compatible! NO = Not compatible</li>
    <li>Compatible: Old/simple coffee makers, some programmable models</li>
    <li>Not Compatible: Requires button press, touchscreen, most pod machines</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF time is 7:00 AM on weekdays
AND coffee maker plug is OFF (loaded and ready)
THEN turn on coffee maker plug
AND send notification "Coffee brewing ☕"</div>

<div class="info-box">
  <strong>🌙 Night Before Preparation</strong>
  <ul>
    <li>Fill coffee maker with water and grounds</li>
    <li>Turn coffee maker switch to "on" position</li>
    <li>Press physical button on smart plug to turn it OFF</li>
    <li>(Turning plug off signals the automation coffee maker is ready)</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>7:00 AM Monday-Friday</li>
      <li>OR when shower turns on</li>
      <li>OR when bedroom motion detected</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Smart plug is currently OFF:</strong> Confirms coffee maker is loaded and ready<br>
    <strong>Purpose:</strong> Prevents turning on empty coffee maker
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on smart plug</li>
      <li>Coffee starts brewing!</li>
      <li>Optional: Send notification "Coffee brewing"</li>
    </ul>
  </div>
</div>

<div class="info-box">
  <strong>⚠️ Critical Safety: Auto-Shutoff Required</strong>
  <ul>
    <li>Always implement 30-minute auto-shutoff automation</li>
    <li>Use smart plug rated for coffee maker wattage (800-1200W)</li>
    <li>Clean coffee maker regularly to prevent fire hazard</li>
    <li>Don't leave house during first few automated cycles</li>
  </ul>
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
        <span class="step-content">Time is 7:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Weekdays, Plug is OFF (ready)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on coffee maker plug</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Safety:</strong> Auto-shutoff after 30 minutes
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
        <span class="step-content">Time is 7:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Day is Mon-Fri, Plug is OFF</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on coffee maker plug</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Safety:</strong> Create routine to turn off after 30 min
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
        <span class="step-content">Time is 7:00 AM, Weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Plug is OFF</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on plug, Auto-shutoff after 30 min</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Simple Automation Rules or Rule Machine
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
        <span class="step-content">Time is 7:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Weekdays only</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on coffee maker plug</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Safety:</strong> Create separate auto-shutoff after 30 min
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
        <span class="step-content">Schedule 7:00 AM weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on coffee maker plug</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Safety:</strong> Turn off after 30 minutes
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
        <span class="step-content">Time 7:00 AM on weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on coffee maker plug</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Add separate safety shutoff routine
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

### Voice-activated coffee

Make coffee on demand:

Create automation triggered by voice command (e.g., Alexa actionable notification) that turns on coffee maker plug if it's currently off (loaded and ready).

Say: "Alexa, start coffee"

### Pre-warm before arrival

Start coffee when arriving home:

Create automation with these elements:
- **Trigger:** Person arrives home
- **Conditions:** Morning hours (6am-10am) AND coffee maker plug is OFF
- **Action:** Turn on coffee maker plug

### Multi-stage morning

Coordinate with other morning routines:

Create automation that runs at wake-up time:
1. Turn on coffee maker plug
2. Gradually increase bedroom light brightness (start at 10%, transition over 60 seconds)
3. Wait 5 minutes
4. Brighten lights to 100% over 30 seconds

## Alternative triggers

### Smart alarm clock integration

Start coffee when alarm dismissed:

If using phone alarm with Home Assistant, trigger coffee maker when mobile app sends alarm dismissed event.

### Presence + time

Only brew if someone home:

Add conditions to automation:
- At least one person is home
- Time is between 6am and 9am

### Weather-based

Skip on very hot days:

Add condition: Only brew if outdoor temperature is below 75°F (don't brew hot coffee when already hot outside)

## Troubleshooting

### Issue: Coffee maker doesn't start

**Causes:**
- Coffee maker incompatible (requires button press)
- Smart plug didn't turn on
- Coffee maker switch not in "on" position
- Automation didn't trigger

**Solutions:**
✅ Re-test coffee maker compatibility (unplug/plug test)
✅ Verify smart plug turns on via app manually
✅ Check coffee maker physical switch is "on"
✅ Review automation logs to see if it triggered
✅ Ensure coffee maker switch wasn't accidentally turned off
✅ Try different coffee maker model if current one incompatible

### Issue: Empty coffee maker turns on

**Causes:**
- Forgot to prepare coffee maker night before
- Smart plug already on (not turned off in prep)
- Automation has no check for "ready" state
- Weekend automation triggered

**Solutions:**
✅ Add condition: Smart plug must be OFF before turning on
✅ Create reminder notification evening before: "Prepare coffee maker"
✅ Add weekday-only condition if don't want weekend coffee
✅ Visual reminder (dashboard tile) showing coffee maker status

Create evening reminder automation:
- **Trigger:** Time is 9:00 PM
- **Condition:** Weeknights (Sun-Thu, night before weekdays)
- **Action:** Send notification "Reminder: Prepare coffee maker for tomorrow morning"

### Issue: Coffee burns or overheats

**Causes:**
- No automatic shutoff implemented
- Coffee maker left on too long
- Heating plate continues heating
- Safety timer not working

**Solutions:**
✅ **Always implement 30-minute auto-shutoff** (shown in examples)
✅ Use coffee maker with auto-shutoff feature
✅ Add notification when shutting off
✅ Test smart plug reliability
✅ Use thermal carafe coffee maker (no heating plate)
✅ Monitor with power monitoring plug (detect malfunction)

Create emergency shutoff automation:
- **Trigger:** Coffee maker plug has been ON for 45 minutes (maximum safe time)
- **Action 1:** Turn off coffee maker plug
- **Action 2:** Send high-priority notification "SAFETY: Coffee maker auto shut-off"

## Safety best practices

### ⚠️ Important Safety Rules

1. **Always use auto-shutoff automation** (30-45 minutes maximum)
2. **Never automate coffee maker without testing compatibility first**
3. **Use smart plug rated for coffee maker wattage** (typically 800-1200W)
4. **Don't leave house with coffee maker automating** (first few times)
5. **Clean coffee maker regularly** to prevent fire hazard
6. **Replace old coffee makers** - worn heating elements dangerous

### Recommended features

✅ Coffee maker with built-in auto-shutoff
✅ Smart plug with power monitoring (detect malfunctions)
✅ Multiple shutoff methods (time-based + power-based)
✅ Notifications when coffee maker turns on/off
✅ Manual override easily accessible

---

**Related automations:**
- [Morning routine automation](/automation/daily-routines/morning-routine/)
- [Play music when shower starts](/automation/entertainment/shower-music/)
- [Turn on bathroom fan when starting shower](/automation/climate/fan-shower/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliance Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
