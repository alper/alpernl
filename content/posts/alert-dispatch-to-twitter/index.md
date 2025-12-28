---
author: alper
categories:
  - english
  - internet
  - product-design
date: "2009-04-09T14:12:27+00:00"
title: Alert Dispatch to Twitter
aliases:
  - /dingen/2009/04/alert-dispatch-to-twitter/

---
I did a small survey with [James](http://www.lifesized.net/) of publicly available government data to see what the obvious targets would be for an interesting mashup. It's an interesting but very limited landscape.

One set we found was the incident reports of Dutch first aid services which are published at [P2000](http://www.online-p2000.nl/) and parsed by the site [Alarmeringen.nl](http://www.alarmeringen.nl/) into nicely Google Mapped displays with RSS feeds and SMS alerts.

What it didn't have yet was a decent output to Twitter. So to prod things a bit I made twitter feeds for the four major cities in the Netherlands. Meet:

- [@al\_amsterdam](http://twitter.com/al_amsterdam) [@pk2amsterdam](http://twitter.com/p2kamsterdam) [^1]
- [@al\_haaglanden](http://twitter.com/al_haaglanden) [@p2khaaglanden](http://twitter.com/p2khaaglanden)
- [@al\_rijnmond](http://twitter.com/al_rijnmond) [@p2krotterdam](http://twitter.com/p2krotterdam)
- [@al\_utrecht](http://twitter.com/al_utrecht) [@p2kutrecht](http://twitter.com/p2kutrecht)

I think it's easiest to attribute the quote to [Matt Jones](http://magicalnihilism.wordpress.com/) who in [this presentation noted](http://www.slideshare.net/blackbeltjones/the-demonhaunted-world#53) that the best people on Twitter aren't in fact people. I agree but here the Tweets represent the aggregations of groups of people: the incident and its cause, somebody noticing it and dialing dispatch and finally the fire fighters, paramedics or policemen moving to the scene [^2].

It's interesting imagining what has happened and where, but I don't really see this feed changing people's behaviour.

Ideally we would achieve a greater granularity intersecting your location with the path of the dispatch, so when you see a police car whizz by, you'd get a tweet later telling you why it was dispatched and what the result was.

**Update:**
As Pascal points out [in his comment](/dingen/2009/04/alert-dispatch-to-twitter/#comment-8378), this data was not supposed to be public at all but is de facto public because of technical architecture decisions. It is clear that these services have not been thought out with an internet enabled world in mind.

Joris [points out](/dingen/2009/04/alert-dispatch-to-twitter/#comment-8381) a bit later that [Remco van Zuijlen](http://twitter.com/remco72) is piping these alerts straight from the air [into twitter feeds on his own site](http://p2000.zuijlen.eu/) [^3].

Given that I was more interested in this as a proof of concept than to make it a long lasting durable service anyway, I'll take down my twitter feeds after I've given its subscribees time to switch to Remco's accounts.

[^1]: This one unfortunately seems to have stalled a bit at the source. We'll see when it comes back up.
[^2]: James noted this could be interesting input for a Sim City style visualization.
[^3]: Which is a lot faster and more elegant than my Twitterfeed from some other guy's RSS.
