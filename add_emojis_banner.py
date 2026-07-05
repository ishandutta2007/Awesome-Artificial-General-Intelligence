import os
import re

base_dir = r'C:\Users\ishan\Documents\Projects\Awesome-Artificial-General-Intelligence'
readme_path = os.path.join(base_dir, 'README.md')
assets_dir = os.path.join(base_dir, 'assets')

os.makedirs(assets_dir, exist_ok=True)

# Generate SVG
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#8A2387;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#E94057;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#F27121;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="15" ry="15" fill="url(#grad1)" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="36" font-weight="bold" fill="white">
    Awesome Artificial General Intelligence
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite" />
  </text>
</svg>"""

with open(os.path.join(assets_dir, 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_content)

# Update README
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Emojis for headers
replacements = {
    "# Awesome-Artificial-General-Intelligence": "# 🌟 Awesome-Artificial-General-Intelligence",
    "## Artificial General Intelligence (AGI):": "## 🧠 Artificial General Intelligence (AGI):",
    "## 1. The Macro Chronological Evolution": "## ⏳ 1. The Macro Chronological Evolution",
    "## 2. Quantitative Classification: The 5 Levels of AGI": "## 📊 2. Quantitative Classification: The 5 Levels of AGI",
    "## 3. High-Capacity Architectural & System Engineering Components": "## 🏗️ 3. High-Capacity Architectural & System Engineering Components",
    "## 4. Production Engineering Challenges & Frontier Mitigations": "## ⚠️ 4. Production Engineering Challenges & Frontier Mitigations",
    "## 5. Frontier Real-World Infrastructure Applications": "## 🚀 5. Frontier Real-World Infrastructure Applications",
    "## References": "## 📚 References"
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Add banner at top
if "![Banner]" not in content:
    content = content.replace("# 🌟 Awesome-Artificial-General-Intelligence", "![Banner](./assets/banner.svg)\n\n# 🌟 Awesome-Artificial-General-Intelligence")

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
