---
title: "Valid Dojo"
date: 2006-02-18T22:55:00
author: alper
categories:
  - english
---

I managed to make it to the [Happy Clog](http://www.happyclog.nl/) meeting ([pictures](http://www.flickr.com/photos/alper/archives/date-posted/2006/02/18/)) one hour late. It was fun having a couple of drinks in de Bruine Boon and talking about standard standards stuff.

Not having any internet ([Wireless Leiden](http://www.wirelessleiden.nl/) is not all that it is made up to be), options for discussion and *show and tell* were quite limited. Luckily I keep recent checkouts of both [dojo](http://www.dojotoolkit.org/) and [django](http://www.djangoproject.com/) on my iBook. I showed a couple of dojo widgets and explained the logic behind, so I could get some evangelizing in.

The first comment I got was that the dojoType in the widgets

<div dojoType="FisheyeList"…

would not validate. On page load dojo scans the dom to see where it has to replace nodes with widgets. The dojoType attribute is one of the handles it can grab hold of.

These guys are really into their validators and were not easily swayed by all this widget loveliness.

I could not dig up the relevant bits then and there, but now at home I can find the relevant FAQ entry. Above code could be made to validate like this:

<div class="dojo-FisheyeList"…

So all's well that ends well.