---
title: "Tv-loos"
date: 2006-02-27T22:13:00
author: alper
categories:
  - nederlands
  - video
---

Het leven zonder televisie wordt steeds makkelijker. Lang verwacht, gesmeekt maar niet gelukt bij [Uitzendinggemist](http://www.uitzendinggemist.nl) komen er nu wel [Vodcasts bij Talpa](http://www.talpa.tv/web/show?id=271831) van BvD en NSE.

iTunes podcatcher functionaliteit is toch echt wel een hele makkelijke manier om dit soort episodische multimedia bij te houden. Het scheelt me een berg zoeken en downloaden, gaat allemaal automatisch en ik kan voortaan de boeiende stukjes van BVD terugkijken wanneer het *mij* uitkomt.

(En dan heb ik het er nog niet eens over als je forenst en een iPod Video hebt…)

Nu nog iets vergelijkbaars voor [NOVA](http://www.novatv.nl) en ik ben helemaal blij. Misschien ga ik dat binnenkort dan zelf schrijven met een sitescraper.

[[via](http://www.kennethverburg.nl/weblog/archives/2006/02/27/abonneer_je_op_talpas_bvd_en_nse_via_itunes.php)]

**Update:** Jan Mulder is nog steeds even vervelend.

**Update 2:**De URLs zijn van de hele eenvoudige vorm:

http://www.talpa.tv/web/show/id=46292/presentationid=271612/cachetimeout=300/output=vodcast/program=18

Het programma id is een simpel getal en dit komt overeen met de ids op “Programma gemist”. Barend en Van Dorp is bijvoorbeeld id 9:

[http://www.talpa.tv/web/show/id=47822/progid=9](http://www.talpa.tv/web/show/id=47822/progid=9)

Voor elk programma op programma gemist bestaat nu dus al een vodcast url (vul maar gewoon een andere id in en vraag het bestand op met [curl](http://curl.haxx.se/) ofzo) maar de meeste zijn gewoon leeg (zoals ook die van NSE).

Dit roept wel de vraag op of dit een pilot is en ze binnenkort de andere programma's ook aan gaan zetten.