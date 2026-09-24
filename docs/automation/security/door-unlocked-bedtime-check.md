---
layout: automation
date: 2026-09-24
title: Alert when a door is left unlocked
description: Keep an unlocked exterior door visible, check locks at bedtime, and add automatic locking only with current door and lock feedback.
keywords: door left unlocked alert, bedtime lock check, smart lock notification, unlocked door reminder, night lock automation
last_modified_at: 2026-09-24
image: /assets/img/social/recipes/security/door-unlocked-bedtime-check.png
compact: true
faqs:
  - question: Is a closed door the same as a locked door?
    answer: No. Use the lock's actual locked, unlocked, jammed, or unknown state. A contact sensor only reports whether the door is open or closed.
  - question: Should the bedtime routine automatically lock every door?
    answer: Start with a status check and alert. Add a lock command only after door position, lock feedback, jam handling, battery state, manual keys, and household expectations are tested.
  - question: What should happen when a lock is unavailable?
    answer: Report the state as unknown and ask for a manual check. Never treat missing data or an old locked event as confirmation that the door is secure.
---

# Alert when a door is left unlocked and check again at bedtime

<figure class="content-hero">
  <img src="/assets/img/social/recipes/security/door-unlocked-bedtime-check.svg" alt="An exterior door lock reports unlocked, prompting an alert and a separate bedtime status check" width="1200" height="630">
</figure>

Keep an exterior door's unlocked state visible after a useful delay, then run one intentional bedtime check that names every unlocked, jammed, or unknown lock.

**Best for:** Exterior doors with a smart lock that reports current lock state, plus a contact sensor when the automation may issue a lock command.

**Not for:** Inferring locked state from a closed door, locking from phone location alone, or hiding a jammed or unavailable lock behind a successful-looking notification.

## Why this exists

People unlock doors for groceries, children, pets, visitors, or work outside and then forget to relock them. Repeated immediate notifications become noise, while a quiet persistent status and one bedtime check remove the need to walk the house and test every lock.

The household keeps keys, thumb turns, and normal lock controls. The automation reports what it knows, distinguishes unknown state, and asks for a person when the result cannot be confirmed.

## What I used

<div class="product-list" markdown="1">
<div class="product-item" markdown="1">

**Report lock state**

No personally verified smart-lock recommendation yet. Use a lock that reports locked, unlocked, jammed, battery, and unavailable state to the chosen platform.

</div>
<div class="product-item" markdown="1">

**Report door position**

A compatible contact sensor can report open or closed when an automatic lock command is being considered. It does not prove the lock is engaged.

</div>
</div>

## Logic

<div class="automation-example">IF an exterior lock remains unlocked for the normal-use delay
AND the home is not in an approved unlocked period
THEN show a persistent "Door unlocked" status
AND send one notification naming the door

IF someone intentionally starts Good night
THEN check every exterior lock
AND report each unlocked, jammed, or unknown lock

IF verified automatic locking is enabled
AND the matching door is confirmed closed
THEN send the lock command
AND report success only after the lock confirms locked</div>

- **Trigger:** A lock remains unlocked past a delay, or the household intentionally starts the bedtime check.
- **Conditions:** The lock report is current, no approved temporary-unlocked period is active, and any automatic lock command has a confirmed closed-door state.
- **Action:** Create persistent status, send one named notification, and at bedtime summarize every lock needing attention.
- **Wait / timeout:** Use a normal-use delay during the day and a short confirmation timeout after any command.
- **Stop condition:** Clear the incident only when the lock reports locked or a person explicitly acknowledges an unresolved manual check.
- **Manual override:** Keys, thumb turns, keypads, and normal lock controls remain available.

## Setup notes

1. Name each lock and door by location.
2. Confirm the platform exposes current locked, unlocked, jammed, battery, and unavailable states.
3. Add a contact sensor before considering an automatic command.
4. Observe how long doors normally stay unlocked during arrivals, unloading, and outdoor activity.
5. Set a delay that catches forgotten locks without interrupting normal use.
6. Create an intentional temporary-unlocked mode for parties, contractors, or repeated trips outside.
7. Make the bedtime action a status check before enabling control.
8. Keep physical keys available and test every household member's normal entry method.
9. Test low battery, jammed bolt, open door, stale state, hub restart, and internet loss.

## Build the alert-first version

The first version should not move the lock:

1. Show a persistent unlocked status after the delay.
2. Send one notification naming the door.
3. Clear the status when the lock reports locked.
4. Report jammed or unavailable as separate attention states.
5. Include all unresolved locks in the intentional bedtime summary.

This version removes repeated checking while leaving the final action with the household.

## Add automatic locking carefully

Only add an automatic command after the alert-first behavior is dependable. Require:

- A current unlocked report from the lock.
- A current closed report from the matching door sensor.
- No temporary-unlocked mode.
- No recent manual unlock that should remain in effect.
- Acceptable battery state.
- A tested command timeout.
- Final locked confirmation from the lock itself.

If the door is open, the lock is jammed, or either state is unknown, do not claim success. Ask for a manual check.

Do not automatically unlock from presence, motion, or bedtime state.

## Pair it with bedtime

The [family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html) should call this check as one part of an intentional Good-night action.

A useful bedtime result is concise:

- "All exterior locks confirmed locked."
- "Back door unlocked."
- "Garage entry lock state unknown."
- "Front door open; lock command not attempted."
- "Side door lock jammed; inspect manually."

Do not bury an unresolved lock inside a broad "bedtime complete" message.

## Advanced features

### Delay by household mode

Use a longer delay while someone is working outside and a shorter delay in Night or Away mode. Keep the trigger based on actual lock state rather than phone location alone.

### Track deliberate temporary access

A visible "Keep patio unlocked for 60 minutes" control is safer than silently disabling alerts. Show the remaining time and restore normal monitoring automatically.

### Escalate only unresolved conditions

If an unlocked incident is not acknowledged after a meaningful interval, notify another responsible adult. Stop escalation as soon as the lock confirms locked.

## Failure modes

- **The door is closed but unlocked:** A contact sensor cannot report lock state. Use actual lock feedback.
- **The bolt jams against the frame:** Report jammed or not confirmed, and ask for inspection.
- **The automation locks an open door:** Require a current closed-door report before any automatic command.
- **A stale locked state looks current:** Add unavailable and last-update checks.
- **Guests are repeatedly locked out:** Use an explicit temporary-unlocked mode and preserve agreed entry methods.
- **The lock battery dies:** Add an earlier battery threshold for locks and keep physical keys accessible.
- **The command is sent but no final state arrives:** Report "lock not confirmed," not success.
- **Bedtime runs while someone is still outside:** Make Good night intentional and show unresolved doors or temporary access before locking.

## FAQ

### Is a closed door the same as a locked door?

No. Use the lock's actual locked, unlocked, jammed, or unknown state. A contact sensor only reports whether the door is open or closed.

### Should the bedtime routine automatically lock every door?

Start with a status check and alert. Add a lock command only after door position, lock feedback, jam handling, battery state, manual keys, and household expectations are tested.

### What should happen when a lock is unavailable?

Report the state as unknown and ask for a manual check. Never treat missing data or an old locked event as confirmation that the door is secure.

## Related recipes

- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Use persistent status tiles](/automation/notifications/status-tiles.html)
- [Get low-battery alerts](/automation/notifications/low-battery-alerts.html)
- [Report a garage door left open](/automation/security/garage-door-notification.html)

<div class="page-navigation">
  <a href="/automation/security/index.html">Back to safety and security automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
