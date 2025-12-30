---
title: "C-hekje"
date: 2005-02-12T16:52:00
author: alper
categories:
  - nederlands
  - delft
  - software-engineering
---

Deze post is een beetje lang geworden, maar ik denk wel de moeite waard. Dus als je feedback hebt, reageer dan alsjeblieft.

Ik ben deze week begonnen aan het MKT-5 project. Dit is het ontwerp en de implementatie van een multimodale applicatie. Dat betekent zoveel als dat de applicatie spraak herkent en uitvoert en dus communiceert met een wat menselijkere dialoogvorm.

De groep heeft in mijn afwezigheid meteen maar besloten om het geheel te gaan schrijven in [C#](http://msdn.microsoft.com/vcsharp/) samen met de [Microsoft Speech SDK](http://www.microsoft.com/speech/). Niet direct mijn eerste keuze maar ik kan ermee leven. Geeft het me meteen de ‘kans’ om deze nieuwe taal te leren kennen. Erg veel van Java verschilt het niet dus in een dagje had ik het meeste wel onder de knie.

Mijn eerste indruk is dat C# frisser aanvoelt dan Java maar dat Microsoft elke kans aangrijpt om dingen te verdraaien en af te snijden. Microsoft-programmeurs hebben natuurlijk schijt aan alles wat netjes en *comme il faut* is. Terminologie is anders, bepaalde dingen werken net anders; en ook leuk zijn de naamgevingsconventies voor bijv. methoden.  In C# beginnen ze met een hoofdletter, dus [ToString()](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/cpref/html/frlrfsystemobjectclasstostringtopic.asp) in plaats van [toString()](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Object.html#toString()).

De taal is beter dan Java maar niet zoveel beter dat een nieuwe taal gerechtvaardigd is. De rechtvaardiging van de taal is natuurlijk ook niet de (beloofde) verbetering, maar de platform-oorlog.

Ondertussen is het meeste van C# nagebouwd onder Linux in de vorm van [Mono](http://www.mono-project.com/about/index.html). Hierdoor mag Microsoft best de platform-oorlog winnen en zit je dan nog steeds niet vast aan Windows. Al je applicaties draaien dan ook nog prima onder Linux, OS X en noem maar op.

Microsoft doet alsof het ze niet kan schelen. Ze hebben van C# een [ECMA-standaard](http://www.ecma-international.org/publications/standards/Ecma-334.htm) gemaakt en ze beloven wat interoperabiliteit betreft lief samen te zullen spelen. Maar het zal ze niet in de koude kleren zitten.

C# wordt onder Linux veel harder geadopteerd dan Java ooit. Mijn muziekspeler [Muine](http://muine.gooeylinux.org/) is hier een goed voorbeeld van maar [Beagle](http://www.gnome.org/projects/beagle/) wordt bijvoorbeeld ook in C# geschreven. Het is hard op weg om de voorkeursprogrammeertaal van Gnome te worden.
Dit komt niet alleen omdat het een lekker vlotte programmeertaal is. Belangrijker is dat het een complete open implementatie betreft zonder [rare clausules](http://www.zdnet.com.au/news/software/0,2000061733,39149502,00.htm).

Mono werkt prima. Ik gebruik het om de software die we op de TU schrijven hier onder Linux te draaien. Het enige probleem dat ik had was het ontbreken van generics ondersteuning in [mcs](http://www.go-mono.com/c-sharp.html) maar daarover zodirect meer.

De CLR ([Common Language Runtime](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/cpguide/html/cpconthecommonlanguageruntime.asp)) is omdat het bij bovenstaande hoort ook erg veelbelovend. Er is aardig wat beweging om het te gebruiken als doel-VM. De Python implementatie hierop —[IronPython](http://www.ironpython.com/)— schijnt gaaf te zijn en 1.7x keer sneller dan de standaard CPython implementatie.

Kortom: We kunnen er niet echt omheen C#.NET is **sexy**.

Ik was dus wat C# code aan het schrijven en ik dacht elite te zijn door generics te gaan gebruiken. Ik dacht altijd dat Java5 ze had ingevoerd als reactie op C#.
Mijn mcs gaf een minder dan behulpzame foutmelding op mijn:


private ArrayList<Travel> travels;


Na wat uitzoeken kwam ik erachter dat ze bij Ximian hard aan het werk zijn aan gmcs, een C#-compiler met ondersteuning voor generics. De C#-versie die we op de TU gebruiken kan het ook niet omdat Microsoft ook nog niet zo ver is.

Een beetje een verassing dat Microsoft dus echt alles heeft gekopieerd van Java, ook JSR's die al jarenlang lagen te rijpen in de [Java Community Proces](http://www.jcp.org/en/home/index). De [JSR voor generics](http://www.jcp.org/aboutJava/communityprocess/review/jsr014/) is uit 2001.

En een verassing dat Java voor loopt op C#. Je gaat toch harder lopen van zo'n hete adem.

Wat wel erg jammer is —als je Eclipse gewend bent— is de tool die je van Microsoft krijgt om C# in te schrijven. [Visual Studio.NET](http://msdn.microsoft.com/vstudio/) kan niet tippen aan [Eclipse](http://www.eclipse.org/). De ondersteuning die Eclipse standaard biedt voor Java moet je er (naar het schijnt) stukje bij beetje bijkopen voor Visual Studio.

Ik ben hele geavanceerde features gewend zoals, auto-complete, source code refactoring, code-wizards/templates/generatie en ga maar door. Om niet te noemen wat je met Eclipse kunt als je een handjevol van de gratis [plugins](http://www.eclipse-plugins.info/eclipse/plugins.jsp) installeert. Ik ga de C#-plugin uitproberen.

Je zou denken dat een bedrijf zo groot als Microsoft met iets beters op de proppen zou kunnen komen. IBM heeft bakken vol met geld gestoken in de ontwikeling van [Eclipse](http://www.eclipse.org/org/). Je zou zeggen dat Microsoft ook niet bepaald arm is.

Ik weet nu meer maar ik heb nog steeds vragen. Ik vraag me bijvoorbeeld af wat voor VM de CLR is. Daar heb ik maar een specificatie van de IL voor gedownload.

En een andere vraag waar ik mee zit is het Microsoft voorstel voor de server, zeg maar ASP.NET.

JavaServer (niet speciaal J2EE) is ontzettend volwassen, krachtig en veelgebruikt overal waar een PHP-speelgoedoplossing het niet meer trekt. Denk maar aan de erg goede Java multi threading ondersteuning en de bergen frameworks en tools die er zijn. Ik zag dus laatst [een filmpje](http://www.jroller.com/page/ccnelson/20050208#i_got_the_video_done) waarin iemand in 11 minuten een applicatie kluste.

Ik weet niet precies wat Microsoft op dit gebied te bieden heeft maar als ik een beetje kijk naar wat ik zie bij C# en dat extrapoleer zal het waarschijnlijk een enkelzijdige oplossing zijn die erg schraal is.

**Update:** De meeste Java-mensen die ik vertel dat er nog geen *generics* zitten in C#, zijn daar verbaasd over. Dat is heel raar. Sun had een persbericht moeten uitbrengen waarin iets staat als: *‘wij hebben lekker iets (generics) wat zij (C#) niet hebben.’*

Het is misschien een simpele boodschap maar simpele soundbytes worden onthouden en *If you're explaining you're losing.*