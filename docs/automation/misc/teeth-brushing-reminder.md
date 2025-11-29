---
layout: default
title: Remind Kids to Brush Teeth - Automated Tooth Brushing Detection
description: Smart home automation to remind kids to brush their teeth if they forget. Uses power monitoring to detect electric toothbrush usage.
keywords: toothbrush reminder, kids automation, teeth brushing, power monitoring, parenting automation, bedtime routine, smart parenting
---

# Remind kids to brush teeth if they forgot

Instead of chasing the kids before bedtime to make sure they brush their teeth, let's make the smart home do it for us. That way we as parents don't have to be the bad guy since we're not the ones telling the kids to brush.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Bedtime Routine</h4>
    <ul>
      <li><strong>Evening Reminder</strong> - Announce reminder if teeth not brushed by 9 PM</li>
      <li><strong>Consistent Habits</strong> - Build routine without nagging</li>
      <li><strong>Parent Relief</strong> - Smart home is the "bad guy" instead of you</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Morning Routine</h4>
    <ul>
      <li><strong>Morning Reminder</strong> - Before school reminder if not brushed</li>
      <li><strong>Tracking</strong> - Know if kids actually brushed</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Electric Toothbrush (any brand)</strong>
      <div class="product-details">
        Oral-B, Sonicare, or any rechargeable electric toothbrush<br>
        Must be charged via plug (not battery-only)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Power Metering Smart Plug</strong>
      <div class="product-details">
        TP-Link Kasa, Shelly, or any plug with power monitoring<br>
        Detects when toothbrush is placed back on charger
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart Speaker/Music System or Voice Assistant</strong>
      <div class="product-details">
        For announcing reminders<br>
        Amazon Echo, Google Home, Sonos, etc.
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 How It Works</strong>
  <p>The electric toothbrush charger is plugged into the smart plug. When the child brushes their teeth and returns the toothbrush to its charging base, the power consumption increases as the charger begins recharging the depleted battery. The smart plug detects this power spike (typically from near-zero to 2-5 watts), which tells your automation that the toothbrush was just used.</p>
</div>

## Basic automation setup

<div class="automation-example">IF time is between 8:00 - 10:00 PM
AND toothbrush NOT used in last 2 hours
THEN announce "It's time to brush your teeth, kids!"</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Step 1: Detect Toothbrush Usage</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Plug's power consumption rises above 2 watts</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>None - we want to track all usage</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Set variable "toothbrush_last_used" to current time</li>
      <li>OR Turn on virtual switch "Teeth Brushed Today"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 2: Evening Reminder</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 8:30 PM (or your chosen reminder time)</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Toothbrush power hasn't risen above 2 watts since 6:00 PM</li>
      <li>OR "Teeth Brushed Today" switch is OFF (reset at 6 PM)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Announce over the speakers: "It's time to brush your teeth, kids!"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 3: Reset Daily</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 6:00 PM (before bedtime routine)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Turn OFF "Teeth Brushed Today" switch</li>
      <li>Reset tracking variable</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Create input_boolean: "teeth_brushed_evening"</li>
      <li>Automation 1: Power > 2W between 6 PM-10 PM → Turn on helper</li>
      <li>Automation 2: At 8:30 PM if helper off → TTS announcement</li>
      <li>Automation 3: At 6 PM → Reset helper to off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Create virtual switch "Teeth Brushed"</li>
      <li>Routine 1: Power > 2W between 6-10 PM → Switch on</li>
      <li>Routine 2: 8:30 PM + Switch off → Speaker announcement</li>
      <li>Routine 3: 6 PM → Switch off (reset)</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Create virtual switch for tracking</li>
      <li>Rule Machine: Power trigger with time window</li>
      <li>Scheduled reminder if switch not set</li>
      <li>Daily reset automation</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>Create virtual switch via Homebridge or HomePod</li>
      <li>Automation: Power rises → Switch on</li>
      <li>Time-based reminder automation if switch off</li>
      <li>Scheduled reset</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>Create virtual switch via SmartThings</li>
      <li>Routine 1: Power > 2W → Switch on</li>
      <li>Routine 2: Time 8:30 PM + Switch off → Alexa says reminder</li>
      <li>Routine 3: 6 PM → Switch off</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Limited native power monitoring</li>
      <li>Use Home Assistant or Hubitat for logic</li>
      <li>Trigger Google Home speaker for announcement</li>
    </ol>
  </div>
</div>

## Advanced features

### Multiple reminder levels

Escalate reminders if not acted upon:

**Level 1 (8:00 PM):**
- Gentle announcement: "Remember to brush your teeth tonight!"

**Level 2 (8:30 PM):**
- More direct: "It's time to brush your teeth, kids!"

**Level 3 (9:00 PM):**
- Urgent: "Brushing teeth required before screen time!"
- Optionally pause TV/gaming until brushed

### Multi-child tracking

Track each child separately:

**Setup:**
- Separate toothbrush per child (different charger locations)
- Separate smart plug per toothbrush
- Individual tracking switches

**Personalized Reminders:**
- "Emma, time to brush your teeth!"
- "Jack, you still need to brush!"

### Morning routine integration

Track morning brushing too:

**Morning Tracking (6-9 AM):**
- Detect morning toothbrush usage
- Reminder at 7:30 AM if not used
- Different announcement: "Brush teeth before leaving for school!"

**Reset Logic:**
- Evening tracking: Reset at 6 PM
- Morning tracking: Reset at 6 AM

### Reward system integration

Gamify the process:

**Tracking:**
- Count consecutive days of brushing
- Log brushing times
- Weekly/monthly streaks

**Rewards:**
- Dashboard showing streak
- Special announcement for milestones
- Integration with reward chart

### Screen time gating

Tie brushing to privileges:

**Logic:**
- TV/gaming only available if teeth brushed
- Smart plug on entertainment controlled by brushing status
- Turns off at 9 PM regardless

**Setup:**
1. Teeth brushed → Enable entertainment plug
2. 9 PM → Disable entertainment plug
3. Next day → Repeat

## Troubleshooting

### Issue: Charger always draws power

**Causes:**
- Toothbrush charger has constant standby power
- Power detection threshold too low
- Charger design varies by model

**Solutions:**
✅ Measure baseline power with toothbrush NOT on charger
✅ Measure power WITH toothbrush on charger (charging)
✅ Set threshold between these values
✅ Some chargers only draw power when toothbrush is actively charging

### Issue: Multiple false positives

**Causes:**
- Charger power fluctuates
- Threshold too sensitive
- Toothbrush replaced on charger multiple times

**Solutions:**
✅ Add debounce: Only trigger once per time window
✅ Increase power threshold
✅ Add cooldown: Ignore triggers for 30 minutes after first detection
✅ Focus on first detection in window only

### Issue: Reminder announces when kids already brushed

**Causes:**
- Power detection missed
- Switch didn't set
- Timing window issue

**Solutions:**
✅ Verify power monitoring is working
✅ Check automation logs
✅ Adjust time window for tracking
✅ Lower power detection threshold

### Issue: Toothbrush used but power doesn't spike

**Causes:**
- Toothbrush fully charged (minimal draw)
- Charger design doesn't show usage
- Wrong plug or device monitored

**Solutions:**
✅ Test when toothbrush is partially discharged
✅ Try different toothbrush model
✅ Use vibration sensor as alternative
✅ Manual button press option as backup

## Best practices

### Age-appropriate messaging

**Younger Kids (5-8):**
- Fun, encouraging tone
- "Time for sparkly teeth!"
- Consider character voices if available

**Older Kids (9-12):**
- Matter-of-fact reminders
- "Teeth brushing time"
- Don't be too cutesy

**Teenagers:**
- Simple notifications
- Optional: Skip audio, use phone notification
- Respect independence

### Timing considerations

**Window, Not Single Time:**
- Allow flexibility in brushing time
- Remind only if NOT brushed in reasonable window
- 8:00-9:30 PM is reasonable evening window

**Avoid:**
- Reminding too early (annoying)
- Reminding too late (already in bed)
- Multiple rapid reminders

### Positive reinforcement

**Focus on Success:**
- "Great job brushing your teeth!" when detected
- Streak tracking and celebration
- Avoid negative messaging

**Avoid:**
- Shaming or guilt-tripping
- Constant nagging
- Punitive automation

---

**Related automations:**
- [Baby sleep mode](/automation/misc/baby-sleep-mode/)
- [Morning routine](/automation/presence/morning-routine/)
- [Bedtime routine](/automation/presence/bedtime-routine/)

<div class="page-navigation">
  <a href="/automation/misc/">← Back to Misc Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
