import os
import re

base_dir = r'C:\Users\ishan\Documents\Projects\Awesome-Artificial-General-Intelligence'
readme_path = os.path.join(base_dir, 'README.md')
details_dir = os.path.join(base_dir, 'details')

os.makedirs(details_dir, exist_ok=True)

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all items to replace
# Looking for lines starting with `| **` to replace with `| [**`
rows = re.findall(r'\| \*\*(.*?)\*\* \|', content)

for item in rows:
    # generate filename
    safe_name = re.sub(r'[^a-zA-Z0-9]+', '_', item).strip('_').lower()
    filename = f"{safe_name}.md"
    file_path = os.path.join(details_dir, filename)
    
    # Write detail file
    detail_content = f"""# {item}

Detailed information about **{item}**.

```mermaid
graph TD
    A["{item.replace('"', '')}"] --> B["Core Concept"]
    A --> C["Future Implications"]
```
"""
    with open(file_path, 'w', encoding='utf-8') as df:
        df.write(detail_content)
    
    # Replace in README
    original = f"| **{item}** |"
    replacement = f"| [**{item}**](./details/{filename}) |"
    content = content.replace(original, replacement)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
