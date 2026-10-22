
The global cybersecurity disaster that consisted of yesterday's critical vulnerabilities in the PHP project is a good moment to talk about the natural life cycle of open source projects. In many cases it may be better to shut down projects instead of having them linger.

The PHP foundation's response yesterday looked inadequate and not well coordinated. The consortium of companies that participated in the release look like they were more interested in this as a marketing opportunity than as a serious incident. How and why the exploit was leaked days ahead of the remediation is something we'll likely see more on in the coming days. The fixes have been back ported to older versions of PHP (of which there are a near infinite amount on the internet) by a third party who filled in the gap left by the official PHP release cycle. The nature of the technology here and the outlay of the governance around it does not seem in any way suitable to the scale of the problem they have let loose on the world.

The nature of it is that PHP is a programming language which had a moment decades ago and that moment has long passed. That is the normal lifecycle. Perl is dead for all intents and purposes. Ruby has been past its moment for the better part of a decade and we should look for it to be effectively legacy soon as well. The only correct answer to yesterday's exploit as a professional software organisation is: “We don't run PHP.” Nobody should be deploying PHP on the internet anymore in this day and age. That there is still so much out there and that even privacy focused enterprise collaboration software such as [NextCloud](https://github.com/nextcloud/server) is being written in it is entirely inexcusable.

In any large C/C++ codebase like the [PHP](https://github.com/php/php-src) one, there's nothing that tells us that we won't have 10 more exploits of this scale coming out in the next years. We should consider every poorly maintained PHP property online to be toxic waste. Yes, that would include all of Wordpress.

The only way out is to either port the language itself to a memory safe language or to port your code off the language to something less exploitable. Both manoeuvres are practical enough these days that there's no excuse not to do it. Nobody is locked into anything anymore and it's hard to believe that writing PHP in particular is the thing that makes anybody happy. I have no stakes in it but probably if all these people would [just write Go](https://blainsmith.com/articles/just-fucking-use-go/), a lot of this could be avoided.

Open source maintainers often complain about their lack of resources to do the tasks they ‘need’ to do. Undoubtedly they are right, but since we only have so many resources to go around it's probably better to cut and focus rather than try to keep every project alive and secure. One answer to a lack of resources and recognition can be to just drop the work. Why would you keep this going while at the same time complaining about it? Is the complaining the goal?

We don't need that many interpreted web languages, we don't need half a dozen libraries doing the same thing. Sometimes the mature thing can be, even for a project that is very ‘successful’ (even if that success is by now mostly toxic) to consider the project finished, cut a final release and archive the repo.

---

Of course they need to pretend that Claude can generate anything and everything from first principles. Not giving attribution is one of the fundamental rules of marketing yourself.

https://sunshowers.io/posts/anthropic-mononoke-2/

---

https://inrng.com/2026/10/shimano-bicycle-museum/

---

https://underreacted.leaflet.pub/3mmevu6woys27
https://luma.com/fywlrw6y

---

https://skamille.medium.com/the-managers-path-in-the-age-of-ai-279cb6611d66

---

https://lobste.rs/s/htfm3p/pyinfra_agentless_infrastructure

---

https://www.scs.stanford.edu/14sp-cs240h/slides/

---

I love these posts where somebody with a high level of skill pushes nix to the very endpoint of what it means. Why couldn't an executable be a sqlite database? is a question some people will ask themselves. But only very few people will actually carry through with it.

https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database

---

Whatever you think about it, this is going to be aan influential article.

https://www.seangoedecke.com/weak-engineers/

---

"A computer can never be held accountable; therefore, a computer must never make a management decision."

Sam Altman can never be held accountable, therefore Sam Altman must never

https://prospect.org/2026/09/29/artificial-intelligence-agents-openai-microsoft-sam-altman-greg-brockman-ah-nice/

---

https://untranslatedjp.substack.com/p/japans-book-scene-is-quietly-moving

---

In my ongoing quest for the best tiling/scrolling window managers on macOS, a new entrant has arrived on the scene: “Nehir”. I didn't expect it but, it is quite functional and has a couple of ideas that I think others should steal.
+
+I reminded myself again that I like the idea of scrolling WMs more than I like using them, so I'm back on Aerospace.
+
+https://github.com/apphane-dev/nehir
+

---

Reconstituting rigor every time software engineering goes through a paradigm shift is a very smart move. Removal of constraints (or additional degrees of freedom if you will) is a systems theoretical move that affects the whole.

https://aicoding.leaflet.pub/3mbrvhyye4k2e

---

This is the stuff that should be in a PRD anyway but these kind of documents tend to accumulate cruft so you have to regularly cut everything away and focus on the essence.

https://marieclairedean.substack.com/p/got-no-time-for-prd

---

A goodbye note from Zarah whose diagnosis about the PEP German Left is entirely correct.

I don't see the issues she's talking about becoming better anywhere in the next ten years. Brace for a hard landing into crisis.

https://taz.de/Migrantisches-Leben-Warum-ich-Deutscland-nach-15-Jahren-verlasse/!6199140/

---
There's a failure mode now in engineers who've gone too deep on AI. Whenever there is a problem they say "AI can fix this" or "We can fix this with AI." There are a bunch of issues with this.

Anytime somebody says "We can" or "We should" that's a drop of ownership. "We" is not a specific person so it might as well be nobody.

This is an issue that did not have anything to do with AI but as seen above AI is a useful layer of indirection that pretends to be a person so people may believe the ownership fumble does not happen.

The next question would then be: "If AI can fix it, why hasn't AI done so then?" which of course has no answer because for AI to fix it, it would need sustained focus and push behind it to create a solution that would actually be fit for purpose and that's often not something that the person who says this wants to do.

Conviction collapse is a useful term in these situations:

And as a corollary, when AI fixes the issue, will AI also be on call for this or pay the Total Cost of Ownership for the solution? Of course not, AI will only do the fun and easy parts of solving the problem, the hard and unpleasant parts of solving it will still need to be carried by humans.

---

Microsoft's stewardship of Github has been disastrously bad which was to be expected. It's amazing that Github worked as well as it did for as long as it did under what is actively malicious management.

The many outages it is suffering are having a real effect

Gutting it and letting it die is the equivalent of burning one of the biggest libraries the world has ever seen.

https://lucumr.pocoo.org/2026/4/28/before-github/

https://mitchellh.com/writing/ghostty-leaving-github

---

Open Source is Art
The art versus design debate is timeless and not really worth rehashing. To summarize my take would be that art is done for intrinsic motivations while design responds to extrinsic ones. You make art mainly for yourself and your own desire for expression while things are designed to meet some external aim (even if it can be self-imposed).

With that in the back of my head I came to realize that open source software development is art.

Open source developers constantly repeat and lament that the software is delivered “as is” and that nobody who can derive any rights or entitlements from the software being out there in the world. That is because usually open source software is written to “scratch somebody’s own itch” which is more or less exactly the definition of art.

That means maybe software is art but only a certain type of software and not in the way that we may think.

---

RSS:

* https://ratfactor.com/
* https://lr0.org/diary/#23042026
* https://drewdevault.com
* https://www.scattered-thoughts.net/log
* https://www.toolofthought.com/posts
* https://lambdaland.org/posts/2025-10-03_reading_papers/
* https://drewdevault.com/blog/index.xml
* https://redmonk.com/sogrady/2026/09/16/new-new-kingmakers/
* https://fzakaria.com

---

Papers

https://eighty-twenty.org/files/Henderson%20-%201982%20-%20Purely%20Functional%20Operating%20Systems.pdf

https://cses.fi/book/book.pdf
https://www.eecg.toronto.edu/~jzhu/csc326/readings/iverson.pdf
https://www.foundationdb.org/files/QuiCK.pdf
