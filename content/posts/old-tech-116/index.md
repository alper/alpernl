---
title: "Plazes Widget"
date: 2006-04-22T18:27:00
author: alper
categories:
  - english
---

After I had seen the innards of the [Tigergotchi widget](http://www.mekentosj.com/widgets/tigergotchi/index.html), it certainly didn't seem too difficult anymore to build a widget of my own.

It seemed like a good idea to make a [Plazes](http://www.plazes.com) widget listing the locations of your buddies and of people in your vicinity on your Dashboard or do something else nifty.

Plazes [recently added](http://blog.plazes.com/?p=100) an [API](http://beta.plazes.com/api/plazes/) to expose some of its functionality. The API is in XML-RPC which is quite ok, but my preference would have been to have a RESTful API optionally returning JSON for easiest access and use.

Python has a very useful [xmlrpc library](http://docs.python.org/lib/module-xmlrpclib.html) to prototype the functionality and call some methods. The [API docs](http://beta.plazes.com/api/plazes/doc) are down currently and the API does work but I have had some trouble getting my current plaze from the API.

My best bet is to get my traze with user.trazes and the most recent plaze from my traze (I'm getting a bit fed up with the z's) will be my current plaze.