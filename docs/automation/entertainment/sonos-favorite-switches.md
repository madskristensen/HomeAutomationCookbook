---
layout: automation
date: 2026-10-25
title: Whole-home music with favorite station switches
description: Virtual switches for favorite stations group the downstairs speakers and start a Sonos favorite, and a nightly reset ungroups them and puts every speaker back at a sensible volume.
keywords: Sonos favorites virtual switch, Sonos group automation Hubitat, whole home music automation, Sonos Advanced Controller, webCoRE music piston
last_modified_at: 2026-10-25
image: /assets/img/social/recipes/entertainment/sonos-favorite-switches.png
compact: true
faqs:
  - question: Why use virtual switches for stations?
    answer: A switch is something every dashboard, voice assistant, and rule understands. Turning on "Country" works the same from a wall tablet, Alexa, or another automation.
  - question: Why ungroup and regroup the speakers at night?
    answer: Over a day, people pull speakers out of the group and change volumes. A reset at night or when leaving puts every speaker back in a known state for the next day.
  - question: Can I still use the Sonos app?
    answer: Yes. The app keeps working normally. The automation only acts when a station switch or a mode change asks it to.
products:
  - job: "Play the music"
    body: "Sonos speakers downstairs, with one chosen as the group coordinator."
  - job: "Control groups and favorites from the hub"
    body: "On Hubitat, I use the community [Sonos Advanced Controller](https://community.hubitat.com/t/release-sonos-advanced-controller/130296). It can load Sonos favorites and manage groups locally."
  - job: "Pick a station"
    body: "Virtual switches on the hub, one per station, plus a stop switch."
---

# Whole-home music with favorite station switches

{% include content-hero.html src="/assets/img/social/recipes/entertainment/sonos-favorite-switches.svg" alt="Station switches group the speakers and start a favorite with one tap" %}

We have a handful of stations we play all the time. This recipe turns each one into a virtual switch. Flip "Mellow rock" and the downstairs speakers group together and start playing it. When the house goes to Night or Away, the music stops and every speaker resets for the next day.

**Best for:** A home with several Sonos speakers in open, connected rooms and a few go-to stations saved as Sonos favorites.

**Not for:** A house where each room plays its own thing most of the time.

## Why this exists

Starting whole-home music in the Sonos app takes several taps: group the rooms, pick a source, find the station. A switch does it in one step. Making it a switch, and not just a button rule, also means it shows up in dashboards and voice assistants without extra work.

The reset half matters just as much. Speakers drift out of the group and volumes creep up or down. Resetting once a day keeps the next morning predictable.

## Logic

<div class="automation-example">IF a station switch turns on (mellow rock, country, tropical, or happy)
OR the home mode changes to Home
THEN group the downstairs speakers with the coordinator speaker
AND load that station's Sonos favorite on the group with repeat and replace queue

IF the stop music switch turns on
THEN pause the group

IF the home mode changes to Night or Away
OR the reset switch turns on
THEN stop and ungroup the speakers
AND set each speaker to its own default volume
AND wait 5 seconds
AND group the speakers again</div>

- **Trigger:** A station switch, a mode change to Home, the stop switch, a mode change to Night or Away, or a reset switch.
- **Conditions:** None beyond which switch or mode triggered it.
- **Action:** Group, load a favorite, pause, or reset.
- **Wait / timeout:** A 5 second pause between ungrouping and regrouping gives the speakers time to settle.
- **Stop condition:** The stop switch, or the next mode change.
- **Manual override:** The Sonos app and the speakers' own buttons keep working.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Save each station as a Sonos favorite first. The automation loads favorites by name or ID, so the favorite has to exist.
2. Create one virtual switch per station and one for stopping the music. Name them the way you would say them out loud, since voice assistants use the device name.
3. Pick one speaker as the coordinator. It should be one that is always powered and on the network.
4. Choose a default volume for each speaker based on its room. A speaker in a small room needs less than one in a big open space.
5. Use repeat and replace queue when loading a favorite, so a playlist loops and a new station replaces what was there.
6. Expose the station switches to your dashboard and voice assistant.

## How I do it in webCoRE

This is a real piston I run on Hubitat with the Sonos Advanced driver.

1. The piston subscribes to the station switches, the stop switch, and the location mode.
2. When a station switch turns on, it groups the downstairs speakers to the coordinator and loads the matching favorite with repeat on and replace queue.
3. When the mode changes to Home, it does the same with the "mainstream" favorite, so music starts when the house wakes up.
4. When the stop switch turns on, it pauses the group.
5. When the mode changes to Night or Away, or the reset runs, it turns the speakers off and ungroups them. Then it sets each speaker to its own default volume, waits 5 seconds, and regroups them so the next start is clean.

Because the stations are plain switches, I did not have to build anything special for the dashboard or Alexa. They just show up as switches.

## Advanced features

### Turn off the other station switches

When one station switch turns on, turn the others off, so the dashboard always shows which station is playing.

### Time-aware defaults

Use a mellower station in the morning and an upbeat one in the afternoon when the mode changes to Home.

## Failure modes

- **Wrong station plays:** Check that the favorite name or ID in the rule still matches the Sonos favorite.
- **One speaker is left out of the group:** Make sure it was online during the regroup. The 5 second wait helps, but a speaker that just woke up may need longer.
- **Volume is wrong after the reset:** Set the volume while the speakers are ungrouped. Group volume changes move every speaker together.
- **Music starts when nobody wants it:** Remove the Home mode trigger and rely on the switches only.

## FAQ

### Why use virtual switches for stations?

A switch is something every dashboard, voice assistant, and rule understands. Turning on "Country" works the same from a wall tablet, Alexa, or another automation.

### Why ungroup and regroup the speakers at night?

Over a day, people pull speakers out of the group and change volumes. A reset at night or when leaving puts every speaker back in a known state for the next day.

### Can I still use the Sonos app?

Yes. The app keeps working normally. The automation only acts when a station switch or a mode change asks it to.

## Related recipes

- [Control music with a physical switch](/automation/entertainment/music-switch-control.html)
- [Shared whole-home music controls](/automation/notifications/music-controls.html)
- [Set smart-speaker volume presets](/automation/entertainment/speaker-volume-presets.html)
- [Play music when arriving home](/automation/entertainment/welcome-home-music.html)

{% include page-navigation.html
  left_url="/automation/entertainment/index.html"
  left_label="Back to entertainment"
  right_url="/automation/index.html"
  right_label="View all automations"
%}
