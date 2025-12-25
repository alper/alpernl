---
_edit_last: "2"
author: alper
date: "2008-01-09T08:53:30+00:00"
guid: http://alper.nl/dingen/2008/01/mifare-gekraakt/
parent_post_id: null
post_id: "220"
tags:
  - berlijn
  - computers
  - openbaar-vervoer
title: Mifare gekraakt
url: /dingen/2008/01/mifare-gekraakt/

---
Een [artikel in de Volkskrant](http://www.volkskrant.nl/economie/article492709.ece/Geheime_code_van_ov-kaart_ligt_op_straat) vandaag over hoe het algemene systeem van de OV-chipkaarten is gekraakt. Dit is aangekondigd door een groep hackers op de CCC in Berlijn tijdens hun presentatie: [Mifare: Little Security, Despite Obscurity](http://events.ccc.de/congress/2007/Fahrplan/track/Hacking/2378.en.html).

Het artikel in de VK laat niets doorschemeren van de techniek en het falen daarvan dus ik ga vanavond de presentatie bekijken om te zien wat er nu precies aan de hand is. Dan dus meer hierover.
Als dit inderdaad is wat het lijkt en wat Rop Gonggrijp gelijk heet met: ‘Deze chipkaarttechnologie is weg, stuk, niet meer te gebruiken.’ dan is het een belachelijke schande.

Ik [schreef al eerder](/dingen/2007/12/open-reisinformatie-voor-de-mensen/) over de extreem slechte aanbesteding van openbaar vervoer-projecten. Het is wel degelijk mogelijk om veilige systemen te maken. Eerlijkheid en openheid is een beginvoorwaarde voor veiligheid, als je aanbesteedt aan bedrijven die dat niet zijn, krijg je ook geen veilig product.

De OV-chipkaart werd al geplaagd door veel problemen. Het leek erop alsof er nergens regie was en dat niemand [het belang van de reizigers](http://www.ov-chipklacht.nl/) behartigde. Wat dat betreft is deze nekslag voor deze technologie een gelukkig ongeluk. Nu nog zien of er koppen gaan rollen.

**Update:** Ik heb de video nu gezien en respect voor de twee hackers (Karsten Nohl & Henryk Plötz). Met relatief goedkoop spul, een microscoop, [OpenPCD](http://www.openpcd.org/) en [OpenPICC](http://www.openpcd.org/openpicc.0.html) tools en veel trial and error, raadwerk naar de ontwerpbeslissingen en algoritmen die gebruikt worden, hebben ze de [Mifare Classic](http://en.wikipedia.org/wiki/Mifare) technologie zoals die in heel veel RFID-toepassingen gebruikt wordt compleet gekraakt ((Tijdens de presentatie wordt gemeldt dat als je Mifare gebruikt dat het verstandig is om weg te migreren naar een andere technologie. Even verderop zelfs dat Philips je vast wel wil helpen om hun geavanceerder (en dus) duurdere chips te gebruiken.)). Spoofen van UIDs met verschilende rechten, kraken van sleutels en semi-willekeurige starttoestanden, replays van transacties ((Oh, €5 bijschrijven op je OV-chipkaart? Één keer opnemen en afspelen zo vaak je wilt.)), alles is mogelijk en meer details worden nog gepubliceerd.
Mooie puzzel en leuke uitleg hoe dit in zijn werk gaat. Maar ga er maar aan om dit zelf te verzinnen.

Toegegeven zoals ook in de presentatie wordt genoemd, RFID-chips hebben beperkingen in stroom en ruimte/complexiteit. Het implementeren van een goed cryptografisch protocol in die beperkingen in betaalbare RFID-chips zoals de Mifare is erg moeilijk.
Phillips claimt dat wel te kunnen en biedt 'geavanceerde beveiliging' aan. De techniek die dit mogelijk maakt is op dit moment niet bekend in de academische wereld. Het is natuurlijk mogelijk dat Philips in-huis buitengewone technologische innovaties hier inzet, maar zoals blijkt is het tegenovergestelde waar. Ze hebben het eenvoudigste geïmplementeerd wat zou kunnen werken, zonder noemenswaardige veiligheidsmaatregelen behalve dan het geheimhouden van hoe het werkt.
In de academische wereld vindt op dit moment onderzoek plaats naar wat wel te implementeren is in de geldende beperkingen. Dit onderzoek vindt plaats in een open wetenschappelijk proces met _peer review_; bewezen de beste manier om te komen tot veilige systemen.

Een journaalitem dat online staat ((Is niet te permalinken.)) citeert [Rover](http://www.rover.nl/) dat staat te janken dat de persoonsgegevens op de chipkaart te kopiëren zouden zijn. Dat is het minst boeiend probleem. Rover zou moeten toejuichen dat openbaar vervoer binnenkort gratis kan zijn.
Translink en NXP doen alsof er niks aan de hand is (zie ook [Bright](http://www.bright.nl/gratis-reizen-door-hack-ov-kaart)) maar als je de presentatie bekijkt ((Hoeveel mensen hebben dat vandaag gedaan?)) blijkt dat Mifare compleet en totaal gekraakt is. Teletekst weet te melden dat TNO de veiligheid van de kaart gaat onderzoeken. Als ze die onderzoeken net zo goed doen ((TNO verricht onderzoek in opdracht. Het is alleen maar natuurlijk dat de uitkomst van het onderzoek onder druk komt door de belangen van de opdrachtgever.)) als ze de onderzoeken naar de veiligheid van stemcomputers gedaan hebben, dan staat ons nog wat te wachten.

**Update 2:** En [mijn reactie](http://sargasso.nl/archief/2008/01/08/wie-is-august-kerkhof/#comment-270799) op Sargasso.

**Update 3:** Ik luister naar [het item op Radio Online](http://www.radio-online.nl/pivot/entry.php?id=1356) met veel van hetzelfde met twee storende dingen:

GroenLinks (Duyvendak, OV-chipklacht) en vrienden (Rover) zeggen steeds dat strippenkaarten e.d. voldoen. Dit is een fijn staaltje achteruit denken en het klopt voor geen meter. Strippenkaarten zijn een idioot systeem ((Probeer het maar eens uit te leggen aan toeristen.)) en ik snap de combinatie van zones, starttarieven en strippen stempelen zelf nog steeds niet ((Mijn hersenen weigeren het. Ik overleef in het openbaar vervoer door chauffeurs en conducteurs te zeggen waar ik heen moet en hun te laten stempelen.)).
Verder slaat het nergens op dat ik als ik bijvoorbeeld naar [de Pilotenstraat](http://maps.google.nl/maps?f=q&hl=nl&geocode=&q=pilotenstraat,+amsterdam&sll=52.003031,4.352147&sspn=0.007054,0.01296&ie=UTF8&z=16&iwloc=addr&om=1) moet, ik een kaartje nodig heb voor de trein en een apart kaartje voor de metro ((Openbaar vervoer moet één ervaring zijn.)) en dat ik het niet van tevoren 's avonds online kan kopen ((Of ik moet stapels ongedateerde treinkaartjes en strippenkaarten bewaren, wat niet handig is en wat ik toch niet doe. Dus ik sta altijd 's ochtends te kutten bij kaartautomaten en gesloten kiosken.)).
Daar komt nog bij dat alle maatregelen die kaartjes in het OV beter zouden kunnen maken op de lange baan zijn geschoven met de belofte van de OV-chipkaart. De OV-chipkaart cancellen betekent een flinke innovatie-schuld op een andere manier moeten inlossen.
Er valt een eis dat een OV-systeem vrijwel waterdicht moet zijn (of temminste zo veilig als strippenkaarten dat nu zijn). Is deze hack niet een duidelijk bewijs dat het proces zoals het hier gehanteerd is, er niet in geslaagd is om te kiezen voor een veilig, open en toekomstbereid systeem en ook niet voor een systeem dat de behoeften van gebruikers voorop stelt. Wat gaat er veranderen in de besluitvormingstrajecten zodat dit niet meer gebeurt?
