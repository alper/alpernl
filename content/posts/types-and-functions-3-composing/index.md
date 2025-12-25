---
author: alper
categories:
  - english
  - software-engineering
date: "2019-11-25T21:23:05+00:00"
guid: http://alper.nl/dingen/?p=15857
parent_post_id: null
post_id: "15857"
title: 'Types and Functions 3: Composing'
aliases:
  - /dingen/2019/11/types-and-functions-3-composing/

---
Then we get at [Chapter 05: Composing](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch05.html) and I really don't understand the need to faff around so much when it comes to such a mathematically simple subject.

Composing is really easy, it's just that programming languages make it hard. Especially if you look at this:

`const compose = (...fns) => (...args) => fns.reduceRight((res, fn) => [fn.call(null, ...res)], args)[0]; `

That curried function is left unexplained and I'm still not sure I can read it.

I'm documenting this because every chapter is spawning off one too many bunny trails for my taste. That also makes it clear how learning functional programming is a reclusive undergrad's game.
