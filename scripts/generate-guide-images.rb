require "cgi"
require "date"
require "fileutils"
require "pathname"

ROOT = Pathname.new(__dir__).parent
OUTPUT = ROOT.join("docs", "assets", "img", "social", "guides")

PAGES = [
  ["docs/about.md", "about", "About", "house", true],
  ["docs/articles/index.md", "articles", "Articles", "book", false],
  ["docs/_articles/pir-vs-mmwave-presence.md", "pir-vs-mmwave-presence", "Sensor guide", "sensors", true],
  ["docs/_articles/motion-sensor-placement.md", "motion-sensor-placement", "Sensor guide", "floorplan", true],
  ["docs/getting-started/index.md", "getting-started", "Getting started", "path", true],
  ["docs/getting-started/philosophy.md", "home-automation-philosophy", "Design principles", "balance", true],
  ["docs/getting-started/device-guide.md", "choose-devices", "Device guide", "devices", true],
  ["docs/getting-started/tips.md", "automation-tips", "Practical tips", "checklist", true],
  ["docs/getting-started/resources.md", "automation-resources", "Resources", "library", true]
].freeze

def wrap_text(text, limit, maximum_lines)
  lines = []
  current = ""

  text.split.each do |word|
    candidate = current.empty? ? word : "#{current} #{word}"
    if candidate.length <= limit
      current = candidate
    else
      lines << current unless current.empty?
      current = word
    end
  end

  lines << current unless current.empty?
  if lines.length > maximum_lines
    lines = lines.first(maximum_lines)
    lines[-1] = "#{lines[-1].sub(/[.,;:!?]?\z/, "")}..."
  end
  lines
end

def text_lines(lines, x:, y:, size:, step:, color:, weight: nil)
  weight_attribute = weight ? %( font-weight="#{weight}") : ""
  lines.each_with_index.map do |line, index|
    %(<text x="#{x}" y="#{y + (index * step)}" fill="#{color}" font-family="Segoe UI, Arial, sans-serif" font-size="#{size}"#{weight_attribute}>#{CGI.escapeHTML(line)}</text>)
  end.join("\n  ")
end

def theme_style
  <<~CSS
    <style>
      @media (prefers-color-scheme: dark) {
        rect[fill="#f8f9fa"] { fill: #14191c; }
        rect[fill="#ffffff"], path[fill="#ffffff"] { fill: #1d2428; }
        [fill="#eef2f3"] { fill: #293238; }
        text[fill="#2c3e50"], circle[fill="#2c3e50"] { fill: #e7edef; }
        text[fill="#5d6d75"], text[fill="#6b777c"] { fill: #b7c2c6; }
        [stroke="#2c3e50"] { stroke: #d7e0e3; }
        [stroke="#9db1b6"] { stroke: #72858c; }
        [stroke="#e0e0e0"] { stroke: #3d494f; }
      }
    </style>
  CSS
end

def illustration(name)
  common = %(fill="none" stroke="#2c3e50" stroke-width="9" stroke-linecap="round" stroke-linejoin="round")

  case name
  when "house"
    <<~SVG
      <g transform="translate(780 125) scale(.75)" #{common}>
        <path d="M25 180 205 35l180 145"/><path d="M66 160v260h278V160" fill="#eef2f3"/>
        <circle cx="162" cy="240" r="31" fill="#6f8f96" stroke="none"/><circle cx="248" cy="240" r="31" fill="#9db1b6" stroke="none"/>
        <path d="M118 330c6-48 82-48 88 0M204 330c6-48 82-48 88 0"/>
        <rect x="365" y="245" width="74" height="118" rx="12" fill="#ffffff"/><path d="M388 280h28M388 311h28M388 342h28" stroke="#6f8f96" stroke-width="6"/>
      </g>
    SVG
  when "book"
    <<~SVG
      <g transform="translate(735 130)" #{common}>
        <path d="M25 52c72-28 144-15 190 24v340c-46-39-118-52-190-24z" fill="#eef2f3"/>
        <path d="M405 52c-72-28-144-15-190 24v340c46-39 118-52 190-24z" fill="#eef2f3"/>
        <path d="M215 76v340"/>
        <path d="M68 137h104M68 192h104M68 247h82M258 137h104M258 192h104M258 247h82" stroke="#6f8f96" stroke-width="7"/>
      </g>
    SVG
  when "sensors"
    <<~SVG
      <g transform="translate(720 125) scale(.9)" #{common}>
        <rect x="40" y="105" width="145" height="225" rx="28" fill="#eef2f3"/><circle cx="112" cy="185" r="32" fill="#6f8f96" stroke="none"/>
        <rect x="290" y="105" width="145" height="225" rx="28" fill="#eef2f3"/><circle cx="362" cy="185" r="32" fill="#9db1b6" stroke="none"/>
        <path d="M112 78c-38-42-38-76 0-112M112 78c38-42 38-76 0-112M362 78c-58-55-58-103 0-158M362 78c58-55 58-103 0-158" stroke="#6f8f96"/>
        <path d="M185 380h105" stroke="#9db1b6" stroke-dasharray="10 12"/><circle cx="165" cy="380" r="11" fill="#6f8f96" stroke="none"/><circle cx="310" cy="380" r="11" fill="#6f8f96" stroke="none"/>
      </g>
    SVG
  when "floorplan"
    <<~SVG
      <g transform="translate(720 102) scale(.9)" #{common}>
        <rect x="25" y="25" width="420" height="420" fill="#eef2f3"/>
        <path d="M205 25v155h240M25 275h180v170M310 180v265"/>
        <path d="M78 112a120 120 0 0 1 120 120H78z" fill="#ffffff" stroke="#6f8f96"/>
        <circle cx="78" cy="112" r="15" fill="#6f8f96" stroke="none"/>
        <path d="M310 320h74M347 283v74" stroke="#9db1b6"/>
      </g>
    SVG
  when "path"
    <<~SVG
      <g transform="translate(720 122) scale(.9)" #{common}>
        <circle cx="55" cy="355" r="38" fill="#eef2f3"/><circle cx="205" cy="255" r="38" fill="#eef2f3"/><circle cx="355" cy="155" r="38" fill="#6f8f96" stroke="none"/>
        <path d="m88 333 84-56M238 233l84-56" stroke="#9db1b6" stroke-dasharray="10 12"/>
        <path d="M260 108 355 28l95 80M292 91v149h126V91" fill="#eef2f3"/>
        <path d="M332 240v-76h46v76"/>
      </g>
    SVG
  when "balance"
    <<~SVG
      <g transform="translate(710 125) scale(.85)" #{common}>
        <path d="M220 40v340M105 105h230M150 380h140"/>
        <path d="m105 105-73 170h146zm230 0-73 170h146z" fill="#eef2f3"/>
        <circle cx="220" cy="40" r="18" fill="#6f8f96" stroke="none"/>
        <rect x="425" y="145" width="70" height="115" rx="12" fill="#ffffff"/>
        <path d="M447 180h27M447 208h27M447 236h27" stroke="#6f8f96" stroke-width="6"/>
      </g>
    SVG
  when "devices"
    <<~SVG
      <g transform="translate(805 125) scale(.67)" #{common}>
        <rect x="20" y="55" width="125" height="180" rx="22" fill="#eef2f3"/><circle cx="82" cy="125" r="26" fill="#6f8f96" stroke="none"/>
        <rect x="190" y="55" width="125" height="180" rx="22" fill="#eef2f3"/><path d="M222 112h61M222 150h61M222 188h61" stroke="#6f8f96" stroke-width="7"/>
        <rect x="360" y="55" width="125" height="180" rx="22" fill="#eef2f3"/><circle cx="422" cy="135" r="34"/><circle cx="422" cy="135" r="10" fill="#6f8f96" stroke="none"/>
        <path d="M82 275v95M252 275v95M422 275v95M82 370h340" stroke="#9db1b6" stroke-dasharray="10 12"/>
      </g>
    SVG
  when "checklist"
    <<~SVG
      <g transform="translate(800 112) scale(.7)" #{common}>
        <rect x="55" y="25" width="310" height="420" rx="25" fill="#eef2f3"/>
        <path d="M140 25v-15h140v60H140V25" fill="#ffffff"/>
        <path d="m102 148 26 26 47-58M102 245l26 26 47-58M102 342l26 26 47-58" stroke="#6f8f96"/>
        <path d="M210 150h105M210 247h105M210 344h105" stroke="#9db1b6"/>
        <rect x="390" y="155" width="95" height="52" rx="26" fill="#ffffff"/><circle cx="457" cy="181" r="18" fill="#6f8f96" stroke="none"/>
      </g>
    SVG
  else
    <<~SVG
      <g transform="translate(755 118) scale(.85)" #{common}>
        <rect x="35" y="65" width="270" height="340" rx="20" fill="#eef2f3"/>
        <path d="M95 65V30h270v340h-60M95 125h150M95 188h150M95 251h110" stroke="#6f8f96"/>
        <circle cx="385" cy="110" r="45" fill="#ffffff"/><path d="M385 88v44M363 110h44" stroke="#9db1b6"/>
        <circle cx="385" cy="260" r="45" fill="#ffffff"/><path d="M360 260h50" stroke="#9db1b6"/>
      </g>
    SVG
  end
end

def extract(content, field)
  match = content.match(/^#{Regexp.escape(field)}:[ \t]*(.+?)[ \t]*\r*$/)
  raise "Missing #{field}" unless match
  match[1]
end

def build_svg(title, description, label, motif)
  title_lines = wrap_text(title, 25, 3)
  title_size = title_lines.length == 3 ? 46 : 54
  title_step = title_size + 8
  description_start = 171 + (title_lines.length * title_step) + 27

  <<~SVG
    <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title desc">
      <title id="title">#{CGI.escapeHTML(title)}</title>
      <desc id="desc">#{CGI.escapeHTML(description)}</desc>
      #{theme_style}
      <rect width="1200" height="630" fill="#f8f9fa"/>
      <rect x="52" y="52" width="1096" height="526" rx="28" fill="#ffffff" stroke="#e0e0e0" stroke-width="2"/>
      <rect x="108" y="88" width="#{label.length * 12 + 46}" height="43" rx="21" fill="#eef2f3"/>
      <text x="131" y="116" fill="#2c3e50" font-family="Segoe UI, Arial, sans-serif" font-size="19" font-weight="600">#{CGI.escapeHTML(label.upcase)}</text>
      #{text_lines(title_lines, x: 108, y: 171, size: title_size, step: title_step, color: "#2c3e50", weight: "700")}
      #{text_lines(wrap_text(description, 46, 3), x: 108, y: description_start, size: 22, step: 31, color: "#5d6d75")}
      #{illustration(motif)}
      <text x="108" y="550" fill="#6b777c" font-family="Segoe UI, Arial, sans-serif" font-size="20">HOME AUTOMATION COOKBOOK</text>
    </svg>
  SVG
end

def wire_page(file, content, image_url, hero_url, dated)
  eol = content.include?("\r\n") ? "\r\n" : "\n"
  updated = content.dup

  if dated
    if updated.match?(/^last_modified_at:/)
      updated.sub!(/^last_modified_at:[^\r\n]*/, "last_modified_at: #{Date.today.iso8601}")
    else
      anchor = updated.match?(/^date:/) ? "date" : "description"
      updated.sub!(/^(#{anchor}:[^\r\n]*)(\r*\n)/, "\\1\\2last_modified_at: #{Date.today.iso8601}#{eol}")
    end
  end

  if updated.match?(/^image:/)
    updated.sub!(/^image:[^\r\n]*/, "image: #{image_url}")
  else
    anchor = dated ? "last_modified_at" : "description"
    updated.sub!(/^(#{anchor}:[^\r\n]*)(\r*\n)/, "\\1\\2image: #{image_url}#{eol}")
  end

  if updated.include?(%(class="content-hero"))
    updated.sub!(/(<figure class="content-hero">\s*<img src=")[^"]+/, "\\1#{hero_url}")
  else
    figure = [
      "",
      %(<figure class="content-hero">),
      %(  <img src="#{hero_url}" alt="" width="1200" height="630">),
      %(</figure>),
      ""
    ].join(eol)
    updated.sub!(/^(# [^\r\n]+)(\r*\n)/, "\\1\\2#{figure}")
  end

  raise "Could not wire #{file}" unless updated.include?(image_url) && updated.include?(hero_url)
  updated
end

FileUtils.mkdir_p(OUTPUT)

PAGES.each do |relative_path, slug, label, motif, dated|
  file = ROOT.join(relative_path)
  content = File.binread(file).force_encoding(Encoding::UTF_8)
  title = extract(content, "title")
  description = extract(content, "description")
  image_url = "/assets/img/social/guides/#{slug}.png"
  hero_url = "/assets/img/social/guides/#{slug}.svg"

  File.write(OUTPUT.join("#{slug}.svg"), build_svg(title, description, label, motif), newline: :lf)
  updated = wire_page(file, content, image_url, hero_url, dated)
  File.binwrite(file, updated) unless updated == content
end

puts "Generated and wired #{PAGES.length} guide images."
