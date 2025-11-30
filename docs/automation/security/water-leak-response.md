---
layout: automation
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
    <div class="platform-card-header">
      <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
      <h4>Home Assistant</h4>
    </div>
    <div class="platform-steps">
      <div class="platform-step">
        <span class="step-label">Trigger</span>
        <span class="step-content">Any water sensor state changes to "on" or "wet"</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Condition</span>
        <span class="step-content">None - always run</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Send persistent notification, turn on lights, close valve</span>
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
        <span class="step-content">Any water sensor detects water</span>
      </div>
      <div class="platform-step">
        <span class="step-label">THEN</span>
        <span class="step-content">Send notification to all members + turn on lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Close smart water valve if compatible
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
        <span class="step-content">Any water sensor wet</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Actions</span>
        <span class="step-content">Push notification, turn on lights, close valve</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Setup:</strong> Use Rule Machine or Hubitat Safety Monitor
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
        <span class="step-content">Water sensor detects leak</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Do</span>
        <span class="step-content">Send notification, turn on lights</span>
      </div>
      <div class="platform-step-variant">
        <div class="step-variant">
          <strong>Note:</strong> Water shutoff requires HomeKit-compatible valve
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
        <span class="step-content">Water sensor detects water</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Notification, announce on Echo, turn on lights</span>
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
        <span class="step-content">Water sensor detects leak</span>
      </div>
      <div class="platform-step">
        <span class="step-label">Action</span>
        <span class="step-content">Send notification, turn on lights, announce</span>
      </div>
    </div>
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
- [Fire safety emergency response](/automation/security/fire-safety/)
- [Away mode automation](/automation/daily-routines/away-mode/)
- [Low battery alerts](/automation/notifications/low-battery-alerts.html)

<div class="page-navigation">
  <a href="/automation/security/">← Back to Security Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
