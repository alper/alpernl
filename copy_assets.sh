#!/bin/bash

# Script to copy assets to their bundles and update references

cd /Users/alpercugun/Documents/projects/wordpress/site

# Process each mapping
cat <<'EOF' | while IFS='|' read asset bundles; do
    filename=$(basename "$asset")

    # Split bundles by comma
    IFS=',' read -ra BUNDLE_ARRAY <<< "$bundles"

    for bundle in "${BUNDLE_ARRAY[@]}"; do
        # Copy asset to bundle directory
        cp "$asset" "$bundle/"
        echo "Copied $filename to $bundle/"

        # Update reference in index.md
        # Replace /dingen/wp-content/uploads/.../$filename with just $filename
        sed -i.bak "s|/dingen/wp-content/uploads/[^)]*/$filename|$filename|g" "$bundle/index.md"
        echo "Updated references in $bundle/index.md"

        # Clean up backup file
        rm -f "$bundle/index.md.bak"
    done
done
EOF
