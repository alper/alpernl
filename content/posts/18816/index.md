---
date: '2026-02-21T12:07:32+01:00'
title: 'Going out of Rust'
author: "alper"
categories:
  - english
  - software-engineering
---
I kept hearing so many good things about Go that I decided to make the jump from Rust. I had Claude port my app and couldn’t be happier with the result.

## Background

I’ve been grinding on the [Cuppings](https://cuppin.gs) backend for years now in Rust/Axum after going through a lengthy process[^framework] to determine the libraries that would make up my à la carte framework. I settled on [Axum](https://docs.rs/axum/latest/axum/) with [SeaORM](https://www.sea-ql.org/SeaORM/) and [Askama](https://askama.rs/en/stable/). This works quite well and is blazingly fast, but from a developer experience point of view it’s always been somewhat miserable.

[^framework]: Mostly because there's a lot of Rust micro web frameworks with different positions on the async question. Why people don't just use Tokio is a different question altogether.

An important bit of context: Cuppings is a side project and I only get to work on it 1-2 times per month for a couple of hours if at all. Any time I spend on picking back up, upgrading things and waiting for compilation is time I cannot afford to waste.

I could have taken the easy way out and built this entire thing in [Django](https://www.djangoproject.com/). I used to be a professional Django developer so what takes me hours to figure out and setup here would literally take me minutes there.

But doing it the hard way and expanding my skills and horizon was the goal. I learned a lot and am now reasonably proficient in Rust, though there’s been a significant amount of self-castigation involved.

## Learning

The main issue with Rust is that even after reading many books and being more than interested in the topic, my lack of time prevents me from going hands-on with the lower level topics.

It took me a long time to understand what a [Box](https://doc.rust-lang.org/std/boxed/struct.Box.html) does because the learning materials assume you already know. I still couldn’t really tell you off the top of my head what a [RefCell](https://doc.rust-lang.org/std/cell/struct.RefCell.html) is for or why the whole [Pin](https://doc.rust-lang.org/std/pin/index.html) thing is such an issue.

It’s also because you don’t need most of that stuff. I write a very vanilla Rust like the kind [described by Steve Klabnik](https://lobste.rs/s/w1bsle/lobsters_interview_with_steveklabnik) here:
> I tend not to write macros at all. I also avoid fancy advanced type system tricks. Although Rust has the reputation of a complicated, big language, you don't have to use it that way.

But the problem is, however much you would like to ignore that Rust is a complicated language, it seeps through both in the technology and the culture. For me it always felt like Rust is for the initiated, even if it pretends not to be.

Language server support in Rust has always been flaky for me. When you ask around nobody can confirm it, which means either it does not happen to them or they find the current behaviour acceptable. There’s no real way to know.

When you use ORMs with lots of generated code and the macros many libraries insist you use, language server support becomes fictional depending on where in the reindexing of your project you are. I feel that typing code should not be so hit and miss.

After writing the code, you need to iterate and there the compile and link times are a deal breaker. Askama templates, for instance, look close enough to Django, but they break your flow because every time you save a template the entire app has to be rebuilt. Asking about this yields the response that it’s not enough of an issue to warrant fixing[^reloading].

[^reloading]: I’ve seen some hot reloading come out in Dioxus recently but who’ll adopt that if they don’t think it’s an issue?

Error handling is taken care of by [poorly documented](https://github.com/dtolnay/anyhow/pull/433) external libraries. It doesn’t matter whether people have ‘a choice’ here. If almost all articles, documentation, and people point to these libraries, they are the “official” way of handling errors. Making error handling an afterthought is a bit weird for a “safe programming language”. No wonder [people just call ￼￼`unwrap()`￼￼](https://blog.cloudflare.com/18-november-2025-outage/) in production code.

Basic framework features such as authentication, login protection of routes, and URL normalization are awkward in Axum. That stuff is non-negotiable and should work out of the box in a web framework. Axum takes inspiration from Django in broad strokes, but that does not translate to how it’s put together, documented, and works at the point of usage. Those are the things that really matter.

I’ll stop there. There have probably been more than enough posts (e.g. [Game dev in Rust](https://users.rust-lang.org/t/game-dev-in-rust-a-year-later/123522)) written about Rust like this.

Rust is great if you need its specific capabilities and guarantees. If you’re writing a low-level system that needs to expose an API server, Axum will get the job done blindingly fast.

My main issue is that people often insist Rust is a general purpose programming language. At the same time, a lot of basics are just not there[^esoteric]. But if you complain about those issues, people insist it’s your own fault for either being dumb or not having suffered as much as they have. It does not surprise me much but I still think it’s messed up.

[^esoteric]: They’ll tell you Rust is pretty much feature complete. So instead of fixing non-functional issues core language development is focused on increasingly esoteric features. That’s of course not limited to Rust. For instance in Python instead of fixing its packaging or async problems, they opted to put out an ill-fated walrus operator.

I want to thank the handful of people in discussions on the various forums who *didn’t* make me feel like I was insane. You know who you are.

## Go

I’ve written a bunch of Go in a previous job and quite enjoyed it back then[^ride]. I tried it out with Claude almost a year ago now, and even then it could generate non-trivial Go applications entirely hands off. It could also talk me through the configuration hell of setting up a Slackbot much better than Slack’s documentation ever could.

[^ride]: I get the argument in [I want off Mr. Golang's Wild Ride](https://fasterthanli.me/articles/i-want-off-mr-golangs-wild-ride). But there's a reason why Go is still more popular for writing high performance web services.

Now I asked Claude to port my Rust application to Go. It had no trouble doing that with minimal oversight. I haven’t written a single line of Go yet. I’m [brushing up](https://gobyexample.com/) mostly to be able to read it effectively and to continue the higher level design.

The opportunity to get out of ‘ORM hell’ was also great. It simplified the code to use Go’s stellar [sqlc](https://github.com/sqlc-dev/sqlc) plugin. I haven’t operated it myself yet, but the SQL it generates checks out. For the rest it’s just a router, a bunch of request handlers and some API calls. That part of a web app is the same across languages and frameworks. It’s all the other bits that matter.

Most noticeable is compiling the app in Go. A clean compile of my Axum project could take the better part of a minute and pull in hundreds of crates. The Go version pulls in almost nothing and builds in seconds. This makes the entire thing and process feel lighter.

## Python

Why wouldn’t I go back to my main programming language, Python?

The Go app I had Claude generate last year was multi-channel: web server and Slack bot in one. I had Claude port it to Python. It did a decent enough job with the logic, but as soon as it had to convert the networking it went down into a Python async rabbit hole from which it couldn’t get out.

Talking to people about this, they confirmed that there’s no obvious way forward here for anybody. One person even asked me: “Are you really sure you need async?” which tells you where the Python discourse is on this topic.

Deploying Python has become a lot easier thanks to `uvx`, but it’s still nice to have a single binary as output that you can ship.

And in raw performance, Python will probably never come close to a language like Go. For a small web app, performance is not a huge goal, but it’s always nice to have, if you can get it without paying too much in complexity.

## Conclusion

I can always go back to Rust when I have a project closer to the hardware with Rust level safety and performance requirements. But until then, for writing a small web app on the side, Go is more than good enough.

I think I can sum it up like this:

* Rust is a better C++
* Zig is a better C
* Go is a better Python

Don’t use a better C++ if your problem wasn’t C++ shaped[^shaped] to begin with.

[^shaped]: Though people use C++ very heavily in game engines and Rust does not seem to fit that use case very well.
