---
title: "JavaScript Multimedia"
date: 2007-01-30T10:30:00
author: alper
categories:
  - english
---

[SoundManager 2](http://www.schillmania.com/content/projects/soundmanager2/) for JavaScript is a neat little library to fill in one of the blank areas of JavaScript/DOM development: decent sound output. It is very cool that it's there, but it's a shame that it has to use Flash to do the playback because browser sound playback is so dismal.

JavaScript is proving more and more that it can compete full force with Flash. The 2D graphics capabilities the dojo guys have built with dojo.gfx (cross browser Canvas stuff) and dojo-svg and the likes already look quite mature.

What has been missing up until now are native in browser sound support and video support. SoundManager provides sound support but its dependency on Flash is not preferrable.

We need a native Sound object which provides play, pause and seek support in arbitrary sound files.

**Audio**

I'm thinking about something like this:

// Need to figure out which sound formats would be supported

// Ideally a basic set of formats (wav, mid, etc.) MUST be supported

// but the object should have a backend capable of playing anything: mov, ra etc.

var s = new Sound('sounds/haha.mp3', true);

s.loop(true);

// do we play onload or do we play streaming?

// what happens on network congestion?

s.play();

// Get the length (in millis?) and allow seeking in the file (also during playback?)

s.length;

s.seek(3000);

s.pause();

s.stop();

Just Googled a bit and it looks like WhatWG is already speccing something along these lines in [Web Applications 1.0: Sound](http://whatwg.org/specs/web-apps/current-work/#sound)

They deferr streaming audio to the object element which might be reasonable for the time being, but is not going to cut it in the long run.

The WHATWG spec has no mention of the audio formats that COULD, SHOULD or MUST be supported. I don't know how you would reasonably develop cross browser applications if you can't depend on a present profile.

pause and seek are not mentioned though they might be emulated using the *current position* from the spec. It is not clear if these properties are settable and the solution would be hackish and therefore not preferrable. Some stuff along these lines has already been [suggested by Mathieu Henry](http://lists.whatwg.org/htdig.cgi/whatwg-whatwg.org/2006-January/005352.html).

**Video**

Along these lines JavaScript should also provide a native video implementation. This could either be a browser exposed low level codec which you pass a Canvas object.

var v = new Video('video/blabla.avi', dojo.byId('player'));

v.play();

If low level codecs are not feasible an alternative could be a video server which passes compressed video data to the browser via something like comet and uses a JavaScript library to decompress and draw on a Canvas. (When am I going to have the time to write this?)

Regarding the WHATWG spec, they will probably defer video to the object element seeing as most real video is streaming but I don't think this position is tenable for the future unless you want the browser to be hollow vehicle for the Flash plugin.