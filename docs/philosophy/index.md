---
layout: default
title: Home Automation Philosophy
---

# Home Automation Philosophy

The best smart home is one that works seamlessly for everyone, requires no explanation, and continues functioning even when things go wrong. These core principles should guide every automation you create.

## Works for everybody

Home automation must work for all members of the household - kids, adults, elderly parents, and even guests. It should never require people to change their behavior to accommodate the technology. Instead, the automation should intelligently adapt to serve everyone's needs.

### Example: Automatic lights done wrong

When I first installed automatic lights in my bathrooms, they worked perfectly for me. However, my wife complained that they didn't work for her at all. The problem? The motion sensor delay. By the time she opened the door and walked in, the lights would just be turning on, which prevented her muscle memory from reaching for the light switch. But once she clicked the switch out of habit, the lights would turn off instead of on.

### The fix

I relocated the motion sensor to a better position and optimized the automation for faster execution. Now the lights turn on instantly, and nobody's muscle memory causes the lights to turn off inadvertently.

**Key takeaway**: Sometimes only real-world usage will reveal flaws in your automation logic. Be prepared to iterate and improve based on feedback from everyone in your household.

---

## Adapts to natural behavior

Home automation systems should improve people's lives by working in ways that follow natural human behavior. It's easy to build automations that work perfectly when people use them the "correct" way, but if that's not how people naturally behave, the automation needs adjustment.

### Example: Linen closet lights

I created an automation that turned on the lights when the linen closet door opened and turned them off when it closed. Simple enough, right? It worked great... except for one problem.

In real life, we often push the door ajar rather than fully closing it. When the door wasn't completely closed, the lights stayed on, making the automation seem broken.

### The fix

I moved the door sensor from the corner of the door to a location where "almost closed" was recognized by the automation as "closed."

**Key takeaway**: Observe how people actually use your space, not how you think they should use it. Adjust your automations accordingly.

---

## No further explanation needed

When the smart home works for everybody and adapts to natural behavior, it shouldn't require explanation. However, some advanced automations go beyond discoverable natural behavior and need to be taught.

### Hidden features as patterns

Some smart switches support double-tapping as a trigger. You can't tell a switch has this feature by looking at it, so unless you're taught, you won't know it exists.

**Solution**: Create patterns throughout your house. For example:
- Double-tap any light switch to turn on/off **all** lights in that room
- Optionally mark switches with this capability for visual identification

Once taught, people can apply the same pattern to any room without further explanation needed.

---

## Resiliency built in

When your internet goes down or the smart home hub fails, the smart home must still be functional. All lights must work from physical switches, door locks must still let you in, and basic functions should continue operating.

**The smart home must fail gracefully.**

### Example: The snowstorm incident

After a major snowstorm knocked out our internet for several days, I learned this lesson the hard way. The smart home hub still worked, but it could only execute automations that didn't require an internet connection. I couldn't use the app to control anything either.

Some automations kept running that shouldn't have - like lights turning on in bedrooms in the middle of the night, because the house couldn't put itself into night mode without internet. I had to unplug the hub entirely.

### The fix

After regaining internet, I made several changes:
1. Ensured all essential automations run locally (no internet required)
2. Made non-essential automations fail gracefully
3. Added physical switches and buttons to control states and variables
4. Created manual overrides for critical automations

---

## The automation pyramid

Think of home automation as a pyramid with three levels. Each level requires the one below it and should be completely independent of any levels above it.

### Level 1: Core functionality (base)

The foundation that must **always** be operational. Only a power outage should disable this level.

**Examples:**
- Physical light switches
- Manual door locks
- Physical thermostat controls
- Manual fan switches

**Requirement:** When the smart home hub and/or internet is down, the home gracefully degrades to a fully functioning "dumb" home.

### Level 2: Basic automations (middle)

Essential automations that should work even when internet is down. These should execute fully locally without dependencies on Level 3.

**Examples:**
- Motion sensor-based lighting
- Door sensor-triggered lights
- Contact sensor automations
- Bathroom fan automations
- Basic thermostat operations

**Requirement:** No internet dependency, all processing done locally by the hub.

### Level 3: Extras (top)

Non-essential automations and features that may require an internet connection. Keep this level as small as possible since these are most likely to break down first.

**Examples:**
- Voice assistant controls (Alexa, Google, Siri)
- Cloud-dependent switches and bulbs
- Remote access and notifications
- Weather-based automations
- Integration with online services

---

## Putting philosophy into practice

As you build your automations, ask yourself:

1. ✅ **Does it work for everyone in my household?**
2. ✅ **Does it adapt to how people naturally behave?**
3. ✅ **Can people figure it out without my explanation?**
4. ✅ **Will it still work if the internet goes down?**
5. ✅ **Do physical controls still function as expected?**

If you can answer "yes" to all five questions, you've created a solid automation that follows these core principles.

---

[Ready to build automations? →](/automation/)
