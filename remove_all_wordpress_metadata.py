#!/usr/bin/env python3

import os
import glob

def remove_wordpress_metadata(filepath):
    """Remove WordPress-specific metadata fields from frontmatter"""
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

        # List of exact keys to remove
        exact_keys = [
            '_wpas_done_all',
            '_edit_last',
            '_last_editor_used_jetpack',
            '_wp_old_slug',
        ]

        # List of prefixes to remove
        prefix_patterns = [
            '_g_feedback_shortcode_',
            '_yoast_wpseo_',
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

            # Check if key matches exact keys
            if key in exact_keys:
                removed_count += 1
                continue

            # Check if key matches any prefix pattern
            should_remove = False
            for prefix in prefix_patterns:
                if key.startswith(prefix):
                    should_remove = True
                    removed_count += 1
                    break

            if not should_remove:
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
print("Removing WordPress metadata from all markdown files...")
total_files = 0
modified_files = 0
total_lines_removed = 0

for pattern in ['content/posts/*/index.md', 'content/pages/*/index.md']:
    for filepath in glob.glob(pattern):
        total_files += 1
        removed = remove_wordpress_metadata(filepath)
        if removed:
            modified_files += 1
            total_lines_removed += removed
            if modified_files <= 10:  # Show first 10
                print(f"  Removed {removed} lines from {filepath}")

print(f"\nProcessed {total_files} files")
print(f"Modified {modified_files} files")
print(f"Removed {total_lines_removed} total WordPress metadata lines")
