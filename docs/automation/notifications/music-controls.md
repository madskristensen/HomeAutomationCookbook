---
layout: automation
title: Music Controls on Dashboard - Smart Home Automation
description: Control music from your dashboard with favorite stations, volume presets, and now playing display. No more yelling at voice assistants.
keywords: music dashboard, smart home music, dashboard controls, volume presets, music tiles, SharpTools music
---

# Music controls

Controlling the music from a dashboard solves several problems. One is to see the album art, artist, and song name to know more information about the current song playing. This is a topic that comes up all the time, and being able to glance at the dashboard to see the information is super convenient.

If you're like me, you have a few favorite stations or playlists that you play most of the time. Giving each of them a tile on the dashboard makes it easy to play any of them. The same goes with presets for volume like low, normal, and loud.

All these controls eliminate the need to yell at Alexa/Google/Siri repeatedly, which is often a cause of frustration.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>For the Household</h4>
    <ul>
      <li><strong>One-Tap Music</strong> - Start favorite playlists instantly</li>
      <li><strong>Volume Control</strong> - Preset levels for different activities</li>
      <li><strong>Now Playing</strong> - See what song is playing at a glance</li>
      <li><strong>No Voice Needed</strong> - Control without speaking</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>For Parties</h4>
    <ul>
      <li><strong>Guest Friendly</strong> - Anyone can control music</li>
      <li><strong>Party Playlists</strong> - Pre-configured party music</li>
      <li><strong>Volume Presets</strong> - Easy adjustment for different phases</li>
      <li><strong>Room Control</strong> - Group or ungroup speakers</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Speakers</strong>
      <div class="product-details">
        Sonos, Amazon Echo, Google Home, HomePod, or any smart speaker system
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dashboard</strong>
      <div class="product-details">
        Wall-mounted tablet with SharpTools, Home Assistant, or native dashboard
      </div>
    </div>
    
    <div class="product-item">
      <strong>Music Service</strong>
      <div class="product-details">
        Spotify, Apple Music, Amazon Music, or other streaming service
      </div>
    </div>
  </div>
</div>

## Dashboard elements for music

### Now playing tile

- Album art display
- Artist and song name
- Play/pause button
- Skip forward/back

### Favorite stations/playlists

- One tile per favorite
- Tap to instantly play
- Examples:
  - "Dinner Music" playlist
  - "Morning Energy" station
  - "Kids Favorites"
  - "Party Mix"

### Volume presets

- "Low" (30%) - background music
- "Normal" (50%) - everyday listening
- "Loud" (70%) - party mode
- Eliminates "Alexa, set volume to..." commands

### Room/Zone selection

- Quick switch between rooms
- Group rooms together
- Ungroup for individual control

## Basic automation setup

<div class="automation-example">IF "Dinner Music" tile tapped
THEN play "Dinner Jazz" playlist on Kitchen speaker
AND set volume to 40%</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Dashboard tile tapped (virtual switch turned on)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Play specific playlist or station</li>
      <li>Set volume to preferred level</li>
      <li>Target specific speaker or group</li>
    </ul>
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
        <span class="step-label">Now Playing</span>
        <span class="step-content">Use media_player cards</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Presets</span>
        <span class="step-content">Create scripts for favorite playlists</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Controls</span>
        <span class="step-content">Button cards + slider for volume</span>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <h4>SharpTools</h4>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Display</span>
        <span class="step-content">Media tile for now playing</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Presets</span>
        <span class="step-content">Virtual switches + automation for each</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Tiles</span>
        <span class="step-content">Hero tiles for playlist buttons</span>
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
        <span class="step-label">Limitation</span>
        <span class="step-content">Limited native music control</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Integration</span>
        <span class="step-content">SmartThings-Sonos integration</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Display</span>
        <span class="step-content">SharpTools dashboard</span>
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
        <span class="step-label">Integration</span>
        <span class="step-content">Sonos or Chromecast integration</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Presets</span>
        <span class="step-content">Virtual switches + Rule Machine</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Dashboard</span>
        <span class="step-content">Hubitat Dashboard</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

### Party dashboard

Create a special dashboard for parties and gatherings:

**Include:**
- Large now playing display
- Prominent volume controls
- Favorite party playlists
- Group speaker controls

**Exclude:**
- Home automation controls
- Security features
- Sensitive settings
- Anything confusing for guests

### Volume automation

Automatically adjust volume based on context:

- **Time-based:** Lower volume after 10 PM
- **Activity-based:** Reduce during phone calls
- **Mode-based:** Louder during party mode
- **Noise-based:** Adjust based on ambient noise sensor

### Multi-room audio

Control speaker groups from dashboard:

- **All Speakers:** Whole house audio
- **Main Floor:** Kitchen, living room, dining
- **Upstairs:** Bedrooms, office
- **Outside:** Patio, garage

Add tiles to quickly switch between groups or individual rooms.

### DJ mode

Let guests participate:

1. Create a shared playlist everyone can add to
2. Display playlist queue on dashboard
3. Allow skip voting (multiple taps to skip)
4. Maintain backup playlist for when queue is empty

## Troubleshooting

### Issue: Now playing not updating

**Solutions:**
✅ Check speaker integration is properly configured
✅ Verify media_player entity is available
✅ Refresh dashboard connection
✅ Check speaker is on same network as hub

### Issue: Playlist won't start

**Solutions:**
✅ Verify music service is linked to speaker
✅ Check playlist still exists in music service
✅ Test playing from music app directly
✅ Re-link music service account

### Issue: Volume too loud/quiet

**Solutions:**
✅ Calibrate volume presets to your preference
✅ Consider room acoustics
✅ Test at different times of day
✅ Add volume normalization if supported

### Issue: Wrong speaker plays

**Solutions:**
✅ Verify correct speaker entity in automation
✅ Check speaker groups are configured correctly
✅ Ensure default speaker is set properly
✅ Specify speaker explicitly in each automation

## Best practices

### Dashboard layout

- Place music controls prominently
- Large tap targets for volume
- Now playing visible at a glance
- Favorite presets easily accessible

### Family-friendly setup

- Include kid-friendly playlists
- Parental controls on explicit content
- Simple interface for all ages
- Guest-accessible controls

### Performance tips

- Use local integrations when possible
- Minimize cloud dependencies
- Cache album art locally
- Test response time of controls

---

**Related automations:**
- [Garbage day reminder](/automation/notifications/garbage-day-reminder.html)
- [Status tiles instead of notifications](/automation/notifications/status-tiles.html)
- [Music switch control](/automation/entertainment/music-switch-control.html)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
