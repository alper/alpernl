#!/bin/bash

cd /Users/alpercugun/Documents/projects/wordpress/site

# Function to URL encode a filename
urlencode() {
    python3 -c "import sys, urllib.parse as ul; print(ul.quote(sys.argv[1], safe='.-'))" "$1"
}

# For each bundle that has assets
/Users/alpercugun/Documents/projects/wordpress/site/process_assets.sh | while IFS='|' read -r asset bundles; do
    if [ -z "$asset" ]; then
        continue
    fi

    filename=$(basename "$asset")
    encoded_filename=$(urlencode "$filename")

    # Split bundles by comma
    IFS=',' read -ra BUNDLE_ARRAY <<< "$bundles"

    for bundle in "${BUNDLE_ARRAY[@]}"; do
        if [ -z "$bundle" ]; then
            continue
        fi

        # Update references - match both plain and URL-encoded filenames
        perl -pi -e "s|/dingen/wp-content/uploads/[^)\"]+/${filename}|${filename}|g" "$bundle/index.md"
        perl -pi -e "s|/dingen/wp-content/uploads/[^)\"]+/${encoded_filename}|${filename}|g" "$bundle/index.md"
        echo "Fixed all references to $filename in $bundle/index.md"
    done
done
