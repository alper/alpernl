
## Research

* [ ] Finish all drafts on blog
* [x] Check metadata of [wordpress-export-to-markdown](https://github.com/lonekorean/wordpress-export-to-markdown?tab=readme-ov-file) and wp2hugo
  * wp2hugo has a lot more metadata
* [x] Check if wp2hugo url metadata is maintained
* [x] Check if Hugo themes can be edited
* [x] Check what the guid field is for
  * It looks like guid can go
* [ ] Check what the post authoring flow would be like on Hugo
* [x] Try out Pelican
  * Pelican does not support multiple categories
* [x] Try out Zola
  * Does not work: https://github.com/getzola/zola/issues/3047
* [ ] Figure out how to publish

## Migration

* [ ] Make backup of blog
* [ ] Pick a theme with taxonomies
  * https://gohugo.io/content-management/taxonomies/
  * https://github.com/parsiya/Hugo-Octopress
  * https://github.com/tomowang/hugo-theme-tailwind
  * https://willfaught.com/paige/categories/
  * https://anatole-demo.netlify.app/post/markdown-syntax/
  * https://themes.gohugo.io/themes/tailroad/

  * maybe: https://github.com/maolonglong/hugo-simple
  * maybe: https://themes.gohugo.io/themes/hugo-bearneo/
  * maybe: https://themes.gohugo.io/themes/rusty-typewriter/
  * maybe: https://themes.gohugo.io/themes/zen/
  * maybe: https://themes.gohugo.io/themes/hugo-theme-yue/
  * maybe: https://themes.gohugo.io/themes/triple-hyde/

* Config setup
  * [ ] https://gohugo.io/configuration/all/
  * [ ] Remove /dingen prefix
  * [ ] https://gohugo.io/configuration/permalinks/
* Theme edits
  * [ ] Fix display of titleless posts
* Data edits
  * [ ] Remove all tags from posts
  * [ ] Remove post_id?
    * https://gohugobrasil.netlify.app/content-management/front-matter/
  * [ ] Fix character encoding issues from posts
  * [ ] Move images to final destination and change image links (see if Claude can move them into folders for each post)
  * [ ] Remove the _edit_last, parent_post_id and _wpas_done_all fields
  * [ ] Check for other superfluous fields to be removed
* [ ] Backport old blog content into markdown


Ask Claude:

* Turn each post into a hugo page bundle
* Go through the static folder and copy it to any post that references it while updating the links to it in all posts to be relative
* Remove all URL fields?
* Fix all the double encoding issues


  Broken links (files don't exist):

  These references remain but point to non-existent files:
  1. /posts/playing-with-public-transportation-data/ → traveltimes.json (missing)
  2. /posts/dutch-public-broadcasting-goes-fake-news/ → ongelofelijke-mensenmassa.mp4 (missing, 2 references)
  3. /posts/fragment-tegengif-87-over-ozb/ → tegengif_ozb.mov (missing)