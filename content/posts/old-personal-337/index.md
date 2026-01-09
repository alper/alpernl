---
title: "Goed op de rails"
date: 2005-07-18T20:32:00
author: alper
categories:
  - nederlands
  - software-engineering
---

Nu net [op Developerworks een artikel](http://www-128.ibm.com/developerworks/linux/library/wa-rubyonrails/?ca=dgr-lnxw07RubyAndJ2EE) waar denk ik redelijk wat behoefte aan is. Het legt in heldere, bewoordingen uit hoe een typische J2EE en een [Ruby on Rails](http://www.rubyonrails.org/) eruit zien en wat de verchillen zijn.

Dit is interessant voor Ruby mensen en J2EE mensen die geïnteresseerd zijn in elkaars eco-systemen. Maar ook de meer all round webontwikkelaar die een goed stuk gereedschap zoekt heeft er veel aan.

En de PHP-programmeurs —voor zover die zijn te helpen— hebben een kans om te ontsnappen uit [hun ghetto](http://blog.ianbicking.org/php-ghetto.html).

**Java**

De J2EE stack die ze gebruiken is heel typisch zoals die draait op de meeste [Tomcats](http://jakarta.apache.org/tomcat/) (of [Jetty](http://jetty.mortbay.org/jetty/)'s). Dit is niet  *echt* J2EE maar dat is niet zo erg. De meeste mensen zullen van hun leven toch geen missie kritieke volledig ge-load-balance'de op Oracle draaiende [JBoss](http://www.jboss.org/) applicatieservers met [JMX](http://java.sun.com/products/JavaManagement/), [JMS](http://java.sun.com/products/jms/) en nog wat andere J*-afkortingen ontwikkelen.

Rails krijgt in de Java wereld navolging met [Trails](https://trails.dev.java.net/). Trails gebruikt [Spring](http://www.springframework.org/) en [Tapestry](http://jakarta.apache.org/tapestry/) (allebei hele goede componenten) en werkt veel van de complexiteit weg onder de kap.

**Ruby**

Wat vooral opvalt is dat de hoeveelheid Ruby code die je moet schrijven voor een vergelijkbare applicatie ongeveer 1/6 tot 1/4 van de Java (en XML) code is. Het is ook niet zo gek dat een Ruby on Rails prototype in een kwestie van uren staat als een huis, terwijl je met Java nog bezig bent je verschillende tools te installeren en alle XML-bestanden goed te krijgen.

Een ander groot voordeel van zó weinig code gebruiken is dat je heel veel wint aan helderheid en onderhoudbaarheid. Minder code staat gelijk aan minder bugs.

**Python**

Het Python verhaal is wat moeilijker. Dit komt omdat het zo makkelijk is om in Python iets te maken dat ‘web’ doet. Iedereen kan het en daardoor is er een gigantische wildgroei aan *web frameworks* in Python. Veel van deze doen hetzelfde, een paar ervan doen compleet verschillende dingen.

Wat ik heb gedaan is kijken wat ik nodig had en kijken wat er op dit moment leefde. Uiteindelijk kwam ik daarmee op [SQLObject](http://sqlobject.org/), [CherryPy](http://www.cherrypy.org) en [Cheetah](http://www.cheetahtemplate.org/) uit.

Zelf mixen is dus goed haalbaar, maar ook bij Python zijn er mensen die de filosofie van Rails proberen over te nemen. De twee belangrijkste zijn [Subway](http://subway.python-hosting.com/) en [Django](http://www.djangoproject.com/). Django is pas uit en ziet er goed uit vooral omdat het al erg bewezen is. Lees het [stuk van Simon Willison](http://simon.incutio.com/archive/2005/07/17/django) maar en bekijk vooral het **[Game](http://www.ljworld.com/game/) voorbeeld (ontwikkeld in 2(!) dagen).