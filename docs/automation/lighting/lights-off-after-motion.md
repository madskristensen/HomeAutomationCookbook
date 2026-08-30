---
layout: automation
title: Turn lights off after motion stops (without leaving people in the dark)
description: A conservative motion-lighting off recipe that respects still occupants, manual wall-switch choices, and local-first control.
keywords: motion sensor lights off, automatic light shutoff, occupancy detection, smart lighting automation, turn off lights automatically
last_modified_at: 2026-08-30
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

**Not for:** A bathroom with a short PIR timer, or a quiet work space. A PIR detects movement, not a person sitting still. Start with a longer delay, or use an [mmWave presence sensor](/gear.html) that can keep detecting someone when motion stops.

<p class="last-reviewed">Last reviewed: August 2026</p>

## Why this exists

The off half makes automatic lighting useful without making it hostile. It should wait long enough for real people, then turn the light off after the room is clear. It must not fight a guest who used the familiar wall switch.

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

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect fast entry motion | [Shelly BLU Motion ZB](https://www.amazon.com/dp/B0H4GD6GGK) | [Aeotec SmartThings Motion Sensor](https://www.amazon.com/dp/B095TZTGNB) - owner favorite for fast reactions | A PIR needs a conservative timer for people who sit still. |
| Dim a fixed light | [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN) | TODO(owner): preferred premium dimmer | Keep the physical paddle usable. |
| Switch a fixed light on or off | [UltraPro Z-Wave Long Range On/Off Switch](https://www.amazon.com/dp/B0FX3CTLW2) | TODO(owner): preferred premium on/off switch | Keep the physical paddle usable. |

For a bathroom that needs humidity, temperature, and light readings too, use the [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY) instead. It is not the owner's first choice when the fastest motion response is the job.

See [recommended gear](/gear.html) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

<div class="info-box">
  <strong>💡 Outdoor Tip</strong>
  <ul>
    <li>Use weather-rated sensors (IP65+) or protect from elements</li>
  </ul>
</div>

## Logic

- **Trigger:** The room sensor reports no motion for the chosen timeout.
- **Conditions:** The light was turned on by this automation, no other room sensor is active, and no manual override is active.
- **Action:** Turn the light off.
- **Wait / timeout:** Start at 5 to 10 minutes for a bathroom or quiet room. Reduce only after normal household testing.
- **Stop condition:** New motion, another active sensor, or a manual wall-switch change cancels the shutoff.
- **Manual override:** The wall switch still wins.

<div class="automation-example">IF the room has been clear for the timeout
AND no manual override is active
THEN turn off the light</div>

<div class="info-box">
  <strong>⏱️ Timing Strategies by Room Type</strong>
  <ul>
    <li><strong>Quick Access (1-2 min):</strong> Closets, pantry, laundry room, hallways - Brief visits, quick in and out</li>
    <li><strong>Living Spaces (3-5 min):</strong> Living room, dining room, kitchen, home gym - May have brief stationary moments, but generally active</li>
    <li><strong>Work/Relaxation (5-10 min):</strong> Home office, reading nook, craft room, bathroom - People often sit still for extended periods</li>
    <li><strong>Bathroom Special:</strong> Use door sensor override (don't turn off if door closed), OR extended delay (10-15 min), OR multiple sensors</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Motion no longer detected for X minutes</li>
      <li>Fast-access areas: 1-2 minutes</li>
      <li>Living spaces: 3-5 minutes</li>
      <li>Work areas: 5-10 minutes</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Time-based:</strong> Different delays for day vs. night<br>
    <strong>Door status:</strong> Don't turn off if bathroom door is closed (someone may be sitting still)<br>
    <strong>Additional sensors:</strong> Check other sensors in room for activity
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn off light switch/bulb</li>
      <li>Can include gradual dimming before turning off (advanced)</li>
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
              <p>Replace the entity IDs. This version waits five minutes, checks that the sensor is still clear, then turns the light off.</p>

              <pre><code class="language-yaml">automation:
          - alias: Turn off entry light after motion clears
            mode: restart
            triggers:
              - trigger: state
                entity_id: binary_sensor.entry_motion
                to: "off"
                for: "00:05:00"
            conditions:
              - condition: state
                entity_id: binary_sensor.entry_motion
                state: "off"
            actions:
              - action: light.turn_off
                target:
                  entity_id: light.entry</code></pre>

              <p>For a bathroom, start at 10 minutes or add a second sensor. Add a helper that records a manual wall-switch override before using this in a shared room.</p>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">IF</span>
        <span class="step-content">Motion sensor no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Door sensor is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Turn off light</span>
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
        <span class="step-content">Motion inactive for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door contact is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Motion Lighting app or Rule Machine
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
        <span class="step-content">Motion stops</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Wait</span>
        <span class="step-content">5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">If</span>
        <span class="step-content">Bathroom door is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Turn off bathroom light</span>
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
        <span class="step-content">Motion sensor detects no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door contact is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
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
        <span class="step-content">Motion no motion for 5 minutes</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Door sensor is open</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Turn off light</span>
      </div>
    </div>
  </div>
</div>

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

- **The light turns off while someone is still:** Increase the timeout before changing anything else. A PIR does not see a person reading, showering, or standing behind a towel. For those rooms, add an [mmWave presence sensor](/gear.html), which can detect a person after motion stops.
- **A guest uses the wall switch:** Treat that as an override. Do not let the next sensor event immediately undo it.
- **The sensor sees motion outside the room:** Reposition it or narrow its view before shortening the timeout.
- **The hub reboots or the internet is down:** The wall switch remains the fallback. A local automation may resume after the hub is ready, but do not rely on it for Level 1 control.
- **The room is in use at night:** Use a longer timeout for quiet nighttime use, especially in bathrooms.

## Done when

- [ ] Leave the room and confirm the light turns off after the selected delay.
- [ ] Sit or stand still in every normal part of the room for the same delay and confirm it does not turn off unexpectedly.
- [ ] Toggle the wall switch manually and verify the automation does not fight the choice.
- [ ] Test after a hub restart and, where local control is expected, with the internet disconnected.
- [ ] Have a guest use the room without explaining the automation.

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
