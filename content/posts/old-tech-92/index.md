---
title: "Two Heads Are Better Than One"
date: 2006-02-27T21:51:00
author: alper
categories:
  - english
---

Why does every operating system known to man have a decent facility to set up dual heads with mirroring and extending options and boxes representing the head and its position with respect to the other head.

Every operating system except Linux of course. In Linux I have to edit a strange file called /etc/X11/xorg.conf and manipulate obscure stanzas such as:

Section "ServerLayout"

Identifier      "XFree86 Dual-Head"

InputDevice     "Generic Keyboard"

InputDevice     "Configured Mouse"

Screen          "Screen0" 0 0

Screen          "Screen1" LeftOf "Screen0"

Option          "Xinerama"      "True"

EndSection

And then brutishly kill and restart my X.

If this is not bad enough, a recent upgrade b0rked my previously working x setup completely. I haven't had the time or the courage yet to tackle this problem, but I will have to. I have a practical assignment due which requires me to use my linux box.