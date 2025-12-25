---
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
  - strategy
date: "2024-07-20T08:27:01+00:00"
guid: https://alper.nl/dingen/?p=17554
parent_post_id: null
post_id: "17554"
title: ""
aliases:
  - /dingen/2024/07/17554/

---
That popular open source package managers will at some point all get owned is so inevitable that it's hardly worth mentioning.

Cocoapods in this case is a bit of an outlier because the entire setup here has been so broken to begin with. iOS development never really allowed for dependency management so Cocoapods did it in an very hacky way and it was written in Ruby, a relatively niche end-of-life language that would have no chance to be blessed by Apple and shouldn't be used for anything serious to begin with. (Don't even get me started on Carthage.)

Swift Package Manager has been released years ago but lots of projects of course never manage to switch. I believe the best thing a project can do in such a situation is to terminate itself for the greater good.

[https://www.theregister.com/2024/07/02/cocoapods\_vulns\_supply\_chain\_potential/](https://www.theregister.com/2024/07/02/cocoapods_vulns_supply_chain_potential/)
