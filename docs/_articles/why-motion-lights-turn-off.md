---
layout: guide
title: Why motion lights turn off while you are still there
description: Stop motion lights from turning off while you are still in the room. Check the timeout, sensor aim, and when to add a presence sensor.
date: 2026-10-19
last_modified_at: 2026-10-19
image: /assets/img/social/guides/why-motion-lights-turn-off.png
---

# Why motion lights turn off while you are still there

{% include content-hero.html src="/assets/img/social/guides/why-motion-lights-turn-off.svg" alt="A checklist for a motion light that turned off while someone is still in the room" %}

A motion light that goes dark while someone is still in the room is usually obeying its timer. The sensor stopped seeing movement. Sitting, reading, typing, or standing in a shower often does not count as movement.

## The short answer

| What you were doing | What a PIR usually reports | Change this first |
|---|---|---|
| Sitting and reading | Little or no movement | A longer off delay |
| Desk work | Small movement that misses the sensor's zones | Aim across the desk, or add presence sensing |
| Bathroom or shower | A still person, or someone behind a curtain | A longer delay. Add presence sensing if it still fails |
| You need the light to stay on | No pause on the off rule | A stay-on control. A door contact can help, but it is not proof anyone is inside |

Change one thing. Use the room the way you normally do. Then change the next thing.

## A PIR sees movement, not a person

A typical passive infrared sensor reacts when heat crosses its zones. Walking through the room does that. Sitting in a chair often does not.

A recent motion event is not proof the room is still occupied. A clear sensor is not proof the room is empty. The light can turn on when you walk in, then turn off while you read. The on rule did its job. The off rule trusted a sensor that had gone quiet.

[PIR vs mmWave presence sensors](/articles/pir-vs-mmwave-presence.html) splits those jobs. PIR is a fast trigger. Presence sensing is the hold signal for someone who stays still.

## Start with a longer timeout

A short off delay looks tidy and fails the first time someone sits down. Extra minutes of light are a smaller problem than a dark desk or a dark bathroom.

Use the room normally for several days before you shorten the delay. Reading, a long call, a shower, and getting ready all count. If the light still drops during those, the timeout is not the only gap.

[Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html) is the off half of motion lighting. It starts bathrooms and other quiet rooms on a longer delay for this reason.

## Point the sensor at the still places

A PIR usually notices a person crossing its zones better than a person walking straight at it. A sensor aimed at the doorway can catch the entry and then lose the person who sits down.

Put the sensor up with tape first. Pause the light rule and watch the raw motion state. Sit in the chair, at the desk, and where you stand in the bathroom. If the sensor stays clear, move it or re-aim it before you edit the rule.

[How to place motion sensors](/articles/motion-sensor-placement.html) is the longer version of that test. It covers the entry path, the places someone stays still, and the hallway or vent that should not count.

Keep the sensor away from vents, fans, and patches of sun. Those make the light stay on, which is a different problem.

## Add presence sensing when stillness is normal

An mmWave presence sensor can notice smaller movement than a typical PIR. That can keep the room occupied while someone types, reads, or stands still.

The extra sensitivity needs a boundary. A sensor aimed at a thin wall, an open doorway, a fan, or a moving curtain can hold the room occupied after everyone has left. Test the clear state with the light rule off before you trust it.

Use the entry event to turn the light on. Use presence to hold it. Turn the light off only after presence clears and the off delay passes. If the presence sensor stops reporting, treat that as missing data, not an empty room. The wall switch still has to work.

Presence is not a person, a lock signal, or proof the house is empty.

## Three small fixes

Pick one change, then live with it for a few days.

**A longer timeout while the room is in use.** Keep a short delay for a hall or a closet. Use a longer delay for a bathroom, a reading chair, or a desk. You can switch to the longer delay when something else says the room is in use, such as motion followed by a closed door, and return to the short delay when that signal is gone.

**A door contact as a helper.** A contact on the bathroom or office door can restart the off timer when the door moves. That helps when the PIR misses the person inside. It can also select the longer timeout while the door stays closed after someone came in. It cannot prove the room is occupied. A closed door in an empty room would leave the light on, so the off delay still has to end. Do not turn a bathroom or office light off because the door closed. That pattern is for a small closet, in [turn a closet light off after the door closes](/automation/lighting/disable-on-door-close.html).

**A stay-on control.** A button, the wall switch, or a dashboard toggle can pause the automatic off until someone clears it. Put it where the person already is, and give it a plain name such as stay on. If someone turns the light on or off by hand, the next timer must not undo that choice.

## Reading, desk work, and bathrooms

A reading chair and a desk fail the same way. Entry motion turns the light on. Still work does not refresh the timer. Aim across the seat or the desk, lengthen the delay, and add presence sensing if the PIR still drops out.

A bathroom fails when someone is in the shower, behind a curtain, or standing at the mirror without crossing a zone. Start with the longer delay. If a normal shower still goes dark, use presence sensing, and keep the sensor in a dry spot it is rated for. Night visits can stay dim with [dim the bathroom light at night](/automation/lighting/bathroom-night-light.html). The on half is [turn lights on when you walk in](/automation/lighting/lights-on-motion.html).

## Failure modes

- **The light drops while you read or type:** Lengthen the timeout, then aim the sensor across the seat or desk. Add presence sensing if the PIR still clears.
- **The bathroom goes dark in the shower:** Use a longer delay first. Add presence sensing if normal showers still fail.
- **The light never turns off:** The sensor is seeing a hall, a vent, a fan, or a pet. Fix the view before you add a stay-on control. [Lights turning on by themselves](/articles/lights-turning-on-by-themselves.html) is the checklist for the opposite surprise.
- **Stay on is left enabled:** Make the control visible, and clear it when the light is turned off by hand.
- **A closed door keeps an empty room lit:** Do not treat the door as occupancy. Keep an off delay that still ends.
- **The sensor stops reporting:** Leave the wall switch working. Missing data must not count as an empty room.

## FAQ

### Why does the light turn off when I am sitting still?

A PIR reports movement across its zones. Sitting, reading, and typing often do not create that movement, so the off timer runs out.

### Should I replace the motion sensor right away?

No. Lengthen the timeout and check the aim first. Add presence sensing when people in that room regularly stay still and the PIR still goes clear.

### Can a door sensor tell that the bathroom is occupied?

No. A door contact can restart a timer or choose a longer delay. It does not prove that someone is inside, or that they left.

### How do I keep the light on while I am in the room?

Add a stay-on control that pauses the off rule, and let the wall switch do the same job. Clear it when you leave so the room can turn off later.

## Related guides and recipes

- [PIR vs mmWave presence sensors](/articles/pir-vs-mmwave-presence.html)
- [How to place motion sensors](/articles/motion-sensor-placement.html)
- [Turn lights on when you walk in](/automation/lighting/lights-on-motion.html)
- [Turn lights off after motion stops](/automation/lighting/lights-off-after-motion.html)
- [Dim the bathroom light at night](/automation/lighting/bathroom-night-light.html)
- [Turn a closet light off after the door closes](/automation/lighting/disable-on-door-close.html)
- [Lights turning on by themselves](/articles/lights-turning-on-by-themselves.html)
