---
layout: default
title: Choose the right platform
---

# Home automation platforms

Choosing the right platform is crucial for your smart home success. Here's a detailed comparison of popular options.

## Platform comparison

| Feature | ![Home Assistant](/assets/img/logos/homeassistant.png "Home Assistant") | ![Hubitat](/assets/img/logos/hubitat.png "Hubitat") | ![Apple HomeKit](/assets/img/logos/homekit.png "Apple HomeKit") | ![SmartThings](/assets/img/logos/smartthings.png "SmartThings") | ![Google Home](/assets/img/logos/google.png "Google Home") | ![Alexa](/assets/img/logos/alexa.png "Alexa") |
|---------|---------------|---------|---------------|-------------|-------------|-------|
| **Hardware** | Optional | Required | Apple Device | Optional | Optional | Optional |
| **Difficulty** | Advanced | Intermediate | Easy | Easy | Easy | Easy |
| **Privacy** | Excellent | Excellent | Excellent | Fair | Poor | Fair |
| **Customization** | Excellent | Excellent | Limited | Good | Limited | Good |
| **Device Support** | Excellent | Excellent | Limited | Excellent | Good | Excellent |

## Detailed platform guides

### Home Assistant

**Best for**: Tech-savvy users who want complete control

Home Assistant is an open-source platform that runs on various hardware (Raspberry Pi, NUC, Docker).

**Pros:**
- Completely local control
- Extensive device support (2000+ integrations)
- Powerful automation engine
- Active community
- No cloud dependency required

**Cons:**
- Steeper learning curve
- Requires dedicated hardware
- Initial setup complexity

**Getting Started:**
1. Choose hardware (recommended: Home Assistant Yellow or Green)
2. Install Home Assistant OS
3. Configure integrations
4. Set up automations

---

### Hubitat

**Best for**: Users wanting local control without complex setup

Hubitat Elevation is a local-first home automation hub that runs entirely on your network.

**Pros:**
- 100% local processing (no cloud required)
- Works without internet
- Built-in Z-Wave and Zigbee radios
- Good automation engine (Rule Machine)
- Active community and marketplace

**Cons:**
- Hardware purchase required
- Less polished interface than cloud platforms
- Steeper learning curve than consumer platforms
- Smaller integration library than Home Assistant

**Getting Started:**
1. Purchase Hubitat Elevation hub
2. Connect to your network
3. Pair Zigbee/Z-Wave devices
4. Create rules with Rule Machine

---

### Apple HomeKit

**Best for**: Apple ecosystem users who value privacy

HomeKit is Apple's smart home platform built into iOS, iPadOS, and macOS.

**Pros:**
- Seamless iOS integration
- Strong privacy focus
- Easy setup with iPhone/iPad
- Secure local control
- Great for basic automations

**Cons:**
- Limited device compatibility
- Requires Apple device as hub
- Less flexible automations
- More expensive devices

**Getting Started:**
1. Ensure you have an Apple device
2. Set up a Home Hub (Apple TV, HomePod, or iPad)
3. Add HomeKit-compatible devices
4. Use the Home app for control

---

### Samsung SmartThings

**Best for**: Beginners wanting extensive device support

SmartThings offers a cloud-based platform with optional hub.

**Pros:**
- Easy to set up
- Wide device compatibility
- No hub required for many devices
- Good mobile app
- SmartThings Find integration

**Cons:**
- Cloud-dependent
- Some features require subscription
- Occasional cloud outages
- Privacy concerns

**Getting Started:**
1. Download SmartThings app
2. Optional: Purchase SmartThings hub
3. Add compatible devices
4. Create routines

---

### Google Home

**Best for**: Google ecosystem integration

Google Home leverages Google Assistant for voice control.

**Pros:**
- Excellent voice control
- Works with many devices
- No hub required
- Integration with Google services
- Affordable hardware

**Cons:**
- Privacy concerns
- Cloud-dependent
- Limited local control
- Data collection

**Getting Started:**
1. Get a Google Home device
2. Download Google Home app
3. Link compatible devices
4. Set up routines

---

## Making your choice

Consider these factors:

1. **Privacy Requirements**: Home Assistant or HomeKit
2. **Technical Skill**: Beginners → SmartThings/Google, Advanced → Home Assistant
3. **Existing Ecosystem**: Already invested? Stick with it
4. **Budget**: All platforms are free, but device costs vary
5. **Device Selection**: Check compatibility first

## Matter and Thread

### What is Thread?

Thread is a low-power, IPv6-based mesh networking protocol designed specifically for smart home devices. Unlike WiFi, Thread devices create a self-healing mesh network that doesn't require a central hub to function.

**Key characteristics:**
- Low power consumption (battery-friendly)
- Mesh networking (devices extend the network)
- No single point of failure
- Requires a Thread border router (built into many newer smart speakers and hubs)

### What is Matter?

Matter is an application-layer protocol that defines how smart home devices communicate. It can run over Thread, WiFi, or Ethernet, and aims to provide cross-platform compatibility.

**Key benefits:**
- Works across platforms (HomeKit, Google Home, Alexa, SmartThings)
- Local control by default
- Improved security standards
- One app to set up devices

**Current status:**

Matter shows promise and progress is being made on both the standard and devices. However, we don't recommend fully committing to Matter devices yet for most users. Reasons include:

- The standard is still evolving with ongoing updates
- Device support is growing but limited
- Some features may require firmware updates
- Interoperability between platforms is improving but not yet seamless

**Our recommendation:** If you're building a new smart home, consider platforms that support Matter (most major platforms do), but don't make Matter support your primary buying criteria yet. Established protocols like Zigbee and Z-Wave remain more reliable choices for now.

## Multi-platform approach

You don't have to choose just one! Many users run:
- Home Assistant as the main hub
- Plus HomeKit for iOS convenience
- Plus Alexa/Google for voice control

## Next steps

- [Explore compatible devices →](/getting-started/device-guide.html)
- [See automation examples →](/automation/)
