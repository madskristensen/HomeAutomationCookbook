# Home Automation Cookbook

> A comprehensive guide for home automation enthusiasts

This repository contains the source for the Home Automation Cookbook website, built with Jekyll and hosted on GitHub Pages.

## Live site

Visit the live site at: https://www.homeautomationcookbook.com

## About

The Home Automation Cookbook is a community-driven documentation project that helps people:

- Get started with home automation
- Choose the right platform and devices
- Create effective automations
- Secure their smart homes
- Troubleshoot common issues

## Development

### Prerequisites

- Ruby 2.7 or higher
- Bundler
- Git

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/madskristensen/HomeAutomationCookbook.git
   cd HomeAutomationCookbook
   ```

2. Install dependencies:
   ```bash
   bundle config set --local path 'vendor/bundle'
   bundle install
   ```

3. Run the local server:
   ```bash
   bundle exec jekyll serve --source docs --port 4001 --host 0.0.0.0
   ```

4. Open your browser to `http://localhost:4001`

### Quick Run Script

For convenience, you can use the provided batch file:
```bash
run-site.cmd
```

### Troubleshooting local development

- Port conflict (wrong site appears):
   ```powershell
   Get-NetTCPConnection -LocalPort 4001 | Select-Object LocalAddress, LocalPort, State, OwningProcess
   ```
- Use a different port for one run:
   ```bash
   bundle exec jekyll serve --source docs --port 4002 --host 0.0.0.0
   ```
- Generated folders are ignored by Git: `_site/` and `docs/_site/`
- If those folders were tracked previously, untrack them once:
   ```bash
   git rm -r --cached _site docs/_site
   ```

## Contributing

We welcome contributions! Here's how you can help:

1. **Add Content**: Create new guides or improve existing ones
2. **Fix Errors**: Spot a mistake? Submit a PR
3. **Share Experience**: Add your automation recipes
4. **Improve Navigation**: Help organize content better

### Content Structure

- `docs/` - Main documentation folder
  - `getting-started/` - Beginner guides
  - `automation/` - Automation recipes
      - `lighting/`
      - `daily-routines/`
      - `climate/`
      - `entertainment/`
      - `appliances/`
      - `security/`
      - `notifications/`
   - `faq/` - Frequently asked questions

### Writing Guidelines

- Use clear, concise language
- Include code examples where applicable
- Add images/diagrams to explain complex concepts
- Follow the existing document structure
- Test your changes locally before submitting

## Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch via GitHub Actions.

### Setting Up GitHub Pages

1. Go to repository Settings → Pages
2. Source: GitHub Actions
3. Custom domain: Add your domain in the CNAME file

### Custom Domain Setup

1. Update `docs/CNAME` with your domain
2. Configure DNS records:
   - Type: `A` → Points to GitHub Pages IPs
   - Type: `CNAME` → Points to `yourusername.github.io`
3. Enable "Enforce HTTPS" in repository settings

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Community

- **Issues**: Report bugs or request features
- **Discussions**: Share ideas and get help
- **Pull Requests**: Contribute directly

## Contact

Questions? Open an issue or start a discussion!

---

Built by the home automation community
