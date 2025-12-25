---
_wp_old_date: "2019-11-26"
author: alper
categories:
  - english
date: "2019-11-27T12:23:56+00:00"
title: 'Types and Functions 6: Applicative'
aliases:
  - /dingen/2019/11/types-and-functions-6-applicative/

---
> Both `Http` calls will happen instantly and `renderPage` will be called when both are resolved.

No idea why this is the case that `ap` makes the calls happen instantly and it is not explained. A paragraph later it is explained, the initial function is curried and is waiting for both of its parameters to arrive before it can run. What ap does is immediately execute whatever needs to be done to get such a parameter.

`liftA2(add, Maybe.of(2), Maybe.of(3));`

That is rather incredible.
