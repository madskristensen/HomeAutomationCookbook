---
layout: automation
title: Support a fire evacuation without delaying the alarm
description: A conservative fire-response recipe that treats listed smoke alarms as primary, turns on useful lighting immediately, and never infers that a fire is over.
keywords: fire safety automation, smoke alarm notification, evacuation lighting, smart home fire alert, smoke alarm listener
last_modified_at: 2026-09-12
image: /assets/img/social/recipes/security/fire-safety.png
compact: true
faqs:
  - question: Should a smart-home rule wait for a second smoke alarm before responding?
    answer: No. Never delay an alarm, evacuation, or emergency call while waiting for another sensor. Any automation is supplemental to the installed smoke and carbon-monoxide alarms.
  - question: Should fire automation unlock every exterior door?
    answer: No. Automatic unlocking can create security and fire-separation problems. Make sure everyone can operate the normal locks and exits without relying on the hub.
  - question: Can the automation announce that the house is safe again?
    answer: No. A clear sensor or stopped alarm is not an all-clear. Only emergency services or a qualified person at the scene should make that decision.
---

# Support a fire evacuation without delaying the alarm

<figure class="content-hero">
  <img src="/assets/img/social/recipes/security/fire-safety.svg" alt="" width="1200" height="630">
</figure>

When a listed smoke or carbon-monoxide alarm activates, optional lighting and notifications run immediately without changing the alarm, delaying evacuation, or declaring an all-clear.

**Best for:** Adding supplemental path lighting and household notifications to a code-compliant alarm and evacuation plan.

**Not for:** Replacing listed alarms, monitored systems, practiced escape routes, or instructions from emergency services.

## Why this exists

A smart home can make an alarm easier to notice, especially at night. It must not become part of the life-safety decision. The installed alarms, clear exits, and the household evacuation plan still work when the hub, power, or internet is unavailable.

This recipe deliberately excludes automatic door unlocking, irrigation, alarm delays, and automatic all-clear messages.

## Logic

<div class="automation-example">IF a supported smoke or carbon-monoxide alarm reports an alarm
THEN turn on the tested evacuation-path lights
AND send a supplemental alert naming the alarm

DO NOT delay the response
DO NOT unlock doors automatically
DO NOT declare an all-clear automatically</div>

- **Trigger:** A supported alarm integration reports smoke or carbon monoxide.
- **Conditions:** None. Do not add mode, time, occupancy, or multi-sensor confirmation conditions.
- **Action:** Turn on fixed path and exterior lights that are safe to operate, then send a supplemental alert naming the reported alarm.
- **Wait / timeout:** None before the first response.
- **Stop condition:** A responsible person manually resets the supplemental response after emergency services or a qualified person says it is safe.
- **Manual override:** Wall switches, normal locks, alarm controls, and exits remain usable without the hub.



## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Detect smoke and carbon monoxide**

Listed alarms installed and maintained for the home. Follow local requirements and the alarm manufacturer's placement, interconnection, testing, and replacement instructions.

</div>
<div class="product-item" markdown="1">

**Expose an alarm event to the hub**

Manufacturer-supported integration or a listed listener approved for the installed alarm type. Failure of the integration must not affect the alarms.

</div>
<div class="product-item" markdown="1">

**Light an exit path**

Existing fixed lights with working wall controls. Lighting is supplemental. People must know the exits in darkness.

</div>
<div class="product-item" markdown="1">

**Reach the household**

Alarm sound and practiced evacuation plan. A phone notification is not the primary warning.

</div>
</div>

Do not add an unlisted relay, microphone, or modification to alarm wiring. Use only equipment and installation methods approved for the installed alarm system.

## Setup notes

1. Install, place, interconnect, test, and replace alarms according to local requirements and manufacturer instructions.
2. Practice an evacuation plan with two ways out where possible and a meeting place outside.
3. Confirm every person can operate the normal locks and exits without the smart home.
4. Add only lights that cannot create a new hazard or obscure alarm indicators.
5. Keep the first alert unconditional and name the alarm location exactly as a person understands it.
6. Treat unavailable, stale, or disconnected integration data as a maintenance problem.
7. Require a manual reset. A stopped alarm or clear reading is not proof that re-entry is safe.

## Test without creating smoke

Use the alarm manufacturer's test procedure. Do not use open flame, burning material, or an improvised aerosol test.

During a planned household test:

- Confirm the physical alarms remain loud and interconnected without the hub.
- Confirm path lights turn on without changing the alarms.
- Confirm alerts identify the correct reported location.
- Disconnect the internet and repeat any behavior expected to remain local.
- Verify that no rule unlocks doors, starts irrigation, delays a response, or sends an all-clear.
- Practice leaving the home and meeting outside.

## Advanced features

### Report integration health

Create a separate maintenance alert when an alarm integration or listener becomes unavailable. Do not represent missing data as "safe."

### Keep intrusion response separate

Glass-break and intrusion events have different risks and actions. Do not combine them with fire logic.

## Failure modes

- **The hub misses the event:** The physical alarms and evacuation plan remain primary. Repair the integration before relying on supplemental actions.
- **A light does not turn on:** Repair it, but do not let one failed light block the rest of the response.
- **A phone is muted or offline:** The installed alarms still provide the primary warning.
- **The wrong location appears:** Rename and retest the integration so the message does not send someone toward danger.
- **The alarm stops:** Keep the supplemental incident open until a person with authority at the scene clears it.
- **Power or internet fails:** Battery-backed alarms and practiced exits must still work.

## FAQ

### Should a smart-home rule wait for a second smoke alarm before responding?

No. Never delay an alarm, evacuation, or emergency call while waiting for another sensor. Any automation is supplemental to the installed smoke and carbon-monoxide alarms.

### Should fire automation unlock every exterior door?

No. Automatic unlocking can create security and fire-separation problems. Make sure everyone can operate the normal locks and exits without relying on the hub.

### Can the automation announce that the house is safe again?

No. A clear sensor or stopped alarm is not an all-clear. Only emergency services or a qualified person at the scene should make that decision.

## Related recipes

- [Get an immediate alert when water is detected](/automation/security/water-leak-response.html)
- [Low-battery alerts](/automation/notifications/low-battery-alerts.html)
- [Safety and security automations](/automation/security/index.html)

<div class="page-navigation">
  <a href="/automation/security/index.html">Back to safety and security automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
