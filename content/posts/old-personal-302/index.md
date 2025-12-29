---
title: "Flickrcrawl"
date: 2005-06-21T01:35:00
author: alper
categories:
  - nederlands
---

Dankzij de [goede zorgen van Nelson](http://nelson.monkey.org/~nelson/weblog/tech/good/flickrClient.html) heb ik in een klein uurtje een script geschreven dat [Flickr](http://www.flickr.com) afstroopt op foto's. Het maakt me eigenlijk niet uit wat voor foto's het zijn of wat erop staat. Ik heb er gewoon heel veel nodig.

De mensen van Flickr zijn erg goed en met weinig als ik de berichten mag geloven. Het schijnt dat Flickr is begonnen met een team van 8 mensen.

In ieder geval ze hebben alle functionaliteit van de site blootgesteld via [een webservices API](http://www.flickr.com/services/api/). Ze doen nog veel meer dingen ontzettend goed. Daarover later misschien meer.

Ik pak steeds een willkeurig woord uit

/usr/share/dict/american-english

. Dat woord stop ik in de flickr.photos.search methode van de API met behulp van [FlickrClient.py](http://micampe.it/things/flickrclient).

Alle foto's die ik terugkrijg [haal ik op](http://www.flickr.com/services/api/misc.urls.html) en schrijf ik weg op mijn harde schijf.

Als ik dit een nachtje laat draaien zou ik een flink corpus moeten hebben. Het idee is dat ik die foto's als aanzetje gebruik om in [ImageSeek](http://imgseek.python-hosting.com/) te pluggen. Een content-based Flickr zoekmachine!