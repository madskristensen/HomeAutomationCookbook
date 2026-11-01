---
layout: automation
redirect_from:
  - /automation/misc/teeth-brushing-reminder.html
date: 2025-11-29
title: Kids teeth-brushing check with a smart plug
description: Know the kids brushed their teeth. A smart plug sees the toothbrush start charging, and a reminder plays only if it never did.
keywords: teeth brushing reminder, kids bedtime automation, energy monitoring smart plug, toothbrush charger
last_modified_at: 2026-11-01
image: /assets/img/social/recipes/notifications/teeth-brushing-reminder.png
compact: true
faqs:
  - question: Does this work with a manual toothbrush?
    answer: No. It needs an electric toothbrush that sits on a charger base. A manual brush draws no power, so there is nothing for the plug to see.
  - question: Does charging prove the kids brushed well?
    answer: No. It only shows the brush went back on the base. It is a good sign that brushing happened, not proof of how well.
  - question: What if my plug never sees the charger draw power?
    answer: The Ezlo 800 plug picks up the charger draw in our house. Chargers differ, though, and some draw very little power. Test your own charger first. If the plug shows no change, try another plug or use a Wi-Fi smart toothbrush instead.
products:
  - job: "Measure when the toothbrush starts charging"
    body: "[Ezlo 800 Series Z-Wave smart plug](https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20). It is the power-monitoring plug on the [device guide](/getting-started/device-guide.html#power-monitoring), and it picks up the charger draw in our house. Test it with your own charger first."
tags: [kids, bedtime, reminders, power-monitoring]
---

# Check that kids brushed their teeth at bedtime

{% include content-hero.html src="/assets/img/social/recipes/notifications/teeth-brushing-reminder.svg" alt="A toothbrush on its charger base plugged into a smart plug that reports when charging starts" %}

Plug the toothbrush charger base into a smart plug that measures power, such as the Ezlo 800 Series Z-Wave smart plug. When the brush goes back on the base after brushing, it starts to charge. The plug sees that. If no charging happens by a set time, a reminder plays.

**Best for:** Kids with an electric toothbrush that charges on a base.

**Not for:** A manual toothbrush. It draws no power, so there is nothing to detect.

## Why this exists

Asking "did you brush?" every night gets old. Kids say yes. Parents check the sink. This recipe answers the question for you and only speaks up when the answer is no. It pairs well with a [bedtime countdown](/automation/notifications/bedtime-countdown.html) that asks kids to brush first.

## How it works

While someone brushes, the brush runs on its battery. When they put it back on the base, the base starts drawing power to recharge it. An energy-monitoring plug notices that jump. So "charging started" during the evening window means the teeth were most likely brushed.

## Logic

<div class="automation-example">IF the charger's power rises above the threshold
AND the time is inside the evening window
THEN mark tonight's brushing as done

IF the reminder time arrives
AND tonight's brushing is not marked done
THEN announce "Time to brush teeth" on a speaker, or send a notification

EVERY morning
THEN clear the done mark for the next evening</div>

- **Trigger:** The plug's power reading rises above the threshold, or the reminder time arrives.
- **Conditions:** Only count charging inside the evening window, for example after dinner.
- **Action:** Mark brushing done. Or, if it is not done by the reminder time, play one reminder.
- **Wait / timeout:** One reminder per night. No repeats.
- **Stop condition:** Charging that starts after the reminder still marks the night as done.
- **Manual override:** A parent can mark the night as done by hand.

## Test your charger first

Some chargers draw very little power, and some plugs cannot register it. Before you build anything:

1. Plug the charger base into the smart plug.
2. Take the brush off for a few minutes, then put it back.
3. Watch the power reading in the plug's app.
4. Note the reading with the brush off and with it charging.
5. Set the threshold between the two numbers.

If the plug shows no clear change, this method will not work with that plug and charger. Try a different plug, or use the alternative below.

## Alternative: a Wi-Fi smart toothbrush

Some electric toothbrushes connect to an app and log each brushing on their own. If yours can share that with your smart home, use it as the trigger instead of the plug. Check what your brush and platform support before you buy for this.

## What I used

{% include product-list.html %}

See [recommended gear](/getting-started/device-guide.html#products-i-have-used) for the job-first checklist. Product recommendations are explained in the [disclosure](/disclosure.html).

## Setup notes

1. Plug the charger into an energy-monitoring smart plug.
2. Run the test above and write down your threshold.
3. Create a "brushed tonight" on and off value, such as a virtual switch or a helper.
4. Turn it on when power rises above the threshold in the evening window.
5. At the reminder time, play the reminder only if it is still off.
6. Turn it off each morning.

## Advanced features

### More than one child

Give each child their own charger, plug, and "brushed tonight" value. The reminder can then name who still needs to brush.

### Mornings too

Add a morning window with its own value and reminder time. For school mornings, see the [school morning countdown](/automation/notifications/school-morning-countdown.html).

## Failure modes

- **Charging is never detected:** The charger may draw too little power for your plug. Recheck the test and the threshold.
- **The brush was left off the base:** No charging means a reminder, even if they brushed. Ask kids to put it back right away.
- **The brush was already full:** Some chargers draw less once the battery is full. Check the reading after a short brushing.
- **The plug went offline:** Treat an offline plug as unknown, not as done.

## FAQ

### Does this work with a manual toothbrush?

No. It needs an electric toothbrush that sits on a charger base. A manual brush draws no power, so there is nothing for the plug to see.

### Does charging prove the kids brushed well?

No. It only shows the brush went back on the base. It is a good sign that brushing happened, not proof of how well.

### What if my plug never sees the charger draw power?

The Ezlo 800 plug picks up the charger draw in our house. Chargers differ, though, and some draw very little power. Test your own charger first. If the plug shows no change, try another plug or use a Wi-Fi smart toothbrush instead.

## Related recipes

- [Bedtime countdown for kids on any smart speaker](/automation/notifications/bedtime-countdown.html), which asks kids to brush first
- [School morning countdown on any smart speaker](/automation/notifications/school-morning-countdown.html)
- [Build a family-safe bedtime routine](/automation/daily-routines/bedtime-routine.html)
- [Get notified when the washer finishes](/automation/appliances/washer-done-notification.html), which uses the same power reading idea
- [Set a nursery quiet mode](/automation/notifications/baby-sleep-mode.html)

{% include page-navigation.html
  left_url="/automation/notifications/"
  left_label="Back to notifications"
  right_url="/automation/"
  right_label="View all automations"
%}
