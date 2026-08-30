---
layout: automation
title: Turn lights on when you walk in (and keep the wall switch)
description: A local-first motion-lighting recipe for turning lights on when someone enters, while keeping the familiar wall switch in control.
keywords: motion sensor lights, automatic lights, smart home lighting, motion detection, home automation, smart lights
last_modified_at: 2026-08-30
faqs:
  - question: Why do motion lights turn on too slowly?
    answer: Put the sensor where it sees someone before they reach the switch, and keep the automation local where the platform supports it.
  - question: Should motion lights turn on during the day?
    answer: Usually no. Add a light-level condition or restrict the recipe to the times when the room is normally dark.
  - question: What happens when the internet is down?
    answer: A local hub and compatible devices can keep the automation running, but the physical wall switch must work either way.
---

# Turn lights on when you walk in

Walk in, lights on. If that fails at 2am, the wall switch still works.

**Best for:** Hallways, closets, entryways, laundry rooms, and bathrooms with a sensor that sees the door.

**Not for:** A room where people sit still for long periods, or a bathroom with a short PIR timer. A PIR is best for detecting entry motion. Use a longer timeout and an [mmWave presence sensor](/gear.html) where the automation must know that someone is still in the room.

## Why this exists

Nobody should have to fumble for a switch with a basket of laundry or explain the light system to a guest. The first detection needs to happen before a hand reaches the wall control. Keep the switch useful so the room remains ordinary when the hub, sensor, or internet is not.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Indoor automation</h4>
    <ul>
      <li><strong>Nighttime navigation</strong> - Bathroom lights turn on at low brightness when you get up at night</li>
      <li><strong>Home office</strong> - Lights automatically turn on when you enter your workspace</li>
      <li><strong>Hallways</strong> - Lights turn on as you move through the house</li>
      <li><strong>Closets</strong> - No more fumbling for switches in dark spaces</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Outdoor automation</h4>
    <ul>
      <li><strong>Garden shed</strong> - Motion sensor triggers light when you enter</li>
      <li><strong>Porch light</strong> - Automatically lights up for guests and delivery drivers</li>
    </ul>
  </div>
</div>

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect fast entry motion | [Shelly BLU Motion ZB](https://www.amazon.com/dp/B0H4GD6GGK) | [Aeotec SmartThings Motion Sensor](https://www.amazon.com/dp/B095TZTGNB) - my favorite for fast reactions | Mount it where it sees the approach to the doorway. |
| Dim a fixed light | [Lower-cost smart dimmer](https://www.amazon.com/dp/B0C2B8SP3W) | [UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN) | Verify hub compatibility. Keep the physical paddle usable. |
| Switch a fixed light on or off | [Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6) | [UltraPro Z-Wave Long Range On/Off Switch](https://www.amazon.com/dp/B0FX3CTLW2) | Keep the physical paddle usable. |

For a bathroom that needs humidity, temperature, and light readings too, use the [Zooz ZSE11 800LR Q Sensor](https://www.amazon.com/dp/B09GDL6BGY) instead. It is not my first choice when the fastest motion response is the job.

See [recommended gear](/gear.html) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

<div class="info-box">
  <strong>💡 Outdoor Motion Sensing Tip</strong>
  <ul>
    <li>Use sensors specifically rated for outdoor use (IP65 or higher)</li>
    <li>OR protect indoor sensors with weatherproof enclosures</li>
    <li>OR place sensors under eaves to avoid direct water exposure</li>
  </ul>
</div>

## Logic

- **Trigger:** The entry sensor changes from clear to motion detected.
- **Conditions:** The room is dark enough, or it is within the hours you want automatic light.
- **Action:** Turn on the light. Use a dim level at night if the light supports it.
- **Wait / timeout:** None for turn-on. The paired [turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html) recipe owns the timeout.
- **Stop condition:** A manual wall-switch change should prevent the off recipe from undoing the person's choice.
- **Manual override:** The wall switch still wins.

<div class="automation-example">IF entry motion is detected AND the room is dark
THEN turn on the light</div>

## Setup notes

Start with only the trigger and light action. Once that is reliable, add the daylight condition and any night brightness adjustment.

- **Daytime:** Leave the light off when daylight is sufficient.
- **Evening:** Use the brightness that makes the room useful.
- **Deep night:** Start at 10 to 20 percent and raise it only enough for safe navigation.

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Multiple brightness levels</h3>
    <p>Create different levels throughout the night:</p>
    <div class="brightness-schedule">
      <div class="brightness-item">
        <span class="time-badge">9 PM - 11 PM</span>
        <span class="brightness-level">30%</span>
        <span class="brightness-desc">Still awake, need moderate light</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">11 PM - 5 AM</span>
        <span class="brightness-level">10%</span>
        <span class="brightness-desc">Minimal disturbance</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">5 AM - 7 AM</span>
        <span class="brightness-level">20%</span>
        <span class="brightness-desc">Gentle wake-up</span>
      </div>
      <div class="brightness-item">
        <span class="time-badge">7 AM - 9 PM</span>
        <span class="brightness-level">100%</span>
        <span class="brightness-desc">Full brightness</span>
      </div>
    </div>
  </div>
  
  <div class="feature-card">
    <h3>Lux-based activation</h3>
    <p>Only turn on lights if the room is actually dark:</p>
    <ul>
      <li>Add a condition that light level must be below a certain threshold (e.g., 100 lux)</li>
      <li>This prevents lights from turning on during daytime when natural light is sufficient</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Zone-based motion</h3>
    <p>For larger rooms, use multiple motion sensors to track which area someone is in and only light that zone.</p>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn on too slowly</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Delay between motion detection and lights turning on causes you to reach for the switch.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check sensor placement - should detect motion before entering room</li>
        <li>Reduce automation processing time - use local control instead of cloud</li>
        <li>Use faster communication protocols (Zigbee/Z-Wave vs WiFi)</li>
        <li>Optimize automation logic to minimize conditions</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Lights turn on when not needed</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Lights activate from pets, sunlight reflections, or other false triggers.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Adjust motion sensor sensitivity</li>
        <li>Add lux sensor condition to prevent daytime activation</li>
        <li>Use pet-immune motion sensors</li>
        <li>Position sensor away from windows and heat sources</li>
        <li>Add time-based conditions</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Inconsistent performance</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Sometimes works, sometimes doesn't.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Check sensor battery levels</li>
        <li>Verify wireless signal strength (Zigbee/Z-Wave mesh)</li>
        <li>Replace batteries before completely dead</li>
        <li>Add repeaters/extenders for distant sensors</li>
        <li>Check for interference from other devices</li>
      </ul>
    </div>
  </div>
</div>

## Sensor placement best practices

<div class="placement-grid">
  <div class="placement-card">
    <h3>Height</h3>
    <ul>
      <li><strong>Optimal:</strong> 6-8 feet high for best coverage</li>
      <li><strong>Corners:</strong> Good for monitoring entire room</li>
      <li><strong>Entry points:</strong> Near doors for immediate detection</li>
    </ul>
  </div>
  
  <div class="placement-card">
    <h3>Angle</h3>
    <ul>
      <li><strong>Ceiling mount:</strong> Wide coverage, detects all motion</li>
      <li><strong>Wall mount:</strong> Directional, catches people entering</li>
      <li><strong>Corner mount:</strong> 90° coverage, good for hallways</li>
    </ul>
  </div>
</div>

<div class="best-practice-card">
  <h3>Coverage testing</h3>
  <ol>
    <li>Mount sensor temporarily with tape</li>
    <li>Walk through room at different paths</li>
    <li>Verify all entry points are covered</li>
    <li>Check for dead zones</li>
    <li>Adjust position or add additional sensors</li>
    <li>Permanently mount once confirmed</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>Near windows</strong> - Sunlight and outdoor motion cause false triggers</li>
    <li><strong>Near heating/AC vents</strong> - Temperature changes trigger sensors</li>
    <li><strong>Pointed at moving objects</strong> - Ceiling fans, curtains, pets</li>
    <li><strong>Behind furniture</strong> - Blocks detection zone</li>
  </ul>
</div>

## Failure modes

- **The light turns on after someone reaches the switch:** Move the sensor to see the entry path earlier and keep the path local.
- **It turns on in daylight:** Add a light-level condition, then test it on a bright overcast day as well as at night.
- **A guest stands still after the light turns on:** This recipe should be paired with a conservative off timeout. Use presence sensing where stillness is normal.
- **The sensor is hidden or affected by steam:** Keep it clear of towels, furniture, vents, and the shower plume.
- **The hub or internet is down:** The physical switch remains the fallback. Verify any Level 2 automation is local before depending on it.

## Done when

- [ ] Walk in from every usual entry path and the light is on before your hand reaches the switch.
- [ ] During daytime, the light stays off when the room is already bright.
- [ ] Turn the wall switch on or off and confirm the paired off recipe does not immediately reverse that choice.
- [ ] Disconnect the internet, if your setup supports local control, and verify the automation still works.
- [ ] Have someone who did not build it try the room without instructions.

## FAQ

### Why do motion lights turn on too slowly?

Put the sensor where it sees someone before they reach the switch, and keep the automation local where the platform supports it.

### Should motion lights turn on during the day?

Usually no. Add a light-level condition or restrict the recipe to the times when the room is normally dark.

### What happens when the internet is down?

A local hub and compatible devices can keep the automation running, but the physical wall switch must work either way.

## Related recipes

- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Bathroom night light](/automation/lighting/bathroom-night-light.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">← Back to lighting automations</a>
  <a href="/automation/index.html">View all automations →</a>
</div>
