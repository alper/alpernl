---
date: '2026-01-01T15:07:39+01:00'
title: ''
author: "alper"
categories:
  - english
  - software-engineering
---

When I read the details of the Mongobleed exploit, I gasped. It's so stunning in its naivete.

What do you mean:

> Instead, it trusts the user’s input and uses that as the canonical size of the payload, even if it got a different number.

and:

> An attacker can send a compressed, invalid BSON object that does NOT contain a null terminator.

It's another data point that nobody reads any of these docs or seriously tests out most of the software out there.

https://bigdata.2minutestreaming.com/p/mongobleed-explained-simply