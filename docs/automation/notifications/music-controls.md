---
layout: automation
title: Add dashboard tiles for music playback controls
description: A platform-neutral recipe that puts play, pause, and volume controls for whole-home audio on a shared dashboard.
keywords: music dashboard, playback controls, whole home audio, dashboard tiles, music control automation
last_modified_at: 2026-08-30
faqs:
  - question: Do I need whole-home audio for this to be useful?
    answer: It helps, since a single dashboard controlling several speakers at once is more valuable than controlling just one. It still works for a single speaker, but a dedicated app may be just as convenient in that case.
  - question: Why use dashboard tiles instead of the speaker manufacturer's app?
    answer: A shared dashboard keeps music controls next to other household controls, such as lights and locks, so anyone in the house can adjust playback without switching apps or needing a specific phone.
  - question: Can this control speakers from different brands together?
    answer: Only if the platform already integrates with each speaker brand individually. This recipe describes the dashboard layer on top of that integration, not a way to unify incompatible speaker ecosystems.
---

# Add dashboard tiles for music playback controls

Put play, pause, and volume controls for whole-home audio on a shared dashboard instead of a separate speaker app.

**Best for:** A household with more than one connected speaker and a shared dashboard already in use for other controls.

**Not for:** A single standalone speaker with no other dashboard use; the manufacturer's own app is likely simpler in that case.

## Why this exists

Music controls scattered across separate manufacturer apps means switching apps just to pause a speaker in another room. Bringing playback controls onto the same dashboard used for lights, locks, and other status tiles keeps everything in one place.

## What I used

| Job | Good enough | Never think about it | Notes |
|---|---|---|---|
| Control connected speakers from a dashboard | No personally verified recommendation yet | No personally verified recommendation yet | This depends on the platform's existing integration with each speaker brand; no additional hardware is needed beyond the speakers themselves. |

See [recommended gear](/gear.html) for the job-first checklist. Product recommendations and any future affiliate relationships are explained in the [disclosure](/disclosure.html).

## Logic

- **Trigger:** A dashboard tile is tapped, such as play, pause, or a volume adjustment.
- **Conditions:** The targeted speaker is online and reachable by the platform.
- **Action:** Send the corresponding playback or volume command to that speaker.
- **Wait / timeout:** None; the command is sent immediately when the tile is tapped.
- **Stop condition:** Not applicable; each tile press is a separate command.
- **Manual override:** The speaker's own physical controls or manufacturer app continue to work independent of the dashboard.

<div class="automation-example">IF the "pause" tile is tapped for the living room speaker
THEN send a pause command to the living room speaker

IF the volume slider is adjusted for the kitchen speaker
THEN set the kitchen speaker's volume to the selected level</div>

## Setup notes

1. Confirm the platform already integrates with each speaker brand in use; this recipe only adds a dashboard layer on top of that integration.
2. Add a dashboard section for music controls, with play, pause, and volume tiles per room or speaker.
3. Group tiles by room so it is clear which speaker each control affects.
4. Test each tile individually to confirm it targets the correct speaker.
5. If the household plays synchronized audio across multiple rooms, consider adding a single tile that controls the whole group at once.

## Advanced features

### Whole-home group control

Add a tile that sends play, pause, or volume commands to every speaker at once, useful for parties or when leaving the house and wanting music off everywhere.

### Now playing display

If the platform supports it, show the current track or source on the dashboard alongside the controls, so it is clear what is playing without opening a separate app.

## Failure modes

- **A tile does not respond:** Confirm the target speaker is online and check the platform's integration status for that speaker brand.
- **The wrong speaker responds to a tile:** Double check the tile's configured target device.
- **Volume changes lag behind the tile:** Some speaker integrations poll status rather than update instantly; this is a platform limitation rather than a dashboard problem.
- **Group control does not include a new speaker:** Confirm the new speaker was added to the group definition, not just the individual room tiles.

## Done when

- [ ] Every connected speaker has working play, pause, and volume tiles.
- [ ] Tiles are clearly grouped or labeled by room.
- [ ] A whole-home group control tile works if the household uses synchronized audio.
- [ ] Each tile reliably targets the correct speaker.

## FAQ

### Do I need whole-home audio for this to be useful?

It helps, since a single dashboard controlling several speakers at once is more valuable than controlling just one. It still works for a single speaker, but a dedicated app may be just as convenient in that case.

### Why use dashboard tiles instead of the speaker manufacturer's app?

A shared dashboard keeps music controls next to other household controls, such as lights and locks, so anyone in the house can adjust playback without switching apps or needing a specific phone.

### Can this control speakers from different brands together?

Only if the platform already integrates with each speaker brand individually. This recipe describes the dashboard layer on top of that integration, not a way to unify incompatible speaker ecosystems.

## Related recipes

- [Control music with a wall switch](/automation/entertainment/music-switch-control.html)
- [Use status tiles instead of notifications](/automation/notifications/status-tiles.html)
- [Set volume presets for a speaker](/automation/entertainment/speaker-volume-presets.html)

<div class="page-navigation">
  <a href="/automation/notifications/index.html">Back to notifications</a>
  <a href="/automation/index.html">View all automations</a>
</div>