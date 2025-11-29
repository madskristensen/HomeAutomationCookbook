---
layout: default
title: Smart Home Dashboards - Status Tiles, Controls, and Reminders
description: Create effective smart home dashboards for status, reminders, and controls. Garbage day reminders, music controls, and status tiles.
keywords: smart home dashboard, status tiles, dashboard controls, SharpTools, garbage reminder, music controls, home dashboard, tablet dashboard
---

# Dashboard automations

We have four dashboards in our home - each customized to their location and purpose. Three of them are wall-mounted tablets, and one is built for our phones. What they all have in common is that they allow us to see the status of the home and provide controls for what's important.

For information on how to wall mount tablets and create dashboards, there are many options. I'll defer to the many tutorials online, so you can find the one that works best for your home. I'll be using SharpTools in this book because it's the product I use, but also because it works with the most smart home systems including SmartThings, Hubitat and Home Assistant.

<div class="category-intro" markdown="1">

## Why dashboards?

**Persistent Visibility** — Status tiles remind you until tasks are done

**Whole Household** — Everyone sees the same information

**Quick Controls** — One tap to play music or run scenes

**No Voice Needed** — Guests can control without learning commands

**Customizable** — Different dashboards for different locations

**Glanceable** — See home status at a glance

</div>

<div class="info-box">
  <strong>🖥️ Our Kitchen Dashboard</strong>
  <p>This is the dashboard located in the kitchen which is also the main area of the house with the most traffic. It serves several purposes:</p>
  <ul>
    <li>Allows us to control the music</li>
    <li>Gives us glanceable status of appliances and doors/windows</li>
    <li>Shows the family calendar</li>
    <li>Shows weather and temperature so we can plan accordingly</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Status & Visibility</h4>
    <ul>
      <li><strong>Appliance Status</strong> - Washer done, dishwasher clean, etc.</li>
      <li><strong>Door/Window Status</strong> - Know what's open before leaving</li>
      <li><strong>Delivery Alerts</strong> - Package waiting to be brought in</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Controls & Reminders</h4>
    <ul>
      <li><strong>Music Controls</strong> - Easy access to favorite stations</li>
      <li><strong>Garbage Day Reminder</strong> - Weekly task reminder</li>
      <li><strong>Quick Actions</strong> - Common scenes and controls</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Tablet</strong>
      <div class="product-details">
        Amazon Fire tablets (affordable option)<br>
        iPad (premium option)<br>
        Android tablets (flexible option)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dashboard Software</strong>
      <div class="product-details">
        SharpTools (works with SmartThings, Hubitat, Home Assistant)<br>
        Home Assistant native dashboards<br>
        ActionTiles (SmartThings)<br>
        Hubitat Dashboard
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Wall Mount</strong>
      <div class="product-details">
        Magnetic mounts, flush mounts, or stands for tablets
      </div>
    </div>
    
    <div class="product-item">
      <strong>Always-On Power</strong>
      <div class="product-details">
        Power cable routing for permanent installation
      </div>
    </div>
    
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        Wake screen when someone approaches (optional)
      </div>
    </div>
  </div>
</div>

## 🌟 Essential Automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

#### [Garbage day reminder](/automation/dashboards/garbage-day-reminder.html)

A weekly reminder tile that lights up red when it's time to take out the trash. Tap to mark complete.

**Best for:** Weekly tasks, recycling day, scheduled reminders

<p><a href="/automation/dashboards/garbage-day-reminder.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

#### [Status tiles instead of notifications](/automation/dashboards/status-tiles.html)

Persistent status tiles that stay visible until tasks are addressed. Better than phone notifications.

**Best for:** Appliance status, door/window alerts, delivery notifications

<p><a href="/automation/dashboards/status-tiles.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

#### [Music controls](/automation/dashboards/music-controls.html)

Control music from your dashboard with favorite stations, volume presets, and now playing display.

**Best for:** Easy music access, party control, eliminating voice command frustration

<p><a href="/automation/dashboards/music-controls.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Quick start guide

### 1. Choose your tablet

**Budget Options:**
- Amazon Fire tablets (most affordable)
- Older Android tablets
- Refurbished iPads

**Premium Options:**
- iPad (best display)
- Samsung Galaxy Tab
- Google Pixel Tablet

### 2. Select dashboard software

**SharpTools:**
- Works with SmartThings, Hubitat, Home Assistant
- Web-based builder
- Cross-platform access

**Home Assistant Lovelace:**
- Native dashboards
- Highly customizable
- Local control

**Hubitat Dashboard:**
- Built-in option
- Local network access
- Simple setup

**ActionTiles:**
- Works with SmartThings
- Panel-based layout
- Easy tile configuration

### 3. Plan your layout

**High-Traffic Location:**
- Kitchen (most common)
- Entry/mudroom
- Living room

**Content Priority:**
1. Most-used controls largest
2. Status information visible
3. Less-used items secondary

### 4. Create your first tiles

Start simple:
1. Add a few virtual switches
2. Create automations to toggle them
3. Add to dashboard with colors
4. Test and refine

---

## Common use cases

### 💡 Status & Visibility
- Appliance done alerts (washer, dryer, dishwasher)
- Door/window open indicators
- Package delivery waiting
- Temperature and weather

### 🎵 Controls
- Music playback and favorites
- Volume presets
- Scene activation
- Room lighting controls

### ⏰ Reminders
- Garbage/recycling day
- Pet feeding schedule
- Medication reminders
- Filter change notifications

### 📍 Information
- Family calendar
- Weather forecast
- Traffic conditions
- Security status

---

## Best practices

### Dashboard design

**Keep It Simple:**
- Don't overcrowd
- Most important items largest
- Group related items
- Consistent layout

**Use Color Meaningfully:**
- Green: Good/off/complete
- Red: Attention needed/on/warning
- Yellow: Caution/transitional
- Blue: Informational

### Tablet considerations

**Placement:**
- High traffic areas
- Eye-level mounting
- Avoid direct sunlight
- Near power outlet

**Settings:**
- Disable auto-updates
- Kiosk mode for dedicated use
- Brightness appropriate for location
- Screen timeout balanced with usability

### Family acceptance

**Make It Useful:**
- Solve real problems
- Easy for everyone to use
- No training needed
- Works reliably

---

**Get Started:**
- [Garbage Day Reminder →](/automation/dashboards/garbage-day-reminder.html)
- [Status Tiles Instead of Notifications →](/automation/dashboards/status-tiles.html)
- [Music Controls →](/automation/dashboards/music-controls.html)

<div class="page-navigation">
  <a href="/automation/">← Back to All Automations</a>
  <a href="/automation/misc/">Next: Misc Automations →</a>
</div>
