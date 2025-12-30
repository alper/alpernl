---
title: "Mark Nottingham - Web 2.0 On Speed"
date: 2006-05-17T14:40:00
author: alper
categories:
  - english
  - software-engineering
---

XTECH

Web caching

HTTP services

TOPdesk Enterprise cache-ing mogelijkheden

global audience

flexible scaling

ajax = more requests

more interactive

more dynamic

ASP = high reliability

Web 2.0 is more demanding than servers.

Three Tier architecture, LAMP PAID

custom code on the server

scaling means adding more servers, expensive

adding them on different locations to reduce latency

LAMP

P = slow 50-250 req/s

M = complex

A = 2-3000 req/s

L = ok

1. static content can be served much faster (duh)

2. it's easier to deploy a commodity box without application specific code

3. there are more clients than servers and they are idle most of the time

think outside of the box

1. highly scalable web servers

2. existing caching infrastructure

3. ajax magic on the client

caches in the network

Take processing offline and remove the bottleneck from the server.

C100k Apache is slow

Apache was not made for speed

Serious web servers use event loops

http://www.kegel.com/c10k.html

lighthttpd.net

30000 req/s

(But applications need to change to enable this. Base things on Twisted, adjust Servlet spec? ~Alper)

Leveraging the caching infrastructure

Freshness

'Expires'

'Cache-Control: max age'

QoS for caching

Validation

'Last-Modified', 'If-Modified-Since'

ETag, 'If-None-Match'

Invalidation by Side effect

POSTing to a page should invalidate its cache

Invalidation not supported by most browsers ('cept Safari)

Work-around: invalidate.js, rewrites URIs based on HTTP methods, stores state in cookies

Cache Targeting

Cache-Control: Private

(We can win a lot by caching just have to enable it by design. Nice URLs, use HTTP properly. Logging of profile information to be able to track down bottlenecks when they do occur. ~Alper)

Browsers misbehave pretty much

Basic validation + freshness supported well

Private caches work

http://mnot.net/blog

Developers use no-cache because they are scared of the cache.

Forwards compatible AJAX

Dynamic content can be cached (YES!, API's RSS etc.)

HTML Includes can make pages composable of different parts on the client and use appropriate cache levels for each part

hinclude.js

can specify default fallback content

Personalisation does not require server code

different modules are client based

Downgraded clients still need to be handled

Open Sourcec intermediary caches aren't as fast/functional as they could be

What else?

need to use this for services as well

More testing of behaviour

Distributing authentication

Offline operation