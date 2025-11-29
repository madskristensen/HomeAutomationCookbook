---
layout: default
title: Play Music When Arriving Home - Welcome Automation
description: Automatically start music when you arrive home. Create a welcoming atmosphere with automatic audio.
keywords: welcome home music, arrival music automation, automatic music greeting, home mode music, presence detection music, greeting automation, arrival routine
---

# Play music when you come home

Coming home to a house with lights on and music playing feels welcoming. It's the little touches that make a house feel like home.

## Use cases

* **After Work Greeting** - Welcome yourself home after long day
* **Morning Wake-Up** - Greet you as morning routine starts
* **Pleasant Atmosphere** - Create welcoming ambiance automatically
* **Energy Boost** - Uplifting music when arriving home
* **Guest Welcome** - Music plays when guests arrive

## Products needed

### Essential

* **Smart Speaker/Music System** - Throughout home or specific rooms
  - Popular brands: Sonos, Amazon Echo, Google Home, Apple HomePod
  - Options: Single room or multi-room audio
  - Key features: WiFi connectivity, streaming service integration
  
* **Presence Detection** - Know when you arrive home
  - Phone app/GPS location services
  - OR smart lock unlock detection
  - OR garage door sensor
  - Popular platforms: Home Assistant, SmartThings, Life360

### Optional enhancements

* **Multiple Speakers** - Music in entry, kitchen, and living room
* **Smart Lights** - Also turn on lights when arriving
* **Voice Announcement** - "Welcome home" greeting

## Basic automation setup

### Triggers
* Home goes into Home mode (when first person arrives)
* OR specific person arrives home
* OR morning routine starts (wake-up music)

### Conditions (optional)
* **NOT between 7 AM and 10 AM** - If you don't want morning music
* **Time is after 4 PM** - Only afternoon/evening arrivals
* **Music not already playing** - Don't interrupt existing playback

### Actions
* Play music on selected speakers
* Set volume to appropriate level
* Optionally announce "Welcome home"
* Optional: Turn on lights, unlock door

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Home mode changes from 'Away' to 'Home'
- **Condition:** Time is after 4 PM
- **Actions:**
  - Activate welcome home scene (lights)
  - Set speaker volume to 35% on entry, kitchen, and living room speakers
  - Play welcome home playlist from Spotify

**With person-specific music:**

Create automation that plays different music based on who arrives:
- **Trigger:** Person arrives home
- **Condition:** Music not currently playing
- **Actions (conditional logic):**
  - If John home alone: Play John's favorites playlist
  - If Jane home alone: Play Jane's favorites playlist
  - If both home: Play shared favorites playlist

### SmartThings

Create routine:
1. **IF** Home mode changes to "Home"
2. **AND** Time is after 4:00 PM
3. **THEN** Turn on welcome scene (lights)
4. **THEN** Play music on speakers
5. **THEN** Set volume to 35%

### Apple HomeKit

1. Create automation in Home app
2. **When:** First person arrives home
3. **Conditions:** Time is after 4:00 PM
4. **Do:** 
   - Turn on welcome scene
   - Play music on HomePod
   - Set volume to 35%

### Alexa

Create routine:
1. **When:** You arrive home (location-based)
2. **Add condition:** Time after 4:00 PM
3. **Action:** Turn on lights (welcome scene)
4. **Action:** Play music from Spotify on Echo devices
5. **Action:** Alexa says "Welcome home"

### Google Home

Create automation:
1. **Starter:** When you get home (location)
2. **Condition:** Time is after 4:00 PM
3. **Action:** Activate welcome scene
4. **Action:** Play music on Google speakers
5. **Action:** Adjust volume to 35%

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
