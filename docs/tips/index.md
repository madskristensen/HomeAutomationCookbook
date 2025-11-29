---
layout: default
title: Tips and Tricks
---

# Tips and Tricks

Not all home automation requires complex technology. Sometimes the simplest solutions are the most effective.

---

## Amazon Subscriptions for Automation

Not all automations have to go through your smart home system. You can use Amazon subscriptions to automate yourself to complete repetitive maintenance tasks.

### How It Works

Subscribe to certain products to be automatically ordered and delivered at specific time intervals. When items arrive, install them right away. This eliminates the need to remember when to order and replace items.

### Examples

**Water Filter for Refrigerator**
- Schedule: Every 6 months
- Action: Install immediately upon arrival

**Air Filters**
- For air purifiers and robot vacuums
- Schedule: Every 4 months
- Action: Replace filters right away

**Other Subscription Ideas:**
- HVAC filters (quarterly)
- Batteries for sensors (annually)
- Pet supplies (monthly)
- Cleaning supplies (bi-monthly)
- Coffee, tea, or other consumables

### Benefits

✅ Never forget to order replacement items
✅ Installation becomes automatic when delivery arrives
✅ Save money with subscribe & save discounts
✅ Reduce mental load of tracking maintenance

---

## Manually Disable Automation in a Room

Sometimes you don't want automations to run. For example, kids love turning lights off to play with flashlights. It ruins the fun if lights come on automatically when motion is detected.

### The Solution

Disable automation when lights are manually switched off. When lights are manually switched on again, re-enable automations automatically.

### Requirements

* **Smart light switch** that can detect manual (often called "physical") operations
* Ability to distinguish between manual and automated control

### Implementation

**When lights are manually turned OFF:**
* Disable motion-based light automations for this room
* Keep automations disabled

**When lights are manually turned ON:**
* Re-enable motion-based light automations
* Resume normal automated behavior

### Supported Platforms

Most smart switches support this feature:
- Zooz switches (Z-Wave)
- Inovelli switches (Z-Wave, Zigbee)
- GE/Jasco switches (Z-Wave)
- Lutron Caseta (proprietary)
- Many others - check specifications

### Platform Setup

**Home Assistant:**
Look for "physical" vs "digital" button press events

**SmartThings:**
Use custom device handlers that expose manual control events

**Hubitat:**
Most switches report button events that can differentiate manual vs automated

---

## Turn Off All Lights in Room from One Switch

In most rooms, the main light switch by the door can turn off all lights in the room with a special gesture.

### The Double-Tap Trick

Many smart switches support double-tap actions. Configure double-tap on the OFF button to turn off all lights and smart plugs in that room.

### Example Use Case

**Leaving the Living Room:**
1. Walk to door
2. Double-tap OFF switch
3. All room lights, lamps, and floor fans turn off
4. Exit room

### Setup Instructions

**Step 1: Identify Devices**
- List all lights and plugs in each room
- Group them by room in your smart home app

**Step 2: Configure Switch**
- Enable double-tap feature on your smart switch
- Set double-tap DOWN to trigger "All Off" scene

**Step 3: Create Scene/Routine**
- Name: "Living Room All Off"
- Actions: Turn off all devices in living room

**Step 4: Test**
- Double-tap the OFF button
- Verify all devices turn off
- Adjust timing if needed

### Compatible Switches

**Switches with Double-Tap:**
- Inovelli (Red/Blue series)
- Zooz (ZEN switches)
- GE/Jasco
- Leviton
- HomeSeer

**Multi-Tap Options:**
Some switches support more gestures:
- Double-tap UP: All on at 100%
- Double-tap DOWN: All off
- Triple-tap UP: Scene 1
- Triple-tap DOWN: Scene 2

---

## Dashboard Status Tiles

Replace notifications with visual status tiles on a dashboard. Instead of getting push notifications that get dismissed and forgotten, display status on a tablet you see regularly.

### Why Dashboards Beat Notifications

**Problems with Notifications:**
- Easy to dismiss and forget
- Interrupt your flow
- Don't provide persistent status
- Require checking phone

**Benefits of Dashboards:**
- Always visible status at a glance
- No interruptions
- Entire household can see
- Multiple statuses visible simultaneously

### Use Cases

**Appliances:**
* ✅ Washer is done, time to move to dryer
* ✅ Dishwasher is clean, ready to empty
* ✅ Dryer finished, clothes need folding

**Deliveries:**
* ✅ Grocery/milk delivery arrived, bring items inside
* ✅ Package delivered at front door
* ✅ Mail arrived

**Home Status:**
* ✅ Doors or windows are open (before leaving)
* ✅ Robot vacuum scheduled to run soon (tidy up first)
* ✅ Trash day tomorrow (take bins out)
* ✅ Low battery on sensors

### Products

**Tablets:**
* Amazon Fire tablets (budget-friendly)
* iPads (premium)
* Android tablets (mid-range)

**Software:**
* SharpTools
* Home Assistant Dashboard
* Hubitat Dashboard
* ActionTiles (SmartThings)
* Fully Kiosk Browser

### Implementation Tips

**Placement:**
- Kitchen counter or wall mount
- Entryway/mudroom
- Master bathroom
- Garage entrance

**Design Principles:**
- Large, easy-to-read tiles
- Color coding (green=good, red=attention needed)
- Most important info at top
- Clear labels

**Power Management:**
- Use motion sensor to wake display
- Dim or sleep when not in use
- Keep plugged in

**Security:**
- Disable browser navigation
- Use kiosk mode app
- Place out of view from windows
- Consider guest mode with limited controls

---

## Creating Patterns Throughout Your Home

When you implement a feature in one room, consider making it a pattern throughout the house.

### Example: Light Switch Double-Tap

**Pattern:** Double-tap any light switch to control all lights in that room

**Benefits:**
- Easy to remember once learned
- Works the same in every room
- No explanation needed after initial teaching
- Intuitive and consistent

### Other Pattern Ideas

**Long-Press for Scenes:**
* Long-press light switch → Activate room scene
* Bedroom: Reading mode
* Living room: Movie mode
* Kitchen: Cooking mode

**Triple-Tap for Special Functions:**
* Triple-tap any switch → All lights in house off
* Useful when leaving home
* Emergency "lights off" function

**Hold for Dimming:**
* Hold UP → Gradually brighten
* Hold DOWN → Gradually dim
* Works across all dimmers

### Visual Markers

Mark switches with special capabilities:
- Small colored dots or stickers
- Printed labels in switch plate
- Subtle engraving
- Consistent placement of "smart" switches

---

[← Back to Home](/) | [View Resources →](/resources/)
