---
author: alper
categories:
  - english
  - software-engineering
  - work
date: "2025-06-05T22:03:50+00:00"
title: ""
aliases:
  - /dingen/2025/06/18243/

---
It's relevant to my interests to read how others have massively scaled the systems we use. Discord has a solid write-up here of how to deal with Elastic Search.

Which is all good and well, but I'm a bit sad that we have so much systems software written in Java which in some cases works well (Kafka, Spring) but in other cases is a bit of a slog (Elastic, Cassandra). There are Rust/C++ search stores out there which out of the box beat a Java solution 2-5x on speed and 1/10th on memory usage. Those are numbers that make a huge difference at scale.

[https://discord.com/blog/how-discord-indexes-trillions-of-messages](https://discord.com/blog/how-discord-indexes-trillions-of-messages)
