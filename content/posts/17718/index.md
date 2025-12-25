---
author: alper
categories:
  - english
  - food
  - software-engineering
  - travel
date: "2024-11-20T08:28:52+00:00"
title: ""
aliases:
  - /dingen/2024/11/17718/

---
I painstakingly built a bespoke Rust web application to host the [Cuppings](https://cuppin.gs) venue data and to add Google place\_ids to almost 2000 Foursquare location. That's been done for a while now but now we have the announcement of Foursquare open sourcing their location dataset.

That has two direct consequences for me:

- I was going to scrub the Foursquare data out of the database as a clean-up but that's something I won't do for now. In fact, I may recode the venues so I have ids in both worlds.
- I was toying around with the idea of building a next generation Foursquare/Dopplr on top of [atproto](https://atproto.com) which is something that I think is a lot more feasible now.

[https://simonwillison.net/2024/Nov/20/foursquare-open-source-places/](https://simonwillison.net/2024/Nov/20/foursquare-open-source-places/#atom-everything)
