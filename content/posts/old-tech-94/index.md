---
title: "Filmhuis Lumen iCal"
date: 2006-03-01T10:21:00
author: alper
categories:
  - english
---

Every week I get a [mailing](http://www.filmhuis-lumen.nl/index.php?datum=2006-03-01&contentid=9) from [Filmhuis Lumen](http://www.filmhuis-lumen.nl/) —my favorite art house theatre— with their movie schedule in it. I was entering them into my [iCal](http://www.apple.com/macosx/features/ical/) as events when I got bored with the repetitivity and the obsolesence of the task.

So I decided to solve this problem once and for all. Voilà! my Filmhuis Lumen iCal Generator: [webcal://alper.nl/cgi-bin/lumen-ical.py](webcal://alper.nl/cgi-bin/lumen-ical.py)

(In iCal: Calendar -> Subscribe and enter the URL above.)

And the proof is in the screenshot below:

![iCal Lumen Calendar](http://static.flickr.com/50/106033695_6561a469c2_m.jpg)[](http://www.flickr.com/photos/alper/106033695/)

Apple's [iCalendar documentation](http://developer.apple.com/internet/appleapplications/icalendarfiles.html) is a bit sparse but they point you to [the iCalendar RFC](http://www.ietf.org/rfc/rfc2445.txt) which is supposed to say everything. Wikipedia also has a nice [writeup](http://en.wikipedia.org/wiki/ICalendar).

I'm not that big a fan of RFC's for implementing. Their layout is unusable and finding stuff is a pain.

Fortunately there is a pretty solid [Python library for iCalendar](http://codespeak.net/icalendar/) which you can feed your data and it will spit out a valid file.

Feel free to use it, any comments are welcome.