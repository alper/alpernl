#!/usr/bin/env python3

import os
import glob
import re

def remove_oembed_fields(filepath):
    """Remove all _oembed* fields from frontmatter"""
    try:
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

        # Count oembed lines before removal
        oembed_count_before = len([line for line in frontmatter.split('\n') if line.strip().startswith('_oembed')])

        if oembed_count_before == 0:
            return False

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
        return False

# Test on a sample file first
print("Testing on sample file...")
test_file = 'content/posts/16392/index.md'

with open(test_file, 'r', encoding='utf-8') as f:
    before = f.read()
    print("BEFORE (first 25 lines):")
    print('\n'.join(before.split('\n')[:25]))

removed = remove_oembed_fields(test_file)

with open(test_file, 'r', encoding='utf-8') as f:
    after = f.read()
    print("\n" + "="*80)
    print("AFTER (first 25 lines):")
    print('\n'.join(after.split('\n')[:25]))

if removed:
    print(f"\n✓ Removed {removed} _oembed lines from test file")
else:
    print("\n✗ No changes made")

print("\nTest complete. Ready to process all files.")
