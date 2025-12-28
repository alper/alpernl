---
author: alper
categories:
  - internet
  - monster-swell
  - nederlands
  - work
date: "2009-09-21T12:04:35+00:00"
title: Widgets overzicht
aliases:
  - /dingen/2009/05/widgets-overzicht/

---
Pas dus het project van een stel widgets voor het [Ministerie van Binnenlandse Zaken](http://www.minbzk.nl) afgerond. Hier een beschrijving per widget met afwegingen over de functionaliteit en de data. In een vervolgbericht wat algemenere projectnotities.

De widgets zelf met installatiecodes staan op [overheid20.nl](http://www.overheid20.nl/workspaces/index/72), de teksten staan gewoon in de beschrijvingen van de widgets en de code staat vrij te gebruiken op [github](http://github.com/alper/nlgovwidgets/tree/master).

### Zoekdienst Bekendmakingen

![](http://widgets.overheid20.nl/bekendmakingen/screenshot.png)

De overheid indexeert voor een hele reeks gemeenten en andere lokale instanties de bekendmakingen die ze publiceren [op overheid.nl](http://www.overheid.nl/overheidsinformatie/bekendmakingen). Dit is een flinke klus omdat elke instantie dit op een andere manier publiceert, maar het is ontzettend handig om op een simpele manier door deze dingen heen te kunnen zoeken.

De website oogt een beetje onvriendelijk maar is wel goed bruikbaar en er is [een zoekdienst](http://zoekdienst.overheid.nl/Zoekdienst/wizard.attenderingen.bekendmakingen/) waar je je kunt abonneren op bekendmakingen in jouw interesseprofiel bij jou in de buurt.

Deze zoekdienst en de bekendmakingen waar deze op gebouwd zijn bieden geen publieke herbruikbare data aan. Er wordt intern wel van enkele webservices gebruik gemaakt maar deze worden (nog) niet ontsloten naar buiten [^1]. Voor dit project konden we niet wachten tot er een API zou zijn omdat het bijzonder onvoorspelbaar is of en wanneer deze er dan is, dus hebben we maar iets gemaakt met wat er voorhanden was. [Vergunningenkaart](http://www.vergunningenkaart.nl/) is een site van geostart die wel toegang heeft tot de gegevens en geocodeert ze zelf en maakt ze weer beschikbaar.

Ik heb voor de widget alle gemeenten van [vergunningenkaart](http://www.vergunningenkaart.nl/) in één overzicht gestopt zodat je snel voor een bepaalde geeente kunt zien welke vergunningen er spelen. Dit is toegegeven een redelijk beperkt gebruiksdoel en in ons ontwerp hadden we ook voorzien dat het relevantste is om snel te kunnen zien wat er bij jou in de buurt nieuw is aan vergunningen [^2]. Zonder goede toegang tot de data is dit helaas niet realiseerbaar.

In Groot Britannië hebben ze de attenderingenservice van de zoekdienst bekendmakingen dus wel gerealiseerd met dat gebruiksdoel voor ogen maar dan niet in een widget maar via Twitter met [Twitterplan](http://twitterplan.co.uk/).

### Agenda van Werken bij de Overheid

![](http://widgets.overheid20.nl/agenda/screenshot.png)

Op Werken bij de Overheid is er ergens achteraf weggestopt [een agenda](http://www.werkenbijdeoverheid.nl/achtergronden/agenda/) met relevante evenementen voor mensen die een baan zoeken bij de overheid. De evenementen op die agenda hebben niet een eigen (landings)pagina, maar op ons verzoek is er door [Rhinofly](http://www.rhinofly.nl) een RSS feed van alle evenementent gemaakt op basis waarvan wij dan de widget konden maken.

Een agenda widget is fijn om te hebben precies omdat dit soort dingen vaak weggestopt worden en vaak op meerdere plaatsen relevant kunnen zijn. De uitvoer naar [ics](http://en.wikipedia.org/wiki/ICalendar) maakt het nog boeiender want uiteindelijk hoort agenda data thuis op de plaats die voor mensen het relevantste is: in de agenda. Het maken van een iCalendar uitvoerformaat was niet de opdracht (wij maken widgets) en uit de metadata in de RSS feed (naar voorbeeld van de RSS van Upcoming gemaakt) zou het niet al te moeilijk moeten zijn om een iCalendar te genereren maar er zijn geen standaard tools voor [^3].

### Rijksoverheidsvideo's

![](http://widgets.overheid20.nl/video/screenshot.png)

De [Rijksoverheid produceert video's](http://www.regering.nl/Actueel/Video_s) van bijzonder hoge kwaliteit in een verscheidenheid aan formaten en met volledig transcript, ondertiteling en noem maar op. Deze video's worden al verspreid naar de traditionele media maar gezien de hoeveelheid werk die erin gestopt wordt en de kwaliteit van het materiaal en metadata spreekt het voor zich om ze online ook verder te verspreiden.

Net zoals evenementengegevens thuishoren in de agenda, horen video's thuis op televisie of een andere player door middel van een podcast. Een [podcast RSS](http://www.apple.com/itunes/whatson/podcasts/specs.html) is een redelijk goed begrepen de facto standaard waarmee de gegevens handig af te spelen zijn en ook op andere manieren bruikbaar zijn.

In dit geval moest er een nieuwe RSS feed gespecificeerd worden waar daadwerkelijk verwijzingen naar de videobestanden in staan. Deze feed is nog niet af. De videowidget draait op een testfeed waar drie video's in staan en die nog geen koppeling met de echte data heeft.

### Waarschuwingen van de VWA

![](http://widgets.overheid20.nl/vwa/screenshot.png)

Een simpele nieuwswidget met daarin de meest recente waarschuwingen en terughaalacties van de [Voedsel en Warenauthoriteit](http://www.vwa.nl/). Van deze nieuwsberichten is er al een [RSS feed](http://www.vwa.nl/pls/feed/cne_content_syndication.feed?channel=10012&context=2001&flavor=rss20) op de site van de VWA te vinden. We hebben die simpelweg ingepakt op een prettige manier.

Het is technisch niet een hele complexe widget, maar de layout, huisstijl en de iconen om te differentieren tussen terughaalacties en waarschuwingen geven hier de meerwaarde die dit de moeite waard maakt.

### Vacatures van Werken bij de Overheid

![](http://widgets.overheid20.nl/vacatures/screenshot.png)

De vacatures van [Werken bij de Overheid](http://www.werkenbijdeoverheid.nl/) ( [RSS](http://www.werkenbijdeoverheid.nl/rss/)) zijn dat waar de meeste bezoekers van die website naar op zoek zijn —denken we. Dus iemand gaat naar Werken bij de Overheid om te zoeken naar een baan, vult op de voorpagina zijn eisen in en zoekt op die manier.

De widget die we hebben gemaakt biedt precies dezelfde zoekcriteria als op die pagina en laat altijd de laatste vacatures zien. Op die manier bespaart de widget iemand die een baan zoekt herhaaldelijke bezoeken naar de site. Qua personaliseerbaarheid en relevantie (voor een baanzoeker) lijkt deze widget me het meest geslaagd.

Voor zover een beschrijving per widget met afwegingen over de functionaliteit en de data. In een vervolgbericht wat meer over de projectbrede afwegingen.

[^1]: Er is misschien sprak dat er op de middellange termijn een publieke webservice komt, maar dat is nu nog niet duidelijk. Het is dan ook nog de vraag of die webservice SOAP of REST zal zijn. Voor ons op het open web is het een gelopen race maar grote bedrijven en overheidsorganisaties komen nu net kijken en aan hen wordt nog steeds SOAP verkocht als dé standaard. Waarschijnlijk blijven we op deze manier altijd achterlopen, maar SOAP is beter dan niks moeten je maar denken.
[^2]: Dat is op Vergunningenkaart ook niet zichtbaar en daardoor is het nut van die site wat ons betreft redelijk beperkt.
[^3]: Als iemand me de zin van [xCal](http://en.wikipedia.org/wiki/XCal) uit kan leggen, hoor ik het graag en ik had liever ook een [hCalendar](http://microformats.org/wiki/hcalendar) opgemaakte pagina gehad die met [X2V](http://suda.co.uk/projects/X2V/) over te zetten is.
