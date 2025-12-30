---
title: "COREMuck"
date: 2006-03-31T17:15:00
author: alper
categories:
  - english
  - software-engineering
  - internet
---

I'm getting increasingly frustrated with COREBlog the Zope based blogging software that runs this show.

This week an upgrade had de-installed the COREBlog Product from my [Zope](http://www.zope.org/) instance so my entire blog was broken. After some looking around a simple symlink fixed that problem. But now I find out that it is impossible to add comments to my posts. Trying yields:

> Zope Error

> Zope has encountered an error while publishing this resource.

> Error Type: KeyError

> Error Value:

> Troubleshooting Suggestions

> This resource may be trying to reference a nonexistent object or variable .

> The URL may be incorrect.

> The parameters passed to this resource may be incorrect.

> A resource that this resource relies on may be encountering an error.

> For more detailed information about the error, please refer to the HTML source for this page.

> If the error persists please contact the site maintainer. Thank you for your patience.

Zope Management Interface logs are useless and I am at work so I don't have shell access to the box (nice…). I can't investigate deeper here but I will try to fix this problem tonight or tomorrow.

COREBlog did its job reasonably well for the time that I have used it, but it has been increasingly lagging behind other mainstream blogging software and it is too niche for its own good.

A recent visit to [the COREBlog site](http://coreblog.org/) revealed to me that my version of COREBlog is being end-of-life'd in favor of a new version that runs on top of Plone. Though it is feature richer than my current version I am not prepared to add another point of failure and obscurity ([Plone](http://plone.org/)) to my already beleaguered setup. I would much sooner switch to [Wordpress 2](http://wordpress.org/) which is as mainstream as it gets and has a divine management interface.

**Update:** Comments are now fixed on all blogs. It seems that the new [1.2.4 version has an additional option](http://coreblog.org/news_items/news_20060215_1) to stop spam. The feature does not display a "Post Comment" button before you have previewed at least once. Because I am using a heavily modded skin without those adjustments some stuff was going wrong in the session and throwing a horrible error message.

I had debugged the error to line 536 from Entry.py and I was just about to tear the offending piece of code out when I thought it would be better to play well. So I added to adjustment from [the news message](http://coreblog.org/news_items/news_20060215_1) to my custom skin.

This means you have to at least Preview your comments once before you can post them and makes my blog slightly better protected against spammers.