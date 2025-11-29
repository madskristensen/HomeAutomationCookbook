# Writing style
- Use sentence case for titles and headings instead of Title Case.
- Don't use em-dashes when writing sentences; use hyphens surrounded by spaces instead.
- Don't use emojis in the text.

# Site structure
- This is a Jekyll static site for homeautomationcookbook.com
- Main CSS: `docs/assets/css/style.css` (consolidated stylesheet, ~1200 lines)
- Config: `docs/_config.yml` contains navigation structure
- Layout: `docs/_layouts/default.html` is the main template
- Homepage: `docs/index.md`
- Documentation pages: `docs/getting-started/philosophy.md`, `docs/getting-started/tips.md`, `docs/getting-started/resources.md`
- Automation categories: 6 directories under `docs/automation/` (motion, contact, presence, climate, media, appliances)
- Each category has: `index.md` (overview) and individual automation pages

# Design system
- Color scheme: Slate gray (#2c3e50 primary, #1a252f hover)
- All blue colors (#0066cc) were replaced with slate gray for subtlety
- Cards use: border `#e0e0e0`, hover border `#2c3e50`, shadow `rgba(44,62,80,0.08-0.12)`
- Backgrounds: `#fafafa` for light sections, `#f8f9fa` for cards
- Typography: System fonts, 17px base, line-height 1.8
- Never use bright or saturated colors

# File editing approach
- Always read files before editing them to understand context
- Use `multi_replace_string_in_file` for multiple changes (never call `replace_string_in_file` multiple times)
- Include 3-5 lines of context before and after target text for uniqueness
- Avoid PowerShell scripts - they cause timeout/cancellation issues; use direct tool calls instead
- For site-wide changes: start with homepage, then category indexes, then detail pages

# Automation page patterns
All automation detail pages follow this structure:
- Use cases
- Products needed
- Basic automation setup
- Platform-specific examples
- Advanced features
- Troubleshooting
- Best practices

When creating or updating automation pages, maintain this consistent structure.

# Navigation
- Main nav in `docs/_includes/navigation.html`
- Config in `docs/_config.yml` under `navigation:` key
- All links use `.html` extension (converted from `/` endings)
- Three-level navigation: main menu → dropdown → flyout
- Mobile uses hamburger menu with nested accordion

# Common tasks
- **Adding new automation**: Create markdown in appropriate category folder, add to `_config.yml` navigation
- **Sentence case conversion**: Use `multi_replace_string_in_file` with heading patterns like "## Title Case" → "## Sentence case"
- **CSS changes**: Edit consolidated `docs/assets/css/style.css` (do not split files)
- **Color updates**: Search for hex values and replace consistently across entire stylesheet

# What works well
- Direct tool usage over scripts
- Batch operations with multi_replace_string_in_file
- Reading file structure with `get_projects_in_solution` and `get_files_in_project` first
- Systematic approach: homepage → categories → details
- Most automation pages already follow style guide - verify before assuming work needed

# Local development - running Jekyll locally
To run the Jekyll site locally for preview and testing:

```bash
# From the repository root directory:
cd /home/runner/work/HomeAutomationCookbook/HomeAutomationCookbook

# Install gems to local vendor directory (avoids permission issues)
bundle config set --local path 'vendor/bundle'
bundle install

# Run Jekyll server (source is in docs/ subdirectory)
bundle exec jekyll serve --source docs --port 4000 --host 0.0.0.0

# Site will be available at http://localhost:4000/
```

- Use Playwright browser to navigate to `http://localhost:4000/` and take screenshots
- The `vendor/` directory will be created - it's already in `.gitignore`
- If you see "Could not find gem" errors, make sure to run from repo root, not from `docs/`

# Platform logos
- Located in: `docs/assets/img/logos/`
- Available logos: `alexa.png`, `google.png`, `homeassistant.png`, `homekit.png`, `hubitat.png`, `smartthings.png`
- Use in platform cards with: `<img src="/assets/img/logos/{platform}.png" alt="{Platform} logo">`

# Platform card structure with logos
Use this HTML structure for platform-specific examples:
```html
<div class="platform-card">
  <div class="platform-card-header">
    <img src="/assets/img/logos/homeassistant.png" alt="Home Assistant logo">
    <h4>Home Assistant</h4>
  </div>
  <ol>
    <li>Step 1</li>
    <li>Step 2</li>
  </ol>
</div>
```

# Automation categories
There are 8 automation categories (not 6):
- `docs/automation/lighting/` - Light automations
- `docs/automation/climate/` - HVAC, fans, blinds
- `docs/automation/security/` - Safety and security
- `docs/automation/appliances/` - Washer, vacuum, coffee maker
- `docs/automation/notifications/` - Alerts and reminders
- `docs/automation/entertainment/` - TV, music, media
- `docs/automation/daily-routines/` - Morning, bedtime, away mode
- `docs/automation/index.md` - Main automation hub page

# All automation detail pages with platform examples
These files need platform logo updates when modifying platform-specific examples:
- lighting: bathroom-night-light.md, disable-on-door-close.md, lights-off-after-motion.md, lights-on-motion.md, outdoor-night-lights.md, toggle-lights-door.md
- security: away-lights.md, fake-dog-deterrent.md, fire-safety.md, garage-door-notification.md, water-leak-response.md
- climate: air-quality-purifier.md, blinds-sunset-sunrise.md, fan-shower.md, room-heater-maintain-temp.md, thermostat-windows-close.md, thermostat-windows-open.md, window-notifications.md
- appliances: coffee-maker-morning.md, dishwasher-done-notification.md, dryer-done-notification.md, robot-vacuum-auto-start.md, washer-done-notification.md
- notifications: baby-sleep-mode.md, doorbell-notification.md, garbage-day-reminder.md, low-battery-alerts.md, music-controls.md, status-tiles.md, teeth-brushing-reminder.md
- entertainment: music-switch-control.md, shower-music.md, speaker-volume-presets.md, tv-dim-lights.md, welcome-home-music.md
- daily-routines: away-mode.md, bedtime-routine.md, morning-routine.md, unlock-door-arrival.md