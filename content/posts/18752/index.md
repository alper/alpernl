---
date: '2026-01-10T22:22:43+01:00'
title: ''
author: "alper"
categories:
  - english
  - software-engineering
---
A somewhat comprehensive suite of benchmarks show that for real workloads you don't need anything like async Django. Most of the response time in your requests will be used somewhere else.

Do not incur the complexity of an half-complete async web framework to optimize something that's not the bottleneck anyway.

[What async really means for your python web app?](https://hackeryarn.com/post/async-python-benchmarks/)