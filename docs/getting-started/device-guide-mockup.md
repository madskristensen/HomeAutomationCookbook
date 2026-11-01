---
layout: guide
title: Devices by hub (mockup)
description: Mockup of a hub-first devices page. Pick your hub and see one device per job.
sitemap: false
noindex: true
---

<div class="dm" markdown="0">
<h1>Devices that work with your hub</h1>
<p>Pick your hub. Each job shows one device for that hub's radio.</p>
<fieldset class="dm-hubs"><legend>Your hub</legend>
<label><input type="radio" name="hub" value="alexa" data-proto="zigbee" data-note="Echo models with a built-in Zigbee hub. Matter also works."> Alexa</label>
<label><input type="radio" name="hub" value="ha" data-proto="zigbee" data-note="Needs a Zigbee or Z-Wave radio. Zigbee is the easy start."> Home Assistant</label>
<label><input type="radio" name="hub" value="hubitat" data-proto="zwave" data-note="Zigbee and Z-Wave both built in. Z-Wave picks shown."> Hubitat</label>
<label><input type="radio" name="hub" value="smartthings" data-proto="zigbee" data-note="Zigbee built in. Matter also works."> SmartThings</label>
<label><input type="radio" name="hub" value="homey" data-proto="zigbee" data-note="Homey Pro has Zigbee and Z-Wave. Zigbee picks shown."> Homey</label>
<label><input type="radio" name="hub" value="apple" data-proto="matter" data-note="Use Matter devices."> Apple Home</label>
</fieldset><p class="dm-note" id="dm-note" hidden></p>
<fieldset class="dm-protos"><legend>Radio</legend><label><input type="radio" name="proto" value="zigbee"> Zigbee</label><label><input type="radio" name="proto" value="zwave"> Z-Wave</label><label><input type="radio" name="proto" value="matter"> Matter</label></fieldset>
<noscript><p>All three radios are listed for each job below.</p></noscript>
<section class="dm-job" id="switch"><h2>Smart switch or dimmer</h2><p class="dm-use">Recipes that light a room, scenes, and double-tap controls.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B000U39QL6/ref=nosim?tag=madsk0f-20">Leviton DG15S Zigbee switch</a></p><p>On/off switch. The paddle stays a normal wall control.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0FX36Z8VN/ref=nosim?tag=madsk0f-20">UltraPro Z-Wave Long Range Dimmer</a></p><p>Dims and stays a normal wall control.</p><p class="dm-alt">On/off only: <a href="https://www.amazon.com/dp/B0FX3CTLW2/ref=nosim?tag=madsk0f-20">UltraPro Z-Wave Long Range On/Off Switch</a></p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0C2B8SP3W/ref=nosim?tag=madsk0f-20">TP-Link Tapo S505D Matter Smart Dimmer Switch</a></p><p>Matter dimmer. The paddle stays a normal wall control.</p></div>
</section>
<section class="dm-job" id="plug"><h2>Smart plug</h2><p class="dm-use">Lamps, fans, and small appliances.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0BPY2KRHH/ref=nosim?tag=madsk0f-20">THIRDREALITY Zigbee Smart Plug with power monitoring</a></p><p>Switches the load and reports power too.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0CQX4JFV2/ref=nosim?tag=madsk0f-20">Minoston 800 Series Z-Wave plug</a></p><p>Simple indoor on/off plug.</p><p class="dm-alt">Outdoors: <a href="https://www.amazon.com/dp/B0B7MLX1ZC/ref=nosim?tag=madsk0f-20">Minoston 800 Series outdoor Z-Wave plug</a></p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job" id="power"><h2>Power-monitoring plug</h2><p class="dm-use">Know when a TV, white noise machine, or charger is on.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0BPY2KRHH/ref=nosim?tag=madsk0f-20">THIRDREALITY Zigbee Smart Plug with power monitoring</a></p><p>Cheaper Zigbee pick with real-time power readings.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GXW9HZRK/ref=nosim?tag=madsk0f-20">Ezlo 800 Series Z-Wave smart plug</a></p><p>Sees the draw of a TV or toothbrush charger in my house.</p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job" id="motion"><h2>Motion sensor</h2><p class="dm-use">Lights on when someone walks in.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B095TZTGNB/ref=nosim?tag=madsk0f-20">Aeotec SmartThings Motion Sensor</a></p><p>My favorite for fast reactions.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0DCL43CS2/ref=nosim?tag=madsk0f-20">Zooz ZSE70 Outdoor/Indoor Motion Sensor</a></p><p>Long Range radio reaches a garage or driveway.</p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job" id="presence"><h2>Presence sensor</h2><p class="dm-use">Keep lights on while someone sits still.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GYJ3LQ5W/ref=nosim?tag=madsk0f-20">Besisglas Zigbee Human Presence Sensor</a></p><p>Sees a person who is still, like at a desk.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-gap">GAP: needs a pick</p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job" id="contact"><h2>Door and window sensor</h2><p class="dm-use">Open door alerts, window and thermostat recipes.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GKFB3XCL/ref=nosim?tag=madsk0f-20">SONOFF SenseGuard Gen2 Zigbee contact sensor</a></p><p>The door itself is the trigger. Easy for guests.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B09JKKLRLW/ref=nosim?tag=madsk0f-20">Zooz ZSE41 800LR Open/Close XS Sensor</a></p><p>Small, with a Long Range radio.</p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job" id="button"><h2>Smart button</h2><p class="dm-use">Bedtime, quiet mode, pet feeding, and scene buttons.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-gap">GAP: needs a pick</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-gap">GAP: needs a pick</p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job" id="leak"><h2>Leak sensor</h2><p class="dm-use">Water where it should not be.</p>
<div class="dm-opt" data-proto="zigbee"><p class="dm-tag">Zigbee</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0GK19F6Z2/ref=nosim?tag=madsk0f-20">THIRDREALITY WL2 Zigbee water leak sensor</a></p><p>Test the alert and make the source obvious.</p></div>
<div class="dm-opt" data-proto="zwave"><p class="dm-tag">Z-Wave</p><p class="dm-pick"><a href="https://www.amazon.com/dp/B0FSKFCKTB/ref=nosim?tag=madsk0f-20">NEO Z-Wave Plus 700 water leak sensor</a></p><p>Test the alert and make the source obvious.</p></div>
<div class="dm-opt" data-proto="matter"><p class="dm-tag">Matter</p><p class="dm-gap">GAP: needs a pick</p></div>
</section>
<section class="dm-job"><h2>Wi-Fi and HomeKit</h2><p>Wi-Fi devices skip the hub but depend on the cloud and your router. Apple Home works best with Matter devices, so pick Matter above.</p></section></div>
<style>
.dm fieldset{border:1px solid #ddd;border-radius:8px;padding:.5rem .75rem;margin:0 0 1rem;display:flex;flex-wrap:wrap;gap:.25rem 1rem;min-width:0}
.dm label{white-space:nowrap}.dm-job{border-top:1px solid #e0e0e0;padding:.75rem 0}
.dm-job h2{margin:.25rem 0}.dm-use{color:#5d6d75;margin:0 0 .5rem}
.dm-opt{border:1px solid #e6e9ea;border-radius:8px;padding:.5rem .75rem;margin:.5rem 0;overflow-wrap:anywhere}
.dm-opt p{margin:.2rem 0}.dm-tag{font-size:.8rem;font-weight:600;text-transform:uppercase;color:#5d6d75}
.dm-pick{font-weight:600}.dm-alt{font-size:.9rem;color:#5d6d75}
.dm-gap{font-weight:700;color:#8a3b12;background:#fff1e6;padding:.25rem .5rem;border-radius:4px;display:inline-block}
.dm.js .dm-opt{display:none}.dm.js .dm-opt.on{display:block}
</style>
<script>
(function(){var r=document.querySelector('.dm');r.classList.add('js');
function proto(p){r.querySelectorAll('input[name=proto]').forEach(function(i){i.checked=i.value==p});
r.querySelectorAll('.dm-opt').forEach(function(e){e.classList.toggle('on',e.dataset.proto==p)});}
r.querySelectorAll('input[name=hub]').forEach(function(i){i.addEventListener('change',function(){proto(i.dataset.proto);var n=document.getElementById('dm-note');n.textContent=i.dataset.note;n.hidden=false;});});
r.querySelectorAll('input[name=proto]').forEach(function(i){i.addEventListener('change',function(){proto(i.value)})});
proto('zigbee');})();
</script>
