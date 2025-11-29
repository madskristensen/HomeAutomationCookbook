---
layout: default
title: Speaker Volume Presets - Smart Audio Management
description: Set and recall speaker volume presets for different occasions. Low, medium, and loud settings for every room.
keywords: speaker volume automation, audio presets, volume control scenes, smart speaker volume, volume management, consistent volume, audio scenes
---

# Speaker volume presets

Volume presets for all speakers save time and create consistency. Define levels for low, medium, and loud to easily adjust for any occasion with one command.

## Use cases

* **Normal Day** - Always play music at pleasant levels when home
* **Party Mode** - Quick adjustment for gatherings and celebrations
* **One-Button Control** - Single action adjusts all rooms
* **Consistent Experience** - Voice assistant and music always at predictable volume
* **Time-Based** - Automatically adjust volume throughout the day

## Products needed

### Essential

* **Smart Speakers/Music System** - Throughout home
  - Brands: Sonos, Amazon Echo, Google Home, Apple HomePod
  - Options: Individual or grouped speakers
  - Key features: Remote volume control via automation

### Optional Enhancements

* **Buttons or Switches** - Physical controls for volume presets
* **Voice Commands** - "Set volume to party mode"
* **Dashboard** - Visual volume preset selector

## Basic automation setup

### Volume Level Examples

**Low (Quiet/Background):**
- Voice assistants: 30%
- Music speakers: 20-25%
- Use for: Normal day, working, early morning

**Medium (Comfortable):**
- Voice assistants: 50%
- Music speakers: 40-50%
- Use for: Entertaining, cooking, cleaning

**Loud (Party):**
- Voice assistants: 60%
- Music speakers: 70-80%
- Use for: Parties, dancing, exercising

### Triggers
* Home goes into Home mode (set to Low)
* Button/switch pressed
* Voice command: "Set volume to [low/medium/loud]"
* Time-based (e.g., 10 PM → Low)

### Conditions
* None (immediate response typically desired)

### Actions
* Set volume of all speakers to preset levels
* Can be per-room or whole-house

## Platform-Specific Examples

### Home Assistant

**Create Input Select for Volume Presets:**

Create a dropdown helper in Home Assistant with three options: Low, Medium, Loud. Set initial value to Low. This will allow you to select and track the current volume preset.

**Automation to Apply Preset:**

Create automation with these elements:
- **Trigger:** Input select (volume_preset) state changes
- **Actions based on selected preset:**
  - **Low:** Set voice assistants (Echos) to 30%, music speakers to 20%
  - **Medium:** Set voice assistants to 50%, music speakers to 45%
  - **Loud/Party:** Set voice assistants to 60%, music speakers to 80%, keep bedroom at 40%

**Auto-Reset Volume at 4 AM:**

Create automation with these elements:
- **Trigger:** Time is 4:00 AM daily
- **Action:** Set volume preset input select to "Low"

**Button to Cycle Volume Presets:**

Create automation with these elements:
- **Trigger:** Volume button pressed
- **Action:** Cycle to next option in volume preset dropdown (Low → Medium → Loud → Low)

### SmartThings

Create scenes for each volume preset:

**Scene: Low Volume**
- Living room Echo: 30%
- Kitchen Echo: 30%
- Living room speaker: 20%
- Kitchen speaker: 20%

**Scene: Medium Volume**
- All Echos: 50%
- All speakers: 45%

**Scene: Party Volume**
- Main area Echos: 60%
- All speakers: 80%

Create routine to activate scenes with button or voice.

### Apple HomeKit

Create scenes in Home app:

**Low Volume Scene:**
1. Set all HomePods to 30%
2. Set AirPlay speakers to 20%

**Medium Volume Scene:**
1. Set all HomePods to 50%
2. Set AirPlay speakers to 45%

Activate via Siri: "Hey Siri, set low volume"

### Alexa

Create routines for each preset:

**Routine: Low Volume**
1. Set Living Room Echo volume to 3 (out of 10)
2. Set Kitchen Echo volume to 3
3. Set Bedroom Echo volume to 3

Activate with: "Alexa, low volume"

### Google Home

Create routines:

**Routine: Party Volume**
1. Set Living Room speaker to 80%
2. Set Kitchen speaker to 80%
3. Set volume on all Home devices to 60%

Activate with: "Hey Google, party volume"

## Room-specific presets

Different rooms may need different levels:

### Kitchen
- Low: 30% (morning coffee)
- Medium: 50% (cooking)
- Loud: 70% (party prep)

### Bedroom
- Low: 15% (sleep sounds)
- Medium: 30% (getting ready)
- Loud: 50% (never too loud)

### Living Room
- Low: 25% (background)
- Medium: 45% (normal use)
- Loud: 80% (party time)

**Implementation:**

Create automation with room-specific volume levels:
- **Trigger:** Volume preset changes
- **Low preset:** Kitchen 30%, Bedroom 15%, Living room 25%
- **Medium preset:** Kitchen 50%, Bedroom 30%, Living room 45%
- **Loud preset:** Kitchen 70%, Bedroom 50%, Living room 80%

## Advanced features

### Time-based auto-adjustment

Automatically adjust volume throughout the day:

Create automation with these elements:
- **Triggers:** Multiple times - 6am, 10am, 6pm, 10pm
- **Actions based on time:**
  - **6am-10am:** Set to Low (morning quiet)
  - **10am-6pm:** Set to Medium (daytime)
  - **6pm-10pm:** Set to Medium (evening)
  - **10pm+:** Set to Low (night quiet hours)

### Ungroup speakers during reset

Dissolve temporary speaker groups:

Create automation with these elements:
- **Trigger:** Time is 4:00 AM daily
- **Action 1:** Ungroup all Sonos speakers (unjoin command)
- **Action 2:** Reset volume preset to Low

### Activity-based presets

Different presets for different activities:

**Options:**
- Podcast (voice-optimized, low volume)
- Music (balanced, medium volume)
- Party (loud, all rooms)
- Movie (low volume, living room only)
- Sleep (minimal, bedroom only)

## Troubleshooting

### Issue: Volumes change unexpectedly

**Causes:**
- Family members manually adjusting
- Multiple automations conflicting
- Daily reset not accounting for special events
- Time-based adjustments too aggressive

**Solutions:**
✅ Communicate volume preset system with household
✅ Add manual override flag to skip auto-adjustments
✅ Review all volume automations for conflicts
✅ Add "party mode" that disables auto-adjustments
✅ Use longer reset interval (weekly instead of daily)

### Issue: Some speakers not adjusting

**Causes:**
- Speaker offline or unreachable
- Entity ID incorrect in automation
- Speaker doesn't support volume control
- Network connectivity issues

**Check:**
- ✅ Verify all speakers show as online in app
- ✅ Test manual volume adjustment for each speaker
- ✅ Check entity IDs match current speaker names
- ✅ Review automation logs for errors
- ✅ Check network connectivity and WiFi signal strength

### Issue: Volume too loud/quiet for specific rooms

**Causes:**
- Room acoustics differ significantly
- Speaker types vary (Echo vs Sonos)
- Room size not accounted for
- Personal preference varies

**Solutions:**
✅ Use room-specific presets (shown above)
✅ Adjust percentages per room acoustics
✅ Test in actual use conditions
✅ Create custom presets for problematic rooms
✅ Consider different speaker types need different levels

---

**Related automations:**
- [Play music when shower starts](/automation/media/shower-music/)
- [Welcome home music automation](/automation/media/welcome-home-music/)
- [Control music with physical switch](/automation/media/music-switch-control/)

<div class="page-navigation">
  <a href="/automation/media/">← Back to Media Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
