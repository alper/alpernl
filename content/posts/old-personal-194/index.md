---
title: "Onfunctioneel Python"
date: 2005-03-17T22:21:00
author: alper
categories:
  - nederlands
  - software-engineering
---

Leve het orakel, Guido [spreekt](http://lambda-the-ultimate.org/node/view/587). Hij wil map, filter en reduce verwijderen uit de taal. En als je hem naleest heeft hij hartstikke gelijk.

Wat heb je liever:

```
map(transfunc, reduce(filterfunc, list))
```

of:

```
[transfunc(el) for el in list if filterfunc(el)]
```

Ik weet het wel.

**Update:** Het eerste voorbeeld moet natuurlijk zijn

```
map(transfunc, filter(filterfunc, list))
```

Nuttige gebruiksmogelijkheden van [reduce](http://www.python.org/doc/current/lib/built-in-funcs.html#l2h-57) zijn sowieso ontzettend zeldzaam. Daarom alleen al mag die functie weg.