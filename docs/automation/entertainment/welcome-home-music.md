---
layout: default
title: Play Music When Arriving Home - Welcome Automation
description: Automatically start music when you arrive home. Create a welcoming atmosphere with automatic audio.
keywords: welcome home music, arrival music automation, automatic music greeting, home mode music, presence detection music, greeting automation, arrival routine
---

# Play music when you come home

Coming home to a house with lights on and music playing feels welcoming. It's the little touches that make a house feel like home.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Daily Arrivals</h4>
    <ul>
      <li><strong>After Work Greeting</strong> - Welcome yourself home after long day</li>
      <li><strong>Morning Wake-Up</strong> - Greet you as morning routine starts</li>
      <li><strong>Energy Boost</strong> - Uplifting music when arriving home</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Atmosphere</h4>
    <ul>
      <li><strong>Pleasant Atmosphere</strong> - Create welcoming ambiance automatically</li>
      <li><strong>Guest Welcome</strong> - Music plays when guests arrive</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Speaker/Music System</strong>
      <div class="product-details">
        Popular brands: Sonos, Amazon Echo, Google Home, Apple HomePod<br>
        Single room or multi-room audio • WiFi connectivity • Streaming service integration
      </div>
    </div>
    
    <div class="product-item">
      <strong>Presence Detection</strong>
      <div class="product-details">
        Phone app/GPS location services, Smart lock unlock detection, OR Garage door sensor<br>
        Platforms: Home Assistant, SmartThings, Life360
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Multiple Speakers</strong>
      <div class="product-details">
        Music in entry, kitchen, and living room for full-home welcome
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Lights</strong>
      <div class="product-details">
        Also turn on lights when arriving for complete welcome scene
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF person arrives home
AND time between 5:00 PM - 9:00 PM
THEN play welcome playlist on main speaker
AND set volume to 35%</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Home goes into Home mode (when first person arrives)</li>
      <li>OR specific person arrives home</li>
      <li>OR morning routine starts (wake-up music)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>NOT between 7 AM - 10 AM:</strong> If you don't want morning music<br>
    <strong>Time is after 4 PM:</strong> Only afternoon/evening arrivals<br>
    <strong>Music not already playing:</strong> Don't interrupt existing playback
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Play music on selected speakers</li>
      <li>Set volume to appropriate level</li>
      <li>Optionally announce "Welcome home"</li>
      <li>Optional: Turn on lights, unlock door</li>
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
        <span class="step-content">Home mode changes from 'Away' to 'Home'</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time is after 4 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Activate welcome scene, Set volume 35%, Play playlist</span>
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
        <span class="step-content">Home mode changes to "Home"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Time is after 4:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on welcome scene, Play music, Set volume 35%</span>
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
        <span class="step-content">Mode changes to "Home"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time is after 4 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set volume 35%, Play welcome playlist</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Mode Manager for presence detection
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
        <span class="step-content">Time is after 4:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Welcome scene, Play music, Set volume 35%</span>
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
        <span class="step-content">You arrive home (location-based)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time after 4:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on lights, Play music, Alexa says "Welcome home"</span>
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
        <span class="step-content">When you get home (location)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time after 4:00 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Activate welcome scene, Play music, Adjust volume</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

### Speaker selection by time and arrival

**Smart grouping:**

Adjust which speakers play based on arrival time:
- **Afternoon arrival (4-7 PM):** Entry, kitchen, living room speakers play "after work playlist"
- **Morning routine (6-10 AM):** Bedroom, bathroom, kitchen speakers play morning news radio
- **Evening arrival (after 7 PM):** Living room and dining room only play "evening relaxing" playlist

Use conditional logic based on current time to select appropriate speakers and content.

### Time-based volume levels

Adjust volume based on time of day:
- **Morning (6-10 AM):** 20% volume
- **Daytime (10 AM - 6 PM):** 40% volume
- **Evening (6-10 PM):** 35% volume
- **Late night (after 10 PM):** 15% volume

Use template logic to check current hour and set appropriate volume.

### Auto-stop after duration

Stop music after certain time if no interaction:

Create automation:
- **Trigger:** Music has been playing for 30 minutes
- **Condition:** Welcome music flag is active
- **Actions:**
  - Stop music playback
  - Turn off welcome music flag

### Voice announcement

Combine with greeting:
- First: Play voice greeting "Welcome home, [name]!"
- Wait 3 seconds for greeting to finish
- Then: Start playing music playlist

## Troubleshooting

### Issue: Music plays every time door opens

**Causes:**
- Triggering on door sensor instead of presence
- No condition to check if already home
- Triggering when leaving and returning briefly
- Family members arriving separately trigger multiple times

**Solutions:**
✅ Use home mode change (Away → Home) not door sensor
✅ Add condition: Only if music not already playing
✅ Add delay: Only if away for at least 30 minutes
✅ Use cooldown: Only play once per 2-hour period
✅ Track automation: Set flag when music plays, reset after time

**Cooldown example:**
Add condition to check that automation hasn't triggered in last 2 hours (7200 seconds) by checking last triggered time.

### Issue: Music volume inappropriate

**Causes:**
- Fixed volume doesn't suit all times of day
- Previous manual adjustment not considered
- Room acoustics vary
- Other household members affected

**Check:**
- ✅ Use time-based volume (shown in Advanced Features)
- ✅ Lower volume for late arrivals (after 9 PM)
- ✅ Higher volume for afternoon (4-7 PM)
- ✅ Consider who's home - quieter if kids sleeping
- ✅ Test volume in actual conditions (with people talking, etc.)

**Fix:**
Use template logic to set volume based on hour:
- If after 9 PM: 15% volume
- If after 6 PM: 30% volume  
- Otherwise: 40% volume

### Issue: Presence detection unreliable

**Causes:**
- Phone GPS inaccurate
- WiFi-based detection has delays
- Router drops phone connection
- Battery saver mode disabling location
- Multiple phones not synchronized

**Solutions:**
✅ Use multiple detection methods (GPS + WiFi + Bluetooth)
✅ Set arrival zone radius appropriately (100-200m)
✅ Combine with garage door sensor or door unlock
✅ Disable battery optimization for home automation app
✅ Use Life360 or similar reliable presence app
✅ Add short delay (2-3 minutes) to allow all sensors to update

**Multi-method example:**
Use multiple triggers for reliability:
- GPS arrival
- OR garage door opens
- OR front door unlocks

This ensures music plays even if one detection method fails.

---

**Related automations:**
- [Play music when shower starts](/automation/entertainment/shower-music/)
- [Control music with physical switch](/automation/entertainment/music-switch-control/)
- [Morning routine automation](/automation/daily-routines/morning-routine/)

<div class="page-navigation">
  <a href="/automation/entertainment/">← Back to Entertainment</a>
  <a href="/automation/">View All Automations →</a>
</div>
