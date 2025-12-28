---
author: alper
categories:
  - english
  - internet
  - video
date: "2009-07-16T13:27:09+00:00"
title: Augmented reality in HTML5
aliases:
  - /dingen/2009/07/augmented-reality-in-html5/

---
One of the last bastions of Flash and native apps is the processing of video from outside sources such as webcams. It does not at all seem difficult to add this functionality to [HTML5](http://www.whatwg.org/specs/web-apps/current-work/).

I don't have much of any experience in designing these kind of specs (though [I did request <audio> and <video>](/blog/tech/238) elements some two and a half years ago), but here are some design notes which seem to make some sense:

### Get outside video

Create a specific [src parameter](http://www.whatwg.org/specs/web-apps/current-work/#dom-media-src) for video, for instance src="webcam" to get image data from a current installed webcam [^1]. The user-agent can mediate the presence of cameras and the routing of sources. This gives the user-agent a way to get device video into the web application.

Besides augmented reality this could be used for most webcam related applications on websites but for that some more facilities for retrieving and transmitting the video stream will be necessary.

### Get at the frames

Now to get at the raw video data the addition to [HTMLVideoElement](http://www.whatwg.org/specs/web-apps/current-work/#htmlvideoelement) of a method (like [the canvas already has](http://www.whatwg.org/specs/web-apps/current-work/#dfnReturnLink-25)) would seem to fit:
`ImageData getImageData();`
that returns [an ImageData object](http://www.whatwg.org/specs/web-apps/current-work/#imagedata) for the current frame of video. This would either work for the current frame when the video is paused or the current frame unpredictably when the video is playing (for applications to retrieve frames of video as fast as they can process them).
Alternatively register a callback function to the <video> element where every video frame is pushed to.

**Update:** [Mark points out below](/dingen/2009/07/augmented-reality-in-html5/#comment-8443) this is already possible using [the drawImage function](http://www.whatwg.org/specs/web-apps/current-work/#images) of the canvas rendering context which accepts a video element and draws [the current playback position](http://www.whatwg.org/specs/web-apps/current-work/#current-playback-position).

If you can reliably extract all video frames and store them locally, you may even be able to build a non-linear video editing application.

### Process and redraw

Processing the frames to create an augmented reality is left as an exercise for the reader.

Ideally each frame of video could also be rendered into a [canvas](http://www.whatwg.org/specs/web-apps/current-work/#canvas) where the client could draw other primitives on top of the video frames. This seems to be necessary for the augmented part of the augmented reality.

**Update:** This already seems to be possible by putting the image back into a canvas, but I don't think that would sync up the audio properly.

So all that is needed is the addition of an extra source and an extra method to the <video> element. Doesn't seem like that much, does it?

[^1]: Though there may be better ways than a ‘magic value’ for the source attribute.
