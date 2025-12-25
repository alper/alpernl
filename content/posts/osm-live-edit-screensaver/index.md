---
_edit_last: "2"
_wpas_done_all: "1"
author: alper
categories:
  - english
  - internet
date: "2015-12-02T16:20:44+00:00"
guid: http://alper.nl/dingen/?p=5397
parent_post_id: null
post_id: "5397"
title: OSM Live Edit Screensaver
url: /dingen/2015/12/osm-live-edit-screensaver/

---
I've been running a [live open streetmap edits](http://osmlab.github.io/show-me-the-way/) view as a screen saver for a couple of years now and it never fails to draw the attention from people in the room (whether they know what OSM is or not). The OSM visualization is pretty cool and really comes to life when it is displayed full screen. It is also a great way to see a part of the world you might not have known existed. I used to browse atlases when I was a kid, so this is me indulging in virtual travel again.

[Will](http://willperkins.com/) attended me to the fact that I shot a video of it but I never wrote up the super basic process behind it, so here goes.

What it looks like:

{{< youtube id="Mi14GK2TX7U" >}}

This must have been the tweet by [Thomas](https://twitter.com/mrtoto) that started it all in early 2013.

> [@mrtoto](https://twitter.com/mrtoto) That should be made quickly with a web view or not? I still use my Barbarian Group screenstagram.
>
> — Alper Çuğun (@alper) [April 26, 2013](https://twitter.com/alper/status/327775871077347328)

After I read that I fiddled around a bit with making my own screensaver in XCode. That seems simple enough but building stuff on OS X is a bit of a pain if you're used to iOS and definitely not something you'll be able to finish in an hour or so. It turns out that there is a far far easier way.

1. Install the [webviewscreensaver](https://github.com/liquidx/webviewscreensaver). Thanks to [Alastair Tse](https://twitter.com/liquidx).
1. Plugin the URL to the live OSM view into the screensaver. This one: [http://osmlab.github.io/show-me-the-way/](http://osmlab.github.io/show-me-the-way/)
1. Enjoy.
