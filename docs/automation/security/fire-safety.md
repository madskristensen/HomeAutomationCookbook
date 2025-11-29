---
layout: default
title: Fire Safety Emergency Response - Smart Home Automation
description: Automated fire emergency response when smoke detector sounds. Lights on, doors unlocked, irrigation started, notifications sent.
keywords: fire safety automation, smoke detector, emergency response, smart home safety, fire evacuation, home emergency, smoke alarm automation
---

# Get safely out of the house in case of fire

If a fire breaks out in the middle of the night, your smoke detector will sound the alarm. However, getting everybody out of the house might be problematic - especially if you have little kids. There are some things we can do to make the situation a little smarter.

We want to make sure all lights come on so we can easily find our way out of the otherwise dark house at night. Also, make sure to unlock all doors. And if you have an irrigation or sprinkler system in the yard or garden, turn it on to prevent any fire from spreading outside.

A variation of this is to listen for the sound of a window breaking at night or when you're not home.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Fire Emergency</h4>
    <ul>
      <li><strong>Smoke Detector Goes Off</strong> - Immediate emergency response</li>
      <li><strong>Nighttime Evacuation</strong> - All lights turn on for safe exit</li>
      <li><strong>Door Unlock</strong> - Quick escape without fumbling for locks</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Break-in Detection</h4>
    <ul>
      <li><strong>Window Breaks</strong> - Alert and response to glass break sound</li>
      <li><strong>Nighttime Intrusion</strong> - Lights and notifications activate</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Smoke Detector or Detection Method</strong>
      <div class="product-details">
        Options:<br>
        • Native smart detector: Nest Protect, First Alert Onelink<br>
        • Sound listener: Amazon Echo Guard feature, dedicated listeners<br>
        • Wired relay: Attached to existing smoke detector wiring
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Lights</strong>
      <div class="product-details">
        Whole-house smart lights for full illumination during emergency
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Door Lock</strong>
      <div class="product-details">
        Auto-unlock for quick escape
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Irrigation System</strong>
      <div class="product-details">
        Wet exterior to prevent fire spread (Rachio, RainMachine, etc.)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Glass Break Sensor</strong>
      <div class="product-details">
        Ring Glass Break, Aqara, SmartThings sensors
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>🔊 Smoke Detection Without Smart Detectors</strong>
  <p>If you don't have a smart smoke detector, there are alternatives you can use to make your existing detector smart:</p>
  <ul>
    <li><strong>Wired relays:</strong> Attach to existing smoke detector wiring, acts like an open/closed sensor when alarm sounds</li>
    <li><strong>Sound listeners:</strong> Devices that pick up the specific sound pattern of smoke detectors and send signals to your smart home</li>
    <li><strong>Amazon Echo Guard:</strong> Built into Echo devices, can detect smoke alarm sounds through its Guard feature</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF smoke detector goes off
THEN turn on all lights
AND unlock all doors
AND start outdoor irrigation
AND send notifications</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Smoke detector goes off (state changes to "smoke detected")</li>
      <li>OR Sound listener detects smoke alarm pattern</li>
      <li>OR Wired relay sensor changes state</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>None - this should always run when triggered</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on lights in the whole house (100% brightness)</li>
      <li>Unlock all doors</li>
      <li>Start the outdoor irrigation (if available)</li>
      <li>Send critical notifications to all family members</li>
      <li>Optional: Announce evacuation message on smart speakers</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Smoke detector state changes to "on" or "smoke"</li>
      <li>No conditions (always run)</li>
      <li>Actions: Turn on all lights group to 100% + Unlock all door locks + Start irrigation zone + Send critical notifications (notify with critical: true)</li>
      <li>Optional: TTS announcement "Fire alarm activated, evacuate immediately"</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF: Smoke detector detects smoke</li>
      <li>THEN: Turn on all lights + Unlock all doors + Start irrigation</li>
      <li>THEN: Send push notification to all members</li>
      <li>Use SHM (SmartThings Home Monitor) for enhanced integration</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Rule Machine or HSM (Hubitat Safety Monitor)</li>
      <li>Trigger: Smoke sensor active</li>
      <li>Actions: All lights on + Doors unlocked + Irrigation on + Push notifications</li>
      <li>HSM can handle comprehensive emergency response</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Smoke detected by HomeKit smoke sensor</li>
      <li>Do: Turn on all lights + Unlock doors (if supported)</li>
      <li>Note: Limited irrigation control in HomeKit</li>
      <li>Notifications sent automatically by Home app</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>Enable Guard feature in Alexa app</li>
      <li>Guard detects smoke alarm sounds</li>
      <li>Create routine: When Guard detects emergency → Turn on all lights</li>
      <li>Smart Alerts sends notifications automatically</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>If using Nest Protect: Native integration with Google Home</li>
      <li>Trigger: Smoke alarm activates</li>
      <li>Actions: Turn on lights, send notifications</li>
      <li>Nest integrates with Works with Google devices</li>
    </ol>
  </div>
</div>

## Glass break detection setup

A variation of fire safety is detecting window break sounds:

<div class="automation-example">IF glass break detected
AND time is nighttime OR home is in Away mode
THEN turn on all lights
AND send critical alert
AND start recording cameras</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Glass break sensor detects breaking glass</li>
      <li>OR Sound listener detects glass break pattern</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>Time is between 10 PM and 6 AM</li>
      <li>OR Home is in Away mode</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on all interior and exterior lights</li>
      <li>Send high-priority notification with location</li>
      <li>Start camera recording</li>
      <li>Optional: Sound audible alarm</li>
      <li>Optional: Announce warning message</li>
    </ul>
  </div>
</div>

## Advanced features

### Zone-based evacuation lighting

Create lit paths to exits:

**Implementation:**
- Identify primary and secondary exit paths
- Light those paths at maximum brightness
- Include stairway and hallway lights
- Exterior lights illuminate exit points

**Automation Logic:**
1. Fire detected → All path lights to 100%
2. Exterior lights on to illuminate exits
3. Smart bulbs flash in exit direction (if supported)

### Smoke detector by room

Different response based on fire location:

**Kitchen Fire:**
- May be cooking related
- Add 30-second delay
- Send alert to check kitchen
- Activate if alarm continues

**Bedroom Fire:**
- Immediate full response
- All lights on
- Doors unlocked
- No delay

**Garage Fire:**
- Specific response
- Close door to house (if safe)
- Alert sent with garage location

### Irrigation zones for fire containment

Strategic irrigation activation:

**Near-House Zones:**
- Activate zones closest to house
- Wet perimeter to slow fire spread
- Focus on roof-adjacent areas

**Timing:**
- Run for 10-15 minutes
- Or until manually stopped
- Automatic shutoff after 30 minutes

### Multi-alarm verification

Reduce false positives:

**Logic:**
- Single detector: Send alert, wait 30 seconds
- Two or more detectors: Full emergency response
- Continued alarm after delay: Full response

### Post-event automation

After emergency is handled:

**Reset Automation:**
- When smoke clears (detector returns to normal)
- Wait 15 minutes
- Send "All clear" notification
- Return lights to previous state
- Relock doors (after verification)

## Troubleshooting

### Issue: False alarms from cooking

**Causes:**
- Kitchen smoke detector too sensitive
- Steam or cooking smoke triggers

**Solutions:**
✅ Add delay for kitchen detector only
✅ Send verification alert before full response
✅ Use "photoelectric" type detector (less sensitive to cooking smoke)
✅ Relocate kitchen detector away from stove

### Issue: Doors don't unlock

**Causes:**
- Lock battery low
- Z-Wave/Zigbee connectivity issue
- Lock not in automation

**Solutions:**
✅ Check lock battery regularly
✅ Verify lock responds to commands
✅ Test automation monthly
✅ Add lock to automation actions

### Issue: Notifications don't arrive

**Causes:**
- Phone in Do Not Disturb mode
- App notification permissions
- Critical alerts not enabled

**Solutions:**
✅ Use "critical" or "priority" notification flags
✅ Enable emergency bypass in notification settings
✅ Test notifications during setup
✅ Use multiple notification methods (push, SMS, call)

### Issue: Automation doesn't trigger

**Causes:**
- Smoke detector not integrated
- Wrong trigger configured
- Detector offline

**Solutions:**
✅ Verify smoke detector appears in smart home
✅ Check detector status and connectivity
✅ Test with manual trigger (test button)
✅ Review automation logs for errors

## Safety considerations

### Test regularly

**Monthly:**
- Test smoke detectors
- Verify automation triggers
- Check all lights respond
- Test door unlocks
- Verify notifications arrive

**Annually:**
- Replace batteries
- Review evacuation plan
- Update family on procedures
- Test irrigation response

### Manual overrides

**Always Ensure:**
- Physical escape routes available
- Manual door locks work
- Physical light switches function
- Don't rely solely on automation

### Fire safety basics

**Remember:**
- Automation assists, doesn't replace safety planning
- Have multiple escape routes
- Practice fire drills with family
- Know when to evacuate vs. fight fire
- Call 911 first

---

**Related automations:**
- [Away lights](/automation/security/away-lights/)
- [Fake dog deterrent](/automation/security/fake-dog-deterrent/)
- [Away mode](/automation/presence/away-mode/)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
