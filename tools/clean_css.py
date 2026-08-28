from pathlib import Path
import re

src = Path('thienbach.css').read_text(encoding='utf-8')

# One typography system: Jost only.
src = re.sub(r'@import\s+url\(["\']https://fonts\.googleapis\.com/css\?family=DM\+Sans:400,500\|Jost:400,500,600,700&display=swap["\']\);\s*', '@import url("https://fonts.googleapis.com/css?family=Jost:400,500,600,700&display=swap");\n\n', src)
src = src.replace('"DM Sans"', '"Jost"').replace("'DM Sans'", "'Jost'")

# Remove redundant comment blocks while keeping meaningful CSS declarations.
src = re.sub(r'/\*.*?\*/', '', src, flags=re.S)

# Normalize whitespace without changing CSS values/selectors.
src = re.sub(r'\n[ \t]+\n', '\n\n', src)
src = re.sub(r'\n{3,}', '\n\n', src)
src = re.sub(r'[ \t]+$', '', src, flags=re.M)
src = src.strip() + '\n'

Path('thienbach-clean.css').write_text(src, encoding='utf-8')
print(f'Generated thienbach-clean.css: {len(src.splitlines())} lines, {len(src)} bytes')
