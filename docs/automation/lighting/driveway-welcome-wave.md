---
layout: automation
title: Light the entry after a verified arrival
description: A platform-neutral welcome-light recipe that confirms a real arrival before lighting the entry and never unlocks a door or overrides manually controlled lights.
keywords: arrival lighting, welcome home lights, entry light automation, outdoor arrival lights, verified presence lighting
last_modified_at: 2026-08-30
faqs:
  - question: Why not turn on the lights as soon as a phone enters the home area?
    answer: Phone location can drift or trigger while someone passes nearby. Use it only to create a short pending-arrival window, then require a physical entry signal before running the welcome lights.
  - question: Should the welcome recipe turn lights off later?
    answer: Only lights it turned on. Track automation ownership, cancel the timeout after a manual change, and leave dusk lighting or already-on lights alone.
  - question: Can the same arrival signal unlock the door?
    answer: No. Lighting is easy to reverse; access control is not. Keep keys, keypads, or a deliberate lock action separate from this recipe.
---

# Light the entry after a verified arrival

After dark, confirm that someone has reached the entry before turning on the porch or path light. Keep the lock, garage, alarm, and every manual light control separate.

**Best for:** A home with a reliable Away state, an exterior or entry light control I have used, and a physical signal that confirms someone reached the property.

**Not for:** A phone geofence by itself, an unverified driveway sensor, theatrical multi-zone effects that have not been installed, or any automatic unlocking or garage movement.

## Why this exists

Arrival lighting should make the final steps to the door easier, not advertise every location wobble. Phone presence can suggest that someone is approaching, but a door contact, deliberate garage operation, keypad event, or other tested property signal is stronger evidence that the arrival is real.

The old version of this page described a multi-zone driveway wave without verified hardware. This recipe uses lighting and contact hardware I have used instead. Add more zones only after each physical light and trigger exists and works independently.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Control plug-in exterior lighting | [Minoston Outdoor Smart Plug](https://www.amazon.com/dp/B07X52W1J8) | [Minoston 800 Series outdoor Z-Wave plug](https://www.amazon.com/dp/B0B7MLX1ZC) | Use only with a suitable outdoor receptacle, enclosure, and lighting load. |
| Switch a fixed entry light | [Leviton DG15S Zigbee switch](https://www.amazon.com/dp/B000U39QL6) | [UltraPro Z-Wave Long Range On/Off Switch](https://www.amazon.com/dp/B0FX3CTLW2) | The wall paddle remains the normal control. |
| Confirm entry-door activity | [SONOFF SenseGuard Gen2 Zigbee contact sensor](https://www.amazon.com/dp/B0GKFB3XCL) | [Zooz ZSE41 800LR Open/Close XS Sensor](https://www.amazon.com/dp/B09JKKLRLW) | A door event confirms activity; it does not prove identity or unlock anything. |
| Suggest that someone is approaching | No personally verified household presence source yet | No personally verified combined arrival method yet | Use phone location only to open a short pending-arrival window. |

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product links on this page are direct, non-affiliate Amazon links. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** A pending-arrival state is followed by a tested physical entry signal within a short confirmation window.
- **Conditions:** It is dark, the home was Away before the candidate arrival, no safety mode blocks the action, and the target light is not already on.
- **Action:** Turn on the approved entry or path light and mark only that light as owned by this welcome run.
- **Wait / timeout:** Keep the light on for a household-tested entry period, then turn it off only if automation still owns it.
- **Stop condition:** The pending arrival expires without a physical signal, the person returns to Away, or a manual light change cancels ownership.
- **Manual override:** Wall switches, outdoor plug controls, keys, keypads, locks, and garage controls remain independent.

<div class="automation-example">IF a candidate arrival creates Pending arrival
AND a tested entry signal occurs before that state expires
AND it is dark
THEN turn on the approved entry light if it was off
AND mark that light as owned by this welcome run

IF the entry timeout ends
AND the welcome run still owns the light
THEN turn it off
BUT never unlock a door or move a garage</div>

## Setup notes

1. Complete the [safe arrival routine](/automation/daily-routines/unlock-door-arrival.html) and use its Home, Away, and pending-arrival states.
2. Start with one porch or entry light I have used, not a sequence of imagined zones.
3. Choose a physical confirmation signal that occurs reliably during real arrivals.
4. Log candidate arrivals and confirmation timing before controlling a light.
5. Require both darkness and a real Away-to-arrival transition.
6. If the target light is already on, leave it alone and do not claim ownership.
7. Clear ownership whenever someone changes the light manually.
8. Test the timeout, a canceled arrival, a second person arriving, and an internet outage.

## Choose a confirmation signal

| Signal | What it can establish |
|---|---|
| Entry contact opens during pending arrival | Someone used that entry; it does not establish identity |
| Deliberate garage or gate operation | The access point was operated; keep movement control separate |
| Verified local vehicle or driveway sensor | Something reached the property; test animals, deliveries, and street traffic |
| Phone enters a geofence | Someone may be approaching; insufficient by itself |

Use the weakest signal only for reversible lighting. Never reuse it as proof for unlocking, disarming, or opening access points.

## Advanced features

### Add a second real lighting zone

After the first light is reliable, add one physically installed path zone. Turn zones on for visibility, not spectacle, and track ownership separately so one timeout cannot override another schedule or manual state.

### Handle later arrivals quietly

When someone is already home, a later arrival may still need the entry light. Use the same physical confirmation and darkness rules, but skip whole-house mode, climate, and announcement changes.

### Coordinate with dusk lighting

If the outdoor-night-light recipe already owns the porch light, the arrival recipe does nothing to that device. It may turn on a separate entry light, but it must not shorten the dusk schedule.

## Failure modes

- **Lights run while someone passes nearby:** Require a physical property signal after the candidate arrival.
- **The light is late:** Measure the real delay and choose a confirmation point earlier on the actual path without enlarging the geofence blindly.
- **Dusk lighting turns off after the arrival timeout:** Track ownership per light and never claim a light that was already on.
- **A manual change is reversed:** Clear ownership and cancel the timeout on any external light change.
- **The second arrival repeats whole-house actions:** Keep this recipe scoped to entry lighting and let the first-arrival routine own Home-state changes.
- **The entry contact fires for departures:** Require the pending-arrival or known arrival context, not the contact event alone.
- **The sensor becomes unavailable:** Expire pending arrival without running the light and show a maintenance warning.
- **The hub or internet is down:** The wall switch, plug control, key, keypad, and garage control remain normal fallbacks.

## Done when

- [ ] Passing near the property never turns on the welcome light.
- [ ] A real after-dark arrival turns on the light before it is needed.
- [ ] Daylight arrivals do not change lighting.
- [ ] A light already on remains under its original schedule or manual control.
- [ ] A manual change cancels welcome-light ownership.
- [ ] Departure contact events do not look like arrivals.
- [ ] A second arrival changes only the entry lighting.
- [ ] No lock, garage, gate, or alarm changes from this recipe.
- [ ] The entry remains usable when the hub or internet is unavailable.

## FAQ

### Why not turn on the lights as soon as a phone enters the home area?

Phone location can drift or trigger while someone passes nearby. Use it only to create a short pending-arrival window, then require a physical entry signal before running the welcome lights.

### Should the welcome recipe turn lights off later?

Only lights it turned on. Track automation ownership, cancel the timeout after a manual change, and leave dusk lighting or already-on lights alone.

### Can the same arrival signal unlock the door?

No. Lighting is easy to reverse; access control is not. Keep keys, keypads, or a deliberate lock action separate from this recipe.

## Related recipes

- [Prepare the house when someone arrives](/automation/daily-routines/unlock-door-arrival.html)
- [Turn outdoor lights on at dusk](/automation/lighting/outdoor-night-lights.html)
- [Lighting automations](/automation/lighting/index.html)

<div class="page-navigation">
  <a href="/automation/lighting/index.html">Back to lighting automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
