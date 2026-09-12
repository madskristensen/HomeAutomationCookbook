---
layout: guide
title: Hubitat home automation guide
description: Use Hubitat built-in apps and local rules for reliable household automation while keeping physical controls and understandable overrides.
last_modified_at: 2026-09-12
---

# Hubitat home automation guide

Hubitat is my current platform because it provides approachable daily management while leaving room for detailed rules, custom apps, drivers, and code. The useful balance is not maximum complexity. It is having enough control to make routines dependable without turning every adjustment into a software project.

**Best for:** Local rules with compatible devices, built-in Zigbee and Z-Wave radios, detailed automation logic, and people comfortable understanding triggers and state.

**Not for:** Households that want every integration configured automatically, rules that only one expert can understand, or assuming every external integration becomes local simply because Hubitat runs locally.

## My experience boundary

I currently use Hubitat and prefer it over the platforms I used previously. This guide reflects firsthand operation plus current Hubitat documentation. Exact hub model, firmware, screenshots, and per-recipe test records will only be added when they are captured and verified.

## Where Hubitat fits

Hubitat offers several automation tools rather than requiring every job to use the most advanced rule builder:

- Use a purpose-built app when it matches the job.
- Use Basic Rules for a clear event-and-action path.
- Use Rule Machine when the automation genuinely needs conditions, branches, waits, or remembered state.
- Use modes and virtual switches to make shared household state visible.

The simplest tool that expresses the complete safe behavior is usually the easiest to maintain.

## Automation building blocks

- [Room Lighting](https://docs2.hubitat.com/en/apps/room-lighting) covers motion and contact activation, delayed turn-off, conditions, and overrides.
- [Basic Rules](https://docs2.hubitat.com/en/apps/basic-rules) provides a direct when-this-happens, do-that model with common sensors, restrictions, waits, and notifications.
- [Rule Machine](https://docs2.hubitat.com/en/apps/rule-machine/rule-5-1) handles required expressions, conditional actions, delays, waits, and stateful logic.
- [Mode Manager](https://docs2.hubitat.com/en/apps/mode-manager) changes household modes from schedules or presence.
- The [Notifications app](https://docs2.hubitat.com/en/apps/notifications) can alert when a condition remains true, with limits and restrictions.

Choose the app by the household job rather than by which tool has the most options.

## How the recipes map to Hubitat

| Household job | Hubitat starting point | Why |
|---|---|---|
| [Motion-triggered lights](/automation/lighting/lights-on-motion.html) | Room Lighting | Purpose-built activation, delayed off, conditions, and override handling. |
| [Door-triggered closet lights](/automation/lighting/toggle-lights-door.html) | Room Lighting or Basic Rules | Contact activation is simple, while Room Lighting helps with off behavior. |
| [Washer completion alert](/automation/appliances/washer-done-notification.html) | Rule Machine | Completion inferred from running then idle needs remembered state and delays. |
| [Garage left-open alert](/automation/security/garage-door-notification.html) | Basic Rules or Notifications | Alert only after the open condition remains true. |
| [Bathroom fan after a shower](/automation/climate/fan-shower.html) | Basic Rules or Rule Machine | Separate humidity thresholds are simple; rapid-rise inference needs deeper logic. |
| [Away and arrival routines](/automation/daily-routines/away-mode.html) | Mode Manager plus focused rules | Shared mode can coordinate independent lighting, climate, and notification behavior. |

## Build and verify one rule

1. Confirm the exact device driver exposes the state and command needed.
2. Choose the simplest built-in app that expresses the whole job.
3. Name the automation after the household outcome.
4. Add a physical or virtual override before enabling broad actions.
5. Observe device events before adding conditions.
6. Test hub restart, device unavailability, low battery, and manual control.
7. Disconnect the internet to separate local automation from cloud notifications or integrations.
8. Document complex Rule Machine logic so another person can understand why it acted.

## Local and cloud behavior

Hubitat automation apps run on the hub, but that does not make every external service local. A cloud integration, voice assistant, mobile push service, or internet API can still fail independently. Keep core room behavior on compatible local devices where practical, and test notification delivery separately from the rule itself.

## Failure modes

- **A rule is technically correct but hard to maintain:** Replace it with a purpose-built app or split it into smaller household outcomes.
- **A device is paired but state is missing:** Verify the driver and the attributes it exposes.
- **A manual change is reversed:** Add an explicit override or use Room Lighting's override-oriented behavior.
- **Away mode acts on incomplete presence:** Require every tracked resident to leave, add delay, and retain a visible Guest mode.
- **The hub runs the rule but no phone alert arrives:** Treat local rule execution and external notification delivery as separate paths.

## Done when

- The rule continues for compatible devices when the internet is disconnected.
- Physical switches and essential controls remain usable.
- Another household member can see and use the override.
- The selected app is no more complex than the job requires.
- Restart and unavailable-device behavior are known.
- Complex rules have names and notes that explain their purpose.

## FAQ

### Should I use Basic Rules or Rule Machine?

Start with Basic Rules when one event leads to a straightforward action. Use Rule Machine when the job needs remembered state, conditional branches, repeated checks, or more detailed timing.

### Is every Hubitat automation local?

Hubitat apps run on the hub, but cloud integrations and external notification services still depend on their own network paths.

### Why use Room Lighting instead of a custom rule?

Room Lighting already models common lighting activation, delayed off, restrictions, and overrides. Reusing that behavior is usually easier to maintain than rebuilding it from individual actions.

## Related guides

- [Compare home automation platforms](/getting-started/choose-the-right-platform.html)
- [Amazon Alexa home automation guide](/platforms/alexa.html)
- [SmartThings home automation guide](/platforms/smartthings.html)
- [Home Assistant technical-fit guide](/platforms/home-assistant.html)
- [Browse platform-neutral recipes](/automation/index.html)
