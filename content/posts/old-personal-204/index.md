---
title: "Twisted"
date: 2005-03-27T17:46:00
author: alper
categories:
  - nederlands
  - software-engineering
---

Ik ben in een opwelling gisteravond begonnen om mijn eigen blog-software te schrijven. Niet echt omdat ik het nodig heb, maar om beter bekend te raken met een paar hele krachtige en ondergewaardeerde libraries (SQLObject & Twisted).

[SQLObject](http://sqlobject.org) is erg gemakkelijk in het gebruik. Ik had niet echt zin om [Foreign Key Constraints](http://www.postgresql.org/docs/7.4/static/ddl-constraints.html#DDL-CONSTRAINTS-FK) in [PostgreSQL](http://www.postgresql.org) uit te gaan zoeken en dat hoeft dus ook niet.

[Twisted](http://www.twistedmatrix.com) is een ander verhaal. Het is een super-stoer raamwerk met best [veel documentatie](http://twistedmatrix.com/documents/) die niet erg helder is. Dat was wel fijn geweest want de opzet is erg complex en vereist een hele andere manier van denken.

**Update:** Hieronder volgt een heleboel nerd-praat over hoe en wat het werkt maar mijn indruk van Twisted komt overeen met mijn verwachtingen.

Twisted is erg groot, er zijn delen die erg volwassen zijn en andere delen die nog ontzettend in ontwikkeling zijn.

Er straalt van alles (behalve de documentatie) of dat het gemaakt is door mensen die weten wat ze doen. Het nette ontwerp, de volwassen admintools etc. dat zit allemaal heel goed in elkaar.

En ook al lijkt het moeilijk, als je de voorbeelden volgt zijn er ook veel dingen die ontzettend makkelijk worden gemaakt. Ik heb een voorbeeld overgenomen, een irc-bot  van een paar(!) regels code, en dat uitgebreid zodat je er galgje mee kunt spelen.

Daar komt de Python-filosofie wel om de hoek kijken: makkelijke dingen makkelijk en complexe dingen mogelijk maken.

**Uitleg:** In een normaal programma voer je gewoon dingen uit:

doeIets()

doeIetsWaarJeLangOpMoetWachten()

doeNogIets()

En als je dat lange wachten niet ziet zitten dan start je een Thread die dat parallel voor je doet zodat jij gewoon door kunt gaan met doeNogIets(). Zo gebeurt het overal, maar dat gaat bij Twisted niet op.

Twisted heeft maar één Thread (want dat is efficienter), nog een Thread starten is niet de bedoeling, lang wachten ook niet. Bovenstaande code moet je dan omklussen tot:

def alsHetKlaarIs(resultaat):

    doeIetsMet(resultaat)

doeIets()

belofte = ikGaDoorIkHoorHetWelAlsHetKlaarIs()

belofte.addCallback(alsHetKlaarIs)

doeNogIets()

De aanroep naar ikGaDoorIkHoorHetWelAlsHetKlaarIs() komt meteen terug en doet ons een belofte (een [Deferred](http://twistedmatrix.com/documents/current/api/twisted.internet.defer.Deferred.html)).

Aan die belofte vragen we om op de hoogte gehouden te worden. Dat doet hij door als het dan klaar is alsHetKlaarIs() aan te roepen.

Dit lijkt heel makkelijk, maar valt in de praktijk vies tegen. Je moet ten eerste compleet anders denken. Verder moet je de databasetoegang zo schrijven dat een [SELECT](http://sqlobject.org/docs/SQLObject.html#selecting-multiple-objects) Deferreds teruggeeft en je daar in de rest van je applicatie mee uit de voeten kunt.

De documentatie [‘Using Deferreds’](http://twistedmatrix.com/documents/current/howto/defer) hielp me niet echt, maar [deze draad](http://twistedmatrix.com/pipermail/twisted-python/2004-August/thread.html#8493) uit de mailinglis wel.

Wat het niet makkelijker maakt is dat ze in Twisted ook een heldere scheiding van de verantwoordelijkheden hebben geïmplementeerd met [adaptatie](http://twistedmatrix.com/documents/current/howto/components) en aspecten. Dit is op het eerste gezicht niet superhelder maar belooft later wel veel ellende te besparen.