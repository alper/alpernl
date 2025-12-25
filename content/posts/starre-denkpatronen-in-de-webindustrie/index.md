---
author: alper
categories:
  - internet
date: "2007-06-08T14:02:00+00:00"
tags:
  - computers
  - html
  - internet
title: Starre denkpatronen in de webindustrie
aliases:
  - /dingen/2007/06/starre-denkpatronen-in-de-webindustrie/

---
Een tijdje geleden praatten we met [wat verlichte zielen](http://www.happyclog.nl/) over de stand van webstandaarden in Nederland. We vonden dat daar verbetering in moest komen en we hebben allemaal wel ons best gedaan om mensen hiervan te overtuigen. Het lijkt er nu op dat de verbetering voor een deel is gerealiseerd maar dat sommige mensen wellicht zijn doorgeschoten.

Ik kom regelmatig webboeren tegen die valide XHTML 1.0 pagina's aan de man proberen te brengen met als argument dat dit het beste is wat er bestaat op het gebied van mooie onderhoudbare webpagina's.

Dit is pertinent onwaar. De voordelen van XHTML boven [HTML 4.01](http://www.w3.org/TR/html401/) zijn —als ze er al zijn— miniem. De genoemde voordelen schone semantische code en een scheiding van inhoud, presentatie en gedrag, kunnen net zo goed en tegen lagere kosten gerealiseerd worden met normale HTML.

Potentiele nadelen zijn er daarentegen genoeg. Hier wat voorbeelden.

### Futiele moeite

XHTML wordt door vrijwel geen enkele browser geïnterpreteerd als XHTML. Aangeraden wordt om vrijwel altijd je pagina's aan te bieden als mimetype `text/html`. Je XHTML code zal dan alsnog geïnterpreteerd worden als normale HTML. Dit doet de meeste voordelen die je dacht te hebben al teniet.

Je kunt beter HTML 4.01 schrijven wat net zo semantisch kan zijn, niet langzamer is en beter begrepen en ondersteund wordt.

### Draconische foutafhandeling

XHTML berust op een harde foutafhandeling om onvoorspelbaar gedrag te voorkomen. Het gevolg hiervan is dat als er een fout in een pagina mocht staan, de afhandeling stopt en de gebruiker geen pagina meer te zien krijgt maar alleen een foutmelding. In een internet dat grotendeels door mensen wordt geschreven en waar content van verschillende bronnen gehaald wordt, is het moeilijk om perfecte pagina's te garanderen.

Een [vergevingsgezinde parser](http://www.whatwg.org/specs/web-apps/current-work/#parsing) zoals bij HTML met heldere ((Temminste in het geval van HTML5.)) afspraken wat te doen bij fouten is handiger.

### Doodlopend pad

Er is geen helder migratiepad gedefinieerd van XHTML 1.0 naar XHTML 2.0 ((Het ontwikkelproces van deze standaarden bij de W3C is ook bijzonder gesloten waardoor veel moet worden gegist. Vergelijk dit met het proces van de WHATWG waar alles uit principe open is.)). De XHTML 2.0 specificatie bevat significante veranderingen ten opzichte van de vorige waardoor veel code handmatig zal moeten worden aangepast. Het gebrek aan visie in deze specificatie zadelt iedereen die meedoet met XHTML 1.0 op met significante kosten wanneer er moet worden overgegaan naar de volgende versie.

HTML 4.01 is goed begrepen en wijd ondersteund. Er is een duidelijk upgrade-pad naar [de HTML5 specificatie](http://www.whatwg.org/specs/web-apps/current-work/) die zowel _backwards compatible_ is met HTML 4.01 als een groot aantal nieuwe features bevat voor de toekomst.

### Conclusie

Het is op dit moment dus af te raden -zelfs schadelijk- om XHTML te gebruiken. Dezelfde voordelen kun je met een veel groter gemak bereiken door het eenvoudige ouwe semantische (( [">Plain Old Semantic HTML](http://microformats.org/wiki/posh))) HTML 4.01 te gebruiken ((Voor een goede bespreking van de kwesties rondom XHTML, waar ik voor dit stuk ook veel inspiratie uit geput heb, zie [deze pagina](http://www.webdevout.net/articles/beware-of-xhtml#benefits) met alle feiten op een rijtje. In het onderzoeken voor dit stukje kwam ik ook dit [stukje van hjdeboer.nl](http://hjdeboer.nl/archives/2006/02/html5) tegen die het ook begrepen heeft.)).

Ik pleit ervoor dat we niet alleen pleiten vóór webstandaarden maar tegelijkertijd ook voor een flexibelere manier van denken en een kritische houding ten opzichte van alles ((In het bijzonder voor je eigen denkpatronen.)). Ik kom ((In de ICT lijkt rigide denken en folklore nog sterker vertegenwoordigd dan elders.)) teveel mensen tegen die na enige deliberatie een standpunt accepteren en er dan niet meer aan twijfelen maar het uitdragen als een soort gospel.

Continue kritiek van alles is noodzakelijk. Wat vandaag waar is, hoeft dat morgen niet meer te zijn. XHTML lijkt op dit moment dood, maar HTML5 biedt een serialisatie naar XML wat mogelijkheden biedt voor de toekomst ((De gasten van de WHATWG zijn serieus slim.)).

Je wereld kan veranderen. Het zou jammer zijn als je daar zelf als laatste achter kwam.

**Update:** Ik denk dat ik hier nog wat aan ga schaven en het dan op [Frankwatching](http://www.frankwatching.com) zet.
