
# TODO

* [x] Finish all drafts on blog
* [x] Check metadata of [wordpress-export-to-markdown](https://github.com/lonekorean/wordpress-export-to-markdown?tab=readme-ov-file) and wp2hugo
  * wp2hugo has a lot more metadata
* [x] Check if wp2hugo url metadata is maintained
* [x] Check if Hugo themes can be edited
* [x] Check what the guid field is for
  * It looks like guid can go
* [x] Check what the post authoring flow would be like on Hugo
  * https://discourse.gohugo.io/t/authoring-flow-without-titles/56428/4
* [x] Try out Pelican
  * Pelican does not support multiple categories
* [x] Try out Zola
  * Does not work: https://github.com/getzola/zola/issues/3047
* [x] Figure out how to publish
* [x] Make backup of blog
* [x] Run blog on an alt domain dingen.alper.nl
* [x] Pick a theme with taxonomies
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
  * [x] Set correct homepage
  * [x] Setup feed with redirect of old feed
  * [ ] Figure out category feeds and why they aren't linked up
* Theme edits
  * [x] Fix display of titleless posts
  * [x] Remove time to read
  * [x] Show all categories
  * [ ] Remove dangling categories
* [x] Remove all tags from posts
* [x] Remove post_id?
  * https://gohugobrasil.netlify.app/content-management/front-matter/
* [x] Fix character encoding issues from posts
* [x] Move images to final destination and change image links (see if Claude can move them into folders for each post)
* [x] Remove the _edit_last, parent_post_id and _wpas_done_all fields
* [x] Check for other superfluous fields to be removed
* [x] Download static.flickr images and put them into the bundles
* [x] Fix footnotes that are of the (()) format

* [x] More charset issues
  * http://localhost:1313/blog/my-year-in-cities-2008/
  * http://localhost:1313/blog/jurriaan-van-stigt-arcam-lecture/
  * http://localhost:1313/blog/encounter-zone-maasenstrase/
  * http://localhost:1313/blog/het-manifest-van-terschelling/
* [x] Recategorize posts
  * [x] Japanese
  * [x] Fix: æ—¥æœ¬èªž
  * Tag publicity: http://localhost:1313/blog/week-323/
* [x] Turn Kumano Kodo posts into a series: https://blowfish.page/docs/series/
* [ ] Fix internal links to: /dingen/2008/06/
* [ ] Pull this and other talks under publicity [“Designing in the Face of Defeat”](http://monsterswell.com/blog/2012/05/designing-in-the-face-of-defeat/)

* [x] What happened with the image in this post? http://localhost:1313/blog/17632/
* [x] More encoding issues: (15ź centigrade), taquerÃ­as, 30-35Ëš C., mÃ­jn

* [ ] Backport old blog content into markdown
  * [x] Check and fix content for tech
  * [x] Check and fix content for studies
  * [ ] Check and fix content for personal
    * [x] 1-100
    * [x] 101-200
    * [x] 201-300
    * [x] 301-400
    * [x] 401-500
    * [x] 501-600
    * [ ] 601-700
    * [ ] 701-800
    * [ ] 801-830
  * [ ] Check all internal links in the blog and fix them
  * [ ] Re-include all flickr images (and their weird links)
* [ ] Get rid of all GIFs
* [ ] Redirect RSS of old blog to new RSS location
* [ ] Create impressum page?
* [ ] Get rid of comments
* [x] Delete CloudFlare pages project
* [ ] Use [Netlify](https://docs.netlify.com/manage/domains/get-started-with-domains/#domain-setup-options) static files hosting?
* [ ] Clean up config
* [ ] Create automatic deploy on Github push
* [ ] Write a script to create a new post
* [ ] Ask Claude to spell check all my writing on the blog

* [x] Archive old blog to dingen.alper.nl
* [x] [Change URL setting of old blog in the database](https://www.hostinger.com/tutorials/how-to-change-wordpress-urls-in-mysql-database?utm_campaign=Generic-Tutorials-DSA-t1%7CNT:Se%7CLang:EN%7CLO:DE&utm_medium=ppc&gad_source=1&gad_campaignid=16184995375&gbraid=0AAAAADMy-hZkuW3COPeD_MOdnnSqsweXh&gclid=Cj0KCQiA6sjKBhCSARIsAJvYcpPJVfBHlD_bfkvswdtf_qCu02iEIqUdzZapPPCCuaKS--0129YUEzEaAgKNEALw_wcB)

* [ ] Fix mp3s and other assets that didn't make it over
  Broken links (files don't exist):

  These references remain but point to non-existent files:
  1. /posts/playing-with-public-transportation-data/ → traveltimes.json (missing)
  2. /posts/dutch-public-broadcasting-goes-fake-news/ → ongelofelijke-mensenmassa.mp4 (missing, 2 references)
  3. /posts/fragment-tegengif-87-over-ozb/ → tegengif_ozb.mov (missing)


## Manual Deployment

* hugo --cleanDestinationDir --minify
* rsync -avzP /Users/alpercugun/Documents/projects/wordpress/site/public/ vimexx:/home/u88479p83432/domains/alper.nl/public_html

## Write a post

* hugo new content/posts/18731/index.md