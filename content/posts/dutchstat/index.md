---
_edit_last: "2"
author: alper
categories:
  - internet
  - monster-swell
  - nederlands
date: "2010-11-26T18:14:04+00:00"
guid: http://alper.nl/dingen/?p=1811
parent_post_id: null
post_id: "1811"
title: Dutchstats - Je persoonlijke atlas van Nederland
aliases:
  - /dingen/2010/05/dutchstat/

---
Release van [Dutchstats](http://bit.ly/dutchstats/) een online interactieve datavisualisatie van verkiezingsuitslagen en statistieken voor Nederlandse gemeenten door [Monster Swell](http://monsterswell.com) een Amsterdams datavisualisatie-bureau i.o.

### Wat?

 **[Dutchstats](http://bit.ly/dutchstats/)** — een applicatie om Nederlandse verkiezingsuitslagen en andere door het [CBS](http://www.cbs.nl/) gepubliceerde statistieken naast elkaar te kunnen bekijken.

[**http://bit.ly/dutchstats**](http://bit.ly/dutchstats)

 [![index.html](http://farm5.static.flickr.com/4009/4648817854_d7b2ffb62e.jpg)](http://www.flickr.com/photos/alper/4648817854/ "index.html by illustir, on Flickr")

Een video'tje:
[Dutchstats](http://vimeo.com/12122480) from [Alper Çugun](http://vimeo.com/illustir) on [Vimeo](http://vimeo.com).

### Wie?

Dutchstats is gemaakt door [Monster Swell](http://monsterswell.com/) met [Alper Cugun](http://twitter.com/alper/) en [Alexander Zeh](http://twitter.com/dmos/).

### Welke gegevens?

Het CBS stelt [Shapefiles beschikbaar](http://www.cbs.nl/nl-NL/menu/themas/dossiers/nederland-regionaal/publicaties/geografische-data/archief/2007/2006-wijk-en-buurtkaart.htm) met de grenzen van gemeentes, wijken en buurten. Hierbij hoort ook nog een [legenda van de bijgevoegde statistieken](http://www.cbs.nl/NR/rdonlyres/79BFE8EC-3328-463E-AED6-EB867CBC9307/0/2006b68pub.pdf). De tools die het CBS aanbiedt om met die gegevens om te gaan munten niet uit in gebruiksvriendelijkheid zie: [Statline](http://statline.cbs.nl/) of [CBS in uw buurt](http://www.cbsinuwbuurt.nl/#pageLocation=index).

De uitslagen voor de Europese Verkiezingen van 2009 van [nlverkiezingen.com](http://www.nlverkiezingen.com). De uitslagen van de Gemeenteraadsverkiezingen van 2010 zelf ingevoerd. De uitslagen van de Tweede Kamer-verkiezingen van de [Kiesraad](http://www.verkiezingsuitslagen.nl/).

### Waarom?

Dit is voortgekomen uit een onderzoek naar een makkelijke manier om gemeentegrenzen te tekenen en dat herbruikbaar te maken om willekeurige statistieken op weer te geven. Na wat [omzwervingen](/dingen/2010/03/municipal-boundaries-of-the-netherlands/) werkte er een proof of concept in [Processing](/dingen/2010/03/verkiezingsuitslagen-gevisualiseerd/), maar omdat dat lastig distribueert hebben we toen het geheel herschreven in [ProcessingJS](http://processingjs.org).

Een logisch vervolg was toen om in dit proof of concept de statistieken die er al in staan te visualiseren. Het resultaat is interessant.

### Wat is er zo boeiend?

Er zijn aan de hand van deze gegevens heel veel verhalen te vertellen. Het is de sociale geografie en de statistiek van het CBS direct tastbaar gemaakt met zo min mogelijk jargon en zonder specialistische gereedschappen.

Een paar interessante dingen:
[De decimering van VVD en PvdA door LPF in 2002](http://monsterswell.com/projects/dutchstats/#tk1998,tk2002) [Het verdwijnen van de LPF weer in 2003](http://monsterswell.com/projects/dutchstats/#tk2002,tk2003) [Locatie van de Bible Belt](http://monsterswell.com/projects/dutchstats/#ep2009,) [Aanwezigheid PVV vergeleken met hoeveelheid Niet-Westerse Allochtonen](http://monsterswell.com/projects/dutchstats/#ep2009,P_N_W_AL) [Gewassenbedrijven tegenover Veeteeltbedrijven](http://monsterswell.com/projects/dutchstats/#P_GEWASSEN,P_VEETEELT)

Maar er zitten nog veel meer interessante verhalen in deze cijfers en dat is ook wat het leuk maakt. Je kunt erdoorheen blijven klikken, vergelijken, veranderen en weer. Dat is wat ons betreft ook wat een goede datavisualisatie zou moeten doen.

### Hoe nu verder?

De broncode is nu al [beschikbaar op github](http://github.com/alper/dutchstats). Binnenkort volgt een open source release met nog wat nettere en gebruiksvriendelijkere code met een duidelijk integratie-punt voor ook niet-programmeurs.

Openstaande punten:

- De Shapefile en de bijbehorende CBS statistieken zijn uit 2006 Als het CBS een nieuwe versie wil uitbrengen zouden we dat op prijs stellen. [Albert de Klein attendeert](http://twitter.com/lbrt/status/14982142438) me op [een Shapefile uit 2009](http://www.cbs.nl/nl-NL/menu/themas/dossiers/nederland-regionaal/publicaties/geografische-data/archief/2010/2010-wijk-en-buurtkaart-2009.htm) die op de site staat maar die met geen mogelijk te vinden was voor mij. Ik zal de kaart binnenkort updaten met deze versie.
- Door gemeentelijke herindelingen gaat de visualisatie van verkiezingsuitslagen op een gegeven moment niet goed meer. Een goede Shapefile voor ieder jaar zou ideaal zijn. Als dat niet mogelijk is, dan is een andere strategie nodig om gemeentes historisch met elkaar te kunnen blijven vergelijken.
- De snelheid kan sterk verbeterd worden. Het is aan te raden om een laatste versie van Webkit of Chromium te gebruiken.
- Meer gegevens die op gemeenteniveau bekeken kunnen worden zijn altijd welkom. Eentje die we graag zouden zien is: rijksuitgaven per inwoner.
- Meer functionaliteit: grootste partij per gemeente is niet de beste manier om naar de uitslagen te kijken blijkt snel. Een uitbreiding om gemeentes aan te kunnen klikken en dan een detailweergave van de uitslag voor die gemeente te zien, ligt voor de hand.

### Links

 [VVOJ: Schatkamer vol verborgen leads](http://www.vvoj.nl/cms/archives/5869#more-5869) [Open Data Network: Hack de Overheid — Hackday in Holland](http://opendata-network.org/2010/05/hack-de-overheid-hackday-in-holland/) [Kennisland: Hacken voor de Goede Zaak](http://www.kennisland.nl/nl/filter/opinies/hacken-voor-de-goede-zaak)
