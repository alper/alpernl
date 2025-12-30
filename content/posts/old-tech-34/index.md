---
title: "XML Generator"
date: 2005-11-05T16:55:00
author: alper
categories:
  - english
  - software-engineering
---

XMLGenerator from [xml.sax.saxutils](http://docs.python.org/lib/module-xml.sax.saxutils.html) is a steaming piece of crap. It is  badly documented and it does not work. It does simple XML output just fine, but as soon as things become namespace aware I get Keyerrors which I cannot debug.

Example:

```
generator .startElementNS((ATOM_NAMESPACE, u'feed'), u'feed', AttributesNSImpl())
```

Luckily I have stumbled upon [JAXML](http://www.librelogiciel.com/software/jaxml/action_Presentation) which looks a lot friendlier to use.