#!/usr/bin/env python3

import os
import glob
from collections import defaultdict

def extract_frontmatter_keys(filepath):
    """Extract all frontmatter keys from a markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check if file has frontmatter
        if not content.startswith('---'):
            return []

        # Split into frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            return []

        frontmatter = parts[1]

        # Manual extraction of keys (works without yaml library)
        keys = []
        for line in frontmatter.split('\n'):
            # Skip empty lines and list items
            if not line or line.strip().startswith('-'):
                continue

            # Look for key: value patterns at the start of lines
            stripped = line.lstrip()
            if stripped and ':' in stripped and not stripped.startswith(' '):
                # Get the part before the first colon
                key = stripped.split(':')[0].strip()
                if key:
                    keys.append(key)

        return keys

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []

# Analyze all markdown files
print("Analyzing frontmatter keys in all markdown files...\n")

key_counts = defaultdict(int)
key_examples = defaultdict(list)
total_files = 0

for pattern in ['content/posts/*/index.md', 'content/pages/*/index.md']:
    for filepath in glob.glob(pattern):
        total_files += 1
        keys = extract_frontmatter_keys(filepath)

        for key in keys:
            key_counts[key] += 1
            if len(key_examples[key]) < 3:  # Store up to 3 examples
                key_examples[key].append(filepath)

# Sort by frequency
sorted_keys = sorted(key_counts.items(), key=lambda x: x[1], reverse=True)

print(f"Total files analyzed: {total_files}")
print(f"Unique frontmatter keys found: {len(sorted_keys)}\n")
print("="*80)
print(f"{'Key':<40} {'Count':<10} {'Percentage'}")
print("="*80)

for key, count in sorted_keys:
    percentage = (count / total_files) * 100
    print(f"{key:<40} {count:<10} {percentage:>6.1f}%")

print("\n" + "="*80)
print("Key categories:")
print("="*80)

# Categorize keys
wordpress_keys = [k for k, c in sorted_keys if k.startswith('_') or k in ['guid', 'post_id', 'parent_post_id']]
hugo_standard = [k for k, c in sorted_keys if k in ['title', 'date', 'author', 'categories', 'tags', 'aliases', 'draft', 'description', 'slug', 'url']]
custom_keys = [k for k, c in sorted_keys if k not in wordpress_keys and k not in hugo_standard]

print(f"\nWordPress-specific keys ({len(wordpress_keys)}):")
for key in wordpress_keys[:20]:  # Show first 20
    print(f"  - {key} ({key_counts[key]} files)")

print(f"\nHugo standard keys ({len(hugo_standard)}):")
for key in hugo_standard:
    if key in key_counts:
        print(f"  - {key} ({key_counts[key]} files)")

print(f"\nOther/Custom keys ({len(custom_keys)}):")
for key in custom_keys[:20]:  # Show first 20
    print(f"  - {key} ({key_counts[key]} files)")
