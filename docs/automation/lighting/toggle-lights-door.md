---
layout: automation
title: Turn lights on when a door opens (without losing the wall switch)
description: A local-first contact-sensor lighting recipe for closets, pantries, and utility rooms that keeps the familiar wall switch usable.
keywords: door sensor automation, contact sensor lights, automatic closet lights, door activated lighting, smart door sensor
last_modified_at: 2026-08-30
faqs:
  - question: Should the light turn off as soon as the door closes?
    answer: Only for a small closet where the light is visible from outside. For a pantry or room, use a short delay and keep the wall switch as the immediate fallback.
  - question: Why does the light turn on when nobody is using the closet?
    answer: Check magnet alignment and make sure the sensor reports closed reliably. A loose sensor or a door that flexes can create false open events.
  - question: Can this work when the internet is down?
    answer: It can when the hub and devices support local automation. Regardless, the physical wall switch should always work normally.
---

# Turn lights on when a door opens

Open the closet or pantry, and the light comes on. If the automation is unavailable, the familiar wall switch still works.

**Best for:** Closets, pantries, linen cupboards, and utility spaces where opening one door clearly means someone needs light.

**Not for:** A shared room or exterior door where normal door traffic would make the light surprising. Use a motion or presence recipe when the door does not reliably mean someone entered the lit space.

<p class="last-reviewed">Last reviewed: August 2026</p>

## Why this exists

A contact sensor is more decisive than a motion sensor in a small enclosed space. It sees the action that starts the task - opening the door - and can turn on a fixed light before someone has to search for a switch. The physical switch remains the Level 1 fallback for guests, maintenance, and every failure mode.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect an open door | [Zooz ZSE41 800LR Open/Close XS Sensor](https://www.amazon.com/dp/B09JKKLRLW) | TODO(owner): preferred premium contact sensor | Test the closed state before relying on it. |
| Dim a fixed light | [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN) | TODO(owner): preferred premium dimmer | Keep the physical paddle usable. |
| Switch a fixed light on or off | [UltraPro Z-Wave Long Range On/Off Switch](https://www.amazon.com/dp/B0FX3CTLW2) | TODO(owner): preferred premium on/off switch | Keep the physical paddle usable. |

See [recommended gear](/gear.html) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The contact sensor changes from closed to open.
- **Conditions:** The space is dark enough, or it is within the hours when automatic light makes sense.
- **Action:** Turn on the light at the desired brightness.
- **Wait / timeout:** None for turn-on. A separate close or timeout rule may turn it off later.
- **Stop condition:** A manual wall-switch change is an explicit choice and should not be immediately reversed.
- **Manual override:** The wall switch still wins.

<div class="automation-example">IF the closet door opens AND the closet is dark
THEN turn on the closet light</div>

## Basic automation setup

<div class="setup-steps">
  <div class="setup-step">
    <h4>Mount and test</h4>
    <ul>
      <li>Mount the magnet and sensor where the door closes consistently.</li>
      <li>Open and close the door ten times and confirm every state change appears in the hub.</li>
    </ul>
  </div>
  <div class="setup-step">
    <h4>Start simply</h4>
    <ul>
      <li>Turn the light on when the door opens.</li>
      <li>Add a light-level condition only after the basic trigger is reliable.</li>
    </ul>
  </div>
  <div class="setup-step">
    <h4>Choose a safe off rule</h4>
    <ul>
      <li>For a closet, turn off after the door is closed for one minute.</li>
      <li>For a pantry, start with a longer delay so it does not turn off during a quick return trip.</li>
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
    <p>Replace the entity IDs. This runs locally when the hub, integration, and automation engine are local.</p>
    <pre><code class="language-yaml">automation:
  - alias: Turn on closet light when door opens
    mode: single
    triggers:
      - trigger: state
        entity_id: binary_sensor.closet_door
        from: "off"
        to: "on"
    conditions:
      - condition: numeric_state
        entity_id: sensor.closet_illuminance
        below: 50
    actions:
      - action: light.turn_on
        target:
          entity_id: light.closet
        data:
          brightness_pct: 100</code></pre>
    <p>Remove the illuminance condition if the closet has no light sensor. Test the contact state before enabling the automation.</p>
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

## Failure modes

- **The light does not turn on:** Check that the contact sensor reports open in the hub, then confirm the automation uses that exact entity.
- **The light turns on at random:** Realign the magnet and sensor. A door that flexes or a loose adhesive mount can briefly report open.
- **The light turns on during the day:** Add a light-level condition or limit the automation to the hours when the space is normally dark.
- **The light turns off while someone is using the space:** Increase the close delay. Do not use an instant off rule for a pantry or a space with more than one door.
- **The hub or internet is down:** The physical wall switch remains the fallback. Verify local behavior before depending on it.

## Done when

- [ ] Opening the door ten times produces ten reliable open events in the hub.
- [ ] The light turns on before anyone needs to reach for the wall switch.
- [ ] The light does not turn on in daylight when the condition is enabled.
- [ ] A manual wall-switch change is not immediately reversed by the automation.
- [ ] Someone who did not build it can use the space without instructions.

## FAQ

### Should the light turn off as soon as the door closes?

Only for a small closet where the light is visible from outside. For a pantry or room, use a short delay and keep the wall switch as the immediate fallback.

### Why does the light turn on when nobody is using the closet?

Check magnet alignment and make sure the sensor reports closed reliably. A loose sensor or a door that flexes can create false open events.

### Can this work when the internet is down?

It can when the hub and devices support local automation. Regardless, the physical wall switch should always work normally.

## Related recipes

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Disable automations when door is closed](/automation/lighting/disable-on-door-close.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">Back to lighting automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
