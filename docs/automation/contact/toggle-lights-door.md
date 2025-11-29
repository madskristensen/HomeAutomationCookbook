---
layout: default
title: Toggle Lights When Door Opens - Contact Sensor Automation
description: Automatically turn on lights when doors open. Complete guide for door sensor lighting automation with examples for closets, rooms, and outdoor areas.
keywords: door sensor automation, contact sensor lights, automatic closet lights, door activated lighting, smart door sensor
---

# Toggle lights on/off when door opens

Automatically turning on lights when doors open is a versatile automation that solves lighting problems in many areas of your home. From closets that never have enough light to garage entries that leave you fumbling in the dark, this automation makes life easier.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Indoor Applications</h4>
    <ul>
      <li>Closets - Illuminate contents automatically</li>
      <li>Pantry - See all shelves clearly</li>
      <li>Linen closet - Find items easily</li>
      <li>Room entry - Automatic lighting</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Outdoor Applications</h4>
    <ul>
      <li>Garage entry - Light up when arriving</li>
      <li>Exterior doors - Porch/patio lights</li>
      <li>Shed/storage - Building illumination</li>
      <li>Gate entry - Pathway lighting</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Contact Sensor</strong>
      <div class="product-details">
        Popular brands: Aqara, SmartThings, Ring, Wyze<br>
        Battery-powered for easy installation • Zigbee/Z-Wave for reliability
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Light Switch or Bulb</strong>
      <div class="product-details">
        In-wall switch for permanent fixtures • Smart bulbs for flexibility • Dimming capability recommended
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Outdoor Installation Tips</strong>
  <ul>
    <li>Use weather-rated sensors (IP65+)</li>
    <li>Protect with weatherproof enclosures</li>
    <li>Consider temperature range (-20°F to 120°F)</li>
    <li>Use UV-resistant materials</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF closet door opens
THEN turn on closet light to 100%</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Contact sensor changes to "open"</li>
      <li>Door opens (specific door)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <strong>Time-based:</strong> Only during certain hours<br>
    <strong>Lux sensor:</strong> Only if room is dark<br>
    <strong>Day vs. Night:</strong> Different brightness levels
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on light switch/bulb</li>
      <li>Set to preferred brightness level</li>
      <li>Optional: Set color temperature</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Closet door opens</li>
      <li>Condition: Light level below 50 lux</li>
      <li>Action: Turn on light at 100%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF "Closet Door Sensor" opens</li>
      <li>THEN Turn on "Closet Light" to 100%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Door sensor detects open</li>
      <li>Time: Anytime (or add condition)</li>
      <li>Do: Turn on Closet Light</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: "Door Sensor" opens</li>
      <li>Add condition: Time between sunrise/sunset</li>
      <li>Action: Turn on light to 100%</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: "Door Sensor" opens</li>
      <li>Condition: Time of day (optional)</li>
      <li>Action: Turn on "Closet Light"</li>
    </ol>
  </div>
</div>

## Advanced features

### Day vs. night brightness

Adjust brightness based on time of day:
- **Nighttime (10 PM - 6 AM):** 30% brightness with warm white (2200K)
- **Daytime:** 100% brightness

### Auto turn-off when door closes

**Simple auto-off:** Turn off light 2 minutes after door closes

**Why the 2-minute delay?**
- Prevents lights turning off while door swings closed
- Avoids rapid on/off cycles during multiple trips
- Still energy efficient

---

**Related automations:**
- [Disable automations when door closed](/automation/contact/disable-on-door-close/)

<div class="page-navigation">
  <a href="/automation/contact/">← Back to Contact Sensor Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
