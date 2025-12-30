---
title: "Django Rocks"
date: 2005-11-13T12:33:00
author: alper
categories:
  - english
  - software-engineering
---

I have been meaning to try out [Django](http://www.djangoproject.com/) (=Python on Rails) for a while now and yesterday I finally managed to do and complete [the tutorial](http://www.djangoproject.com/documentation/tutorial1/). I totally love it!

Getting an environment up and running was not a completely smooth experience. Development on the Mac is more difficult than it is on Debian. I wanted to have a full working environment on my iBook so I can play with Django when I am offline.

[Checking out Django](http://www.djangoproject.com/download/) and staying up to date is a cinch with [subclipse](http://subclipse.tigris.org/). You symlink a the trunk checkout into your python site-packages and you are set to go.

Then I wanted to spare myself the installation of mysql or postgresql so I opted to run it on [sqlite3](http://sqlite.org/). A solid file based database which you get with OS X. But to use that I needed to [build pysqlite](http://initd.org/pub/software/pysqlite/doc/install-source.html), because they do not have OS X packages.

I could find some pre-built packages lying around on the internet but they were massively outdated (as were the packages in darwinports).

Building pysqlite is very easy —distutils takes care of that — but it does require a C compiler environment present. That is something you do not get out of the box with OS X. So I was off to the Apple developer site, getting an account there and downloading an 800MB (!) [Xcode](http://developer.apple.com/tools/xcode/index.html) package. From this package I think I installed over a gigabyte of stuff and then finally I could do:

`python setup.py build`

without errors. Django got along fine with the resulting pysqlite package.

Running Django is easier if you set the PYTHONPATH to appropriate values and export some environment variables. I was never good at that stuff, but I absolutely stink at it on OS X.

I worked around it by doing a

`sys.path.append('PATH')`

hack somewhere in Django code and I pass

`--settings=alperdjango.settings`

to `django-admin.py` every time.

Compared to Debian, setting up development stuff and installing libraries is something of a disappointment on OS X. This is partly due to my lack of knowledeg about the system and its policies but not having apt-get is also a big part of it.