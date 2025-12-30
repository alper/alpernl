---
title: "Blocking (or"
date: 2005-11-07T00:03:00
author: alper
categories:
  - english
  - internet
---

Annoying thing about a lot of stuff on OS X is that they block and block a lot. And too often they stay blocked and I have to kill the application.

Doing so many things well and failing at non-blocking I/O is a bit of a shame.

Some day-to-day examples.

- **Safari** — Certain stages of loading a page block the UI and tabs so you are stuck on that tab waiting. Usually these stages do not take too long but given a slow network and slow servers sometimes they do.

Another gripe is that when a page is done loading, in certain cases, its tab will get focus to indicate it is finished loading. This is not what tabs are for and I have closed GMail more than once because of this ‘feature’.

- **Dashboard** — Usually after sleeping or after a network outage (which tends to happen when you are mobile) all of the Dashboard Widgets will feel they need to rebalance themselves. This proces takes 5-10 seconds on a reasonably crowded Dashboard and makes it useless for looking up stuff on a whim.

- **Fire** — Network outages and other connect/disconnect events to networks will have Fire block the entire GUI. This means you cannot continue typing chat messages until Fire is done and well. This takes the *Instant* out of my Instant Messaging.

Fire will also happily show me error messages about failed network connections, probably thinking I give a damn. I do not. I can see perfectly well if a network is not connected. Just keep trying to connect (silently) at reasonable intervals.

- **Finder** — Connecting to SMB shares, or FTP servers or browsing networks will hang Finder indefinitely in some cases. I know this behaviour, I am used to it in Windows though Windows does it somewhat better.

Havin one of the most important pieces of software in the OS hang and crash on a regular basis is not cool.

I did not know that stuff could be too cool for Apple people. It seems that async-I/O is.