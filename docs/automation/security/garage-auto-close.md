---
layout: automation
title: Close a garage safely after an open-door alert
description: Alert first, keep people in control, and allow unattended closing only through equipment designed for it with working entrapment protection and warnings.
keywords: garage door left open, garage close alert, unattended garage closing, garage door safety, tilt sensor
last_modified_at: 2026-08-30
faqs:
  - question: Is a motion sensor enough to prove the garage is empty?
    answer: No. Motion can miss a still person, child, pet, or obstruction. It is not entrapment protection and must not authorize a close.
  - question: Can an automation close any garage-door opener?
    answer: No. Use unattended closing only when the opener and controller are designed, installed, and configured for it according to their instructions, including required warnings and entrapment protection.
  - question: Does a closed tilt sensor prove the doorway is clear?
    answer: No. It reports door position only. The opener's approved obstruction and entrapment protections must make the closing decision.
---

# Close a garage safely after an open-door alert

The house reports a garage door left open, and closing remains manual unless the installed opener and controller explicitly support safe unattended operation.

**Best for:** Open-door reminders, clear status, and manufacturer-approved closing equipment with working photo-eyes, warnings, and normal wall controls.

**Not for:** Using phone location, motion, a camera, or a tilt sensor as proof that the doorway is clear.

## Why this exists

An open garage door is easy to forget, but an unattended close moves a large door where people, pets, vehicles, and objects may be present. Presence and motion signals are useful for deciding who should receive an alert. They are not safety devices.

Start with an alert. Add unattended closing only through equipment designed for that operation, installed and maintained exactly as required.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Know door position | [THIRDREALITY Zigbee Smart Garage Door Tilt Sensor](https://www.amazon.com/dp/B0CZP2CJXF) | [Ecolink Z-Wave Plus Garage Door Tilt Sensor](https://www.amazon.com/dp/B01MRZB0NT) | I have used both. They report position, not a clear doorway. |
| Close the door | Existing wall control and opener remote | No personally verified unattended-closing controller yet | Use only equipment approved for the opener and unattended operation. |
| Detect an obstruction | The opener's required, tested entrapment protection | The opener's required, tested entrapment protection | Never replace or bypass it with hobby sensors. |

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the tilt sensors I have used. No unattended-closing controller is recommended until I have verified one.

## Logic

- **Trigger:** The door remains open longer than the household expects.
- **Conditions:** The position sensor is recent and available.
- **Action:** Send a persistent alert naming the door and its reported state.
- **Wait / timeout:** Escalate once if the alert remains unacknowledged.
- **Stop condition:** The position sensor reports closed after a person closes it, or a person explicitly dismisses the reminder.
- **Manual override:** The normal wall control and remotes remain primary.

<div class="automation-example">IF the garage door remains open past the chosen delay
THEN send a persistent open-door alert

IF a person chooses Close
AND the installed opener supports that operation
THEN let the opener perform its required warning and safety checks

DO NOT use motion, location, a camera, or a tilt sensor as entrapment protection</div>

## Setup notes

1. Test the opener, wall control, remote, photo-eyes, auto-reverse, audible warning, and visual warning according to manufacturer instructions.
2. Mount and calibrate the tilt sensor so open, closed, unavailable, and low-battery states are distinct.
3. Start with alerts only.
4. Make the message identify the exact door and how long it has been open.
5. Treat unavailable status as unknown, not closed.
6. If the equipment supports a user-requested remote close, let its built-in warning and safety behavior run without bypasses.
7. Enable unattended schedules only if the complete installed system explicitly supports them.

## Before enabling unattended closing

- Confirm the opener and added controller are compatible and approved for the exact installation.
- Confirm all required entrapment-protection devices work.
- Confirm the required audible and visual warnings occur before and during movement.
- Confirm obstruction causes reversal as designed.
- Confirm a failed or unavailable position sensor cannot report success.
- Confirm everyone understands the warnings and normal controls.
- Retest on the schedule required by the manufacturer and after any service.

## Advanced features

### Escalate based on context

Away or nighttime state can change who receives an alert or how quickly it escalates. It must not replace the opener's own safety requirements.

### Confirm the final position

After a supported close command, report success only when the position sensor reaches closed within the expected time. Otherwise report "close not confirmed" and require inspection.

## Failure modes

- **Tilt sensor is unavailable:** Report unknown status and do not claim the door is closed.
- **Door reverses:** Report that closing failed and require a person to inspect the path and opener.
- **Photo-eyes are blocked or misaligned:** Repair them before any remote or unattended closing.
- **Motion reports clear while someone is present:** Ignore it for safety authorization.
- **Phone location says everyone left:** Use it only to route the alert, not to approve movement.
- **Close command receives no final state:** Send "close not confirmed" rather than a success message.

## Done when

- [ ] Open, closed, unavailable, and low-battery states are distinguishable.
- [ ] The alert names the exact door and remains visible until handled.
- [ ] Normal wall controls and remotes still work.
- [ ] Required photo-eyes, warnings, and reversal behavior pass manufacturer tests.
- [ ] No motion, location, camera, or tilt sensor is used as entrapment protection.
- [ ] A failed close never produces a success-shaped notification.
- [ ] Unattended closing is disabled unless the complete installed system supports it.

## FAQ

### Is a motion sensor enough to prove the garage is empty?

No. Motion can miss a still person, child, pet, or obstruction. It is not entrapment protection and must not authorize a close.

### Can an automation close any garage-door opener?

No. Use unattended closing only when the opener and controller are designed, installed, and configured for it according to their instructions, including required warnings and entrapment protection.

### Does a closed tilt sensor prove the doorway is clear?

No. It reports door position only. The opener's approved obstruction and entrapment protections must make the closing decision.

## Related recipes

- [Garage door notification](/automation/security/garage-door-notification.html)
- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Low-battery alerts](/automation/notifications/low-battery-alerts.html)

<div class="page-navigation">
  <a href="/automation/security/index.html">Back to safety and security automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
