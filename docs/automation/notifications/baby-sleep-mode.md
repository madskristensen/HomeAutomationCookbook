---
layout: automation
title: Set a nursery quiet mode without guessing whether a baby is asleep
description: Let a caregiver explicitly request nursery quiet mode while urgent safety alerts, manual controls, and normal emergency behavior remain active.
keywords: nursery quiet mode, baby sleep automation, quiet lighting, nursery automation, caregiver control
last_modified_at: 2026-08-30
faqs:
  - question: Can white-noise power use prove that a baby is asleep?
    answer: No. It can be a convenient hint that quiet mode was requested, but it does not reveal whether anyone is asleep, awake, present, or safe.
  - question: Which alerts should quiet mode suppress?
    answer: Only optional nuisance sounds and bright convenience lighting chosen by the caregiver. Smoke, carbon-monoxide, leak, security, medical, and other urgent alerts must still run.
  - question: Should quiet mode turn off motion lighting completely?
    answer: Usually no. A very dim path light or manual-only behavior is safer for a caregiver entering the room at night.
---

# Set a nursery quiet mode without guessing whether a baby is asleep

A caregiver explicitly selects Quiet, and the room uses dimmer, quieter convenience behavior without suppressing urgent alerts or manual controls.

**Best for:** Nurseries, nap rooms, guest rooms, and home offices where a person wants a clear temporary quiet state.

**Not for:** Detecting sleep, monitoring a child, replacing a baby monitor, or muting safety and security alerts.

## Why this exists

Caregivers should decide when the nursery enters Quiet mode rather than leaving that judgment to a sensor. A white-noise machine can be on while a baby is awake, and it can be off while a baby is asleep. Power use is not proof of sleep, presence, identity, or safety.

Model the thing the automation actually knows: a caregiver requested Quiet mode. Keep its effects narrow, visible, easy to cancel, and separate from every urgent alert.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Request quiet mode**

A physical control or deliberate app button. The label should say Quiet, not Baby sleeping.

</div>
<div class="product-item" markdown="1">

**Provide low light**

Existing dimmable room or hallway light. Keep the normal switch usable.

</div>
<div class="product-item" markdown="1">

**End quiet mode**

The same visible control. Automatic expiry may remind, but must not claim anyone woke up.

</div>
</div>

## Logic

- **Trigger:** A caregiver deliberately selects Quiet.
- **Conditions:** None based on inferred sleep, motion, sound, or device power.
- **Action:** Use the household's chosen dim lighting and lower only optional chimes or media.
- **Wait / timeout:** Remind the caregiver after the expected quiet window, but do not silently change safety behavior.
- **Stop condition:** A caregiver selects Normal.
- **Manual override:** Physical light, audio, monitor, and emergency controls remain usable.

<div class="automation-example">IF a caregiver selects Nursery Quiet
THEN use dim path lighting
AND lower only optional household sounds

KEEP smoke, carbon-monoxide, leak, security, medical, and urgent alerts active

IF a caregiver selects Normal
THEN restore normal convenience behavior</div>

## Setup notes

1. Name the state Nursery Quiet, not Baby sleeping.
2. Put an obvious control where a caregiver starts and ends the routine.
3. List every automation Quiet may change.
4. Limit changes to convenience lighting, optional chimes, and entertainment volume.
5. Explicitly exclude alarms, urgent notifications, locks, cameras, monitors, and medical devices.
6. Keep a low manual path-light option for nighttime care.
7. Add a reminder after the expected nap or overnight window so the state is not forgotten.
8. Make the active state visible without using red or green as the only cue.

## Optional convenience signals

A white-noise machine, monitor, or lamp can suggest that someone may want Quiet mode. It may offer a prompt such as "Turn on Nursery Quiet?" It must not set a sleeping state or suppress anything by itself.

Motion and sound can likewise prompt a caregiver to check the room. They do not determine whether the baby is awake or safe.

## Advanced features

### Use room-specific effects

Keep nursery lighting very dim, reduce an adjacent hallway light, and leave the rest of the home unchanged. Broad whole-house changes are harder for guests to understand.

### Add a temporary visit mode

A caregiver can temporarily brighten the room for feeding, medicine, or cleanup without ending Quiet. The physical control still wins.

## Failure modes

- **Quiet is left on all day:** Show the state clearly and send a reminder instead of silently inferring wake time.
- **A convenience device turns on by itself:** Do not let device power activate Quiet without a person.
- **A caregiver needs brighter light:** Provide a direct physical override that does not require an app.
- **An urgent alert is muted:** Remove Quiet from that alert path immediately and retest every urgent category.
- **The hub restarts:** Restore a visible known state or ask for confirmation. Do not infer sleep.
- **A guest does not understand the mode:** Use plain labels and keep normal room controls functional.

## Done when

- [ ] A caregiver deliberately starts and ends Quiet mode.
- [ ] The state is labeled Quiet, not Sleeping.
- [ ] Only documented convenience behaviors change.
- [ ] Every urgent safety, security, and medical alert still runs.
- [ ] Physical lighting and audio controls still work.
- [ ] Power, motion, sound, and camera signals do not infer sleep or identity.
- [ ] A forgotten mode creates a reminder rather than a false wake assumption.

## FAQ

### Can white-noise power use prove that a baby is asleep?

No. It can be a convenient hint that quiet mode was requested, but it does not reveal whether anyone is asleep, awake, present, or safe.

### Which alerts should quiet mode suppress?

Only optional nuisance sounds and bright convenience lighting chosen by the caregiver. Smoke, carbon-monoxide, leak, security, medical, and other urgent alerts must still run.

### Should quiet mode turn off motion lighting completely?

Usually no. A very dim path light or manual-only behavior is safer for a caregiver entering the room at night.

## Related recipes

- [Guest mode](/automation/daily-routines/guest-mode.html)
- [Dim bathroom lighting at night](/automation/lighting/bathroom-night-light.html)
- [Notification automations](/automation/notifications/index.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notification automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
