---
author: alper
categories:
  - english
  - internet
  - monster-swell
  - work
date: "2010-04-04T12:30:05+00:00"
title: New disciplines for a real-time data world
aliases:
  - /dingen/2010/04/new-disciplines-for-a-real-time-data-world/

---
Some posts that had been sitting in my browser tabs for a while combined together in a brand new job guide for 2010. You can also read this as a follow-up post to my previous post on [Why developers are important](/dingen/2009/12/developers-are-so-important/), this is which developers are important. This post has been lying in my drafts folder for a while, but it has actually only become more relevant.

Some interesting jobs for the coming year(s):

### Scalability Engineer

These are already highly sought after ever since Twitter was [failwhaling](http://www.flickr.com/photos/factoryjoe/2631644440/) half of the time. Having the competency to keep a website running while it is experiencing massive growth is going to be highly sought after. Some technologies such as [Google App Engine](http://code.google.com/appengine/) promise to make this easy, but they introduce a set of problems of their own. Traditional relational databases are abandoned more and more for the looser often schemaless variety of [BigTable](http://labs.google.com/papers/bigtable.html)-like NOSQL databases that live in the cloud ( [CouchDB](http://couchdb.apache.org/), [HSQL](http://hsqldb.org/), [Cassandra](http://cassandra.apache.org/), [MongoDB](http://www.mongodb.org/display/DOCS/Home), [Tokyo Cabinet](http://1978th.net/tokyocabinet/) etc.) or can be scaled at will. If you want to get up to speed on this stuff really fast, there's a [NOSQL conference](http://nosqleu.com/) in London April 20-22nd.

Also knowing your [Scala](http://www.scala-lang.org/), [Tornado](http://www.tornadoweb.org/documentation), [Twisted](http://twistedmatrix.com/), [NodeJS](http://nodejs.org/) or other non-blocking framework is increasingly important, since we're slowly moving out of the request/single response paradigm for the web.

**Key skills:** Everything command line, functional programming, traditional database management, SQL, virtual machine configuration, [puppet](http://freshmeat.net/projects/puppet/)

### Client Side King

The web based client already was the biggest delivery mechanism for functionality and experience, but it is going to become more and more important. Functionality which you would not have thought possible in a web application, will become available. Some apps may at first be functionally inferior to their native versions, but the fact that they are web native and inherently social will draw people in. After a while either the apps will become more capable or the users won't care anymore.

Developments in [HTML5](http://dev.w3.org/html5/spec/Overview.html) bode well for those of us who would like to abolish slow and crashy plugins (yes, Flash). Audio, video, hardware accelerated 3D graphics and much more will soon be native to the web. Just look at [Quake II written in JavaScript](http://googlewebtoolkit.blogspot.com/2010/04/look-ma-no-plugin.html). There is still a place for adding Silverlight and Flash to certain sites, but the benefits of those technologies are much harder to argue for.

**Key skills:** JavaScript all variants, styles and frameworks; web-native UI design; marginal IE skills required (since you will not be building for that platform but you should know its limitations); iterative development; guerilla user testing

### Algorithm Cook

Ridiculous amounts of data requires strong analytics, very capable navigation and a new sort of editorial proces. These databases draw more and more information from the real world:

> “The advent of inexpensive high-bandwidth sensors is transforming every field from data-poor to data-rich,”Edward Lazowska, \[…\] said ( [NYT](http://www.nytimes.com/2009/12/15/science/15books.html?_r=1&sudsredirect=true)) and “Today,”he added, “you have real-time access to the social structuring and restructuring of 100 million [Facebook](http://topics.nytimes.com/top/news/business/companies/facebook_inc/index.html?inline=nyt-org "More articles about Facebook.") users.”((I don't know exactly who has that access, but…)) (same source)

Better algorithms will allow us to make better sense of all this data and will provide inputs for the other fields. Everything can have an interestingness in a given context for a given person.

**Key skills:** [multivariate statistics](http://en.wikipedia.org/wiki/Multivariate_statistics), data wrangling, screen scraping, machine learning, data mining, Excel, SPSS, R/SPlus, Matlab, [NumPy](http://numpy.scipy.org/), digital signal processing

### Visualization Artist

Making sense of all the information requires condensed views with aesthetic qualities. There is simply too much data out there for us to be able to grasp it, so being able to filter and mine the datasets with the help of the other disciplines is essential. But after that step any data needs to be refined, represented and made interactive.

> “Decode”ends with “Network,”which examines the interconnections of mobile technologies and the Internet. It also illustrates how digital imagery is helping us to make sense of a frenzied, often confusing world. ( [NYT](http://www.nytimes.com/2009/12/14/arts/design/14iht-design14.html))

There are tons of frameworks, tools and libraries in a variety of languages for anybody who wants to try out visualizing stuff. In the end no single one will fit the bill and the best result is achieved combining, mixing and writing something by yourself.

There's a new O'Reilly book coming out for anybody in the finer arts who's interested in getting their feet wet with [Processing](http://processing.org/): [“Processing for Visual Artists”](http://www.amazon.com/gp/product/059680721X?ie=UTF8&tag=alpercugun-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=059680721X) Then after a while you may be able to produce stuff such as: **Key skills:** aesthetic sense, 2D/3D graphics, cognitive psychology, Processing, OpenGL, JavaScript, SVG, design tools, Tufte

And we haven't even treated the _Natural Language Processer_, the _Urban Information Planner_ and the _Machine Vision Trainer_ yet but there's considerable overlap with the above disciplines. If you have any other that we should look at, please suggest them in the comments.

**Update:** And the New York Times is just looking for somebody with [roughly this description](https://careers.nytco.com/TAM/nyt_docs/TAM/Candidate.html?Page=HRS_CE_JOB_DTL&Action=A&JobOpeningId=1001338&SiteId=1&PostingSeq=1).
