---
layout: default
title: Auto-Unlock Front Door When Arriving Home - Smart Lock Automation
description: Automatically unlock your front door when you arrive home. Complete guide with presence detection, security considerations, and arrival routine integration.
keywords: auto unlock door, smart lock automation, arrival home automation, automatic door unlock, presence detection unlock, smart door lock
---

# Unlock front door when you come home

Arriving home with arms full of groceries and having the door automatically unlock is a luxury that becomes essential once you experience it. Combined with lights turning on and music starting, it creates a truly welcoming smart home experience.

## Why this automation is valuable

**Convenience:**
- No fumbling for keys with groceries
- Hands-free entry
- Works automatically for everyone with app

**Combined experience:**
- Door unlocks
- Lights turn on
- Music starts playing
- Thermostat adjusts
- Perfect welcome home

**Universal:**
- Works for all household members
- Kids arriving from school
- Partners coming home from work
- Anyone with location enabled

## Use cases

* **Grocery Shopping** - Arms full, can't reach keys
* **After Work** - Seamless entry after commute
* **Kids from School** - Safe automatic entry
* **Package Delivery** - Easy re-entry after retrieving packages
* **Late Night** - No searching for keys in the dark

## Products needed

### Essential

* **Smart home platform app** - On every adult's phone
  - Home Assistant Companion
  - SmartThings
  - August App
  - HomeKit (Apple)
  
* **Smart lock or deadbolt**
  - August Smart Lock
  - Yale Assure Lock
  - Schlage Encode
  - Kwikset Halo
  - Zigbee/Z-Wave locks

* **Location services** - Enabled on all phones

### Optional enhancements

* **Driveway motion sensor** - Additional verification
* **Smart doorbell** - Visual confirmation
* **Geofence zones** - Approaching/arriving triggers

## Basic automation setup

### Triggers

**Primary:**
* Any phone/person arrives home (enters geofence)
* Person state changes to "home"

**Verification:**
* Person has been "away" before arriving
* Prevent unlocking if already home

### Conditions (recommended)

**Security verification:**
* Motion detected in driveway (optional but recommended)
* Person was away for at least 5 minutes
* Time delay: Present for 20 seconds before unlocking

**Time-based (optional):**
* Only during typical arrival times
* Not during sleeping hours

### Actions

**Immediate:**
* Unlock front door

**Associated actions:**
* Change house mode to "Home"
* Turn on entry lights
* Start music
* Adjust thermostat
* Stop robot vacuum
* Disarm security

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Any person arrives home (state changes to 'home') for 20 seconds
- **Condition:** 
  - Person was previously 'not_home'
  - Optional: Driveway motion sensor detected movement
- **Actions:**
  - Unlock front door
  - Send notification: "Welcome home! Door unlocked."

### Advanced: Home mode trigger

Better approach - trigger on door unlock from ANY source:
- **Trigger:** Front door unlocks
- **Condition:** House mode is currently "Away"
- **Actions:**
  - Set house mode to "Home"
  - Turn on entry lights
  - Start music on house speakers
  - Set thermostat to "home" preset
  - Stop robot vacuum (return to dock)

### SmartThings

**Create Routine:**
1. **IF** Member arrives home (location)
2. **AND** After 20 seconds
3. **THEN** Unlock front door

**Create Second Routine:**
1. **IF** Front door unlocks
2. **THEN**
   - Change mode to "Home"
   - Turn on entry lights
   - Run welcome scene

### Apple HomeKit

**Create Automation:**
1. When: I arrive home
2. Time: Anytime
3. People: Anyone arrives
4. Do:
   - Unlock front door
   - Turn on lights
   - Activate home scene

**Note:** HomeKit automation runs on iPhone/iPad, so requires device to be home hub.

### August/Yale App

Most smart locks have built-in auto-unlock:

**Setup:**
1. Open lock app
2. Settings → Auto-Unlock
3. Enable auto-unlock
4. Set distance threshold (usually 200ft)
5. Enable for each person

### Alexa

**Create Routine:**
1. When: You arrive home (location-based)
2. Add: Wait 20 seconds
3. Actions:
   - Unlock front door (requires voice PIN)
   - Turn on lights
   - Start music

**Security Note:** Alexa requires voice PIN confirmation for unlock commands in routines.

### Google Home

**Create Automation:**
1. Starter: When I arrive home
2. Delay: 20 seconds
3. Actions:
   - Unlock front door
   - Turn on lights
   - Change mode

## Home mode actions

When door unlocks OR person arrives, activate Home Mode:

### Lighting
* **Entry lights** - 100% brightness
* **Living room** - 60% brightness
* **Kitchen** - If dark, 80%
* **Hallway** - Path to main areas

### Climate
* **Thermostat** - Resume home temperature
  - Heating: 70°F (21°C)
  - Cooling: 72°F (22°C)
* **Fans** - Resume normal schedule

### Security
* **Disarm system** - Interior motion sensors
* **Pause recording** - Interior cameras
* **Exterior cameras** - Continue recording

### Entertainment
* **Music** - Start favorite station/playlist
* **Volume** - Moderate level (40%)
* **Speakers** - Living room, kitchen

### Appliances
* **Robot vacuum** - Return to dock
* **Coffee maker** - Start brewing (if configured)
* **Fireplace** - Turn on (electric only)

### Notifications
Send useful status updates:
* "Dryer finished while you were out"
* "Package delivered today"
* "Windows left open"
* "Take out trash tonight"

## Security considerations

### Important: Multiple verification points

**Never rely solely on GPS!** Use multiple signals:

✅ **Recommended Verification:**
1. Phone location (primary)
2. Motion in driveway (physical confirmation)
3. Time delay (20-30 seconds to confirm)
4. Away → Home state change (must have left first)

❌ **Don't Do:**
- Unlock based only on GPS
- No delay/verification
- No motion confirmation

### Geo-fence configuration

**Home zone settings:**
- **Radius:** 50-100 meters (150-300 feet)
- **Too small:** Late unlocking, already at door
- **Too large:** Unlocks while approaching

**Test and adjust:**
1. Set initial radius
2. Test arriving from different directions
3. Note when trigger happens
4. Adjust for 20-30 seconds before reaching door

### Security best practices

**Driveway motion sensor:**
Add condition: Motion detected in driveway

**Why:** Confirms physical presence, not just GPS.

**Time-based restrictions:**Add condition: Only between 6 AM and 11 PM

**Why:** Unusual for late-night arrivals, adds security.

**Notification always:**
Always send notification when door auto-unlocks, including person's name

**Why:** Aware of all auto-unlocks, spot any unusual activity.

## Advanced features

### Approaching home detection

Create "Approaching" zone (500m radius):

**Benefits:**
- Pre-heat/cool home
- Turn on exterior lights (if dark)
- Prepare home before arrival
- Smoother experience

**Setup:** Create automation triggered when person enters approaching zone:
- Start climate adjustment (set thermostat to desired temperature)
- Turn on exterior lights if after sunset

### Staggered unlocking

Only unlock when very close:

**Zone Strategy:**
- **Approaching (500m):** Prepare home
- **Nearby (200m):** Turn on lights
- **Arrival (50m):** Unlock door

### Person-specific actions

Different routines per person:
- Check which person triggered the automation
- Play their preferred music playlist
- Example: Parent 1 plays jazz, Parent 2 plays rock

### First person vs. additional

Different behavior for first arrival:

Add condition: Check if only 1 person is home (first arrival)

**First person:**
- Full home activation
- All lights
- Music starts

**Additional arrivals:**
- Just unlock door
- Minimal disruption

## Troubleshooting

### Door unlocks too early

**Causes:**
- Geofence too large
- No arrival delay
- GPS drift

**Solutions:**
- Reduce geofence radius
- Add 20-30 second delay
- Require driveway motion

### Door doesn't unlock

**Check:**
- Location services enabled
- App has background permissions
- Geofence configured
- Lock has power/battery

**Fix:**
- Verify location settings
- Check app permissions
- Test geofence manually
- Replace lock batteries

### Unlocks while approaching

**Causes:**
- Geofence too large
- No delay configured

**Solutions:**
- Reduce radius to 50-100m
- Add 20 second arrival delay
- Require physical trigger (motion)

### False unlocks from GPS drift

**Causes:**
- GPS inaccuracy
- Phone location jumps

**Solutions:**
- Add motion sensor requirement
- Increase arrival confirmation time
- Require Home → Away → Home state change

## Manual override options

**Always Maintain:**
- Physical key still works
- Keypad code entry
- Manual unlock from app
- Voice unlock (with PIN)

**Disable auto-unlock:**
- Vacation mode toggle
- Guest mode
- "Manual only" period
- Temporary disable (24 hours)

## Battery backup

**Smart lock considerations:**
- Most use batteries (4-6 months life)
- Monitor battery level
- Replace proactively
- Some support external power

**Low battery automation:**
Create automation that monitors lock battery level and sends notification when it drops below 20%.

---

**Related automations:**
- [Set away mode when leaving](/automation/presence/away-mode/)
- [Morning routine](/automation/presence/morning-routine/)
- [Home mode activation](/automation/presence/)

[← Back to presence & modes](/automation/presence/) | [View all automations →](/automation/)
