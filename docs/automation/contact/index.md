---
layout: default
title: Contact Sensor Automations - Door & Window Smart Home Guide
description: Master contact sensor automations for doors and windows. Automatic lighting, security alerts, and HVAC control with door/window sensors.
keywords: contact sensor automation, door sensor, window sensor, magnetic sensor, smart door automation, door contact sensor
---

# Contact sensor automations

Contact sensors are among the most versatile and reliable smart home devices. These simple magnetic sensors detect when doors, windows, cabinets, or gates open or close, enabling instant automation triggers.

<div class="category-intro" markdown="1">

## Why contact sensors?

**Instant Response** — Detect open/close immediately with no delay

**Long Battery Life** — 1-2 years on a single battery

**Highly Reliable** — Simple magnetic detection, minimal false positives

**Versatile** — Works on doors, windows, cabinets, garage doors, mailboxes

**Affordable** — Among the most cost-effective smart home sensors

</div>

## 🌟 Essential Automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Toggle lights when door opens

Automatically turn lights on when doors open, off when they close. Perfect for closets, pantries, and storage areas.

<span class="card-meta">**Best for:** Closets, pantries, cabinets, garage</span>

<p><a href="/automation/contact/toggle-lights-door.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Disable motion lights when door closes

Prevent motion sensors from turning lights back on after you've left. Essential bathroom light control.

<span class="card-meta">**Best for:** Bathrooms, offices, bedrooms</span>

<p><a href="/automation/contact/disable-on-door-close.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Quick start guide

### 1. Choose your sensors

**Zigbee/Z-Wave (Recommended):**
- Aqara, SmartThings, Ring, Sonoff
- Local control, no cloud dependency
- Mesh network extends range
- Faster response time

**WiFi Sensors:**
- Wyze, Shelly
- Direct WiFi connection
- No hub required
- Higher battery consumption

### 2. Strategic placement

**High-Value Locations:**
- 🚪 Entry doors (front, back, garage)
- 🪟 Windows (security & climate control)
- 🚽 Bathroom doors
- 🗄️ Closets and pantries
- 📬 Mailboxes and gates

**Installation Tips:**
- Sensor on frame, magnet on moving part
- Within 20mm (3/4 inch) gap when closed
- Clean surfaces before mounting
- Test before permanent installation

### 3. Start with simple automations

**Easy Wins:**
1. **Closet door opens** → Turn on closet light
2. **Front door opens** → Send notification
3. **Window opens** → Pause thermostat

**Then Enhance:**
- Add time-based conditions (only at night)
- Combine with presence detection
- Create multi-step routines
- Integrate with security systems

---

## Common use cases

### 💡 Lighting Automation
- Closet/pantry lights on door open
- Cabinet under-lighting triggers
- Bathroom light overrides
- Entry lights when door opens

### 🔐 Security & Monitoring
- Window open alerts when away
- Door left open reminders
- Entry notifications
- Mailbox delivery alerts

### 🌡️ Climate Control
- Pause HVAC when windows open
- Resume heating/cooling when closed
- Energy-saving notifications
- Temperature alerts

### 🏠 Smart Home Integration
- Trigger arrival routines
- Enable/disable other automations
- Track appliance doors (fridge, washer)
- Garage door status monitoring

---

## Best practices

### ✅ Installation
- Test alignment before permanent mounting
- Keep gap under 20mm when closed
- Use screws for long-term reliability
- Clean mounting surfaces thoroughly

### 🔋 Battery Management
- Monitor levels monthly
- Replace at 20% or annually
- Keep spare CR2032 batteries
- Set up low-battery alerts

### 🎯 Automation Design
- Add 2-5 second delays to avoid false triggers
- Use conditions (time, presence, mode)
- Test different door speeds
- Group related sensors logically

---

## Troubleshooting

**Sensor Not Reporting?**
- Check battery level
- Verify magnet alignment (within 20mm)
- Add mesh repeater if too far from hub
- Re-pair sensor if needed

**False Triggers?**
- Add "for: 2 seconds" delay to automation
- Remount sensor more securely
- Check for vibration sources
- Verify magnet hasn't shifted

**Battery Draining Fast?**
- Use quality batteries (Energizer, Duracell)
- Reduce report frequency in settings
- Check for signal strength issues
- Avoid extreme temperature locations

<div class="page-navigation">
  <a href="/automation/">← Back to All Automations</a>
  <a href="/automation/presence/">Next: Presence & Modes →</a>
</div>
