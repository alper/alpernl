#!/bin/bash

cd /Users/alpercugun/Documents/projects/wordpress/site

/Users/alpercugun/Documents/projects/wordpress/site/process_assets.sh | while IFS='|' read -r asset bundles; do
    if [ -z "$asset" ]; then
        continue
    fi

    filename=$(basename "$asset")

    # Split bundles by comma
    IFS=',' read -ra BUNDLE_ARRAY <<< "$bundles"

    for bundle in "${BUNDLE_ARRAY[@]}"; do
        if [ -z "$bundle" ]; then
            continue
        fi

        # Copy asset to bundle directory
        cp "$asset" "$bundle/"
        echo "Copied $filename to $bundle/"

        # Update reference in index.md
        # Replace /dingen/wp-content/uploads/.../$filename with just $filename
        sed -i.bak "s|/dingen/wp-content/uploads/[^)]*/\\${filename}|${filename}|g" "$bundle/index.md"
        echo "Updated references in $bundle/index.md"

        # Clean up backup file
        rm -f "$bundle/index.md.bak"
    done
done
