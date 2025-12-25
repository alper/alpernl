---
author: alper
categories:
  - english
  - software-engineering
date: "2025-01-11T11:42:00+00:00"
guid: https://alper.nl/dingen/?p=17890
parent_post_id: null
post_id: "17890"
title: ""
aliases:
  - /dingen/2025/01/17890/

---
I've had to spend more time than I like thinking about how datetimes are stored in databases and even the commonly accepted practice of storing UTC does not work for all cases.

Specifically when you store something that would happen in the future, you need to store the location of the event as well. Otherwise any time of daylight savings change will shift your event around. This is not just for single events but can also happen for say ordering cut-off times which aren't pinned to a single date.

https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/
