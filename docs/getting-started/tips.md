---
layout: default
title: Tips and tricks
---

# Tips and tricks

Not all home automation requires complex technology. Sometimes the simplest solutions are the most effective.

<div class="tips-grid">

<div class="tip-card">
  <div class="tip-header">
    <span class="tip-icon">📦</span>
    <h2>Amazon subscriptions for automation</h2>
  </div>
  
  <p class="tip-intro">Not all automations have to go through your smart home system. You can use Amazon subscriptions to automate yourself to complete repetitive maintenance tasks.</p>
  
  <div class="tip-section">
    <h3>How it works</h3>
    <p>Subscribe to certain products to be automatically ordered and delivered at specific time intervals. When items arrive, install them right away. This eliminates the need to remember when to order and replace items.</p>
  </div>
  
  <div class="tip-section">
    <h3>Popular subscription items</h3>
    <div class="subscription-examples">
      <div class="subscription-item">
        <strong>Water filters</strong>
        <span>Every 6 months</span>
      </div>
      <div class="subscription-item">
        <strong>Air filters</strong>
        <span>Every 4 months</span>
      </div>
      <div class="subscription-item">
        <strong>HVAC filters</strong>
        <span>Every 3 months</span>
      </div>
      <div class="subscription-item">
        <strong>Sensor batteries</strong>
        <span>Annually</span>
      </div>
      <div class="subscription-item">
        <strong>Pet supplies</strong>
        <span>Monthly</span>
      </div>
      <div class="subscription-item">
        <strong>Cleaning supplies</strong>
        <span>Bi-monthly</span>
      </div>
    </div>
  </div>
  
  <div class="tip-benefits">
    <div class="benefit-item">
      <span class="benefit-icon">✓</span>
      <span>Never forget to order replacement items</span>
    </div>
    <div class="benefit-item">
      <span class="benefit-icon">✓</span>
      <span>Installation becomes automatic when delivery arrives</span>
    </div>
    <div class="benefit-item">
      <span class="benefit-icon">✓</span>
      <span>Save money with subscribe & save discounts</span>
    </div>
    <div class="benefit-item">
      <span class="benefit-icon">✓</span>
      <span>Reduce mental load of tracking maintenance</span>
    </div>
  </div>
</div>

<div class="tip-card">
  <div class="tip-header">
    <span class="tip-icon">💡</span>
    <h2>Manually disable automation in a room</h2>
  </div>
  
  <p class="tip-intro">Sometimes you don't want automations to run. For example, kids love turning lights off to play with flashlights. It ruins the fun if lights come on automatically when motion is detected.</p>
  
  <div class="tip-section">
    <h3>The solution</h3>
    <p>Disable automation when lights are manually switched off. When lights are manually switched on again, re-enable automations automatically.</p>
  </div>
  
  <div class="tip-requirements">
    <h3>Requirements</h3>
    <ul>
      <li>Smart light switch that can detect manual (physical) operations</li>
      <li>Ability to distinguish between manual and automated control</li>
    </ul>
  </div>
  
  <div class="tip-implementation">
    <div class="implementation-flow">
      <div class="flow-step">
        <div class="flow-trigger">When lights are manually turned OFF</div>
        <div class="flow-arrow">→</div>
        <div class="flow-action">Disable motion-based automations for this room</div>
      </div>
      <div class="flow-step">
        <div class="flow-trigger">When lights are manually turned ON</div>
        <div class="flow-arrow">→</div>
        <div class="flow-action">Re-enable motion-based automations</div>
      </div>
    </div>
  </div>
  
  <div class="tip-section">
    <h3>Compatible switches</h3>
    <p>Most smart switches support this feature: Zooz (Z-Wave), Inovelli (Z-Wave/Zigbee), GE/Jasco (Z-Wave), Lutron Caseta, and many others - check specifications for "physical button" or "manual control" detection.</p>
  </div>
</div>

<div class="tip-card">
  <div class="tip-header">
    <span class="tip-icon">👆</span>
    <h2>Turn off all lights from one switch</h2>
  </div>
  
  <p class="tip-intro">In most rooms, the main light switch by the door can turn off all lights in the room with a special gesture.</p>
  
  <div class="tip-section">
    <h3>The double-tap trick</h3>
    <p>Many smart switches support double-tap actions. Configure double-tap on the OFF button to turn off all lights and smart plugs in that room.</p>
  </div>
  
  <div class="example-scenario">
    <h3>Example: Leaving the living room</h3>
    <div class="scenario-steps">
      <div class="scenario-step">
        <span class="step-number">1</span>
        <span>Walk to door</span>
      </div>
      <div class="scenario-step">
        <span class="step-number">2</span>
        <span>Double-tap OFF switch</span>
      </div>
      <div class="scenario-step">
        <span class="step-number">3</span>
        <span>All lights, lamps, and plugs turn off</span>
      </div>
      <div class="scenario-step">
        <span class="step-number">4</span>
        <span>Exit room</span>
      </div>
    </div>
  </div>
  
  <div class="setup-steps">
    <h3>Setup instructions</h3>
    <div class="setup-step">
      <h4>Identify devices</h4>
      <p>List all lights and plugs in each room, then group them by room in your smart home app.</p>
    </div>
    <div class="setup-step">
      <h4>Configure switch</h4>
      <p>Enable double-tap feature on your smart switch and set double-tap DOWN to trigger "All Off" scene.</p>
    </div>
    <div class="setup-step">
      <h4>Create scene/routine</h4>
      <p>Name it "Living Room All Off" with actions to turn off all devices in that room.</p>
    </div>
    <div class="setup-step">
      <h4>Test and adjust</h4>
      <p>Double-tap the OFF button, verify all devices turn off, and adjust timing if needed.</p>
    </div>
  </div>
  
  <div class="tip-section">
    <h3>Multi-tap possibilities</h3>
    <p>Some switches (Inovelli, Zooz, GE/Jasco) support multiple gestures:</p>
    <ul>
      <li><strong>Double-tap UP:</strong> All on at 100%</li>
      <li><strong>Double-tap DOWN:</strong> All off</li>
      <li><strong>Triple-tap UP:</strong> Custom scene 1</li>
      <li><strong>Triple-tap DOWN:</strong> Custom scene 2</li>
    </ul>
  </div>
</div>

<div class="tip-card">
  <div class="tip-header">
    <span class="tip-icon">📱</span>
    <h2>Dashboard status tiles</h2>
  </div>
  
  <p class="tip-intro">Replace notifications with visual status tiles on a dashboard. Instead of getting push notifications that get dismissed and forgotten, display status on a tablet you see regularly.</p>
  
  <div class="comparison-section">
    <div class="comparison-column comparison-bad">
      <h3>Problems with notifications</h3>
      <ul>
        <li>Easy to dismiss and forget</li>
        <li>Interrupt your flow</li>
        <li>Don't provide persistent status</li>
        <li>Require checking phone</li>
      </ul>
    </div>
    <div class="comparison-column comparison-good">
      <h3>Benefits of dashboards</h3>
      <ul>
        <li>Always visible status at a glance</li>
        <li>No interruptions</li>
        <li>Entire household can see</li>
        <li>Multiple statuses simultaneously</li>
      </ul>
    </div>
  </div>
  
  <div class="tip-section">
    <h3>Perfect for tracking</h3>
    <div class="status-examples">
      <div class="status-category">
        <strong>Appliances</strong>
        <ul>
          <li>Washer done - move to dryer</li>
          <li>Dishwasher clean - ready to empty</li>
          <li>Dryer finished - fold clothes</li>
        </ul>
      </div>
      <div class="status-category">
        <strong>Deliveries</strong>
        <ul>
          <li>Grocery delivery arrived</li>
          <li>Package at front door</li>
          <li>Mail delivered</li>
        </ul>
      </div>
      <div class="status-category">
        <strong>Home status</strong>
        <ul>
          <li>Doors/windows open before leaving</li>
          <li>Robot vacuum runs soon - tidy up</li>
          <li>Trash day tomorrow</li>
          <li>Low battery on sensors</li>
        </ul>
      </div>
    </div>
  </div>
  
  <div class="tip-section">
    <h3>Implementation tips</h3>
    <div class="implementation-tips">
      <div class="tip-subsection">
        <h4>Best placement</h4>
        <p>Kitchen counter, entryway, master bathroom, or garage entrance</p>
      </div>
      <div class="tip-subsection">
        <h4>Design principles</h4>
        <p>Large tiles, color coding (green=good, red=attention), most important info at top</p>
      </div>
      <div class="tip-subsection">
        <h4>Hardware options</h4>
        <p>Amazon Fire tablets (budget), iPads (premium), or Android tablets (mid-range)</p>
      </div>
      <div class="tip-subsection">
        <h4>Software choices</h4>
        <p>SharpTools, Home Assistant Dashboard, Hubitat Dashboard, ActionTiles, or Fully Kiosk Browser</p>
      </div>
    </div>
  </div>
</div>

<div class="tip-card">
  <div class="tip-header">
    <span class="tip-icon">🔄</span>
    <h2>Create patterns throughout your home</h2>
  </div>
  
  <p class="tip-intro">When you implement a feature in one room, consider making it a pattern throughout the house.</p>
  
  <div class="pattern-example">
    <h3>Example: Light switch double-tap</h3>
    <div class="pattern-benefit">
      <strong>Pattern:</strong> Double-tap any light switch to control all lights in that room
    </div>
    <div class="pattern-reasons">
      <div class="pattern-reason">
        <span class="reason-icon">✓</span>
        <span>Easy to remember once learned</span>
      </div>
      <div class="pattern-reason">
        <span class="reason-icon">✓</span>
        <span>Works the same in every room</span>
      </div>
      <div class="pattern-reason">
        <span class="reason-icon">✓</span>
        <span>No explanation needed after initial teaching</span>
      </div>
      <div class="pattern-reason">
        <span class="reason-icon">✓</span>
        <span>Intuitive and consistent</span>
      </div>
    </div>
  </div>
  
  <div class="tip-section">
    <h3>Other pattern ideas</h3>
    <div class="pattern-ideas">
      <div class="pattern-idea">
        <strong>Long-press for scenes</strong>
        <p>Bedroom: Reading mode, Living room: Movie mode, Kitchen: Cooking mode</p>
      </div>
      <div class="pattern-idea">
        <strong>Triple-tap for special functions</strong>
        <p>Triple-tap any switch → All lights in house off (useful when leaving home)</p>
      </div>
      <div class="pattern-idea">
        <strong>Hold for dimming</strong>
        <p>Hold UP → Gradually brighten, Hold DOWN → Gradually dim</p>
      </div>
    </div>
  </div>
  
  <div class="tip-section">
    <h3>Visual markers</h3>
    <p>Mark switches with special capabilities using small colored dots, printed labels in switch plates, subtle engraving, or consistent placement of "smart" switches.</p>
  </div>
</div>

</div>

---

[← Back to Home](/) | [View Resources →](/getting-started/resources.html)
