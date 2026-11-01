---
layout: automation
date: 2026-11-01
last_modified_at: 2026-11-01
image: /assets/img/social/recipes/notifications/school-morning-countdown.png
title: School morning countdown on any smart speaker
description: A smart speaker calls out each step of a school morning at set times, so parents stop repeating it. Works with any speaker or platform.
keywords: school morning routine, smart speaker announcement, kids morning countdown, school day reminders
compact: true
tags: [kids, school-morning, reminders, notifications]
faqs:
  - question: Which speakers work?
    answer: Any speaker your platform can make talk. Sonos, Alexa, Google, and Home Assistant setups can all play a spoken message at a set time.
  - question: How do I skip weekends and holidays?
    answer: Limit the schedule to school days. Add a manual "no school" switch for holidays and snow days.
products:
  - job: "Speak the reminders in the room where kids get ready"
    body: "Any smart speaker your platform can send a spoken message to. No new hardware is needed if you already have one."
---

# School morning countdown on any smart speaker

{% include content-hero.html src="/assets/img/social/recipes/notifications/school-morning-countdown.svg" alt="A smart speaker card for a school morning countdown that calls out brush teeth and shoes on time" %}

A smart speaker says each step of the morning at a set time. Brush teeth. Shoes on. Kids hear the cue and move, and parents stop repeating it from the hallway.

**Best for:** Families with a fixed school departure time and a speaker near where kids get ready.

**Not for:** Mornings with no set leaving time.

## Why this exists

In our house, school mornings meant we were the soundtrack. We now let the speaker give the cues instead. We wrote about how that changed our mornings in [It's time to brush teeth](https://www.afterpickup.com/its-time-to-brush-teeth/) on After Pickup.

## What we do

Two announcements, every school day:

- **8:52:** "It's time to brush teeth."
- **8:58:** "It's time to put on shoes."

Same words, same times, every school day. Pick times that fit your own departure.

## Add more steps if you need them

You can add more cues the same way, such as "Grab your backpack" and "Time to leave." We only use the two above, so set the times for any extra steps from your own morning.

## Logic

<div class="automation-example">IF it is a school day
AND the time is the set time for a step
THEN announce that step on the speaker

IF "no school" is on
THEN skip all announcements</div>

- **Trigger:** A set time for each step.
- **Conditions:** It is a school day and "no school" is off.
- **Action:** Speak one short sentence on the speaker.
- **Wait / timeout:** Each step plays once.
- **Stop condition:** None needed. The countdown ends after the last step.
- **Manual override:** A "no school" switch skips the whole morning.

## Setup notes

1. Pick the speaker kids can hear while getting ready.
2. Write each step as one short sentence.
3. Set a time for each step, working back from when you leave.
4. Limit the schedule to school days.
5. Add a "no school" switch for holidays.
6. Test the volume while the house is busy.

## Platform notes

- **Sonos:** Use your hub's text-to-speech command. Some can resume the music after the message. See the [Sonos and Hubitat version](/automation/notifications/school-morning-reminders.html).
- **Alexa:** A routine with a time trigger and an "Alexa says" action.
- **Google:** A household routine with a set time and a spoken message.
- **Home Assistant:** An automation with a time trigger and a text-to-speech action.

## What I used

{% include product-list.html %}

## Failure modes

- **The speaker is too quiet:** Set a fixed volume in the announcement.
- **It plays on a holiday:** Turn on "no school" the night before.
- **Music stops and does not come back:** Not every speaker resumes after a message. Check yours.

## FAQ

### Which speakers work?

Any speaker your platform can make talk. Sonos, Alexa, Google, and Home Assistant setups can all play a spoken message at a set time.

### How do I skip weekends and holidays?

Limit the schedule to school days. Add a manual "no school" switch for holidays and snow days.

## Related recipes

- [All kids and family routines](/articles/smart-home-automations-for-kids.html)
- [Check that kids brushed their teeth at bedtime](/automation/notifications/teeth-brushing-reminder.html)
- [Spoken school morning reminders with Sonos](/automation/notifications/school-morning-reminders.html)
- [Bedtime countdown for kids on any smart speaker](/automation/notifications/bedtime-countdown.html)
- [Smart home morning routine and scenes](/automation/daily-routines/morning-routine.html)
- [Set up a garbage day reminder tile](/automation/notifications/garbage-day-reminder.html)

{% include page-navigation.html
  left_url="/automation/notifications/"
  left_label="Back to notifications"
  right_url="/automation/"
  right_label="View all automations"
%}
