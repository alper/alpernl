---
_edit_last: "2"
author: alper
categories:
  - english
  - internet
  - monster-swell
  - work
date: "2009-06-24T23:21:25+00:00"
guid: http://alper.nl/dingen/?p=1083
parent_post_id: null
post_id: "1083"
title: Friendlier and more open government data
aliases:
  - /dingen/2009/06/friendlier-and-more-open-government-data/

---
_This is an English rewording of [a post in Dutch](/dingen/2009/06/overheidsgegevens-opener-en-vriendelijker/) earlier this week just in time for [this Reboot session](http://www.reboot.dk/page/21801/en)._

I've recently been involved with several government initiatives to make government data more accessible and to show what's possible if that data is publicly available. The premise is that if government data is open, developers and other third parties kan reuse that data and make useful stuff with it. Stuff that can for instance serve as inspiration for our Dutch [show us a better way](http://www.showusabetterway.co.uk/) contest: [Dat Zou Handig Zijn](http://www.datzouhandigzijn.nl).

Most recently we had a [Hack the Government](http://www.hackdeoverheid.nl) [devcamp/unconference](http://www.zylstra.org/blog/archives/2009/06/hack_the_govern.html) where people interested in this stuff could exchange ideas and build stuff.

[![Hack de Overheid](http://farm4.static.flickr.com/3638/3628560864_0401f32b22.jpg)](http://www.flickr.com/photos/silvertje/3628560864/ "Hack de Overheid by Anne Helmond, on Flickr")_photograph by [Anne Helmond](http://www.annehelmond.nl/)_

A while back I did [a project on widgets](/dingen/index.php?s=widgets) which was mostly a supply side initiative triggered by a listing of readily available data.

Simultaneously Ton and James did [a project on process recommendations](http://www.zylstra.org/blog/archives/2009/06/open_government_2.html) for the public sector when it comes to releasing their data. As a part of that project I helped them sift through the currently [available data sources](http://opendataoverheid.nl/3_Bronnen) from a technical point of view and to see which of those sources could be repackaged in an interesting and more user and developer friendly way.

That wasn't very easy. Dutch government does publish a ton of data online but usually in rather unaccessible formats and interfaces and without clear descriptions on what it is. We picked two data sources and we managed to realize two new websites based on that data: [Schoolvinder](http://www.schoolvinder.nl) (‘School finder’) and [Vervuilingsalarm](http://www.vervuilingsalarm.nl) (‘Pollution alert’).

### School finder

 [![](http://aardverschuiving.com/image/schoolvinder.png)](http://aardverschuiving.com/portfolio#schoolvinder)

A Dutch institution called the [CFI](http://www.cfi.nl) already has a store with a lot of data on schools. We used their search interface and output (which though ugly and slow was remarkably reusable) and rebranded that into a simplest possible school search engine which is easily understood by parents looking for schools in their area.

Besides that we also create a canonical URL for every school in the Netherlands so other parties can refer to that and we can build stuff on top of those school pages.

The first problem this fixes is that the website is poorly usable and worded almost exclusively in jargon. Employees from the ministry of education told us later that the CFI data is not meant to be used by the public but we think this is still a fix.

Secondly it fixes the fact that this information is quite hard to find and to refer to. Our search engine is easy and open and school data is republished at unique URLs using microformats.

We would have liked to link our school pages to some numerical data from another database of the CFI but that was too hard to realize within the alotted time. Even linking to that other site proved to be too hard because those webpages were shielded in a needlessly complex ASP.NET environment.

### Pollution alert

 [![](http://aardverschuiving.com/image/vervuilingsalarm-1.png)](http://aardverschuiving.com/portfolio#vervuilingsalarm) [Pollution alert](http://www.vervuilingsalarm.nl/) takes the predicted particulate values for a number of sensor stations and makes those accessible. I made a scraper to take the predicted data from the [RIVM](http://www.rivm.nl/) site and store it in Google App Engine. From our own store in Google App Engine, we show the geocoded stations, we push alerts out to [Pachube](http://www.pachube.com) and [Twitter](http://twitter.com), graph the data and provide an API. We believe there is a lot of latent interest in the general public for this kind of data but that usable presentation forms have not been forthcoming.

RIVM to their credit does publish most of their data online, but definitely not in the most accessible formats nor in ways that enable normal people to audit their living environment.

### Principles

The sites we built are very advanced prototypes which are completely functional and even highly scalable. During building we followed some principles which may be interesting to touch upon here.

### Friendly design

Both sites have a pleasant and friendly design created by [Buro Pony](http://www.buropony.nl/). This is important because people are more inclined to use sites that look nice and experience those sites as being more user friendly.

A nice design needs to be accompanied by clear and simple writing without jargon that connects with the way people think about the stuff you're describing.

Most websites can be improved massively by just implementing these two points.

### Playing well with others

Both websites also connect with a bunch of other sites that improve upon the concept. They've been built on [Google App Engine](http://code.google.com/appengine/) a system which is easy to develop for and which is readily scalable. Maps are retrieved from [Google Maps](http://maps.google.com), graphs are provided by [Google Charts](http://code.google.com/apis/chart/) and sensor data is pushed to [Pachube](http://www.pachube.com) and [Twitter](http://twitter.com).

The experience on the main site is just a part of the whole. The data needs to be accessible from and easily pushable to where it's needed most.

On the [Hack the Government](http://www.hackdeoverheid.nl) event somebody said something along these lines: ‘systems integration is difficult and complicated and if you're good at it, you can make a lot of money with it’. This is a well known Enterprise IT mantra but if there's one thing that the abundances of mashups proves, it's that integrating systems on the open web is everything but complex.

On the open web we have usable and developer friendly API standards with tooling (( [cURL](http://en.wikipedia.org/wiki/CURL) as the simplest example)), besides that we have proper standards for [identity](http://openid.net/) and [authentication](http://oauth.net/) ((And it's all open which means it can't be hijacked by one party and controlled or made needlessly complex.)).

If you don't dig yourself into a hole, it really doesn't have to be that difficult. And none of this is exactly new, this technology has been around for ages and it just builds on the strengths of the internet.

### Standards based

Both sites are completely standards based. As an experiment I wrote both in a conservative form of HTML5 (and [validated that](http://html5.validator.nu/)) partly out of curiosity to see how it would turn out and partly because I think that our current Dutch industry standard XHTML is a dead end.

Added to that I have sprinkled in some [microformats](http://microformats.org) in places where it was obvious to do so (e.g. school addresses). The notion that it takes significant extra time to add microformats to a project is absurd ((Client: “Yeah, you can do that when you have time to spare.”)) and these days [the advantages of adding](http://twitpic.com/84b7d?also=hReview-aggregate-in-Google-search-results) them keep piling up.

Yes, it takes some effort to learn to use standards and microformats properly, but once learned I think it actually takes more effort not to use them.

### Quickly

Finally, both sites have been built in a couple of days over the course of about a week and a half. We wanted to show that when we're talking about a quick project, it really can be quick and that building a non-trivial usable beautiful website does not need to cost a lot of time or money.

All of this **can** be improved. Let's get at it ((Or like [Chris](http://factoryjoe.com/blog/) says it: “This can all be made better. Ready? Begin.”)).
