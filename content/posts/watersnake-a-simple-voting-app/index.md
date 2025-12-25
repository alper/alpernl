---
author: alper
categories:
  - english
  - internet
  - open-state
  - politics
date: "2013-02-16T05:05:29+00:00"
guid: http://alper.nl/dingen/?p=4315
parent_post_id: null
post_id: "4315"
title: Watersnake, a simple voting app
aliases:
  - /dingen/2013/02/watersnake-a-simple-voting-app/

---
My small project during [Swhack](http://janl.github.com/swhack-berlin/) was to create a django version of a delegated voting system partially inspired by [Liquid Feedback](http://liquidfeedback.org/) and [the manyfold problems that system](http://wiki.piratenpartei.de/AG_Liquid_Feedback) has ((Among others: the atrocious user experience, the fact that it does not support anonymity, the impossibility of i18n.)). In particular that it is written on such an esoteric stack ((The core is a 4500 line pgsql file which is a solid way to deter outside involvement in a project.)) that it is near impossible to get running without root on a Linux machine and let's not even discuss the maintenance. What is even worse is that it makes it nearly impossible for outsiders to join the project and contribute to it significantly.

In [this interview about Liquid Democracy](http://www.zeit.de/digital/internet/2013-02/liquid-democracy-nitsche/komplettansicht) you can read quite clearly how the technical mandate drives the direction of the project. Something that may not be very desirable if you think of it as a democracy-centric issue and not a technology-centric one.

So to see how hard it would be to write something similar in vanilla [django](https://www.djangoproject.com/). It's easy to hate on django but you can find tons of people who can work on this in just about every major city, the framework and the documentation are mature and many parts of the framework can be called excellent ((I for instance can't really imagine using sqlalchemy over the django ORM.)).

I thought putting something together that at its core implements a delegated voting engine should be doable in an afternoon and it was. What took the most time was playing around with the settings of the testrunner which I hadn't really used before. So [the watersnake app in this project](https://github.com/alper/enhydris) does majority voting on single proposals with support for delegation ((We can build it out to support as complex a voting setup and algorithms as you would like, but I would be reluctant to do so without clear indications that it will be actually beneficial.)). To see it work you have to run the tests, but building this out into a full fledged (web) app that can be deployed to [heroku](http://heroku.com/) with a single command is technically trivial (and also time consuming).

This wasn't a stretch to implement right now because I'm also doing some other projects which border on collaborative writing/decision making/filtering. As always, technology is neither the problem or the solution, but certain technical systems grant different socio-technical affordances than others. I will probably not work on this unless there is a clear demand, but I thought it would be useful to debunk the idea that building such a system needs to be difficult or complex.
