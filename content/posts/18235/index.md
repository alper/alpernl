---
author: alper
categories:
  - english
  - software-engineering
date: "2025-05-27T06:00:25+00:00"
title: ""
aliases:
  - /dingen/2025/05/18235/

---
I fully agree with Paolo Scanferla here that very complex typing ("hyper-typing") is an impediment to get anything done but besides the technical aspects, here are some ratchets here that are very pernicious.

1. Creating very complex typing is hard to argue against ("But don't you see how this is safer?") and simplicity rarely wins in group programming environments. You're essentially arguing against somebody who's posturing as being very clever ("It's very easy and safe this way.").
1. Once you lose the initial argument and the complexity gets in, it's impossible to get out again. It will only expand in your code base and make everything it touches also overly complex. Getting this out is several orders of magnitude more work than getting it in and can only be done by (the very few) people who understand the entire thing. Those people have made an excellent manoeuvre for their own job security and against everybody else's productivity.
1. This kind of typing is not incidental. The very design of Typescript and its increasingly more and more complex type system is meant to enable this. Language features that are there will always be used and regularly misused. It's near impossible to guard against that. That's why I consider any language with an overly expressive type system to be suspect (and this is why Go is good). Liking Typescript is a code smell on the person.

[https://pscanf.com/s/341](https://pscanf.com/s/341)
