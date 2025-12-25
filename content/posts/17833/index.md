---
author: alper
categories:
  - english
  - reading
  - science
  - software-engineering
date: "2025-01-02T07:17:08+00:00"
title: ""
aliases:
  - /dingen/2025/01/17833/

---
[Adapting While Learning: Grounding LLMs for Scientific Problems with Intelligent Tool Usage Adaptation](https://arxiv.org/abs/2411.00412)

A paper where they fine tune an LLM to be able to answer some questions itself and figure out for which questions it needs to use a specialized tool. Intelligent tool usage seems like it would expand the use cases for LLM driven systems much more than any kind of scaling (real or imagined).

> However, scholars note that their abilities are capped at approximately high-school levels

That seems like a noteworthy statement especially if you are looking to LLMs to provide "novel thinking". It would seem much more that high school problems are abundantly available and relatively trivial so they see a specific focus.

> For numerical answers in the MATH and SciBench datasets, we consider answers correct if they fall within a small tolerance range of the true value, specifically within ±5%.

Don't really see why you could not get exact answers in a mathematical domain.

> This performance gap on public benchmarks is likely due to the larger parameter count and specific optimization of state-of-the-art models on the open-source datasets.

Same as with the high school questions. These datasets are easily available and draw attention so the models overfit on them.

> The model Ours-Pn demonstrates performance comparable to Base-Pf , both showing a significant improvement over the base model. This similarity indicates successful internalization of distilled knowledge from tools. The transition from Ours-Pn to Ours-Pi showcases further improvement in answer accuracy, resulting from the model’s enhanced ability to intelligently switch to tools for harder questions.

This is the core proposition of the paper. Looking at Table 1 with the accuracy percentages there is something of an improvement but it does not really look dramatic or so convincing that you could use these systems in any critical context.

{{< figure src="CleanShot-2025-01-02-at-08.10.34@2x.png" alt="" caption="" >}}

We're looking at increases of 10-20% and an accuracy that's still well under 90% (which I'm also not convinced would be usable).

> We introduced a novel two-component fine-tuning approach to enhance Large Language Models (LLMs) in solving **scientific** **problems** of varying complexity.

One of the key issues with the paper I have is how much work the term "scientific problems" is doing. If this is published, people are going to think that the LLM is solving actual novel issues where in this case it's just filling in relatively basic question/answer pairs that are well understood. Calling them problems is problematic.

The most interesting part of the paper is the appendix where you can see the actual questions and answers in the various datasets and the prompts they used (with example responses). The answers mostly are multiple choice which already influences how many of them you should expect to be correct.
