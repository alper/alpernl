---
title: "NOVA RSS"
date: 2006-04-02T01:05:00
author: alper
categories:
  - nederlands
  - video
  - internet
---

Na al [het gezeik](/posts/old-personal-591), ook weer eens tijd voor wat goed nieuws. Ze hebben bij NOVA voor de items in het weekarchief nu ook [een RSS feed](http://www.novatv.nl/rss/novafeed.xml). Dit is iets wat ik al heel lang wilde en waar ik pas met een screen scraper aan was begonnen te schrijven. Dat hoeft nu dus niet meer.

Hun feed [valideert zelfs](http://www.feedvalidator.org/check.cgi?url=http%3A%2F%2Fwww.novatv.nl%2Frss%2Fnovafeed.xml) volgens de Feed Validator.

Ik zou als simpele eindgebruiker nog een paar kleine suggesties hebben:

- Autodiscovery aanzetten voor de pagina's door deze code in de template te zetten <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="http://www.novatv.nl/rss/novafeed.xml" />


- Een nieuwerwets standaard feed-icoon ![](http://www.alper.nl/img/feed-icon.png) gebruiken ([verkrijgbaar in verschillende kleuren](http://www.feedicons.com/))


- In de title van een item zoals in het geval *“03/29 - Asielzoekerskinderen achter de tralies”* staat de datum er op zijn Amerikaans. Dat zou vriendelijker kunnen bijv. *29 maart*.


- In de description staat de eerste alinea van het verhaal op de site. Het zou fijner zijn als dit het complete verhaaltje was.


- De directe links naar de rm- en asf-streams in de description zetten zodat ik in één keer naar de video van het item kan.