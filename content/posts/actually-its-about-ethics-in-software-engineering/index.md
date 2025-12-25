---
author: alper
categories:
  - english
  - politics
date: "2015-11-11T22:27:00+00:00"
guid: http://alper.nl/dingen/?p=5329
parent_post_id: null
post_id: "5329"
title: Actually it's about ethics in software engineering
aliases:
  - /dingen/2015/10/actually-its-about-ethics-in-software-engineering/

---
This is an expanded transcription of a tweetstorm (based partially on [conversations with Peter](http://www.thewavingcat.com/2015/10/09/what-we-can-learn-from-vws-emission-scandal-for-iot/)) that starts at this Tweet about the Volkswagen emissions scandal but actually as we go along it will be clear that it is about ethics in software engineering. First the news that started it all.

**Volkswagen's US head Michael Horn [blamed his engineers during a testimony](http://www.latimes.com/business/autos/la-fi-hy-vw-hearing-20151009-story.html) about the emissions scandal.**

> 1/ Volkswagen's US head Michael Horn blamed his engineers during a testimony about the emissions scandal. [http://t.co/ZSbrT8UyLM](http://t.co/ZSbrT8UyLM)
>
> — Alper Çuğun (@alper) [October 9, 2015](https://twitter.com/alper/status/652516175339917312)

 **Does anybody believe a German multinational is agile enough for a couple of engineers to be able to ship a feature without oversight?** Because on the one side as people have commented if this were true that would leave huge questions open when it comes to their quality control and delivery process. On the other side if true it would be a refreshing level of agility in a German corporation. A car maker that uses the tagline ‘move fast and break things’ would certainly be a novelty.

I would be curious to see what the codebase of a modern car looks like but thanks to the [DMCA](https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act) that will probably never happen. Unless maybe if somebody dumps the VW code during the CCC this year?

**This isn't about car manufacturing or recruiting engineers, this is actually about ethics in software engineering.** How this will affect VW's chances of hiring the best engineers (“ [Volkswagen, and how not to describe your employees](http://redmonk.com/fryan/2015/10/09/volkswagen-and-how-not-to-describe-your-employees/)”) is one issue. They couldn't hire the best anyway but they will likely always be able to hire a fair level of talent. To write good code, having a clear vision and a stable process are more important than having a mythical 10x engineer on your team. The questions now are why this took so long to be discovered and what the consequences are for the various parties involved.

I will focus on the software engineers because I am one and because I think they will be underrepresented.

**Programmers could get away not caring about ethics when it involved being callous with user data or new ways to serve banner ads.** The proliferation of [really weird privacy-invading ad tech](http://idlewords.com/talks/what_happens_next_will_amaze_you.htm) used to be considered a perfectly acceptable way for engineers to spend their time. Even the leak of sensitive user data like in the Ashley Madison hack was more or less business as usual among digital companies. Software companies being liable for their errors and engineers engaging in ethical behaviour were considered optional.

**Not anymore. You probably wish you hadn't snoozed through that ethics class in university. Not that that would have helped that much.** Unlike many others, in university we got courses in both ethics and in the history of science and technology. Courses which at the time were much maligned by my fellow students for their lack of practical application. They were right that that course wouldn't have helped you much by itself, but some basic level of understanding on this subject is nice to have.

**Besides continuing to teach ethics, schools should teach engineers about rights and liability.** Those courses in ethics could be supplemented by a practical course about your rights and liabilities when you are working at somebody else's company or at your own. It used to be that either nobody cared about this stuff or that the company would bear the consequences. Both of those notions seem fairly shaky right now.

**What do you do when your boss tells you to implement a feature, or very very strongly encourages you to reach a certain outcome?** What VW seems to be arguing is that nobody gave the order to build this specific feature but it arose from a rogue group of people. That seems just as unlikely as the case where this was mandated but VW management maintained the operational security required to keep it a secret. The investigation almost certainly will reveal that an order was given and who gave it.

In an ideal company a manager of course will not tell their people how to do their work. Your boss should give you an ‘Auftrag’ (assignment) to reach certain strategic goals and leave it to you to determine the best way of getting there. They will trust that you will operate to the best of your ‘Fingerspitzengefühl’ (working knowledge) within the framework that is the norm in the ‘Einheit’ (unity) that is the company. This all borrowed liberally from Chet Richards's excellent [Certain to Win](https://www.ethz.ch/content/dam/ethz/special-interest/mtec/chair-of-entrepreneurial-risks-dam/documents/Certain_to_Win_Boyd_conflict_manoeuver.pdf).

Even if an order was not given this points to an atmosphere in which exerting huge pressure is normal and where people consider it standard operating practice to cut corners maybe even without informing their superiors.

What recourse does a software engineer have in that situation? The current policy situation and broader environment suggest they have almost none.

**Who's responsible when that feature threatens the planet, evaporates shareholder value and leads to criminal investigations?** Now that software is a determinant in one of the biggest industries in the world, bad actions have large consequences. Selling millions of faulty cars and exposing many millions more to pollution finally gives us a software malfunction that everybody can relate to.

This isn't just the case for VW since other car companies are also implicated in fraud during emissions testing. It isn't even exclusive for car makers since the sequence of events leading up to the financial crash were nothing but a large number of model/software malfunctions.

In the case of the financial crash nobody got punished. The American enthusiasm to extract [punitive damages](https://en.wikipedia.org/wiki/Punitive_damages) from VW may be attributed to the fact that the U.S.A. finally is a relevant player in [(clean) car technology](http://www.teslamotors.com/) again.

Because these are the biggest industries in the world with immense resources and influence, normal or just rules of responsibility don't really apply.

**We need to answer these questions ourselves because if you ask the higher-ups it is clear who'll get thrown under the VW bus.** Software engineers can refuse to do work that they find ethically objectionable and find another job easily (the [Snowden](https://twitter.com/snowden) option). That is a luxurious position but it still remains to be seen how many actually do this.

What will likely happen is that the legal investigation will take forever and in the end some convenient people will take the fall. I think it's unlikely that that will create a just outcome or improve the overall situation.

The criteria to which these emissions tests were held were already watered down thanks to the lobbyists of various car companies who also set the tests so that it would be easy to cheat on them. The tests may be fixed a little bit ostentatiously because they are the most visible point of failure.

The actual problem will go unfixed. We can't independently verify the code that runs in cars now thanks to our broken copyright legislation. When cars become self-driving and dependent on remote services this will become infinitely harder. We are not be able to check software running in our devices to see whether it does what it promises to. That is the real problem and one I don't think that is going to be fixed anytime soon.

**Update:** So today the word got out that [some 30 managers at VW were involved](http://www.spiegel.de/wirtschaft/unternehmen/volkswagen-dutzende-manager-in-vw-skandal-verwickelt-a-1057741.html) in this. It looks like Michael Horn's statement about the rogue engineers was not true.
