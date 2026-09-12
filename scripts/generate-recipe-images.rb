require "cgi"
require "date"
require "fileutils"
require "pathname"

ROOT = Pathname.new(__dir__).parent
RECIPES = ROOT.join("docs", "automation")
OUTPUT = ROOT.join("docs", "assets", "img", "social", "recipes")
PLATFORM_IMAGES = ROOT.join("docs", "assets", "img", "social")

CATEGORIES = {
  "lighting" => ["Lighting", "#7f9072"],
  "climate" => ["Climate", "#6f8f96"],
  "security" => ["Safety and security", "#7c8794"],
  "appliances" => ["Appliances", "#907f72"],
  "notifications" => ["Alerts and reminders", "#8b8291"],
  "entertainment" => ["Entertainment", "#71818f"],
  "daily-routines" => ["Daily routines", "#8c8572"]
}.freeze

def wrap_text(text, limit, maximum_lines)
  words = text.split
  lines = []
  current = ""

  words.each do |word|
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

def illustration(category, accent)
  common = %(fill="none" stroke="#2c3e50" stroke-width="9" stroke-linecap="round" stroke-linejoin="round")

  case category
  when "lighting"
    <<~SVG
      <g transform="translate(730 125)" #{common}>
        <path d="M82 178c0-67 54-121 121-121s121 54 121 121c0 45-25 85-63 106v58H145v-58c-38-21-63-61-63-106z" fill="#eef2f3"/>
        <path d="M145 385h116M158 425h90"/>
        <circle cx="203" cy="178" r="28" fill="#{accent}" stroke="none"/>
        <path d="M203 57V7M82 91 45 54M324 91l37-37M42 178H-8M414 178h-50" stroke="#{accent}"/>
        <rect x="-12" y="305" width="95" height="125" rx="12" fill="#ffffff"/>
        <path d="M14 343h43M14 372h43M14 401h43" stroke="#{accent}" stroke-width="6"/>
      </g>
    SVG
  when "climate"
    <<~SVG
      <g transform="translate(680 118)" #{common}>
        <rect x="77" y="38" width="220" height="360" rx="110" fill="#eef2f3"/>
        <path d="M187 90v190"/>
        <circle cx="187" cy="310" r="56" fill="#{accent}" stroke="none"/>
        <path d="M187 154h54M187 210h38" stroke="#{accent}" stroke-width="7"/>
        <circle cx="386" cy="170" r="70"/>
        <path d="M386 170c-55-48-53-82-18-87 34-5 43 35 18 87zm0 0c55 48 53 82 18 87-34 5-43-35-18-87zm0 0c-48 55-82 53-87 18-5-34 35-43 87-18z" fill="#ffffff" stroke="#{accent}" stroke-width="7"/>
        <circle cx="386" cy="170" r="12" fill="#2c3e50" stroke="none"/>
      </g>
    SVG
  when "security"
    <<~SVG
      <g transform="translate(700 110) scale(.9)" #{common}>
        <path d="M205 20c61 43 123 54 168 58v131c0 108-68 183-168 225C105 392 37 317 37 209V78c45-4 107-15 168-58z" fill="#eef2f3"/>
        <path d="m125 223 53 53 111-124" stroke="#{accent}" stroke-width="15"/>
        <rect x="390" y="112" width="52" height="142" rx="10" fill="#ffffff"/>
        <rect x="465" y="112" width="25" height="142" rx="8" fill="#ffffff"/>
        <path d="M442 183h23" stroke="#{accent}" stroke-width="6" stroke-dasharray="5 8"/>
      </g>
    SVG
  when "appliances"
    <<~SVG
      <g transform="translate(700 112)" #{common}>
        <rect x="55" y="15" width="300" height="420" rx="25" fill="#eef2f3"/>
        <path d="M55 112h300"/>
        <circle cx="205" cy="270" r="102" fill="#ffffff"/>
        <path d="M136 273c24-42 65-27 87-5 24 24 55 35 84 7" stroke="#{accent}" stroke-width="12"/>
        <circle cx="102" cy="64" r="13" fill="#{accent}" stroke="none"/>
        <circle cx="151" cy="64" r="13" fill="#{accent}" stroke="none"/>
        <rect x="218" y="45" width="92" height="37" rx="8" fill="#ffffff"/>
        <path d="M410 155v176M380 185h60M380 301h60" stroke="#{accent}"/>
      </g>
    SVG
  when "notifications"
    <<~SVG
      <g transform="translate(700 118) scale(.9)" #{common}>
        <path d="M85 305h250c-35-35-48-77-48-145 0-62-37-108-77-122V15h-1v23c-40 14-77 60-77 122 0 68-12 110-47 145z" fill="#eef2f3"/>
        <path d="M165 346c8 34 28 53 44 53s36-19 44-53"/>
        <circle cx="209" cy="174" r="24" fill="#{accent}" stroke="none"/>
        <path d="M367 91c50 43 50 123 0 166M408 51c75 66 75 190 0 256" stroke="#{accent}"/>
        <rect x="8" y="116" width="72" height="116" rx="13" fill="#ffffff"/>
        <circle cx="44" cy="204" r="7" fill="#{accent}" stroke="none"/>
      </g>
    SVG
  when "entertainment"
    <<~SVG
      <g transform="translate(735 120) scale(.84)" #{common}>
        <rect x="25" y="45" width="330" height="230" rx="18" fill="#eef2f3"/>
        <path d="M145 340h90M190 275v65"/>
        <rect x="390" y="106" width="88" height="235" rx="25" fill="#ffffff"/>
        <circle cx="434" cy="170" r="22" fill="#{accent}" stroke="none"/>
        <circle cx="434" cy="275" r="43"/>
        <path d="M96 134v75c0 24-40 30-40 4 0-20 23-29 40-20M96 134l92-20v75c0 24-40 30-40 4 0-20 23-29 40-20" stroke="#{accent}"/>
      </g>
    SVG
  else
    <<~SVG
      <g transform="translate(690 112) scale(.85)" #{common}>
        <path d="M25 197 205 48l180 149"/>
        <path d="M66 177v250h278V177" fill="#eef2f3"/>
        <circle cx="205" cy="270" r="76" fill="#ffffff"/>
        <path d="M205 218v58l42 26" stroke="#{accent}" stroke-width="12"/>
        <circle cx="205" cy="270" r="10" fill="#2c3e50" stroke="none"/>
        <circle cx="405" cy="82" r="45" fill="#{accent}" stroke="none"/>
        <path d="M405 12V-18M405 182v30M335 82h-30M505 82h30M355 32l-22-22M455 132l22 22M455 32l22-22" stroke="#{accent}" stroke-width="7"/>
      </g>
    SVG
  end
end

def build_svg(title, description, category)
  category_name, accent = CATEGORIES.fetch(category)
  title_lines = wrap_text(title, 25, 3)
  title_size = title_lines.length == 3 ? 46 : 54
  title_step = title_size + 8
  title_start = 171
  description_start = title_start + (title_lines.length * title_step) + 27
  description_lines = wrap_text(description, 46, 3)

  <<~SVG
    <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title desc">
      <title id="title">#{CGI.escapeHTML(title)}</title>
      <desc id="desc">#{CGI.escapeHTML(description)}</desc>
      #{theme_style}
      <rect width="1200" height="630" fill="#f8f9fa"/>
      <rect x="52" y="52" width="1096" height="526" rx="28" fill="#ffffff" stroke="#e0e0e0" stroke-width="2"/>
      <rect x="108" y="88" width="#{category_name.length * 12 + 46}" height="43" rx="21" fill="#eef2f3"/>
      <text x="131" y="116" fill="#2c3e50" font-family="Segoe UI, Arial, sans-serif" font-size="19" font-weight="600">#{CGI.escapeHTML(category_name.upcase)}</text>
      #{text_lines(title_lines, x: 108, y: title_start, size: title_size, step: title_step, color: "#2c3e50", weight: "700")}
      #{text_lines(description_lines, x: 108, y: description_start, size: 22, step: 31, color: "#5d6d75")}
      <g transform="translate(108 469)" font-family="Segoe UI, Arial, sans-serif" font-size="17" font-weight="600">
        <rect width="105" height="39" rx="19" fill="#eef2f3"/><text x="23" y="25" fill="#2c3e50">TRIGGER</text>
        <path d="M117 20h39" stroke="#9db1b6" stroke-width="4"/>
        <rect x="168" width="96" height="39" rx="19" fill="#eef2f3"/><text x="190" y="25" fill="#2c3e50">CHECK</text>
        <path d="M276 20h39" stroke="#9db1b6" stroke-width="4"/>
        <rect x="327" width="102" height="39" rx="19" fill="#{accent}"/><text x="346" y="25" fill="#ffffff">ACTION</text>
      </g>
      #{illustration(category, accent)}
      <text x="108" y="550" fill="#6b777c" font-family="Segoe UI, Arial, sans-serif" font-size="20">HOME AUTOMATION COOKBOOK</text>
    </svg>
  SVG
end

def extract(content, field)
  match = content.match(/^#{Regexp.escape(field)}:[ \t]*(.+?)[ \t]*\r*$/)
  raise "Missing #{field}" unless match

  match[1]
end

def wire_page(file, content, image_url, hero_url)
  already_wired = content.include?(%(class="content-hero")) &&
    content.match?(/^image:[ \t]*#{Regexp.escape(image_url)}\r*$/) &&
    content.include?(%(src="#{hero_url}"))
  return content if already_wired

  eol = content.include?("\r\n") ? "\r\n" : "\n"
  updated = content.sub(/^last_modified_at:[^\r\n]*/, "last_modified_at: #{Date.today.iso8601}")

  if updated.match?(/^image:/)
    updated.sub!(/^image:[^\r\n]*/, "image: #{image_url}")
  else
    updated.sub!(/^(last_modified_at:[^\r\n]*)(\r*\n)/, "\\1\\2image: #{image_url}#{eol}")
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

  unless updated.include?(image_url) && updated.include?(hero_url) && updated.include?(%(class="content-hero"))
    raise "Could not wire #{file}"
  end

  updated
end

generated = 0

Dir[PLATFORM_IMAGES.join("platform*.svg")].sort.each do |path|
  content = File.read(path, encoding: "UTF-8")
  next if content.include?("@media (prefers-color-scheme: dark)")

  themed = content.sub("</desc>", "</desc>\n#{theme_style}")
  raise "Could not add dark theme to #{path}" if themed == content

  File.write(path, themed, encoding: "UTF-8")
end

Dir[RECIPES.join("*", "*.md")].sort.each do |path|
  file = Pathname.new(path)
  content = File.binread(file).force_encoding(Encoding::UTF_8)
  next unless content.match?(/^layout:[ \t]*automation[ \t]*\r*$/)

  category = file.dirname.basename.to_s
  title = extract(content, "title")
  description = extract(content, "description")
  destination = OUTPUT.join(category, "#{file.basename(".md")}.svg")
  image_url = "/assets/img/social/recipes/#{category}/#{file.basename(".md")}.png"
  hero_url = "/assets/img/social/recipes/#{category}/#{file.basename(".md")}.svg"

  FileUtils.mkdir_p(destination.dirname)
  File.write(destination, build_svg(title, description, category), newline: :lf)

  updated = wire_page(file, content, image_url, hero_url)
  File.binwrite(file, updated) unless updated == content
  generated += 1
end

puts "Generated and wired #{generated} recipe images."
