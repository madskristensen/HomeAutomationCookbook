---
layout: default
title: Smart Home Dashboards - Status Tiles, Controls, and Reminders
description: Create effective smart home dashboards for status, reminders, and controls. Garbage day reminders, music controls, and status tiles.
keywords: smart home dashboard, status tiles, dashboard controls, SharpTools, garbage reminder, music controls, home dashboard, tablet dashboard
---

# Dashboards

We have four dashboards in our home - each customized to their location and purpose. Three of them are wall-mounted tablets, and one is built for our phones. What they all have in common is that they allow us to see the status of the home and provide controls for what's important.

For information on how to wall mount tablets and create dashboards, there are many options. I'll defer to the many tutorials online, so you can find the one that works best for your home. I'll be using SharpTools in this book because it's the product I use, but also because it works with the most smart home systems including SmartThings, Hubitat and Home Assistant.

<div class="info-box">
  <strong>🖥️ Our Kitchen Dashboard</strong>
  <p>This is the dashboard located in the kitchen which is also the main area of the house with the most traffic. It serves several purposes:</p>
  <ul>
    <li>Allows us to control the music</li>
    <li>Gives us glanceable status of appliances and doors/windows</li>
    <li>Shows the family calendar</li>
    <li>Shows weather and temperature so we can plan accordingly</li>
  </ul>
</div>

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Status & Visibility</h4>
    <ul>
      <li><strong>Appliance Status</strong> - Washer done, dishwasher clean, etc.</li>
      <li><strong>Door/Window Status</strong> - Know what's open before leaving</li>
      <li><strong>Delivery Alerts</strong> - Package waiting to be brought in</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Controls & Reminders</h4>
    <ul>
      <li><strong>Music Controls</strong> - Easy access to favorite stations</li>
      <li><strong>Garbage Day Reminder</strong> - Weekly task reminder</li>
      <li><strong>Quick Actions</strong> - Common scenes and controls</li>
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
        Amazon Fire tablets (affordable option)<br>
        iPad (premium option)<br>
        Android tablets (flexible option)
      </div>
    </div>
    
    <div class="product-item">
      <strong>Dashboard Software</strong>
      <div class="product-details">
        SharpTools (works with SmartThings, Hubitat, Home Assistant)<br>
        Home Assistant native dashboards<br>
        ActionTiles (SmartThings)<br>
        Hubitat Dashboard
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Wall Mount</strong>
      <div class="product-details">
        Magnetic mounts, flush mounts, or stands for tablets
      </div>
    </div>
    
    <div class="product-item">
      <strong>Always-On Power</strong>
      <div class="product-details">
        Power cable routing for permanent installation
      </div>
    </div>
    
    <div class="product-item">
      <strong>Motion Sensor</strong>
      <div class="product-details">
        Wake screen when someone approaches (optional)
      </div>
    </div>
  </div>
</div>

---

## Garbage day reminder

This is a great way to remember to take out the trash before garbage day. The tile on the dashboard lights up red, so you know you have a task to complete. Once you are done, simply click the tile to turn it back green. This indicates you have completed the task.

### Use cases

- A weekly reminder to take out the trash for garbage collection
- Any other time-scheduled reminder

### Products needed

- Dashboard
- Virtual switch or variable

### Automation setup

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

### Dashboard tile setup

1. Create a virtual switch named "Garbage Out"
2. Add tile to dashboard linked to the virtual switch
3. Configure tile colors:
   - **OFF state (green):** Task completed or not due
   - **ON state (red):** Garbage needs to go out
4. When you complete the task, tap the tile to turn it green

### Advanced: Calendar integration

You can take this to a new level if you integrate with the garbage company's service calendar. That way you don't falsely get a reminder on holidays when no garbage is being picked up. Also, if there's a change in schedule due to weather your smart home adapts accordingly. It doesn't happen often enough that I've done this, but for areas where service changes are more normal it could be helpful.

---

## Status tiles instead of notifications

It's easy to ignore or forget notifications sent to your phone. Also, they don't keep reminding you once you've seen or dismissed them. Status tiles on a dashboard located in a place you often see solves that problem.

### Use cases

- Washer is done, it's time to put it in the dryer
- Dishwasher is clean, it's ready to be emptied
- Grocery/milk/other items have been delivered, time to bring them in and put them away
- Doors and windows are open - good to know before leaving the house
- Robot vacuum is scheduled to run - make sure to tidy up before leaving the house

### Products needed

- Any tablet you prefer (I use the less expensive Amazon Fire tablets)
- Software such as SharpTools

### Automation setup

Any automation where you send a notification, consider using a dashboard tile instead. You can do that by using either a virtual switch or variable.

<div class="automation-example">IF washer is done
THEN set "Washer Done" switch ON
(tile shows red until clothes moved)

IF dryer door opens
THEN set "Washer Done" switch OFF
(tile returns to normal)</div>

### Status tile examples

**Washer/Dryer Status:**
- Create virtual switch for each appliance
- Turn on when cycle completes
- Turn off when door opens or manually tapped

**Door/Window Status:**
- Show all open doors/windows
- Glanceable before leaving house
- No action needed - just informational

**Delivery Status:**
- Turn on when package detected on porch
- Turn off when front door opens (brought in)
- Persistent until addressed

**Robot Vacuum Schedule:**
- Show when vacuum will run today
- Reminder to tidy up
- Countdown to scheduled run

### Why tiles beat notifications

| Notifications | Dashboard Tiles |
|---------------|-----------------|
| Can be dismissed and forgotten | Persistent until addressed |
| Individual to one person | Visible to whole household |
| Interrupt what you're doing | Glanceable at your convenience |
| No ongoing reminder | Always visible status |
| Easy to miss | Hard to miss in high-traffic area |

---

## Music controls

Controlling the music from a dashboard solves several problems. One is to see the album art, artist, and song name to know more information about the current song playing. This is a topic that comes up all the time, and being able to glance at the dashboard to see the information is super convenient.

If you're like me, you have a few favorite stations or playlists that you play most of the time. Giving each of them a tile on the dashboard makes it easy to play any of them. The same goes with presets for volume like low, normal, and loud.

All these controls eliminate the need to yell at Alexa/Google/Siri repeatedly, which is often a cause of frustration.

### Benefits

**For the Household:**
- Anyone can control music without voice commands
- No need to repeat yourself to voice assistant
- Guests can participate easily

**For Parties:**
- Create party-specific music dashboard
- Hide other smart home controls
- Let guests choose music they like
- Volume presets for different party phases

### Dashboard elements for music

**Now Playing Tile:**
- Album art display
- Artist and song name
- Play/pause button
- Skip forward/back

**Favorite Stations/Playlists:**
- One tile per favorite
- Tap to instantly play
- Examples:
  - "Dinner Music" playlist
  - "Morning Energy" station
  - "Kids Favorites"
  - "Party Mix"

**Volume Presets:**
- "Low" (30%) - background music
- "Normal" (50%) - everyday listening
- "Loud" (70%) - party mode
- Eliminates "Alexa, set volume to..." commands

**Room/Zone Selection:**
- Quick switch between rooms
- Group rooms together
- Ungroup for individual control

### Party dashboard

Create a special dashboard for parties and gatherings:

**Include:**
- Large now playing display
- Prominent volume controls
- Favorite party playlists
- Group speaker controls

**Exclude:**
- Home automation controls
- Security features
- Sensitive settings
- Anything confusing for guests

---

## Platform-specific examples

<div class="platform-grid">
  <div class="platform-card">
    <h4>SharpTools</h4>
    <ol>
      <li>Works with SmartThings, Hubitat, Home Assistant</li>
      <li>Create dashboard in web builder</li>
      <li>Add tiles for switches, sensors, media</li>
      <li>Configure colors and layouts</li>
      <li>Access via tablet browser or app</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Home Assistant</h4>
    <ol>
      <li>Use native Lovelace dashboards</li>
      <li>Cards for every entity type</li>
      <li>Custom cards available for advanced features</li>
      <li>Button cards for virtual switches</li>
      <li>Media player cards for music control</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>Hubitat</h4>
    <ol>
      <li>Use built-in Dashboard app</li>
      <li>Add tiles for devices and variables</li>
      <li>Configure templates and colors</li>
      <li>Access via local network</li>
    </ol>
  </div>
  
  <div class="platform-card">
    <h4>ActionTiles</h4>
    <ol>
      <li>Works with SmartThings</li>
      <li>Create panels with tiles</li>
      <li>Media tiles for music</li>
      <li>Custom icons and colors</li>
    </ol>
  </div>
</div>

## Advanced features

### Multiple dashboards for different locations

**Kitchen Dashboard:**
- Music controls (most used)
- Calendar
- Weather
- Appliance status
- Garbage reminder

**Bedroom Dashboard:**
- Alarm clock
- Weather for tomorrow
- Morning routine button
- Sleep mode control
- Minimal distractions

**Entry Dashboard:**
- Door lock status
- Security system status
- "Leaving Home" scene button
- Weather for planning

### Screen wake on approach

**Motion-Activated Screen:**
- Motion sensor near tablet
- Wake screen when motion detected
- Screen sleeps after no motion
- Saves power and screen life

### Automatic dashboard switching

**Time-Based:**
- Morning: Weather and calendar prominent
- Evening: Music controls prominent
- Night: Dim, minimal information

**Mode-Based:**
- Away: Security status visible
- Home: Normal dashboard
- Party: Party music dashboard

## Best practices

### Dashboard design

**Keep It Simple:**
- Don't overcrowd
- Most important items largest
- Group related items
- Consistent layout

**Use Color Meaningfully:**
- Green: Good/off/complete
- Red: Attention needed/on/warning
- Yellow: Caution/transitional
- Blue: Informational

**Prioritize:**
- Most-used controls largest and top/center
- Informational items smaller
- Rarely-used items on secondary screens

### Tablet considerations

**Placement:**
- High traffic areas
- Eye-level mounting
- Avoid direct sunlight
- Near power outlet

**Settings:**
- Disable auto-updates
- Kiosk mode for dedicated use
- Brightness appropriate for location
- Screen timeout balanced with usability

### Family acceptance

**Make It Useful:**
- Solve real problems
- Easy for everyone to use
- No training needed
- Works reliably

**Involve Family:**
- Ask what they want to see
- Iterate based on feedback
- Different dashboards for different users
- Kids-friendly options

---

**Related automations:**
- [Washer done notification](/automation/appliances/washer-done-notification/)
- [Music controls](/automation/media/music-switch-control/)
- [Away mode](/automation/presence/away-mode/)

<div class="page-navigation">
  <a href="/automation/misc/">← Back to Misc Automations</a>
  <a href="/automation/">View All Automations →</a>
</div>
