---
title: "Doorbouwen"
date: 2005-01-26T00:35:00
author: alper
categories:
  - nederlands
  - software-engineering
---

Meer [Ximian](http://www.ximian.com/): [een uitleg](http://primates.ximian.com/~miguel//texts/gtkjava.html) hoe Java code gebruik te laten maken van Gtk# en te draaien op [Mono](http://www.mono-project.com/).

Het draait dan in [IKVM](http://www.ikvm.net/) wat een Java VM tussenlaag is die zelf weer op Mono draait. Je krijgt dus een JIT-vertaling van Java-bytecode naar CIL (Commmon Intermediate Language) en daarna weer een JIT-vertaling van CIL naar native x86-code. Twee keer JIT'ten lijkt misschien overbodig maar het gave is dat het mogelijk is. Net zoals in [het artikel](http://primates.ximian.com/~miguel//texts/gtkjava.html) staat hoe allebei die JIT-slagen uit de weg geruimd kunnen worden.

Ik vind het geweldig hoe die gasten C# effectief compleet hebben nagemaakt. Met allemaal gave features en interoperabiliteit dat allemaal gewoon werkt. Op deze manier hebben we én Microsoft én Sun allebei niet nodig.

Ik heb gehoord dat het nog niet heel erg snel is maar ze zijn er nog steeds hard mee bezig. En slim als ze zijn houden ze zich aan *Knuth*.