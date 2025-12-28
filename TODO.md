
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
* [ ] Run blog on an alt domain
* [ ] Pick a theme with taxonomies
  * https://gohugo.io/content-management/taxonomies/
  * https://github.com/parsiya/Hugo-Octopress
    * Sidebar is empty
    * No search
  * https://github.com/tomowang/hugo-theme-tailwind
    * Can't figure out how to change the homepage
    * For the rest does everything I need
  * https://willfaught.com/paige/categories/
    * Does not show categories on the detail page
  * https://anatole-demo.netlify.app/post/markdown-syntax/
    * Typography is reasonable though not great
    * Sidebar looks pretty broken out of the box
  * https://themes.gohugo.io/themes/tailroad/
    * Does pretty much everything I want to do
    * Sidebar does not show
    * Posts list is pretty broken
    * Posts list does not paginate at all and displays everything

  * maybe: https://github.com/maolonglong/hugo-simple
  * maybe: https://themes.gohugo.io/themes/hugo-bearneo/
    * Doesn't display categories on the post detail
  * maybe: https://themes.gohugo.io/themes/rusty-typewriter/
    * Shows fallback for titleless posts by default
    * Sidebar won't show
    * Search is supposedly built-in but not findable
  * maybe: https://themes.gohugo.io/themes/zen/
    * Does pretty much everything I want it to do
    * Typography is just not very good
    * Search is broken
  * maybe: https://themes.gohugo.io/themes/hugo-theme-yue/
  * maybe: https://themes.gohugo.io/themes/triple-hyde/
    * Typography on detail is fine
    * List views do not show any body text
  * https://github.com/zetxek/adritian-free-hugo-theme
  * https://github.com/tom2almighty/hugo-narrow
    * Nice layout
    * Very good: http://localhost:1313/categories/
    * Broken: http://localhost:1313/posts/
    * No search, though it's supposed to have it, search is a modal
    * [ ] Remove copyright notice
    * [ ] Do fuller configuration
    * This could definitely be the theme.
  * https://github.com/tomfran/typo
    * Very clean and empty
  * https://github.com/CaiJimmy/hugo-theme-stack
    * Clean if a bit bare theme
    * Not sure if it has search
  * https://github.com/nunocoracao/blowfish
    * Very nice by default
    * Need to see what this can do if it's fully configured

* Config setup
  * [ ] https://gohugo.io/configuration/all/
  * [x] Remove /dingen prefix
  * [x] Create new permalink setup and alias the old links
    * https://gohugo.io/configuration/permalinks/
  * [ ] Set correct homepage
  * [ ] Setup feed with redirect of old feed
  * [ ] Figure out category feeds and why they aren't linked up
* Theme edits
  * [x] Fix display of titleless posts
  * [ ] Fix display of titleless posts in search
  * [x] Remove time to read
  * [x] Show all categories
  * [ ] Remove dangling categories
  * [ ] Show full posts on list display
* Data edits
  * [x] Remove all tags from posts
  * [x] Remove post_id?
    * https://gohugobrasil.netlify.app/content-management/front-matter/
  * [x] Fix character encoding issues from posts
  * [x] Move images to final destination and change image links (see if Claude can move them into folders for each post)
  * [x] Remove the _edit_last, parent_post_id and _wpas_done_all fields
  * [x] Check for other superfluous fields to be removed
* [ ] Backport old blog content into markdown
* [ ] Download statick.flickr images and put them into the bundles
* [ ] Fix footnotes that are of the (()) format

* [x] More charset issues
  * http://localhost:1313/blog/my-year-in-cities-2008/
  * http://localhost:1313/blog/jurriaan-van-stigt-arcam-lecture/
  * http://localhost:1313/blog/encounter-zone-maasenstrase/
  * http://localhost:1313/blog/het-manifest-van-terschelling/
* [ ] Recategorize posts
  * [ ] Japanese
  * [ ] Fix: æ—¥æœ¬èªž
  * Tag publicity: http://localhost:1313/blog/week-323/
* Turn Kumano Kodo posts into a series: https://blowfish.page/docs/series/

* [ ] What happened with the image in this post? http://localhost:1313/blog/17632/

* [ ] Pick a better theme
  * Triple Hyde is good
* [ ] Get rid of all GIFs
* [ ] Create impressum page?


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