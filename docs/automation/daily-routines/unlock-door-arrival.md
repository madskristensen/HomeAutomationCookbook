---
layout: automation
title: Auto-Unlock Front Door When Arriving Home - Smart Lock Automation
description: Automatically unlock your front door when you arrive home. Complete guide with presence detection, security considerations, and arrival routine integration.
keywords: auto unlock door, smart lock automation, arrival home automation, automatic door unlock, presence detection unlock, smart door lock
---

# Unlock front door when you come home

Arms full of groceries, a bag slipping from your shoulder, keys buried somewhere at the bottom of it all - and then you reach the door, and it is already unlocked. The house recognized your approach and opened for you, as if it had been waiting. Combined with lights and music that stir to life as you enter, the welcome feels complete.

<div class="info-box">
  <strong>Why this automation is valuable</strong>
  <ul>
    <li><strong>Convenience:</strong> No fumbling for keys with groceries. Hands-free entry. Works automatically for everyone with the app.</li>
    <li><strong>Combined experience:</strong> Door unlocks, lights turn on, music starts playing, thermostat adjusts - perfect welcome home</li>
    <li><strong>Universal:</strong> Works for all household members - kids arriving from school, partners coming home from work, anyone with location enabled</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Daily Arrivals</h4>
    <ul>
      <li><strong>Grocery Shopping</strong> - Arms full, can't reach keys</li>
      <li><strong>After Work</strong> - Seamless entry after commute</li>
      <li><strong>Kids from School</strong> - Safe automatic entry</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Special Situations</h4>
    <ul>
      <li><strong>Package Delivery</strong> - Easy re-entry after retrieving packages</li>
      <li><strong>Late Night</strong> - No searching for keys in the dark</li>
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
        On every adult's phone<br>
        Options: Home Assistant Companion, SmartThings, August App, HomeKit (Apple)<br>
        <em>Requires location services enabled on all phones</em>
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Lock or Deadbolt</strong>
      <div class="product-details">
        Brands: August Smart Lock, Yale Assure Lock, Schlage Encode, Kwikset Halo, Zigbee/Z-Wave locks
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Driveway Motion Sensor</strong>
      <div class="product-details">
        Additional verification for security
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Doorbell</strong>
      <div class="product-details">
        Visual confirmation of arrival
      </div>
    </div>
    
    <div class="product-item">
      <strong>Geofence Zones</strong>
      <div class="product-details">
        Approaching/arriving triggers for staged actions
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF person arrives home
AND within 50 feet of front door
THEN unlock front door
AND turn on entry lights</div>

<div class="info-box">
  <strong>🔒 Security: Multiple Verification Points Required</strong>
  <ul>
    <li><strong>Never rely solely on GPS!</strong> Use multiple signals for safety.</li>
    <li><strong>✅ Recommended Verification:</strong> Phone location (primary) + Motion in driveway (physical confirmation) + Time delay (20-30 seconds to confirm) + Away → Home state change (must have left first)</li>
    <li><strong>❌ Don't Do:</strong> Unlock based only on GPS, no delay/verification, no motion confirmation</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Any phone/person arrives home (enters geofence)</li>
      <li>Person state changes to "home"</li>
    </ul>
    <p><em>Verification: Person has been "away" before arriving (prevent unlocking if already home)</em></p>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (Recommended for Security)</h4>
    <ul>
      <li>Motion detected in driveway (optional but recommended)</li>
      <li>Person was away for at least 5 minutes</li>
      <li>Time delay: Present for 20 seconds before unlocking</li>
    </ul>
    <p><em>Optional: Only during typical arrival times, not during sleeping hours</em></p>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <strong>Immediate:</strong> Unlock front door<br>
    <strong>Associated:</strong> Change house mode to "Home" • Turn on entry lights • Start music • Adjust thermostat • Stop robot vacuum • Disarm security
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
        <span class="step-content">Person arrives home (state 'home') for 20 sec</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Was previously 'not_home' + driveway motion (optional)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Unlock door, send notification, set mode "Home"</span>
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
        <span class="step-label">Routine 1</span>
        <span class="step-content">Member arrives + 20 sec → Unlock door</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Routine 2</span>
        <span class="step-content">Door unlocks → Mode "Home", lights, welcome scene</span>
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
        <span class="step-content">Presence sensor arrives for 20 sec</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Previous state was "not present"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Unlock door, Mode "Home", welcome actions</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Combined Presence or Life360 + Rule Machine
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
        <span class="step-content">I arrive home (or anyone arrives)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Unlock door, Turn on lights, Activate home scene</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Requires device to be home hub
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <h4>August/Yale App</h4>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Built-in</span>
        <span class="step-content">Most smart locks have auto-unlock feature</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Setup</span>
        <span class="step-content">Settings → Auto-Unlock → Set distance threshold</span>
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
        <span class="step-content">You arrive home + Wait 20 sec</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Unlock door (requires voice PIN), lights, music</span>
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
        <span class="step-content">When I arrive home + Delay 20 sec</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Unlock door, Turn on lights, Change mode</span>
      </div>
    </div>
  </div>
</div>

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
- [Set away mode when leaving](/automation/daily-routines/away-mode/)
- [Morning routine](/automation/daily-routines/morning-routine/)
- [Home mode activation](/automation/daily-routines/)

<div class="page-navigation">
  <a href="/automation/daily-routines/">← Back to Daily Routines</a>
  <a href="/automation/">View All Automations →</a>
</div>
