---
layout: default
title: Choose the right platform
description: Compare Home Assistant, Hubitat, HomeKit, SmartThings, Google Home, and Alexa. Find the best smart home platform for your needs.
---

# Home automation platforms

Choose the platform that fits the person who will maintain the house, not the platform with the longest feature list.

I have personally used Amazon Echo with Alexa, SmartThings, and Hubitat. I now prefer Hubitat because everyday management is user-friendly, while detailed rules and coding are available when I need them. I have not personally run Home Assistant, so its placement here describes technical fit rather than a hands-on review.

For the practical decision between the two most flexible options, read [Hubitat vs Home Assistant for a family house](/getting-started/hubitat-vs-home-assistant.html).

## Platform comparison

| Feature | <span class="platform-table-header"><img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo" class="platform-table-logo"><span class="platform-table-name">Home Assistant</span></span> | <span class="platform-table-header"><img src="/assets/img/logos/hubitat.png" alt="Hubitat logo" class="platform-table-logo"><span class="platform-table-name">Hubitat</span></span> | <span class="platform-table-header"><img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo" class="platform-table-logo"><span class="platform-table-name">Apple HomeKit</span></span> | <span class="platform-table-header"><img src="/assets/img/logos/smartthings.png" alt="SmartThings logo" class="platform-table-logo"><span class="platform-table-name">SmartThings</span></span> | <span class="platform-table-header"><img src="/assets/img/logos/google.png" alt="Google Home logo" class="platform-table-logo"><span class="platform-table-name">Google Home</span></span> | <span class="platform-table-header"><img src="/assets/img/logos/alexa.png" alt="Amazon Alexa logo" class="platform-table-logo"><span class="platform-table-name">Amazon Alexa</span></span> |
|---------|---------------|---------|---------------|-------------|-------------|-------|
| **Hardware** | Optional | Required | Apple Device | Optional | Optional | Optional |
| **Difficulty** | Advanced | Intermediate | Easy | Easy | Easy | Easy |
| **Privacy** | Excellent | Excellent | Excellent | Fair | Poor | Fair |
| **Customization** | Excellent | Excellent | Limited | Good | Limited | Good |
| **Device Support** | Excellent | Excellent | Limited | Excellent | Good | Excellent |

## Detailed platform guides

<div class="platform-comparison-grid">

<div class="platform-detail-card">
  <div class="platform-detail-header">
    <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
    <div>
      <h3>Home Assistant</h3>
      <p class="platform-tagline">Complete control for tech enthusiasts</p>
    </div>
  </div>

  <div class="platform-description">
    Home Assistant offers the broadest flexibility in this group. It suits technically confident users who want to choose and maintain more of the system themselves.
  </div>

  <div class="platform-highlights">
    <div class="highlight-section highlight-pros">
      <h4>✓ Strengths</h4>
      <ul>
        <li>Broad device and service integration options</li>
        <li>Powerful automation and customization tools</li>
        <li>Control over hardware, dashboards, and system design</li>
      </ul>
    </div>

    <div class="highlight-section highlight-cons">
      <h4>△ Considerations</h4>
      <ul>
        <li>Steeper learning curve than consumer platforms</li>
        <li>You are responsible for more setup and maintenance decisions</li>
        <li>Hardware, radios, backups, and remote access need a plan</li>
      </ul>
    </div>
  </div>

  <div class="platform-quickstart">
    <strong>Before choosing:</strong> Verify current hardware, radio, backup, integration, and remote-access requirements in the official Home Assistant documentation.
  </div>
</div>

<div class="platform-detail-card">
  <div class="platform-detail-header">
    <img src="/assets/img/logos/hubitat.png" alt="Hubitat logo">
    <div>
      <h3>Hubitat</h3>
      <p class="platform-tagline">Local control without the complexity</p>
    </div>
  </div>

  <div class="platform-description">
    Hubitat Elevation is the middle ground I prefer. It is a dedicated, managed hub with approachable built-in automation tools, detailed rules, and a path into custom code when the house needs something unusual.
  </div>

  <div class="platform-highlights">
    <div class="highlight-section highlight-pros">
      <h4>✓ Strengths</h4>
      <ul>
        <li>Local automation for supported devices and rules</li>
        <li>Built-in Z-Wave and Zigbee support</li>
        <li>Rule Machine for detailed automations</li>
        <li>Custom apps and drivers when built-in tools are not enough</li>
      </ul>
    </div>

    <div class="highlight-section highlight-cons">
      <h4>△ Considerations</h4>
      <ul>
        <li>Requires intermediate technical knowledge</li>
        <li>Smaller integration ecosystem than Home Assistant</li>
        <li>Complex rules still require careful testing</li>
        <li>Requires a dedicated hub purchase</li>
      </ul>
    </div>
  </div>

  <div class="platform-quickstart">
    <strong>Getting started:</strong> Pair one representative device and build one useful local automation before moving the rest of the house.
  </div>
</div>

<div class="platform-detail-card">
  <div class="platform-detail-header">
    <img src="/assets/img/logos/homekit.png" alt="Apple HomeKit logo">
    <div>
      <h3>Apple HomeKit</h3>
      <p class="platform-tagline">Seamless for the Apple ecosystem</p>
    </div>
  </div>

  <div class="platform-description">
    HomeKit is Apple's smart home platform, deeply integrated into iOS, iPadOS, and macOS. If you're already invested in the Apple ecosystem, HomeKit offers the most seamless experience - your devices appear automatically on all your Apple products, and Siri integration works beautifully across all of them.
  </div>

  <div class="platform-highlights">
    <div class="highlight-section highlight-pros">
      <h4>✓ Strengths</h4>
      <ul>
        <li>Seamless integration across all Apple devices</li>
        <li>Industry-leading privacy and encryption</li>
        <li>Remarkably simple setup - just scan a code</li>
        <li>Secure local and remote access via iCloud</li>
      </ul>
    </div>

    <div class="highlight-section highlight-cons">
      <h4>△ Considerations</h4>
      <ul>
        <li>More restricted device compatibility</li>
        <li>Requires Apple device as home hub</li>
        <li>Limited automation complexity</li>
        <li>HomeKit devices tend to be pricier</li>
      </ul>
    </div>
  </div>

  <div class="platform-quickstart">
    <strong>Getting started:</strong> Set up a Home Hub (Apple TV, HomePod, or iPad), add HomeKit-compatible devices, and use the Home app to control everything.
  </div>
</div>

<div class="platform-detail-card">
  <div class="platform-detail-header">
    <img src="/assets/img/logos/smartthings.png" alt="SmartThings logo">
    <div>
      <h3>Samsung SmartThings</h3>
      <p class="platform-tagline">Broad support without deep technical management</p>
    </div>
  </div>

  <div class="platform-description">
    SmartThings was my step up from Alexa. It fits people who want broader device and automation support but do not want to become deeply technical.
  </div>

  <div class="platform-highlights">
    <div class="highlight-section highlight-pros">
      <h4>✓ Strengths</h4>
      <ul>
        <li>Approachable app and routine setup</li>
        <li>Broad device compatibility</li>
        <li>More automation depth than basic voice routines</li>
      </ul>
    </div>

    <div class="highlight-section highlight-cons">
      <h4>△ Considerations</h4>
      <ul>
        <li>Less room for detailed control than Hubitat or Home Assistant</li>
        <li>Local behavior varies by device and automation</li>
      </ul>
    </div>
  </div>

  <div class="platform-quickstart">
    <strong>Getting started:</strong> Download the SmartThings app, optionally purchase a hub for advanced devices, add compatible devices, and create routines.
  </div>
</div>

<div class="platform-detail-card">
  <div class="platform-detail-header">
    <img src="/assets/img/logos/google.png" alt="Google Home logo">
    <div>
      <h3>Google Home</h3>
      <p class="platform-tagline">Superior voice control and integration</p>
    </div>
  </div>

  <div class="platform-description">
    Google Home leverages Google Assistant to provide one of the most sophisticated voice control experiences available. The natural language processing is exceptional, understanding context and complex requests that would confuse other assistants. If you're already using Google services like Gmail, Calendar, and YouTube, the integration feels natural and adds real convenience to daily routines.
  </div>

  <div class="platform-highlights">
    <div class="highlight-section highlight-pros">
      <h4>✓ Strengths</h4>
      <ul>
        <li>Best-in-class natural language processing</li>
        <li>Works with thousands of devices, no hub needed</li>
        <li>Deep integration with Google services</li>
        <li>Affordable hardware widely available</li>
      </ul>
    </div>

    <div class="highlight-section highlight-cons">
      <h4>△ Considerations</h4>
      <ul>
        <li>Significant privacy considerations</li>
        <li>Completely cloud-dependent operation</li>
        <li>No option for local processing</li>
        <li>Internet outages disable control</li>
      </ul>
    </div>
  </div>

  <div class="platform-quickstart">
    <strong>Getting started:</strong> Get a Google Home device (or use Google Assistant on Android), download the app, link smart home devices, and set up routines.
  </div>
</div>

</div>

## Making your choice

Start with Alexa if simple voice commands and routines are enough. Choose SmartThings when you want broader support without deep technical management. Choose Hubitat when you want friendly daily operation plus detailed rules and optional coding. Consider Home Assistant when maximum flexibility matters enough to justify owning more of the setup and maintenance.

Always verify the exact devices and integrations you need before committing. Test one representative device, one important automation, backup and recovery, and behavior without internet access.

The good news is that you're not locked into a single choice forever. Many users start with a simpler platform and migrate to more advanced options as their needs evolve. Some run multiple platforms simultaneously, using each for its strengths.

## Matter and Thread

The smart home industry is evolving toward greater interoperability through two complementary technologies: Thread and Matter.

### Understanding Thread

Thread is a low-power mesh networking protocol designed specifically for battery-operated smart home devices. Unlike WiFi, which drains batteries and requires every device to connect to your router, Thread devices create a self-healing mesh network where each device can relay signals to others. This mesh architecture eliminates single points of failure - if one device stops working, the network automatically routes around it.

Thread requires a border router (essentially a bridge between your home network and the Thread mesh), but many newer smart speakers and hubs already include this functionality. The protocol's low power consumption makes it ideal for sensors, locks, and other devices that need to run on batteries for months or years.

### The promise of Matter

Matter is an application-layer protocol that sits on top of networking technologies like Thread, WiFi, or Ethernet. Think of it as a common language that all smart home platforms agree to speak. When a device supports Matter, it can work with HomeKit, Google Home, Alexa, and SmartThings simultaneously - no more choosing between ecosystems or buying multiple devices for different rooms.

The standard emphasizes local control and security by default. Devices communicate directly with your controller on your local network, reducing latency and improving privacy. Setup is simplified too - configure a Matter device once, and it becomes available across all your compatible platforms.

### Current reality and recommendations

While Matter represents an exciting future for smart home interoperability, we recommend a measured approach for now. The standard continues to evolve with regular updates adding new device categories and fixing interoperability issues. Device availability is growing but still limited compared to established protocols. Some features require firmware updates that may arrive months after purchase, and cross-platform functionality, while improving, doesn't always work seamlessly.

For users building a new smart home today, choose platforms that support Matter - most major platforms do - but don't make Matter compatibility your primary criterion. Established protocols like Zigbee and Z-Wave offer more reliable performance and broader device selection. As the Matter ecosystem matures, you'll be positioned to gradually incorporate Matter devices without rebuilding your entire system.

## Multi-platform approach

You're not limited to a single platform - many experienced users run multiple systems, leveraging each platform's strengths. A common configuration uses Home Assistant as the central hub for advanced automations and local control, HomeKit for seamless iOS integration when family members are at home, and Alexa or Google for voice control throughout the house.

This approach requires more technical knowledge to set up, but the flexibility can be worth the effort. Home Assistant can integrate with most other platforms, acting as a bridge that unifies everything under one powerful automation engine while preserving the convenience of platform-specific features.

## Next steps

- [Explore compatible devices →](/getting-started/device-guide.html)
- [Compare Hubitat and Home Assistant →](/getting-started/hubitat-vs-home-assistant.html)
- [See automation examples →](/automation/)
