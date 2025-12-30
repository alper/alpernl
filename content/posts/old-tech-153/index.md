---
title: "Control-less layout"
date: 2006-06-26T15:54:00
author: alper
categories:
  - english
  - software-engineering
---

I am quite turned off of the whole CSS Zen table-less design ethic. It is most unpractical. The most basic layout primitives have a less than straight forward translation to CSS.

**Task:** I have a series of <div> elements which I want to put side by side hard, no wrapping.

The obvious solution to this using

display: inline;

or

display: inline-block;

fails to work completely. The divs are not placed side by side.

Getting the divs to sit side by side is best accomplished by using

float: left;

though that seems to be a less than ideal use of the float attribute and floats are prone to incompatibilities of their own.

This still does not fix the fact that the floating divs wrap at the screen edge and I wanted them to sit side by side **hard**. The beautifully hackish solution to this is to wrap all the divs with a parent div set at

width: 10000px;

That makes enough room for the divs to sit in and not wrapping though it is horrible.

Separating style and content… yeah right. If there are better solutions to this, I would be glad to hear them.