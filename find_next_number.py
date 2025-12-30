#!/usr/bin/env python3
"""
Find the highest numeric folder name in content/posts and return the next available number.
"""

import os
from pathlib import Path

def find_next_available_number(posts_dir='content/posts'):
    """Find the highest numeric folder name and return next available."""
    posts_path = Path(posts_dir)

    if not posts_path.exists():
        print(f"Error: Directory {posts_dir} does not exist")
        return None

    numeric_folders = []

    # Get all directories in content/posts
    for item in posts_path.iterdir():
        if item.is_dir():
            try:
                # Try to convert folder name to integer
                number = int(item.name)
                numeric_folders.append(number)
            except ValueError:
                # Skip non-numeric folder names
                continue

    if not numeric_folders:
        print("No numeric folders found")
        return 1

    # Sort the numbers
    numeric_folders.sort()

    highest = numeric_folders[-1]
    next_number = highest + 1

    # print(f"Found {len(numeric_folders)} numeric folders")
    # print(f"Highest number: {highest}")
    print(f"{next_number}")

    return next_number


if __name__ == '__main__':
    find_next_available_number()
