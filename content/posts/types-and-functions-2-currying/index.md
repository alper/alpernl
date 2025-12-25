---
author: alper
categories:
  - english
date: "2019-11-25T21:13:20+00:00"
title: 'Types and Functions 2: Currying'
aliases:
  - /dingen/2019/11/types-and-functions-2-currying/

---
It goes wrong fairly quickly when it comes to [Chapter 04: Currying](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch04.html). It is unclear why you would want to do this ((I suspect that that will be a recurring theme.)) and how the code really works.

An additional problem is that many function definitions after this are written in curried form, like so:

`// join :: String -> [String] -> String`

It would have been nice if it was mentioned how to read these. To be fair it is in a way in the same [Chapter 07](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch07.html#tales-from-the-cryptic) where I found the above signature: “Without fully understanding the details, you could always just view the last type as the return value.”

Digging through a bunch of mostly unhelpful documents, I figured out that you can take everything around the arrows as function arguments except for the last one.

So the join above is a function that takes a `String` and an `array of Strings` and returns a `String`.

**Addendum:** This also makes it easier to read [the Ramda type signatures](https://github.com/ramda/ramda/wiki/Type-Signatures).
