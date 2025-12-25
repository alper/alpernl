---
author: alper
categories:
  - english
  - reading
  - science
  - software-engineering
date: "2024-12-26T23:12:15+00:00"
title: ""
aliases:
  - /dingen/2024/12/17805/

---
[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/pdf/2305.10601)

I came across this paper after the recent [o3 high score](https://arcprize.org/blog/oai-o3-pub-breakthrough) on the ARC-AGI-PUB test. It's a quick read and details how to scale LLMs at inference stage by generating new states at every node and so create a tree on which to perform DFS/BFS search algorithms.

> A specific instantiation of ToT involves answering four questions: 1. How to decompose the intermediate process into thought steps; 2. How to generate potential thoughts from each state; 3. How to heuristically evaluate states; 4. What search algorithm to use.

For each of these steps they can deploy the LLM to generate the desired results which then scaled over the search space balloons the number of calls that need to be done (costing almost 200x the compute).

This isn't your normal LLM stochastic parrot anymore. We've gone one up the abstraction chain and here we have a computer science algorithm running with LLM calls as its basic atoms.
