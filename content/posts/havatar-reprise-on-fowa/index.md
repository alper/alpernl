---
_edit_last: "2"
author: alper
categories:
  - english
  - internet
date: "2008-10-12T18:33:28+00:00"
guid: http://alper.nl/dingen/?p=554
parent_post_id: null
post_id: "554"
title: hAvatar reprise on FOWA
aliases:
  - /dingen/2008/10/havatar-reprise-on-fowa/

---
Funny to hear from Cristiano that [David Recordon](http://twitter.com/daveman692) just flashed [Four Starters](http://fourstarters.com/) on stage (slide 37 of [this presentation](http://www.slideshare.net/daveman692/blowing-up-social-networks-by-going-open-presentation/)) on FOWA in London to demo the concept of [hAvatar](http://fourstarters.com/2008/01/20/havatar-wordpress-plugin/), a Wordpress plugin I developed about half a year ago. And a strange bit of anti-serendipity this stuff happening in London while I'm in SF.

The concept of the plugin is very simple. There are a ton of avatar standards out there the most widely used of whom is gravatar. Gravatar uses an e-mail hash and was acquired by Wordpress. There are some others which rely on a <link> in the head of the page or some other convoluted agreed upon standard.

hAvatar does it by following somebody's profile URL that they leave at a comment and seeing if there's an hCard on that URL. If there is an hCard there, hAvatar retrieves the linked image representation and displays that. The approach is decentral and uses existing standards and conventions so I thought it interesting enough to build. If there's interest I can check out the source code and make it run on the latest Wordpress and see if there are any bugs that need fixing.

Interesting talk about blowing up the social network and there's even more possible than what he's describing, seeing as hAvatar is half a year old. The stuff [Open-CI](http://www.viddler.com/explore/illustir/videos/1/) can do with remote profiles and avatars is further along but still rather poorly documented. And I'm missing a big part of the stack which is necessary for notification (mostly XMPP).

P.S. [Four Starters](http://fourstarters.com/) is unofficially defunct. Most of our attentions have slipped back to our personal weblogs. We're looking for a good way to preserve the content there and save it from the spammers.
