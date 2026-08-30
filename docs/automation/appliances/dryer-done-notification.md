---
layout: automation
title: Get notified when the dryer finishes
description: A platform-neutral laundry recipe that detects sustained dryer vibration and sends one completion alert without controlling appliance power.
keywords: dryer finished alert, dryer vibration sensor, laundry notification, dryer automation, dryer done notification
last_modified_at: 2026-08-30
faqs:
  - question: Why use vibration instead of a smart plug for a dryer?
    answer: Many electric dryers use a 240-volt high-current circuit that a normal smart plug cannot safely monitor. A battery vibration sensor is non-invasive when mounted away from hot and moving parts.
  - question: How long should vibration be absent before the dryer counts as finished?
    answer: Measure the dryer's longest normal pause and cooldown behavior, then use a delay comfortably longer than that observation.
  - question: What if the washer makes the dryer sensor vibrate?
    answer: Reposition the sensor, require sustained vibration before marking the dryer as running, and test washer-only cycles before trusting the alert.
---

# Get notified when the dryer finishes

Detect a real drying cycle, wait through normal pauses, and send one alert when sustained vibration stops.

**Best for:** A dryer with a safe exterior mounting point and a vibration pattern that can be distinguished from nearby appliances.

**Not for:** A sensor mounted near heat, vents, belts, drums, controls, or other moving parts, or an ordinary smart plug connected to a 240-volt dryer circuit.

## Why this exists

Dryers can pause, reverse, tumble intermittently, or run a cooldown phase. Nearby washers can shake the same floor. A useful completion alert must prove the dryer was running and wait longer than its normal quiet periods.

Vibration sensing is imperfect, but it is non-invasive and does not put an unverified relay in the dryer's power path.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect dryer vibration | TODO(owner): verified battery vibration sensor | TODO(owner): preferred vibration sensor | Mount only on a cool, fixed exterior panel after testing surface temperature through a full cycle. |
| Clear the waiting-laundry state | A manual dashboard or phone action | TODO(owner): verified dryer-door sensor | Do not assume one sensor can reliably detect both vibration and door position. |

See [recommended gear](/gear.html) for the job-first checklist. The site does not yet have an owner-verified dryer vibration sensor, so no product link is presented as a recommendation.

## Logic

- **Trigger:** Vibration remains active long enough to prove the dryer started.
- **Conditions:** The sensor is available and the dryer was not already marked as running.
- **Action:** Mark the dryer as running and clear any previous waiting-laundry state.
- **Wait / timeout:** Wait until vibration remains inactive longer than the dryer's longest observed pause or cooldown gap.
- **Stop condition:** Mark the cycle finished, send one notification, and set a waiting-laundry state.
- **Manual override:** A person can clear the waiting state without changing power to the dryer.

<div class="automation-example">IF dryer vibration remains active for the calibrated start delay
THEN mark the dryer as running

IF vibration remains inactive for the calibrated finish delay
AND the dryer is marked as running
AND the sensor is available
THEN send one "Dryer finished" notification
AND mark laundry as waiting
AND clear the running marker</div>

## Setup notes

1. Find a fixed exterior panel that remains cool and does not block vents, labels, controls, or service access.
2. Attach the sensor securely with removable mounting material suitable for the surface.
3. Observe at least three full cycles, including cooldown and wrinkle-prevention behavior.
4. Record the shortest sustained vibration that proves a start and the longest quiet period during a cycle.
5. Run the washer by itself and confirm it does not mark the dryer as running.
6. Create separate running and waiting-laundry states.
7. Test with silent logging before enabling notifications.
8. Add one completion notification, not repeated announcements.

## Calibrate from evidence

The sensor's location matters as much as its sensitivity:

| Test | Expected result |
|---|---|
| Dryer off, washer running | Dryer remains idle |
| Door closes firmly | A bump does not prove a cycle started |
| Full dryer cycle | Sustained vibration marks running |
| Normal pause or cooldown | Dryer remains marked running |
| Cycle completed | One alert after the calibrated quiet delay |
| Sensor unavailable | State becomes unknown, not finished |

If the washer and dryer cannot be distinguished reliably, move the sensor or use professionally installed circuit-level energy monitoring.

## Advanced features

### Add one restrained reminder

Set a waiting-laundry state after completion. Send one later reminder if it remains set, then let the household clear it manually or through a separately verified door sensor.

### Respect wrinkle-prevention modes

Some dryers tumble again after the main cycle. Decide whether the household wants the alert at the main-cycle end or after all intermittent tumbling, then calibrate against that selected mode.

### Monitor sensor health

Alert on a low battery or stale sensor before laundry day. Never interpret unavailable as no vibration.

## Failure modes

- **Washer activity marks the dryer as running:** Reposition the sensor and require a longer sustained-start period.
- **A door slam starts the cycle marker:** Increase the start delay so a single bump cannot qualify.
- **Alert arrives during cooldown:** Lengthen the finish delay beyond the longest observed quiet period.
- **No alert arrives:** Confirm the sensor stayed attached, remained available, and set the running marker.
- **Duplicate alerts arrive:** Clear the running marker with the first completion event.
- **The sensor falls or gets hot:** Stop using that mounting point and inspect the sensor and adhesive.
- **Someone tries to add a normal smart plug:** Do not connect an ordinary inline plug to a high-voltage or high-current dryer circuit.

## Done when

- [ ] The mounting point stays cool and clear through a complete cycle.
- [ ] Three representative cycles establish reliable start and finish delays.
- [ ] Washer-only operation never marks the dryer as running.
- [ ] A door slam never proves a cycle started.
- [ ] Every test cycle creates exactly one completion notification.
- [ ] An unavailable sensor does not count as finished.
- [ ] The dryer still works normally without the automation.

## FAQ

### Why use vibration instead of a smart plug for a dryer?

Many electric dryers use a 240-volt high-current circuit that a normal smart plug cannot safely monitor. A battery vibration sensor is non-invasive when mounted away from hot and moving parts.

### How long should vibration be absent before the dryer counts as finished?

Measure the dryer's longest normal pause and cooldown behavior, then use a delay comfortably longer than that observation.

### What if the washer makes the dryer sensor vibrate?

Reposition the sensor, require sustained vibration before marking the dryer as running, and test washer-only cycles before trusting the alert.

## Related recipes

- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)
- [Appliance automations](/automation/appliances/index.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)

<div class="page-navigation">
  <a href="/automation/appliances/index.html">Back to appliance automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
