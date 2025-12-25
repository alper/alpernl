#!/bin/bash

# Script to find which bundles reference which assets
# Output format: asset_path|bundle1,bundle2,bundle3

cd /Users/alpercugun/Documents/projects/wordpress/site

# Find all assets
find static/dingen/wp-content -type f | while read asset; do
    # Extract the filename
    filename=$(basename "$asset")

    # Search for references in content
    bundles=$(grep -l "$filename" content/posts/*/index.md 2>/dev/null | sed 's|/index.md||' | tr '\n' ',' | sed 's/,$//')

    if [ -n "$bundles" ]; then
        echo "$asset|$bundles"
    fi
done
