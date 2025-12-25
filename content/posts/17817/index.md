---
author: alper
categories:
  - english
  - software-engineering
date: "2024-12-27T00:16:08+00:00"
guid: https://alper.nl/dingen/?p=17817
parent_post_id: null
post_id: "17817"
title: ""
aliases:
  - /dingen/2024/12/17817/

---
> The low-latency user wants Bigtable’s request queues to be (almost always) empty so that the system can process each outstanding request immediately upon arrival. (Indeed, inefficient queuing is often a cause of high tail latency.) The user concerned with offline analysis is more interested in system throughput, so that user wants request queues to never be empty. To optimize for throughput, the Bigtable system should never need to idle while waiting for its next request.

This is also at the moment my abject suffering where we have lots of shared resources which need to stay available but can also be hammered by various parties.

Good to read that in this piece by Dan Slimmon: [The Latency/Throughput Tradeoff: Why Fast Services Are Slow And Vice Versa](https://blog.danslimmon.com/2019/02/26/the-latency-throughput-tradeoff-why-fast-services-are-slow-and-vice-versa/). I read the SRE book as well but that part did not register with me back then.
