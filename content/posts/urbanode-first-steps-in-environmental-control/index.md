---
author: alper
categories:
  - amsterdam
  - english
  - internet
  - music
  - product-/-design
  - the-city
  - work
date: "2010-12-20T14:38:07+00:00"
title: 'Urbanode: first steps in environmental control'
aliases:
  - /dingen/2010/12/urbanode-first-steps-in-environmental-control/

---
[Urbanode running from an Android Phone](http://vimeo.com/17403000) from [VURB](http://vimeo.com/user5376973) on [Vimeo](http://vimeo.com). The movie shows an Android phone controlling the stagelights at the Melkweg using a colour picker on a webpage.

I'm quite proud to have been part of the local systems integration crew of [Urbanode](http://urbanode.net) with the steps we made on controlling environments using web technology. The movie above shows my laptop connected to a lighting panel in the [Melkweg](http://www.melkweg.nl) running an OLAD ( [Open Lighting Architecture](http://opendmx.net/index.php/OLA)) server talking ARTNET/ [DMX](http://en.wikipedia.org/wiki/DMX512) to talk with the panel and the [urbsville](https://github.com/termie/urbsville) [NodeJS](http://nodejs.org/) application that exposes the available lights as an interface on a webpage for the Android phone.

So the flow is as follows:

- Android phone (or other), goes to a webpage on the local network
- The webpage is served by urbsville using NodeJS which means everything is live and can be kept consistent across clients
- Any device setting is mirrored using an internal mapping by updating the DMX values of the corresponding device on the ARTNET output
- OLAD sends its current state to the lighting panel
- The lighting panel updates (merges) the values into its universe and when they are hooked up the lights change their behaviour —or colour in this case— accordingly.

So starting with colours and intensities of lights, the next step is being able to hookup arbitrary properties of any kind of device and making it all work solidly so application developers, lighting specialists and game designers can get ahold of this technology.

A lot of this is still quite abstract and the technology setup is pretty cutting edge but this is an essential building block for moving forward. Being able to control [physical devices using Javascript](http://www.phidgets.com/) has already been possible as has service discovery in spaces (tons of demos by Philips, [Sun](http://en.wikipedia.org/wiki/Jini) and the likes). Urbanode breaks out of the local application cul-de-sac and exposes everything straight to the web using the web's most native control language: Javascript. This is a big step in totally commoditizing device control and normalizing and expanding the scale of operation.

This has been blogged about already by the Urbanode team [“Prototypes for discoverable services in public space”](http://urbanode.net/2010/12/prototypes-for-discoverable-services-in-public-space/), [“Alpha Release: Urbanode”](http://urbanode.net/2010/12/let-light-be-urbed/) and picked up by [Bruce Sterling on Wired](http://www.wired.com/beyond_the_beyond/2010/12/prototypes-for-discoverable-services-in-public-space-urbanode/). I would encourage you to [go to github and clone](https://github.com/termie/urbsville) the code and tell us what you think.
