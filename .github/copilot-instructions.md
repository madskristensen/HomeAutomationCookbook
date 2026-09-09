# Writing style

- Use sentence case for titles and headings instead of Title Case.
- Don't use em-dashes when writing sentences; use hyphens surrounded by spaces instead.
- Don't use emojis in the text, except for the lightbulb emoji (💡) when introducing a practical tip or reusable guidance.
- In public content, describe the author's experience with "I" and "my." Never call the author "the owner."
- Use each recommended product's name. Do not use price adjectives such as "lower-cost" or "cheaper" as the link text.
- Never publish TODO placeholders for unverified hardware. Use "No personally verified recommendation yet" or a specific variation that names the unverified job.

# Editorial promise

- Frame home automation as a way to quietly support routines the household already has.
- Lead with the reader's benefit: less to remember, fewer repeated checks or adjustments, better comfort or coordination, and more confidence to build and adapt.
- Help readers understand the reusable pattern rather than merely copy a finished rule.
- For substantive pages, make clear what burden is removed, what everyday benefit remains, what control the household keeps, how the reader can adapt the idea, and how they can tell it works.
- Keep products, platforms, and technical features in supporting roles. Do not make the site feel like a sales funnel.

# Site structure

- This is a Jekyll static site for homeautomationcookbook.com
- Main CSS: `docs/assets/css/style.css` (consolidated stylesheet, ~1200 lines)
- Config: `docs/_config.yml` contains navigation structure
- Layout: `docs/_layouts/default.html` is the main template
- Homepage: `docs/index.md`
- Documentation pages: `docs/getting-started/philosophy.md`, `docs/getting-started/tips.md`, `docs/getting-started/resources.md`
- Device selection and personally used products: `docs/getting-started/device-guide.md`
- Chronological articles: `docs/_articles/`, listed at `docs/articles/index.md`
- Automation categories: 7 directories under `docs/automation/`, plus the main automation hub page
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

When creating or updating an automation detail page, use this structure:

- Title and one-sentence job
- Best for and Not for
- Why this exists
- What I used
- Logic
- Setup notes
- Advanced features, only when they are useful
- Failure modes
- Done when
- FAQ
- Related recipes

Keep the recipe platform-neutral. Do not add platform-specific walkthroughs, code blocks, logos, or capability claims unless Mads has personally verified them and they materially change the recipe.

# Content dates

- Recipes use `layout: automation` and always include `last_modified_at`.
- Substantive evergreen guides use `layout: guide` and include `last_modified_at`; the guide layout shows the date below the headline.
- Articles use `layout: guide` and include a publication `date`. Add `last_modified_at` only after a later substantive update.
- Hub, category, redirect, and navigation pages use `layout: default` and remain undated.
- Legal pages may show an explicit date in their content when the wording requires it.

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

# Platform-specific content

- Keep the core recipe platform-neutral.
- Only add a platform-specific note when Mads has personally verified a limitation or workaround that materially changes the outcome.
- Never create unverified platform code, UI steps, or capability claims.
- Mads has personally used Amazon Echo with Alexa, SmartThings, and Hubitat. Hubitat is his current and preferred platform because daily management is user-friendly while detailed rules and coding remain available.
- Mads has not personally used Home Assistant. Clearly label Home Assistant guidance as a technical-fit comparison rather than firsthand experience.

# Amazon affiliate links

- All Amazon product links must be affiliate links. Any new link to an Amazon product page must append `/ref=nosim?tag=madsk0f-20` to the `amazon.com/dp/ASIN` URL (e.g. `https://www.amazon.com/dp/B0H4GD6GGK/ref=nosim?tag=madsk0f-20`).
- Any page that adds its first Amazon link needs an affiliate disclosure line near the link (see existing pattern in automation pages: "Amazon product links on this page are affiliate links, and I earn from qualifying purchases." linking to `/disclosure.html`).
- `docs/disclosure.md` is the canonical page describing the Amazon Associates Program relationship; keep it in sync if the affiliate program status changes.

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
