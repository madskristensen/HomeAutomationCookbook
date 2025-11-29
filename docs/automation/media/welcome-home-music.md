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
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Home mode changes from 'Away' to 'Home'</li>
      <li>Condition: Time is after 4 PM</li>
      <li>Action: Activate welcome scene, Set volume 35%</li>
      <li>Play welcome playlist from Spotify</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF Home mode changes to "Home"</li>
      <li>AND Time is after 4:00 PM</li>
      <li>THEN Turn on welcome scene</li>
      <li>THEN Play music, Set volume 35%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Mode Manager for presence detection</li>
      <li>Trigger: Mode changes to "Home"</li>
      <li>Condition: Time is after 4 PM</li>
      <li>Action: Set volume 35%, Play welcome playlist</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: First person arrives home</li>
      <li>Conditions: Time is after 4:00 PM</li>
      <li>Do: Welcome scene, Play music on HomePod</li>
      <li>Set volume to 35%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: You arrive home (location-based)</li>
      <li>Condition: Time after 4:00 PM</li>
      <li>Action: Turn on lights, Play Spotify music</li>
      <li>Alexa says "Welcome home"</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: When you get home (location)</li>
      <li>Condition: Time after 4:00 PM</li>
      <li>Action: Activate welcome scene</li>
      <li>Play music, Adjust volume to 35%</li>
    </ol>
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
- [Play music when shower starts](/automation/media/shower-music/)
- [Control music with physical switch](/automation/media/music-switch-control/)
- [Morning routine automation](/automation/presence/morning-routine/)

<div class="page-navigation">
  <a href="/automation/media/">← Back to Media Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
