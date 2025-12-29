---
title: "teach an old C new tricks"
date: 2005-03-11T22:02:00
author: alper
categories:
  - nederlands
---

Ik kom net op dit [artikel](http://www.chiark.greenend.org.uk/~sgtatham/coroutines.html) over Coroutines in C en het zit boordevol met lekkere low-level programmeer-juweeltjes. Dat alles om iets ontzettend handigs te implementeren: coroutines die ik het beste ken als Python-generators ([niet te verwarren](http://c2.com/cgi/wiki?GeneratorsAreNotCoroutines)).

Van een geniale onduidelijkheid is bijvoorbeeld Duff's device hieronder:


>
> switch (count % 8) {
>         case 0:        do {  *to = *from++;
>         case 7:              *to = *from++;
>         case 6:              *to = *from++;
>         case 5:              *to = *from++;
>         case 4:              *to = *from++;
>         case 3:              *to = *from++;
>         case 2:              *to = *from++;
>         case 1:              *to = *from++;
>                        } while ((count -= 8) > 0);
>     }
>

Daarna wordt het alleen maar erger. Uiteindelijk volgen er een bijzonder vies stel macro's die er met

GOTO

's en statische variabelen voor zorgen dat je na

return

door kunt gaan in die functie waar je was gebleven.

Ooit iemand C ouderwets horen noemen?