---
layout: automation
title: Get an immediate alert when water is detected
description: A platform-neutral leak recipe that identifies the wet sensor, alerts the household immediately, and adds automatic water shutoff only after verified testing.
keywords: water leak alert, leak sensor notification, water detection automation, smart water shutoff, flood sensor, NEO water leak sensor
last_modified_at: 2026-08-30
faqs:
  - question: Should one leak sensor automatically close the main water valve?
    answer: Start with immediate alerts. Add automatic shutoff only after the valve, manual bypass, sensor behavior, and safe reopen procedure have all been tested with the household.
  - question: Does a dry sensor mean the leak is resolved?
    answer: No. A dry report can mean water moved away from the contacts or the sensor was picked up. Require a person to inspect the area and clear the alert manually.
  - question: Where should leak sensors go first?
    answer: Start where a hidden or pressurized leak would cause damage quickly, such as the water heater, washing-machine supply hoses, under sinks, and near a dishwasher or refrigerator water line.
---

# Get an immediate alert when water is detected

Put a name on the exact sensor, alert the household at any hour, and require a person to inspect the source before clearing the incident.

**Best for:** Water heaters, washing-machine hoses, sinks, dishwashers, refrigerator water lines, sump areas, and other places where water would collect near a sensor.

**Not for:** Replacing smoke, carbon-monoxide, sump, or professionally monitored safety systems, or automatically operating an untested main-water valve.

## Why this exists

A generic "water detected" message wastes time. The useful alert says where water was found, reaches more than one responsible person, stays visible until acknowledged, and still leaves a clear manual response when the hub or internet is unavailable.

Automatic shutoff can reduce damage, but a valve that cannot reopen, closes on a false report, or has no manual bypass creates a different emergency. Build and test the alert first.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect water | [THIRDREALITY WL2 Zigbee water leak sensor](https://www.amazon.com/dp/B0GK19F6Z2) | [NEO Z-Wave Plus 700 water leak sensor](https://www.amazon.com/dp/B0FSKFCKTB) | Name every sensor for the place a person should inspect. |
| Stop incoming water | Manual main-water shutoff | No personally verified automatic shutoff valve yet | Everyone responsible for the home should know the manual valve location. |
| Reach the household | Persistent phone notification to at least two adults | No personally verified backup alert path yet | A local audible alert is useful when phones are muted or away. |

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. I have used both leak sensors. No automatic shutoff product is recommended until I have verified one in this home.

## Logic

- **Trigger:** Any leak sensor reports wet.
- **Conditions:** None for the first alert. Leak alerts run in Home, Away, Night, and guest modes.
- **Action:** Send a persistent high-priority notification naming the sensor and location, alert at least two responsible people, and turn on a local indicator if it is safe and useful.
- **Wait / timeout:** Repeat through a separate backup path only while the incident remains unacknowledged.
- **Stop condition:** A person inspects the source, stops the water if necessary, and manually clears the incident.
- **Manual override:** The main water supply and any automatic valve remain manually operable.

<div class="automation-example">IF any leak sensor reports wet
THEN create a persistent incident with the sensor's location
AND alert the responsible household members
AND activate the local warning

IF a verified automatic shutoff is enabled
AND the wet report passes its tested confirmation rule
THEN close the main-water valve
AND report whether the valve actually reached closed</div>

## Setup notes

1. Name each sensor for the response location, such as "Laundry supply hoses" instead of "Leak sensor 3."
2. Place the contacts where the first escaping water is likely to collect, without blocking drains or creating a trip hazard.
3. Confirm wet, dry, unavailable, low-battery, and tamper states before writing the response.
4. Send the first alert without time, presence, or mode conditions.
5. Include the sensor name, location, detection time, manual shutoff location, and acknowledgment action.
6. Deliver the alert to at least two responsible people.
7. Test a local audible or visible warning that does not depend on a phone.
8. Require manual incident clearing even after the sensor reports dry.

## Test the alert safely

Follow the sensor's instructions for testing. Use a damp test surface or cloth on the sensing contacts rather than immersing a device unless its documentation explicitly permits that.

Run the test with:

- Every phone locked and muted as it would normally be overnight.
- Home and Away modes active in separate tests.
- The internet disconnected if local alert behavior is expected.
- The sensor marked unavailable to verify that missing data does not look dry.
- A household member following the message to the correct shutoff.

Retest after moving a sensor, changing its battery, changing notification settings, or editing the automation.

## Optional automatic shutoff

Do not add valve control until alert-only behavior is dependable. Before enabling automatic closure:

- Have the valve installed in a manner appropriate for the plumbing and local requirements.
- Verify it can close the actual valve fully and report the final position.
- Label and test the manual bypass.
- Decide which sensors may close the main supply and which should only alert.
- Use a short, tested confirmation rule without delaying the first notification.
- Notify on the close command, successful closure, failure, and unexpected reopening.
- Require a person to inspect the home before reopening.
- Keep freeze protection, fire-suppression supply, boilers, irrigation, and other water-dependent systems in the safety review.

Do not automatically turn off a water heater or other appliance unless its manufacturer instructions and a qualified professional support that exact response.

## Advanced features

### Add a sensing cable

A remote probe or sensing cable can cover a wider edge behind an appliance or around a tank. Test every section that must detect water and keep the control body above the likely water line.

### Escalate only when nobody acknowledges

Send the immediate alert to the primary household group. If nobody acknowledges it, use one independent backup route to a trusted person. Avoid endless repeated notifications that hide new information.

### Track sensor health

Treat low battery, unavailable, and stale reports as maintenance problems. A silent sensor must not appear healthy just because it is not reporting wet.

## Failure modes

- **Alert does not identify the source:** Rename the sensor for a physical location and include that name in every message.
- **Only one person receives the alert:** Add a second responsible recipient and test both locked phones.
- **Sensor reports dry after being moved:** Keep the incident open until a person inspects and clears it.
- **Condensation causes nuisance alerts:** Move the sensor without moving it away from the first likely leak path, or use a remote probe suited to the location.
- **Water misses the contacts:** Observe drainage paths and use a tray, probe, or sensing cable where appropriate.
- **Sensor becomes unavailable:** Create a separate health alert and inspect the device promptly.
- **Automatic valve does not close:** Report the failure clearly and direct the household to the labeled manual shutoff.
- **Automatic valve closes unexpectedly:** Keep manual bypass instructions at the valve and disable automation until the cause is understood.

## Done when

- [ ] Every sensor has a response-oriented location name.
- [ ] A wet test creates one immediate persistent incident in every household mode.
- [ ] At least two responsible people receive an alert naming the correct location.
- [ ] The local warning works without relying on a phone.
- [ ] Dry or unavailable never clears the incident automatically.
- [ ] A person can find and operate the manual shutoff from the alert instructions.
- [ ] If automatic shutoff is enabled, closure, failure, bypass, and manual reopen have all been tested.
- [ ] The system remains useful when the internet is unavailable.

## FAQ

### Should one leak sensor automatically close the main water valve?

Start with immediate alerts. Add automatic shutoff only after the valve, manual bypass, sensor behavior, and safe reopen procedure have all been tested with the household.

### Does a dry sensor mean the leak is resolved?

No. A dry report can mean water moved away from the contacts or the sensor was picked up. Require a person to inspect the area and clear the alert manually.

### Where should leak sensors go first?

Start where a hidden or pressurized leak would cause damage quickly, such as the water heater, washing-machine supply hoses, under sinks, and near a dishwasher or refrigerator water line.

## Related recipes

- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html)
- [Low-battery alerts](/automation/notifications/low-battery-alerts.html)
- [Safety and security automations](/automation/security/index.html)

<div class="page-navigation">
  <a href="/automation/security/index.html">Back to safety and security automations</a>
  <a href="/automation/index.html">View all automations</a>
</div>
