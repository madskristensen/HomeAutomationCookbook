---
layout: automation
title: Speaker Volume Presets - Smart Audio Management
description: Set and recall speaker volume presets for different occasions. Low, medium, and loud settings for every room.
keywords: speaker volume automation, audio presets, volume control scenes, smart speaker volume, volume management, consistent volume, audio scenes
---

# Speaker volume presets

Volume presets for all speakers save time and create consistency. Define levels for low, medium, and loud to easily adjust for any occasion with one command.

## Use cases

<div class="use-case-grid">
  <div class="use-case-card">
    <h4>Daily Convenience</h4>
    <ul>
      <li><strong>Normal Day</strong> - Always play music at pleasant levels when home</li>
      <li><strong>One-Button Control</strong> - Single action adjusts all rooms</li>
      <li><strong>Consistent Experience</strong> - Voice assistant and music always at predictable volume</li>
    </ul>
  </div>
  <div class="use-case-card">
    <h4>Special Occasions</h4>
    <ul>
      <li><strong>Party Mode</strong> - Quick adjustment for gatherings and celebrations</li>
      <li><strong>Time-Based</strong> - Automatically adjust volume throughout the day</li>
    </ul>
  </div>
</div>

## Products needed

<div class="product-section">
  <h4>Essential Equipment</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Smart Speakers/Music System</strong>
      <div class="product-details">
        Brands: Sonos, Amazon Echo, Google Home, Apple HomePod<br>
        Individual or grouped speakers • Remote volume control via automation
      </div>
    </div>
  </div>
</div>

<div class="product-section">
  <h4>Optional Enhancements</h4>
  
  <div class="product-list">
    <div class="product-item">
      <strong>Buttons or Switches</strong>
      <div class="product-details">
        Physical controls for volume presets
      </div>
    </div>
    
    <div class="product-item">
      <strong>Voice Commands</strong>
      <div class="product-details">
        "Set volume to party mode" for hands-free control
      </div>
    </div>
  </div>
</div>

## Logic

<div class="automation-example">IF volume preset changes to "Low"
THEN set all speakers to 20-30%
ELSE IF preset is "Medium"
THEN set all speakers to 40-50%
ELSE IF preset is "Loud"
THEN set all speakers to 70-80%</div>

<div class="info-box">
  <strong>🔊 Volume Level Guide</strong>
  <ul>
    <li><strong>Low (Quiet/Background):</strong> Voice assistants 30%, Music 20-25% - Normal day, working, early morning</li>
    <li><strong>Medium (Comfortable):</strong> Voice assistants 50%, Music 40-50% - Entertaining, cooking, cleaning</li>
    <li><strong>Loud (Party):</strong> Voice assistants 60%, Music 70-80% - Parties, dancing, exercising</li>
  </ul>
</div>

<div class="setup-steps">
  <div class="setup-step">
    <h4>Triggers</h4>
    <ul>
      <li>Home goes into Home mode (set to Low)</li>
      <li>Button/switch pressed</li>
      <li>Voice command: "Set volume to [low/medium/loud]"</li>
      <li>Time-based (e.g., 10 PM → Low)</li>
    </ul>
  </div>
  
  <div class="setup-step">
    <h4>Conditions</h4>
    <strong>Note:</strong> Immediate response typically desired
  </div>
  
  <div class="setup-step">
    <h4>Actions</h4>
    <ul>
      <li>Set volume of all speakers to preset levels</li>
      <li>Can be per-room or whole-house</li>
    </ul>
  </div>
</div>

## Advanced features

### Time-based auto-adjustment

Automatically adjust volume throughout the day:

Create automation with these elements:
- **Triggers:** Multiple times - 6am, 10am, 6pm, 10pm
- **Actions based on time:**
  - **6am-10am:** Set to Low (morning quiet)
  - **10am-6pm:** Set to Medium (daytime)
  - **6pm-10pm:** Set to Medium (evening)
  - **10pm+:** Set to Low (night quiet hours)

### Ungroup speakers during reset

Dissolve temporary speaker groups:

Create automation with these elements:
- **Trigger:** Time is 4:00 AM daily
- **Action 1:** Ungroup all Sonos speakers (unjoin command)
- **Action 2:** Reset volume preset to Low

### Activity-based presets

Different presets for different activities:

**Options:**
- Podcast (voice-optimized, low volume)
- Music (balanced, medium volume)
- Party (loud, all rooms)
- Movie (low volume, living room only)
- Sleep (minimal, bedroom only)

## Failure modes

### Issue: Volumes change unexpectedly

**Causes:**
- Family members manually adjusting
- Multiple automations conflicting
- Daily reset not accounting for special events
- Time-based adjustments too aggressive

**Solutions:**
✅ Communicate volume preset system with household
✅ Add manual override flag to skip auto-adjustments
✅ Review all volume automations for conflicts
✅ Add "party mode" that disables auto-adjustments
✅ Use longer reset interval (weekly instead of daily)

### Issue: Some speakers not adjusting

**Causes:**
- Speaker offline or unreachable
- Entity ID incorrect in automation
- Speaker doesn't support volume control
- Network connectivity issues

**Check:**
- ✅ Verify all speakers show as online in app
- ✅ Test manual volume adjustment for each speaker
- ✅ Check entity IDs match current speaker names
- ✅ Review automation logs for errors
- ✅ Check network connectivity and WiFi signal strength

### Issue: Volume too loud/quiet for specific rooms

**Causes:**
- Room acoustics differ significantly
- Speaker types vary (Echo vs Sonos)
- Room size not accounted for
- Personal preference varies

**Solutions:**
✅ Use room-specific presets (shown above)
✅ Adjust percentages per room acoustics
✅ Test in actual use conditions
✅ Create custom presets for problematic rooms
✅ Consider different speaker types need different levels

---

## Related recipes
- [Play music when shower starts](/automation/entertainment/shower-music.html)
- [Welcome home music automation](/automation/entertainment/welcome-home-music.html)
- [Control music with physical switch](/automation/entertainment/music-switch-control.html)

<div class="page-navigation">
  <a href="/automation/entertainment/index.html">Back to entertainment</a>
  <a href="/automation/">View All Automations →</a>
</div>
