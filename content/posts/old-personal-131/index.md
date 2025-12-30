---
title: "Domein Specifieke Talen"
date: 2005-01-19T23:43:00
author: alper
categories:
  - nederlands
  - delft
  - software-engineering
---

(Ik moet studeren maar dat boek over AI is echt te saai en slecht geschreven voor  woorden.)

Martijnv had tijdens het hardlopen een idee om DTD's en XML beter te benutten. Natuurlijk weinig op af te dingen.

Het hele XML is een rijke ecologie die met tooltjes vrij makkelijk aan elkaar te knopen is. Grote kracht, maar moeilijk in één keer te behapstukken.

Zoals waar wij nu mee bezig zijn om XML's te transformeren met behulp van XSL's kan je formaliseren van DTD -> DTD. Aangezien een valide XML een instantie is van een DTD is een XSLT op de DTD ook op de XML toe te passen. Simpel tot zover.

Waar ik de laatste tijd wat over hoor en wat ook de kant is die Martijnv op wil is het gebruik van XML in extreem-flexibele, domein-specifieke programmeertalen.

Extreem flexibel omdat de invoer een DTD-gebaseerde XML is en je dat met een XSL kun transformeren in een gevolg. Dit gevolg weer een DTD-gebaseerde XML waar je iets mee kunt. Dus misschien gebruiken om een pagina te tekenen, of een recept wat je in een agent kunt invoeren.

Het domein-specifieke zorgt ervoor dat de taal waarin je je probleem oplost heel eenvoudig is en alleen elementen bevat die wat te maken hebben met de problemen waar je mee bezig bent.

Complex is misschien beter dan ingewikkeld maar simpel is ook beter dan complex. Je kunt hier erg gave dingen mee doen maar fatsoenlijke ondersteuning door tools ontbreekt (nu) nog. De leercurve van dingen als XSL is vrij hoog en de belofte was nu juist om de dingen makkelijker te maken.

Daar komt nu misschien verandering in met de introductie van JSF. JSF gebruikt veel XML om de structuur en inhoud van een webapplicatie te specificeren. Dus navigatie van scherm naar scherm, en het tekenen van widgets. De belofte is dat je zo'n JSF-applicatie niet alleen direct op het web kan deployen maar dat je dezelfde object-boom ook kan publiceren als bijv. Swing-applicatie.

Bij JSF wordt ook goede ondersteuning door tools beloofd.

Een andere kant op is waar onder andere JetBrains (van IntelliJ IDEA) mee bezig schijnt te zijn. [MPS](http://www.codegeneration.net/tiki-read_article.php?articleId=60) (Meta Programming Systems) en DSL (Domain Specific Languages). Hun idee is om het heel makkelijk te maken om voor elk probleem een daarop toegespitste taal te creëren en met die taal het probleem snel op te lossen.

Microsoft zit hier natuurlijk ook bovenop. Visual Studio 2005 ‘Whidbey’ gaat er [ondersteuning](http://lab.msdn.microsoft.com/vs2005/teamsystem/workshop/dsltools/) voor bieden.

DSLs schijnen origineel bedacht te zijn in de FP (Functional Programming) gemeenschap (als [Combinators](http://www.cs.chalmers.se/~rjmh/Combinators/)) en het schijnt te maken te hebben met onder andere Monads (en hun opvolgers [Arrows](http://www.haskell.org/arrows/)). Ik heb Monaden nooit echt gesnapt maar ook nooit echt de tijd geïnvesteerd die daarvoor nodig is.

**Update:** Wat het gebruik van XML betreft, is dit [artikel](http://www.acmqueue.com/modules.php?name=Content&pa=showpage&pid=247&page=1) (*Extensible Programming for the 21st Century*) uit de ACM-queue een goed overzicht van de mogelijkheden.

Een een idee om een programmeertaal te maken die directere interactie met XML toestaat: [Cω](http://www.xml.com/lpt/a/2005/01/12/comega.html).