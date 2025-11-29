---
layout: default
title: Water Leak Detection and Response - Smart Home Safety
description: Detect water leaks early and respond automatically with alerts, water shutoff, and damage prevention. Complete guide for water leak automation.
keywords: water leak sensor, leak detection, water damage prevention, smart water shutoff, flood sensor, basement flooding, leak alert, water sensor automation
---

# Water leak detection and response

Water damage is one of the most expensive home disasters. A single undetected leak can cause thousands of dollars in damage within hours. Smart water leak sensors combined with automated responses can detect leaks early and minimize damage.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Leak detection locations</h4>
    <ul>
      <li><strong>Under sinks</strong> - Kitchen and bathroom pipe connections</li>
      <li><strong>Near water heater</strong> - Tank failures and pressure relief</li>
      <li><strong>Behind washing machine</strong> - Hose failures and connections</li>
      <li><strong>Near dishwasher</strong> - Supply line and drain issues</li>
      <li><strong>Basement/utility room</strong> - Sump pump failures, foundation seepage</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Response actions</h4>
    <ul>
      <li><strong>Immediate alerts</strong> - Phone notifications day or night</li>
      <li><strong>Automatic water shutoff</strong> - Stop the source immediately</li>
      <li><strong>Turn off water heater</strong> - Prevent dry-fire damage</li>
      <li><strong>Alert family members</strong> - Multiple people notified</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Water leak sensors</strong>
      <div class="product-details">
        Popular brands: Aqara, Samsung SmartThings, Honeywell, Fibaro<br>
        Place at each potential leak location - plan for 5-10 sensors for full coverage
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart water shutoff valve</strong>
      <div class="product-details">
        Brands: Moen Flo, Phyn, LeakSmart, Dome<br>
        Installs on main water line - automatically stops water flow when leak detected
      </div>
    </div>
    
    <div class="product-item">
      <strong>Smart water heater controller</strong>
      <div class="product-details">
        Turn off water heater to prevent dry-fire damage when water is shut off
      </div>
    </div>
    
    <div class="product-item">
      <strong>Rope-style water sensors</strong>
      <div class="product-details">
        Extends detection area - good for long runs like behind washer or along basement walls
      </div>
    </div>
  </div>
</div>

<div class="info-box">
  <strong>💡 Sensor placement tips</strong>
  <ul>
    <li>Place sensors on the floor where water would collect first</li>
    <li>Ensure sensor contacts touch the floor surface directly</li>
    <li>Avoid carpeted areas if possible - use hard surface or drip tray</li>
    <li>Check sensors periodically - dust can affect sensitivity</li>
  </ul>
</div>

## Basic automation setup

<div class="automation-example">IF any water sensor detects leak
THEN send critical notification to all family
AND turn on all lights in affected area
AND (if equipped) shut off main water valve</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Any water leak sensor detects water (wet)</li>
      <li>Water sensor state changes to "wet" or "leak detected"</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <p>None - this should always trigger regardless of time, mode, or other factors</p>
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Send critical/high-priority notification with sensor location</li>
      <li>Send notification to all family members</li>
      <li>Turn on lights in affected area</li>
      <li>If equipped: Close smart water shutoff valve</li>
      <li>If water heater area: Turn off water heater</li>
      <li>Optional: Flash lights or sound alarm</li>
    </ul>
  </div>
</div>

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Trigger: Any water sensor state changes to "on" or "wet"</li>
      <li>No conditions - always run</li>
      <li>Actions: Send persistent notification with sensor name</li>
      <li>Turn on lights in sensor area</li>
      <li>Call service to close water shutoff valve (if equipped)</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>SmartThings</h4>
    <ol>
      <li>IF Any water sensor detects water</li>
      <li>THEN Send notification to all members</li>
      <li>Turn on lights in that room</li>
      <li>Close smart water valve (if compatible)</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use Rule Machine or Hubitat Safety Monitor</li>
      <li>Trigger: Any water sensor wet</li>
      <li>Actions: Push notification, turn on lights</li>
      <li>Close water valve if equipped</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Apple HomeKit</h4>
    <ol>
      <li>When: Water sensor detects leak</li>
      <li>Do: Send notification, turn on lights</li>
      <li>Note: Water shutoff requires HomeKit-compatible valve</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Alexa</h4>
    <ol>
      <li>When: Water sensor detects water</li>
      <li>Action: Send notification, announce on Echo</li>
      <li>Turn on lights, close valve if compatible</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Google Home</h4>
    <ol>
      <li>Starter: Water sensor detects leak</li>
      <li>Action: Send notification, turn on lights</li>
      <li>Announce "Water leak detected" on speakers</li>
    </ol>
  </div>
</div>

## Priority sensor locations

### High priority (install first)

**Water heater area:**
- Tank failures can release 40-80 gallons quickly
- Place sensor at base of water heater
- Consider rope sensor around perimeter

**Under kitchen sink:**
- Multiple connections, garbage disposal
- Common failure point for supply lines
- Place sensor at lowest point under sink

**Behind washing machine:**
- Supply hoses are common failure point
- High water pressure area
- Place sensor on floor behind or beside machine

### Medium priority

**Under bathroom sinks:**
- P-trap connections, supply lines
- Place sensor at lowest point in cabinet

**Near dishwasher:**
- Supply line connection to hot water
- Place sensor at front edge where water would spread

**Near refrigerator (if ice maker):**
- Ice maker supply line is small but can leak continuously
- Often goes unnoticed in back corner

### Recommended for full coverage

**Basement or utility room:**
- Sump pump area
- HVAC condensate drain
- Foundation walls (rope sensor)

**Near toilets:**
- Supply line connection
- Wax ring failures

## Advanced features

### Location-specific responses

Create separate automations for different areas:

**Water heater leak:**
- All standard actions plus
- Turn off water heater power (smart plug or circuit)
- Prevents dry-fire damage

**Basement leak:**
- Check sump pump status
- Notify if pump not running
- Higher urgency during rain

**Washer area leak:**
- Turn off washer power (smart plug)
- Prevents further water addition

### Escalating alerts

Create progressive notification system:

1. **Immediate:** Critical push notification to all phones
2. **2 minutes later:** If not acknowledged, call phones (using IFTTT or Pushover)
3. **5 minutes later:** Text emergency contacts or neighbors
4. **10 minutes later:** Continue calling until acknowledged

### All-clear notification

When sensor dries:

- **Trigger:** Water sensor state changes to "dry"
- **Condition:** Previous state was "wet"
- **Action:** Send notification "Water sensor dried - check area and assess damage"

### Integration with insurance

Some insurance companies offer discounts for:
- Whole-home water shutoff valves
- Connected leak detection systems
- Check with your insurer for potential savings

## Troubleshooting

### Issue: False alerts

**Causes:**
- High humidity triggering sensor
- Condensation on cold pipes
- Sensor placed on damp surface
- Sensor battery dying (erratic behavior)

**Solutions:**
✅ Raise sensor slightly off ground (still touching but elevated)
✅ Move away from high-humidity areas
✅ Use drip tray under potential leak sources
✅ Check and replace batteries regularly
✅ Clean sensor contacts periodically

### Issue: Sensor not detecting water

**Causes:**
- Sensor placed too far from leak source
- Water flowing away from sensor
- Sensor contacts dirty or corroded
- Wireless signal not reaching hub

**Solutions:**
✅ Test sensor by placing wet paper towel on contacts
✅ Reposition sensor to lowest point where water collects
✅ Clean contacts with isopropyl alcohol
✅ Add repeater or move hub closer
✅ Check battery level

### Issue: Notification not received

**Causes:**
- Phone notifications disabled
- Automation disabled or errored
- Critical alerts filtered by phone
- Hub offline

**Solutions:**
✅ Verify push notification permissions
✅ Check automation is enabled and error-free
✅ Mark app as critical/priority in phone settings
✅ Test automation with manual trigger
✅ Ensure hub is online and connected

## Best practices

### Sensor maintenance

**Monthly:**
- Test sensors with wet paper towel
- Check battery levels
- Verify notifications arrive

**Quarterly:**
- Clean sensor contacts
- Check sensor placement
- Review automation logs

### Response planning

**Know your shutoff locations:**
- Main water shutoff valve location
- Individual fixture shutoffs
- Water heater shutoff

**Emergency contacts:**
- Plumber phone number saved
- Water damage restoration service
- Insurance claim contact

**Family awareness:**
- All adults know manual shutoff location
- Emergency procedures documented
- Test automation with family periodically

### Battery management

- Use quality batteries (lithium recommended for sensors)
- Set low battery alerts
- Replace on schedule, not when dead
- Keep spare batteries on hand

---

**Related automations:**
- [Fire safety emergency response](/automation/security/fire-safety.html)
- [Away mode automation](/automation/presence/away-mode.html)
- [Low battery alerts](/automation/notifications/low-battery-alerts.html)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
