---
layout: automation
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
    <div class="platform-card-header">
      <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
      <h4>Home Assistant</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Closet door opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Light level below 50 lux</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on light at 100%</span>
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
        <span class="step-content">"Closet Door Sensor" opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn on "Closet Light" to 100%</span>
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
        <span class="step-content">Contact sensor opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on closet light to 100%</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Simple Automation Rules or Rule Machine
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
        <span class="step-content">Door sensor detects open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Time</span>
        <span class="step-content">Anytime (or add condition)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn on Closet Light</span>
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
        <span class="step-content">"Door Sensor" opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between sunrise/sunset</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on light to 100%</span>
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
        <span class="step-label">When</span>
        <span class="step-content">"Door Sensor" opens</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time of day (optional)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn on "Closet Light"</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Day vs. night brightness</h3>
    <p>Adjust brightness based on time of day:</p>
    <ul>
      <li><strong>Nighttime (10 PM - 6 AM):</strong> 30% brightness, warm white (2200K)</li>
      <li><strong>Daytime:</strong> 100% brightness</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Auto turn-off when door closes</h3>
    <p>Turn off light 2 minutes after door closes:</p>
    <ul>
      <li>Prevents lights turning off while door swings closed</li>
      <li>Avoids rapid on/off cycles during multiple trips</li>
      <li>Still energy efficient</li>
    </ul>
  </div>
</div>

---

**Related automations:**
- [Disable automations when door closed](/automation/lighting/disable-on-door-close/)

<div class="page-navigation">
  <a href="/automation/lighting/">← Back to Lighting Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
