---
layout: default
title: Garbage Day Reminder - Dashboard Automation
description: Create a dashboard tile that reminds you to take out the trash. The tile turns red until the task is complete.
keywords: garbage reminder, trash day, dashboard automation, virtual switch, weekly reminder, smart home dashboard
---

# Garbage day reminder

This is a great way to remember to take out the trash before garbage day. The tile on the dashboard lights up red, so you know you have a task to complete. Once you are done, simply click the tile to turn it back green. This indicates you have completed the task.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Weekly reminders</h4>
    <ul>
      <li><strong>Garbage Day</strong> - Take out the trash before collection</li>
      <li><strong>Recycling Day</strong> - Sort and put out recycling</li>
      <li><strong>Yard Waste</strong> - Seasonal collection reminders</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Other scheduled tasks</h4>
    <ul>
      <li><strong>Water Plants</strong> - Weekly or bi-weekly reminders</li>
      <li><strong>Pet Care</strong> - Medication or grooming reminders</li>
      <li><strong>Filter Changes</strong> - HVAC or water filter reminders</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Dashboard</strong>
      <div class="product-details">
        Wall-mounted tablet or phone dashboard<br>
        SharpTools, Home Assistant, Hubitat Dashboard, or ActionTiles
      </div>
    </div>
    
    <div class="product-item">
      <strong>Virtual Switch or Variable</strong>
      <div class="product-details">
        Created in your smart home platform to track task status
      </div>
    </div>
  </div>
</div>

## Basic automation setup

<div class="automation-example">IF it is Wednesday at 6:00 PM
THEN turn on "Garbage Out" virtual switch
(tile turns red on dashboard)</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Every Wednesday at 6:00 PM (adjust for your garbage day)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <ul>
      <li>None</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Turn on the virtual switch or variable</li>
    </ul>
  </div>
</div>

## Dashboard tile setup

1. Create a virtual switch named "Garbage Out"
2. Add tile to dashboard linked to the virtual switch
3. Configure tile colors:
   - **OFF state (green):** Task completed or not due
   - **ON state (red):** Garbage needs to go out
4. When you complete the task, tap the tile to turn it green

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Create input_boolean helper "garbage_out"</li>
      <li>Time trigger: Wednesday at 6:00 PM</li>
      <li>Action: Turn on input_boolean.garbage_out</li>
      <li>Add button card to dashboard with color conditions</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Create virtual switch "Garbage Out"</li>
      <li>Create routine: Time is Wednesday 6 PM</li>
      <li>Action: Turn on virtual switch</li>
      <li>Add to SharpTools dashboard with colors</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Create virtual switch "Garbage Out"</li>
      <li>Use Simple Automation Rules for time trigger</li>
      <li>Add to Hubitat Dashboard with templates</li>
      <li>Configure ON/OFF colors</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SharpTools</h4>
    <ol>
      <li>Link virtual switch from your hub</li>
      <li>Add Hero tile to dashboard</li>
      <li>Configure "Active" color as red</li>
      <li>Configure "Inactive" color as green</li>
    </ol>
  </div>
</div>

## Advanced features

### Calendar integration

You can take this to a new level if you integrate with the garbage company's service calendar. That way you don't falsely get a reminder on holidays when no garbage is being picked up. Also, if there's a change in schedule due to weather your smart home adapts accordingly.

**Implementation options:**
- **ICS calendar import:** Many garbage companies provide ICS calendar feeds you can subscribe to
- **Custom integration:** Some regions have community-built integrations (check Home Assistant Community Store)
- **Manual calendar:** Create a Google/Apple calendar with your garbage schedule and check it as a condition
- **API integration:** Some waste management companies offer APIs for service schedules

### Multiple bins

Create separate virtual switches for different collection types:

- **Trash:** Every week (e.g., Wednesday)
- **Recycling:** Every two weeks or different day
- **Yard Waste:** Seasonal schedule
- **Bulk Pickup:** Monthly or on-demand

### Auto-reset

Reset the reminder automatically after garbage is collected:

**Triggers:**
- Time is Thursday at 10:00 AM (after collection)

**Actions:**
- Turn off "Garbage Out" virtual switch

## Troubleshooting

### Issue: Reminder at wrong time

**Solutions:**
✅ Verify your hub's time zone settings
✅ Check daylight saving time adjustments
✅ Use local time, not UTC

### Issue: Tile doesn't change color

**Solutions:**
✅ Verify virtual switch is properly linked to tile
✅ Check dashboard tile color settings
✅ Refresh dashboard if using cached view

### Issue: Forgot to tap tile after completing task

**Solutions:**
✅ Add auto-reset automation as described above
✅ Use NFC tag at trash cans to automatically complete
✅ Create voice command: "Alexa, garbage is out"

---

**Related automations:**
- [Status tiles instead of notifications](/automation/notifications/status-tiles.html)
- [Music controls](/automation/notifications/music-controls.html)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
