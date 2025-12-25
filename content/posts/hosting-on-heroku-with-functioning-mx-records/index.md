---
_edit_last: "2"
author: alper
categories:
  - english
  - internet
  - work
date: "2013-03-04T15:59:42+00:00"
guid: http://alper.nl/dingen/?p=4376
parent_post_id: null
post_id: "4376"
title: Hosting on Heroku with functioning MX records
aliases:
  - /dingen/2013/03/hosting-on-heroku-with-functioning-mx-records/

---
It seems to be not completely obvious how to host a website on [heroku](http://heroku.com) while at the same time also maintaining e-mail delivery. You would think that this is a very common situation and it would be well documented but unfortunately it is not.

We got a [DNSimple](http://dnsimple.com/) account because that's the way that heroku allows naked domains to function. DNSimple [sets up the ALIAS record](http://blog.dnsimple.com/zone-apex-naked-domain-alias-that-works/) for you rather easily, but what it doesn't do is warn you if you have both MX and CNAME records on something. What happens is that [the CNAME record always takes precedence](https://groups.google.com/d/msg/hosted-the-basics/bTa3_MUGe5o/dcyx_UCy4_IJ) as a redirect so your e-mails are then routed to proxy.heroku.com. Something that is undesirably and that DNSimple should warn against.

What turns out to be the best solution is to [set ALIAS records for both your apex domain](http://support.dnsimple.com/questions/32831-How-do-I-point-my-domain-apex-to-Heroku) and your subdomains (as proposed [here](http://stackoverflow.com/questions/14763601/do-i-need-to-add-both-naked-and-www-domain-to-my-heroku-app)). This way you don't need a CNAME record anymore that can interfere with other settings. Heroku in [their documentation](https://devcenter.heroku.com/articles/custom-domains#dns-setup) advise you to use a CNAME record, so I'm going to ask them if there are any problems with using an ALIAS for all web routing.

The other option would be to purchase another plan for [Zerigo](http://www.zerigo.com/) which seems to be [heroku's preferred solution](http://xtargets.com/2010/10/04/using-gmail-for-email-on-a-heroku-managed-domain/) for this issue right now. Again this is rather poorly documented and we would have liked to be informed about that before we chose for the DNSimple option.

**Update:** Heroku replied with the following.

> Great question. The ALIAS record, created by DNSimple, is basically a bunch of magic that does a combination of what CNAMEs and A Records do, but does it behind the scenes. You can read more about the ALIAS records here: http://blog.dnsimple.com/zone-apex-naked-domain-alias-that-works/
>
> That said, DNSimple would likely be better quipped to answer a question like this. I don't see any reason why you couldn't use ALIAS records in place of CNAMEs. There might be a slight difference in performance between the two, but I'm not certain enough about that to say for sure.

After which I asked [the same question over at DNSimple](http://blog.dnsimple.com/zone-apex-naked-domain-alias-that-works/#comment-518) on their blog. That comment is awaiting moderation and an answer but I'll post that here as soon as it appears.
