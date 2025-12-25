#!/bin/bash

cd /Users/alpercugun/Documents/projects/wordpress/site

# Remove the assets that were copied to bundles
/Users/alpercugun/Documents/projects/wordpress/site/process_assets.sh | while IFS='|' read -r asset bundles; do
    if [ -z "$asset" ]; then
        continue
    fi

    if [ -n "$bundles" ]; then
        rm -f "$asset"
        echo "Removed $asset"
    fi
done

echo "All processed assets removed from static directory"
