next_number := `uv run find_next_number.py`

publish:
    hugo --cleanDestinationDir --minify
    rsync -avzP --delete /Users/alpercugun/Documents/projects/wordpress/site/public/ vimexx:/home/u88479p83432/domains/alper.nl/public_html

sync:
    jj git fetch
    jj tug
    jj git push

_write title:
    echo "New path: content/posts/{{ title }}/index.md"
    hugo new content/posts/{{ title }}/index.md
    code content/posts/{{ title }}/index.md

write slug=next_number: (_write slug)

serve:
    hugo server --buildDrafts --disableFastRender