---
title: "Wiki"
date: 2006-07-14T10:30:00
author: alper
categories:
  - english
  - internet
---

You might have noticed that my wiki is back up again. I saw it in my referer logs. Debian self-healing is pretty nice.

I reverted the latest batch of spam and then I edited SpecialUserlogin.php to this:

```
if (TRUE or !$wgUser->isAllowedToCreateAccount()) {
```

So nobody is able to create accounts on this server anymore. I got the hint from Peter's [Rukapedia](http://ruk.ca/wiki/).

I can always make accounts, so if you think you need to edit *my* wiki, mail me.