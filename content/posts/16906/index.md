---
author: alper
categories:
  - english
  - software-engineering
date: "2022-12-27T13:01:42+00:00"
title: ""
aliases:
  - /dingen/2022/12/16906/

---
Looks like we can bootstrap a web app using pretty much only Postgres for the data layer and kick out the redis cluster, the celery process and the ElasticSearch server.

That makes an early stage project incredibly lean and with some care and feeding this setup will likely go _very_ far before it needs to be overhauled.

[https://www.amazingcto.com/postgres-for-everything/](https://www.amazingcto.com/postgres-for-everything/)
