---
layout: automation
title: Pet Feeding Reminder - Smart Home Pet Care
description: Never forget to feed your pets with automated feeding reminders. Time-based notifications and smart feeder integration for consistent pet care.
keywords: pet feeding reminder, dog feeding notification, cat feeding alert, smart pet care, automatic feeding reminder, pet schedule automation
---

# Pet feeding reminder

The cat circles the kitchen, eyeing you with that particular look. But who fed her this morning? With multiple people in the house, it is easy to lose track - or worse, to feed her twice and then wonder why she seems unwell. A simple tracker notes when the bowl is filled, and a reminder arrives if the hour grows late without anyone tending to the task.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Feeding consistency</h4>
    <ul>
      <li><strong>Busy mornings</strong> - Don't forget to feed before rushing out</li>
      <li><strong>Multiple people</strong> - Coordinate who feeds to avoid double-feeding</li>
      <li><strong>Medication timing</strong> - Ensure meds are given with food on schedule</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Household coordination</h4>
    <ul>
      <li><strong>Kids helping</strong> - Remind children of their pet care responsibilities</li>
      <li><strong>Traveling</strong> - Remind pet sitter of feeding times</li>
      <li><strong>Work from home</strong> - Easy to lose track of time</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Basic setup (reminders only)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart home platform</strong>
      <div class="product-details">
        Any platform with time-based automation and notifications<br>
        Home Assistant, SmartThings, Hubitat, or even phone reminders
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Enhanced setup (tracking completion)</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart pet feeder</strong>
      <div class="product-details">
        Brands: PetSafe, Petlibro, WOpet, Sure Petcare<br>
        Features: WiFi, portion control, feeding logs
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart button</strong>
      <div class="product-details">
        Brands: Flic, Aqara, SmartThings Button<br>
        Press to confirm feeding (for manual feeders)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Contact sensor on food container</strong>
      <div class="product-details">
        Detect when food container is opened<br>
        Auto-track feeding without button press
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Smart feeder vs. reminder</strong>
  <ul>
    <li><strong>Smart auto-feeder:</strong> Dispenses food automatically at set times - no reminder needed</li>
    <li><strong>Reminder automation:</strong> For wet food, special diets, or when you prefer manual feeding</li>
    <li><strong>Combination:</strong> Auto-feeder for dry food, reminders for wet food supplements</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF time is 7:00 AM
AND pet not fed yet today (optional tracking)
THEN send notification "Time to feed the pets"
AND announce on kitchen speaker</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Automation 1: Morning feeding reminder</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 7:00 AM (adjust to your schedule)</li>
    </ul>
    <h4>Conditions (optional)</h4>
    <ul>
      <li>Pets not fed today (if tracking)</li>
      <li>Someone is home</li>
      <li>Not vacation mode</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Time to feed Max and Luna!"</li>
      <li>Announce on kitchen speaker</li>
      <li>Optional: Flash kitchen lights</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Automation 2: Evening feeding reminder</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Time is 6:00 PM</li>
    </ul>
    <h4>Conditions</h4>
    <ul>
      <li>Morning feeding confirmed (if tracking)</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "Time for evening feeding"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Automation 3: Mark as fed (with button)</h4>
    <h4>Triggers</h4>
    <ul>
      <li>Smart button pressed</li>
      <li>OR Food container contact sensor opened</li>
    </ul>
    <h4>Actions</h4>
    <ul>
      <li>Set helper variable "pet_fed_today" to true</li>
      <li>Send confirmation: "Feeding logged for Max and Luna"</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
      <h4>Home Assistant</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Time is 7:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">input_boolean.pets_fed_morning is off</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">notify.mobile_app + tts.speak on kitchen speaker</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Create input_boolean to track feeding status, reset at midnight
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
      <h4>SmartThings</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">IF</span>
        <span class="step-content">Time is 7:00 AM every day</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Send push notification to all members</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Optional:</strong> Use virtual switch to track feeding status
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
      <h4>Hubitat</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Time is 7:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Virtual switch "Pets Fed" is off</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send push notification + speak on device</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine with virtual switches
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
      <h4>Apple HomeKit</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Time of day is 7:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Send notification</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Limited native tracking; use Shortcuts for complex logic
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Alexa logo">
      <h4>Alexa</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Schedule: 7:00 AM every day</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send notification + announce on Echo devices</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Say "Alexa, pets are fed" to log via voice
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/google.png" alt="Google Home logo">
      <h4>Google Home</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Schedule: 7:00 AM daily</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Announce on Nest speakers</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Say "Hey Google, mark pets as fed"
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Feeding status tracking</h3>
    <p>Track whether feeding has occurred:</p>
    <ul>
      <li><strong>Button press:</strong> Physical confirmation</li>
      <li><strong>Food container sensor:</strong> Automatic detection</li>
      <li><strong>Smart feeder integration:</strong> Feeder reports feeding</li>
      <li><strong>Voice command:</strong> "Pets are fed"</li>
      <li><strong>Dashboard display:</strong> Visual status indicator</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Escalating reminders</h3>
    <p>Persistent reminders if feeding is missed:</p>
    <ul>
      <li><strong>First reminder:</strong> 7:00 AM - Standard notification</li>
      <li><strong>Second reminder:</strong> 7:30 AM - "Pets still waiting for breakfast!"</li>
      <li><strong>Third reminder:</strong> 8:00 AM - High priority + voice announcement</li>
      <li><strong>Final reminder:</strong> 8:30 AM - Alert all family members</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Multi-pet management</h3>
    <p>Track different pets with different schedules:</p>
    <ul>
      <li>Separate tracking per pet</li>
      <li>Different feeding times (e.g., puppy needs 3x daily)</li>
      <li>Medication reminders tied to specific pets</li>
      <li>Special diet notifications</li>
    </ul>
  </div>
</div>

<div class="feature-grid">
  <div class="feature-card">
    <h3>Dashboard status tile</h3>
    <p>Visual feeding status:</p>
    <ul>
      <li>Morning fed: ✅ / ❌</li>
      <li>Evening fed: ✅ / ❌</li>
      <li>Last fed time displayed</li>
      <li>Days since last medication (if applicable)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Family coordination</h3>
    <p>Prevent double-feeding:</p>
    <ul>
      <li>Announce to household when fed: "Pets have been fed by Mom"</li>
      <li>Show feeding status prominently on dashboard</li>
      <li>Ask for confirmation before second feeding</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Reminder comes too early/late</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Feeding time doesn't match your schedule.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Adjust reminder time to match your routine</li>
        <li>Create weekday vs. weekend schedules</li>
        <li>Tie to motion sensor (when you wake up)</li>
        <li>Link to morning routine trigger</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Pet gets fed twice</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Multiple family members feeding because they don't know it's done.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Implement feeding tracking with confirmation</li>
        <li>Announce to whole house when fed</li>
        <li>Show status on kitchen dashboard</li>
        <li>Visual indicator (physical sign or smart display)</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Reminder when already fed</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Getting reminders even after feeding.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add feeding tracking via button or sensor</li>
        <li>Add condition to check if fed before reminding</li>
        <li>Use snooze action on notification</li>
        <li>Voice command to cancel reminder</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Tracking not resetting</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Fed status stays "fed" and reminders never trigger.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Create automation to reset status at midnight</li>
        <li>Reset both morning and evening trackers</li>
        <li>Verify reset automation is running</li>
        <li>Check for automation errors in logs</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

### Timing feeding reminders

**Morning feeding:**
- Set for when you typically wake up
- Give 15-30 minutes buffer before you need to leave
- Weekend schedule may differ from weekdays

**Evening feeding:**
- Set for when you typically get home
- Or when dinner prep usually starts
- Consistent time helps pet's digestion

### Tracking methods comparison

**Smart button (manual):**
- Simple and reliable
- Requires remembering to press
- Works for any feeding type

**Food container sensor:**
- Automatic detection
- Only works for dry food container
- May miss wet food from fridge

**Smart feeder integration:**
- Fully automatic
- Only for compatible feeders
- Best for dry food automation

### Pet-specific considerations

**Dogs:**
- Usually 1-2 meals per day
- More flexible timing
- Consider medication with meals

**Cats:**
- Often prefer smaller, frequent meals
- Timed feeder works well for dry food
- Reminder for daily wet food supplement

**Multiple pets:**
- Track each pet separately if different schedules
- Consider slow feeder bowls for fast eaters
- Monitor that each pet eats their own food

---

**Related automations:**
- [Morning routine automation](/automation/daily-routines/morning-routine.html)
- [Garbage day reminder](/automation/notifications/garbage-day-reminder.html)
- [Low battery alerts](/automation/notifications/low-battery-alerts.html)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
