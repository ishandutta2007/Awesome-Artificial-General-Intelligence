import os
import re

readme_path = r'C:\Users\ishan\Documents\Projects\Awesome-Artificial-General-Intelligence\README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

rows = re.findall(r'\| \*\*(.*?)\*\* \|', content)
print(f'Found {len(rows)} items')
for r in rows:
    print(r)
