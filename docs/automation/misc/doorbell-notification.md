---
layout: default
title: Traditional Doorbell Notification - Smart Alert for Dumb Doorbells
description: Get phone notifications when your traditional doorbell rings. No smart doorbell needed - just a contact sensor and existing doorbell.
keywords: doorbell notification, traditional doorbell, dumb doorbell alert, doorbell sensor, smart doorbell alternative, contact sensor doorbell
---

# Notify when traditional doorbell rings

If you don't want a smart doorbell, but still want a notification when someone rings the doorbell, then this is for you. It comes in handy when you are outside in the backyard and can't hear the chime. It requires a little bit of extra work to set up but works like a charm.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Awareness</h4>
    <ul>
      <li><strong>Backyard Notification</strong> - Know when someone's at the door even when outside</li>
      <li><strong>Large House</strong> - Don't miss doorbell in distant rooms</li>
      <li><strong>Hearing Impaired</strong> - Visual/vibration notification alternative</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Away Notifications</h4>
    <ul>
      <li><strong>Package Delivery</strong> - Know when delivery person arrives</li>
      <li><strong>Visitor Log</strong> - Track when doorbell is pressed</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Regular "Dumb" Doorbell</strong>
      <div class="product-details">
        Your existing wired doorbell with transformer
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dry Contact Sensor with External Wires</strong>
      <div class="product-details">
        Options:<br>
        • Aqara Door/Window Sensor (has external wire terminals)<br>
        • Ecolink Z-Wave Door/Window Sensor<br>
        • Any contact sensor with external input terminals
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>🔧 How It Works</strong>
  <p>The contact sensor is wired in parallel with your doorbell chime. When someone presses the doorbell button, the sensor detects the circuit change and triggers your automation. The existing doorbell continues to work normally.</p>
  <p><strong>Video Tutorial:</strong> This one is best explained if you watch a video on how to do it. There are several available online. Here is one that I like: <a href="https://www.youtube.com/watch?v=2IsiWG-BOTs" target="_blank">https://www.youtube.com/watch?v=2IsiWG-BOTs</a></p>
</div>

## Basic automation setup

<div class="automation-example">IF contact sensor changes state (open or closed)
THEN send notification to phone
"Someone is at the front door"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Hardware Setup (Summary)</h4>
    <ol>
      <li>Turn off power to doorbell transformer</li>
      <li>Connect sensor wires to doorbell chime terminals</li>
      <li>Restore power</li>
      <li>Test: Press doorbell button, sensor should change state</li>
    </ol>
  </div>
  
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Contact changes to open or closed (depending on how you set it up)</li>
      <li>Some setups trigger on open, some on closed - test yours</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>None - always notify on doorbell press</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Send notification to phone: "Someone is at the front door"</li>
      <li>Optional: Flash lights</li>
      <li>Optional: Play chime on smart speaker</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Add contact sensor to system</li>
      <li>Trigger: binary_sensor.doorbell_sensor changes to "on" (or "off")</li>
      <li>Action: notify.mobile_app with "Doorbell: Someone at the door"</li>
      <li>Optional: Add media_player.play_media for chime sound</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Pair contact sensor with hub</li>
      <li>Create routine: IF Contact opens → Send push notification</li>
      <li>Optional: Add smart speaker chime action</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Add contact sensor to system</li>
      <li>Create Rule Machine or Notification rule</li>
      <li>Trigger: Contact sensor opens/closes</li>
      <li>Action: Send push notification via Hubitat app</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>Add HomeKit-compatible contact sensor</li>
      <li>Create automation: When sensor opens → Send notification</li>
      <li>May need Home app or third-party app for notifications</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>Pair compatible contact sensor</li>
      <li>Create routine: When sensor detects → Send notification</li>
      <li>Can also announce on Echo devices</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Pair sensor through compatible integration</li>
      <li>Create routine with sensor trigger</li>
      <li>Action: Send notification or announce</li>
    </ol>
  </div>
</div>

## Advanced features

### Multi-location notification

Different notifications for different situations:

**At Home:**
- Flash lights in current room
- Play chime on nearby speaker
- Send standard notification

**Away:**
- High-priority push notification
- Start camera recording (if available)
- Activate porch light

### Time-based behavior

Adjust response based on time:

**Daytime:**
- Standard notification
- Normal chime

**Evening (after 8 PM):**
- Quieter chime volume
- Still send notification

**Nighttime (10 PM - 7 AM):**
- Silent chime (or very quiet)
- Notification only
- Perhaps flash bedroom light instead

### Visitor detection pattern

Track and identify visitors:

**Logging:**
- Record timestamp of each ring
- Track frequency
- Identify patterns

**Repeat Detection:**
- If doorbell pressed twice in 2 minutes: "Persistent visitor at door"
- Different notification for repeat presses

### Integration with cameras

If you have a porch camera:

**Trigger on Doorbell:**
- Send snapshot from camera with notification
- Start recording
- Keep recording for 2 minutes after last motion

### Visual alerts for accessibility

For hearing impaired household members:

**Flash Lights:**
- Flash hallway light 3 times
- Pulse smart bulb in living room
- Different flash pattern for doorbell vs. other alerts

**Smart Display:**
- Show "Doorbell" on smart display
- Pop up notification on tablets
- Dashboard tile activation

## Troubleshooting

### Issue: Sensor doesn't trigger when doorbell pressed

**Causes:**
- Wiring not connected properly
- Wrong terminals on chime
- Sensor not detecting voltage change

**Solutions:**
✅ Verify wiring connections at chime
✅ Test with multimeter during button press
✅ Try different terminals on chime
✅ Ensure sensor is designed for this use (has external wire capability)

### Issue: Sensor triggers constantly

**Causes:**
- Wiring picking up interference
- Sensor too sensitive
- Doorbell transformer voltage issues

**Solutions:**
✅ Check for loose connections
✅ Add capacitor if sensor supports it
✅ Verify transformer is correct voltage
✅ Shield wiring from interference

### Issue: False notifications

**Causes:**
- Electrical noise triggering sensor
- Doorbell transformer humming
- Other electrical interference

**Solutions:**
✅ Add debounce delay in automation (ignore triggers within 10 seconds)
✅ Check transformer condition
✅ Add filtering capacitor
✅ Relocate sensor away from interference sources

### Issue: Notifications arrive late

**Causes:**
- Cloud processing delay
- Network latency
- Phone notification settings

**Solutions:**
✅ Use local processing hub if possible
✅ Check network connectivity
✅ Verify app notification permissions
✅ Disable battery optimization for smart home app

## Best practices

### Wiring safety

**Important:**
- Turn off power before any wiring work
- Doorbell transformers are typically 16-24V AC (low voltage, but still be careful)
- If unsure, consult an electrician
- Don't modify the doorbell button or transformer

**Recommended Approach:**
- Work only at the chime unit
- Add sensor in parallel (existing doorbell still works)
- Secure all connections properly
- Test thoroughly before closing up

### Debounce logic

**Why Needed:**
- Doorbell button can bounce (multiple quick signals)
- Prevents multiple notifications for one press
- Cleaner automation behavior

**Implementation:**
- Ignore repeat triggers within 30 seconds
- Only notify on first press
- Reset after delay

### Notification management

**Keep Useful:**
- Include location: "Front doorbell"
- Include time if logged
- Different tone than other notifications

**Avoid Fatigue:**
- Don't over-notify
- Group repeat presses
- Consider quiet hours

---

**Related automations:**
- [Motion detection lights](/automation/motion/lights-on-motion/)
- [Away mode](/automation/presence/away-mode/)
- [Dashboards](/automation/misc/dashboards/)

<div class="page-navigation">
  <a href="/automation/misc/">← Back to Misc Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
