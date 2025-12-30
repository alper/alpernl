---
title: "Next Step"
date: 2005-11-25T17:20:00
author: alper
categories:
  - english
  - software-engineering
  - video
---

Is anybody busy writing a simple MPEG decoder in Javascript? Would it be difficult to port the standard routines from mplayer?

I would envision a purely Javascript decoder which gets it data packets using successive `XmlHttpRequests`. It would then decode the data and render into a suitable pixel array (<canvas> or something).

In the current state of browsers the resulting implementation would be too slow to be workable, but it would be nice to already have it. Because if I predict right, browsers are going to become more important and faster in the future. Probably fast enough to make this feasible.