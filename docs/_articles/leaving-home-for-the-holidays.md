---
layout: guide
title: Leaving home for the holidays
description: A smart home checklist for a holiday trip. Set away mode, lights, heat, leak alerts, and locks, then test them before you go.
date: 2026-10-26
last_modified_at: 2026-10-26
image: /assets/img/social/guides/leaving-home-for-the-holidays.png
---

# Leaving home for the holidays

{% include content-hero.html src="/assets/img/social/guides/leaving-home-for-the-holidays.svg" alt="A checklist for leaving the smart home ready before a holiday trip" %}

A holiday trip is the longest stretch most homes sit empty all year. The automations you lean on every day now run with nobody there to notice a mistake. A few minutes of checking before you leave is worth it.

This checklist ties together the recipes I care about most when the house is empty. Work through it a day or two before the trip, not in the driveway.

## The short checklist

| Check | Why it matters | Recipe |
|---|---|---|
| Away mode turns on and off | Most of the other rules depend on it | [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html) |
| A few lights run in the evening | A dark house every night is a visible pattern | [Turn on away lights to look occupied](/automation/security/away-lights.html) |
| Heat stays at a safe floor | Frozen pipes are worse than a small energy bill | [Safe thermostat auto-away](/automation/climate/safe-thermostat-away.html) |
| Leak alerts reach your phone | Water damage grows while nobody is home | [Water leak detection alerts](/automation/security/water-leak-response.html) |
| Doors are locked | One unlocked door undoes the rest | [Alert when a door is left unlocked](/automation/security/door-unlocked-bedtime-check.html) |
| Smoke alarms still do their job | Nobody is there to hear them | [Supplemental fire evacuation support](/automation/security/fire-safety.html) |

## Start with away mode

Away mode is the switch that the other recipes watch. If it does not turn on, the away lights stay dark and the thermostat keeps heating an empty house as if you were there.

Test it the way you will actually leave. Take the whole household out the door with phones, or set it by hand if you plan to. Then check that it turned on. Check the return too. A house stuck in away mode after you get home is a common surprise.

If your arrive and leave triggers have been unreliable, set away mode by hand for this trip. [Why arrive and leave triggers fail](/articles/why-arrive-leave-triggers-fail.html) explains the usual causes.

## Make the house look lived in

Pick two or three lights a person would really use in the evening. A living room lamp and one bedroom light are enough. Stagger them a little and turn them off at a normal bedtime.

[Turn on away lights to look occupied](/automation/security/away-lights.html) has the full logic. Run it once with away mode on by hand before you leave. That way you see it work instead of hoping it will.

## Keep the heat at a safe floor

An away setback saves energy. It should not drop the house so low that pipes are at risk in a cold snap. Pick a floor for heating and a ceiling for cooling, and let the thermostat hold those while you are gone.

[Safe thermostat auto-away](/automation/climate/safe-thermostat-away.html) covers the limits and what to do when a sensor stops reporting. If you leave a space heater plugged in, unplug it. Do not leave it for an automation to manage while nobody is home.

## Check the leak sensors

Put a damp paper towel under each leak sensor, or follow the test the maker suggests. Make sure the alert reaches every phone that should get it, including people who are traveling with you.

If you have a shutoff valve, confirm the leak sensor closes it. Know who can get into the house if something does go wrong. [Water leak detection alerts](/automation/security/water-leak-response.html) has the setup.

Replace weak batteries before you go. [Smart home low-battery alerts](/automation/notifications/low-battery-alerts.html) can tell you which ones are close.

## Lock up and confirm it

Walk the house and lock every door. Then check that your lock status matches what you see. A lock that reports locked while the bolt is not thrown is worth finding now.

[Alert when a door is left unlocked](/automation/security/door-unlocked-bedtime-check.html) is built for bedtime. It works just as well as a check that runs when away mode turns on. If a house sitter or neighbor will visit, give them their own code instead of sharing yours.

## Fire safety while you are gone

Automations are a supplement to listed smoke alarms, not a replacement. Test the alarms the way the maker says. Make sure any smoke alert you rely on goes to your phone and to someone nearby who can check the house.

[Supplemental fire evacuation support](/automation/security/fire-safety.html) covers how the lights and alerts can help. It does not replace a monitored alarm or a call to emergency services.

## Before you walk out the door

- Turn on away mode, or confirm it turned on by itself.
- Look at a single status view, such as [a house status check on demand](/automation/notifications/house-status-on-demand.html).
- Make sure your hub, router, and any bridges are on power you trust. A hub that runs locally keeps the core rules working if the internet drops while you are away.
- Tell one nearby person how to reach you and how to get in.

## Failure modes

- **Away mode never turned on:** Nothing else ran as planned. Set it by hand for a long trip and check it from your phone.
- **The away lights ran every night at the same minute:** Add a small stagger or rotate rooms.
- **The thermostat dropped too low:** The setback ignored the safe floor. Fix the limit before the next cold night.
- **A leak alert went to one phone that was off:** Send it to more than one person.
- **The house stayed in away mode after you got home:** Test the return path, not just the leave path.

## FAQ

### Do I need all of these recipes before a trip?

No. Start with away mode, safe heat, and leak alerts. Those protect the house. Away lights and lock checks are the next layer.

### Should I rely on my phone's location to set away mode for a long trip?

You can, but set it by hand if your arrive and leave triggers have been flaky. A wrong state for a week is worse than a wrong state for an evening.

### What if the internet goes down while I am away?

A hub that runs rules locally keeps the core automations working. You may not get alerts until the connection returns, so a nearby person who can check the house still matters.

## Related guides and recipes

- [Set away mode when everyone leaves](/automation/daily-routines/away-mode.html)
- [Turn on away lights to look occupied](/automation/security/away-lights.html)
- [Safe thermostat auto-away](/automation/climate/safe-thermostat-away.html)
- [Water leak detection alerts](/automation/security/water-leak-response.html)
- [Alert when a door is left unlocked](/automation/security/door-unlocked-bedtime-check.html)
- [Supplemental fire evacuation support](/automation/security/fire-safety.html)
- [Why arrive and leave triggers fail](/articles/why-arrive-leave-triggers-fail.html)
