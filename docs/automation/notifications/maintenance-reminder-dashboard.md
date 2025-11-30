---
layout: default
title: Maintenance Reminder Dashboard - Smart Home Notifications
description: Wall-mounted tablet showing days remaining for filters, pool chemicals, and other maintenance tasks. One-tap add to shopping list.
keywords: maintenance reminder, smart home dashboard, filter replacement, pool maintenance, household tasks, shopping list automation, home maintenance tracker
---

# Maintenance reminder dashboard

Keep track of all household maintenance with a wall-mounted tablet that shows days remaining for filters, pool chemicals, and other recurring tasks. One tap adds items to your shopping list when it's time to restock.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Maintenance tracking</h4>
    <ul>
      <li><strong>HVAC filters</strong> - Replace every 30-90 days</li>
      <li><strong>Water filters</strong> - Fridge, whole-house, under-sink</li>
      <li><strong>Pool chemicals</strong> - Weekly chlorine, monthly pH adjusters</li>
      <li><strong>Smoke detector batteries</strong> - Annual replacement</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Convenience features</h4>
    <ul>
      <li><strong>Visual countdown</strong> - See days remaining at a glance</li>
      <li><strong>One-tap shopping</strong> - Add to list with single touch</li>
      <li><strong>Color-coded status</strong> - Green/yellow/red indicators</li>
      <li><strong>Family visibility</strong> - Everyone sees what's needed</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Wall-mounted tablet</strong>
      <div class="product-details">
        Options: Amazon Fire tablet, iPad, Android tablet<br>
        Mount: Wall mount bracket or magnetic mount
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dashboard software</strong>
      <div class="product-details">
        Home Assistant dashboard, Fully Kiosk Browser, ActionTiles, SharpTools<br>
        Displays maintenance counters and status
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Shopping list integration</strong>
      <div class="product-details">
        Todoist, AnyList, OurGroceries, Apple Reminders, Alexa Shopping List<br>
        For one-tap adding items when maintenance is due
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart sensors</strong>
      <div class="product-details">
        Filter pressure sensors, water quality monitors for automatic tracking
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Common maintenance intervals</strong>
  <ul>
    <li><strong>HVAC filter:</strong> 30-90 days (depends on filter type)</li>
    <li><strong>Fridge water filter:</strong> 6 months</li>
    <li><strong>Pool chlorine:</strong> Weekly</li>
    <li><strong>Smoke detector battery:</strong> 12 months</li>
    <li><strong>Water softener salt:</strong> Monthly (varies by usage)</li>
    <li><strong>Vacuum filter/bag:</strong> 1-3 months</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">DASHBOARD DISPLAY:
- Show card for each maintenance item
- Display days remaining with color coding
- Green (>30% time left), Yellow (10-30%), Red (<10%)
- Show "Add to shopping list" button when Red

ONE-TAP ACTION:
IF "Add to list" button tapped
THEN add item to shopping list
AND mark as "ordered/added"
AND optionally reset counter when marked complete</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Dashboard elements</h4>
    <ul>
      <li>Card for each maintenance item</li>
      <li>Days remaining counter</li>
      <li>Progress bar or color indicator</li>
      <li>Last replaced date</li>
      <li>Action buttons (Add to list, Mark complete)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Counter logic</h4>
    <strong>Start date:</strong> When item was last replaced/added<br>
    <strong>Interval:</strong> Days until next replacement needed<br>
    <strong>Days remaining:</strong> Start date + Interval - Today<br>
    <strong>Status:</strong> Green/Yellow/Red based on percentage
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li><strong>Add to list:</strong> Push item to shopping list app</li>
      <li><strong>Mark complete:</strong> Reset counter to full interval</li>
      <li><strong>Snooze:</strong> Delay reminder by X days</li>
      <li><strong>Adjust interval:</strong> Change if replacing more/less often</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Notifications</h4>
    <ul>
      <li>Alert when item reaches Yellow status</li>
      <li>Urgent alert when Red status</li>
      <li>Weekly summary of upcoming maintenance</li>
      <li>Confirmation when item added to shopping list</li>
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
        <span class="step-label">Counters</span>
        <span class="step-content">Use input_datetime for last replaced date per item</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Templates</span>
        <span class="step-content">Calculate days remaining with template sensor</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Dashboard</span>
        <span class="step-content">Lovelace cards with gauge/progress display</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Tip:</strong> Use button card with tap_action to call shopping list service
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
        <span class="step-label">Setup</span>
        <span class="step-content">Use virtual switches for each maintenance item</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Dashboard</span>
        <span class="step-content">SharpTools or ActionTiles for display</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Link to IFTTT or Alexa for shopping list</span>
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
        <span class="step-label">Tracking</span>
        <span class="step-content">Use Hub Variables for dates and intervals</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Dashboard</span>
        <span class="step-content">Hubitat Dashboard or SharpTools</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Rules</span>
        <span class="step-content">Rule Machine for notifications and actions</span>
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
        <span class="step-label">Reminders</span>
        <span class="step-content">Use Apple Reminders with recurring dates</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Display</span>
        <span class="step-content">iPad with Reminders widget or Home app</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Shopping</span>
        <span class="step-content">Link to Apple Reminders shopping list</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Use Shortcuts for more advanced automation
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
        <span class="step-label">Reminders</span>
        <span class="step-content">Alexa recurring reminders for each item</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Display</span>
        <span class="step-content">Echo Show or Fire Tablet with reminder display</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Shopping</span>
        <span class="step-content">"Add HVAC filter to shopping list"</span>
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
        <span class="step-label">Reminders</span>
        <span class="step-content">Google Calendar events for maintenance</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Display</span>
        <span class="step-content">Nest Hub or Android tablet with calendar</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Shopping</span>
        <span class="step-content">"Add to shopping list" via Google Assistant</span>
      </div>
    </div>
  </div>
</div>

## Advanced features

<div class="feature-grid">
  <div class="feature-card">
    <h3>Automatic tracking</h3>
    <p>Use sensors to detect when maintenance is actually needed:</p>
    <ul>
      <li><strong>HVAC filter:</strong> Pressure differential sensor across filter</li>
      <li><strong>Water filter:</strong> Flow rate or TDS sensor</li>
      <li><strong>Pool:</strong> Automated water chemistry testing</li>
      <li><strong>Vacuum:</strong> Track usage hours or cleaning cycles</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Smart shopping integration</h3>
    <p>Automated purchasing options:</p>
    <ul>
      <li>Add to Amazon Subscribe & Save</li>
      <li>Push to shared family shopping list</li>
      <li>Create recurring Amazon orders</li>
      <li>Integration with grocery delivery services</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Cost tracking</h3>
    <p>Monitor maintenance expenses:</p>
    <ul>
      <li>Log cost of each item when replaced</li>
      <li>Track monthly/yearly maintenance spending</li>
      <li>Compare costs between brands</li>
      <li>Predict upcoming expenses</li>
    </ul>
  </div>
</div>

## Common maintenance items to track

<div class="feature-grid">
  <div class="feature-card">
    <h3>HVAC and air quality</h3>
    <ul>
      <li>HVAC air filter (30-90 days)</li>
      <li>Humidifier filter (30-60 days)</li>
      <li>Air purifier filter (6-12 months)</li>
      <li>Dryer vent cleaning (yearly)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Water systems</h3>
    <ul>
      <li>Refrigerator water filter (6 months)</li>
      <li>Under-sink filter (6-12 months)</li>
      <li>Whole-house filter (3-6 months)</li>
      <li>Water softener salt (monthly)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Pool and outdoor</h3>
    <ul>
      <li>Pool chlorine (weekly)</li>
      <li>Pool pH adjuster (as needed)</li>
      <li>Pool filter cleaning (monthly)</li>
      <li>Lawn fertilizer (seasonal)</li>
    </ul>
  </div>
  
  <div class="feature-card">
    <h3>Safety and appliances</h3>
    <ul>
      <li>Smoke detector batteries (yearly)</li>
      <li>CO detector replacement (5-7 years)</li>
      <li>Vacuum filter/bags (1-3 months)</li>
      <li>Dishwasher cleaner (monthly)</li>
    </ul>
  </div>
</div>

## Common issues and solutions

<div class="troubleshooting-grid">
  <div class="issue-card">
    <div class="issue-header">
      <h3>Counters not updating</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Days remaining stays the same or shows wrong value.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify template sensor is calculating correctly</li>
        <li>Check that start date was set properly</li>
        <li>Ensure timezone settings are correct</li>
        <li>Force refresh of template sensors</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Shopping list not syncing</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Items don't appear in shopping list app.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Verify API connection to shopping list service</li>
        <li>Check authentication hasn't expired</li>
        <li>Test service call manually in developer tools</li>
        <li>Use alternative integration (IFTTT, Zapier)</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Tablet screen burns in</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Static dashboard causes screen burn-in over time.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Enable screensaver or screen-off during unused hours</li>
        <li>Use Fully Kiosk Browser with motion-activated screen</li>
        <li>Reduce brightness when not in use</li>
        <li>Use OLED-safe themes with moving elements</li>
      </ul>
    </div>
  </div>
  
  <div class="issue-card">
    <div class="issue-header">
      <h3>Family doesn't check dashboard</h3>
    </div>
    <div class="issue-problem">
      <strong>Problem:</strong> Dashboard exists but nobody looks at it.
    </div>
    <div class="issue-solutions">
      <strong>Solutions:</strong>
      <ul>
        <li>Mount in high-traffic area (kitchen, entryway)</li>
        <li>Send push notifications when items need attention</li>
        <li>Add useful features (weather, calendar) to encourage viewing</li>
        <li>Make screen activate on motion detection</li>
      </ul>
    </div>
  </div>
</div>

## Best practices

<div class="best-practice-card">
  <h3>Setting up maintenance dashboard</h3>
  <ol>
    <li>List all recurring maintenance items in your home</li>
    <li>Research proper replacement intervals for each</li>
    <li>Set up counters with last-replaced dates</li>
    <li>Create visual dashboard with color-coded status</li>
    <li>Connect to shopping list for one-tap adding</li>
    <li>Add notifications for Yellow and Red status items</li>
    <li>Mount tablet where family will see it daily</li>
  </ol>
</div>

<div class="warning-card">
  <h3>What to avoid</h3>
  <ul>
    <li><strong>Too many items</strong> - Start with 5-10 most important</li>
    <li><strong>Wrong intervals</strong> - Research proper timing for your equipment</li>
    <li><strong>Hidden location</strong> - Put dashboard where everyone sees it</li>
    <li><strong>No notifications</strong> - Dashboard alone won't catch attention</li>
    <li><strong>Static intervals</strong> - Some items need adjustment based on usage</li>
  </ul>
</div>

---

**Related automations:**
- [Status tiles](/automation/notifications/status-tiles/)
- [Low battery alerts](/automation/notifications/low-battery-alerts/)
- [Garbage day reminder](/automation/notifications/garbage-day-reminder/)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
