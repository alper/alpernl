number := "`uv run find_next_number.py`"
path := "content/posts/{{ number }}/index.md"

publish:
    hugo --cleanDestinationDir --minify
    rsync -avzP /Users/alpercugun/Documents/projects/wordpress/site/public/ vimexx:/home/u88479p83432/domains/alper.nl/public_html

write:
    hugo new {{ path }}
    hx {{ path }}