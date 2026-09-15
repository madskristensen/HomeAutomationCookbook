---
layout: guide
title: Hubitat home automation guide
description: Use Hubitat built-in apps and local rules for reliable household automation while keeping physical controls and understandable overrides.
last_modified_at: 2026-09-14
image: /assets/img/social/platform-hubitat.png
---

# Hubitat home automation guide

<figure class="content-hero">
  <img src="/assets/img/social/platform-hubitat.svg" alt="A small Hubitat hub connects local devices with conditional automation logic" width="1200" height="630">
</figure>

Hubitat is my current platform because it is fast, compact, and managed while still leaving room for detailed rules, community drivers, custom drivers, and code. It gives me enough control to make routines dependable without turning every daily adjustment into a software project.

**Best for:** Local rules with compatible devices, built-in Zigbee and Z-Wave radios, detailed automation logic, and people comfortable understanding triggers and state.

**Not for:** Households that want every integration configured automatically, rules that only one expert can understand, or assuming every external integration becomes local simply because Hubitat runs locally.

## My experience boundary

I moved to Hubitat during a whole-house remodel, when I could rebuild the automation system from scratch instead of migrating it piecemeal. It has been an excellent fit for my needs: fast in daily use, supported by a large community-driver ecosystem, and open enough for me to write a driver when an unusual device needs one.

AI coding tools have made writing my own Hubitat drivers easier, but generated code still needs the same review, device testing, failure handling, and maintenance as any other integration. In a few cases I have been able to create the Hubitat support I needed even when I could not find an existing implementation elsewhere.

For rules, webCoRE is my preferred engine. It can express the conditional and stateful scenarios that I could not comfortably build on earlier platforms. I also use SharpTools.io dashboards on several wall-mounted tablets, just as I did with SmartThings, so useful controls and status remain visible around the house.

This guide reflects firsthand operation plus current Hubitat documentation. Exact hub model, firmware, screenshots, and per-recipe test records will only be added when they are captured and verified.

## Where Hubitat fits

Hubitat offers several automation tools rather than requiring every job to use the most advanced rule builder:

- Use a purpose-built app when it matches the job.
- Use Basic Rules for a clear event-and-action path.
- Use Rule Machine when the automation genuinely needs conditions, branches, waits, or remembered state.
- Use webCoRE when its piston model is the clearest way to express and maintain a more involved rule.
- Use modes and virtual switches to make shared household state visible.

The simplest tool that expresses the complete safe behavior is usually the easiest to maintain.

## Automation building blocks

- [Room Lighting](https://docs2.hubitat.com/en/apps/room-lighting) covers motion and contact activation, delayed turn-off, conditions, and overrides.
- [Basic Rules](https://docs2.hubitat.com/en/apps/basic-rules) provides a direct when-this-happens, do-that model with common sensors, restrictions, waits, and notifications.
- [Rule Machine](https://docs2.hubitat.com/en/apps/rule-machine/rule-5-1) handles required expressions, conditional actions, delays, waits, and stateful logic.
- [Mode Manager](https://docs2.hubitat.com/en/apps/mode-manager) changes household modes from schedules or presence.
- The [Notifications app](https://docs2.hubitat.com/en/apps/notifications) can alert when a condition remains true, with limits and restrictions.

Choose the app by the household job rather than by which tool has the most options. Although webCoRE is my preference for advanced rules, I still use a simpler built-in app when it expresses the complete behavior more clearly.

## How the recipes map to Hubitat

| Household job | Hubitat starting point | Why |
|---|---|---|
| [Motion-triggered lights](/automation/lighting/lights-on-motion.html) | Room Lighting | Purpose-built activation, delayed off, conditions, and override handling. |
| [Door-triggered closet lights](/automation/lighting/toggle-lights-door.html) | Room Lighting or Basic Rules | Contact activation is simple, while Room Lighting helps with off behavior. |
| [Washer completion alert](/automation/appliances/washer-done-notification.html) | webCoRE or Rule Machine | Completion inferred from running then idle needs remembered state and delays. |
| [Garage left-open alert](/automation/security/garage-door-notification.html) | Basic Rules or Notifications | Alert only after the open condition remains true. |
| [Bathroom fan after a shower](/automation/climate/fan-shower.html) | Basic Rules, webCoRE, or Rule Machine | Separate humidity thresholds are simple; rapid-rise inference needs deeper logic. |
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

The same documentation rule applies to webCoRE pistons and custom drivers. Advanced capability is useful only when I can still understand and repair it later.

## Local and cloud behavior

Hubitat automation apps run on the hub, but that does not make every external service local. A cloud integration, voice assistant, mobile push service, or internet API can still fail independently. Keep core room behavior on compatible local devices where practical, and test notification delivery separately from the rule itself.

## Failure modes

- **A rule is technically correct but hard to maintain:** Replace it with a purpose-built app or split it into smaller household outcomes.
- **A device is paired but state is missing:** Verify the driver and the attributes it exposes.
- **A manual change is reversed:** Add an explicit override or use Room Lighting's override-oriented behavior.
- **Away mode acts on incomplete presence:** Require every tracked resident to leave, add delay, and retain a visible Guest mode.
- **The hub runs the rule but no phone alert arrives:** Treat local rule execution and external notification delivery as separate paths.

## FAQ

### Should I use Basic Rules or Rule Machine?

Start with Basic Rules when one event leads to a straightforward action. Use Rule Machine when the job needs remembered state, conditional branches, repeated checks, or more detailed timing.

### Is every Hubitat automation local?

Hubitat apps run on the hub, but cloud integrations and external notification services still depend on their own network paths.

### Why use Room Lighting instead of a custom rule?

Room Lighting already models common lighting activation, delayed off, restrictions, and overrides. Reusing that behavior is usually easier to maintain than rebuilding it from individual actions.

### Why is Hubitat my current preference?

It checks the combination I care about: fast local behavior for compatible devices, a small managed hub, broad community-driver support, and enough openness to write my own drivers and advanced webCoRE rules. It lets me go deep when necessary without making routine household management feel like maintaining a server.

### Can I use SharpTools with Hubitat?

I use SharpTools.io with Hubitat to display controls and status on wall-mounted tablets around my house. The dashboards support visibility and convenient control, while physical switches remain the ordinary way to operate each room.

## Related guides

- [Hubitat vs SmartThings for a family house](/articles/hubitat-vs-smartthings-family-house.html)
- [Compare home automation platforms](/getting-started/choose-the-right-platform.html)
- [Amazon Alexa home automation guide](/platforms/alexa.html)
- [SmartThings home automation guide](/platforms/smartthings.html)
- [Home Assistant technical-fit guide](/platforms/home-assistant.html)
- [Browse platform-neutral recipes](/automation/index.html)
