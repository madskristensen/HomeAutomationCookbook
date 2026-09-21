---
layout: guide
redirect_from:
  - /getting-started/pir-vs-mmwave-presence.html
title: PIR vs mmWave presence sensors
description: Choose between PIR motion, mmWave presence, or both for bathrooms, offices, halls, and other rooms without causing false turn-offs.
date: 2026-08-30
last_modified_at: 2026-09-21
image: /assets/img/social/guides/pir-vs-mmwave-presence.png
---

# PIR vs mmWave presence sensors

<figure class="content-hero">
  <img src="/assets/img/social/guides/pir-vs-mmwave-presence.svg" alt="PIR motion and mmWave presence sensors compared for detecting entry and continued occupancy" width="1200" height="630">
</figure>

PIR is good at noticing someone walk into a room. mmWave is better at noticing that someone is still there. The right answer depends on whether the automation needs a fast trigger, reliable occupied state, or both.

Neither technology identifies a person. Neither should make security, lock, or safety decisions by itself.

## The short answer

| Need | PIR motion | mmWave presence | PIR and mmWave together |
|---|---|---|---|
| Notice someone walking in | Usually a strong fit | Can work, but depends on placement and tuning | Let PIR provide the fast trigger |
| Keep lights on while someone sits still | Often unreliable | Stronger fit | Let mmWave hold the occupied state |
| Run for a long time on a small battery | Often a strong fit | Many models need continuous power | Depends on the device |
| Avoid detecting through a wall or doorway | Easier to constrain by placement | Requires careful range and zone tuning | Tune mmWave for the occupied area |
| Automate a hall, closet, or pantry | Usually enough | Often unnecessary | Usually unnecessary |
| Automate a bathroom, office, or reading area | Use a long off-delay | Better when people remain still | Often the most forgiving option |

Start with PIR when the room is brief and active. Add mmWave when false turn-offs happen because people sit, shower, read, or work without making large movements.

## What each sensor actually tells you

### PIR motion

A passive infrared sensor reacts to changes in heat across its detection zones. Walking across those zones creates a useful motion event. Sitting still does not.

PIR is a good trigger, but a recent motion event is not proof that the room is still occupied. Use an off-delay instead of turning things off as soon as PIR reports no motion.

### mmWave presence

An mmWave sensor uses radio reflections to notice movement, including smaller movement than a typical PIR can detect. That can keep a room occupied while someone sits quietly.

The extra sensitivity needs boundaries. A sensor aimed at a thin wall, open doorway, moving fan, curtain, or nearby traffic can hold the room occupied when nobody is using it.

### A combined sensor

A device with both technologies can use PIR for a quick arrival event and mmWave to maintain presence. Separate sensors can do the same job and let you place each one where it works best.

Do not assume a combined sensor has sensible defaults for your room. Test its detection range and clear delay before it controls anything.

## Bathrooms need presence, not just motion

A cheap PIR and a short timer can turn off the lights while someone is in the shower or sitting still. A safer bathroom pattern is:

- **Trigger:** PIR sees entry motion, or mmWave changes to occupied.
- **Conditions:** Turn lights on only when the room is dark enough or the night-light rule applies.
- **Action:** Turn on the appropriate light level.
- **Hold:** Keep the room occupied while mmWave reports presence.
- **Wait:** After mmWave clears and PIR remains inactive, wait a forgiving amount of time before turning lights off.
- **Manual override:** The physical switch still works and wins.

If you only have PIR, start with a longer delay. Saving a few minutes of light is not worth leaving someone in the dark.

## Home offices need a hold signal

A PIR can detect someone entering an office, then lose them while they type, read, or sit through a long call. Those activities may not create enough movement across the PIR's detection zones.

Use PIR as the fast arrival trigger and mmWave to hold the occupied state. Turn the office off only after mmWave clears for a forgiving delay. The desk light and wall switch should still work manually throughout the workday.

## Choose by room

| Room | Start with | Add mmWave when |
|---|---|---|
| Hall or stair landing | PIR | People regularly remain in the detection area |
| Closet or pantry | Door contact or PIR | The space is large enough for someone to remain still |
| Bathroom | PIR with a long off-delay | Showers or quiet use cause false turn-offs |
| Home office | mmWave or both | PIR cannot reliably hold occupancy while someone works |
| Bedroom | Manual controls first | Presence has a clear, limited purpose that does not disturb sleep |
| Living room | mmWave or both | The automation must distinguish quiet use from an empty room |

Presence sensing should solve a specific failure. Do not add it everywhere just because the sensor is newer.

## Placement and tuning

1. Mount the sensor temporarily before making holes or hiding wires.
2. Watch its raw occupied and clear states without connecting it to lights.
3. Walk through every doorway and nearby room that should not count as occupied.
4. Sit still in the places that must remain detected.
5. Test fans, curtains, pets, open doors, and normal household traffic.
6. Reduce range or narrow zones until adjacent activity stops triggering it.
7. Add the light automation with a long clear delay.
8. Shorten the delay only after the household stops seeing false turn-offs.

Keep sensors away from water and steam unless their instructions and rating allow that exact location.

## Combined or separate sensors?

Use a combined PIR and mmWave sensor when one mounting location sees both the entrance and the occupied area. It is simpler to install and exposes fewer devices to maintain.

Use separate sensors when the doorway needs a fast PIR trigger but the desk, shower, or seating area needs a differently aimed presence zone. Separate devices also let an existing PIR continue doing the job it already does well.

See [recommended smart home gear](/getting-started/device-guide.html#products-i-have-used) for examples I have used in both tiers.

## Failure modes

- **Lights turn off while someone is still:** Lengthen the clear delay, reposition the sensor, or add mmWave presence.
- **The room never clears:** Reduce mmWave range, exclude adjacent zones, and test fans, curtains, and nearby rooms.
- **Lights turn on from hallway traffic:** Aim PIR across the intended entry path and tighten the mmWave boundary.
- **A shower causes inconsistent results:** Move the sensor to a dry, approved location and test with the door and curtain in their normal positions.
- **The sensor becomes unavailable:** Keep the wall switch usable. Missing sensor data must not look like a confidently empty room.
- **Guests fight the automation:** Preserve normal physical controls and use forgiving timeouts.

## FAQ

### Is mmWave always better than PIR?

No. PIR is simpler and often better for brief, active spaces. mmWave earns its complexity where people remain still.

### Can mmWave detect through walls?

Some sensors can react to movement beyond the intended room, depending on construction, placement, range, and sensitivity. Treat the room boundary as something to test and tune.

### Do I need both PIR and mmWave in a bathroom?

Not always. Start with PIR and a generous off-delay. Add mmWave if normal bathroom use still produces false turn-offs.

### Should presence automatically lock doors or arm security?

No. Presence is not identity, and a clear room is not proof that everyone left. Use explicit security state and trusted confirmation for those decisions.

## Related guides

- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Dim the bathroom light at night](/automation/lighting/bathroom-night-light.html)
- [Home automation philosophy](/getting-started/philosophy.html)
