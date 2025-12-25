---
_edit_last: "2"
author: alper
categories:
  - english
  - internet
  - work
date: "2009-05-02T22:37:14+00:00"
guid: http://alper.nl/dingen/?p=956
parent_post_id: null
post_id: "956"
title: Mobile Widget Camp
url: /dingen/2009/05/mobile-widget-camp/

---
In spite of the nice weather, I spent today at [Mobile Widget Devcamp](http://www.mobilewidgetcamp.nl/) in Pakhuis de Zwijger. Having done some projects on widgets recently, I was curious to see what the state of mobile widgets was.

[Vodafone](http://www.vodafone.com/) presented their app manager which will be rolled out to Vodafone mobile users. The app manager makes it easier to find and install widgets/apps to the mobile phone. Widgets can be submitted to the app manager in an App Store like proces and in due time —I think the word was come September ((Though it will be interesting to see how far Apple will have advanced the signposts by then.))— you can even charge money for your widget in a 70/30 split.

[![](http://farm4.static.flickr.com/3398/3496036077_83a186081b.jpg)](http://www.flickr.com/photos/silvertje/3496036077/)

[CC BY-NC-ND](http://creativecommons.org/licenses/by-nc-nd/2.0/) photo by [Anne Helmond](http://www.annehelmond.nl)

The mobile widgets by Vodafone are a [W3C standard](http://dev.w3.org/2006/waf/widgets/) and the app manager is an application which wraps the widget rendering components of the Opera browser into a user and developer friendly package. Opera has quite some experience in mobile rendering engines, widgets and web technology in general and it shows.

The afternoon was widget building workshops and a contest for which I built two widgets: [a pollen prediction widget](/ajax/widgetproject/opera/Hooikoorts.wgt) and a [Dutch government job search widget](/ajax/widgetproject/opera/WerkenBijDeOverheid.wgt) (if you run Opera, clicking those links will actually do something).

The documentation is a bit sparse (as are the APIs) and the environment is mostly unfamiliar but that probably will be fixed over time. I built and tested these on my desktop Opera browser. I don't have a mobile phone that runs these widgets, which is a problem.

Depending on your target audience you may or may not want to build for this platform. In any case if you have your data, APIs and design in order, it shouldn't be too difficult to build a basic widget.

I think you can find more detailed coverage, slides and maybe even streams of the day if you look around a bit. Here are some observations.

### Terminology

There is a lot of terminology confusion in this space: widsets, widgets, apps, gadgets and applications which can get pretty unclear here and there.

### Simple is not important

All the talk focused on how simple it is to get a simple widget running. It hardly ever is about the simple stuff, we can believe that that works. It's about the tools and documentation, the nooks and crannies and the 80% of effort necessary to nail that last 20% ((In many cases it's not even possible to do that.)). Every new platform, however simple it may be, adds another of that 80% of extra overhead.

### OpenSocial

There is a lot of overlap with OpenSocial and I find it hard to believe that it would not be possible (not to mention wise) to converge the two. Both specifications deal with rendering a bit of HTML in a tiny window with specific Javascript APIs, social APIs in the case of OpenSocial and device specific APIs in the case of mobile widgets. Added to that OpenSocial feels like it has [more momentum](http://wiki.opensocial.org/), a [solid implementation](http://incubator.apache.org/shindig/) and [better documentation](http://code.google.com/apis/opensocial/docs/index.html).

One difference here is that the widgets we ran today must be rendered by the Opera browser whereas an OpenSocial widget is processed on the server and the resulting HTML can be rendered by any standards compliant browser.

In any case more consolidation and convergence can only be a good thing, especially when the essential differences are so minor. I found [a brief reference to that possibility](http://zope.cetis.ac.uk/members/scott/blogview?entry=20071105151422) by a CETIS guy.

I also think it's curious that OpenSocial/iGoogle gadgets don't run in more places. Why isn't there an OpenSocial container for Vista and OS X desktop gadgets just to name one ((You may notice that [Netvibes](http://www.netvibes.com) offers the option to intall widgets to Desktop widget runtimes and Google does not.))?

### Promises, promises

Many of the presentations were promising a lot of things and the current SDK and capabilities we have been presented are just a taste of what is to come.

There currently aren't any APIs yet to access any mobile specific device features from your widget. These are ‘forthcoming’ somewhere but the process and timeframe in which these should be available were vague. Without these APIs the widgets you can make don't go much further than a twitter search or your daily fortune, with those APIs really serious things become possible (as does really serious abuse).

Vodafone positions this app manager framework as a platform to reach the vast masses who do not yet use the mobile internet and do not yet run applications on their mobile phones. To reach them a lot of components must be in the right place and the experience to get and run applications needs to be smooth as silk and even then it remains to be seen if it will work. This is a big promise with a huge potential payoff.

In that future being able to install and share widgets/applications across platforms with minimal effort will have serious consequences for the very notion of what a mobile app is. Just a web service with a bit of logic and access (control) to device hardware using uniform APIs?

As [Chipchase wrote](http://www.janchipchase.com/blog/archives/2009/04/1000000000-apps-pfft.html): “\[…\] the interesting trend to watch will be the mainstreaming of just-in-time discovery and consumption of highly focused and contextually useful applications.”

I can't wait to see if and how ((And how will Nokia's interests in widgets, lightweight applications, device APIs and their own webkit browser relate to these developments?)) we will get there.
