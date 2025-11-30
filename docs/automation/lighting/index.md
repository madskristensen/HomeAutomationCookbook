---
layout: default
title: Lighting Automations - Smart Home Lighting Guide
description: Master automatic lighting for your smart home. Motion-triggered lights, door-activated lighting, night lights, and outdoor illumination.
keywords: smart lighting automation, motion sensor lights, automatic lighting, door sensor lights, outdoor lights, night light automation
---

# Lighting automations

Lighting is often the first area people automate in their smart home - and for good reason. Automatic lighting creates a magical experience where lights respond to your presence and needs without you ever touching a switch.

<div class="category-intro" markdown="1">

## Why automate lighting?

**Hands-Free Convenience** - Lights turn on automatically as you enter any room

**Energy Savings** - Lights turn off when rooms are unoccupied

**Safety at Night** - Never stumble in the dark with gentle nighttime lighting

**True Automation** - Works without any input from you

**Versatile Triggers** - Motion sensors, door sensors, time of day, and more

**Instant Response** - Modern sensors detect presence in milliseconds

</div>

## Essential automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Turn on lights when motion is detected

The most common and useful automation. Automatically turn on lights when entering a room.

<span class="card-meta">**Best for:** Bathrooms, hallways, closets, entryways</span>

<p><a href="/automation/lighting/lights-on-motion.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Turn off lights after motion stops

Complete the cycle by turning lights off when a room is no longer occupied.

<span class="card-meta">**Best for:** All rooms with motion sensors, energy savings</span>

<p><a href="/automation/lighting/lights-off-after-motion.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Bathroom night light

Gentle low-brightness lighting for nighttime bathroom visits that won't disrupt sleep.

<span class="card-meta">**Best for:** Nighttime navigation, sleep quality</span>

<p><a href="/automation/lighting/bathroom-night-light.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Toggle lights when door opens

Automatically turn on lights when doors open - perfect for closets, pantries, and garages.

<span class="card-meta">**Best for:** Closets, pantries, cabinets, garage entry</span>

<p><a href="/automation/lighting/toggle-lights-door.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Outdoor night lights

Turn on outdoor lights automatically at sunset for safety, curb appeal, and convenience.

<span class="card-meta">**Best for:** Curb appeal, safety, holiday lights</span>

<p><a href="/automation/lighting/outdoor-night-lights.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Gradual wake-up lights

Simulate a natural sunrise to wake up gently with gradually brightening lights.

<span class="card-meta">**Best for:** Better mornings, dark winter wake-ups</span>

<p><a href="/automation/lighting/wake-up-lights.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Driveway welcome wave

Create a stunning ripple lighting effect from street to front door when you arrive home.

<span class="card-meta">**Best for:** Impressive arrivals, curb appeal, security</span>

<p><a href="/automation/lighting/driveway-welcome-wave.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Trigger types for lighting

### Motion sensors

Motion sensors are the most popular trigger for lighting automation:

**How it works:** Detects movement using infrared (PIR), microwave, or mmWave technology

**Best for:**
- Rooms you enter briefly (bathrooms, hallways)
- Hands-full situations (laundry, garage)
- Nighttime navigation

**Popular sensors:** Philips Hue, Aqara, SmartThings, Wyze

### Door and window sensors (contact sensors)

Contact sensors trigger lights when doors or windows open:

**How it works:** Magnetic sensor detects when door/window opens or closes

**Best for:**
- Closets and pantries (100% reliable - door must open to access)
- Garage entry lighting
- Preventing lights turning off while occupied

**Popular sensors:** Aqara, SmartThings, Ring, Sonoff

### Time-based triggers

Schedule lights based on time of day:

**How it works:** Automation triggers at specific times or sunset/sunrise

**Best for:**
- Outdoor lighting at dusk
- Morning wake-up lights
- Nighttime security lighting

### Combined triggers

The most reliable automations use multiple triggers:

**Example:** Motion sensor + door sensor + time condition

- Motion triggers lights on
- Door sensor prevents lights turning off while occupied
- Time condition adjusts brightness (dim at night)

---

## Best practices

### Sensor placement

**Motion sensors:**
- 6-8 feet high for optimal coverage
- Pointed toward entry points
- Away from windows and heat sources
- Test coverage before permanent mounting

**Door sensors:**
- Sensor on door frame, magnet on door
- Within 20mm gap when closed
- Clean surfaces before mounting

### Timing strategies

**Quick access spaces (1-2 min timeout):**
- Closets, pantry, laundry room, hallways

**Living spaces (3-5 min timeout):**
- Living room, dining room, kitchen

**Work/relaxation (5-10 min timeout):**
- Home office, reading nook, bathroom

### Night vs. day

Create different behaviors for day and night:

**Daytime:**
- Full brightness (100%)
- Skip if room has natural light

**Nighttime:**
- Reduced brightness (10-30%)
- Warm color temperature (2200-2700K)
- Longer timeout delays

---

## Common challenges

### Lights turn off while room is occupied

**Solutions:**
- Add door sensor to prevent off when door closed
- Increase timeout duration
- Add additional motion sensors for full coverage
- Use mmWave sensors for stationary detection

### False triggers

**Solutions:**
- Adjust sensor sensitivity
- Add lux sensor condition (only in dark)
- Use pet-immune sensors
- Position away from windows and heat sources

### Slow response time

**Solutions:**
- Use local automation (not cloud)
- Add Zigbee/Z-Wave repeaters
- Simplify automation conditions
- Position sensor to detect entry earlier

---

**Get Started:**
- [Turn On Lights When Motion Detected →](/automation/lighting/lights-on-motion.html)
- [Turn Off Lights After Motion Stops →](/automation/lighting/lights-off-after-motion.html)
- [Bathroom Night Light →](/automation/lighting/bathroom-night-light.html)
- [Toggle Lights on Door Open →](/automation/lighting/toggle-lights-door.html)
- [Outdoor Night Lights →](/automation/lighting/outdoor-night-lights.html)
- [Gradual Wake-Up Lights →](/automation/lighting/wake-up-lights.html)
- [Driveway Welcome Wave →](/automation/lighting/driveway-welcome-wave.html)

<div class="page-navigation">
  <a href="/automation/">← Back to All Automations</a>
  <a href="/automation/daily-routines/">Next: Daily Routines →</a>
</div>
