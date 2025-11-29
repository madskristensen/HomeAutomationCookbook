---
layout: default
title: FAQ
---

# Frequently asked questions

Quick answers to common smart home questions.

## Getting started

<details markdown="1">
<summary>Do I need a hub?</summary>

It depends on your platform:
- **Yes**: Home Assistant, Hubitat, SmartThings (for Zigbee/Z-Wave)
- **No**: Google Home, Alexa (WiFi only)
- **Maybe**: HomeKit (Apple device acts as hub)
</details>

<details markdown="1">
<summary>What's the difference between WiFi, Zigbee, and Z-Wave?</summary>

**WiFi (2.4GHz/5GHz)**
- ✅ No hub needed, fast, easy setup
- ❌ Congests network, higher power usage

**Zigbee**
- ✅ Mesh network, low power, reliable
- ❌ Requires hub, 2.4GHz only

**Z-Wave**
- ✅ No interference, very reliable, mesh
- ❌ Requires hub, more expensive

**Recommendation**: Zigbee for most users (good balance)
</details>

<details markdown="1">
<summary>How much does it cost to start?</summary>

**Minimal** ($100-200)
- Budget smart speaker: $50
- 2-3 smart bulbs: $30-60
- Smart plug: $10-20

**Recommended** ($300-500)
- Quality hub/speaker: $100-150
- Starter kit (bulbs): $100
- Smart plugs (3): $50
- Motion sensor: $20-30
- Smart outlet: $30
</details>

<details markdown="1">
<summary>Which platform should I choose?</summary>

**For beginners**: Google Home or Alexa
**For Apple users**: HomeKit
**For privacy**: Home Assistant, Hubitat, or HomeKit
**For customization**: Home Assistant
**For local control**: Home Assistant or Hubitat
**For Samsung users**: SmartThings
</details>

## Devices

<details markdown="1">
<summary>Can I mix brands?</summary>

Yes! Most platforms support multiple brands. Check compatibility first.

**Tips**:
- Choose a standard (WiFi, Zigbee, Z-Wave)
- Verify platform support
- Read reviews for integration quality
- Consider Matter devices (universal standard)
</details>

<details markdown="1">
<summary>Do smart bulbs work with normal switches?</summary>

**Smart Bulbs**: Switch must stay ON (control via app/voice)
- Pro: Cheap, easy to install
- Con: Confusing for guests, switch must stay on

**Smart Switches**: Replace wall switch
- Pro: Works like normal switch, controls any bulb
- Con: Requires wiring, more expensive

**Recommendation**: Smart switches for fixed lights, smart bulbs for lamps
</details>

<details markdown="1">
<summary>How long do batteries last?</summary>

Typical battery life:
- **Door/window sensors**: 1-2 years
- **Motion sensors**: 6-12 months
- **Smart locks**: 6-12 months
- **Temperature sensors**: 1-2 years

Use quality alkaline or lithium batteries for best results.
</details>

<details markdown="1">
<summary>Are smart devices secure?</summary>

**It depends**:
- ✅ Reputable brands with updates
- ✅ Local control options
- ✅ Strong passwords + 2FA
- ❌ Cheap unknown brands
- ❌ Cloud-only devices
- ❌ Outdated firmware

See [Security Best Practices →](/best-practices/#security)
</details>

## Automation

<details markdown="1">
<summary>What can I automate?</summary>

Common automations:
- **Lighting**: Motion-based, schedule, presence
- **Climate**: Temperature scheduling, away mode
- **Security**: Arm/disarm, alerts, recording
- **Energy**: Off when away, peak hour management
- **Convenience**: Good morning, good night routines

[Browse Automation Recipes →](/automation/)
</details>

<details markdown="1">
<summary>Why isn't my automation working?</summary>

**Troubleshooting checklist**:
1. ✅ Automation enabled?
2. ✅ Conditions met? (time, presence, etc.)
3. ✅ Devices online?
4. ✅ Triggers configured correctly?
5. ✅ Check logs for errors
6. ✅ Test manually
</details>

<details markdown="1">
<summary>How do I make automations reliable?</summary>

**Best practices**:
- Use multiple trigger conditions
- Add appropriate delays
- Include fallback actions
- Test edge cases
- Keep it simple
- Monitor performance
</details>

<details markdown="1">
<summary>Can automations run without internet?</summary>

**It depends**:
- **Home Assistant**: Yes (fully local)
- **Hubitat**: Yes (fully local)
- **HomeKit**: Yes (local hub)
- **SmartThings**: Partial (some local, some cloud)
- **Google Home/Alexa**: No (requires cloud)
</details>

## Network and technical

<details markdown="1">
<summary>How many devices can I have?</summary>

**Typical limits**:
- **WiFi**: 50-100 devices per router (varies)
- **Zigbee**: 100+ devices (mesh network)
- **Z-Wave**: 232 devices (protocol limit)

**Router capacity matters most** - upgrade if congested
</details>

<details markdown="1">
<summary>Do I need a special router?</summary>

Not necessarily, but helpful:
- ✅ Dual-band (2.4GHz + 5GHz)
- ✅ Supports many clients
- ✅ Guest network capability
- ✅ Good 2.4GHz range

Consider mesh WiFi for larger homes (250+ sqm)
</details>

<details markdown="1">
<summary>What is VLAN and do I need it?</summary>

**VLAN** = Separate network segments

**Benefits**:
- Isolate IoT devices
- Better security
- Network organization
- Traffic management

**Who needs it**:
- Advanced users
- Security-conscious
- Large deployments
- Enterprise equipment

**Beginners**: Guest network is enough
</details>

<details markdown="1">
<summary>My WiFi is slow. Is it my smart devices?</summary>

Possibly. Smart devices can congest 2.4GHz.

**Solutions**:
1. Move computers/phones to 5GHz
2. Use Zigbee instead of WiFi devices
3. Upgrade router
4. Reduce device polling
5. Use wired connections where possible
</details>

## Platform-specific

<details markdown="1">
<summary>Can I switch platforms later?</summary>

**Mostly yes**, but:
- ✅ WiFi devices: Usually compatible
- ✅ Zigbee/Z-Wave: Need compatible hub
- ⚠️ Platform-specific: May not work elsewhere

**Minimize lock-in**:
- Choose open standards
- Avoid cloud-only devices
- Document setup
- Consider Matter devices
</details>

<details markdown="1">
<summary>What is Matter?</summary>

**Matter** = New universal smart home standard

**Benefits**:
- Works across platforms
- Local control
- Better security
- Future-proof

**Status**: Growing device support (2024+)

**Recommendation**: Good choice for new purchases
</details>

<details markdown="1">
<summary>Do I need a subscription?</summary>

**Usually no**, but some features require it:

**Free**:
- Basic automation
- Local control
- App access

**Paid** (optional):
- Cloud video storage
- Advanced analytics
- Professional monitoring
- Extended features

Examples:
- Nest Aware (video history)
- Ring Protect (video storage)
- SmartThings Storage (extra space)
</details>

## Troubleshooting

<details markdown="1">
<summary>My device won't connect</summary>

**Steps**:
1. Restart device (unplug 30 seconds)
2. Restart hub/router
3. Check WiFi signal strength
4. Verify 2.4GHz network available
5. Reset device and re-pair
6. Update firmware
</details>

<details markdown="1">
<summary>Devices keep disconnecting</summary>

**Common causes**:
- Weak WiFi signal
- Router overloaded
- Interference
- Firmware issues
- Power problems

**Solutions**:
- Add WiFi extender/mesh
- Reduce device count per AP
- Switch to Zigbee
- Update firmware
- Check power supply quality
</details>

<details markdown="1">
<summary>Automation is slow</summary>

**Causes**:
- Cloud processing
- Network latency
- Polling delay
- Device response time

**Solutions**:
- Use local processing
- Reduce polling intervals
- Optimize automations
- Check device placement
- Upgrade hub
</details>

<details markdown="1">
<summary>How do I factory reset a device?</summary>

**Varies by device**, but common methods:
- Press reset button 5-10 seconds
- Power cycle 5 times rapidly
- Hold button during power on
- Check manual for specific steps

**Note**: Reset removes all pairing and configuration
</details>

## Privacy and data

<details markdown="1">
<summary>What data do smart devices collect?</summary>

**Typical data**:
- Device usage patterns
- Voice recordings (if enabled)
- Video footage (cameras)
- Sensor readings
- Location (phone app)

**Varies by brand** - read privacy policies
</details>

<details markdown="1">
<summary>How can I protect my privacy?</summary>

**Best practices**:
1. Use local control platforms
2. Disable analytics/telemetry
3. Review camera placement
4. Use separate IoT network
5. Read privacy policies
6. Avoid unnecessary features
7. Regular security audits

[Privacy guide →](/best-practices/#privacy-protection)
</details>

<details markdown="1">
<summary>Can companies access my data?</summary>

**It depends**:
- **Cloud devices**: Yes (read terms)
- **Local devices**: Usually no
- **Encryption**: Reduces access

**Most private**: Home Assistant or Hubitat (fully local)
**Moderate**: HomeKit (encrypted)
**Less private**: Google, Amazon, cloud-based
</details>

## Cost and value

<details markdown="1">
<summary>Is it worth the investment?</summary>

**Benefits**:
- Convenience and comfort
- Energy savings (5-15%)
- Security improvements
- Home value increase
- Accessibility features

**Consider**:
- Your lifestyle needs
- Technical comfort
- Budget constraints
- Long-term value
</details>

<details markdown="1">
<summary>How much can I save on energy?</summary>

**Potential savings**:
- **Smart thermostat**: 10-23% on heating/cooling
- **Smart lighting**: 50-75% on lighting costs
- **Smart plugs**: 5-10% by eliminating standby power

**ROI timeline**: Typically 2-5 years
</details>

<details markdown="1">
<summary>Which devices save the most money?</summary>

**Best ROI**:
1. Smart thermostat
2. Smart power strips
3. LED smart bulbs (if replacing incandescent)
4. Energy monitoring plugs
5. Smart irrigation

**Not for savings**:
- Voice assistants
- Smart locks
- Cameras
- Entertainment devices
</details>

---

## Still have questions?

- Browse detailed guides in each section
- Join community forums
- Check platform-specific documentation
- [Contact us](https://github.com/madskristensen/HomeAutomationCookbook/issues)
