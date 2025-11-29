---
layout: default
title: Dim Lights When TV Turns On - Theater Mode Automation
description: Automatically dim lights when TV turns on for better viewing experience. Complete guide with power monitoring and smart TV integration.
keywords: TV lighting automation, dim lights TV, theater mode automation, movie lighting, automatic TV lights, smart TV automation, cinema mode
---

# Dim lights when TV turns on

Enhance movie watching by automatically dimming lights when the TV turns on. Create the perfect viewing atmosphere without fumbling for light switches.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Entertainment</h4>
    <ul>
      <li><strong>Movie Watching</strong> - Optimize lighting for better screen visibility</li>
      <li><strong>TV Show Viewing</strong> - Reduce glare and eye strain</li>
      <li><strong>Gaming</strong> - Create immersive gaming environment</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Comfort & Ambiance</h4>
    <ul>
      <li><strong>Afternoon Viewing</strong> - Close blinds when sun hits screen</li>
      <li><strong>Theater Experience</strong> - Automatic cinema mode in your living room</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment - Option 1: Power Monitoring (Most Universal)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Plug with Power Monitoring</strong>
      <div class="product-details">
        Popular brands: TP-Link Kasa, Shelly, Zigbee power monitoring plugs<br>
        Real-time power measurement • Relay control
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Essential Equipment - Option 2: Smart TV Integration (More Reliable)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart TV with Platform Integration</strong>
      <div class="product-details">
        Compatible: Chromecast, Fire TV, Roku, Apple TV, Samsung, LG<br>
        Works with: Home Assistant, SmartThings
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Lights or Light Switches</strong>
      <div class="product-details">
        Popular brands: Philips Hue, LIFX, Lutron, Inovelli<br>
        Dimmable capability required
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>RGB Bias Lighting</strong>
      <div class="product-details">
        Colored LED strip behind TV for enhanced viewing
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Blinds</strong>
      <div class="product-details">
        For daytime glare control
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF TV power > 50W
AND time after sunset
THEN dim living room lights to 10%
AND close blinds</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Using Power Monitor</h4>
    <strong>Trigger:</strong> Smart plug power consumption rises above 50 watts (TV turns on)<br>
    <strong>Conditions:</strong> Time between sunset and sunrise (optional)<br>
    <strong>Actions:</strong> Dim lights to 10% OR turn off completely • Optional: Close blinds/curtains
  </div>
  
  <div class="setup-step">
    <h4>Using Smart TV</h4>
    <strong>Trigger:</strong> TV turns on OR specific app opens (Netflix, Disney+, etc.)<br>
    <strong>Conditions:</strong> Time between 6 PM - midnight (movie hours) • Only for video apps<br>
    <strong>Actions:</strong> Dim lights to 10-20% • Close blinds if daytime
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: TV plug power > 50W for 5 sec</li>
      <li>Condition: Time after sunset, before sunrise</li>
      <li>Action: Dim living room lights to 10%</li>
      <li>Alternative: Use media player 'playing' state</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF TV plug power > 50W for 5 seconds</li>
      <li>AND Time is after sunset</li>
      <li>THEN Set lights to 10%</li>
      <li>THEN Close blinds</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Rule Machine with power monitoring plug</li>
      <li>Trigger: TV plug power > 50W for 5 sec</li>
      <li>Condition: Time after sunset</li>
      <li>Action: Set living room lights to 10%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: TV power monitor > 50W</li>
      <li>Conditions: Time after sunset</li>
      <li>Do: Dim lights to 10%, Close blinds</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: TV plug power above 50W</li>
      <li>Condition: Time after 6:00 PM</li>
      <li>Action: Set lights to 10%</li>
      <li>Action: Close smart blinds</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: TV plug power above 50 watts</li>
      <li>Condition: Time after 6:00 PM</li>
      <li>Action: Dim living room lights to 10%</li>
    </ol>
  </div>
</div>

## Advanced features

### Content-aware lighting

Different content types get different lighting:

Create automation triggered by TV app changes with conditional logic:
- **Movie mode (Netflix, Disney+, Plex):** 5% brightness, warm white, close blinds
- **TV show mode (Hulu, YouTube TV):** 15% brightness
- **Gaming mode (HDMI inputs):** 25% brightness, activate RGB bias lighting with dynamic effect
- **Sports mode (ESPN):** 30% brightness

Use app name or input source to determine content type and adjust accordingly.

### Daytime glare control

Different behavior for daytime vs nighttime:

Create two automations:

**Daytime (sunrise to sunset):**
- Close blinds to reduce glare
- Keep lights at 40% (more light needed during day)

**Nighttime (after sunset):**
- Dim lights significantly to 10%
- Blinds already closed or less critical

### Bias lighting synchronization

Sync LED strip behind TV:
- Dim main room lights to 5%
- Activate TV backlight LED strip at 50% brightness
- Set warm white/orange color (RGB: 255, 140, 60)

### Pause dimming for movement

Don't dim if people are moving around:

Add condition: No motion detected in last 5 minutes before dimming lights

## Troubleshooting

### Issue: Lights dim when TV menu on

**Causes:**
- Power monitoring can't differentiate between menu and playback
- Trigger threshold too low
- No delay to ensure actually watching content

**Solutions:**
✅ Increase power threshold (try 80W instead of 50W)
✅ Add longer delay (30 seconds) before dimming
✅ Use smart TV integration instead - detect 'playing' state
✅ Add condition: Only between certain hours (6 PM - midnight)
✅ Use app-specific triggers (Netflix/Disney+ only)

### Issue: Lights don't restore when TV off

**Causes:**
- Power drops gradually, not instantly
- No reverse automation created
- Previous brightness not saved
- TV on standby still drawing power

**Check:**
- ✅ Create separate "restore lights" automation (shown in examples)
- ✅ Use lower power threshold for "off" detection (below 10W)
- ✅ Add 2-minute delay to ensure TV actually off (not just paused)
- ✅ Save previous light state before dimming
- ✅ Test actual TV power consumption when off (may be 5-15W)

**Fix with state saving:**
- When dimming: Create scene snapshot of current light state, then dim
- When restoring: Activate saved scene to restore exact previous brightness

### Issue: Smart TV state inaccurate

**Causes:**
- TV integration losing connection
- TV firmware outdated
- Network issues
- Platform doesn't support TV model well

**Solutions:**
✅ Update TV firmware to latest version
✅ Check TV integration in platform (reconnect if needed)
✅ Use power monitoring as backup method
✅ Restart hub/integration
✅ Check TV is on same network as hub
✅ Use Cast device (Chromecast) instead of TV direct integration

---

**Related automations:**
- [Away mode automation](/automation/presence/away-mode/)
- [Bedtime routine automation](/automation/presence/bedtime-routine/)
- [Speaker volume presets](/automation/media/speaker-volume-presets/)

<div class="page-navigation">
  <a href="/automation/media/">← Back to Media Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
