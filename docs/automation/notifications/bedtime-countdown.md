---
layout: automation
date: 2026-11-01
last_modified_at: 2026-11-01
title: Bedtime countdown for kids on any smart speaker
description: A smart speaker calls out each bedtime step at set times, from last call for snacks to brushing teeth. Works with any speaker or platform.
keywords: kids bedtime routine, bedtime countdown, smart speaker announcement, evening reminders
image: /assets/img/social/recipes/notifications/bedtime-countdown.png
compact: true
tags: [kids, bedtime, reminders, notifications]
faqs:
  - question: Which speakers work?
    answer: Any speaker your platform can make talk. Sonos, Alexa, Google, and Home Assistant setups can all play a spoken message at a set time.
  - question: Can I change the times on weekends?
    answer: Yes. Make a second schedule for nights with a later bedtime, or add a "late night" switch that skips the countdown.
products:
  - job: "Speak the reminders where kids can hear them"
    body: "Any smart speaker your platform can send a spoken message to. No new hardware is needed if you already have one."
---

# Bedtime countdown for kids on any smart speaker

{% include content-hero.html src="/assets/img/social/recipes/notifications/bedtime-countdown.svg" alt="A smart speaker card for a kids bedtime countdown from last call for snacks to brushing teeth" %}

A smart speaker says each bedtime step at a set time. Last call for snacks. Time to go upstairs. Pajamas on. Brush teeth. The speaker keeps the pace, so parents do not have to.

**Best for:** Families with a set bedtime and a speaker kids can hear in the evening.

**Not for:** Nights with no fixed bedtime.

## Why this exists

Bedtime has many small steps, and each one can turn into a reminder from a parent. A countdown on the speaker gives every step a clear time. It works the same way as the [school morning countdown](/automation/notifications/school-morning-countdown.html), just in the evening.

## Example steps

Work back from bedtime. Here is one way to space it out:

- **About an hour before bed:** "Last call for snacks."
- **Later:** "Time to go upstairs."
- **Next:** "Put on your pajamas."
- **15 minutes after pajamas:** "Time to brush teeth."

Pick the exact times from your own evening.

## Logic

<div class="automation-example">IF it is a bedtime night
AND the time is the set time for a step
THEN announce that step on the speaker

IF "late night" is on
THEN skip all announcements</div>

- **Trigger:** A set time for each step.
- **Conditions:** It is a normal bedtime night and "late night" is off.
- **Action:** Speak one short sentence on the speaker.
- **Wait / timeout:** Each step plays once.
- **Stop condition:** The countdown ends after the brush teeth step.
- **Manual override:** A "late night" switch skips the whole evening.

## Follow up with a toothbrushing check

The last step asks kids to brush. To know they did, add the [teeth-brushing check](/automation/notifications/teeth-brushing-reminder.html). It watches the toothbrush charger and only reminds again if the brush never went back on to charge.

## Setup notes

1. Pick a speaker kids can hear in the evening.
2. Write each step as one short sentence.
3. Set a time for each step, working back from bedtime.
4. Add a "late night" switch for weekends and special nights.
5. Keep the volume low enough for younger kids who may already be asleep.

## Platform notes

- **Sonos:** Use your hub's text-to-speech command.
- **Alexa:** A routine with a time trigger and an "Alexa says" action.
- **Google:** A household routine with a set time and a spoken message.
- **Home Assistant:** An automation with a time trigger and a text-to-speech action.

## What I used

{% include product-list.html %}

## Failure modes

- **It wakes a sleeping child:** Use a speaker away from bedrooms, or lower the volume for later steps.
- **It plays on a late night:** Turn on "late night" before the first step.
- **Kids tune it out:** Keep the steps short and few.

## FAQ

### Which speakers work?

Any speaker your platform can make talk. Sonos, Alexa, Google, and Home Assistant setups can all play a spoken message at a set time.

### Can I change the times on weekends?

Yes. Make a second schedule for nights with a later bedtime, or add a "late night" switch that skips the countdown.

## Related recipes

- [Check that kids brushed their teeth at bedtime](/automation/notifications/teeth-brushing-reminder.html)
- [School morning countdown on any smart speaker](/automation/notifications/school-morning-countdown.html)
- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Set a nursery quiet mode](/automation/notifications/baby-sleep-mode.html)

{% include page-navigation.html
  left_url="/automation/notifications/"
  left_label="Back to notifications"
  right_url="/automation/"
  right_label="View all automations"
%}
