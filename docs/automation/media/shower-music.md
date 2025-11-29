---
layout: default
title: Play Music When Shower Starts - Bathroom Automation
description: Automatically play your favorite music or podcasts when you start the shower. Complete guide for bathroom entertainment automation.
keywords: shower music automation, bathroom speaker automation, automatic music, shower entertainment, smart bathroom music, bathroom audio control, morning music
---

# Play music in the bathroom when you start a shower

Having music in the bathroom is one of life's luxuries. However, remembering to turn on your favorite jam isn't always easy, especially early in the morning. Automate your shower soundtrack for the perfect start to your day.

## Use cases

* **Morning Shower Music** - Automatically start your favorite playlist when shower begins
* **Podcast Listening** - Continue your audiobook or podcast during shower time
* **News Briefing** - Catch up on morning news while getting ready
* **Relaxing Bath Sounds** - Calming music for evening bath routine
* **Multi-User Households** - Everyone gets their preferred audio automatically

## Products needed

### Essential

* **Smart Speaker/Music System** - Bathroom audio
  - Waterproof or water-resistant speaker recommended
  - Popular brands: Amazon Echo, Google Home, Sonos, JBL waterproof speakers
  - Key features: WiFi connectivity, voice control optional

**PLUS one of these trigger options:**

* **Option 1: Smart Light Switch** - Trigger when shower lights turn on
  - Easiest method if you have smart shower lights
  - Reliable trigger for shower start
  
* **Option 2: Contact Sensor** - Trigger when shower door opens
  - Best for glass shower enclosures with door
  - Also useful for tracking shower duration

### Optional enhancements

* **Smart Fan Switch** - Also turn on fan automatically
* **Motion Sensor** - Alternative trigger option
* **Voice Control** - Request specific music by voice

## Basic automation setup

### Triggers (choose one method)

**Method 1: Light-based**
* Shower lights turn on

**Method 2: Door sensor**
* Shower door opens (contact sensor)

**Method 3: Combined**
* Shower lights on AND door opens (more reliable)

### Conditions (optional)

* **Home Mode:** Home is NOT in Night mode (don't wake sleeping household members)
* **Time-Based:** Only between 6 AM and 10 AM (morning routine)
* **Day of Week:** Only weekdays (different weekend routine)

### Actions

* Play music/podcast on bathroom speaker
* Set volume to preset level (e.g., 30-40%)
* Optional: Turn on bathroom fan
* Optional: Flash lights if doorbell rings

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Shower lights turn on
- **Conditions:**
  - Home mode is 'Home' (not Night or Away)
  - Time is between 6 AM and 10 AM
  - Weekdays only (Mon-Fri)
- **Actions:**
  - Set bathroom speaker volume to 35%
  - Play Spotify playlist on bathroom speaker

**Using Spotify:**
Use Spotcast service to start specific playlist with shuffle enabled

**Resume podcast/audiobook:**
Simply resume playback on bathroom speaker (continues from last position)

### SmartThings

Create routine:
1. **IF** Shower lights turn on
2. **AND** Home mode is "Home" (not Night or Away)
3. **AND** Time is between 6:00 AM and 10:00 AM
4. **THEN** Play music on bathroom speaker
5. **THEN** Set speaker volume to 35%

### Apple HomeKit

1. Create automation in Home app
2. **When:** Shower light turns on
3. **Conditions:** 
   - Time is between 6:00 AM and 10:00 AM
   - Weekdays only
4. **Do:** 
   - Play music on HomePod/AirPlay speaker
   - Set volume to 35%

### Alexa

Create routine:
1. **When:** Smart Home device (shower light) turns on
2. **Add condition:** Time between 6:00 AM - 10:00 AM
3. **Add condition:** Days of week: Mon-Fri
4. **Action:** Play music from specific playlist on bathroom Echo
5. **Action:** Set volume to level 4 (out of 10)

### Google Home

Create automation:
1. **Starter:** Shower light turns on
2. **Condition:** Time between 6:00 AM - 10:00 AM and weekdays
3. **Action:** Play music on bathroom speaker
4. **Action:** Adjust volume to 35%

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
- [Morning routine automation](/automation/presence/morning-routine/)
- [Speaker volume presets](/automation/media/speaker-volume-presets/)

<div class="page-navigation">
  <a href="/automation/media/">← Back to Media Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
