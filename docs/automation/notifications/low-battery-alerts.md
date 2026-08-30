---
layout: automation
title: Low Battery Alerts - Smart Home Maintenance Automation
description: Never be surprised by dead smart home device batteries. Get proactive alerts when device batteries are low to maintain reliable automation.
keywords: low battery alert, smart home battery, device battery notification, battery monitoring, smart device maintenance, battery replacement reminder
---

# Low battery alerts

Smart home devices with dead batteries can't do their jobs. Motion sensors stop detecting, door sensors go offline, and automations fail silently. Proactive battery monitoring ensures your smart home stays reliable.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Prevention</h4>
    <ul>
      <li><strong>Security gaps</strong> - Door/window sensors going offline unnoticed</li>
      <li><strong>Failed automations</strong> - Motion sensors not triggering lights</li>
      <li><strong>Missed alerts</strong> - Water leak sensors not reporting</li>
      <li><strong>Lock failures</strong> - Smart lock battery dying at worst time</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Maintenance</h4>
    <ul>
      <li><strong>Proactive replacement</strong> - Replace before failure</li>
      <li><strong>Batch ordering</strong> - Know which batteries to stock</li>
      <li><strong>Scheduled maintenance</strong> - Plan battery swaps efficiently</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart home platform that reports battery levels</strong>
      <div class="product-details">
        The hub must receive a battery percentage or low-battery state from each monitored device
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Devices that commonly need battery monitoring</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Sensors</strong>
      <div class="product-details">
        Motion sensors, door/window contact sensors, water leak sensors, temperature sensors
      </div>
    </div>
    
    <div class="product-item">
      <strong>Locks and controls</strong>
      <div class="product-details">
        Smart locks, smart buttons, remote controls, keypads
      </div>
    </div>
    
    <div class="product-item">
      <strong>Other battery devices</strong>
      <div class="product-details">
        Smoke detectors, blinds, some cameras, wireless switches
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Stock common battery types</strong>
  <ul>
    <li><strong>CR2032:</strong> Most small sensors (Aqara, SmartThings)</li>
    <li><strong>CR123A:</strong> Some motion sensors, locks</li>
    <li><strong>AA/AAA:</strong> Larger sensors, some locks, remotes</li>
    <li><strong>CR2450:</strong> Some Zigbee sensors</li>
    <li>Keep 2-3 of each common type on hand</li>
  </ul>
</div>

## Logic

<div class="automation-example">IF any device battery drops below 20%
THEN send notification with device name and battery level
AND add to low battery list on dashboard</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Any battery-powered device drops below 20%</li>
      <li>OR Device reports "low battery" state</li>
      <li>OR Daily check of all battery levels</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions (optional)</h4>
    <ul>
      <li>Battery level dropped (not already low)</li>
      <li>Haven't notified about this device in last 7 days</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Send notification: "[Device name] battery is at [X]%"</li>
      <li>Update dashboard tile or list</li>
      <li>Optional: Log to file for tracking</li>
    </ul>
  </div>
</div>

## Advanced features

### Tiered warnings

Different alerts at different levels:

**First warning (25%):**
- Normal notification
- "Consider replacing soon"
- Add to low battery list

**Second warning (15%):**
- Higher priority notification
- "Replace within next few days"

**Critical (5%):**
- Urgent notification
- "Replace immediately - device may stop working"

### Battery dashboard

Create visual overview:

**Dashboard elements:**
- All devices with battery percentage
- Color coding: green (50%+), yellow (20-50%), red (<20%)
- Sort by lowest first
- Show days since last change (if tracked)

### Device offline detection

Catch devices that died without warning:

- **Trigger:** Device hasn't reported in 24 hours
- **Action:** Send alert: "[Device] may be offline - check battery"
- **Note:** Some devices only report when triggered

### Battery change tracking

Log when batteries are replaced:

**Create input helper:**
- Date of last battery change per device
- Calculate expected replacement date
- Alert when approaching typical lifespan

**Typical battery life:**
- Contact sensors: 1-2 years
- Motion sensors: 6-18 months
- Smart locks: 6-12 months
- Temperature sensors: 1-2 years

### Critical device priority

Higher priority for important devices:

**Critical devices (immediate alert):**
- Smart locks
- Water leak sensors
- Smoke detector sensors

**Standard devices (daily report):**
- Motion sensors
- Temperature sensors
- Remote buttons

## Notification strategies

### Consolidated daily report

Instead of individual alerts:

**Daily at 9 AM:**
- Check all batteries
- Group into categories
- Send single notification:
  - "Critical: Front door lock (8%)"
  - "Low: Kitchen motion (18%), Garage door (22%)"
  - "OK: 15 devices above 30%"

### Weekly maintenance reminder

Scheduled battery check:

**Every Sunday at 10 AM:**
- List all devices below 30%
- Remind to check and replace
- Include battery types needed

### Notification cooldown

Prevent repeated alerts:

- Only notify once per device per week
- Unless level drops to next tier
- Reset cooldown when battery replaced

## Failure modes

### Issue: Battery shows 100% then suddenly 0%

**Causes:**
- Device doesn't report gradual levels
- Reporting only "OK" or "Low"
- Battery type issue (some drop voltage rapidly)

**Solutions:**
✅ Check if device supports gradual reporting
✅ Watch for "low battery" state instead of percentage
✅ Use quality batteries (may report more accurately)
✅ Set replacement schedule based on time, not percentage

### Issue: Battery percentage fluctuates

**Causes:**
- Temperature affecting readings
- Voltage bounce after use
- Sensor inaccuracy
- Old battery recovering temporarily

**Solutions:**
✅ Use average over time instead of instant reading
✅ Only alert if low for extended period (hours)
✅ Consider actual battery age not just percentage
✅ Ignore small fluctuations (±5%)

### Issue: Missing devices in monitoring

**Causes:**
- Device doesn't report battery
- Entity not included in group
- Device using different attribute name

**Solutions:**
✅ Check device capabilities for battery reporting
✅ Manually add to monitoring group
✅ Check for alternative battery entity names
✅ Some devices need custom integration

### Issue: Too many notifications

**Causes:**
- Threshold too high (50% is too early)
- No cooldown between alerts
- Fluctuating readings triggering repeatedly

**Solutions:**
✅ Lower threshold to 20-25%
✅ Add cooldown (one notification per week)
✅ Use "dropped below" trigger not "is below"
✅ Consolidate into daily/weekly report

## Best practices

### Setting thresholds

**Recommended levels:**
- **Warning:** 20-25% (weeks of life remaining)
- **Low:** 10-15% (days of life remaining)
- **Critical:** 5% (replace immediately)

**Adjust for device type:**
- Smart locks: Higher threshold (25%) - don't want lockout
- Motion sensors: Standard threshold (20%)
- Temperature sensors: Lower threshold (15%) - less critical

### Battery inventory

**Keep on hand:**
- List of all battery types used
- 2-3 spares of common types
- Note which devices use which battery
- Order before running out

### Replacement strategy

**Best practices:**
- Replace at warning level, not when dead
- Replace all batteries in multi-battery devices together
- Note replacement date for tracking
- Use quality batteries for critical devices
- Consider rechargeable for frequently changed devices

### Device placement for longevity

**Extend battery life:**
- Avoid extreme temperatures
- Reduce unnecessary triggers (adjust sensitivity)
- Keep devices in good signal range (less retry = less battery)
- Consider wired alternatives for high-use locations

---

## Related recipes
- [Water leak detection](/automation/security/water-leak-response.html)
- [Away mode automation](/automation/daily-routines/away-mode/)
- [Bedtime routine](/automation/daily-routines/bedtime-routine/)

<div class="page-navigation">
  <a href="/automation/notifications/">← Back to Notifications</a>
  <a href="/automation/">View All Automations →</a>
</div>
