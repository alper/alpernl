---
title: "All hail the holy snake"
date: 2004-12-04T23:00:00
author: alper
categories:
  - nederlands
  - software-engineering
---

[Python](http://www.python.org) is zoveel beter dan Java dat het gewoon niet leuk meer is. Ik dacht dat ik redelijk op de hoogte was van wat de taal allemaal kan maar ik ben een paar jaar geleden opgehouden de [nieuwsgroep](news://comp.lang.python) te volgen.
De taal is nog steeds volop in ontwikkeling, blijkt nu. Ik had vandaag een Wauw!-moment. Dit is net als een WTF-moment maar dan op een positieve manier.

[Via](http://simon.incutio.com/archive/2004/12/03/getters) kwam ik op dit [artikel](http://dirtsimple.org/2004/12/python-is-not-java.html). Het is een goede gids Python-idioom voor de Java-programmeur. Eigenlijk is het ons manifest dat dingen niet moeilijk hoeven en **wel** makkelijk kunnen. Dat minder regels code beter zijn omdat code vaker gelezen wordt dan geschreven. Dat programmeren leuk kan zijn.

Het Wauw komt door dit stuk code:

```
# test property

"""Eenvoudige klasse met 1 attribuut: size.

Toegang is eenvoudig en helder."""
class OldTest(object):
def __init__(self):
self.size = 0

ot = OldTest()
ot.size = 1
print ot.size

"""We willen achter de schermen toch een paar dingen afhandelen bij het opvragen van size
We refactoren dus de klasse om een nieuw attribuut __size te gebruiken om size in op
te slaan.
Met de property methode wordt het attribuut size bewaard en wordt toegang tot dat
attribuut doorgelust naar de juiste methoden.

De oude toegang werkt nog steeds en deze is dus nog steeds eenvoudig, helder en niet te
vergeten interface-compatibel met de vorige versie."""
class Test(object):
def getSize(self):
print "Get size called"
return self.__size

def setSize(self, size):
print "Set size called"
self.__size = size

size = property(getSize, setSize, None, "Size mutators")

t = Test()
t.size = 2
print ot.size
```

Het is een van de vele truucjes die Python door zijn dynamische aard toestaat. En die het programmeren leuk maken. Nog een voorbeeld is dit [recept](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/355045) ([via](http://lambda-the-ultimate.org/node/view/407)).

Het is zo ontzettend jammer dat Python niet op veel meer plaatsen gebruikt wordt. Gebrek aan gedrevenheid, vertrouwen en competentie van programmeurs samen met een flinke berg folklore en vooroordelen over scripttalen lijken me daar de oorzaak van.

Ze zijn er [wel](http://zope.freerecruiting.com/Resumes/JobOpennings/index.html).