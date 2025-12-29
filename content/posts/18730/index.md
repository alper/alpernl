---
author: "alper"
categories:
  - internet
  - english
  - software-engineering
date: '2025-12-29T01:45:32+01:00'
title: ""
---
And with that we are over to a new blogging system. It's not exactly because blogging is still a thing, but I use this site as a personal content store providing backing for the things that I share. Having it under my control and [in markdown](https://gohugo.io) is useful.

## Reading Back

Reading back all those old posts and weeknotes I have here is super nice and reminds me:

1. Keeping a record of things is really valuable. Just write and trust that it will come in handy at some point.
2. I used to do so many things in a given week. Compared to what I'm doing now, my life was insanely eventful.
3. I was consistently (too) early on a lot of things. For instance: I read myself complaining about restaurants and food in Amsterdam, something which is mostly solved now.

## Reasons to Move

The main reasons why I'm moving away from Wordpress:

Poorly configured hosts have botched UTF-8 on MySQL for so many times now that the entire blog was riddled with weird encoding errors. I [tried a while back](/posts/17649) to get them out with custom SQL statements, but it turns out I wasn't successful. PHP/MySQL is losing adoption and the more people refuse to use it, the sooner it'll die.

Web2.0 seems to have been a mistake and is being rolled back entirely. The whole concept of having your own web property that other people can write to (leave comments and other things) has gone away. That means also there's no need for a dynamic website with database anymore.

Even the cheapest hosting is not that cheap anymore. I'm at [Vimexx](https://www.vimexx.nl/) and, because I didn't have an exit, in September I was forced to pay €102.44[^1] for a year of hosting. That money does not buy me anything other than poorly usable, super outdated admins and a base that won't run anything other than PHP shit apps. I'm keeping my stuff on there, since I already paid, but this time I won't be forced to renew.

Matt Mullenweg [has gone off the deep end](https://ma.tt/2024/12/inc-hit-piece/) as have many tech leaders during the Trump administration. I'll admit that this is minor but still worth mentioning.

## Hugo

Hugo is an interesting mix of popularity, openness and customizability. It's written in Go, so it's fast and the code is relatively nice to work with. They've gone through a bunch of re-architectures, so maybe by now they're stable.

Most importantly having everything in markdown makes it easier for me to control what's happening on the blog than having to deal with a slow database and bad editors.

Fixing the encoding errors was mostly a Claude assissted find and replace job over the entire body of files (see: [57e5c81](https://github.com/alper/alpernl/commit/57e5c811cf1f9ec4a9ccb066535283612248cdbf) and [93d9e2a](https://github.com/alper/alpernl/commit/93d9e2a7176b8c98e248762a2700156d3a34f42a)). And now I can be fairly sure that they won't come back because the connection to the database didn't have a magic parameter specified.

Also I'd like to see if I can add more content types here. I use Obsidian for Notes so that is its own vault of markdown files. I think it'd be interesting to see if I can add some of my old data exports and things like reviews on other sites here as their own data type. I've always wanted that but building and managing my own Django site for that seemed too much work.

[^1]: More than 100 euros! Vimexx claims they're still the cheapest but have been very regularly pushing "pricing adjustments". The prices they list on their website are without BTW.