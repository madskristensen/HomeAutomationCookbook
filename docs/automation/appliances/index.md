---
layout: default
title: Appliance Automations
---

# Appliance automations

The latest generation of appliances have WiFi connectivity and phone apps. But you may want deeper integration with your smart home, or you may have "dumb" appliances that need creative solutions. Here are ways to automate any appliance.

<div class="category-intro" markdown="1">

## Why appliance automation?

**Never Forget** — Get notified when washer, dryer, or dishwasher finishes

**Hands-Free Operation** — Robot vacuum runs automatically when you leave

**Perfect Timing** — Coffee ready exactly when you wake up

**Energy Monitoring** — Track power usage of any appliance

**Smart Scheduling** — Run appliances during off-peak electricity hours

**Any Appliance** — Even "dumb" appliances become smart with power monitoring

</div>

## 🌟 Essential Automations

<div class="automation-cards">

<div class="automation-card" markdown="1">

### Washer done notification

Get notified when the washing machine cycle completes so you can transfer clothes to dryer promptly.

<span class="card-meta">**Best for:** Preventing mildew, laundry efficiency</span>

<p><a href="/automation/appliances/washer-done-notification.html" class="card-link">View Automation →</a></p>

</div>

<div class="automation-card" markdown="1">

### Auto-start robot vacuum when away

Robot vacuum automatically cleans your home when everyone leaves.

<span class="card-meta">**Best for:** Automated cleaning, hands-free maintenance</span>

<p><a href="/automation/appliances/robot-vacuum-auto-start.html" class="card-link">View Automation →</a></p>

</div>

</div>

---

## Quick start guide

### 1. Power monitoring smart plugs

**Best for Appliance Detection:**
- TP-Link Kasa EP25 (16A, energy monitoring)
- Aqara Smart Plug (Zigbee, compact)
- Sonoff S31 (Tasmota-flashable, local control)
- Shelly Plug S (WiFi, accurate power monitoring)

**Note:** Most dryers use 240V special outlets and can't use standard smart plugs. Use vibration sensors instead.

### 2. Alternative detection methods

**Vibration Sensors:**
- Aqara Vibration Sensor
- SmartThings Multi-Sensor
- Attach to appliance body
- Detects running/stopped states

**Contact Sensors:**
- On appliance doors
- Track open/close cycles
- Verify state changes

### 3. Learn power patterns

**Before Automating:**
1. Plug appliance into power monitoring plug
2. Run complete cycle
3. Note power consumption:
   - **Idle:** < 5W
   - **Running:** 100-500W (varies)
   - **Done:** < 5W for 3+ minutes
4. Set automation thresholds based on observed patterns

---

## Common use cases

### 🔔 Completion Notifications
- Washer/dryer cycle finished
- Dishwasher clean and ready
- Coffee maker brewing complete
- Bread machine finished baking

### 🤖 Scheduled Operations
- Robot vacuum runs when away
- Dishwasher starts during off-peak hours
- Coffee maker on timer for morning
- Slow cooker timed start

### ⚡ Energy Monitoring
- Track appliance power usage
- Detect always-on power drains
- Identify malfunctioning appliances
- Monitor monthly consumption

### 🔐 Safety Automations
- Auto-shutoff for heaters after X hours
- Notifications if oven left on
- Alerts for abnormal power draw
- Disable appliances when away

---

## Best practices

### ✅ Power Monitoring Tips

**Calibration:**
- Watch full cycle to learn patterns
- Note different cycle types (heavy, delicate, etc.)
- Set conservative thresholds
- Test multiple times before trusting

**Reliable Detection:**
- Use 3-5 minute delays to avoid false triggers
- Account for different cycle types
- Some cycles use less power
- Combine with other sensors (vibration, door)

### 🔋 Smart Plug Selection

**Consider:**
- Maximum amperage rating (check appliance requirements)
- Power monitoring accuracy
- Local vs. cloud processing
- Size (won't block other outlets)
- Integration with your platform

### 🔔 Notification Strategy

**Progressive Reminders:**
1. **First:** Informational ("Washer done!")
2. **Second (30 min):** Reminder ("Don't forget wet clothes")
3. **Third (2 hours):** Urgent ("Clothes still in washer - mildew risk!")

**Multi-Channel:**
- Push notification to phone
- Dashboard tile
- Smart speaker announcement
- Flash lights

**Quiet Hours:**
- Mute audible between 10 PM - 7 AM
- Visual notifications only at night
- Resume normal in morning

### ⚠️ Safety Considerations

**Never Automate:**
- ❌ Gas appliances
- ❌ High heat without supervision
- ❌ Anything fire-hazardous

**Safe to Automate:**
- ✅ Coffee makers (with auto shut-off)
- ✅ Robot vacuums
- ✅ Dishwashers (already automated)
- ✅ Washing machines
- ✅ Electric kettles (with auto shut-off)

---

## Troubleshooting

**Power Monitoring Not Detecting Cycle End?**
- Lower the power threshold (try 15W instead of 10W)
- Increase delay time (try 5 minutes instead of 3)
- Check if appliance has standby power draw
- Verify smart plug power monitoring accuracy

**False "Done" Notifications?**
- Increase delay before triggering (5+ minutes)
- Raise power threshold slightly
- Check for power fluctuations in your home
- Use additional verification (vibration sensor)

**Vibration Sensor Triggers Too Often?**
- Adjust sensitivity in sensor settings
- Add "for: 2 minutes" delay to automation
- Relocate sensor to less vibration-prone spot
- Combine with door sensor for verification

**Robot Vacuum Starts at Wrong Time?**
- Verify presence detection is accurate
- Add 15-minute delay after away mode
- Check for motion sensors that could indicate presence
- Use time-based conditions (only 9 AM - 6 PM)

<div class="page-navigation">
  <a href="/automation/media/">← Previous: Media</a>
  <a href="/automation/security/">Next: Security & Safety →</a>
</div>
