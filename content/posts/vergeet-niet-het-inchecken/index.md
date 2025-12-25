---
author: alper
categories:
  - internet
  - monster-swell
  - nederlands
  - product-/-design
  - the-city
date: "2009-11-30T13:21:09+00:00"
title: Vergeet niet het inchecken
aliases:
  - /dingen/2009/11/vergeet-niet-het-inchecken/

---
We hadden het pas nog in de kroeg over om [de ov-chipkaart](http://www.ov-chipkaart.nl/) te hijacken en te gebruiken als unieke id voor interactieve digitale projecten. Ik had lang geleden een vergelijkbaar idee om hetzelfde te doen met bijvoorbeeld de AH-bonuskaart. Het zijn allebei machine-leesbare tokens met een uniek nummer die (bijna) iedereen altijd bij zich heeft.

Toen kreeg ik gisteren deze [link door met een serie API-implementaties](http://inventorspot.com/articles/early_adopter_apis_foursquare_34937) van Foursquare waaronder: [FourTap](http://www.vimeo.com/7068682) van [Dan](http://twitter.com/iamdanw). Dan leest dus met een RFID reader zijn Oyster uit en met een vooraf gelegde koppeling tussen die id en zijn account op Foursquare, kan hij dan een actie uitvoeren zoals bijvoorbeeld inchecken in een venue.

[FourTap - Checking in to Foursquare using an Oystercard](http://vimeo.com/7068682) from [danw](http://vimeo.com/iamdanw) on [Vimeo](http://vimeo.com).

De OV-chipkaart is een vergelijkbare technologie, dus het zou mogelijk moeten zijn om hetzelfde te doen. Meer toepassingen voor verschillende applicaties en databases met correspondenties tussen je OV-chipkaart en Hyves/Facebook, laten op zich wachten.

### Geolocatie

[![Irreducible Complexity?](http://farm4.static.flickr.com/3499/3810654377_7e6ef6d839_m.jpg)](http://www.flickr.com/photos/alper/3810654377/ "Irreducible Complexity? by illustir, on Flickr")

Nog een andere leuke toepassing zou het zijn wanneer [het transactie-overzicht op ov-chipkaart.nl](https://www.ov-chipkaart.nl/mijnov/reizenentransacties/transactieoverzicht/) niet zo ontzettend vertraagd zou zijn. In het ideale geval zou elke checkin en checkout via [een pubsubhubbub](http://code.google.com/p/pubsubhubbub/) naar geïnteresseerde en geautoriseerde partijen gestuurd worden ((Maar ik zou al blij zijn als recente transacties binnen een kwartier in het transactie-overzicht stonden.)).

Je zou dan bijvoorbeeld een automatische Foursquare of [Google Latitude](http://www.google.com/intl/en_us/latitude/intro.html) inchecker kunnen bouwen die je locatie op die manier automatisch doorkrijgt.
Of een [kleurrijk spel](http://www.wearemudlark.com/projects/project-6/) in de stad.
Of een mobiele applicatie die via GPS ziet wanneer je vergeten bent uit te checken en je erop attendeert zodat je naar het poortje terug kunt lopen ((Hoe vet zou dat zijn!)).

Voorlopig lijkt het erop dat het systeem goed draaiende krijgen prioriteit heeft (terecht) en dat dat al moeilijk genoeg is (jammer) zodat we nog even moeten wachten op dit soort technologische hoogstandjes.

**Update:** Lees net bij de goede [mensen van Stamen](http://content.stamen.com/hq2_week1) over het project [Fake Subway APIs](http://fakesubwayapis.appspot.com/) ( [source](http://github.com/straup/gae-fakesubwayapis)) want:

> you know, for when realtime proper APIs are an assumed part of digital civic infrastructure, just like electricity

Van de week maar even een patch toevoegen voor de Amsterdamse metro. We hebben hier ook [afkortingen](http://nl.wikipedia.org/wiki/Wibautstraat_(metrostation)).

En woensdag kunnen we over dit soort dingen praten in [de Verdieping](http://www.facebook.com/event.php?eid=188558907275&ref=mf).
