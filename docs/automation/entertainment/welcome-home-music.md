---
layout: automation
title: Play music when arriving home
description: A platform-neutral recipe that starts music on arrival, using a tested presence signal, to create a consistent welcome-home moment.
keywords: welcome home music, arrival music automation, automatic music greeting, presence detection music, greeting automation
last_modified_at: 2026-08-30
faqs:
  - question: What presence signal should trigger this?
    answer: Use whatever the household has already tested and trusts, such as a phone's location, a smart lock unlocking, or a garage door opening. A single untested signal is the most common source of false triggers.
  - question: Will this play music every time the front door opens?
    answer: Not if it is built around a change from away to home, rather than the door itself. A door can open and close many times while everyone is already home, and only the arrival transition should start music.
  - question: What if multiple people arrive separately?
    answer: Add a cooldown period, so the automation only plays music once per arrival window rather than restarting every time a different household member gets home shortly after the first.
---

# Play music when arriving home

Start music automatically when the household arrives home, using a presence signal that has already been tested and trusted.

**Best for:** A household with a presence-detection method, such as phone location, a smart lock, or a garage door sensor, that has been confirmed to work reliably for every regular occupant.

**Not for:** A home where presence detection is unreliable or untested; a false trigger here just means music plays at an odd time, which is a minor nuisance, but it is still worth getting right.

## Why this exists

Coming home to music playing is a small but pleasant touch, and it removes the need to reach for a phone or speak to an assistant right after walking in. Using an arrival transition, rather than a door sensor alone, keeps it from firing every time someone opens a door while already home.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Detect arrival | No personally verified recommendation yet | No personally verified recommendation yet | Phone-based location, a smart lock, or a garage door sensor can all work; use whichever the household has already tested. |
| Play the music | No personally verified recommendation yet | No personally verified recommendation yet | Any speaker that accepts playback and volume commands from the platform. |

See [recommended gear](/gear.html) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** The household's presence state changes from away to home.
- **Conditions:** The current time falls within hours the household wants a welcome-home moment, and music is not already playing.
- **Action:** Start the welcome playlist on the main speaker at a preset volume.
- **Wait / timeout:** None; playback continues normally once started.
- **Stop condition:** Manual, or a separate automation that stops music after a set duration if desired.
- **Manual override:** The speaker's own controls always work to pause, stop, or change volume directly.

<div class="automation-example">IF the household's presence state changes from away to home
AND the current time is within the hours the household wants this
AND music is not already playing
THEN play the welcome playlist on the main speaker at the preset volume</div>

## Setup notes

1. Confirm the presence signal being used, phone location, lock, or garage sensor, has been tested and works reliably for every regular household member, not just one phone.
2. Trigger on the transition from away to home, not on a door or lock event by itself, so this does not fire repeatedly while everyone is already home.
3. Add a condition that skips the action if music is already playing, so returning briefly does not interrupt something already going.
4. Add a cooldown period so multiple people arriving within a short window only starts music once.
5. Restrict the hours this runs, if the household does not want a welcome-home moment at every hour, such as very early morning.

## Advanced features

### Time-based volume and playlist

Choose a different playlist and volume depending on arrival time, such as a quieter volume for a late-evening arrival and a livelier one earlier in the day.

### Voice announcement before music

Play a short spoken greeting first, then start the playlist a few seconds later, if the platform supports sequencing announcements and playback.

## Failure modes

- **Music plays every time a door opens:** Confirm the trigger uses the away-to-home presence transition, not a raw door or lock event.
- **Presence detection is unreliable:** Combine more than one tested signal, such as phone location together with a garage door or lock event, rather than relying on a single method.
- **Music plays at an inconvenient time:** Add or correct the hours condition.
- **Music restarts for each household member arriving separately:** Add a cooldown so only the first arrival within a window starts playback.
- **Volume is inappropriate for the time of day:** Set volume explicitly per time window rather than using one fixed level for every arrival.

## Done when

- [ ] The presence signal has been tested and confirmed reliable for every regular household member.
- [ ] Arriving home reliably starts music without needing a manual action.
- [ ] The automation does not restart music when someone who is already home opens a door.
- [ ] Multiple arrivals in a short window do not restart music repeatedly.
- [ ] The speaker's own manual controls still work independently.

## FAQ

### What presence signal should trigger this?

Use whatever the household has already tested and trusts, such as a phone's location, a smart lock unlocking, or a garage door opening. A single untested signal is the most common source of false triggers.

### Will this play music every time the front door opens?

Not if it is built around a change from away to home, rather than the door itself. A door can open and close many times while everyone is already home, and only the arrival transition should start music.

### What if multiple people arrive separately?

Add a cooldown period, so the automation only plays music once per arrival window rather than restarting every time a different household member gets home shortly after the first.

## Related recipes

- [Play music when a shower starts](/automation/entertainment/shower-music.html)
- [Play or pause music with a physical switch](/automation/entertainment/music-switch-control.html)
- [Start a quiet good-morning routine](/automation/daily-routines/morning-routine.html)

<div class="page-navigation">
  <a href="/automation/entertainment/index.html">Back to entertainment</a>
  <a href="/automation/index.html">View all automations</a>
</div>