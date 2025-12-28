---
author: alper
categories:
  - internet
  - nederlands
  - product-design
  - reading
  - the-city
date: "2010-06-22T07:04:24+00:00"
title: "Check in / Check Out, Case by Case — Case 0001, 'Pasjes en poortjes'"
aliases:
  - /dingen/2010/06/check-in-check-out-case-by-case-—-case-0001-“pasjes-en-poortjes”/

---
Ik ben [het boek](http://rathenauinstituut.nl/en/themes/project/digitalisering-van-de-openbare-ruimte-1.html) [“Check in / Check out”](http://www.naipublishers.nl/checkin_checkuit/index.html) van [het Rathenau Instituut](http://rathenauinstituut.nl/) aan het lezen.

Het boek gaat over de digitalisering van de openbare ruimte en welke gevolgen dat heeft voor de privacy van de Nederlanders. Het boek is opgebouwd uit een serie cases en die zal ik hier één voor één lezen en mijn opmerkingen plaatsen.

### Case 0001 — “Pasjes en poortjes”

Er worden zes doelstellingen genoemd ‘van de vervoerder en technologie-aanbieders’:

> 1\. eerlijke en actuele verrekenening van kosten en opbrengsten
> 2\. betere managementinformatie
> 3\. tariefdifferentiatie
> 4\. betere sociale veiligheid
> 5\. betaalgemak voor de klant
> 6\. mogelijkheden voor aanvullende diensten (p. 42)

In dat rijtje mis ik een zevende doelstelling die je uiteraard niet zult horen van de vervoerders en ook niet van de technologie-aanbieders die door hen zijn opgezet:
7\. Het openbreken van de markt door betalingen te standaardiseren en de betalingsfrictie weg te nemen en zo concurrentie in het (openbaar) vervoer te vergemakkelijken.

Elke andere aanbieder van vervoer heeft het probleem dat potentiele reizigers erachter moeten komen 1. wanneer ze dat middel kunnen gebruiken en 2. hoe ze daar dan voor kunnen betalen. Het standaardiseren van de informatie in het [NDOV](/dingen/index.php?s=ndov) en de betaling in de ov-chipkaart en beide middelen laagdrempelig inplugbaar maken voor meer partijen kan leiden tot een dynamischer systeem van [Transmobiliteit](http://speedbird.wordpress.com/2010/05/01/transmobility-part-i/).

> Opvallend weinig mensen blijken zich zorgen te maken over het gebruik van hun persoonsgegevens. (p. 49)

Als mensen zich geen zorgen maken is er voor een groot deel ook geen probleem. Privacy is voor een groot deel een kwestie van perceptie.

> De vervoeraanbieder heeft echter geen live-informatie over de reizigerstromen. (p. 57)

Hier komen we straks ook op. Er is dus een systeem dat periodiek informatie doorstuurt. Raar in deze netwerksamenleving en ook niet nodig. Volgens mij zitten er in de meeste message queue systemen robuuste functionaliteit om berichten over het netwerk te sturen en bij netwerkfalen ze lokaal op te slaan tot ze wel verstuurd kunnen worden.

> Reizigersinformatie kan worden gebruikt voor opsporingsdoeleinden en marketing, maar blijkt van beperkte waarde. (p. 58)

Dit is interessant maar het is de vraag of je deze gegevens dan maar niet moet opslaan, met name omdat de gegevens voor de gebruikers ook van waarde kunnen zijn. Een anonieme kaart die niet inferieur is aan de persoonsgebonden kaart lijkt het beste alternatief voor diegenen die hun privacy willen behouden.

Daarnaast is er ook een referentie naar de [Digital Security Group](http://www.ru.nl/ds/) (DSG) van Bart Jacobs die met financiele steun van NLnet werkt aan een OV-chipkaart 2.0 (p. 60). Iets wat hard nodig blijkt.

> RET en GVB zijn daarom van plan abonnementhouders die niet hebben ingecheckt, bij controle te beboeten met 35 euro voor het niet hebben van een geldig vervoersbewijs. Los van het feit dat dit onsympathiek overkomt, is nog onduidelijk of dit juridisch wel kan. (p. 61)

Bovenstaande laat zien hoe technocratisch de bestuurders van de vervoersmaatschappijen denken.

Ik mis deze vraag in de privacy-afweging van de ov-chipkaart: Worden contacten met de conducteur zoals controles en boetes ook vastgelegd in het systeem? Bouw je zo een strafblad op en wat voor gevolgen heeft dat?

> Deze zogenaamde location based services heeft de staatssecretaris vooralsnog verboden. (p. 67)

De location based services hierboven worden alleen maar gezien in het kader van de broodjesverkoper die je korting wil geven als je op hetzelfde station bent. De aloude natte droom van de marketeers.

Wat niet mee wordt genomen is de opkomst van locatie-gebaseerde diensten die door mensen zelf worden gebruikt om hun leven vast te leggen en om meer context toe te kennen aan hun dagelijks handelen. [Locatie gebaseerde spellen](http://www.chromaroma.com/), [locatie brokers](http://fireeagle.yahoo.net/) en andere interessante dingen die je zelf met je locatie kunt doen, kunnen heel waardevol zijn maar zijn niet in het systeem of in de afweging meegenomen (en worden ook vermoeilijkt doordat het systeem niet real-time is).

> Naar onze mening is het systeem vooralsnog teveel vanuit de vervoerders aan de reizigers opgelegd en zal dat het systeem op de lange termijn opbreken. Dit net neemt - zonder veel terug te geven.
> Inzicht in transactie via [mijnovchipkaart.nl](http://www.ov-chipkaart.nl/) kwam pas lang nadat het systeem al was in gevoerd (En is traag en vaak stuk. -Alper). De NDOV (Nationale Database Openbaar Vervoersgegevens), die ook de bewegingen van de voertuigen inzichtelijk zou moeten maken, laat nog lang op zich wachten. Een best pricing system is ooit overwogen, maar nooit ingevoerd. Het enige voordeel is vooralsnog betaalgemak, al zal niet elke reiziger de nieuwe manier van betalen echt handiger vinden. (p.68)

Gemiste kansen en het compleet negeren van de eindgebruiker is in het kort het verhaal van de OV-chipkaart.

> Maak duidelijk wie de reizigersidentiteiten beheert en dat ook degenen die kijken worden gecontroleerd.

Hier zou het bijvoorbeeld interessant kunnen zijn om elke toegang tot je gegevens ook op mijnovchipkaart.nl weer te geven. Ge-anonimiseerd qua naam maar niet qua functie zodat je kunt zien wie in welke rol wanneer welke gegevens van jou bekeken heeft.

> Zoek oplossingen voor systeemfalen in het systeem zelf en niet in het bestraffen van reizigers.

Zomaar een idee.

> Overweeg een ‘live’-scenario.
> De reizigersdata worden momenteel gebufferd en zijn daardoor altijd verouderd.

Gek dat we net nu we aanstalten maken om het real-time internet in te gaan, zitten met een systeem waar alle transacties gespooled worden in buffers van soms wel meerdere dagen. Heb je zo'n gigantische infrastructuur geïnstalleerd, is nog alle sturing die je kunt plegen en al het inzicht dat je kunt bieden belegen omdat de gegevens verouderd zijn voordat je ze ziet.

Al met al een goed historisch overzicht van de implementatie van de ov-chipkaart, de controlerende mogelijkheden en de kansen voor de gebruikers.

De vraag is alleen of en wanneer deze dingen verbeterd zullen worden. Er zijn al [meerdere fora](http://nsforum.uservoice.com/pages/30994-ikchip-ns-reizigersforum) geweest waar gebruikers hun problemen met de chipkaart mochten aankaarten. Hier en daar zijn er wel dingen verbeterd maar vaak word je gewezen op systeembeperkingen of onderlinge afspraken waardoor dingen niet mogelijk zouden zijn.
