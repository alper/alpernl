---
date: '2026-03-23T12:47:22+01:00'
title: 'Remapping Dvorak'
author: "alper"
categories:
  - english
---
Using [my external 40% keyboards](https://alper.nl/uses/) has always been very annoying with my Macbook. I type Dvorak so that's what the keyboard layout is set to but that only really works properly if the laptop is set to the US layout. But when I type on the laptop directly I have to switch it to the Dvorak layout. This is already a pain but the remapping also messes with many keyboard shortcuts.

Trying to debug this did my head in and it's complicated enough that you can't really ask for help online about it either. What worked this time round is working through the problem with Claude and brainstorming solutions.

The most straightforward way to do this sounded a bit iffy but worked a treat. We leave the laptop on the US layout always but we remap the device keyboard keys to Dvorak using [Karabiner Elements](https://karabiner-elements.pqrs.org). That means my [QMK remapped keyboards](https://github.com/alper/40pct-layout) can connect as is. This also clears up my keyboard shortcuts though I'm hard pressed to explain exactly how.

Once I was on this trail, I found this [blogpost by my former teacher Charl Botha](https://cpbotha.net/2016/12/16/dvorak-remapping-with-karabiner-elements-on-macos-sierra-works/) who faced the exact same problem and landed on the same solution with examples in Karabiner Elements. It really is a small world.
