---
layout: automation
date: 2026-10-25
title: Spoken school morning reminders
description: On school days, a kitchen speaker announces when it is time to brush teeth and put on shoes, then goes back to the music that was playing.
keywords: school morning reminder, spoken reminder Sonos, kids morning routine automation, Sonos text to speech Hubitat, webCoRE school reminder
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/notifications/school-morning-reminders.png
compact: true
faqs:
  - question: Why a spoken reminder instead of a phone notification?
    answer: Kids in the kitchen do not see a parent's phone. A voice from the speaker reaches everyone in the room at once.
  - question: What happens to the music that was playing?
    answer: The announcement uses a high-priority text-to-speech command that briefly interrupts the speaker, then resumes what was playing.
  - question: Does this run on holidays and vacations?
    answer: It only runs on weekdays when the home is in Home mode. On school holidays, you either accept it or add a virtual switch that turns it off.
products:
  - job: "Speak the reminder"
    body: "A Sonos speaker in the kitchen. On Hubitat, I use the community [Sonos Advanced Controller](https://community.hubitat.com/t/release-sonos-advanced-controller/130296), which adds the high-priority text-to-speech command."
---

# Spoken school morning reminders

{% include content-hero.html src="/assets/img/social/recipes/notifications/school-morning-reminders.svg" alt="A kitchen speaker reminds the family when it is time to get ready for school" %}

School mornings run on a clock. This recipe has the kitchen speaker call out two reminders at fixed times on school days: one to brush teeth and one to put on shoes. If music is playing, it gets interrupted for the announcement and then picks back up.

**Best for:** A family with a fixed school departure time and a speaker in the room where everyone gathers in the morning.

**Not for:** Mornings with no fixed schedule, or a house where nobody wants a speaker talking at them.

## Why this exists

The same two reminders get shouted across the house every school morning. A speaker is calmer than a parent on the fifth reminder, and it never forgets the time.

## Logic

<div class="automation-example">IF it is 8:52 AM
AND today is a weekday
AND the home mode is Home
THEN announce "It's time to brush them teeth" on the kitchen speaker at volume 30

IF it is 8:57 AM
AND today is a weekday
AND the home mode is Home
THEN announce "It's time to put on your shoes" on the kitchen speaker at volume 30</div>

- **Trigger:** Two fixed times in the morning.
- **Conditions:** Monday through Friday, and the home mode is Home.
- **Action:** A spoken announcement at a fixed volume that interrupts and then resumes music.
- **Wait / timeout:** None.
- **Stop condition:** Each reminder plays once.
- **Manual override:** Switch the home to a different mode, or pause the rule, on days without school.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Pick the times by working backward from when you need to leave. Our two reminders are five minutes apart.
2. Set a fixed volume for the announcement. Morning music volume varies, and the reminder should be heard every time.
3. Use the Home mode as a condition. If the house is still in Night mode or everyone is away, the reminder stays quiet.
4. Keep the wording short. A little playful is fine.
5. Test on a weekend morning first, while music is playing, to confirm the music comes back.

## How I do it in webCoRE

This is a real piston I run on Hubitat.

1. The piston has two timers: one at 8:52 AM and one at 8:57 AM, both limited to Monday through Friday.
2. Each timer first checks that the location mode is Home.
3. At 8:52 it sends `playHighPriorityTTS` to the kitchen Sonos with the text "It's time to brush them teeth" and volume 30.
4. At 8:57 it does the same with "It's time to put on your shoes".

The high-priority command is what makes this work well. It cuts in over the music so nobody misses it, and the driver resumes the music right after.

## Advanced features

### Skip school holidays

Add a virtual "school day" switch that a parent can turn off for holidays and breaks, and check it as a condition.

### Confirm teeth were actually brushed

Pair the spoken reminder with the [teeth-brushing reminder](/automation/notifications/teeth-brushing-reminder.html) that watches the toothbrush charger.

## Failure modes

- **No announcement:** Check that the mode is Home at that time. A late morning routine can still have the house in Night mode.
- **Music does not resume:** Make sure the command used is the interrupt-and-resume one, not a plain speak command.
- **Too loud or too quiet:** Adjust the announcement volume, not the music volume.
- **It ran on a holiday:** Add the school day switch above.

## FAQ

### Why a spoken reminder instead of a phone notification?

Kids in the kitchen do not see a parent's phone. A voice from the speaker reaches everyone in the room at once.

### What happens to the music that was playing?

The announcement uses a high-priority text-to-speech command that briefly interrupts the speaker, then resumes what was playing.

### Does this run on holidays and vacations?

It only runs on weekdays when the home is in Home mode. On school holidays, you either accept it or add a virtual switch that turns it off.

## Related recipes

- [Kids' teeth-brushing reminder](/automation/notifications/teeth-brushing-reminder.html)
- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)
- [Set smart-speaker volume presets](/automation/entertainment/speaker-volume-presets.html)

{% include page-navigation.html
  left_url="/automation/notifications/index.html"
  left_label="Back to notifications"
  right_url="/automation/index.html"
  right_label="View all automations"
%}
