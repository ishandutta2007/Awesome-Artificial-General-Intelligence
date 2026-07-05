import os

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Artificial-General-Intelligence\README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

seo_text = "\n\n<!-- SEO tags: AGI, Artificial General Intelligence, Human-Level AI, Strong AI, Embodied AI, Machine Learning, Deep Learning, Foundation Models, LLMs, Neural Networks -->\n*A comprehensive curated list of Awesome Artificial General Intelligence (AGI) resources, tracking the evolution, architecture, and milestones toward human-level and superhuman AI.*"

# Insert badges and SEO text after the main heading
heading = "# 🌟 Awesome-Artificial-General-Intelligence"
if heading in content:
    new_text = heading + "\n\n<div align=\"center\">\n" + left_badges + "\n</div>" + seo_text
    content = content.replace(heading, new_text)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
