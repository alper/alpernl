---
_edit_last: "2"
_oembed_0bc20bae1733332c279d5f40c0e10052: <blockquote class="twitter-tweet" width="550"><p lang="en" dir="ltr">TimBL&#39;s RDF temple priests still mad as hell about <a href="https://twitter.com/Hixie">@hixie</a> coming up with a better alternative to RDFa in a weekend <a href="http://t.co/jmvQbgxC">http://t.co/jmvQbgxC</a></p>&mdash; mattur (@mattur) <a href="https://twitter.com/mattur/status/272745213611622401">November 25, 2012</a></blockquote><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
_oembed_91ea3097d5898185db7c01c4e0a48c1b: '{{unknown}}'
_oembed_87434e204ae3c6d8a1be793e0a7e2d8f: '{{unknown}}'
_oembed_e56c9c19cae20c08ba017889e2cf8400: <blockquote class="twitter-tweet" width="500"><p>TimBL's RDF temple priests still mad as hell about @<a href="https://twitter.com/hixie">hixie</a> coming up with a better alternative to RDFa in a weekend <a href="http://t.co/jmvQbgxC" title="http://lists.w3.org/Archives/Public/public-html/2012Nov/0177.html">lists.w3.org/Archives/Publiâ€¦</a></p>&mdash; mattur (@mattur) <a href="https://twitter.com/mattur/status/272745213611622401" data-datetime="2012-11-25T16:55:00+00:00">November 25, 2012</a></blockquote><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
_oembed_time_0bc20bae1733332c279d5f40c0e10052: "1442444674"
_tweet-272745213611622401: ""
author: alper
categories:
  - english
  - monster-swell
  - work
date: "2012-12-07T23:21:59+00:00"
guid: http://alper.nl/dingen/?p=4030
parent_post_id: null
post_id: "4030"
tags:
  - weeknotes
title: 'Week 298: Berlin odds and ends, hackday'
aliases:
  - /dingen/2012/12/week-298-berlin-odds-and-ends-hackday/

---
Horribly late but here goes anyway. On Monday I briefly dropped by the Makers Loft and finally managed to see the [Third Wave](http://thirdwaveberlin.com/) crew again.

_Sake_ started up in earnest and team participation started to ramp up. Just now I piped the git commits into our communal chatroom, something I should have done a lot earlier because it so nicely shows the active heartbeat of a project.

I installed two applications I had been holding out on. I'm trying to backup my files to [Amazon Glacier](http://aws.amazon.com/glacier/) using [arq](http://www.haystacksoftware.com/arq/) but Berlin bandwidths are not very conducive to sending 192GB to the internet. Also I installed [Flux](http://stereopsis.com/flux/) to modulate my screen temperature into something a bit warmer for these cold winter days.

I think this bears sharing regularly:

https://twitter.com/mattur/status/272745213611622401

The rest of the week sake kept up. On Tuesday I picked up my visa from the Russian consulate for the trip to Moscow. I'm on the plane back to Berlin as I'm typing this.

Wednesday I had a coffee with [Niels van der Linden](http://dtdid.com/blog/about-me/), a Dutch national who's living in Istanbul and is active in the startup scene over there. Lots of interesting parallels and things to learn from each other in that one. We had a nice lunch with [Praxis](http://praxisberlin.net/) and then I went to the [Iron Blogger Berlin](http://ironbloggerberlin.com/) meetup.

[![Picked up a pack of these stickers](http://farm9.staticflickr.com/8200/8230237120_b426cc08fa.jpg)](http://www.flickr.com/photos/alper/8230237120/ "Picked up a pack of these stickers by illustir, on Flickr")

A sizable part of the week was spent finalizing paperwork both for my German bookkeeper and for various institutions back in the Netherlands. After making my rounds through the city I dropped by at the ÖPNV hackday [Apps and the City](http://appsandthecity.net/apps/) at Supermarkt.

[![Apps and the City hacking around](http://farm9.staticflickr.com/8339/8230492822_8d4c77543d.jpg)](http://www.flickr.com/photos/alper/8230492822/ "Apps and the City hacking around by illustir, on Flickr")

I couldn't hack as much as I wanted because I needed to send my slides to Moscow for the following week, but once I finished those I still managed to get two small things in:

Firstly I uploaded the sample file of [the various POIs for Berlin's S-Bahn stations](https://www.google.com/fusiontables/embedviz?viz=MAP&q=select+col7+from+1yHx-9xRpcVU5B4oboTfiSSR4y8so6cV1zAALoU0&h=false&lat=52.49216510989638&lng=13.370220703651414&z=17&t=1&l=col7&y=2&tmplt=3) to Google Fusion Tables to be able to get a quick feel for the data. What's in it, what's not and how accurate it is.

Sadly, there is a full dataset available with the points for all stations in Berlin, but that is geocoded in some obscure German datum and therefore cannot be readily loaded into Fusion Tables. Ready usability is key for many hackday datasets, even if other participants had more time to do a possible conversion than I did. For a data provider: you show knowledge of the outside world by supplying GPS.

The issue to be solved with this dataset would be: finding your ideal way around a station for a transfer or your ideal exit for your final destination and based on that information to chain back and guide you into the optimal carriage of the underground train.

The first approach, to brute force the problem by tabulating all possible entries and exits, turned out to quickly balloon into something horribly large. After some thinking I thought up a graph representation of a subway station and demonstrated with a proof of concept [“Stationsrouter”](http://appsandthecity.net/apps/app/stationsrouter.html) that you can route through that using the well-known A\* algorithm. ((Web developers many of which are self-taught and who are not regularly faced with problems that are not solvable using procedural programming and databases often have no idea how more difficult problems in the domain of computer science can be solved. Corollary: game development contains many many of these more difficult problems.))

This can be easily extended for for instance wheelchair access by using a weighted graph and setting the weights of stairs to infinity for those users. I [posted the algorithm and a rough graph coding online](https://gist.github.com/4172489), I need to find the time to make the interface more attractive (probably by porting it to Javascript) and to transcode a couple more stations. To figure out where an arriving train lands on a platform and therefore which graph segment that corresponds to wouldn't be too difficult.

[![There's a bride dancing in the middle of the street. #xberg](http://farm9.staticflickr.com/8061/8233087336_b873a5cf13.jpg)](http://www.flickr.com/photos/alper/8233087336/ "There's a bride dancing in the middle of the street. #xberg by illustir, on Flickr")

On Friday I was supposed to take an introductory German language course, but the hackday shenanigans made sure I missed that early appointment. Trying to reschedule something for the new year to level up my Deutsch. We did a capacity planning session with Hubbub and I ended the afternoon by watching a bit of [TEDxAmsterdam](http://www.tedxamsterdam.com/) waiting for the new talk by [Kevin Slavin](http://twitter.com/slavin_fpo).

On Sunday I met with Peter Bihr, Matt Patterson and Daniela Augenstein to talk about open government in Berlin and then the next day it was off to Moscow!
