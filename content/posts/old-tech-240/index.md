---
title: "CSS is a miserable failure"
date: 2007-02-13T15:44:00
author: alper
categories:
  - english
---

I've been taking a peek at the [CSS layouts at Dynamic Drive](http://www.dynamicdrive.com/style/layouts/) and especially at [CSS Fixed Layout #2.1](http://www.dynamicdrive.com/style/layouts/item/css-fixed-layout-21-fixed-fixed/) and I'm slightly stumped.

For one, why is stuff like the following code necessary? It looks like a ridiculous hack to me:

#leftcolumn{

float: left;

width: 200px; /*Width of left column*/

margin-left: -840px; /*Set left margin to -(MainContainerWidth)*/

background: #C8FC98;

}

And another is the nesting of DIVs which leaves nothing semantic in the design and does not yield any advantage over tables. Trace with me:

DIV#contentwrapper > DIV#contentcolumn > DIV.innertube > P

And then still when copying over the style rules, the design renders differently in my template. Firebug lists an offsetTop of 16px on the first DIV and I have no clue where this is coming from. Looks like I'll have to literally copy the Dynamic Drive example and work from that (later on).

**CSS Gurus:** You have succeeded in building an elitist edifice which is inaccessible to all but the most hardcore of webdesigners. Your standards suck, they are incomplete both in conception and adoption and the tooling which we are supposed to work with is meagre [at best](http://www.getfirebug.com/).

I'm not saying you have lost and should go home. I'm saying you should work even harder at sharing your knowledge because the current state isn't anything to write home about.

Seriously, if I can't figure this out after some fiddling there are literal millions out there who do not stand any chance whatsoever.

Here's to <table>s who might become the new black again in a year or two.