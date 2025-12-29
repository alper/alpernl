---
title: "Vet aapje"
date: 2005-03-12T18:14:00
author: alper
categories:
  - nederlands
---

Stel: je kijkt weleens op de site van de [Duwo](http://www.duwo.nl) naar [actuele instemmingen](http://www.duwo.nl/aanbod/layout/Aanbod.cfm?NodeID=3).

En stel: je ergert je ontzettend aan al die instemmingen voor onderhuur die niet makkelijk uit elkaar te houden zijn van echte instemmingen.

En stel: je bent een nerd.

Wat doe je dan?

Je installeert [Greasemonkey](http://greasemonkey.mozdev.org/). Dit is een coole tool voor [Firefox](http://www.getfirefox.com) waarmee je  aan specifieke pagina's alles kunt aanpassen. Dit alles met een klein beetje Javascript, XPath en DOM.

En dan schrijf je [duwoOnderhuur.user.js](http://www.alper.nl/ajax/duwoOnderhuur.user.js) die alle tekst waar het woord 'Onderhuur' of 'Onderhuurder' ofzo in voorkomt een roze achtergrond geeft.

Dit soort scripts —er zijn nog een berg andere handige— moet eindigen op .user.js. Dan kan je ze openen en installeren met *Tools -> Install User Script*.

De [mozilla XPath gids](http://www-jcsu.jesus.cam.ac.uk/~jg307/mozilla/xpath-tutorial.html) wil nog weleens handig zijn als je zelf een script wil schrijven.

Let op: de simple manier van doorlopen met iterateNext() gaat fout omdat door wijzigingen in de boom de iteratorState invalid raakt. Dus het moet zoals het staat in mijn script of bij de [berg voorbeelden](http://dunck.us/collab/GreaseMonkeyUserScripts).

Volgend project: alle verstopte asf, mov en rm op pagina's klikbaar maken. Plugins werken onder Linux niet zo goed.