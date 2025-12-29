---
title: "Monkey Lives"
date: 2005-11-12T18:21:00
author: alper
categories:
  - english
---

High profile security vulnerabilities led to the Greasemonkey's disappearance some time ago. It appears that it is now back from the dead.

This [article by Mark Pilgrim](http://www.oreillynet.com/pub/a/network/2005/11/01/avoid-common-greasemonkey-pitfalls.html?page=1) lists the ways in which it was vulnerable and what they did to make it safe again. It comes down to mainly wrap everything Greasemonkey does in XPCNativeWrappers to get untampered access to page elemets. A disadvantage is that it makes Greasemonkey scripts even harder to write.

Must read for anybody interested in Javascript security.