---
title: "phpMyAdmin also stinks"
date: 2007-01-10T14:53:00
author: alper
categories:
  - english
  - software-engineering
---

I am trying to import a database to the [MAMP](http://www.mamp.info/) install on my Macbook using phpMyAdmin's import tool. Trying to do this yields:

SQL query:

```
-- MySQL dump 10.10

--

-- Host: localhost Database: drupal

-- ------------------------------------------------------

-- Server version	5.0.24a-Debian_3-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
```

MySQL said:

```
#1065 - Query was empty
```

This message is utterly useless. Googling around a bit did not yield a direct answer (that's why I'm blogging this) but it did point me in the right direction.

It seems that PHP has a set maximum for uploads. If you go over that, you get the useful help message above. PHP also has maxima for runtime memory and the likes, going over any of these limits results in truly obtuse errors which are near impossible to debug.

PHP is a ghetto.