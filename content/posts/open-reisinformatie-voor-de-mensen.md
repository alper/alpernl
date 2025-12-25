---
author: alper
date: "2007-12-24T14:08:30+00:00"
guid: http://alper.nl/dingen/2007/12/open-reisinformatie-voor-de-mensen/
parent_post_id: null
post_id: "197"
tags:
  - openbaar-vervoer
  - overheid
  - trein
title: Open reisinformatie voor de mensen
url: /dingen/2007/12/open-reisinformatie-voor-de-mensen/

---
Ik zit al een tijdje na te denken over reisinformatie en het zou erg fijn zijn als die informatie makkelijk publiek beschikbaar zou zijn. Het is in het huidige klimaat kansloos en dat maakt het zo jammer want je zou er ontzettend veel handige dingen mee kunnen doen.

**Idee 1:** Een widget op je bureaublad met daarin altijd de volgende trein/bus/tram naar drie locaties waar je vaak heengaat. Een soort snelkoppelingen maar dan beter.
Het is een redelijk triviale applicatie, maar eentje die voor veel mensen nuttig kan zijn. Als de gegevens makkelijk beschikbaar waren, konden we honderden van dit soort tools maken ((Elke weer gesitueerd aan de specifieke wensen en eisen van een groep gebruikers.)).

**Idee 2:** De [OV-chipkaart](http://www.ov-chipkaart.nl/) gaat binnenkort al onze reisbewegingen vastleggen. Dit is [slecht](http://www.ov-chipklacht.nl/site/197/index.html) maar kan ook goed zijn. Die gegevens zijn van jezelf, privacy zegt dat ze niet met derden gedeeld mogen worden maar het is ook een fundamenteel recht om te kunnen beschikken over je eigen informatie. Wat zou je kunnen doen met deze informatie?
![OV Chipklacht](/dingen/wp-content/uploads/2007/12/header.gif)

1. Het CO2 verbruik van je vervoersbewegingen in kaart brengen en het verschil tonen met als je de auto had genomen.
1. Automatisch uitdraaien maken door een vertrouwde derde partij en die direct naar je werk laten sturen voor je reiskostenvergoeding.

Hoe? Een Atom gebaseerd API waar je toegang tot kun verlenen via een [OAuth](http://oauth.net/) endpoint. Erg simpel maar waarschijnlijk niet op de radar van de partij die dit ontwikkelt.

**Idee 3:**![Google Transit](/dingen/wp-content/uploads/2007/12/transit_labs_hp_logo.gif) [Google Transit](http://www.google.com/transit) is een uitbreiding op [Google Maps](http://maps.google.nl) die openbaar vervoersinformatie aanbiedt. Transit is nog experimenteel maar wordt [beter en beter](http://www.google.com/maps?f=d&hl=en&geocode=&time=5:15pm&date=12%2F7%2F07&ttype=dep&saddr=800+Bancroft+Way,+Berkeley,+CA+94710&daddr=5008+Telegraph+Ave,+Oakland,+CA+94609&sll=37.849239,-122.28384&sspn=0.062623,0.116386&dirflg=r&ie=UTF8&z=13&om=1&start=0) ((Let op de meerdere vervoersopties met kosten erbij en ook afgezet tegen de kosten van autorijden.)).
Google vraagt geen geld voor deze dienst. Als we dit in Nederland ook willen (en dat willen we), hoeven de vervoerders alleen maar hun gegevens in een standaard formaat aan Google aan te bieden.
Op dit moment piekeren vervoerders in Nederland hier niet over omdat ze de vervoersinformatie hebben ondergebracht bij [een monopolist](http://www.9292ov.nl). Het doel van OV9292 is om een minimale dienst aan te bieden en de gemaakte investering terug te verdienen.

Er gaat hier dus iets ernstig mis. Als burger betaal je dubbel voor openbaar vervoer: zowel in belastingen als voor je kaartje. Je zou zeggen dat vervoersinformatie bij openbaar vervoer hoort en dus ook al betaald is. Mensen die geen gebruik maken van openbaar vervoer hebben ook niks aan die informatie.

### Winstoogmerk

Dit begint op zich al met de privatisering van het openbaar vervoer maar werkt dus ook door op de vervoersinformatie. Vervoerders moeten geld verdienen, reisinformatie is een kostenpost. Investeringen moeten terugverdiend.

Aan de ene kant zou je het weggeven van reisinformatie kunnen goedpraten met het argument: hoe meer mensen weten van mogelijke vervoersopties, hoe groter de kans dat ze er gebruik van maken. Dus direct meer inkomsten voor de vervoerders.
Aan de andere kant zijn zowel goed openbaar vervoer als de bijbehorende goede reisinformatie voorwaarden voor het (economisch) verkeer in Nederland. Als marktpartijen hierinfalen, moet de overheid ingrijpen.

### Investeringen

De reisinformatiesystemen en de (verschrikkelijk slechte) sites die ze ontsluiten naar het publiek worden gebouwd door IT-leveranciers uit de markt. Dit zijn investeringen die de vervoerders moeten doen van de overheid. Zonder die dwang hadden we waarschijnlijk een situatie zoals in Duitsland waar elke lokale vervoerder zijn eigen (nog veel slechtere) site heeft en je geen binnengrens-overschrijdende ritten kunt plannen.

Deze investeringen worden aanbesteed naar preferred suppliers wat neerkomt op een hele beperkte groep gespecialiseerde of grote IT-bedrijven. Kleine bedrijven die het goed en goedkoop willen doen krijgen uiteraard geen kans omdat die een risico vormen ((Het nemen van risico's en zeker het nemen van risico's die op jezelf terug te voeren kunnen zijn staat niet hoog op de prioriteitenlijst van de aanbesteders. Het met bakken uitgeven van andermans geld is daarentegen geen enkel probleem.)). De bedrijven waarnaar wordt uitbesteed zijn op zich al niet goedkoop maar binnen kleine groepen gaan [prijzen vanzelf ook nog omhoog](http://en.wikipedia.org/wiki/Conscious_parallelism).

Dus als vervoerders het hebben over investeringen die terug verdiend moeten, dan gaat het om bedragen die hoger zijn dan nodig. Terugverdienmodellen zijn daardoor erg onrealistisch. Op een vraag van mij werd voor OV9292 een bedrag van €0,70 per aanvraag genoemd.

Realistischer zou zijn als de investeringen werden afgeschreven en er werd gekeken naar een actuele waarde van een systeem. Hardware (GPS, GSM) wordt exponentieel goedkoper en een website moet je in 2-3 jaar afschrijven tenzij je wil blijven zitten met heel oud spul.

### Kosten

Fair is wel dat de exploitatiekosten betaald moeten worden. Nu is dat probleem makkelijk opgelost door alle gegevens in Google Transit te stoppen zodat iedereen erbij kan en mensen die zinnige toepassingen bouwen te laten zorgen voor hun hosting. Dit is een klein en makkelijk op te lossen probleem.

### Conclusie

De gegevens zijn al betaald door elke inwoner van dit land.

Laat marktpartijen met deze gegevens innovatieve oplossingen bouwen waarmee ze waarde kunnen creëeren voor zichzelf en anderen. De huidige uitbaters gaan dat namelijk zeker niet doen.

De vervoerders zelf kunnen alleen maar meer (niet minder) klandizie krijgen bij het goed toegankelijk en verspreid zijn van hun informatie ((Dit lijkt de muziekdiscussie wel.)).
