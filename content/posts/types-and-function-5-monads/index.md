---
_wp_old_date: "2019-11-26"
_wpas_done_all: "1"
author: alper
categories:
  - english
date: "2019-11-27T12:23:46+00:00"
guid: http://alper.nl/dingen/?p=15865
parent_post_id: null
post_id: "15865"
title: 'Types and Function 5: Monads'
aliases:
  - /dingen/2019/11/types-and-function-5-monads/

---
I'm looking forward to this chapter. When they taught us Haskell as an undergrad they made sure to stop well short of Monads. At the time I was happy about that but by now I wish we had pushed on.

> Monads are pointed functors that can flatten

I get this definition by now but it is exactly the kind of stuff that I wasn't going for. But maybe an ELI5 introduction to functional programming is too much to ask for?

> Mind you, we have not thrown out purity, but merely removed one layer of excess shrink wrap.

What is good here is that this tutorial does not gloss over this necessity with a bunch of jargon but in excruciating detail builds up the explanation.

> If you've read about monads previously, you might have seen `chain` called `>>=` (pronounced bind) or `flatMap` which are all aliases for the same concept.

This ridiculous aliasing into tons of different names in large part explains my confusion. Chain, bind and flatMap ar all the same thing.

One question that I'm left with then is how much of this do you need to be able to use functional programming at an application level and how much do you need to be able to write functional libraries yourself.

The exercises in this chapter are hopeless. The tiny IDE does not help at all and it feels like the only way to do them is to poke at it with `map` and `chain` until it sticks. That may very well be the essence of functional programming for all I know.

Again, the thing is that I know what I want to do and that it theoretically should fit together but the various functions feel like broken legos. If they were physical legos with affordances, things would be a lot easier.
