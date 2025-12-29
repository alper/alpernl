---
title: "Subversief"
date: 2005-04-04T23:06:00
author: alper
categories:
  - nederlands
---

Vandaag een partij GUI geschreven in [Java/Swing](http://java.sun.com/products/jfc/index.jsp). Jammer dat dat altijd zo'n ontzettende diarree aan code oplevert die veel minder doet dan je zou denken. Zonder Eclipse is er niet tegenop te vechten.

Het schijnt dat [Java/SWT](http://www.eclipse.org/swt/) minder erg is, maar ik hou mijn adem niet in. Vergeleken met Python of Haskell leveren de meeste programmeertalen overtollige code op.

De code die we geproduceerd hebben (een schamele 0.5 KLOC) wilde ik in een [subversion](http://subversion.tigris.org/) repository kwijt, dus heb ik er maar eentje opgezet. Het [opzetten van een repository](http://svnbook.red-bean.com/en/1.0/ch05.html) en het draaien van [svnserve](http://svnbook.red-bean.com/en/1.0/ch06s03.html) is net zoals alles in subversion helder en makkelijk.

Toen ook maar voor mijn Eclipse 3.1M5 een nieuwe versie van [subclipse](http://subclipse.tigris.org/) geïnstalleerd. Tot mijn verassing werkt het Team Synchronize een beetje. Het doet wat het moet doen maar het geeft wel foutmeldingen.

Ik heb even gezocht naar aanwijzingen dat het Eclipse-team subversion zou adopteren als de standaard voor Eclipse. Ik kwam [deze bug](https://bugs.eclipse.org/bugs/long_list.cgi?buglist=37154) tegen die twijfelend maar hoopvol is.

De moeite die het Eclipse-team moeten doen om CVS fatsoenlijk te ondersteunen was al gigantisch (lees ik). Daarom zijn ze waarschijnlijk huiverig om een tweede versiebeheersysteem ‘erbij te nemen.’ Ze laten subclipse extern rijpen maar ze zullen er niet omheen kunnen. Subversion is niet zomaar nog een versiebeheerpakket, het is de **vervanging** van het kapotte CVS.

Ik heb pas trouwens een project uitgecheckt uit een [darcs](http://abridgegame.org/darcs/)-repository. Hopeloos alternatief en weinig gebruikt, maar het werkt wel goed en er zit een solide idee achter.