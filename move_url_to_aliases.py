#!/usr/bin/env python3

import os
import re
import glob

def process_file(filepath):
    """Process a single markdown file to move url to aliases"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Check if file has frontmatter
    if not content.startswith('---'):
        return False

    # Split into frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1]
    body = parts[2]

    # Extract url value
    url_match = re.search(r'^url:\s*(.+)$', frontmatter, re.MULTILINE)
    if not url_match:
        return False  # No url field

    url_value = url_match.group(1).strip()

    # Check if aliases already exists
    aliases_match = re.search(r'^aliases:\s*$', frontmatter, re.MULTILINE)

    if aliases_match:
        # Aliases exists - add url to it
        # Find where aliases section ends (next non-indented line)
        aliases_start = aliases_match.end()
        remaining = frontmatter[aliases_start:]

        # Find where to insert (before next non-indented line)
        next_field = re.search(r'\n([a-zA-Z_])', remaining)
        if next_field:
            insert_pos = aliases_start + next_field.start() + 1
            new_frontmatter = (
                frontmatter[:insert_pos] +
                f"  - {url_value}\n" +
                frontmatter[insert_pos:]
            )
        else:
            # Aliases is the last field
            new_frontmatter = frontmatter + f"  - {url_value}\n"
    else:
        # No aliases field - create it where url was
        new_frontmatter = re.sub(
            r'^url:\s*.+$',
            f'aliases:\n  - {url_value}',
            frontmatter,
            flags=re.MULTILINE
        )

    # Write back
    new_content = '---' + new_frontmatter + '---' + body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

# Process all posts
processed = 0
for filepath in glob.glob('content/posts/*/index.md'):
    if process_file(filepath):
        processed += 1
        print(f"Processed: {filepath}")

# Process all pages
for filepath in glob.glob('content/pages/*/index.md'):
    if process_file(filepath):
        processed += 1
        print(f"Processed: {filepath}")

print(f"\nTotal processed: {processed} files")
