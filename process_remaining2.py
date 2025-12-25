#!/usr/bin/env python3

import os
import re
import shutil
import urllib.parse

# Find all remaining assets
remaining_assets = []
for root, dirs, files in os.walk('static/dingen/wp-content'):
    for file in files:
        filepath = os.path.join(root, file)
        remaining_assets.append(filepath)

print(f"Found {len(remaining_assets)} remaining assets")

# For each asset, find references with URL-encoded names
for asset in remaining_assets:
    filename = os.path.basename(asset)
    # Encode with only dots and dashes as safe characters
    encoded_filename = urllib.parse.quote(filename, safe='.-')

    # Search for references (both encoded and unencoded)
    bundles = set()

    for root, dirs, files in os.walk('content/posts'):
        if 'index.md' in files:
            index_path = os.path.join(root, 'index.md')
            with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Check for encoded version (the %XX pattern)
            # Replace _ with %5F, spaces with %20, etc.
            pattern = filename.replace('_', '%5F').replace(' ', '%20').replace('(', '%28').replace(')', '%29')

            if pattern in content or filename in content:
                bundle_dir = root
                bundles.add(bundle_dir)

    if bundles:
        print(f"\nProcessing {filename}:")
        for bundle in bundles:
            # Copy asset to bundle
            dest = os.path.join(bundle, filename)
            if not os.path.exists(dest):
                shutil.copy2(asset, dest)
                print(f"  Copied to {bundle}")
            else:
                print(f"  Already exists in {bundle}")

            # Update references to use unencoded filename
            index_path = os.path.join(bundle, 'index.md')
            with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Replace encoded version with unencoded
            pattern = filename.replace('_', '%5F').replace(' ', '%20').replace('(', '%28').replace(')', '%29')
            if pattern in content:
                content = content.replace(pattern, filename)

                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Updated references in {index_path}")

        # Remove original
        os.remove(asset)
        print(f"  Removed original {asset}")

print("\nDone!")
