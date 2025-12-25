---
_edit_last: "2"
author: alper
categories:
  - english
  - internet
  - monster-swell
date: "2010-03-30T15:37:44+00:00"
guid: http://alper.nl/dingen/?p=333
parent_post_id: null
post_id: "333"
tags:
  - coworker.nl
  - coworking
  - freelance
  - geodata
  - google
  - google-map
  - map
  - noma
  - uncategorized
  - visualization
  - webworker
title: Coworker.nl — Map of coworking spots in the Netherlands
aliases:
  - /dingen/2008/08/coworkernl-—-map-of-coworking-spots-in-the-netherlands/

---
Some ideas start out small and then grow larger than you thought imaginable. [Coworker.nl](http://coworker.nl) is one such idea. This is a write up about how it came to be and how you can build your own.

As a wandering free agent, you end up in strange places and if you're stuck somewhere, it could be useful to get some work done in the neighborhood. I was not the only person with this problem and I couldn't find a good WiFi map either, so I thought we could start something up.

A conversation about coworking on Jaiku quickly turned into the idea to gather those locations onto a Google Map and see if we could make that work. So talking back and forth a bit, I made a custom Google Map and invited people to add their offices with drop-in coworking spaces on it. This took off a bit and we had a functioning coworking map of cool companies and startups in the Netherlands willing to host a nomadic worker. [Robert](http://53miles.com/) had the domain [coworker.nl](http://coworker.nl) lying around and he pasted the code for the map on that domain and [Coworker.nl](http://coworker.nl) was born.

After some time, other people also started to add coffee shops with WiFi with a coffee cup icon and a public utility was born.

[![Coworker.nl - Coworking spots in The Netherlands](http://farm4.static.flickr.com/3053/2720317281_11161cb6d1.jpg)](http://www.flickr.com/photos/alper/2720317281/ "Coworker.nl - Coworking spots in The Netherlands by illustir, on Flickr")

### Attention

A lot of people have seen the map by now (22'000 and counting) and I have never launched a project as small as this which got so much attention in so little time. Robert and myself didn't have any problems getting this featured in various publications and even in a [national newspaper](http://www.fd.nl). This says something about the immediate appeal of a simple geo-visual application and about the climate in which we launched this.

![coworking.pdf (1 page)](http://img.skitch.com/20080731-dhhuj672ita6yye2a6e7wuqbiq.preview.jpg)

Independent web workers are seen as the vanguard of the hot Dutch new economy. Small shops, people setting up office in lunchrooms and coffee shops are seen as a ‘new’ trend. These workers also are in need of more flexible office space solutions (of which there are precious few in the Netherlands). Our map provides a handy visualization of this trend, it exactly fits a niche and appeals to people.

### Values and Misconceptions

What differentiates this map from most other WiFi maps and other custom maps and geoapplications is its incredibly narrow focus based on a shared set of goals and values. The initial participants in the map all know on a near instinctive level what is meant by [coworking](http://en.wikipedia.org/wiki/Coworking). They understand the problem of needing a place to work and are willing to share their offices.

A lot of outsiders who find the map do not really get it and just a link to [the Coworking wiki](http://coworking.pbwiki.com/) is not nearly enough to explain the shared values and history this map is built upon. Some people think we are an exchange for short-term office space, others want to sell their office space on a per day basis to make an extra buck. All interesting tangential applications of this map, and it's nice that people are running with it, but we should stay true to the original goal.

### The Tools

We should be really thankful of Google for providing these powerful and easy to use tools like [Google Maps](http://maps.google.nl) which we can use to hack something together in literally no time at all. We could have built our own database and map editor etc. but that would have taken some days if not weeks and would have greatly reduced the appeal of a small project such as this.

The fact that we could paste some minimal code to Jaiku and invite people to edit the map made all te difference. One additional step which would help in the management would be to add some kind of versioning or backup facility so if somebody accidentily deletes the entire map, I could easily restore it to a previous version.

### The Data

The data is available as [a KML file](http://maps.google.nl/maps/ms?ie=UTF8&hl=nl&msa=0&output=nl&msid=104975379960972971875.00044ae5b28a85f0210d7) to anybody who wants it (feel free to take it, distributed backup is the best kind) and I think we're willing to publish it under a [Creative Commons Attribution-Share Alike](http://creativecommons.org/licenses/by-sa/3.0/) license but I would appreciate it if you let us know if you're going to build something.

### Build your own local

Because this is so simple to setup local versions have already been made ( [Coworking São Paulo](http://zappa.cc/cowork/) by [Michel Zappa](http://zappa.cc/)) by others but the vision is to eventually cover the entire world both with maps and locations one country at a time, so to get this started here's a small recipe how to set this up:

1. Create a custom [Google Map](http://maps.google.com)
1. Call out to your local scene on [Twitter](http://twitter.com/), [Jaiku](http://jaiku.com) and whatnot to ask if they're interested and if they have spaces they know.
1. Invite these people to edit your Google Map, be sure to allow them to invite others as well to help your map grow virally.
1. Get [a (short and memorable) domain](http://coworker.nl) and paste the embed iframe code of the Google Map onto the domain for better visibility. You can also copy [our CSS and JavaScript](view-source:http://coworker.nl/) for extra ease.
1. Let it grow. You don't have to go about it too agressively, in our case we built it to scratch our own itch. Any value others derive from it is a plus.

Once enough countries have their own map, we may be able to combine them all into one massive global coworking map, for those people hopping countries.

### Tangents

There is some stuff which this map is not really about but wich bears talking about anyway:

The fact that the map also houses coffee shops with WiFi and a place to sit may not really be about coworking, but these are spots where you can get some work done and they show that there was no high quality WiFi wap for webworkersin the Netherlands. I expect this is the same in other countries.

[![Working area](http://farm2.static.flickr.com/1263/548345381_88bfe67445.jpg)](http://www.flickr.com/photos/alper/548345381/ "Working area by illustir, on Flickr")

There are quite some commercial spots available with meeting rooms and desks which you can lease by the day or some other period. These are not exactly in the coworking spirit, but they do serve a need, so for now we have allowed these to be on the map as well.

As I already wrote there's a shortage of office space which you can lease flexibly. The map could be used to show policy makers and realtors in which regions of the Netherlands there's demand for flexible office solutions and in the future we may add a vetted exchange to the map to help freelancers and small companies such as ourselves to get suitable office space.

[![](http://farm3.static.flickr.com/2370/2440853766_e08cd965a6.jpg)](http://www.flickr.com/photos/tonz/2440853766/)

Most of the people on the map are either free agents, people working in small companies, startups or a combination of these. So that way the map also serves as a list of interesting companies and people in the Netherlands who are active in the web scene and who have an open attitude. I think that is also a valuable thing to have for a nascent scene such as ours.
