---
_wpas_done_all: "1"
author: alper
categories:
  - deutsch
  - english
  - software-engineering
date: "2024-12-29T09:05:47+00:00"
guid: https://alper.nl/dingen/?p=17823
parent_post_id: null
post_id: "17823"
title: ""
url: /dingen/2024/12/17823/

---
The Digital Patient Record system in Germany is built on smart cards and hardware which make it impossible to update and keep secure.

Of course a company like Gematik can't update algorithms and keys on such a widespread heterogenous system. This is a competency that is impossible to organise except at the largest scales and even then companies like Microsoft will routinely leak their root keys.

The ‘hackers’ who made this presentation also can't make something better than this and their culture is what led us to this point in the first place. It's the same story with the German digital ID card which nobody uses.

The recipe is simple:

- Demand absurd levels of security for threat models that are outlandish and paranoid
- Have those demands complicate your architecture with security measures that look good but are impossible to maintain
- Reap the exploits that you can run against that architecture and score publicity
- <repeat>

It's a great way to make sure that everybody loses in the German IT landscape.

Solution: Simplify the architecture to a server model with a normal 2FA login and keep that server secure. Done.

[https://www.golem.de/news/elektronische-patientenakte-so-laesst-sich-auf-die-epa-aller-versicherten-zugreifen-2412-192003.html](https://www.golem.de/news/elektronische-patientenakte-so-laesst-sich-auf-die-epa-aller-versicherten-zugreifen-2412-192003.html)
