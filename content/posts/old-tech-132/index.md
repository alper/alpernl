---
title: "Frank Mantek - Google Data API"
date: 2006-05-17T16:50:00
author: alper
categories:
  - english
  - software-engineering
---

XTECH

ex Microsoft

currently working for Google

computers make things simpler so you can do stuff you like

Google has lots of APIs widely different

(WSDL?)

Use case:

simple data protocol

query!

update data

need RESTific design

easy to understand format, easy to consume (easy to produce?)

data format -> Syndication Atom 1.0 (let's forget about RSS ~Alper)

URL -> Atom feed of calendar data

namespaced extensions for semantic entitiies beyond the scope of Atom?RSS

google extensions have own namespace with types and kinds

semantical grouping of types

types can appear anywhere

do not have own semantic meanings



kinds

Contacts

Events

Messages

Entry with category of Event implies several types are either compulsory or optional

category URL query model

http://test.com/-/xtech/talks/2006?q=bla

parameter query model

q=

author=

updated-min=

updated-max=

gives you the entity

Updates based on APP (still in development)

Optimistic Concurrency

New entry: POST to sevice.post URI

DELETE to entries edit URI

PUT to entries edit URI

(hack to pass strange methods past firewalls)

1 property supporting GData more will follow

Active community at code.google.com

Libraries available for Java + C#

Shows C# code for reading and adding data to a Google calendar. Looks very clean but would prefer a JS implementation.

Shows OS X Dashboard Widget Google Calendar widget written in JS.

Uses programmatic Login, username, password returns token

Webservice authentication enables mashups

First step.

Questions: Javascript support? does that use sane JSON conversion?

Questoins: What does the C# update API do in case of conflict? Raise exception?

Question: Does Google Calendar use the API to get its data?

No, Calendar was made before API was thought of. Might switch later.

Question: Can we just forget about RSS?