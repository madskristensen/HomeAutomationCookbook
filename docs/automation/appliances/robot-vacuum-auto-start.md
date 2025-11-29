---
layout: default
title: Start Robot Vacuum When Everyone Leaves
description: Automatically start your robot vacuum when the house is empty. Clean while away without lifting a finger.
keywords: robot vacuum automation, auto start vacuum, vacuum when away, automatic vacuum cleaning, smart vacuum, presence detection vacuum, away mode cleaning
---

# Start the robot vacuum when everybody leaves

Robot vacuums are great, but even better when they clean while you're away. Automate daily cleaning to happen when no one is home to disturb or be disturbed.

## Use cases

* **Clean During Work Hours** - House cleaned while away at work
* **No Disturbance** - No one home to be bothered by vacuum noise
* **Daily Cleaning** - Automatic consistent cleaning schedule
* **Pet Hair Management** - Keep up with pet shedding automatically
* **Guest Ready** - House always clean when you return

## Products needed

### Essential

* **WiFi-Enabled Robot Vacuum** - Any smart vacuum
  - Popular brands: Roomba, Roborock, Eufy, Shark, Neato
  - Key features: WiFi connectivity, app control, scheduling override
  
* **Presence Detection** - Know when everyone leaves
  - Phone app location services
  - GPS-based (Home Assistant, SmartThings, Life360)
  - OR door lock status + motion sensors

### Optional Enhancements

* **Contact Sensors** on doors - Ensure all doors closed
* **Smart Notifications** - Alert if vacuum gets stuck
* **Dashboard Widget** - Vacuum status and manual control

## Basic automation setup

### Triggers
* Home goes into Away Mode
* (Last person leaves house based on presence detection)

### Conditions
* **Time is between 9 AM and 6 PM** - Vacuum during daytime only
* **House has been in Away Mode for 15 minutes** - Ensure everyone actually left
* **Optional:** Day of week (e.g., only weekdays)

### Actions
* Start robot vacuum cleaning cycle
* OR trigger vacuum's existing schedule

## Platform-Specific Examples

### Home Assistant

Create automation with these elements:
- **Trigger:** Home mode changes to 'Away' for 15 minutes (ensures everyone actually left)
- **Conditions:** Time between 9am-6pm AND weekdays AND vacuum is docked
- **Action:** Start robot vacuum cleaning cycle

**Using person entity:**

Create automation with these elements:
- **Trigger:** All persons group changes to 'not_home' for 15 minutes
- **Condition:** Time between 9am-6pm
- **Action:** Start robot vacuum

**Stop vacuum when someone returns:**

Create automation with these elements:
- **Trigger:** Home mode changes to 'Home' from 'Away'
- **Condition:** Vacuum is currently cleaning
- **Action:** Send vacuum to dock (return to base)

### SmartThings

Create routine:
1. **IF** Home mode changes to "Away"
2. **AND** Mode stays "Away" for 15 minutes
3. **AND** Time between 9:00 AM - 6:00 PM
4. **AND** Day is Monday through Friday
5. **THEN** Start robot vacuum

### Apple HomeKit

1. Create automation in Home app
2. **When:** Last person leaves home
3. **Conditions:**
   - Time between 9:00 AM - 6:00 PM
   - Weekdays only
4. **Do:** Start vacuum (if vacuum supports HomeKit)

### Alexa

Create routine:
1. **When:** Location-based (last person leaves home)
2. **Add condition:** Time between 9:00 AM - 6:00 PM
3. **Add condition:** Weekdays
4. **Action:** Smart Home control → Start vacuum

### Google Home

Create automation:
1. **Starter:** When last person leaves home
2. **Condition:** Time between 9 AM - 6 PM and weekdays
3. **Action:** Start robot vacuum

## Advanced features

### Room-by-room daily schedule

Different rooms on different days:

Create automation that triggers when away for 15 minutes during daytime (9am-6pm), then uses day-based logic:
- **Monday:** Clean kitchen & dining room (segment IDs 1, 2)
- **Tuesday:** Clean living room (segment 3)
- **Wednesday:** Clean bedrooms (segments 4, 5)
- **Thursday:** Clean hallways (segment 6)
- **Friday:** Full house cleaning (all rooms)

*Note: Requires vacuum model supporting room-specific cleaning commands*

### Pre-cleaning notification

Remind to tidy up before vacuum starts:

Create automation with these elements:
- **Trigger:** Home mode changes to 'Away' for 5 minutes
- **Condition:** Time between 9am-6pm
- **Action:** Send notification "Vacuum will start in 10 minutes. Tidy floors if needed!"

### Stuck vacuum alert

Get notified if vacuum has problems:

Create automation with these elements:
- **Trigger:** Vacuum state changes to 'error'
- **Action:** Send high-priority notification "Robot vacuum is stuck or has an error!"

### Battery-based smart start

Only start if battery sufficient:

Add condition to automation: Vacuum battery level must be above 50% before starting cleaning cycle.

## Safety considerations

### Pre-checks before starting

Ensure conditions are safe:

Add conditions to automation:
- All doors closed (prevent vacuum getting stuck in closets - check bedroom closet door, utility room door)
- No maintenance needed (vacuum is docked AND bin is not full)

### Stop conditions

Automatically stop vacuum if:

Create automation with these elements:
- **Trigger:** Any person arrives home (group.all_persons changes to 'home')
- **Condition:** Vacuum is currently cleaning
- **Action:** Send vacuum to dock (return to base)

## Troubleshooting

### Issue: Vacuum starts when someone is still home

**Causes:**
- Presence detection too fast/inaccurate
- Phone GPS delay
- One person left but others home
- Away mode triggered prematurely

**Solutions:**
✅ Increase away delay to 20-30 minutes
✅ Use "all persons away" not "any person away"
✅ Combine presence with door lock status
✅ Add motion sensor check - no motion for 15+ minutes
✅ Use more reliable presence detection (Life360, multiple methods)

Add multiple detection methods to conditions:
- All persons away for 15+ minutes
- AND no motion detected for 15+ minutes
- AND front door locked

### Issue: Vacuum gets stuck

**Causes:**
- Doors left open (closets, bathrooms)
- Obstacles not cleared (shoes, toys, cables)
- Low battery starting cycle
- Virtual barriers not set

**Solutions:**
✅ Add notification before start: "Tidy floors in 10 minutes"
✅ Check battery level before starting (>50%)
✅ Set virtual barriers in vacuum app
✅ Add door sensors - only start if problem doors closed
✅ Implement stuck detection and notification (shown above)

### Issue: Vacuum doesn't start

**Causes:**
- Vacuum already running or has error
- Battery too low
- Maintenance needed (bin full, filter)
- Integration not working

**Check:**
- ✅ Verify vacuum shows as "docked" before automation triggers
- ✅ Check vacuum battery level
- ✅ Empty bin and clean filter
- ✅ Test manual start via app
- ✅ Review automation logs
- ✅ Check vacuum WiFi connection

Add diagnostics to automation:
- If vacuum is docked, start cleaning
- Otherwise, send notification with current vacuum state and battery level

---

**Related automations:**
- [Away mode automation](/automation/presence/away-mode/)
- [Morning routine automation](/automation/presence/morning-routine/)
- [Washer done notification](/automation/appliances/washer-done-notification/)

[← Back to appliance automations](/automation/appliances/) | [View all automations →](/automation/)
