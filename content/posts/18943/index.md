---
date: '2026-10-23T13:09:40+02:00'
title: 'Software can be finished'
author: "alper"
categories:
  - english
  - software-engineering
  - strategy
  - internet
---
The global cybersecurity disaster that consisted of yesterday's [critical vulnerabilities in the PHP project](https://www.php2shell.com) is a good moment to talk about the natural life cycle of open source projects. There are cases where it may be better to shut things down.

The PHP foundation's response looked inadequate and not well coordinated. The exploit was leaked and the fix was neither expedited nor rolled out quickly. The consortium of companies that participated in the release were mostly interested in using this security incident as a marketing opportunity. The details of how the response was fumbled and how to improve it is something that will be discussed in the following days. PHP and other orgs have promised improvements to their governance and processes.

The fixes have been back ported to older versions of PHP by a third party who filled the gap left by the official PHP release cycle. Even then, for large parts of the internet the fix may never happen. The fundamental nature of PHP as a technology and the governance they can effect do not seem in any way suitable to the scale of the problem they have let loose on the world.

PHP's nature is that as a programming language it is bad. It had a moment and that moment passed decades ago. Software is subject to a lifecycle. Perl is dead for all intents and purposes. Ruby is well past its prime and should be considered legacy software sooner rather than later.

The only correct answer to yesterday's exploit as a professional software organisation is: “We don't run PHP.” Nobody should be deploying PHP on the internet in this day and age. That a privacy focused enterprise collaboration suite such as [NextCloud](https://github.com/nextcloud/server) is written in PHP is laughable.

Large C/C++ codebases like the [PHP](https://github.com/php/php-src) one are fundamentally unsecurable. There's nothing that tells us we won't see 10 more exploits of this scale coming out in the next years. Every poorly maintained online PHP property should be considered to be toxic waste. Yes, that includes all of [Wordpress](http://wordpress.org).

The only way out is to either port the language itself to a memory safe language or to port your code to something less exploitable. Both manoeuvres are practical enough these days that there's no excuse not to do it. Nobody is locked into anything anymore and it's hard to believe that writing PHP in particular is the thing that makes somebody's heart sing. I have no stakes in it but probably if all these people would [just write Go](https://blainsmith.com/articles/just-fucking-use-go/), a lot of this could have been avoided. I moved this blog off Wordpress to Hugo with some help from Claude and it has been a blessing.

Open source maintainers often complain about their lack of resources to do the tasks they ‘need’ to do. Undoubtedly they are right, but since we only have so many resources to go around it's probably better to cut and focus rather than try to keep every project alive and secure. One answer to a lack of resources and recognition can be to just drop the work. Why would you keep going while at the same time complaining about it? Most people who believe they can't be replaced are entirely wrong.

We don't need this many interpreted web languages. More generally we don't need half a dozen open source libraries doing the same thing. Sometimes the mature thing can be even for a project that is very ‘successful’—especially if that success is by now mostly toxic—to consider the project finished, cut a final release and archive the repos.
