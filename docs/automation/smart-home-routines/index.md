---
layout: default
title: "Smart home routines: morning, overnight, and away"
description: Smart home routine ideas for mornings, overnight, leaving, arriving, and guests. Each one links a plain-English recipe with switches that still work.
permalink: /automation/smart-home-routines/
canonical_url: https://www.homeautomationcookbook.com/automation/smart-home-routines/
last_modified_at: 2026-10-27
keywords: smart home routines, home automation routines, overnight automation, morning routine automation, away mode
---

# Smart home routines

A smart home routine is a small set of actions the house runs for you at a certain moment. That moment might be waking up, going to bed, or leaving the house. Good routines are easy to see and easy to undo. The wall switches keep working, and nobody gets surprised.

Pick one moment of the day below. Start with a single recipe, live with it for a week, and then add the next.

{% assign groups = "" | split: "" %}
{% capture routine_sections %}
morning|Morning routines|Ease into the day. Bring up light slowly and get gentle reminders, while people who are still asleep stay undisturbed.|/automation/daily-routines/morning-routine.html,/automation/lighting/wake-up-lights.html,/automation/appliances/coffee-maker-morning.html,/automation/notifications/school-morning-reminders.html,/automation/climate/blinds-sunset-sunrise.html
overnight|Bedtime and overnight automation|Wind the house down and keep it calm overnight. Check doors and the garage, and light the way to the bathroom without waking everyone.|/automation/daily-routines/bedtime-routine.html,/automation/security/door-unlocked-bedtime-check.html,/automation/security/garage-door-notification.html,/automation/lighting/bathroom-night-light.html,/automation/daily-routines/wall-tablet-modes.html
away|Away routines|Leave without a checklist. Switch to Away once the house is empty, make it look lived in, and keep the temperature safe.|/automation/daily-routines/away-mode.html,/automation/security/away-lights.html,/automation/security/fake-dog-deterrent.html,/automation/climate/safe-thermostat-away.html
arriving|Arriving home|Come home to a lit path and normal comfort settings.|/automation/daily-routines/unlock-door-arrival.html,/automation/lighting/driveway-welcome-wave.html,/automation/entertainment/welcome-home-music.html
guests|Guests and visitors|Keep the house simple for people who do not live there.|/automation/daily-routines/guest-mode.html
{% endcapture %}
{% assign section_lines = routine_sections | strip | newline_to_br | split: "<br />" %}
{% for line in section_lines %}
{% assign parts = line | strip | split: "|" %}
<h2 id="{{ parts[0] }}">{{ parts[1] }}</h2>

<p>{{ parts[2] }}</p>

<div class="card-grid">
{% assign urls = parts[3] | split: "," %}
{% for u in urls %}
{% assign recipe = site.pages | where: "url", u | first %}
{% if recipe %}
{% include automation-card.html url=recipe.url title=recipe.title description=recipe.description %}
{% endif %}
{% endfor %}
</div>
{% endfor %}

## Tips for routines that last

- Start each routine from something you can see, such as a button or a set time.
- Keep a manual way to do every step, like the wall switch.
- Treat a sensor that stops reporting as unknown, not as safe or empty.
- Make it easy to cancel or undo a routine when plans change.

Want the full list? Browse all [daily routine recipes](/automation/daily-routines/) or search every [automation recipe](/automation/).
