---

> The SQLite team themselves suggest that SQLite is a better fopen(), and they meant it as a design goal, not a joke.

After using Postgres for everything, we can go one step further and use sqlite for everything.

https://joecode.com/2026-08-19-sqlite3/

---

A really clean update for Mastodond and a well communicated set of changes. Particularly mixing dms with normal posts was something that I think caused no small amount of grief so I'm glad they fixed that.

https://blog.joinmastodon.org/2026/08/5.0-laying-the-foundation/

---

> The exact words we choose when writing matter. I want any LLM I use to choose the very best, most precise words at every single decision point.

How can you in teh same sentence talk about e xact words when writing and talking about LLMs?

https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing

---

A very helpful guide how to combine jj which already provides native stacked changes with Github's new stacked PR functionality.

It's stunning mostly how a feature on Github that everybody has been waiting the better part of a decade for has come out and is so lacklustre.

https://alan.norbauer.com/articles/github-stacks-with-jujutsu/

---

I've been waiting for the rewrite to conclude and to be able to use Roc for a long time now. Gleam scratches most of the itches that Roc does but for some reason I'm looking forward to this more.

https://www.youtube.com/watch?v=a7qEOtkkDb8

---

A truly wild story of debugging a really obscure race condition in sqlite. Even the most reliable systems when pushed to their limits will run into these kind of weird edge cases.

https://tailscale.com/blog/sqlite-wal-reset-bug

---

The major inference providers are making their setups increasingly more proprietary and obfuscated removing user choice and portability.

https://earendil.com/posts/session-portability/

---

a lovely interview with Emily Wilson that reminds me i need to resd her translation and watch the movie adaptstion of The Odyssey

https://open.substack.com/pub/derekthompson/p/emily-wilsons-complicated-feelings

---

Shoehorning the public forge and open source into the same website where private professional software engineering takes place was a historic mistake. It would be good to cut these two very different things loose from each other and explore what really makes sense for either use case.

Open source is facing lots of challenges around trust, effort and financing at the moment fueleld in large part by the LLM boom in code. At the same time private software engineering is becoming faster and more industrial (also thanks to LLMs) with massive requirements in logic, gating and repository sizes.

https://nesbitt.io/2026/05/02/a-github-for-maintainers.html

---

> These look intimidating the first time you see them, but they are boilerplate.

And that's exactly the problem with Rust. You can know precisely what you want to do but you'll spend lots of time making this stuff line up and dealing with obtuse type checking complaints.

It really ruins what is an otherwise cool language.

> Under the hood, the async block is the compiler’s desugaring of an anonymous state machine that implements Future, and Box::pin boxes-and-pins that anonymous future so its concrete type disappears behind the dyn in type Future = Pin<Box<dyn Future<…>>>.

I've read stuff like this dozens of times and it does make sense at some point, but it remains aggravating. This is a good article and it does a decent job of explaining everything, but it's simply "too much".

Of course a lot of this annoyance is now so well documented that it's relatively easy to have the LLM do this kind of work for you while you can stay busy with the real problem. And once everything is put together, it will run well and quickly.

https://loige.co/writing-middlewares-for-rust-lambda-functions/

---

You can do lots of cool things with systemd, that is if you can fight your way through it's awful documentation.

https://blog.tjll.net/you-dont-love-systemd-timers-enough/

---

You may have seen that deleting lots of small files on your laptop can already be a very intense and slow process. Deleting lots of things in a database can require so much extra work and bookkeeping that it can be quite detrimental to the health of the system.

https://planetscale.com/blog/the-only-scalable-delete

---

This tallies with my intuition for why it's often more profitable to leave commercial properties vacant. The operating costs for an empty office are really not that high.

Two data points that are essential:

* Commercial real estate is a financial product much more than it is a building that humans use and its financing is structured in ways that are alien if you go by the residential properties you're used to.
* Commercial leases are long term (in the Netherlands often 5+5 years) which means that if you settle for a lower rent than you had planned for, that is locked in for half a decade or more which when you think about 20 year terms is already a quarter of its runtime.

This knowledge is especially useful in Berlin right now since we have empty commercial lots that were all built in the past 5-10 years flooding the market, all sitting empty as Berlin and the entire German economy goes into a slump. Adam Tooze said to have faith that the stimulus money is coming, which may be exactly what all these operators are doing right now.

This is also why it's hard to convert offices into housing. It's not so much about the architecture being unsuitable as it is about the financials not making sense anymore in that scenario.

https://www.freerange.city/p/why-do-commercial-spaces-sit-vacant

---

Interesting new problem in database design about how to do observability for LLM traces.

https://buttondown.com/jaffray/archive/smithdb/

---

Why would anybody pay attention to what a German court says about something digital? The country has no idea and is behind by decades.

Was the ruling delivered by fax machine?

https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/

---

https://x.com/mitchellh/status/2031776788532379996
https://the.scapegoat.dev/slowing-down-in-the-age-of-coding-agents/

---
There's a failure mode now in engineers who've gone too deep on AI. Whenever there is a problem they say "AI can fix this" or "We can fix this with AI." There are a bunch of issues with this.

Anytime somebody says "We can" or "We should" that's a drop of ownership. "We" is not a specific person so it might as well be nobody.

This is an issue that did not have anything to do with AI but as seen above AI is a useful layer of indirection that pretends to be a person so people may believe the ownership fumble does not happen.

The next question would then be: "If AI can fix it, why hasn't AI done so then?" which of course has no answer because for AI to fix it, it would need sustained focus and push behind it to create a solution that would actually be fit for purpose and that's often not something that the person who says this wants to do.

Conviction collapse is a useful term in these situations:

And as a corollary, when AI fixes the issue, will AI also be on call for this or pay the Total Cost of Ownership for the solution? Of course not, AI will only do the fun and easy parts of solving the problem, the hard and unpleasant parts of solving it will still need to be carried by humans.

---

> The candidates who stand out are the ones who understood the problem before they started designing the solution.

> The ability to incorporate new information fluidly, showing both conviction and flexibility, is one of the highest-signal moments in the entire loop.

nothing new here. do you mean they were scream for these things?

https://open.substack.com/pub/theskip/p/what-pm-hiring-managers-actually

---

> This sense of invulnerability has deep psychological ramifications. If everything is free and nothing matters, then the world and other people exist only to be acted upon, if they are acknowledged at all. This is different from classic narcissism, in which a grandiose but fragile self-image can mask deep insecurity. What I’m talking about is a self-definition in which the individual grows to the size of the universe, and the universe vanishes.

https://archive.ph/2026.04.21-180013/https://www.theatlantic.com/magazine/2026/05/billionaire-consequence-free-reality/686588/

---

Microsoft's stewardship of Github has been disastrously bad which was to be expected. It's amazing that Github worked as well as it did for as long as it did under what is actively malicious management.

The many outages it is suffering are having a real effect

Gutting it and letting it die is the equivalent of burning one of the biggest libraries the world has ever seen.

https://lucumr.pocoo.org/2026/4/28/before-github/

https://mitchellh.com/writing/ghostty-leaving-github

---

I can't agree more with this. Programming shouldn't be that complicated. Type systems are a plague that needs to be checked.

https://blainsmith.com/articles/just-fucking-use-go/

---

The state of AI security is such that you can't give a deployed LLM write access to any important endpoints.

I have a relatively high value Instagram username that I'm hanging onto for dear life. On the Meta side this is clearly not a priority, so I have a piece of my online identity that could disappear at any moment.

https://thecybersecguru.com/news/instagram-meta-ai-vulnerability-account-recovery-exploit/

---

Surfacing the extent of Meta's malicious practices around Instagram and other services and then getting damages back from them is great.

https://www.theguardian.com/media/2026/mar/25/jury-verdict-us-first-social-media-addiction-trial-meta-youtube

---

RSS:

* https://ratfactor.com/
* https://lr0.org/diary/#23042026
* https://drewdevault.com
* https://www.scattered-thoughts.net/log
* https://www.toolofthought.com/posts
* https://lambdaland.org/posts/2025-10-03_reading_papers/
