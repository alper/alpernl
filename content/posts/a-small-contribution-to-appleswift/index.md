---
author: alper
categories:
  - english
  - software-engineering
date: "2017-11-23T22:00:51+00:00"
title: A small contribution to apple/swift
aliases:
  - /dingen/2017/11/a-small-contribution-to-appleswift/

---
I saw a starter task fly by in the Swift Weekly Brief and jumped on it. Now it turns out that the Swift project has a util directory full of various [Python](https://www.python.org/) scripts that perform various tasks including cloning and building the project.

One of those python scripts needed to print out a message if somebody calls it without the --clone parameter. If you don't do that, it doesn't clone all the repositories that you need to be able to build the project. I did some path fiddling and testing against a sample of directories that should be present and there is [PR #12856](https://github.com/apple/swift/pull/12856/) that got merged into the project (and got mentioned in [the next Brief](https://swiftweekly.github.io/issue-95/)).

I had to run the thing by the people who have testing/merging privileges a couple of times mostly because of how stringent Python linting is these days. Writing code that adheres to [PEP8](https://www.python.org/dev/peps/pep-0008/) is no joke but I'm glad that people have set such a high standard for themselves and the community. I got commit access to [another project](https://github.com/reubano/csv2ofx) [^1] and figured out how to run the linter there until it was happy with the code on my machine.

There is also lots to do even just in the python part of the Swift codebase without me even having to dive into C++. I also have 15+ years of python experience to draw from vs. two months or so of C++. I've been looking around for some other python starter tasks to contribute some more stuff but still have to find the time to do them. Whether I'll get around to ever contribute to the core project is still open, but knowing how to build and run Swift is useful if I want to try out some of the interesting new proposals.

I'm very glad too that the Swift project itself has chosen for python as its scripting language. Too many iOS tools to my taste are written in ruby a language I have zero inclination to learn. I taught myself a bit to be able to get a plugin into fastlane, but that was more than enough. But it looks like we may be able to get rid of ruby in the future since more and more functionality of [fastlane](https://fastlane.tools/) is being rolled into Xcode and [cocoapods](http://cocoapods.org/) is being superseded by the [Swift Package Manager](https://swift.org/package-manager/). SPM especially is a project where there is still a lot of rather accessible work to be done which will yield huge improvements in the quality of life of lots of developers.

[^1]: Ask me how much fun it is to maintain a project to work on both Python 2.7 and 3.6.
