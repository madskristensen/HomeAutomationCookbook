---
layout: automation
date: 2026-11-01
last_modified_at: 2026-11-01
image: /assets/img/social/recipes/daily-routines/kids-music-wake-up.png
title: Wake kids up to their own music with a smart speaker
description: A smart speaker alarm in the kid's room plays music they picked, so they wake up on their own. Add blinds or a slow light fade if you like.
keywords: kids music alarm, wake up kids smart speaker, Alexa music alarm for kids, kids morning routine, smart speaker alarm
compact: true
tags: [kids, morning]
faqs:
  - question: Which speakers work?
    answer: An Echo speaker can set an alarm that plays music. Google speakers no longer offer music alarms, so use a timed routine that plays music instead. Any speaker your platform can start music on at a set time works the same way.
  - question: How do I skip weekends?
    answer: Set the alarm or routine for school days only. Keep a separate, later one for weekends, or none at all.
products:
  - job: "Play the music in the kid's room"
    body: "Any smart speaker in their room. No new hardware is needed if you already have one."
  - job: "Fade the light up slowly (optional)"
    body: "[UltraPro Z-Wave Long Range Dimmer](https://www.amazon.com/dp/B0FX36Z8VN/ref=nosim?tag=madsk0f-20), or any dimmable light your hub can fade."
---

# Wake kids up to their own music with a smart speaker

{% include content-hero.html src="/assets/img/social/recipes/daily-routines/kids-music-wake-up.svg" alt="A smart speaker card with a music note, for a kid's alarm that plays music they picked" %}

A smart speaker in the kid's room plays music they chose at wake-up time. They wake up on their own. Nobody has to go in and wake them.

**Pairs well with:** [School morning countdown on any smart speaker](/automation/notifications/school-morning-countdown.html)

**Best for:** Kids with their own room and a fixed wake time on school days.

**Not for:** A shared room where one child needs to sleep longer.

## Why this exists

When kids don't wake up on their own, or wake up slowly, the whole house has a rough morning. We have used this since our kids were very young. Their own music wakes them. They start the day in a better mood, and we don't start it by calling their names down the hall.

Letting them pick the song matters. It is their alarm, not ours.

See [all kids and family routines](/articles/smart-home-automations-for-kids.html) for more like this.

## Logic

<div class="automation-example">IF it is a school day
AND the time is the wake-up time
THEN play the kid's chosen music on the speaker in their room

OPTIONAL: open the blinds
OPTIONAL: in winter, fade the light up slowly</div>

- **Trigger:** The wake-up time.
- **Conditions:** It is a school day.
- **Action:** Play the music they picked on the speaker in their room.
- **Wait / timeout:** The music plays until they turn it off.
- **Stop condition:** The kid says stop or presses the speaker.
- **Manual override:** Turn off the alarm or routine for days off.

## Setup notes

1. Put a smart speaker in the kid's room.
2. Let them pick a song, artist, or playlist.
3. Set it up for your platform. See the notes below.
4. Limit it to school days.
5. Set the volume low enough to be pleasant, and loud enough to work.
6. Test it once on a weekend morning.

## Platform notes

- **Alexa:** Say "Alexa, set an alarm for 7 AM to [song or playlist] every weekday." The music plays as the alarm. Link the music service in the Alexa app first.
- **Google:** Music alarms are no longer available on Google speakers. Make a household routine with a time starter and a "Play music" action on the speaker in their room.
- **Other speakers:** Use your hub to start music on the speaker at a set time, like any timed routine.

## Optional extras

### Open the blinds

If their room has smart blinds or shades, open them at wake-up time. See [adjust blinds at sunset and sunrise](/automation/climate/blinds-sunset-sunrise.html).

### Fade the lights up in winter

Winter mornings are dark. A light that fades up slowly before the music helps. See [gradual wake-up lighting](/automation/lighting/wake-up-lights.html) for the fade.

### Start extras when the alarm stops

On Alexa, a routine can start when an alarm is dismissed. Use it to open the blinds or turn on the lights once the kid stops the music.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html) for more. Amazon product links on this page are affiliate links, and I earn from qualifying purchases. See the [disclosure](/disclosure.html).

## Failure modes

- **They sleep through it:** Raise the volume, or pick a more upbeat song.
- **The song gets old:** Let them pick a new one every few weeks.
- **It plays on a day off:** Check the day setting. Turn it off for holidays.
- **No music, just a beep:** The music service may not be linked, or it may be offline. Check the app.

## FAQ

### Which speakers work?

An Echo speaker can set an alarm that plays music. Google speakers no longer offer music alarms, so use a timed routine that plays music instead. Any speaker your platform can start music on at a set time works the same way.

### How do I skip weekends?

Set the alarm or routine for school days only. Keep a separate, later one for weekends, or none at all.

## Related recipes

- [All kids and family routines](/articles/smart-home-automations-for-kids.html)
- [School morning countdown on any smart speaker](/automation/notifications/school-morning-countdown.html)
- [Set up gradual wake-up lighting](/automation/lighting/wake-up-lights.html)
- [Adjust blinds at sunset and sunrise](/automation/climate/blinds-sunset-sunrise.html)
- [Smart home morning routine and scenes](/automation/daily-routines/morning-routine.html)

{% include page-navigation.html
  left_url="/automation/daily-routines/"
  left_label="Back to daily routines"
  right_url="/automation/"
  right_label="View all automations"
%}
