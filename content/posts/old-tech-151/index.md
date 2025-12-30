---
title: "R project"
date: 2006-06-12T16:06:00
author: alper
categories:
  - english
  - software-engineering
---

From the [R Language Definition](http://stat.ethz.ch/R-manual/R-patched/doc/manual/R-lang.html#Debugging):

> Debugging code has always been a bit of an art.

This is them saying that they have long transcended the language's quirks and they feel newcomers should go through the same pain they did, so they can't be arsed to provide decent error messages and debugging facilities.

I've been trying to do some statistical analysis in [R](http://www.r-project.org) (try Googling that) today and the experience has been less than satisfactory. Strange language conventions (What's the difference between a frame, list, matrix, vector or array? And [the ways of indexing](http://stat.ethz.ch/R-manual/R-patched/doc/manual/R-lang.html#Indexing) them?), awkward and outdated syntax and standard library, some of the obtusest error messages known to man, too concise documentation, and a very steep learning curve.

I'm getting less and less convinced there is a need for stuck in the mud domain specific languages such as R, Splus, Matlab and the likes.

Python is much more consistent and easier to learn and your Python knowledge will also be applicable to other domains. Numeric provides a solid vector processing foundation on which most statistics operations can be built or imported from R.

**Update:** I see something like this exists: [R/SPlus - Python Interface](http://www.omegahat.org/RSPython/index.html) but this project does not seem mature enough for real use and the wrapper abstraction looks to be laid too thin on R.