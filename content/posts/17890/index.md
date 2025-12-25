---
_oembed_264badce50b4351f694fa2eb2f641518: '<blockquote class="wp-embedded-content" data-secret="u0C19gzHUT"><a href="https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/">Storing UTC is not a silver&nbsp;bullet</a></blockquote><iframe class="wp-embedded-content" sandbox="allow-scripts" security="restricted" style="position: absolute; visibility: hidden;" title="&#8220;Storing UTC is not a silver&nbsp;bullet&#8221; &#8212; Jon Skeet&#039;s coding blog" src="https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/embed/#?secret=Qan6D8v3iE#?secret=u0C19gzHUT" data-secret="u0C19gzHUT" width="600" height="338" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>'
_oembed_time_264badce50b4351f694fa2eb2f641518: "1736595694"
_wpas_done_all: "1"
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
