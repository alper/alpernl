---
author: alper
categories:
  - internet
date: "2007-08-17T16:23:07+00:00"
guid: http://alper.nl/dingen/2007/08/havatar-voor-wordpress/
parent_post_id: null
post_id: "113"
tags:
  - computers
  - internet
title: hAvatar voor Wordpress
url: /dingen/2007/08/havatar-voor-wordpress/

---
Ik had het al een tijdje gehad met [gravatar](http://www.gravatar.com/) en alle andere verschillende manieren om avatars ((Plaatjes van gebruikers.)) toe te voegen aan blogs en vond tijd dat er een simpele open versie kwam.

Ik heb net de MyAvatar plugin aangepast tot wat uiteindelijk de hAvatar plugin moet worden. Je ziet hem nu in actie bij de commentaren op dit blog. Als jij een [hCard](http://microformats.org/wiki/hcard) met photo of logo eigenschap op je URL hebt staan ((Je Flickr profielpagina bevat bijvoorbeeld een hCard net zoals een heleboel andere plaatsen.)) die je achterlaat, dan haal ik die op en toon hem als je avatar.

Aardig proof of concept ((En geïmplementeerd op dit blog, omdat hier een stuk minder mensen boos worden als ik de boel sloop.)), en ik denk wel het uitbreiden waard. Probeer het maar uit. Je kunt een pagina gebruiken met een hCard of je kunt hier inloggen met OpenID en zorgen dat op je OpenID site een hCard staat zoals beschreven in [mijn artikel op Four Starters](http://fourstarters.com/2007/05/21/openavatar-combining-openid-and-hcard/).

Deze versie gebruikt nog mijn hAvatar parse dienst zoals beschreven op Four Starters maar een definitievere versie moet [hKit](http://allinthehead.com/hkit/) gebruiken om de hCard te parsen.

De recente commentaren op de voorpagina gebruiken nog gravatar zoals opgeleverd door de thema-bouwer, maar dat is zulke afgrijselijke PHP-code, dat de revisie daarvan niet op een luie zondagavond kan.
