---
author: alper
categories:
  - internet
  - monster-swell
  - nederlands
  - work
date: "2009-06-23T12:49:20+00:00"
title: Overheidsgegevens opener en vriendelijker
aliases:
  - /dingen/2009/06/overheidsgegevens-opener-en-vriendelijker/

---
Ik ben pas bezig geweest met verschillende overheidsinitiatieven om overheidsgegevens makkelijker toegankelijk te maken en te laten zien wat er mogelijk is als die gegevens toegankelijk zijn. Het idee is dat als de gegevens van de overheid open zijn, ontwikkelaars en andere partijen die kunnen hergebruiken en dingen kunnen maken waar andere mensen behoefte aan hebben. En dat zou weleens [handig kunnen zijn](http://www.datzouhandigzijn.nl).

[![Hack de Overheid](http://farm4.static.flickr.com/3602/3627750541_f855464ecd.jpg)](http://www.flickr.com/photos/silvertje/3627750541/ "Hack de Overheid by Anne Helmond, on Flickr")_foto door [Anne Helmond](http://www.annehelmond.nl/)_

Pas was er al [het widget-project](/dingen/2009/05/widgets-algemene-afwegingen/) wat een initiatief was gedacht vanuit het aanbod: ‘Wat hebben we waar we iets van kunnen maken?’

Parallel daaraan liep [Ton en James hun project](http://www.zylstra.org/blog/archives/2009/06/open_government_2.html) over aanbevelingen voor de publieke sector wat betreft het vrijgeven van data. Als onderdeel van dat project heb ik meegeholpen met een inventarisatie van de [al online beschikbare gegevensbronnen in Nederland](http://opendataoverheid.nl/3_Bronnen) en kijken welke gegevens we op een interessante manier zouden kunnen heraanbieden.

Dat viel nog redelijk tegen. Er zijn online wel veel gegevens beschikbaar maar meestal zitten ze in relatief ontoegankelijke formaten en zonder veel uitleg erbij wat het is en wat je ermee kunt. Uiteindelijk hebben we twee diensten gerealiseerd [Schoolvinder](http://www.schoolvinder.nl) en [Vervuilingsalarm](http://www.vervuilingsalarm.nl).

### Schoolvinder

 [![](http://aardverschuiving.com/image/schoolvinder.png)](http://aardverschuiving.com/portfolio#schoolvinder)

Zoals op [de over-pagina van Schoolvinder](http://www.schoolvinder.nl/over/) al staat hebben we de gegevens die bij het CFI al geregistreerd staan over scholen versimpeld aangeboden met een simpel zoekscherm wat aan zal sluiten bij de ideeën van de gemiddelde ouder.

Daarnaast doen we een poging om voor elke school in Nederland een canonieke URL —een basisbehoefte op het internet— te definieren waar je naar kunt refereren en waar je dingen bovenop kunt bouwen.

Dit is een probleem wat we bij de overheid vaker tegenkomen, dat webpagina's slecht samenwerken maar ook dat ze niet mooi zijn en vaak omkomen in jargon. Later hebben we van mensen van [MinOCW](http://www.minocw.nl) begrepen dat de CFI gegevens niet voor het bredere publiek bedoeld zijn en dat schoolgegevens ook op andere plaatsen (en dan vaak ook op andere aggregatieniveau's) bijgehouden worden.

Dat is misschien onhandig maar waarschijnlijk verklaarbaar waarom de gegevens dubbel bijgehouden worden maar dat de site voor werknemers bedoeld is doet er niks aan af dat hij moeilijk bruikbaar is. De herbruikbaarheid is redelijk ok —we hebben immers onze dienst er bovenop kunnen bouwen— maar het kan zeker veel beter.

En we hadden graag ook elke school gekoppeld met de database Onderwijs in Cijfers maar dat viel niet te realiseren omdat die webpagina's (onnodig) ver weg zijn weggestopt in een complexe ASP.NET omgeving.

### Vervuilingsalarm

 [![](http://aardverschuiving.com/image/vervuilingsalarm-1.png)](http://aardverschuiving.com/portfolio#vervuilingsalarm)

Bij [Vervuilingsalarm](http://www.vervuilingsalarm.nl/) hebben we de gegevens uit een webpagina van het [RIVM](http://www.rivm.nl/) geplukt. We denken dat de interesse voor dit soort gegevens uit de omgeving bij het publiek potentieel groot is maar dat het tot nu toe te weinig op een gebruiksvriendelijke manier wordt weergegeven.

Bij het RIVM staan wel veel bestanden online maar ik kan niet zeggen dat ze in de meest toegankelijke formaten beschikbaar zijn of dat ze gewone mensen in staat stellen hun leefomgeving door te lichten.

### Principes

De sites die we gemaakt hebben zijn vergevorderde prototypes die compleet bruikbaar en schaalbaar zijn. Bij het bouwen hebben we een paar principes gehanteerd die misschien interessant zijn om aan te stippen.

### Vriendelijk ontwerp

De sites hebben een mooi en vriendelijk ontwerp gemaakt door [Buro Pony](http://www.buropony.nl/). Dit is belangrijk omdat mensen een site die er mooi uitziet liever gebruiken en ervaren als gebruiksvriendelijker.

Bij dat mooi ontwerp hoort ook kopij met simpel en helder taalgebruik zonder jargon, die aansluit bij de belevingswereld van mensen.

De meeste websites kun je met deze twee verbeteringen al gigantisch vooruit helpen.

### Integratie met anderen

Beide websites integreren zonder al teveel problemen met een serie andere sites die het concept versterken. Het is gebouwd op [Google App Engine](http://code.google.com/appengine/) een systeem wat bijzonder schaalbaar en betrouwbaar is en zonder veel problemen worden kaarten opgehaald van [Google Maps](http://maps.google.com), grafieken van Google Charts en sensorgegevens worden doorgestuurd naar [Pachube](http://www.pachube.com)

Op het [Hack de Overheid](http://www.hackdeoverheid.nl) event zei iemand dat ‘het integreren van systemen moeilijk en complex is en dat als je dat goed kunt je er veel geld mee kunt verdienen’. Dit is een bekende algemene wijsheid in de enterprise IT maar als er één ding is wat de mashups die online normaal zijn bewijzen, is het dat integratie op het open web alles behalve moeilijk is.

Er zijn bruikbare API-standaarden met tooling [^1], daarnaast zijn er goede standaarden voor [identiteit](http://openid.net/) en [authenticatie](http://oauth.net/) [^2] en als je het jezelf niet te ingewikkeld maakt hoeft het echt niet moeilijk te zijn. En dit is niet nieuw ofzo, deze technologie bestaat al lang en bouwt gewoon door op wat het internet al goed doet.

### Standaarden gebaseerd

De sites die we gebouwd zijn zijn compleet op standaarden gebaseerd. Ik heb de pagina's als experiment geschreven in HTML5 (en [gevalideerd](http://html5.validator.nu/) [^3]) deels uit interesse en deels omdat ik van mening ben dat het nu gangbare XHTML een dood spoor is.

Verder heb ik waar ik het gepast vond ook gegevens (bijvoorbeeld de contactgegevens van de scholen) met [microformats](http://microformats.org) geannoteerd. Het idee dat microformats toevoegen aan een project significante extra tijd kost [^4] is wat mij betreft achterhaald en tegenwoordig is er een hard reëel voordeel aan te voeren.

Het kost even moeite om jezelf aan te leren om standaarden en microformats te gebruiken, maar als je het kunt is het bijna meer moeite om het niet te doen.

### Snel

Verder heb ik beide sites gebouwd in een tijdspanne van een paar dagen. Waarmee we wilden aangeven dat een snel project ook echt snel kan en dat het maken van een gebruiksvriendelijke niet-triviale site niet veel tijd en geld hoeft te kosten.

Het kan allemaal wél beter. Laten we het dus gaan doen.

[^1]:  [cURL](http://en.wikipedia.org/wiki/CURL) bijvoorbeeld
[^2]: En het is allemaal open waardoor één partij er niet een onevenredig belang bij heeft om het te controleren en complex te maken.
[^3]: Validatie zegt niet zoveel trouwens. Ik krijg vaak genoeg valide XHTML-code die compleet onsemantisch is.
[^4]: Opdrachtgever: “Ja, doe dat maar als je tijd over hebt.”
