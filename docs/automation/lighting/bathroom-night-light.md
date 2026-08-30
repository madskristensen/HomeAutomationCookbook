---
layout: automation
title: Turn on a dim bathroom light at night (without waking everyone)
description: A local-first bathroom night-light recipe that uses motion, low brightness, and a reliable wall-switch fallback.
keywords: bathroom night light, nighttime motion lighting, low brightness automation, smart bathroom lighting, motion sensor dimming, night mode lighting
last_modified_at: 2026-08-30
faqs:
  - question: What brightness should a bathroom night light use?
    answer: Start at 10 percent, then test it in the dark. Raise it only enough for safe navigation.
  - question: Why does a bathroom motion light turn off during a shower?
    answer: A PIR sensor can miss someone who is still or hidden by steam and a shower curtain. Use a longer timeout or a presence sensor.
---

# Turn on a dim bathroom light at night

Walk in half asleep, get enough light to see, and do not wake the house. If it fails, the wall switch still works.

**Best for:** Bathrooms with a dimmable light and a sensor placed near the entry.

**Not for:** A bathroom where a short PIR timeout would turn lights off during a shower. A PIR sees movement, not a still person. Start with a longer timeout or use the [PIR vs mmWave presence guide](/getting-started/pir-vs-mmwave-presence.html) to add occupancy sensing.

## Why this exists

Bright bathroom light at 2am is miserable. This recipe uses only enough light to navigate safely, then hands the shutoff to the paired motion-lighting recipe. It should work without explaining a special night mode to a guest.

<div class="info-box">
  <strong>🌙 Why This Automation Matters</strong>
  <ul>
    <li><strong>Sleep Quality:</strong> Bright lights suppress melatonin production. Low-light maintains sleep readiness and makes it easier to fall back asleep.</li>
    <li><strong>Safety:</strong> No stumbling in the dark. Safe navigation for all ages, reduces fall risk for elderly. Kids can navigate independently.</li>
    <li><strong>Family-Friendly:</strong> Whole household benefits. Great for overnight guests. Works for everyone automatically with no explanation needed.</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Nighttime Navigation</h4>
    <ul>
      <li><strong>Middle of Night Bathroom Trips</strong> - Common for everyone</li>
      <li><strong>Nighttime Hallway Navigation</strong> - Safe path to bathroom</li>
      <li><strong>Kids Walking to Parents' Bedroom</strong> - Safe independent movement</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Early Morning & Kitchen</h4>
    <ul>
      <li><strong>Getting Water from Kitchen</strong> - Any nighttime navigation</li>
      <li><strong>Early Morning Routine</strong> - Before sunrise gentle lighting</li>
    </ul>
  </div>
</div>

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect bathroom motion, humidity, temperature, and light | [Lower-cost bathroom multisensor](https://www.amazon.com/dp/B0D47WR1S2) | [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY) | Verify compatibility for the lower-cost option. Use the extra readings where they solve a real bathroom problem. |
| Dim a fixed light | [Lower-cost smart dimmer](https://www.amazon.com/dp/B0C2B8SP3W) | [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN) | Verify hub compatibility. The physical paddle must remain usable. |

See [recommended gear](/gear.html) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** Bathroom or entry motion is detected.
- **Conditions:** It is within your night window, and optionally the room is dark enough.
- **Action:** Turn on the bathroom light at 10 percent. Set a warm color temperature only if the light supports it.
- **Wait / timeout:** The paired [turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html) recipe owns the timeout. Start at 10 minutes for a shower bathroom.
- **Stop condition:** New motion cancels the shutoff. A manual wall-switch change wins.
- **Manual override:** The wall switch still wins.

<div class="automation-example">IF bathroom motion is detected during the night window
THEN turn on the light at 10%</div>

## Creating "Night Mode"

Night Mode is a home state that indicates sleeping hours. Set it up using:

**Option 1: Time-based**
- IF time is 10:00 PM
- THEN set house to Night Mode

**Option 2: Manual trigger**
- IF "Good Night" voice command
- OR bedtime button pressed
- THEN set house to Night Mode

**Option 3: Presence-based**
- IF last person goes to bedroom
- AND time is after 9:00 PM
- THEN set house to Night Mode

See [daily routine automations](/automation/daily-routines/index.html) for related night-mode setup.

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Multiple brightness levels</h3>
    <p>Adjust brightness based on time of night:</p>
    <div class="brightness-schedule">
      <div class="brightness-item">
        <span class="time-badge">9 PM - 11 PM</span>
        <span class="brightness-level">15%</span>
        <span class="brightness-desc">Still awake, moderate light</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">11 PM - 5 AM</span>
        <span class="brightness-level">5%</span>
        <span class="brightness-desc">Deep night, very warm (2200K)</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">5 AM - 7 AM</span>
        <span class="brightness-level">20%</span>
        <span class="brightness-desc">Early morning, warm (2700K)</span>
      </div>
    </div>
  </div>
  
  <div class="feature-card">
    <h3>Strategic sensor placement</h3>
    <p>The motion sensor doesn't have to be in the room you want to light up:</p>
    <ul>
      <li><strong>Separate toilet room:</strong> Sensor in main bathroom triggers both lights</li>
      <li><strong>Bedroom sensor</strong> triggers bathroom lights</li>
      <li><strong>Hallway sensor</strong> triggers multiple room lights</li>
      <li><strong>Stairway sensor</strong> triggers upstairs bathroom</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Color temperature guidelines</h3>
    <p>Choose appropriate color for minimal sleep disruption:</p>
    <ul>
      <li><strong>Warm White (2200-2700K):</strong> Minimal melatonin suppression</li>
      <li><strong>Ultra Warm/Red (1800K):</strong> Even less sleep disruption</li>
      <li><strong>Avoid Cool White (4000K+):</strong> Suppresses melatonin, disrupts sleep</li>
    </ul>
  </div>
</div>

<div class="placement-grid">
  <div class="placement-card">
    <h3>Brightness by location</h3>
    <ul>
      <li><strong>Very Low (5-8%):</strong> Bedroom, baby's room</li>
      <li><strong>Low (10-15%):</strong> Bathroom, toilet room</li>
      <li><strong>Medium-Low (15-25%):</strong> Hallway, kitchen, stairs</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Extending to other rooms</h3>
    <ul>
      <li><strong>Hallways:</strong> 15%, warm white (2200K)</li>
      <li><strong>Kitchen:</strong> 20%, warm (2700K)</li>
      <li><strong>Stairs:</strong> 25%, safety priority</li>
      <li><strong>Kids' rooms:</strong> 8%, very low</li>
    </ul>
  </div>
</div>

<div class="best-practice-card">
  <h3>Auto turn-off integration</h3>
  <ol>
    <li>Trigger: Motion sensor shows no motion for 5 minutes</li>
    <li>Condition: House mode is "Night"</li>
    <li>Action: Turn off bathroom light</li>
  </ol>
</div>

See [turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html) for complete details.

<div class="feature-grid">
  <div class="feature-card">
    <h3>Per-person brightness</h3>
    <p>Use presence detection to adjust brightness by person:</p>
    <ul>
      <li><strong>Parent 1 home:</strong> 5% brightness (very dim preference)</li>
      <li><strong>Parent 2 home:</strong> 15% brightness (slightly brighter preference)</li>
      <li><strong>Guests/others:</strong> 10% brightness (default)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Gradual brightening</h3>
    <p>Lights start very dim and gradually increase:</p>
    <ol>
      <li>Start at 5% brightness</li>
      <li>Wait 3 seconds</li>
      <li>Check if motion still detected</li>
      <li>If yes, increase to 10% with 2-second transition</li>
    </ol>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights still too bright</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Even at lowest setting, lights are too bright for comfortable sleep.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Reduce to 5% or lower if bulb supports it</li>
        <li>Use red/amber color if supported</li>
        <li>Add dimming film to bulb (diffuses light)</li>
        <li>Use dedicated nightlight instead</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights too dim for safety</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lighting is not sufficient for safe navigation.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Increase to 15-20%</li>
        <li>Use warmer but brighter setting</li>
        <li>Add additional lighting in critical areas</li>
        <li>Motion-sensitive nightlights as backup</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Delay before lights come on</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Noticeable delay between motion detection and lights turning on.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Ensure local automation processing</li>
        <li>Move sensor closer to entry point</li>
        <li>Add Zigbee/Z-Wave repeaters</li>
        <li>Optimize automation logic</li>
      </ul>
    </div>
  </div>
</div>

## Failure modes

- **The light is too bright:** Start at 10 percent, then test in a dark bathroom. Increase only enough for safe footing.
- **It turns off during a shower:** A PIR can miss a still person through steam or a shower curtain. Use the paired off recipe with a 10-minute starting timeout, or follow the [PIR vs mmWave presence guide](/getting-started/pir-vs-mmwave-presence.html) to keep detecting a person after motion stops.
- **The sensor sees a hallway instead:** Aim and test the sensor so passing traffic does not light the bathroom unnecessarily.
- **A guest uses the wall switch:** Treat it as the final answer. The next automation must not immediately undo that choice.
- **The hub or internet is down:** The wall switch remains the fallback. Confirm that any relied-on Level 2 path is local.

## Done when

- [ ] Enter during the night window and the room has enough light to navigate before you reach the switch.
- [ ] Enter outside the night window and the recipe does not turn on the dim night setting.
- [ ] Shower or sit still for the chosen off timeout and confirm the light does not turn off.
- [ ] Use the physical switch and verify the automation respects it.
- [ ] Have someone who did not configure the automation use the room at night.

## FAQ

### What brightness should a bathroom night light use?

Start at 10 percent, then test it in the dark. Raise it only enough for safe navigation.

### Why does a bathroom motion light turn off during a shower?

A PIR sensor can miss someone who is still or hidden by steam and a shower curtain. Use a longer timeout or a presence sensor.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">← Back to lighting automations</a>
  <a href="/automation/index.html">View all automations →</a>
</div>
