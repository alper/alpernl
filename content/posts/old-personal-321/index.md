---
title: "Fragmentatie"
date: 2005-07-03T22:51:00
author: alper
categories:
  - nederlands
  - software-engineering
---

Het leven van de webontwikkelaar is de laatste tijd een stuk leuker. Het [AJAX](http://www.adaptivepath.com/publications/essays/archives/000385.php) neemt de boel compleet over en er zit schot in de ontwikkeling van de grote browsers, zowel in het voldoen aan standaarden als in nieuwe functionaliteit.

Er komt binnenkort een IE 7 die belooft veel verbeteringen wat betreft standaarden door te voeren. Eindelijk…

De andere browsermakers zijn daar over het algemeen al lang voorbij en hebben weinig zin om te wachten tot IE besluit mee te spelen. Zij gaan rustig door met nieuwe dingen ontwikkelen, zoals:

- ****[Ecmascript for XML (E4X):](http://www.ecma-international.org/publications/standards/Ecma-357.htm) Een manier om natuurlijker om te gaan met XML gegevens in JavaScript. XML verwerken voor gebruik in een webpagina is redelijk onaangenaam. Kijk alleen al naar het [whitespace probleem](http://www.mozilla.org/docs/dom/technote/whitespace/).

- ****[XForms:](http://www.w3.org/MarkUp/Forms/) zou ons van de huidige primitieve formulieren af moeten helpen en nog meer gave dingen.

Firefox Deer Park Alpha biedt hier ondersteuning voor. Je kunt XForms dan als extensie installeren.

- ****[SVG:](http://www.w3.org/TR/SVG/) Iedereens favoriete volgende generatie vector graphics standaard.

Opera 8 onderseunt het en huidige ontwikkelversies van Firefox ook.

- **<canvas>:** Dit staat in ieder geval in de voorstel specificatie [Web Applications 1.0](http://www.whatwg.org/specs/web-apps/current-work/) van de WhatWG. Het zou een makkelijk manier moeten bieden om bitmap plaatjes te tekenen in je webpagina. Ik heb het al eens geprobeerd met 640x480 <div>'jes maar dat is niet echt de manier.

Safari is begonnen dit te implementeren (vooral voor Dashboard) en Firefox heeft het overgenomen voor de volgende versie.

- ****[XUL:](http://www.mozilla.org/projects/xul/joy-of-xul.html) is de Mozilla manier voor het tekenen van GUIs (moet ik nog steeds een keer leren). Het bestaat al heel lang, en het wordt op best wel wat plaatsen gebruikt.

Firefox heeft dit dus al en er is nu [een project](http://developer.kde.org/summerofcode/xul.html) om Konqueror een complete XUL implementatie te geven. Dan zou Safari niet ver achterblijven.

Die volgende versie van Firefox, dat wordt me wat. Misschien zelfs wel een sterk argument om IE-ondersteuning weg te gooien en zulke stoere webpagina's te bouwen dat iedereen Firefox zal willen gaan gebruiken.

Microsoft gaat met XAML sommige van de bovenstaande functionaliteiten ook in IE inbouwen maar dat gaat dus anders werken. Het valt niet zo goed te rijmen met hun voornemen om standaarden te gaan volgen.

Groter probleem is dat dat weer gaat zorgen voor **fragmentatie** van de technologie en vooral van de ondersteuning. Als webontwikkelaar wil je met één stuk code zoveel mogelijk gebruikers raken. Daarom zit je vast aan een redelijke kleine en relatief achterhaalde grootste gemene deler. En dat wordt dan alleen maar erger.

Een mogelijke oplossing voor dit probleem is om bovenstaande componenten niet direct te gebruiken. Ze zijn allemaal nog niet overal bruikbaar. Er is een hoger niveau applicatie-programmeertaal nodig die onder de kap deze dingen gebruikt en waar niet beschikbaar ze emuleert of netjes weglaat. Dan kunnen we [zorgeloos programmeren](http://www.python.org) zonder al teveel energie kwijt te zijn aan [quirks](http://www.quirksmode.org).