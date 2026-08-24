---
date: '2026-08-24T08:51:45+02:00'
title: ''
author: "alper"
categories:
  - english
  - software-engineering
---
> These look intimidating the first time you see them, but they are boilerplate.

And that's exactly the problem with Rust. You can know precisely what you want to do but you'll spend lots of time making this stuff line up and dealing with obtuse type checking complaints.

It really ruins what is an otherwise cool language.

> Under the hood, the async block is the compiler’s desugaring of an anonymous state machine that implements Future, and Box::pin boxes-and-pins that anonymous future so its concrete type disappears behind the dyn in type Future = Pin<Box<dyn Future<…>>>.

I've read stuff like this dozens of times and it does make sense at some point, but it's still aggravating. This is a good article and it does a decent job of explaining it all, but it's just "too much".

Most of this stuff by now is so well documented that it's relatively easy to have the LLM do this kind of work for you. And once everything is put together, it will run well and quickly.

https://loige.co/writing-middlewares-for-rust-lambda-functions/
