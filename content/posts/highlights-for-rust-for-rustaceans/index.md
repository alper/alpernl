---
author: alper
categories:
  - english
  - reading
  - software-engineering
date: "2022-03-11T21:40:53+00:00"
title: Highlights for Rust for Rustaceans
aliases:
  - /dingen/2022/03/highlights-for-rust-for-rustaceans/

---
> For example, there cannot be two parallel flows with mutable access to a value. Nor can there be a flow that borrows a value while there is no flow that owns the value.

> Freeing the memory twice could have catastrophic consequences.

> If you just want to leave some valid value behind, std::mem::take 2 is a good candidate. It is equivalent to std::mem::replace(&mut value, Default::default()); it moves value out from behind the mutable reference but leaves a new, default value for the type in its place.

> but as we dive deeper into the more complex parts of Rust, you will need a more rigorous mental model to work with.

> The aim of this chapter has been to establish a solid, shared foundation that we can build on in the chapters to come.

> False sharing occurs when two different CPUs access different values that happen to share a cache line; while they can theoretically operate in parallel, they both end up contending to update the same single entry in the cache.

> Simply stated, the orphan rule says that you can implement a trait for a type only if the trait or the type is local to your crate.

> For example, consider a type like SshConnection, which may or may not have been authenticated yet. You could add a generic type argument to SshConnection and then create two marker types: Unauthenticated and Authenticated. When the user first connects, they get SshConnection. In its impl block, you provide only a single method: connect. The connect method returns a SshConnection, and it’s only in that impl block that you provide the remaining methods for running commands and such.

> you can see the building blocks in the RawWakerVTable type in the standard library.

> In a way, unsafe is misleading as a keyword when it is used to allow unsafe operations through unsafe {}; it’s not that the contained code is unsafe, it’s that the code is allowed to perform otherwise unsafe operations because in this particular context, those operations are safe.

> In practice, the safety and performance trade-off for unchecked methods is rarely worth it. As always with performance optimization, measure first, then optimize.

> and then document them rigorously.

> Not all code is written in Rust. It’s shocking, I know.

> Instead, as shown in Listing 3-2, we can introduce a generic parameter on Rocket, Stage, and use it to restrict what methods are available when.

> Rust Fuzz Book (https://rust-fuzz.github.io/book/)

> Rust Cookbook (https://rust-lang-nursery.github.io/rust-cookbook/), which suggests idiomatic so

> the Tokio project has published mini-redis (https://github.com/tokio-rs/mini-redis/), an incomplete but idiomatic implementation of a Redis client and server that’s extr

> Philipp Oppermann’s Writing an OS in Rust (https://os.phil-opp.com/) goes through the whole operating system stack in great detail while teaching you good Rust patterns in the process. I also highly recommend Amos’s collection of articles (https://fasterthanli.me/tags/rust/) if you want a wide sampling of interesting deep dives written in a conversational styl
