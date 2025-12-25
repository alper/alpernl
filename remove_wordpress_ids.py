#!/usr/bin/env python3

import os
import glob

def remove_wordpress_ids(filepath):
    """Remove WordPress ID fields (guid, post_id, parent_post_id) from frontmatter"""
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

        # List of fields to remove
        fields_to_remove = [
            'guid',
            'post_id',
            'parent_post_id',
        ]

        lines = frontmatter.split('\n')
        new_lines = []
        removed_count = 0

        for line in lines:
            stripped = line.strip()

            # Skip empty lines or list items
            if not stripped or stripped.startswith('-'):
                new_lines.append(line)
                continue

            # Check if this is a key: value line
            if ':' not in stripped:
                new_lines.append(line)
                continue

            # Extract the key
            key = stripped.split(':')[0].strip()

            # Check if key matches fields to remove
            if key in fields_to_remove:
                removed_count += 1
                continue

            new_lines.append(line)

        if removed_count == 0:
            return 0

        new_frontmatter = '\n'.join(new_lines)

        # Write back
        new_content = '---' + new_frontmatter + '---' + body

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return removed_count

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

# Process all markdown files
print("Removing WordPress IDs (guid, post_id, parent_post_id) from all markdown files...")
total_files = 0
modified_files = 0
total_lines_removed = 0

for pattern in ['content/posts/*/index.md', 'content/pages/*/index.md']:
    for filepath in glob.glob(pattern):
        total_files += 1
        removed = remove_wordpress_ids(filepath)
        if removed:
            modified_files += 1
            total_lines_removed += removed
            if modified_files <= 10:  # Show first 10
                print(f"  Removed {removed} IDs from {filepath}")

print(f"\nProcessed {total_files} files")
print(f"Modified {modified_files} files")
print(f"Removed {total_lines_removed} total WordPress ID lines")
