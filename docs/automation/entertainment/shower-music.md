---
layout: default
title: Play Music When Shower Starts - Bathroom Automation
description: Automatically play your favorite music or podcasts when you start the shower. Complete guide for bathroom entertainment automation.
keywords: shower music automation, bathroom speaker automation, automatic music, shower entertainment, smart bathroom music, bathroom audio control, morning music
---

# Play music in the bathroom when you start a shower

Having music in the bathroom is one of life's luxuries. However, remembering to turn on your favorite jam isn't always easy, especially early in the morning. Automate your shower soundtrack for the perfect start to your day.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Morning Routines</h4>
    <ul>
      <li><strong>Morning Shower Music</strong> - Automatically start your favorite playlist when shower begins</li>
      <li><strong>News Briefing</strong> - Catch up on morning news while getting ready</li>
      <li><strong>Multi-User Households</strong> - Everyone gets their preferred audio automatically</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Entertainment & Relaxation</h4>
    <ul>
      <li><strong>Podcast Listening</strong> - Continue your audiobook or podcast during shower time</li>
      <li><strong>Relaxing Bath Sounds</strong> - Calming music for evening bath routine</li>
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
        Popular brands: Amazon Echo, Google Home, Sonos, JBL waterproof speakers<br>
        Waterproof or water-resistant recommended • WiFi connectivity
      </div>
    </div>
    
    <div class="product-item">
      <strong>Trigger Option (choose one)</strong>
      <div class="product-details">
        <strong>Smart Light Switch:</strong> Trigger when shower lights turn on (easiest, most reliable)<br>
        <strong>Contact Sensor:</strong> Trigger when shower door opens (best for glass enclosures)
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Fan Switch</strong>
      <div class="product-details">
        Also turn on fan automatically with music
      </div>
    </div>
    
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        Alternative trigger option for bathroom entry
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF shower lights turn on
AND time between 6:00 AM - 10:00 AM
THEN play music on bathroom speaker
AND set volume to 35%</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers (choose one method)</h4>
    <strong>Method 1 - Light-based:</strong> Shower lights turn on<br>
    <strong>Method 2 - Door sensor:</strong> Shower door opens (contact sensor)<br>
    <strong>Method 3 - Combined:</strong> Shower lights on AND door opens (more reliable)
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>Home Mode:</strong> Home is NOT in Night mode (don't wake sleeping household)<br>
    <strong>Time-Based:</strong> Only between 6 AM and 10 AM (morning routine)<br>
    <strong>Day of Week:</strong> Only weekdays (different weekend routine)
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Play music/podcast on bathroom speaker</li>
      <li>Set volume to preset level (30-40%)</li>
      <li>Optional: Turn on bathroom fan</li>
      <li>Optional: Flash lights if doorbell rings</li>
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
    <ol>
      <li>Trigger: Shower lights turn on</li>
      <li>Condition: Home mode, Time 6-10 AM, Weekdays</li>
      <li>Action: Set bathroom speaker volume to 35%</li>
      <li>Play Spotify playlist with Spotcast service</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <ol>
      <li>IF Shower lights turn on</li>
      <li>AND Home mode "Home", Time 6-10 AM</li>
      <li>THEN Play music on bathroom speaker</li>
      <li>THEN Set speaker volume to 35%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <ol>
      <li>Use Rule Machine with speaker integration</li>
      <li>Trigger: Shower light turns on</li>
      <li>Condition: Mode is "Home", Time 6-10 AM, Weekdays</li>
      <li>Action: Set speaker volume to 35%, Play playlist</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <ol>
      <li>When: Shower light turns on</li>
      <li>Conditions: Time 6-10 AM, Weekdays only</li>
      <li>Do: Play music on HomePod/AirPlay speaker</li>
      <li>Set volume to 35%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa</h4>
    </div>
    <ol>
      <li>When: Shower light turns on</li>
      <li>Condition: Time 6-10 AM, Days Mon-Fri</li>
      <li>Action: Play specific playlist on bathroom Echo</li>
      <li>Action: Set volume to level 4</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <ol>
      <li>Starter: Shower light turns on</li>
      <li>Condition: Time 6-10 AM, weekdays</li>
      <li>Action: Play music on bathroom speaker</li>
      <li>Action: Adjust volume to 35%</li>
    </ol>
  </div>
</div>

## Advanced features

### Auto-stop music

Turn off music automatically after shower ends:

Create automation with these elements:
- **Trigger:** Shower lights turn off for 2 minutes
- **Action:** Stop music playback on bathroom speaker

**Pause instead (for podcasts):**
Use pause action instead of stop to maintain position for next shower

### Context-aware audio

Play different content based on time or day:

Use conditional logic:
- **Weekday morning (6-8 AM):** Play news podcast
- **Weekend morning:** Play relaxing music playlist
- **Evening (after 6 PM):** Resume previous podcast
- **Default:** Play favorite shower playlist

Automation checks day of week and time, then plays appropriate content.

### Bonus automations

Since your smart home knows when you're showering:

**Flash lights for doorbell:**
When doorbell rings while shower lights are on:
- Flash bathroom main lights
- Send mobile notification: "Someone at the door!"

**Lock front door:**
Automatically lock front door for security

**Adjust temperature:**
Increase thermostat by 2°F for comfort

## Troubleshooting

### Issue: Music doesn't play

**Causes:**
- Speaker not connected to WiFi
- Music service not linked or subscription expired
- Automation not triggering
- Speaker already playing something else
- Volume set to zero

**Solutions:**
✅ Verify speaker shows as online in your app
✅ Test speaker manually - play music directly to verify it works
✅ Check music service login (Spotify, Apple Music, etc.)
✅ Review automation logs to see if trigger fired
✅ Test trigger manually (turn shower light on via app)
✅ Ensure volume preset is audible (30-40% recommended)
✅ Add stop/pause action before playing new content

### Issue: Wrong music plays

**Causes:**
- Playlist URI incorrect
- Music service changed playlist ID
- Speaker grouped with other rooms
- Previous music still queued

**Check:**
- ✅ Verify playlist URI/ID in automation matches desired playlist
- ✅ Test playlist manually in music app
- ✅ Check speaker grouping - ungroup from other rooms
- ✅ Clear speaker queue before playing new content
- ✅ Use specific content type (playlist, album, station)

**Fix:**
Sequence of actions:
1. Clear previous queue on speaker
2. Set volume to 35%
3. Play specific playlist by URI

### Issue: Music too loud or too quiet

**Causes:**
- Volume preset incorrect for room acoustics
- Previous manual adjustment not reset
- Speaker settings changed
- Time of day not considered

**Solutions:**
✅ Adjust volume level in automation (test range 0.20-0.50)
✅ Set volume BEFORE playing content (shown in examples)
✅ Use volume presets automation to reset daily
✅ Add time-based volume:
  - Early morning (6-7 AM): 25%
  - Morning (7-9 AM): 35%
  - Evening (6-10 PM): 30%
✅ Test with actual shower running (sound dampening affects perception)

---

**Related automations:**
- [Turn on bathroom fan when starting shower](/automation/climate/fan-shower/)
- [Morning routine automation](/automation/daily-routines/morning-routine/)
- [Speaker volume presets](/automation/entertainment/speaker-volume-presets/)

<div class="page-navigation">
  <a href="/automation/entertainment/">← Back to Entertainment</a>
  <a href="/automation/">View All Automations →</a>
</div>
