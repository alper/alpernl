---
author: alper
categories:
  - internet
date: "2007-11-01T14:42:49+00:00"
guid: http://alper.nl/dingen/2007/10/hyves-zit-erop/
parent_post_id: null
post_id: "176"
tags:
  - internet
title: Hyves zit erop
aliases:
  - /dingen/2007/10/hyves-zit-erop/

---
Ik probeerde vandaag eens te kijken of ik voor een gegeven [Hyves](http://www.hyves.nl)-gebruiker zou kunnen achterhalen wie zijn vrienden zijn. Hyves-profielen en vriendenlijsten zijn te bekijken als je niet ingelogd bent. Daar wilde ik dus een scriptje voor schrijven, en als je dan heel Hyves afgaat kun je zo de complete sociale graaf ophalen ((Je zou denken dat dit niet mag, maar Google doet het ook en dan heet het indexeren voor zoektoepassingen.)), superhandig voor analyse en toepassingen ((Er zijn al mensen die [dit hebben verzonnen](http://wiki2.issuecrawler.net/twiki/bin/view/Dmi/AfstandTussenHyvesNetwerken) en stappen hebben genomen om [dit te realiseren](http://wiki2.issuecrawler.net/twiki/bin/view/Dmi/ScrapesterResearch#Sources).)).

Dus ik de code ingedoken om te kijken hoe dat in elkaar zit maar wat ik daar zag heeft me bang gemaakt. Een Hyves-gebruikerspagina laadt meerdere JavaScript-bibliotheken —Scriptaculous en YUI zag ik al, samen met wat zelfgeschreven spul— meerdere keren en deze doen allemaal rare dingen met de pagina. Geen wonder dat het zo ontzettend traag is.
Verder heb je de nare paginerings van de vriendenlijst waarvan de aanroep niet echt te vinden is. En dan bedoel ik niet _niet direct zichtbaar_, maar echt niet te vinden. In ieder geval als je met een kijkje onder de schermen met [Firebug](http://www.getfirebug.com/) er niet achter komt, dan zit het goed verstopt.

Het is een beetje de vraag of dit expres is gedaan ((De netwerk informatie op Hyves is hun grootste asset.)) of dat het uit willekeur zo gegroeid is. Ik denk een beetje van allebei. Ik heb vaker dit soort gegroeide HTML-bouwsels gezien en die dingen groeien en groeien maar uit noodzaak en op een gegeven moment valt het niet meer te onderhouden of nieuwe functionaliteit aan toe te voegen.

Als ik binnenkort wat meer tijd heb, zal ik kijken of ik er meer werk in kan steken. Hulp is welkom. Volgens mij is er een Python ((Of anderstalig.)) framework wat een complete browser simuleert om dit soort sites makkelijk te kunnen crawlen.

Ondertussen in ander nieuws: [Facebook groeit als kool](http://erwinboogert.jaiku.com/presence/16008301).
