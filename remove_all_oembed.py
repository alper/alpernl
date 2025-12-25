#!/usr/bin/env python3

import os
import glob

def remove_oembed_fields(filepath):
    """Remove all _oembed* fields from frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check if file has frontmatter
        if not content.startswith('---'):
            return 0

        # Split into frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            return 0

        frontmatter = parts[1]
        body = parts[2]

        # Count oembed lines before removal
        oembed_count_before = len([line for line in frontmatter.split('\n') if line.strip().startswith('_oembed')])

        if oembed_count_before == 0:
            return 0

        # Remove all lines starting with _oembed
        lines = frontmatter.split('\n')
        new_lines = []

        for line in lines:
            # Skip lines that start with _oembed (after stripping leading whitespace)
            if not line.strip().startswith('_oembed'):
                new_lines.append(line)

        new_frontmatter = '\n'.join(new_lines)

        # Write back
        new_content = '---' + new_frontmatter + '---' + body

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return oembed_count_before

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

# Process all markdown files
print("Removing _oembed fields from all markdown files...")
total_files = 0
modified_files = 0
total_lines_removed = 0

for pattern in ['content/posts/*/index.md', 'content/pages/*/index.md']:
    for filepath in glob.glob(pattern):
        total_files += 1
        removed = remove_oembed_fields(filepath)
        if removed:
            modified_files += 1
            total_lines_removed += removed
            if modified_files <= 10:  # Show first 10
                print(f"  Removed {removed} lines from {filepath}")

print(f"\nProcessed {total_files} files")
print(f"Modified {modified_files} files")
print(f"Removed {total_lines_removed} total _oembed lines")
