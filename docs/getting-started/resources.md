---
layout: guide
title: Home automation resources
description: A short list of official documentation, support communities, and research checks for verifying devices and platform behavior.
last_modified_at: 2026-08-30
---

# Home automation resources

Use official documentation for current requirements, then use community discussions to find edge cases. A forum post or video can reveal a problem, but it does not replace the current manual or compatibility list for the exact model.

## Official platform documentation

- [Home Assistant documentation](https://www.home-assistant.io/docs/) - Current installation, integration, automation, backup, and maintenance documentation. I have not personally run Home Assistant.
- [Hubitat documentation](https://docs2.hubitat.com/) - Hub setup, built-in apps, device support, and administration for the platform I currently use.
- [SmartThings support](https://support.smartthings.com/) - Current consumer setup and troubleshooting information for a platform I previously used.
- Use the Alexa app and Amazon's current help pages for the exact Echo, routine, and connected-device behavior you need. I have used Alexa for beginner-friendly voice control and simple routines.

## Support communities

- [Hubitat Community](https://community.hubitat.com/) - Product announcements, device discussions, custom apps and drivers, and troubleshooting.
- [SmartThings Community](https://community.smartthings.com/) - Device integration and automation discussions.
- [Home Assistant Community](https://community.home-assistant.io/) - Installation, integration, dashboard, and automation discussions.
- [r/homeautomation](https://www.reddit.com/r/homeautomation/) - Broad discussion across platforms. Verify advice against product documentation before acting on it.

Community code and instructions can become stale. Check the date, platform version, exact device model, comments reporting breakage, and whether the proposed behavior affects safety or security.

## Research a device before buying

1. Write the job, trigger, required states, action, and manual override.
2. Find the exact model and hardware revision in the platform's current compatibility information.
3. Read the manufacturer's manual, especially power, load, placement, reset, and safety instructions.
4. Search the platform community for the exact model number, not just the brand.
5. Look for long-term reports about disconnects, battery life, firmware, and unavailable states.
6. Understand the return policy.
7. Buy one and test it in the real location before ordering more.

## Evaluate community advice

Ask:

- Does the writer clearly say what they personally tested?
- Is the advice for the same country, voltage, radio frequency, model, and firmware?
- Does it preserve normal physical control?
- Does it explain internet, hub, and sensor failure?
- Does it use one weak signal to infer identity, occupancy, permission, or safety?
- Does it bypass manufacturer instructions, listings, interlocks, or entrapment protection?

If the last two answers are yes, do not copy the automation.

## This site's source and corrections

Home Automation Cookbook is open source:

- [View the repository](https://github.com/madskristensen/HomeAutomationCookbook)
- [Ask a question or share an idea](https://github.com/madskristensen/HomeAutomationCookbook/discussions)
- [Report a problem](https://github.com/madskristensen/HomeAutomationCookbook/issues/new?template=report-issue.md)
- [Suggest an automation](https://github.com/madskristensen/HomeAutomationCookbook/issues/new?template=suggest-automation.md)

## Next steps

- [Choose a platform](/getting-started/choose-the-right-platform.html)
- [Choose devices by job](/getting-started/device-guide.html)
- [See products I have used](/gear.html)
- [Read the disclosure](/disclosure.html)

<div class="page-navigation">
  <a href="/getting-started/index.html">Back to getting started</a>
  <a href="/">Back to home</a>
</div>
