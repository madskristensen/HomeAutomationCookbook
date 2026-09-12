---
layout: default
title: Smart lighting automation ideas and recipes
description: Make lights respond to movement, doors, and time of day while keeping every familiar wall switch useful.
permalink: /automation/lighting/index.html
canonical_url: https://www.homeautomationcookbook.com/automation/lighting/index.html
keywords: smart lighting automation, motion sensor lights, automatic lighting, door sensor lights, outdoor lights, night light automation
---

# Lighting automations

Lighting is usually the first thing people automate, because the payoff is easy to feel: you stop reaching for switches in the dark and stop wondering whether you left a light on somewhere. Good lighting automations support the way you already move through the house, and every wall switch keeps working exactly as it always has.

<div class="category-intro" markdown="1">

## Why automate lighting?

**Fewer switches to hunt for** - Lights come on as you walk into a room, so you are not groping for a switch with your hands full or the room dark.

**Less energy left running** - A room that empties out turns its own lights off, so you do not have to circle back and check.

**Safer footing at night** - Gentle nighttime lighting means a trip to the bathroom does not require full brightness or a fumble in the dark.

**One less thing to remember** - Once it is set up, the lighting keeps working without you thinking about it each time.

**A trigger for almost any room** - Motion, a door opening, or the time of day - choose whichever fits the space, and change it later if it does not.

**Fast enough to feel automatic** - Modern sensors respond quickly enough that the light feels like it was already on when you needed it.

</div>

## Essential automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Turn on lights when motion is detected

The automation most people try first. Lights come on as you enter a room, so you stop reaching for a switch when your hands are full or the room is dark.

<span class="card-meta">**Best for:** Bathrooms, hallways, closets, entryways</span>

<p><a href="/automation/lighting/lights-on-motion.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Turn off lights after motion stops

Finish the cycle so a light left on in an empty room is not something you have to remember to check.

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

Turn on lights the moment a door opens, so closets, pantries, and garage entries are already lit instead of making you feel around first.

<span class="card-meta">**Best for:** Closets, pantries, cabinets, garage entry</span>

<p><a href="/automation/lighting/toggle-lights-door.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Turn a closet light off after closing

Complete the door-lighting cycle without reversing a manual wall-switch choice or turning off while the door reopens.

<span class="card-meta">**Best for:** Small single-door closets, cupboards, and shallow pantries</span>

<p><a href="/automation/lighting/disable-on-door-close.html" class="card-link">View automation</a></p>

</div>

<div class="automation-card" markdown="1">

### Outdoor night lights

Turn on outdoor lights at sunset, so the path to your door is already lit and nobody has to remember a switch.

<span class="card-meta">**Best for:** Curb appeal, safety, holiday lights</span>

<p><a href="/automation/lighting/outdoor-night-lights.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Gradual wake-up lights

Simulate a natural sunrise, so mornings start gradually instead of with a jarring alarm and a hand fumbling for a lamp.

<span class="card-meta">**Best for:** Better mornings, dark winter wake-ups</span>

<p><a href="/automation/lighting/wake-up-lights.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Verified entry welcome lights

Confirm a real after-dark arrival before lighting the entry, so the walk from the car is lit without unlocking a door or overriding dusk lighting.

<span class="card-meta">**Best for:** A safe path from the driveway or entry after dark</span>

<p><a href="/automation/lighting/driveway-welcome-wave.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Trigger types for lighting

### Motion sensors

Motion sensors are a common trigger for lighting automation:

**How it works:** Detects movement using infrared (PIR), microwave, or mmWave technology

**Best for:**
- Rooms you enter briefly (bathrooms, hallways)
- Hands-full situations (laundry, garage)
- Nighttime navigation

Choose a sensor that works with your hub and fits the room. See [Recommended gear](/getting-started/device-guide.html#products-i-have-used) for the models I have personally used.

### Door and window sensors (contact sensors)

Contact sensors trigger lights when doors or windows open:

**How it works:** Magnetic sensor detects when door/window opens or closes

**Best for:**
- Closets and pantries where the door state matches the lighting need
- Garage entry lighting
- Preventing lights turning off while occupied

Contact sensors are easier to reason about than occupancy sensors, but alignment and battery state still matter.

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

Follow the sensor manufacturer's placement and alignment guidance. Test the final approach path, seated positions, doors, sunlight, and heat sources before mounting anything permanently.

### Timing strategies

Start with a conservative timeout, then tune it from real use. Passing spaces can usually use a shorter delay. Bathrooms, offices, and rooms where people sit still need a longer delay or a presence sensor.

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
- [Verified entry welcome lights →](/automation/lighting/driveway-welcome-wave.html)

<div class="page-navigation">
  <a href="/automation/">← Back to All Automations</a>
  <a href="/automation/daily-routines/index.html">Next: daily routines</a>
</div>
