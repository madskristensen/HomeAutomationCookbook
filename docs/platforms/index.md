---
layout: default
title: Home automation platform guides
description: Compare Alexa, SmartThings, Hubitat, and Home Assistant by maintenance burden, automation depth, local behavior, and household control.
permalink: /platforms/index.html
canonical_url: https://www.homeautomationcookbook.com/platforms/index.html
image: /assets/img/social/platforms-overview.png
---

# Home automation platform guides

{% include content-hero.html src="/assets/img/social/platforms-overview.svg" alt="Choose a home automation platform you will be comfortable maintaining" %}

Choose a platform by how comfortably you can build, test, and maintain useful household routines. The best platform is not the one with the longest feature list. It is the one that removes repeated work without making normal lights, climate controls, or family routines harder to understand.

The core [automation recipes](/automation/index.html) remain platform-neutral. These guides explain how each platform approaches the same triggers, conditions, actions, delays, overrides, and failure behavior.

## Choose by the experience you want

<div class="category-grid">

{% include category-card.html
  url="/platforms/alexa.html"
  title="Amazon Alexa"
  description="Voice control and approachable routines when compatible devices expose the required triggers and actions."
%}

{% include category-card.html
  url="/platforms/smartthings.html"
  title="SmartThings"
  description="Approachable routines with a path to more detailed rules and broader device state."
%}

{% include category-card.html
  url="/platforms/hubitat.html"
  title="Hubitat"
  description="A managed local hub with built-in automation apps and deeper rule tools when needed."
%}

{% include category-card.html
  url="/platforms/home-assistant.html"
  title="Home Assistant"
  description="A technical-fit guide for people who want to own more of the hardware, integrations, dashboards, and maintenance."
%}

</div>
## How experience is labeled

- **Personally used:** I have operated the platform in my own home.
- **Current platform:** The platform I presently depend on and maintain.
- **Technical-fit comparison:** A comparison based on architecture and official documentation rather than my own daily operation.

I have personally used Alexa, SmartThings, and Hubitat. Hubitat is my current platform. I have not personally operated Home Assistant, so its guide does not present technical fit as firsthand experience.

## Start with the household job

Do not begin by moving every device or recreating every old rule. Pick one reversible job:

1. [Turn lights on automatically with motion](/automation/lighting/lights-on-motion.html).
2. [Get notified when a garage door stays open](/automation/security/garage-door-notification.html).
3. [Run a bathroom fan after a shower](/automation/climate/fan-shower.html).
4. [Set Away mode only after everyone leaves](/automation/daily-routines/away-mode.html).

Build the smallest useful rule, observe it during normal household use, and then decide whether the platform remains understandable enough to expand.

## Compare before committing

Use the [platform chooser](/getting-started/choose-the-right-platform.html) for a side-by-side decision. Each detailed guide then covers:

- Best fit and poor fit.
- My experience boundary.
- Automation building blocks.
- How existing recipes map to the platform.
- Local and cloud considerations.
- Manual control and household overrides.
- Failure modes.
- A practical finish line.

{% include page-navigation.html
  left_url="/getting-started/choose-the-right-platform.html"
  left_label="Compare platforms"
  right_url="/automation/index.html"
  right_label="Browse automation recipes"
%}
