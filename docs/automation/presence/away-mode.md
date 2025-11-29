---
layout: default
title: Set Away Mode When Everyone Leaves - Presence Automation
description: Automatically activate Away Mode when everyone leaves home. Complete guide with presence detection, motion verification, and security integration.
keywords: away mode automation, presence detection, leave home automation, GPS automation, location based automation, smart home away mode
---

# Set away mode when everyone leaves

Automatically transition your home to Away Mode when the last person leaves. This foundational automation enables energy savings, security activation, and peace of mind that your home is properly secured.

## Why this matters

**Energy savings:**
- Turn off unnecessary lights
- Adjust thermostat to eco mode
- Stop running appliances

**Security:**
- Lock all doors automatically
- Arm security system
- Activate surveillance cameras

**Convenience:**
- No manual mode switching needed
- Works automatically for everyone
- Consistent behavior

## Use cases

* **Daily Work Commute** - Everyone leaves for work/school
* **Weekend Trips** - Family leaves for activities
* **Vacations** - Extended absence from home
* **Evening Outings** - Dinner, movies, events
* **Running Errands** - Quick trips away from home

## Products needed

### Essential

* **Smart home platform app** - Installed on every adult's phone
  - Home Assistant Companion
  - SmartThings app
  - Life360 (works with multiple platforms)
  - Apple Home (for HomeKit)
  
* **Location services enabled** - On each phone
  - GPS/location always on
  - Background app refresh enabled
  - Battery optimization exceptions

### Optional enhancements

* **Motion sensors** - Verify no one home
* **Smart locks** - Auto-lock doors
* **Smart thermostat** - Energy savings
* **Security cameras** - Visual verification

## Basic automation setup

### Triggers

**Primary:**
* Last phone leaves home geofence

**Alternative triggers:**
* Person 1 leaves AND Person 2 leaves
* All tracked devices leave home zone

### Conditions (important!)

**Verify truly empty:**
* Both phones not present for 10 minutes
* No motion detected in any room for 9 minutes
* No TV is currently on
* No music playing
* Optional: No computers active

**Why multiple conditions?**
- Phone GPS can drift
- Someone without phone may be home (kids, guests, nanny)
- Prevents false away activation

### Actions

**Immediate:**
* Set house mode to "Away"
* Send confirmation notification

**Triggered by Away Mode:**
* Turn off all lights
* Lock all doors
* Adjust thermostat
* Arm security system
* Start robot vacuum (optional)

## Platform-specific examples

### Home Assistant

Create automation with these elements:
- **Trigger:** All persons leave home for 10 minutes
- **Conditions:** 
  - No motion detected for 9 minutes
  - TV is off
- **Actions:**
  - Set house mode to "Away"
  - Send notification: "Home is now in Away mode"

### Away mode actions automation

Create separate automation that responds to Away mode:
- **Trigger:** House mode changes to "Away"
- **Actions:**
  - Turn off all lights
  - Lock all doors
  - Set thermostat to away/eco preset
  - Arm security system
  - Optional: Start robot vacuum

### SmartThings

**Create Routine:**
1. **IF** All members away for 10 minutes
2. **AND** No motion detected for 9 minutes
3. **AND** TVs are off
4. **THEN** Change mode to "Away"

**Create Second Routine for Actions:**
1. **IF** Mode changes to "Away"
2. **THEN** 
   - Turn off all lights
   - Lock doors
   - Set thermostat to Away
   - Arm security

### Apple HomeKit

**Automation:**
1. When: Last person leaves
2. Conditions: 
   - After 10 minutes
   - No motion detected
3. Do: 
   - Turn off lights
   - Lock doors
   - Set thermostat
   - Activate security scene

### Alexa

**Create Routine:**
1. When: Last person leaves (via Alexa app location)
2. Wait: 10 minutes
3. Actions:
   - Change mode to "Away"
   - Turn off lights
   - Lock doors
   - Adjust thermostat

### Google Home

**Create Automation:**
1. Starter: Last person leaves home
2. Delay: 10 minutes
3. Actions:
   - Set home to Away
   - Turn off lights
   - Lock doors

## Away mode actions checklist

### Lighting

**Turn Off:**
- All interior lights
- Decorative lighting
- Night lights
- Under-cabinet lighting

**Turn On (if dark):**
- Away lighting pattern (see security section)
- Exterior lights on timer

### Climate control

**Thermostat settings:**
- **Heating season:** 60°F (15°C)
- **Cooling season:** 78°F (26°C)
- Switch to "Away" or "Eco" mode

**Other climate:**
- Turn off bathroom fans
- Stop humidifiers/dehumidifiers
- Close smart vents in unused rooms

### Security

**Lock everything:**
- Front door
- Back door
- Side doors
- Garage door (close if open)
- Deadbolts

**Arm security:**
- Interior motion sensors
- Door/window sensors
- Cameras start recording
- Enable push notifications

### Appliances & devices

**Turn off:**
- Coffee maker
- Space heaters
- Fans
- Entertainment systems
- Smart plugs (non-essential)

**Automation pause:**
- Robot vacuum (or start if scheduled)
- Watering systems (unless scheduled)
- Turn off screens on dashboards

### Notifications

**Alert options:**
- "Home is now in Away mode"
- "All doors locked ✓"
- "Thermostat set to eco mode"
- "Security system armed"

## Advanced features

### Graduated timeouts

Different delay times for different situations:
- **Short trip (daytime, no calendar event):** 10 minute delay before activating away mode
- **Likely longer trip (calendar shows event):** 3 minute delay

Use conditional logic to check time of day and calendar status to determine appropriate timeout.

### Approaching home detection

Create "Approaching" zone 500m from home:

**Benefits:**
- Pre-heat/cool home
- Turn on entry lights
- Unlock door as you arrive
- Disarm security

**Setup:** Create zone trigger when person enters approaching zone (500m radius).

### False positive prevention

**Scenario:** Phone GPS drifts, triggers away mode while you're home

**Solution 1: Motion verification**
Add condition: Must have no motion for extended time (15 minutes)

**Solution 2: Door activity check**
Add condition: No door opened in last 15 minutes

**Solution 3: Manual override**
- Physical button: "Staying Home"
- Voice command: "Cancel away mode"
- App toggle: Disable auto-away for X hours

### Phased away activation

Gradually transition to full away mode:

**Phase 1: Pre-Away (5 minutes after leaving)**
- Turn off non-essential lights
- Reduce thermostat by 2°

**Phase 2: Away (10 minutes after leaving)**
- Turn off all lights
- Set thermostat to eco
- Lock doors

**Phase 3: Secure Away (20 minutes after leaving)**
- Arm security system
- Enable enhanced monitoring
- Activate away lighting patterns

## Handling edge cases

### Kids without phones

**Solution 1: Time-based override**
Add condition: Don't activate during after-school hours (3-6 PM on weekdays)

**Solution 2: Door lock check**
- Kids can't lock deadbolt from inside
- Check deadbolt status before activating away

**Solution 3: Motion sensor required**
- Must have no motion for longer period
- 20+ minutes instead of 10

### Guests visiting

**Solution 1: Guest mode toggle**
- Manual switch: "Guests over"
- Disables auto-away
- Re-enables automatically after 24 hours

**Solution 2: Extended delays**
- Increase motion-free time to 30 minutes
- Require explicit departure signal

### Dead phone battery

**Solution 1: Fallback verification**
- Must have multiple verification methods pass
- Motion + door activity + time of day

**Solution 2: Manual check-in**
- Send notification: "Haven't heard from you, are you home?"
- Await response before activating

**Solution 3: Conservative approach**
- Only activate if ALL signs point to empty
- When in doubt, don't activate

### Left phone at home

**Automatic recovery:**
Create automation that detects quick return (door opens within 1 hour of away mode activation) and switches back to Home mode.

## Troubleshooting

### Away mode activates while home

**Check:**
- GPS accuracy on phones
- Motion sensor placement and function
- Motion-free timeout setting
- Other verification conditions

**Fix:**
- Increase geofence size
- Add more verification conditions
- Extend motion-free timeout
- Add manual override button

### Away mode doesn't activate

**Check:**
- Location services enabled on all phones
- App has background permissions
- Geofence configured correctly
- Conditions are being met

**Fix:**
- Review location settings
- Test geofence manually
- Check automation logs
- Verify all triggers/conditions

### Delayed activation

**Causes:**
- Conservative timeout settings
- Many verification conditions
- Cloud processing delays

**Solutions:**
- Reduce timeout if safe
- Remove unnecessary conditions
- Use local processing

## Security considerations

**Don't rely solely on GPS:**
- Add motion verification
- Check door activity
- Verify TV/music status

**Fail-safe approach:**
- When uncertain, don't activate
- Better to not activate than false activate
- Manual override always available

**Notification strategy:**
- Always notify when activating
- Include what actions were taken
- Allow quick undo via notification

---

**Related automations:**
- [Unlock door when arriving home](/automation/presence/unlock-door-arrival/)
- [Morning routine](/automation/presence/morning-routine/)
- [Bedtime routine](/automation/presence/bedtime-routine/)

<div class="page-navigation">
  <a href="/automation/presence/">← Back to Presence Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
