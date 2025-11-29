---
layout: default
title: Status Tiles Instead of Notifications - Dashboard Automation
description: Use dashboard status tiles for persistent reminders instead of phone notifications. See appliance status, door states, and delivery alerts at a glance.
keywords: dashboard tiles, status tiles, smart home dashboard, appliance status, persistent notifications, visual alerts
---

# Status tiles instead of notifications

It's easy to ignore or forget notifications sent to your phone. Also, they don't keep reminding you once you've seen or dismissed them. Status tiles on a dashboard located in a place you often see solves that problem.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Appliance Status</h4>
    <ul>
      <li><strong>Washer Done</strong> - Time to put clothes in the dryer</li>
      <li><strong>Dishwasher Clean</strong> - Ready to be emptied</li>
      <li><strong>Dryer Done</strong> - Clothes ready to fold</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Home Awareness</h4>
    <ul>
      <li><strong>Doors/Windows Open</strong> - Know before leaving the house</li>
      <li><strong>Delivery Waiting</strong> - Package on porch to bring in</li>
      <li><strong>Robot Vacuum</strong> - Scheduled to run, time to tidy up</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Tablet</strong>
      <div class="product-details">
        Any tablet you prefer (Amazon Fire tablets are an affordable option)<br>
        Wall-mounted in high-traffic area
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dashboard Software</strong>
      <div class="product-details">
        SharpTools, Home Assistant Lovelace, Hubitat Dashboard, or ActionTiles
      </div>
    </div>
    
    <div class="product-item">
      <strong>Virtual Switches</strong>
      <div class="product-details">
        One for each status you want to track
      </div>
    </div>
  </div>
</div>

## Basic automation setup

Any automation where you send a notification, consider using a dashboard tile instead. You can do that by using either a virtual switch or variable.

<div class="automation-example">IF washer is done
THEN set "Washer Done" switch ON
(tile shows red until clothes moved)

IF dryer door opens
THEN set "Washer Done" switch OFF
(tile returns to normal)</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Step 1: Create virtual switch</h4>
    <ul>
      <li>Name it descriptively (e.g., "Washer Needs Attention")</li>
      <li>Add to dashboard with appropriate colors</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 2: Set switch ON when attention needed</h4>
    <ul>
      <li>Trigger from the event that needs attention</li>
      <li>Turn on the virtual switch</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Step 3: Set switch OFF when resolved</h4>
    <ul>
      <li>Trigger from the resolution action</li>
      <li>Turn off the virtual switch</li>
    </ul>
  </div>
</div>

## Status tile examples

### Washer/Dryer status

- Create virtual switch for each appliance
- Turn on when cycle completes (power monitoring)
- Turn off when door opens or manually tapped

### Door/Window status

- Show all open doors/windows
- Glanceable before leaving house
- No action needed - just informational

### Delivery status

- Turn on when package detected on porch (camera or motion sensor)
- Turn off when front door opens (brought in)
- Persistent until addressed

### Robot vacuum schedule

- Show when vacuum will run today
- Reminder to tidy up before it starts
- Countdown to scheduled run

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Create input_boolean for each status</li>
      <li>Use automations to toggle based on events</li>
      <li>Add conditional cards to Lovelace dashboard</li>
      <li>Use card-mod for custom colors</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>Create virtual switches for each status</li>
      <li>Use routines to toggle on events</li>
      <li>Display in SharpTools with color rules</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Create virtual switches</li>
      <li>Use Rule Machine for complex logic</li>
      <li>Add to Hubitat Dashboard with templates</li>
      <li>Configure state-based colors</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SharpTools</h4>
    <ol>
      <li>Link virtual switches from hub</li>
      <li>Use Hero tiles for visibility</li>
      <li>Configure Active/Inactive colors</li>
      <li>Group related tiles together</li>
    </ol>
  </div>
</div>

## Why tiles beat notifications

| Notifications | Dashboard Tiles |
|---------------|-----------------|
| Can be dismissed and forgotten | Persistent until addressed |
| Individual to one person | Visible to whole household |
| Interrupt what you're doing | Glanceable at your convenience |
| No ongoing reminder | Always visible status |
| Easy to miss | Hard to miss in high-traffic area |

## Advanced features

### Priority-based colors

Use a color system to indicate urgency:

- **Green:** All good, no action needed
- **Yellow:** Attention needed soon (informational)
- **Red:** Urgent, needs immediate attention
- **Blue:** In progress or running

### Escalating alerts

If a status tile stays red too long, add additional alerts:

1. **0-30 min:** Red tile only
2. **30 min - 2 hours:** Add flashing or notification
3. **2+ hours:** Add voice announcement

### Auto-reset

Some status tiles should reset automatically:

- **Time-based:** Reset at midnight if not addressed
- **Event-based:** Reset when related event occurs (door opens, motion detected)
- **Manual:** Require tap to reset (for important items)

## Troubleshooting

### Issue: Tile not updating

**Solutions:**
✅ Check virtual switch is properly linked
✅ Verify automation is firing (check logs)
✅ Refresh dashboard browser/app
✅ Check hub connectivity

### Issue: Too many tiles clutter dashboard

**Solutions:**
✅ Group related items on separate screen
✅ Use conditional visibility (only show when active)
✅ Prioritize most important status items
✅ Create summary tile that shows count of issues

### Issue: Family ignores tiles

**Solutions:**
✅ Place dashboard in high-traffic area
✅ Use motion sensor to wake screen when approaching
✅ Add audio alerts for critical items
✅ Make tiles actionable (tap to dismiss)

---

**Related automations:**
- [Garbage day reminder](/automation/notifications/garbage-day-reminder.html)
- [Music controls](/automation/notifications/music-controls.html)
- [Washer done notification](/automation/appliances/washer-done-notification.html)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
