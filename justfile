path := "content/posts/" + `uv run find_next_number.py` + "/index.md"

publish:
    hugo --cleanDestinationDir --minify
    rsync -avzP /Users/alpercugun/Documents/projects/wordpress/site/public/ vimexx:/home/u88479p83432/domains/alper.nl/public_html

_write path:
    echo "New path: {{ path }}"
    hugo new {{ path }}
    hx {{ path }}

write: (_write path)