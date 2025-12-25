#!/bin/bash

cd /Users/alpercugun/Documents/projects/wordpress/site

# Find all files that still have wp-content references
grep -l "dingen/wp-content/uploads" content/posts/*/index.md | while read -r file; do
    echo "Fixing broken links in $file"

    # Replace remaining wp-content URLs with just the filename
    perl -pi -e 's|/dingen/wp-content/uploads/[^)"\s]+/([^/)"\s]+\.(?:jpg|jpeg|png|gif|pdf|mp3))|$1|g' "$file"
done

echo "All broken links fixed"
