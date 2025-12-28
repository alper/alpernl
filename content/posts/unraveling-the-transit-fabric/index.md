---
author: alper
categories:
  - english
  - internet
  - product-design
date: "2009-03-30T00:14:50+00:00"
title: Unraveling the Transit Fabric
aliases:
  - /dingen/2009/03/unraveling-the-transit-fabric/

---
Previous efforts of privatizing Dutch rail failed miserably. In 1999 [Lovers Rail](http://nl.wikipedia.org/wiki/Lovers_Rail) ran competing trains along a couple of Dutch tracks ((Among which Amsterdam — Haarlem, also the oldest Dutch railway connection.)). I was just starting my studies in Delft and did a daily commute from Amsterdam where I was living back then ((And where I will be living again in the near future if things work out.)), so I remember their service, though I never actually used it.

[![Full Train](http://farm1.static.flickr.com/15/18906108_10d182aeac_m.jpg)](http://www.flickr.com/photos/alper/18906108/ "Full Train by illustir, on Flickr")

Sometimes when stuck on a station, because the [NS](http://en.wikipedia.org/wiki/Nederlandse_Spoorwegen) had messed up again, it could actually have been useful to take a Lovers train from Haarlem to Amsterdam. In reality this never worked out. Nobody knew when those trains actually departed and where to buy tickets for them ((Of course you couldn't buy tickets on board.)).

The privatization was stalled and the [NS](http://en.wikipedia.org/wiki/Nederlandse_Spoorwegen) was granted a monopoly on the main rail system until 2015. Now if we want to be in good shape to turn another privatization attempt into a success by then or hopefully before, we had better get our digital infrastructure in order.

### Solution

I think two ingredients are now slowly getting into place to turn another privatization attempt of the railways into a success:

1. Full dynamic and open transit **data**
1. Seamless transit **payment**

[![](http://farm4.static.flickr.com/3185/2981951806_43fbd8de96_m.jpg)](http://www.flickr.com/photos/moosterbroek/2981951806/)
OV-chipkaart terminal
[CC](http://creativecommons.org/licenses/by-nc-nd/2.0/deed.en_GB) picture by [mooste](http://www.flickr.com/people/moosterbroek/)

Neither of these is fully there yet ((For a Dutch argument see [a previous post](/dingen/2009/03/op-radio-online-tegen-de-ns/).)), but in a couple of years we may expect both deployments to mature significantly. In that [future perfect](http://www.janchipchase.com/) you will always know which train will take you to your destination regardless of the operator who runs the service. Payment of that service should be as easy as the check-in, check-out system of the [OV-chipkaart](http://en.wikipedia.org/wiki/OV-chipkaart) right now if not easier.

Rail services would then finally be completely commoditized ((This is assuming [ProRail](http://nl.wikipedia.org/wiki/ProRail) would be able to cope with the complexity of accomodating for all these operators.)) and by extension we could do the same to all of transit.

### Breaking it open

Rail is one thing, but the transit experience entails the door to door planning and execution of a trip of which rail is just one part. Data and payment are just as essential to a nationwide ((We could also think about the transnational problem but let's leave that for now.)) transit infrastructure. Probably even more so because of the greater diversity of transit providers ((And the Netherlands has one of the finest transit meshes in the world. We would be stupid not to take advantage of that.)), many of which are not bound to fixed rail.

For my day to day transportation needs I want to get from **A** to **B** at a certain time for a certain price. A mobile device would know my location and when given my destination it would be able to show me a list of offers from which I could pick my preferred one. Some of the planners available do just this but because they are usually limited to a single operator, their offerings do not differ much.

[![9292ov.nl: OV-reisinformatie en routeplanner voor bus, trein, metro, tram en veerboot](http://farm4.static.flickr.com/3586/3392789731_c81580065f.jpg)](http://www.flickr.com/photos/alper/3392789731/ "9292ov.nl: OV-reisinformatie en routeplanner voor bus, trein, metro, tram en veerboot by illustir, on Flickr")

Google goes for a more modus agnostic integrated and modern view of the experience:

[![Google Transit](http://farm4.static.flickr.com/3560/3393643096_572ef340a6.jpg)](http://www.flickr.com/photos/alper/3393643096/ "Google Transit by illustir, on Flickr")

Further opening up and integration would benefit travellers enormously. Ideally we would have one planner for all transit options, which includes rail, (micro)bus, lightrail, ferry but ideally also taxicabs and private individuals willing to carpool ((Just think how disruptive this would be to the whole concept of transit.)). This would add options and level the playing field.

### What we would need

The following data dimensions would influence your choice of transportation option and would need to be offered to you by your planning tool of choice:

**Time:** How fast will this get me somewhere? How long do I have to wait before it leaves? Or did it already leave? How many times do I need to change?

**Money:** How much does this trip cost me? How much does it cost me in terms of CO2? Is it offset? How much would it cost me (in time and money) if I'd taken my car instead?

**Quality:** What is the quality of service offered? Are there different classes with different amenities? Is there WiFi on board? Do I get assistence getting on/off or with my luggage?
These would probably be standardized per modus of transportation but the class separation is pretty ingrained and influences the cost.

**Reviews:** What do people think of this particular operator?
In the case of standardized operators, you will usually know what you will get, but especially useful for modi where there is a great variety of operators performing services. Taxicabs would be a very nice target for community judgement.

Of course you should be able to set your preferences as to which modi and operators to prefer and which to never take unless no other options are available. Complicated but also a very nice UX problem to solve.

### Planning and Negotiation

Some extra functionality may also be interesting to incorporate in this dynamic transit fabric:

**Planning:** Submitting a tentative plan may be interesting for transit operators so that they can optimize their services ahead of time. Many commuters know when they will travel which route a year or so in advance sometimes. Marginal discounts may be offered to those who submit a plan and stick to it (penalties for those who deviate) ((Of course this will completely cloud the pricing structure of transit. I'd be fine with it. It's mostly voodoo to me anyway already (never really figured out the relation between [strippen](http://en.wikipedia.org/wiki/Strippenkaart#Strippenkaart) and zones).)). Publishing the statistics of trips requested and trips completed would show over- and undercapacity and give the various operators the chance to adjust their offerings.

Submitting a plan may involve a negotiation step: e.g. it will be cheaper if you walk to a certain place (stop) or the bus will swerve round to pick you up for a couple extra euros, which do you prefer?

A plan would then need to be finalized, either at the point of getting on/off (and paying the fare amount) or ahead of time to reserve a (type of) seat in a vehicle or for remote locations to guarantee the fact that the vehicle will pass by your area at all.

**Renegotiation:** Changes do happen, most impactful are those due to calamities: vehicle failure, track obstruction. Being able to flexibly catch these will vastly improve the transit experience ((Though people may not notice. Failure is annoying when it happens but quickly forgotten. A system which resolves not to fail may set itself up to impossibly high standards.)). A good system would both inform transit operators so they can allocate extra resources where suitable and help travellers replan their journey in light of changed circumstances.

In a dynamic system with the planning functionality as described above in place, others' change of plans in the system may influence your journey but no more than a couple of minutes. What would happen when those changes propagate through the entire network?

### Conclusion

If we could achieve the openness and added integration of more information and more transit providers described above we could make very satisfying complete transit experiences.

[![iPhone Transit Planner](http://farm4.static.flickr.com/3577/3394196679_def20471c7.jpg)](http://www.flickr.com/photos/alper/3394196679/ "iPhone Transit Planner by illustir, on Flickr")

I've made a mockup what such an application could look like:

Being able to compare and contrast various transit options would of course be fantastic, but that isn't so far off anymore. For me the most promising idea is to provide the information and the incentives to enable the transit problem to be made transparent and to be crowd-sourced.
