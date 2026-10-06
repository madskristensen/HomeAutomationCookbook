# frozen_string_literal: true

# Fingerprint CSS and JS before Jekyll reads static files and data, so
# pages link hashed URLs and the service worker can precache them.
Jekyll::Hooks.register :site, :after_init do |site|
  root = File.expand_path("../..", site.source)
  script = File.join(root, "script/fingerprint-assets.py")
  success = system("python3", script, chdir: root)
  unless success
    raise "Could not fingerprint assets. Install rcssmin with: python3 -m pip install rcssmin"
  end
end
