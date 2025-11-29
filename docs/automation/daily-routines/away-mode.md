---
layout: default
title: Set Away Mode When Everyone Leaves - Presence Automation
description: Automatically activate Away Mode when everyone leaves home. Complete guide with presence detection, motion verification, and security integration.
keywords: away mode automation, presence detection, leave home automation, GPS automation, location based automation, smart home away mode
---

# Set away mode when everyone leaves

Automatically transition your home to Away Mode when the last person leaves. This foundational automation enables energy savings, security activation, and peace of mind that your home is properly secured.

<div class="info-box">
  <strong>⭐ Why This Matters</strong>
  <ul>
    <li><strong>Energy Savings:</strong> Turn off unnecessary lights, adjust thermostat to eco mode, stop running appliances</li>
    <li><strong>Security:</strong> Lock all doors automatically, arm security system, activate surveillance cameras</li>
    <li><strong>Convenience:</strong> No manual mode switching needed. Works automatically for everyone with consistent behavior.</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Daily & Short Trips</h4>
    <ul>
      <li><strong>Daily Work Commute</strong> - Everyone leaves for work/school</li>
      <li><strong>Running Errands</strong> - Quick trips away from home</li>
      <li><strong>Evening Outings</strong> - Dinner, movies, events</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Extended Absences</h4>
    <ul>
      <li><strong>Weekend Trips</strong> - Family leaves for activities</li>
      <li><strong>Vacations</strong> - Extended absence from home</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Home Platform App</strong>
      <div class="product-details">
        Installed on every adult's phone<br>
        Options: Home Assistant Companion, SmartThings app, Life360, Apple Home (for HomeKit)<br>
        <em>Requirements: GPS/location always on, background app refresh enabled, battery optimization exceptions</em>
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Motion Sensors</strong>
      <div class="product-details">
        Verify no one home
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Locks</strong>
      <div class="product-details">
        Auto-lock doors
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Thermostat</strong>
      <div class="product-details">
        Energy savings
      </div>
    </div>
    
    <div class="product-item">
      <strong>Security Cameras</strong>
      <div class="product-details">
        Visual verification
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF everyone leaves home
THEN set house to Away mode
AND turn off all lights
AND adjust thermostat to eco</div>

<div class="info-box">
  <strong>⚠️ Important: Verify Truly Empty (Multiple Conditions Recommended)</strong>
  <ul>
    <li>Both phones not present for 10 minutes</li>
    <li>No motion detected in any room for 9 minutes</li>
    <li>No TV is currently on</li>
    <li>No music playing</li>
    <li>Optional: No computers active</li>
    <li><strong>Why?</strong> Phone GPS can drift. Someone without phone may be home (kids, guests, nanny). Prevents false away activation.</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Last phone leaves home geofence</li>
      <li>OR Person 1 leaves AND Person 2 leaves</li>
      <li>OR All tracked devices leave home zone</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (Important!)</h4>
    <ul>
      <li>Both phones not present for 10 minutes</li>
      <li>No motion detected in any room for 9 minutes</li>
      <li>No TV is currently on</li>
      <li>No music playing</li>
      <li>Optional: No computers active</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <strong>Immediate:</strong> Set house mode to "Away" • Send confirmation notification<br>
    <strong>Triggered by Away Mode:</strong> Turn off all lights • Lock all doors • Adjust thermostat • Arm security system • Start robot vacuum (optional)
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
        <span class="step-content">All persons leave home for 10 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">No motion for 9 minutes + TV is off</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Set mode "Away", Turn off lights, Lock doors, Set thermostat</span>
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
        <span class="step-content">All members away 10 min AND No motion 9 min</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Change mode to "Away"</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Routine 2:</strong> Mode "Away" → Lights off, Lock doors, Set thermostat
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
        <span class="step-content">All presence sensors "not present" 10 min</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">No motion for 9 min + Media off</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Change mode to "Away"</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Mode Manager + Rule Machine for Away actions
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
        <span class="step-content">Last person leaves</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">After 10 minutes + No motion detected</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Lights off, Lock doors, Set thermostat, Arm security</span>
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
        <span class="step-content">Last person leaves (via Alexa app location)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Wait</span>
        <span class="step-content">10 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Mode "Away", Lights off, Lock doors, Adjust thermostat</span>
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
        <span class="step-content">Last person leaves home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Delay</span>
        <span class="step-content">10 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Set home to Away, Turn off lights, Lock doors</span>
      </div>
    </div>
  </div>
</div>

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
- [Unlock door when arriving home](/automation/daily-routines/unlock-door-arrival/)
- [Morning routine](/automation/daily-routines/morning-routine/)
- [Bedtime routine](/automation/daily-routines/bedtime-routine/)

<div class="page-navigation">
  <a href="/automation/daily-routines/">← Back to Daily Routines</a>
  <a href="/automation/">View All Automations →</a>
</div>
