---
author: alper
categories:
  - english
  - reading
  - science
  - software-engineering
date: "2025-01-06T06:14:08+00:00"
title: ""
aliases:
  - /dingen/2025/01/17879/

---
[RARE: Retrieval-Augmented Reasoning Enhancement for Large Language Models](https://arxiv.org/abs/2412.02830)

> Medical QA depends heavily on domain-specific knowledge that is not always available within pre-trained models, necessitating knowledge-based retrieval from external sources.

> In addition medical knowledge evolves rapidly, and new treatments or updated guidelines may not be included in the model's pertained corpus.

The question example for the reasoning process in Figure 1 is on a multiple-choice question. That seems overly simple.

> In parallel, Commonsense Question Answering shares similar complexities with Medical QA, particularly in its reliance on structured multi-step reasoning and iterative evidence retrieval.

> rStar ( [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solvers](https://arxiv.org/abs/2408.06195))

The rStar approach seems worth diving into. That will be the paper I read next.

> Monte Carlo Tree Search

> enabling the open source LLMs (LLAMA3.1) to achieve competitive performance with top closed-source LLMs like GPT-4 and GPT-4o.

We'll come to this later in the paper. Their conclusion is that they can trick out LLAMA to get similar performance to GPT-4 in these domains.

> Upper Confidence Bound applied on trees (UCT)

> In contrast, rStar incorporates five distinct actions that enable more adaptive exploration:
>
> A1: Propose a One-Step Thought. This action generates the next reasoning step based on previous steps, allowing the LLM to build the solution incrementally.
>
> A2: Propose Remaining Thought Steps. This action enables the LLM to produce all remaining reasoning steps in one inference, similar to CoT, for simpler questions.
>
> A3: Generate Next Sub-question and Answer. This action decomposes the main problem into a sequence of sub-questions, each solved in turn. A4: Re-answer Sub-question. This action allows the LLM to re-answer a previously generated sub- question, increasing accuracy by using few-shot prompting.
>
> A5: Rephrase Question/Sub-question. This action rephrases the question to clarify conditions and reduce misunderstandings, enhancing the LLM’s interpretation of the problem.

I need to trace the rStar algorithm after reading the original paper. The explanation here is too short.

> These queries target information that can either support or refute the content of each statement, ensuring comprehensive factual verification.

How does this approach deal with (non-)negation that LLMs often have a lot of trouble with? From a language perspective it could just as easily say I can or can't eat grapefruit (iykyk) based on the temperature that day but especially in a medical context these kind of errors can be catastrophic.

> RARE achieves substantial gains, outperforming rStar by 5.17% on MedQA, 2.19% on MedMCQA and 2.39% on MMLU-Medical.

Even if these numbers are statistically significant (which they don't say), these increases are really modest. I would not call this in any way "substantial".

Looking at Table 1, RARE is as much of an increase over rStar as rStar is over the next best approach so from that perspective maybe you could call it significant. The difference between worst and best framework here is around 10% across CoT, RAG, SC, rStar, RARE.

> evaluated on StrategyQA (SQA), CommonsenseQA (CQA), Social IQA (SIQA) and Physical IQA (PIQA)

The main question I have is from what percentage accuracy such a system would be reasonably possible to use in a real world context. Even at 90-95% that would seem like it would be too low to rely on when the stakes are high.

> By enhancing LLMs with retrieval-augmented reasoning, RARE bridges the gap between open source models and state-of-the-art proprietary systems.

> The framework has only been tested on open source models like LLaMA 3.1 and not on larger proprietary models such as GPT-4. This is due to the high number of API calls required by RARE's iterative retrieval and reasoning process, making evaluation on closed source models prohibitively costly.

So here they repeat the statement that they've bridged the gap but they say they haven't used this approach with a model like GPT-4 because the number of API calls would make it too expensive.

That leaves on the table that these kind of many-call approaches are open to OpenAI because they _can_ do these numbers of calls much more affordably from inside the house. No real gap has been closed here and it shows again how big of an advantage OpenAI has.

That raises the question: What makes GPT-4 so good? Why does it perform so much better than open source models?

> RARE is designed to identify a single reasoning trajectory that leads to a correct answer but does not necessarily optimise for the best or shortest path that maximises robustness.

> Any integration into medical workflows must be supervised by qualified practitioners to ensure patient safety and ethical use.
