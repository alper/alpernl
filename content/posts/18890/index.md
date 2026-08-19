---
date: '2026-08-20T00:11:20+02:00'
title: ''
author: "alper"
categories:
  - english
  - software-engineering
---
I often joke that Kubernetes is nothing more than a Docker installation and a bunch of shell scripts interacting with each other. In fact, at the most basic level, if you don't have any knowledge, you could definitely build a very fragile cluster that way. It might even be fun!

But once you go about abstracting that and making it robust and turning it into a series of cascading and interlocking loops, you get the massive beast we all know and love.

Fatih here does a good job of explaining what goes into Kubernetes's inner functioning and that all those loops together can also be called ‘control theory’.

https://planetscale.com/blog/the-feedback-loops-behind-kubernetes
