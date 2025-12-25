#!/bin/bash

# Script to convert Hugo posts to page bundles
# Each post file (post.md) becomes post/index.md

POSTS_DIR="/Users/alpercugun/Documents/projects/wordpress/site/content/posts"

# Counter for progress
count=0
total=$(find "$POSTS_DIR" -maxdepth 1 -type f -name "*.md" | wc -l)

echo "Converting $total posts to bundles..."

# Find all markdown files in the posts directory (not in subdirectories)
find "$POSTS_DIR" -maxdepth 1 -type f -name "*.md" | while read -r file; do
  # Get the filename without path and extension
  filename=$(basename "$file" .md)

  # Create directory for the bundle
  bundle_dir="$POSTS_DIR/$filename"

  # Skip if directory already exists (shouldn't happen, but just in case)
  if [ -d "$bundle_dir" ]; then
    echo "Skipping $filename - directory already exists"
    continue
  fi

  # Create the bundle directory
  mkdir "$bundle_dir"

  # Move the file into the directory and rename to index.md
  mv "$file" "$bundle_dir/index.md"

  # Increment counter and show progress
  count=$((count + 1))
  if [ $((count % 100)) -eq 0 ]; then
    echo "Processed $count/$total posts..."
  fi
done

echo "Conversion complete! Processed $count posts."
