---
layout: default
title: Lighting Automations - Smart Home Lighting Guide
description: Master automatic lighting for your smart home. Motion-triggered lights, door-activated lighting, night lights, and outdoor illumination.
keywords: smart lighting automation, motion sensor lights, automatic lighting, door sensor lights, outdoor lights, night light automation
---

# Lighting automations

Lighting is often where people begin. Perhaps because light itself carries such weight - the warmth of a lamp welcoming you home after dark, the gentle glow that guides bare feet through the hallway at 3 a.m., the simple relief of never fumbling for a switch with arms full of groceries. When lights respond to presence rather than commands, a house starts to feel less like a collection of rooms and more like a space that knows you.

<div class="category-intro" markdown="1">

## Why automate lighting?

**Hands-free convenience** - Lights appear as you enter and fade when you leave

**Energy savings** - Empty rooms stay dark without anyone remembering to flip a switch

**Safety at night** - Gentle illumination guides midnight wanderings without startling anyone awake

**True automation** - Works without any input from you

**Versatile triggers** - Motion sensors, door sensors, time of day, and more

**Instant response** - Modern sensors detect presence in milliseconds

</div>

## Essential automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Turn on lights when motion is detected

The cornerstone of any lighting automation. A motion sensor notices your arrival before you reach for the switch.

<span class="card-meta">**Best for:** Bathrooms, hallways, closets, entryways</span>

<p><a href="/automation/lighting/lights-on-motion.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Turn off lights after motion stops

The natural companion to motion-triggered lighting. Rooms return to darkness when they are no longer needed.

<span class="card-meta">**Best for:** All rooms with motion sensors, energy savings</span>

<p><a href="/automation/lighting/lights-off-after-motion.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Bathroom night light

In the small hours, bathroom light should behave more like embers than daylight - just enough red-amber glow to guide your feet, never enough to remind your brain that morning has not yet arrived.

<span class="card-meta">**Best for:** Nighttime navigation, sleep quality</span>

<p><a href="/automation/lighting/bathroom-night-light.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Toggle lights when door opens

Closets and pantries have a natural trigger: the door itself. Light appears the moment you reach inside and vanishes when you step away.

<span class="card-meta">**Best for:** Closets, pantries, cabinets, garage entry</span>

<p><a href="/automation/lighting/toggle-lights-door.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Outdoor night lights

As daylight fades, outdoor lights rise to meet the darkness - for safety, for curb appeal, and for the simple pleasure of coming home to a house that looks awake.

<span class="card-meta">**Best for:** Curb appeal, safety, holiday lights</span>

<p><a href="/automation/lighting/outdoor-night-lights.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Gradual wake-up lights

A simulated sunrise that coaxes you from sleep - brightness climbing slowly, gently, like dawn arriving at its own pace on a winter morning.

<span class="card-meta">**Best for:** Better mornings, dark winter wake-ups</span>

<p><a href="/automation/lighting/wake-up-lights.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Driveway welcome wave

A theatrical flourish for homecoming: lights rippling from the street to your front door, as if the house itself is rising to greet you.

<span class="card-meta">**Best for:** Impressive arrivals, curb appeal, security</span>

<p><a href="/automation/lighting/driveway-welcome-wave.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Trigger types for lighting

### Motion sensors

The motion sensor is perhaps the most patient of all smart home devices. It watches doorways and hallways, never tiring, never distracted, ready to summon light the instant someone appears. For rooms you pass through quickly - bathrooms, closets, entryways - it is the ideal trigger.

**How it works:** Detects movement using infrared (PIR), microwave, or mmWave technology

**Best for:**
- Rooms you enter briefly (bathrooms, hallways)
- Hands-full situations (laundry, garage)
- Nighttime navigation

**Popular sensors:** Philips Hue, Aqara, SmartThings, Wyze

### Door and window sensors (contact sensors)

Where motion sensors guess, contact sensors know. A pantry door can only be opened by someone who intends to reach inside. That certainty makes contact sensors ideal for spaces where the act of entry is the only signal you need.

**How it works:** Magnetic sensor detects when door/window opens or closes

**Best for:**
- Closets and pantries (100% reliable - door must open to access)
- Garage entry lighting
- Preventing lights turning off while occupied

**Popular sensors:** Aqara, SmartThings, Ring, Sonoff

### Time-based triggers

Some lights belong to the clock rather than to motion. Porch lights that greet the dusk, bedroom lamps that gently brighten before the alarm, holiday strands that sparkle through the evening hours.

**How it works:** Automation triggers at specific times or sunset/sunrise

**Best for:**
- Outdoor lighting at dusk
- Morning wake-up lights
- Nighttime security lighting

### Combined triggers

The most thoughtful automations weave multiple signals together. Motion brings the light, a door sensor keeps it on while you linger, and the time of day decides whether you receive full brightness or a soft amber glow.

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
