---
layout: default
title: Presence and Modes Automations - Location-Based Smart Home
description: Master presence detection and mode-based automations. Away mode, arrival routines, morning and bedtime automations for your smart home.
keywords: presence detection, location automation, home modes, away mode, arrival automation, GPS automation, smart home presence
---

# Presence and modes automations

Presence detection and home modes unlock powerful automations based on location and daily routines. While notoriously tricky to perfect, these fundamentals enable energy savings, security, and seamless smart home experiences.

<div class="category-intro" markdown="1">

## Why presence detection?

**Automatic Home/Away** — House knows when everyone leaves or arrives

**Energy Savings** — Reduce heating/cooling when away by 10-15%

**Enhanced Security** — Arm systems automatically when you leave

**Seamless Entry** — Unlock doors, turn on lights as you arrive

**Daily Routines** — Morning and bedtime automations happen automatically

**Location Context** — Automations adapt based on who's home

</div>

## 🌟 Essential Automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

#### [Set away mode when everyone leaves](/automation/presence/away-mode.html)

Automatically activate Away Mode when the last person leaves. Includes energy savings, security activation, and verification strategies.

**Best for:** Energy savings, security, automated home management

<p><a href="/automation/presence/away-mode.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

#### [Morning routine automation](/automation/presence/morning-routine.html)

Wake up to an automated morning routine. Lights, coffee, weather, and climate all prepared automatically.

**Best for:** Consistent wake-up experience, morning efficiency

<p><a href="/automation/presence/morning-routine.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Understanding home modes

Most smart home platforms include default modes:

### Home mode
**When:** Someone is home and awake
**Actions:**
- Normal lighting automation
- Comfortable temperature
- Interior sensors disabled
- Music/entertainment available

### Away mode  
**When:** No one is home
**Actions:**
- Lights off (or away pattern)
- Eco temperature settings
- Security armed
- Cameras active

### Night mode
**When:** Sleeping hours
**Actions:**
- Low-brightness lighting only
- Lower temperature
- Minimal notifications
- Quiet hours enabled

### Custom modes
Many platforms allow custom modes:
- **Guest Mode** - Modified automation for visitors
- **Vacation Mode** - Extended away with security
- **Party Mode** - Special lighting and music
- **Movie Mode** - Theater lighting and DND

---

## Quick start guide

### 1. Set up location tracking

**Enable on All Phones:**
- Download platform app
- Allow location "Always"
- Enable background app refresh
- Disable battery optimization for app

**Platforms:**
- Home Assistant Companion App
- SmartThings App
- Life360 (integrates with many)
- Apple Home (built-in)

### 2. Create home zones

**Home Zone:**
- Radius: 50-100 meters
- Center: Your home address
- Trigger when enter/exit

**Approaching Zone (Optional):**
- Radius: 500 meters
- Pre-heat/cool home
- Turn on exterior lights

### 3. Configure modes

**Create mode input:**
- Home
- Away
- Night
- (Any custom modes)

**Set default mode actions:**
- What happens in each mode
- Transition behaviors
- Fallback rules

### 4. Build basic automations

**Start Simple:**
1. Away mode when everyone leaves
2. Home mode when someone arrives
3. Night mode at bedtime
4. Home mode in morning

**Then Enhance:**
- Add verification conditions
- Per-person customization
- Mode-specific actions
- Advanced triggers

---

## Presence detection methods

### GPS/Location Services

**How it works:** Phone reports location to platform

**Pros:**
- Works everywhere
- No additional hardware
- Integrates with platform

**Cons:**
- Battery drain
- GPS can drift
- Requires app background access
- Privacy considerations

**Accuracy:** 10-50 meters typical

### WiFi Presence

**How it works:** Detect phone connected to home WiFi

**Pros:**
- No battery drain
- Very accurate when home
- Privacy-friendly

**Cons:**
- Only works at home
- Doesn't detect arriving/leaving
- False positives if WiFi reaches outside

**Use case:** Verification method, not primary

### Bluetooth Presence

**How it works:** Detect Bluetooth beacons

**Pros:**
- Room-level accuracy
- Low power
- Fast detection

**Cons:**
- Requires beacons
- Limited range
- Setup complexity

**Use case:** Room presence, not home/away

### Combined approach (recommended)

Use multiple methods for accuracy:

1. **GPS** - Primary detection (home/away)
2. **Motion sensors** - Verify no one home
3. **WiFi** - Confirm presence at home
4. **Door sensors** - Physical entry/exit

---

## Common challenges & solutions

### Challenge: False away mode activation

**Causes:**
- GPS drift
- Phone location jumps
- Someone without phone is home

**Solutions:**
- ✅ Add motion sensor verification
- ✅ Increase geofence radius
- ✅ Add 10-15 minute delay
- ✅ Check door activity
- ✅ Verify TV/music status

### Challenge: Delayed presence detection

**Causes:**
- Background app restrictions
- Battery optimization
- Slow GPS update
- Cloud processing delay

**Solutions:**
- ✅ Disable battery optimization for app
- ✅ Enable "Always" location
- ✅ Use local processing
- ✅ Add WiFi presence backup

### Challenge: Battery drain from location

**Causes:**
- Continuous GPS polling
- Frequent position updates
- Background processing

**Solutions:**
- ✅ Adjust update frequency
- ✅ Use WiFi presence when home
- ✅ Enable battery-saving mode
- ✅ Consider dedicated device (tablet)

### Challenge: Kids without phones

**Causes:**
- Young kids don't have phones
- Can't track their presence

**Solutions:**
- ✅ Time-based overrides (after-school hours)
- ✅ Door sensor verification (can't lock deadbolt from inside)
- ✅ Extended motion-free period required
- ✅ Manual "Kids Home" toggle

---

## Advanced techniques

### Graduated geofences

Create multiple zones for progressive actions:

**Far (2km):**
- Start preparing home

**Approaching (500m):**
- Pre-heat/cool
- Turn on exterior lights

**Arriving (100m):**  
- Full arrival routine
- Unlock door

**Home (50m):**
- Inside home zone

### Room-level presence

Track which room each person is in:

**Methods:**
- Bluetooth beacons
- mmWave sensors
- WiFi triangulation
- Camera person detection

**Use cases:**
- Light only occupied rooms
- Per-room climate control
- Follow-me music
- Presence-based scenes

### Predictive presence

Learn patterns and predict:
- Typical arrival times
- Weekend vs weekday behavior
- Seasonal variations
- Special events

**Actions:**
- Pre-condition home before arrival
- Adjust timing based on traffic
- Skip automation if running late

### Multi-person logic

Different behaviors based on who's home:

{% raw %}
```yaml
condition:
  # If just kids home
  - condition: template
    value_template: >
      {{ is_state('person.parent1', 'not_home') and
         is_state('person.parent2', 'not_home') and
         is_state('person.kid', 'home') }}
action:
  # Enable kid-specific rules
```
{% endraw %}

---

## Best Practices

### Start conservative

**Initial Setup:**
- Longer delays (15 minutes)
- Multiple verification methods
- Manual override always available
- Conservative geofence radius

**Then Refine:**
- Gradually reduce delays
- Remove unnecessary verifications
- Expand automation actions
- Adjust geofence as needed

### Notification strategy

**Always Notify For:**
- Away mode activation
- Door auto-unlock
- Security state changes
- Unusual presence patterns

**Optional Notifications:**
- Someone arrived home
- Someone left home
- Mode changes

### Fail-safe design

**When Uncertain:**
- Don't activate away mode
- Don't unlock doors
- Don't change security state
- Better safe than automated

**Manual Override:**
- Physical controls always work
- App manual mode toggle
- Voice command override
- Automation disable switch

### Testing protocol

**Before Trusting:**
1. Test for 2 weeks with notifications only
2. Review all triggers and false positives
3. Add verification conditions
4. Enable actions gradually
5. Monitor for another week
6. Fine-tune based on real usage

---

## Additional presence & mode ideas

### Guest mode

Create a special mode when guests are staying:

* Disable bedroom automation
* Keep bathroom lights at higher brightness at night
* Extend "away" timing before activating (guests may not have app)
* Provide simple physical controls

### Vacation mode

Extended away period with extra security:

* Random light patterns to simulate presence
* More aggressive energy savings
* Enhanced security monitoring
* Pause routine notifications
* Hold mail/package delivery alerts

### Work from home mode

Optimize for home office use:

* Keep office well-lit during work hours
* Adjust thermostat for productivity
* Enable focus mode (minimize notifications)
* Disable daytime vacuum routines

### Sleep mode vs. night mode

Differentiate between being awake at night and sleeping:

**Night Mode** (10 PM - 11 PM)
* Lights still functional at low brightness
* Can watch TV, read, etc.
* Motion sensors active but dimmed

**Sleep Mode** (11 PM - 6 AM)
* Minimal automation
* Very low light levels only
* Most sensors passive

---

## Best practices (continued)

### Presence detection accuracy

**Multiple Data Points:**
Don't rely on GPS alone. Combine with:
* Motion sensors
* Device activity (TV, lights manually controlled)
* Time of day patterns
* Door lock status

**Arrival Delays:**
* Add 20-30 second delay before triggering
* Prevents false triggers from GPS drift
* Allows time to actually arrive home

**Departure Delays:**
* Wait 10 minutes after last phone leaves
* Check for motion during that time
* Confirm all departure conditions met

### Zone-based presence

Create zones around your home:

* **Home Zone** - 50-100 meter radius
* **Away Zone** - Outside home zone
* **Approaching Zone** - 200-500 meters (optional)
  - Pre-heat/cool home
  - Turn on exterior lights
  - Prepare arrival routine

### Handling edge cases

**Dead Phone Battery:**
* Manual override buttons
* Alternative triggers (door unlock, motion)
* Grace period before full Away Mode

**Left Phone at Home:**
* Additional motion/activity checks
* Time-based overrides
* Physical controls remain functional

**Guest Without App:**
* Extended motion detection windows
* Manual mode toggles
* Guest mode that disables aggressive automation

<div class="page-navigation">
  <a href="/automation/lighting/">← Previous: Lighting</a>
  <a href="/automation/climate/">Next: Climate →</a>
</div>
