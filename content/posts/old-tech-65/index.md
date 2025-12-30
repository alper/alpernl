---
title: "Eclipse 3.2"
date: 2005-12-13T11:44:00
author: alper
categories:
  - english
  - software-engineering
---

I am running on a new Eclipse 3.2.0 in the shop right now. It's pretty nice with some cosmetic tweaks and it feels a bit faster.

Most noticeably it has a Memory Monitor in the bottom with a button to force GC. I like the indication but I am opposed against the GC button.

![Eclipse Memory Monitor](http://static.flickr.com/34/73136781_a1fdb88d8f_o.jpg)[](http://www.flickr.com/photos/alper/73136781/)

It was always common practice to teach Java programmers that calls to [System.gc()](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/System.html#gc()) are harmful. The system usually is the better judge when it is necessary to collect. Programmers calling gc() can never really know if it is necessary and end up harming performance.

Two problems:

- If a programmer of an application cannot even be the judge of when to call gc(), how can a user know when to call it? It is pretty ridiculous exposing a call like this to the GUI.

And the usability is zero. Pressing the button completely freezes the system (as expected) and ends up with some more free memory. If you needed that free memory, the system would already have collected the garbage for you.

- More subtly, the message sent by exposing this button to a programmer who is building his own Java application in Eclipse is that it is ok to call gc(). This is a bad message promoting bad programmer practices spreading gc calls throughout Java applications because Eclipse says it is all right.

Thoughts?

Maybe it is not completely evil. Right clicking on it reveals some memory profiling options which might be handy if you're into that sort of thing.

IDEs should promote [good programmer practices](http://arguscodewatch.sourceforge.net/).