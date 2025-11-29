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
- Documentation pages: `docs/philosophy/index.md`, `docs/getting-started/tips.md`, `docs/getting-started/resources.md`
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