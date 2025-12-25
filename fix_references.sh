#!/bin/bash

cd /Users/alpercugun/Documents/projects/wordpress/site

# For each bundle that has assets
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

        # Update references - use perl for more robust regex
        perl -pi -e "s|/dingen/wp-content/uploads/[^)]+/${filename}|${filename}|g" "$bundle/index.md"
        echo "Fixed references to $filename in $bundle/index.md"
    done
done
