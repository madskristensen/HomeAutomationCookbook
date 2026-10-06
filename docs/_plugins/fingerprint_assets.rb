# frozen_string_literal: true

# NO-OP under github-pages: Jekyll safe mode skips custom _plugins.
# Fingerprinting runs in .github/workflows/jekyll.yml via
# script/fingerprint-assets.py before `jekyll build`. Kept as a stub so
# local non-safe builds do not double-run if someone enables plugins.
