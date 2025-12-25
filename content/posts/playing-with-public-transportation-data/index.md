---
_edit_last: "2"
author: alper
categories:
  - english
  - monster-swell
date: "2008-09-08T14:50:15+00:00"
guid: http://alper.nl/dingen/?p=381
parent_post_id: null
post_id: "381"
tags:
  - json
  - open-data
  - public-transportation
  - travel-times
  - visualization
title: Playing with Public (Transportation) Data
aliases:
  - /dingen/2008/09/playing-with-public-transportation-data/

---
As [promised a while back](/dingen/2008/06/workshop-session-on-geodata-visualization/) after we got our fill playing with the data I would release it to the public to see if you could come up with something interesting. I'd leaked the JSON file to [Kars](http://www.leapfrog.nl) and he applied his skills in visualizing things in processing ((With some help from [Ben Fry](http://benfry.com/).)) to the dataset.

Then after some more back and forth I retrieved a similar dataset from the [ANWB](http://www.anwb.nl) site ((These site operators are so friendly and accomodating.)): the time to travel a similar distance at a similar time but this time by car ((With historical traffic congestion information added, but because the sampled time was around noon the effect should be negligible.)).

[![](http://farm4.static.flickr.com/3103/2743375229_dcc34baa21.jpg)](http://www.flickr.com/photos/kaeru/2743375229/in/set-72157606466915102)

The juxtaposition of those two datasets made for some interesting results and some nice applications of [interactive filtering](http://www.flickr.com/photos/kaeru/2761843373/in/set-72157606466915102). Kars has [a full writeup](http://leapfrog.nl/blog/archives/2008/08/15/the-making-of-a-travel-time-map-of-the-netherlands/) of his process.

So without further ado, here is the dataset under a [Creative Commons Attribution license](http://creativecommons.org/licenses/by/3.0/nl/). It's a [JSON](http://json.org/) file: [Traveltimes](/dingen/wp-content/uploads/2008/09/traveltimes.json) with as keys a four digit string for the postal code. The value is a dictionary with this key-value mapping:

latLatitude GPS coordinatelngLongitude GPS coordinateplaceInferred name of the locationtimeThe time it takes using public transportationcarTimeThe time it takes by car (a small amount of null values where the time could not be retrieved)All times are from the center of the 4 digit postal code as well as can be determined to Dam Square in Amsterdam around noon on a given day.

I find it interesting (and somewhat appalling) to see how large the difference is between taking the car or going by public transportation. Doing a sampling for 08:00 on Monday morning during rush hour might somewhat equalize this, but I think it's safe to say that car owners will remain at an advantage.

So next up is e-mailing [GroenLinks](http://www.groenlinks.nl) and [Rover](http://www.rover.nl) to see if they can use this data or these visualizations.
