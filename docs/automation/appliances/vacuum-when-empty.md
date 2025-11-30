---
layout: automation
title: Robot Vacuum Only When Empty - Smart Cleaning Automation
description: Start your robot vacuum only when the house is truly empty and finish before anyone returns. Smart presence-based cleaning automation.
keywords: robot vacuum automation, smart vacuum scheduling, presence-based cleaning, roomba automation, robot vacuum when away, automatic vacuum, smart home cleaning
---

# Robot vacuum only when house is empty

Make your robot vacuum truly smart by only running when the house is completely empty and ensuring it finishes before anyone returns. No more vacuums running underfoot or startling pets.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Convenience benefits</h4>
    <ul>
      <li><strong>Out of the way</strong> - Vacuum runs while you're at work</li>
      <li><strong>No pet stress</strong> - Pets aren't home to be scared</li>
      <li><strong>Quiet home</strong> - Never hear the vacuum running</li>
      <li><strong>Always clean</strong> - Come home to freshly cleaned floors</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Smart scheduling</h4>
    <ul>
      <li><strong>Presence-aware</strong> - Only when truly empty</li>
      <li><strong>Return estimation</strong> - Finishes before you're back</li>
      <li><strong>Skip when needed</strong> - Doesn't run on work-from-home days</li>
      <li><strong>Guest awareness</strong> - Skips when guests are visiting</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart robot vacuum</strong>
      <div class="product-details">
        Popular brands: iRobot Roomba, Roborock, Ecovacs Deebot, Shark<br>
        Must support smart home integration (WiFi, app control)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Presence detection</strong>
      <div class="product-details">
        Options: Phone GPS/geofencing, Life360, smart home presence<br>
        Must track all household members accurately
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Calendar integration</strong>
      <div class="product-details">
        Connect to work calendars to predict return times
      </div>
    </div>
    
    <div class="product-item">
      <strong>Self-emptying base</strong>
      <div class="product-details">
        Vacuum can run longer cleaning cycles without manual bin emptying
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Cleaning time estimation</strong>
  <ul>
    <li>Most robot vacuums clean 1,000 sq ft in 60-90 minutes</li>
    <li>Factor in return-to-dock time (5-10 minutes)</li>
    <li>Add buffer time for unexpected obstacles</li>
    <li>Consider if vacuum needs to empty mid-cycle</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF last person leaves home
AND time is after 9:00 AM (everyone should be gone for work)
AND vacuum hasn't run today
AND estimated return is more than 2 hours away
THEN wait 10 minutes (confirm everyone really left)
THEN start robot vacuum

IF anyone arrives home
AND vacuum is running
THEN send vacuum to dock immediately</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Home mode changes to "Away" (last person left)</li>
      <li>OR scheduled time when typically away (backup)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Time:</strong> After 9 AM (avoid early morning false triggers)<br>
    <strong>Day:</strong> Weekdays only, or specific days of week<br>
    <strong>Already ran:</strong> Vacuum hasn't run today<br>
    <strong>Duration:</strong> Expected away time > cleaning time + buffer<br>
    <strong>Guest mode:</strong> No guests present
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Wait 10 minutes (confirm departure is real)</li>
      <li>Verify still in Away mode</li>
      <li>Start robot vacuum cleaning cycle</li>
      <li>Send notification: "Vacuum started cleaning"</li>
      <li>Mark that vacuum ran today (prevent duplicate runs)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Return protection</h4>
    <ul>
      <li>When anyone enters home zone, check if vacuum is running</li>
      <li>If running, send vacuum to dock immediately</li>
      <li>Notify: "Vacuum returning to dock - you're home early"</li>
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
        <span class="step-content">Zone.home person count changes to 0</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time after 9 AM, weekday, vacuum not run today</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Delay 10 min, verify empty, vacuum.start</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use input_boolean.vacuum_ran_today to track daily runs
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
        <span class="step-content">Everyone leaves (location mode Away)</span>
      </div>
      <div class="platform-step">
        <span class="step-label">AND</span>
        <span class="step-content">Time between 9 AM - 5 PM on weekdays</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Wait 10 min, start robot vacuum</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use iRobot or Roborock SmartThings integration
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
        <span class="step-content">Mode changes to Away</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time after 9 AM, day is weekday</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Wait 10 min, start vacuum via integration</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use community Roomba or Roborock driver
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
        <span class="step-content">Last person leaves home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time is after 9:00 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Start vacuum via Homebridge/HomePod shortcut</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> May need Homebridge plugin for vacuum integration
        </div>
      </div>
    </div>
  </div>
  
  <div class="platform-card">
    <div class="platform-card-header">
      <img src="/assets/img/logos/alexa.png" alt="Amazon Alexa logo">
      <h4>Alexa</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">When</span>
        <span class="step-content">Location: Everyone leaves</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Time between 9 AM - 5 PM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Wait 10 min, start iRobot Roomba</span>
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
        <span class="step-label">Starter</span>
        <span class="step-content">Everyone leaves home</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">Weekday, after 9 AM</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Start vacuum via Google Home integration</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Vacuum must have Google Home integration
        </div>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Smart return estimation</h3>
    <p>Predict when to stop cleaning:</p>
    <ul>
      <li>Check calendar for meeting end times</li>
      <li>Track typical commute duration</li>
      <li>Monitor phone location distance from home</li>
      <li>Stop cleaning when anyone is 20 minutes away</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Room-by-room scheduling</h3>
    <p>Clean different areas on different days:</p>
    <ul>
      <li><strong>Monday/Thursday:</strong> Living room and kitchen</li>
      <li><strong>Tuesday/Friday:</strong> Bedrooms and hallways</li>
      <li><strong>Wednesday:</strong> Bathrooms and entryway</li>
      <li><strong>Weekend:</strong> Full house deep clean if away</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Completion notification</h3>
    <p>Know when cleaning is done:</p>
    <ul>
      <li>Notification when vacuum returns to dock</li>
      <li>Report on area cleaned and duration</li>
      <li>Alert if vacuum got stuck or needs attention</li>
      <li>Reminder if bin needs emptying</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Vacuum starts when someone's home</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Presence detection falsely reported everyone away.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add 10-15 minute delay before starting</li>
        <li>Re-check presence status after delay</li>
        <li>Use multiple presence detection methods</li>
        <li>Add manual override button to cancel</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Vacuum still running when you arrive</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Came home early and vacuum is still cleaning.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add "return protection" automation to dock vacuum on arrival</li>
        <li>Send vacuum to dock when anyone enters home zone</li>
        <li>Use location-based trigger when 10-15 min away</li>
        <li>Voice command: "Stop the vacuum"</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Vacuum runs multiple times per day</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Every time someone leaves and returns, vacuum starts again.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Track if vacuum already ran today (input_boolean)</li>
        <li>Reset "ran today" flag at midnight</li>
        <li>Add condition: only run if last run was > 20 hours ago</li>
        <li>Limit to specific time window (9 AM - 2 PM)</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Doesn't run on work-from-home days</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Vacuum never runs when working from home.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Add manual trigger: "Run the vacuum" voice command</li>
        <li>Schedule specific rooms while in another part of house</li>
        <li>Create "WFH mode" that runs vacuum during lunch hour</li>
        <li>Use weekend for full-house cleaning</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="best-practice-card">
  <h3>Setting up smart vacuum scheduling</h3>
  <ol>
    <li>Track presence for all household members</li>
    <li>Add 10-15 minute delay after departure</li>
    <li>Re-verify empty status before starting</li>
    <li>Create "return protection" to dock on arrival</li>
    <li>Track daily runs to prevent duplicates</li>
    <li>Include manual trigger for work-from-home days</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>No departure buffer</strong> - Quick trips will trigger vacuum</li>
    <li><strong>No return protection</strong> - Vacuum still running when you get home</li>
    <li><strong>Running during sleep</strong> - Add time restrictions</li>
    <li><strong>Ignoring pets</strong> - Pets may be home alone and stressed by vacuum</li>
  </ul>
</div>

---

**Related automations:**
- [Robot vacuum auto start](/automation/appliances/robot-vacuum-auto-start/)
- [Away mode](/automation/daily-routines/away-mode/)
- [Morning routine](/automation/daily-routines/morning-routine/)

<div class="page-navigation">
  <a href="/automation/appliances/">← Back to Appliances</a>
  <a href="/automation/">View All Automations →</a>
</div>
