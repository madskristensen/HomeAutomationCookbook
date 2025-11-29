---
layout: default
title: Auto-Unlock Front Door When Arriving Home - Smart Lock Automation
description: Automatically unlock your front door when you arrive home. Complete guide with presence detection, security considerations, and arrival routine integration.
keywords: auto unlock door, smart lock automation, arrival home automation, automatic door unlock, presence detection unlock, smart door lock
---

# Unlock front door when you come home

Arriving home with arms full of groceries and having the door automatically unlock is a luxury that becomes essential once you experience it. Combined with lights turning on and music starting, it creates a truly welcoming smart home experience.

<div class="info-box">
  <strong>🏡 Why This Automation Is Valuable</strong>
  <ul>
    <li><strong>Convenience:</strong> No fumbling for keys with groceries. Hands-free entry. Works automatically for everyone with app.</li>
    <li><strong>Combined Experience:</strong> Door unlocks, lights turn on, music starts playing, thermostat adjusts - perfect welcome home</li>
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
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Any person arrives home (state changes to 'home') for 20 seconds</li>
      <li>Condition: Person was previously 'not_home' + Optional: Driveway motion sensor detected movement</li>
      <li>Actions: Unlock front door + Send notification: "Welcome home! Door unlocked."</li>
      <li>Advanced: Trigger on door unlock (any source) → If mode is "Away" → Set to "Home" + Turn on entry lights + Start music + Set thermostat + Stop robot vacuum</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Routine 1: IF Member arrives home (location) AND After 20 seconds → THEN Unlock front door</li>
      <li>Routine 2: IF Front door unlocks → THEN Change mode to "Home" + Turn on entry lights + Run welcome scene</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Combined Presence or Life360 integration</li>
      <li>Trigger: Presence sensor arrives for 20 seconds</li>
      <li>Condition: Previous state was "not present"</li>
      <li>Action: Unlock front door + Change mode to "Home"</li>
      <li>Use Rule Machine for welcome actions: lights, music, thermostat</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: I arrive home</li>
      <li>Time: Anytime • People: Anyone arrives</li>
      <li>Do: Unlock front door + Turn on lights + Activate home scene</li>
      <li>Note: HomeKit automation runs on iPhone/iPad, requires device to be home hub</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>August/Yale App</h4>
    <ol>
      <li>Most smart locks have built-in auto-unlock</li>
      <li>Open lock app → Settings → Auto-Unlock</li>
      <li>Enable auto-unlock + Set distance threshold (usually 200ft)</li>
      <li>Enable for each person</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: You arrive home (location-based) + Wait 20 seconds</li>
      <li>Actions: Unlock front door (requires voice PIN) + Turn on lights + Start music</li>
      <li>Security Note: Alexa requires voice PIN confirmation for unlock commands in routines</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: When I arrive home + Delay: 20 seconds</li>
      <li>Actions: Unlock front door + Turn on lights + Change mode</li>
    </ol>
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
