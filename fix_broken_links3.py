#!/usr/bin/env python3

import re
import sys
import os
import glob

# Pattern to match wp-content URLs
pattern = r'/dingen/wp-content/uploads/[^)"\s]+/([^/)"\s]+\.(jpg|jpeg|png|gif|pdf|mp3))'

# Find all index.md files
for filepath in glob.glob('content/posts/*/index.md'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has wp-content references
    if 'dingen/wp-content/uploads' not in content:
        continue

    print(f"Fixing {filepath}")

    # Replace URLs with just the filename
    content = re.sub(pattern, r'\1', content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done!")
