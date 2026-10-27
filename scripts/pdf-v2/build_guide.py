#!/usr/bin/env python3
"""Build the Starter House Setup Guide v2 (review copy). Usage: python3 build_guide.py"""
import pathlib, subprocess, sys
from rp import recipe_page
HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "hac-starter-house-setup-guide-v2.pdf"
W = "www.homeautomationcookbook.com"

def chk(*items): return '<ul class="check">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def tip(t, lbl="Tip"): return f'<div class="callout"><b class="lbl">{lbl}</b><p>{t}</p></div>'
def warn(t, lbl="Safety note"): return f'<div class="callout warn"><b class="lbl">{lbl}</b><p>{t}</p></div>'
def win(t): return f'<div class="callout win"><b class="lbl">What you will have working</b><p>{t}</p></div>'
def head(kicker, title, lede=""):
    return f'<p class="kicker">{kicker}</p><h2>{title}</h2><div class="rule"></div>' + (f'<p class="lede">{lede}</p>' if lede else "")

ZW = "Z-Wave. Needs a hub with a Z-Wave radio, such as Home Assistant with a Z-Wave stick, Hubitat, SmartThings, Homey Pro or HomeSeer. It does not work with Apple Home, Google Home or Alexa."
ZB = "Zigbee. Needs a hub with a Zigbee radio, such as Home Assistant with a Zigbee stick, Hubitat, SmartThings, Homey Pro or an Echo with a built-in Zigbee hub. Apple Home and Google Home have no Zigbee radio."
MT = "Matter over Wi-Fi. Works with most hubs that support Matter, including Apple Home, Google Home and Alexa."
ALT_PLUG = ("Alternative for Apple Home, Google Home or Alexa: any Matter or Zigbee smart plug with energy monitoring that your hub supports. "
            "Check that it is rated for your washer's motor load. Many small plugs are not.")

def step_recipe(n, cat, title, lede, steps, test, tipt, path, extra=""):
    body = ('<h4>Why this matters</h4><p>' + lede[1] + '</p>' + extra +
            '<h4>Steps</h4><ol class="steps">' + "".join(f"<li>{s}</li>" for s in steps) + "</ol>" +
            f'<div class="callout win"><b class="lbl">Test it</b><p>{test}</p></div>' + tip(tipt) +
            '<p class="small">You have got this. If the test fails, change one setting at a time and try again.</p>')
    return recipe_page(cat, f"Walkthrough {n} of 11", title, lede[0], body, path, f"w{n}")

R = []
R.append(step_recipe(1, "Lighting", "Lights on motion",
 ("The light comes on before your hand reaches the switch. The switch still works.",
  "This is the recipe that makes a house feel smart. It is also the easiest one to get right, so it is a great first win."),
 ["Install the switch first. Check that the paddle works like a normal switch.",
  'Pair the motion sensor. Name it by room and job, for example "Hallway Motion".',
  "Mount the sensor where it sees the path into the room, not the wall switch.",
  "Create the rule. Trigger: motion becomes active.",
  "Add a condition: the light is off. This keeps the rule from changing a level someone picked.",
  "Add a second condition: the room is dark, or it is inside your night hours.",
  "Action: turn on the light. At night use 10 to 20 percent. In the evening use a useful level, such as 60 percent.",
  "Do not add a turn-off step yet. That is the next walkthrough."],
 "Walk in from the dark at night. The light should be on before you reach the switch. Then walk in on a bright day. It should stay off.",
 "Use your hub's simplest rule tool for a single on action. Many hubs also have a motion lighting app. Room Lighting on Hubitat is one example.",
 "/automation/lighting/lights-on-motion.html"))
R.append(step_recipe(2, "Lighting", "Lights off after motion",
 ("The light turns off after the room has been empty for a while, but never while someone is still there.",
  "A light that goes dark on someone reading is the fastest way to lose the family's trust. A patient timeout keeps everyone happy."),
 ["Live with walkthrough 1 for a week before you add this one.",
  "Trigger: the room sensor has reported no motion for the timeout.",
  "Start the timeout at 5 to 10 minutes for a bathroom or quiet room. Use 15 minutes if people sit still.",
  "Condition: no other sensor in the same space is active. If a closet opens into the room, watch both sensors.",
  "Condition: no manual override. If someone used the wall switch, leave the light alone.",
  "Optional condition: music is not playing in the room. Playing music is a good sign someone is still there.",
  "Action: turn the light off.",
  "Make sure new motion cancels the countdown."],
 "Sit still in the room for longer than the timeout. If the light goes off on you, raise the timeout before you blame the sensor.",
 "Shorten the timeout only after the household has lived with it for a while.",
 "/automation/lighting/lights-off-after-motion.html"))
R.append(step_recipe(3, "Lighting", "Bathroom night-light",
 ("A dim, warm light at night so nobody is blinded at 2 AM.",
  "Small comforts like this are what make people love the system. Everyone in the house will notice it on the first night."),
 ["Install the dimmer and pair the multisensor.",
  "Trigger: bathroom or entry motion is detected.",
  "Condition: the mode is Night, or the time is inside your night window.",
  "Optional condition: the room is dark enough, using the sensor's light reading.",
  "Action: set the bathroom light to 10 percent. Add a warm color only if the light supports it.",
  "Let walkthrough 2 own the turn-off. Start at 10 minutes for a shower bathroom."],
 "Walk in at night with the house in Night mode. The light should come on dim. A press on the switch should still bring full light.",
 "If you later add the shower fan recipe, the same multisensor gives you the humidity reading.",
 "/automation/lighting/bathroom-night-light.html"))
R.append(step_recipe(4, "Appliances", "Washer done alert",
 ("One alert when the washer is really done. No alerts during pauses in the cycle.",
  "No more damp clothes forgotten in the drum. A few minutes of measuring now gives you an alert you can trust for years."),
 ["Plug the washer into the washer power-monitoring plug. Check that the washer is within the plug's rated load.",
  "Run three loads with logging only. Write down the power while running, during pauses, and when finished.",
  "Pick a running threshold that is clearly above idle power. Pick a finished threshold just above the idle level.",
  'Rule A. Trigger: power stays above the running threshold long enough to prove a cycle started. Action: set a "Washer running" marker.',
  "Rule B. Trigger: power stays below the finished threshold longer than the longest normal pause.",
  'Rule B condition: the "Washer running" marker is set.',
  'Rule B actions: send one "Washer finished" notification, set "Laundry waiting", and clear the running marker.',
  "Never let the rule turn the plug off."],
 "Run a normal load and watch your phone. You should get exactly one alert, a few minutes after the washer stops.",
 "Some hubs have an app that tracks running and finished states for you. Appliance Cycle Monitor on Hubitat is one example.",
 "/automation/appliances/washer-done-notification.html",
 warn("The Zooz ZEN15 is Z-Wave. It needs a hub with a Z-Wave radio and will not work with Apple Home, Google Home or Alexa. " + ALT_PLUG, "Check your hub")))
R.append(step_recipe(5, "Appliances", "Dryer done alert",
 ("One alert when the dryer stops shaking for good.",
  "Dryers pause and tumble during cooldown. Measuring one load first is what keeps this to a single, useful alert."),
 ["Stick the vibration sensor on top of the dryer, away from the hot vent.",
  "Run a load and note how long vibration stops during normal pauses or cooldown.",
  'Rule A. Trigger: vibration stays active for the start delay. Action: set a "Dryer running" marker.',
  "Rule B. Trigger: vibration stays inactive longer than the longest pause you saw.",
  'Rule B conditions: the "Dryer running" marker is set, and the sensor is online.',
  'Rule B actions: send one "Dryer finished" notification, set "Laundry waiting", and clear the marker.'],
 "Run a full load, including any wrinkle guard. You should get one alert, not three.",
 "If you get alerts during cooldown, the finish delay is too short.",
 "/automation/appliances/dryer-done-notification.html"))
R.append(step_recipe(6, "Safety", "Water leak alert",
 ("An alert at any hour that says exactly where the water is.",
  "A small leak caught early is a towel. A leak found days later is a repair bill. This one is worth doing carefully."),
 ['Name each sensor by place, for example "Leak Water Heater" and "Leak Washer".',
  "Place them flat on the floor where water shows up first.",
  "Trigger: any leak sensor reports wet.",
  "No conditions. Leak alerts run in Home, Away, Night, and Guest modes.",
  "Action: send a high-priority notification that names the sensor. Send it to at least two people.",
  "Optional: repeat the alert only while nobody has checked on it.",
  "Clear the incident by hand, after a person has looked at the source. A dry sensor does not mean the leak is fixed."],
 "Touch the sensor with a wet towel. Check that both phones get the alert and that the message names the right place.",
 "Leave automatic water shutoff for later. Get trusted alerts first.",
 "/automation/security/water-leak-response.html"))
R.append(step_recipe(7, "Lighting", "Closet light on door open",
 ("The closet or pantry light comes on when the door opens.",
  "It is a simple recipe that gets used many times a day. It is also a gentle way to learn how contact sensors behave."),
 ["Mount the contact sensor on the door and frame with the two parts lined up.",
  "Trigger: the contact changes from closed to open.",
  "Condition: the space is dark enough, or it is inside the hours when light makes sense.",
  "Action: turn on the light at the level you want.",
  "Optional second rule: turn the light off when the door closes, or after a timeout.",
  "Do not undo a manual switch change right away."],
 "Open the door ten times in a row. The light should come on every time.",
 "If it misses, check the gap between the two sensor parts.",
 "/automation/lighting/toggle-lights-door.html"))
R.append(step_recipe(8, "Safety", "Garage door left open",
 ("A reminder when the garage door has been open longer than expected.",
  "An open garage door at night is easy to miss and easy to fix. A friendly reminder covers it without any risky automation."),
 ["Mount the tilt sensor on the top panel of the garage door.",
  "Trigger: the door reports open and stays open for 10 minutes.",
  'Action: send "Garage door has been open for 10 minutes".',
  'Second rule. Trigger: 10:00 PM. Condition: the door is open. Action: send a high-priority "Garage door still open at bedtime".',
  "Do not close the door from this recipe. Closing stays manual."],
 "Open the garage door and wait 10 minutes. Then close it and make sure no more alerts arrive.",
 "Auto-closing is a separate, later project. It needs an opener that supports safe unattended operation.",
 "/automation/security/garage-door-notification.html"))
R.append(step_recipe(9, "Notifications", "Low-battery alerts",
 ("No sensor ever goes quiet without anyone knowing.",
  "A dead battery is the most common reason a good rule stops working. This alert quietly protects every other recipe."),
 ["Add every battery device to one list.",
  "Trigger: a battery drops below its threshold, or reports low battery.",
  "Condition: this device has not been flagged in the last 7 days.",
  'Action: send "[Device name] battery is at [level]".',
  "The alert resets when the battery is replaced and reports normal again."],
 "Put a weak battery in one sensor. You should get one alert, not one every hour.",
 "Keep spare batteries of each size in one drawer.",
 "/automation/notifications/low-battery-alerts.html"))
R.append(step_recipe(10, "Daily routines", "Away mode",
 ("The house switches to Away only when it is really empty.",
  "Away mode ties the whole house together. Being careful here means nobody at home ever gets left in the dark."),
 ["Set up presence for each person and test it for a week.",
  "Trigger: the last tracked person leaves.",
  "Condition: everyone has been away for 15 minutes.",
  "Condition: Guest mode is off, and no recent indoor motion suggests someone is home.",
  "Actions: set the mode to Away, turn off lights that are safe to turn off, and send a summary.",
  "Cancel it if someone returns, or if a person picks Home or Guest."],
 "Leave together and check that Away is set after the delay. Then leave one person home and check that it is not.",
 "Shorten the 15 minutes only after several weeks without a false Away.",
 "/automation/daily-routines/away-mode.html"))
R.append(step_recipe(11, "Daily routines", "Bedtime and Night mode",
 ("Night mode from one intentional action, with an automatic backup.",
  "Going to bed should be one tap. The backup rule catches the nights everyone forgets, without ever surprising someone still up."),
 ["Manual rule. Trigger: a double tap down on a stair or hallway switch.",
  "Conditions: the mode is Home, and the time is between 8 PM and midnight.",
  "Action: set the mode to Night and turn off approved unoccupied lights. Keep path lighting.",
  "Automatic backup. At 10 PM, if the mode is Home, check every 10 minutes, up to 12 times.",
  "Each pass: stop if the mode is no longer Home. If every downstairs motion sensor has been inactive for 15 minutes, set Night and stop.",
  "If people are still up after about two hours, stay in Home until someone sets Night by hand.",
  "Report anything that still needs a person, like an open garage door."],
 "Double tap the switch and check that the mode changes. On another night, go to bed without it and check that the backup sets Night.",
 "The double tap is the main action. The automatic rule only catches the nights when everyone forgets.",
 "/automation/daily-routines/bedtime-routine.html"))

shop_rows = [
 ("Hub", "Any hub that runs rules locally (see \"Pick the hub\")", "Central spot, wired to the router", "1", "Pick this first. Check every device below against it."),
 ("Motion sensor", "Aeotec SmartThings Motion Sensor", "Hallway or laundry", "1", "Zigbee. Needs a Zigbee radio."),
 ("Smart switch", "Leviton DG15S Zigbee switch", "Same room as the motion sensor", "1", "Zigbee. Needs a Zigbee radio."),
 ("Bathroom multisensor", "Aeotec TriSensor 8", "Bathroom", "1", "Z-Wave. Needs a Z-Wave radio. Not Apple, Google or Alexa."),
 ("Smart dimmer", "TP-Link Tapo S505D", "Bathroom or living room", "1", "Matter over Wi-Fi. Works with most hubs."),
 ("Washer power-monitoring plug", "Zooz ZEN15, a Z-Wave plug-in switch that measures power", "Washer", "1", "<b>Z-Wave. Not for Apple, Google or Alexa.</b> See the note below."),
 ("Vibration sensor", "THIRDREALITY Zigbee Vibration Sensor", "Dryer", "1", "Zigbee. Needs a Zigbee radio."),
 ("Leak sensor", "THIRDREALITY WL2", "Water heater, washer, sink", "2", "Zigbee. Needs a Zigbee radio."),
 ("Contact sensor", "SONOFF SenseGuard Gen2", "Closet or pantry door", "1", "Zigbee. Needs a Zigbee radio."),
 ("Garage tilt sensor", "THIRDREALITY Garage Tilt Sensor", "Garage door", "1", "Zigbee. Needs a Zigbee radio."),
]
shop = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td class='n'>{d}</td><td class='small'>{e}</td></tr>" for a,b,c,d,e in shop_rows)

H = f'''<!doctype html><html><head><meta charset="utf-8"><title>Starter house setup guide</title>
<link rel="stylesheet" href="hac-print.css"></head><body>
<section class="cover"><img src="cover-starter.svg"></section>

<section class="chapter">{head("Before you start", "Welcome")}
<p class="lede">You're starting this the right way.</p>
<p>Most people buy a pile of gadgets, wire them up in a weekend, and end up with a house that feels random. Lights turn on when nobody's there. Alerts fire at 3 AM. The family gives up on it.</p>
<p>This guide helps you skip that part. By the end of your first month you'll have one hub, about ten devices, and a handful of automations your whole household actually likes.</p>
<h3>What is inside</h3>
<ol class="toc"><li>How to use this guide</li><li>The rules for a starter house</li><li>Pick the hub</li><li>The four-weekend plan</li><li>Shopping list</li><li>Room-by-room checklists</li><li>Step-by-step walkthroughs <small>(11 recipes, one per page)</small></li><li>Add modes, then routines</li><li>What to skip in the first month</li><li>Troubleshooting</li><li>Notes page</li></ol>
</section><section class="chapter">{head("Chapter 1", "How to use this guide", "A few minutes here makes the rest of the month easier.")}
<p>Print it. Keep it near the hub. Check the boxes as you go. It feels good to see them fill up.</p>
<p>Do one room at a time. Finish a room, live with it for a week, then move on. A slow start beats a house nobody trusts.</p>
<p>Every walkthrough is written in plain steps that work on any hub. A few tips name a specific hub as one example among many. Each walkthrough links to the full recipe on the website for platform notes and failure modes.</p>
<div class="callout warn"><b class="lbl">Disclosure and safety</b><p>Amazon product links on the website are affiliate links, and the site earns from qualifying purchases. See {W}/disclosure.html. Check that every device works with your hub before you buy. Follow the maker's instructions and local electrical codes. Hire an electrician for wiring you are not comfortable with.</p></div>
</section>

<section class="chapter">{head("Chapter 2", "The rules for a starter house", "Five simple rules. They are the difference between a house that feels random and one your family relies on.")}
<ol class="rules">
<li><b>Pick one hub and stick with it.</b>Three apps on day one means three places to look when something breaks.</li>
<li><b>Choose local first.</b>Pick a hub and devices that run locally, so they keep working when the internet goes down. Z-Wave, Zigbee, Matter over Thread, and HomeKit are all good examples.</li>
<li><b>Keep the wall switches working.</b>Every light keeps a normal wall control. Guests, grandparents and babysitters should never need an app.</li>
<li><b>One room at a time.</b>Finish a room, live with it for a week, then move on. A small win you trust beats a big project you're always fixing.</li>
<li><b>Save the risky stuff for later.</b>Leave locks, heaters, and garage door control for later. You will be ready for them once the basics feel boring.</li>
</ol>
{tip("If you ever feel stuck, come back to this page. Almost every problem in a first month traces back to breaking one of these five rules.", "Keep this handy")}
</section>

<section class="chapter">{head("Chapter 3", "Pick the hub", "The hub is the brain of the house. The good news: you do not need the perfect one. You need one you will keep.")}
<p>Home Assistant, Hubitat, SmartThings, Homey, HomeSeer, Apple Home, Google Home, and Alexa can all run this plan. The best pick runs your rules locally and supports the devices you want. If you already own one, start there.</p>
<div class="callout"><b class="lbl">Check the radios</b><p>Devices talk to the hub over a radio type. Z-Wave devices need a hub with a Z-Wave radio. Zigbee devices need a hub with a Zigbee radio. Apple Home and Google Home have neither, and Alexa has Zigbee only on some Echo models. On those platforms, look for Matter versions of each device. The shopping list marks the radio type for every item.</p></div>
<h3>Do these three things on day one</h3>
{chk("Give the hub a fixed IP address on your router.", "Turn on its backups.", "Install the hub's app on at least two phones, so alerts reach more than one person.")}
<p>Read more: <span class="url">{W}/getting-started/choose-the-right-platform.html</span></p>
<h3>Naming devices</h3>
<p>Name every device by room and job. "Laundry Washer Power" is better than "Zooz ZEN15 plug". Good names make every rule easier to read, and every alert easier to act on.</p>
<p>Mixing radio types is fine if your hub supports them. Mains-powered switches and plugs usually act as repeaters and make the mesh stronger. Install those before the battery sensors in far rooms.</p>
{win("A hub that is set up, backed up and reachable from two phones. That is a real foundation.")}
</section>

<section class="chapter">{head("Chapter 4", "The four-weekend plan", "One small project per weekend. Each one ends with something that works, so you build confidence as you go.")}
<table><thead><tr><th>When</th><th>Room</th><th>Devices</th><th>Recipes</th></tr></thead><tbody>
<tr><td><b>Weekend 1</b></td><td>Hallway or laundry lights</td><td>Switch, motion sensor</td><td>Lights on motion. A week later, lights off after motion.</td></tr>
<tr><td><b>Weekend 2</b></td><td>Laundry</td><td>Washer power-monitoring plug (Zooz ZEN15), vibration sensor</td><td>Washer done, dryer done. Log three loads first.</td></tr>
<tr><td><b>Weekend 3</b></td><td>Bathroom</td><td>Multisensor, dimmer</td><td>Bathroom night-light</td></tr>
<tr><td><b>Weekend 4</b></td><td>Safety and status</td><td>Leak sensors, contact sensor, tilt sensor</td><td>Leak alerts, closet light, garage open alert, low-battery alerts</td></tr>
<tr><td><b>After that</b></td><td>Whole house</td><td>None new</td><td>Modes, away mode, bedtime routine</td></tr>
</tbody></table>
{tip("Running late is fine. If a weekend slips, the plan just moves a week. Nothing here depends on speed.", "Go at your pace")}
{win("By the end of weekend 4 you have lights that follow you, laundry alerts, a bathroom night-light and leak, garage and battery alerts. Modes and routines come after.")}
</section>

<section class="chapter">{head("Chapter 5", "Shopping list", "These are the products the website recommends for a starter house. You can pick the &quot;good enough&quot; option or the step up from the device guide.")}
<p class="small">Device guide: <span class="url">{W}/getting-started/device-guide.html</span></p>
<table class="tight"><thead><tr><th>Job</th><th>Product</th><th>Where it goes</th><th>Qty</th><th>Works with</th></tr></thead><tbody>{shop}</tbody></table>
<p>That is ten devices plus the hub. Prices and stock change, so check the current listing. Also buy spare batteries for each sensor, and double-sided mounting tape.</p>
{warn("The Zooz ZEN15 is a Z-Wave plug-in switch that measures how much power the washer draws. It needs a hub with a Z-Wave radio. It does not work with Apple Home, Google Home or Alexa. " + ALT_PLUG, "Using Apple Home, Google Home or Alexa?")}
<div class="keep"><h3>Before you order</h3>
{chk("Each device is listed as working with your hub, including its radio type.", "Switch and dimmer boxes have the wiring the device needs (check for a neutral wire if required).", "The washer's load is within the power-monitoring plug's rating.", "Buy one of each first. Buy more of what works.")}</div>
</section>

<section class="chapter">{head("Chapter 6", "Room-by-room checklists", "Tick these off as you go. Each box is a small win.")}
<div class="boxgrid">
<div class="box"><h3>Whole house</h3>{chk("Hub set up and updated","Fixed IP address set on the router","Hub backups turned on","Modes created: Day, Evening, Night, Away","Notification app installed for at least two people","Mains switches and plugs paired before far battery sensors","Every device named by room and job")}</div>
<div class="box"><h3>Hallway or laundry lights</h3>{chk("Smart switch installed, paddle works without the hub","Motion sensor placed to see the entry path","Lights on motion built and tested at night","Lights on motion tested in daylight (stays off)","Lived with it for one week","Lights off after motion added","Sat still past the timeout to test")}</div>
<div class="box"><h3>Laundry</h3>{chk("Power-monitoring plug on the washer, load within its rating","Vibration sensor on the dryer","Three loads logged before alerts","Thresholds written down","Washer alert gives one notification per load","Dryer alert gives one notification per load")}</div>
<div class="box"><h3>Bathroom</h3>{chk("Dimmer installed, paddle still works","Multisensor away from the shower plume and towels","Night-light at 10 percent in Night mode","Off timeout tested during a shower","Optional: humidity reading checked for a future fan recipe")}</div>
<div class="box"><h3>Kitchen and water</h3>{chk("Leak sensor under the water heater","Leak sensor behind the washer or dishwasher","Optional: leak sensor under the kitchen sink","Wet towel test done for every sensor","Two people received the alert")}</div>
<div class="box"><h3>Closet, pantry, and garage</h3>{chk("Contact sensor parts lined up","Door tested ten times in a row","Tilt sensor on the top garage panel","10 minute open alert tested","Bedtime garage check tested")}</div>
</div>
<div class="box" style="margin-top:16px"><h3>Before you call it done</h3>{chk("Low-battery alert tested with a weak battery","Away mode tested with everyone gone and with one person home","Night mode tested by hand and by the backup rule","Someone else in the house can work the lights without the app","Device names and thresholds written on the notes page")}</div>
</section>

<section class="chapter">{head("Chapter 7", "Step-by-step walkthroughs", "Eleven recipes, one per page. Each one has the same shape: a trigger, conditions, and actions.")}
<p>Build the smallest version first. Add extras only when daily use shows you need them. Every walkthrough ends with a quick test, so you know it works before you rely on it.</p>
{tip("Follow the order of the four-weekend plan. Walkthroughs 10 and 11 come last, after the room recipes have run well for a few weeks.", "Where to start")}
{win("By the last page of this chapter you will have eleven tested automations. That is a starter house most people never reach.")}
</section>
{"".join(R)}

<section class="chapter">{head("Chapter 8", "Add modes, then routines", "Modes are where the house starts to feel calm and joined up.")}
<p>Once the devices work on their own, add home modes. Day, Evening, Night, and Away are enough.</p>
<p>Modes make every later recipe simpler. A rule can check one mode instead of five conditions.</p>
<p>Build Away mode and the bedtime routine (walkthroughs 10 and 11) only after the room recipes have run well for a few weeks.</p>
{win("Four modes that every rule can lean on, and a house that knows when you are home, away or asleep.")}
<p class="kicker" style="margin-top:40px">Chapter 9</p><h2>What to skip in the first month</h2><div class="rule"></div>
<p class="lede">These are great later. Skipping them now keeps your first month safe and stress-free.</p>
<ol class="rules">
<li><b>Smart locks and auto-closing garage doors.</b>Get alerts working first.</li>
<li><b>Plugs on heaters or cooking appliances.</b>Not safe for general-purpose plugs.</li>
<li><b>Voice-only control.</b>Fine as an extra, not as the only way to turn on a light.</li>
<li><b>Bundles of cheap devices.</b>Test one, then buy more of what works.</li>
</ol>
</section>

<section class="chapter">{head("Chapter 10", "Troubleshooting", "Something not quite right? That is normal. Most fixes take a few minutes.")}
<table><thead><tr><th style="width:42%">Problem</th><th>First thing to try</th></tr></thead><tbody>
<tr><td>Light turns on after you reach the switch</td><td>Move the sensor so it sees the entry path earlier.</td></tr>
<tr><td>Light turns on in daylight</td><td>Add a light-level condition. Test on a bright overcast day too.</td></tr>
<tr><td>Light turns off while someone sits still</td><td>Raise the timeout, or watch a second sensor.</td></tr>
<tr><td>Washer or dryer alert comes more than once</td><td>The finish delay is shorter than a normal pause. Make it longer.</td></tr>
<tr><td>No washer alert at all</td><td>Check that the "running" marker is set during a load.</td></tr>
<tr><td>A battery sensor drops off</td><td>Add a mains-powered switch or plug between it and the hub.</td></tr>
<tr><td>A device will not pair at all</td><td>Check that your hub has the radio the device needs (Z-Wave, Zigbee or Matter).</td></tr>
<tr><td>A rule stops working when the internet is down</td><td>Check that the devices and rule run locally on the hub.</td></tr>
</tbody></table>
{tip("Change one thing at a time, then test again. It is slower for a minute and much faster overall.")}
</section>

<section class="chapter">{head("Chapter 11", "Notes", "Write it down once and you will never have to hunt for it again.")}
<table class="notes"><thead><tr><th>Device name</th><th>Room</th><th>Threshold or timeout</th><th>Battery size</th></tr></thead><tbody>{"<tr><td></td><td></td><td></td><td></td></tr>"*10}</tbody></table>
<h3>Hub details</h3>
<table class="notes"><tbody><tr><td style="width:40%"><b>Hub IP address</b></td><td></td></tr><tr><td><b>Last backup date</b></td><td></td></tr><tr><td><b>Washer running / finished watts</b></td><td></td></tr><tr><td><b>Dryer longest pause</b></td><td></td></tr></tbody></table>
<p class="small" style="margin-top:30px">Home Automation Cookbook. For personal use. Please do not share or resell this file. More recipes at {W}.</p>
</section></body></html>'''
assert "\u2014" not in H and "github" not in H.lower()
(HERE / "guide.html").write_text(H, encoding="utf-8")
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
   f"--print-to-pdf={OUT}", (HERE / "guide.html").as_uri()], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, timeout=180)
print("PDF ->", OUT)
