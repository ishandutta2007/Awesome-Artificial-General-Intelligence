import os

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Artificial-General-Intelligence\README.md'

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

# Find the badge block and append the right badge before the closing </div>
if 'alt="Discord" /></a>\n</div>' in content:
    content = content.replace('alt="Discord" /></a>\n</div>', f'alt="Discord" /></a>{right_badge}\n</div>')
elif 'alt="Discord" /></a></div>' in content:
    content = content.replace('alt="Discord" /></a></div>', f'alt="Discord" /></a>{right_badge}</div>')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
