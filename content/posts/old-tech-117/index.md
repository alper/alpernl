---
title: "Plazes Widget First Version"
date: 2006-04-23T17:46:00
author: alper
categories:
  - english
  - software-engineering
---

After mucking around with Dashboard some more, I gave up last night. My widget worked fine in Safari but every time I installed my widget in Dashboard the widget would disappear. The fact that Dashboard does not give you any feedback does not really help in solving this problem.

Programming Dashboard is really really painful experience.

Today I took a widget which was doing something similar to what I wanted: the [GMaps Dashboard Widget](http://www.macupdate.com/info.php/id/18304) and tore that apart to see why it was working and my widget was not. I'm thinking it was either the sizes which were not correct or the AllowNetworkAccess directive from the plist file.

Using that as a starting point I could bootstrap my widget into existence and finally have a working prototype: [Download Plazes Maps Widget](http://alper.nl/ajax/widgets/Plazes%20Maps.wdgt.zip).

The dimensioning thing is still not really clear to me but that shouldn't be too difficult to figure out. I do not know in how far the dimensions specified in the plist file override any other dimension settings or how they interact.

The same goes for the confusing number of ways you can specify a background image for your widget.

It is functional and not much more than that. It could use at least some graphics that I haven't bothered with. Partly because I do not have any graphics editing software installed on my iBook and mostly because I'm not so good with graphics work.

So don't be confused with the strange icon and the horrible background, the functionality should be there. I'll try to arrange some polish for the next version.