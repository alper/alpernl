---
_wpas_done_all: "1"
author: alper
categories:
  - english
  - software-engineering
date: "2025-01-04T17:47:46+00:00"
guid: https://alper.nl/dingen/?p=17867
parent_post_id: null
post_id: "17867"
title: ""
aliases:
  - /dingen/2025/01/17867/

---
The terminal I use daily (because it's the best really), fish, has been rewritten entirely in Rust, because it's nice and more fun: "For one, fish is a hobby project, and that means we want it to be fun for us. Nobody is being paid to work on fish, so we _need_ it to be fun. Being fun and interesting also attracts contributors."

I can testify to this because when most of the code was rewritten I checked it out, built it and poked around a bunch to see how it works. I don't think I would have done that or enjoyed doing it if it had been a C++ codebase. That was also when I was confronted with the fact that what makes a terminal really complicated is not the language in which it is programmed, but the underlying system that it is an interface to.

The story of the port and its success is legendary as far as these things go.

[https://fishshell.com/blog/rustport](https://fishshell.com/blog/rustport)
