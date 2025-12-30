---
title: "Google Calendar History Buffing"
date: 2006-05-18T00:19:00
author: alper
categories:
  - english
  - software-engineering
---

I was thinking along the line of calendars and events and such, among others after the [talk of Frank Mantek](/posts/old-tech-132) about the Google Data API on [XTECH](http://xtech.org) and I had the idea:

**Why don't we save and share historical data using Google Calendar and the GData API?**

You could create a [Google Calendar](http://www.google.com/calendar/) called ‘History’ and just put in historical events in it. Calendars can also be shared, so other people could subscribe to your *history* and get your historical event stream. Or you could make specific Calendar for a part of history, say Dutch history or history of the [VOC](http://en.wikipedia.org/wiki/Dutch_East_India_Company).

![Adding an event](http://static.flickr.com/48/148384574_8b0413b46d_m.jpg)[](http://www.flickr.com/photos/alper/148384574/)

**Snag** So I ran into a snag when I tried to enter the discovery of America ([October 12, 1492](http://en.wikipedia.org/wiki/1492)) in my calendar. Google Calendar does not accept year values smaller than 1901.

I have no idea why. [GregorianCalendar](http://java.sun.com/j2se/1.5.0/docs/api/java/util/GregorianCalendar.html) (which most Java applications use for their date handling) is proleptic, which means it should be good for any year you can think of.

**Workaround** The alternative is to get your historical data and input it into the current year. Wikipedia's date pages seem to be a good candidate for this eg. [the page for October 12th](http://en.wikipedia.org/wiki/October_12) lists all events, holidays, births and deaths on that day.

Those pages can be crawled and inserted wholesale into my Google Calendar using [its API](http://code.google.com/apis/gdata/calendar.html). For each item you could create one event in the year 2006 and set it to repeat yearly.

Voilà, complete historical birthday calendars for your iCal inclusion (as soon as I get around to writing the script).

That's a lot of event data. How are we going to browse that? I think we need different ways of representing calendars than we are doing right now. I'll blog some more about one such way (probably) later this week.