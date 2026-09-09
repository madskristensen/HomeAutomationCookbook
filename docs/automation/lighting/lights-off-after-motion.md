---
layout: automation
title: Turn lights off after motion stops (without leaving people in the dark)
description: A conservative motion-lighting off recipe that respects still occupants, manual wall-switch choices, and local-first control.
keywords: motion sensor lights off, automatic light shutoff, occupancy detection, smart lighting automation, turn off lights automatically
last_modified_at: 2026-08-30
compact: true
faqs:
  - question: How long should motion lights stay on?
    answer: Start longer than you think, then reduce the timeout only after the household has used the room normally for several days.
  - question: Why do bathroom motion lights turn off while someone is inside?
    answer: A PIR sensor can miss someone who is still or behind a shower curtain. Use a longer timeout, another sensor, or presence detection.
  - question: Can a wall switch override the automatic shutoff?
    answer: It should. Treat a manual change as an explicit choice and avoid turning the light back off immediately.
---

# Turn lights off after motion stops

Leave the room, lights off. Stay still, and they should not leave you in the dark. The wall switch still wins when someone wants a different answer.

**Best for:** Hallways, closets, laundry rooms, and other spaces with predictable short visits.

**Not for:** A bathroom with a short PIR timer, or a home office where someone sits still for long periods. A PIR detects movement, not a person sitting still. Start with a longer delay, or follow the [PIR vs mmWave presence article](/articles/pir-vs-mmwave-presence.html).

## Why this exists

The off half makes automatic lighting useful without making it hostile. It should wait long enough for real people, then turn the light off after the room is clear. It must not fight a guest who used the familiar wall switch.

💡 For reliable coverage and testing, see [how to place motion sensors for reliable automations](/articles/motion-sensor-placement.html).

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Quick Access Spaces</h4>
    <ul>
      <li><strong>Bathroom</strong> - Turn off lights 5 minutes after no motion detected</li>
      <li><strong>Closets</strong> - Turn off immediately after 1 minute (quick access areas)</li>
      <li><strong>Garage</strong> - Turn off after 3-5 minutes of no activity</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Living & Work Spaces</h4>
    <ul>
      <li><strong>Living Areas</strong> - Turn off lights 2 minutes after no motion at nighttime</li>
      <li><strong>Home Office</strong> - Longer delay (10 minutes) for stationary work</li>
    </ul>
  </div>
</div>

## Logic

<div class="automation-example">IF the room has been clear for the timeout
AND no manual override is active
THEN turn off the light</div>

- **Trigger:** The room sensor reports no motion for the chosen timeout.
- **Conditions:** The light was turned on by this automation, no other room sensor is active, and no manual override is active.
- **Action:** Turn the light off.
- **Wait / timeout:** Start at 5 to 10 minutes for a bathroom or quiet room. Reduce only after normal household testing.
- **Stop condition:** New motion, another active sensor, or a manual wall-switch change cancels the shutoff.
- **Manual override:** The wall switch still wins.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect fast entry motion**

[Shelly BLU Motion ZB](https://www.amazon.com/dp/B0H4GD6GGK/ref=nosim?tag=madsk0f-20). A PIR needs a conservative timer for people who sit still.

</div>
<div class="product-item" markdown="1">

**Dim a fixed light**

[TP-Link Tapo S505D Matter Smart Dimmer Switch](https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20). Verify hub compatibility. Keep the physical paddle usable.

</div>
<div class="product-item" markdown="1">

**Switch a fixed light on or off**

[Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20). Keep the physical paddle usable.

</div>
</div>

For a bathroom that needs humidity, temperature, and light readings too, use the [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY/ref=nosim?tag=madsk0f-20) instead. It is not my first choice when the fastest motion response is the job.

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. Product recommendations and the affiliate relationship are explained in the [disclosure](/disclosure.html).

💡 **For outdoor placement and weather protection**, see [how to place motion sensors for reliable automations](/articles/motion-sensor-placement.html).

## Setup notes

Start with a longer delay than you expect to need, then shorten it only after normal household use.

- **Quick access spaces:** One to two minutes can work for a closet or hallway.
- **Living spaces:** Start at three to five minutes.
- **Bathrooms and quiet spaces:** Start at 10 minutes, or use a contact sensor, another motion sensor, or [mmWave presence sensing](/articles/pir-vs-mmwave-presence.html) before reducing the delay.

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Day vs. night timing</h3>
    <p>Create separate automations with different delay times:</p>
    <ul>
      <li><strong>Daytime:</strong> Shorter delays (2-3 minutes), more active movement</li>
      <li><strong>Nighttime:</strong> Longer delays (5-10 minutes), slower movement</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Multiple sensor logic</h3>
    <p>For larger rooms, use multiple sensors to ensure no one is present:</p>
    <ul>
      <li>All motion sensors must show "no motion" before turning off</li>
      <li>Set appropriate delay (e.g., 5 minutes)</li>
      <li>Prevents false shutoffs in sensor blind spots</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Activity-based override</h3>
    <p>Don't turn off lights if other activity detected:</p>
    <ul>
      <li>TV is on in the room</li>
      <li>Music is playing</li>
      <li>Computer is active</li>
      <li>Smart plug shows power usage</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn off while room is occupied</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Person sitting very still, motion sensor dead zone, or delay too short.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add door sensor - don't turn off if door closed</li>
        <li>Use longer delay (5-10 minutes instead of 2-3)</li>
        <li>Add additional motion sensors for full coverage</li>
        <li>Use occupancy sensors instead of motion</li>
        <li>Add manual override button to extend time</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights stay on too long after leaving</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Delay too long or sensor sees movement outside room (hallway traffic).
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reduce delay time</li>
        <li>Reposition sensor to focus on room interior only</li>
        <li>Add door sensor - turn off immediately when door closes</li>
        <li>Use presence detection for faster response</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Inconsistent behavior</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sometimes works, sometimes doesn't respond at all.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Replace batteries before fully depleted</li>
        <li>Add Zigbee/Z-Wave repeaters</li>
        <li>Check sensor configuration</li>
        <li>Update firmware</li>
        <li>Test sensor range and coverage</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="placement-grid">
  <div class="placement-card">
    <h3>Testing your delays</h3>
    <ul>
      <li><strong>Start conservative:</strong> 10 minute delay initially</li>
      <li><strong>Monitor:</strong> Watch for false shutoffs over several days</li>
      <li><strong>Gradually reduce:</strong> Find the sweet spot</li>
      <li><strong>Room-specific:</strong> Different delay per room type</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Sensor coverage verification</h3>
    <ul>
      <li>Walk through room at different paths</li>
      <li>Stand still in each area for 2 minutes</li>
      <li>Verify motion sensor still "sees" you</li>
      <li>Add sensors to eliminate dead zones</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Manual override options</h3>
    <p>Always provide a way to override automation:</p>
    <ul>
      <li><strong>Physical switch:</strong> Manual operation keeps lights on indefinitely</li>
      <li><strong>Voice command:</strong> "Keep bathroom lights on" for 30 min override</li>
      <li><strong>Dashboard button:</strong> Toggle to disable/enable automation</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Energy savings</h3>
    <p>While LED bulbs use minimal power, automatic shutoff still provides benefits:</p>
    <ul>
      <li>10W LED × 2 hours/day = 7.3 kWh/year per bulb</li>
      <li>Halogen/incandescent: 60W bulbs save 10x more</li>
      <li>Commercial spaces: significant savings</li>
      <li>Environmental impact: reduced energy generation</li>
    </ul>
  </div>
</div>

## Failure modes

- **The light turns off while someone is still:** Increase the timeout before changing anything else. A PIR does not see a person working quietly, reading, showering, or standing behind a towel. For those rooms, follow the [PIR vs mmWave presence article](/articles/pir-vs-mmwave-presence.html).
- **A guest uses the wall switch:** Treat that as an override. Do not let the next sensor event immediately undo it.
- **The sensor sees motion outside the room:** Reposition it or narrow its view before shortening the timeout.
- **The hub reboots or the internet is down:** The wall switch remains the fallback. A local automation may resume after the hub is ready, but do not rely on it for Level 1 control.
- **The room is in use at night:** Use a longer timeout for quiet nighttime use, especially in bathrooms.

## FAQ

### How long should motion lights stay on?

Start longer than you think, then reduce the timeout only after the household has used the room normally for several days.

### Why do bathroom motion lights turn off while someone is inside?

A PIR sensor can miss someone who is still or behind a shower curtain. Use a longer timeout, another sensor, or presence detection.

### Can a wall switch override the automatic shutoff?

It should. Treat a manual change as an explicit choice and avoid turning the light back off immediately.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Bathroom night light](/automation/lighting/bathroom-night-light.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">← Back to lighting automations</a>
  <a href="/automation/index.html">View all automations →</a>
</div>
