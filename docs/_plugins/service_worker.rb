# frozen_string_literal: true

require "digest"

module HomeAutomationCookbook
  # Paths the service worker precaches. Built from real static files so a
  # new stylesheet, script, or icon is picked up without editing sw.js.
  class ServiceWorkerShell < Jekyll::Generator
    priority :low

    SHELL_EXTS = [".css", ".js", ".webmanifest"].freeze

    def generate(site)
      pages = ["/"]
      images = []
      hashed = []
      site.static_files.each do |file|
        next unless file.is_a?(Jekyll::StaticFile)

        path = public_path(file)
        ext = File.extname(path).downcase
        name = File.basename(path).downcase
        if SHELL_EXTS.include?(ext)
          next if path == "/sw.js"

          pages << path
          hashed << file
        elsif name == "favicon.ico" || (path.start_with?("/assets/img/") && shell_icon?(name))
          images << path
          hashed << file
        end
      end
      site.data["shell"] = {
        "pages" => pages.uniq,
        "images" => images.uniq.sort,
        "version" => shell_version(hashed)
      }
    end

    def public_path(file)
      path = file.relative_path.to_s
      "/#{path.sub(%r{\A/}, '')}"
    end

    def shell_icon?(name)
      name.include?("favicon") || name.include?("apple-touch") || name.match?(/\Aicon-\d/)
    end

    def shell_version(files)
      digest = Digest::SHA256.new
      files.sort_by { |file| public_path(file) }.each do |file|
        digest << public_path(file)
        digest << "\0"
        source = file.respond_to?(:path) ? file.path.to_s : ""
        if !source.empty? && File.file?(source)
          digest << Digest::SHA256.file(source).hexdigest
        end
        digest << "\0"
      end
      digest.hexdigest[0, 12]
    end
  end
end
