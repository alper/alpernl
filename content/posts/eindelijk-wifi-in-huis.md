---
author: alper
categories:
  - internet
date: "2007-08-04T10:50:05+00:00"
guid: http://alper.nl/dingen/2007/05/eindelijk-wifi-in-huis/
parent_post_id: null
post_id: "39"
tags:
  - computers
  - huishoudelijk
  - internet
title: Eindelijk WiFi in huis
url: /dingen/2007/05/eindelijk-wifi-in-huis/

---
[![](http://farm1.static.flickr.com/167/486973408_27d5c89b22.jpg)](http://www.flickr.com/photos/alper/486973408/ "photo sharing")  
[linksys](http://www.flickr.com/photos/alper/486973408/), originally uploaded by [illustir](http://www.flickr.com/people/alper/).

Sinds ik een Mac heb maak ik gebruik van het bestaande draadnetwerk in huis. Het is een beetje primitief maar met de twee kabels die er zijn kon ik op de meeste plekken wel internetten.

[![Mess of cables](http://farm1.static.flickr.com/223/487004211_69d9698c1c_m.jpg)](http://www.flickr.com/photos/alper/487004211/ "Photo Sharing")

De drang naar WiFi was er wel maar het was nog niet zo makkelijk te realiseren. In de eerste plaats was onze internet router een oude Linux-bak ((Die ook begon te piepen en te kraken. Ik weet niet meer hoeveel foute sectoren er op die harde schijf stonden maar blijkbaar markeert Linux die dan en gaat gewoon verder. Hij heeft prima als web-/fileserver gefunctioneerd met als enige manco dat de /-partitie minder dan 40Mb vrij had.)) waar tegelijkertijd de webserver ((Dit waren zowel een Apache frontend webserver alswel een complete geproxyde [Zope](http://www.zope.org) installatie waar het blog onder draaide. Het feit dat Zope zo bijzonder exotisch is, zorgde ervoor dat migratie naar een standaard PHP/MySQL hosting provider niet één-twee-drie geklaard was.)) van [alper.nl](http://alper.nl) op draaide. Dat moest dus blijven draaien. Met [de recente migratie](/blog/alper/830) van alles van alper.nl naar [Dreamhost](http://www.dreamhost.com) is de weg dus vrij gemaakt voor het opheffen van die bak en het installeren van een echte draadloze router.

Vandaag deze oude [FON](http://www.fon.com/) router bij mijn ouders opgehaald en geïnstalleerd ((Het idee was om aldaar een FON-hotspot te creëren maar UPC en die router konden niet zo goed met elkaar overweg.)). Op Cristiano's aanraden heb ik de Fon-firmware overschreven met [dd-wrt](http://www.dd-wrt.com) wat bijzonder fijn werkt ((Fon heb ik altijd bijzonder gebruikersonvriendelijk gevonden. Zeker niet geschikt om de burger ertoe te krijgen een draadloze revolutie voor elkaar te krijgen.)) en uit den treure configureerbaar lijkt.

### Mis-configuratie

Ik probeerde na de nieuwe firmware de router draadloos te configureren en ik kwam op een langzame en vreemd uitziende gebruikersinterface uit. Hier een beetje rondgeklikt, het wachtwoord veranderd en een [ACL](http://en.wikipedia.org/wiki/Access_control_list) voor Mac-adressen ingesteld.

Toen kwam ik er niet meer in en na het inpluggen van een kabel in mijn linksys kwam ik op een andere (!) —de juiste— admin interface terecht. Het blijkt dus dat ik de router van iemand anders in de buurt heb zitten configureren, maar nu kom ik (en waarschijnljk hij ook) er niet meer in.

### Eerlijk delen

De enige functionaliteit die ik mis in de dd-wrt router is de mogelijkheid om mijn netwerk af te schermen maar voor mensen in de buurt een kleine internetlijn open te stellen. Ik waardeer het erg als ik ergens ben en er open WiFi is. Ik zou graag datzelfde willen aanbieden. Het schijnt dat die functionaliteit er in een volgende versie in komt.
