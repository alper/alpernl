---
title: "Lumen iCal"
date: 2006-09-21T11:33:00
author: alper
categories:
  - nederlands
---

Mijn [Filmhuis Lumen iCal generator](http://alper.nl/wiki/index.php/Lumen_iCal) deed het niet meer. En hij was stiekem toch best wel handig.

Even graven onthulde dat ik de python versie op mijn server had ge-upgrade maar dat python2.4 het betreffende pakket niet meer had (pakket staat niet in Debian). Even verplaatsen en hij doet het weer.

Nu wil ik in de kalender informatie opnemen over mij zodat gebruikers contact met me op kunnen nemen als het weer mis gaat en sowieso te horen als meer mensen het gebruiken. Te lezen in RFC 2445 heeft het VCALENDAR object alleen een version en een prodid.

In sectie 4.8.8.1 staat dat je je eigen eigenschappen kunt definieren met een X--prefix maar ik kan nergens vinden welke clienten welke eigenschappen ondersteunen. Ik heb nu maar de X-AUTHOR toegevoegd maar knappe kop die mij op die manier weet te bereiken.

Gebruik jij het? Vind je het handig? Laat het weten.