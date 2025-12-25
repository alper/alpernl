---
author: alper
categories:
  - english
  - reading
  - software-engineering
date: "2021-08-22T22:06:47+00:00"
guid: https://alper.nl/dingen/?p=16581
parent_post_id: null
post_id: "16581"
title: Highlights for Site Reliability Engineering
aliases:
  - /dingen/2021/08/highlights-for-site-reliability-engineering/

---
> Traditional operations teams and their counterparts in product development thus often end up in conflict, most visibly over how quickly software can be released to production. At their core, the development teams want to launch new features and see them adopted by users. At their core, the ops teams want to make sure the service doesn’t break while they are holding the pager. Because most outages are caused by some kind of change—a new configuration, a new feature launch, or a new type of user traffic—the two teams’ goals are fundamentally in tension.

> SRE is what happens when you ask a software engineer to design an operations team.

> The use of an error budget resolves the structural conflict of incentives between development and SRE. SRE’s goal is no longer “zero outages”; rather, SREs and product developers aim to spend the error budget getting maximum feature velocity. This change makes all the difference. An outage is no longer a “bad”thing—it is an expected part of the process of innovation, and an occurrence that both development and SRE teams manage rather than fear.

> When humans are necessary, we have found that thinking through and recording the best practices ahead of time in a “playbook”produces roughly a 3x improvement in MTTR as compared to the strategy of “winging it.”The hero jack-of-all-trades on-call engineer does work, but the practiced on-call engineer armed with a playbook works much better.

> However, some systems should be instrumented with client-side collection, because not measuring behavior at the client can miss a range of problems that affect users but don’t affect server-side metrics.

> Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.

> At least 50% of each SRE’s time should be spent on engineering project work that will either reduce future toil or add service features. Feature development typically focuses on improving reliability, performance, or utilization, which often reduces toil as a second-order effect.

> A product’s feature velocity will slow if the SRE team is too busy with manual work and firefighting to roll out new features promptly.

> This kind of tension is common within a team, and often reflects an underlying mistrust of the team’s self-discipline: while some team members want to implement a “hack”to allow time for a proper fix, others worry that a hack will be forgotten or that the proper fix will be deprioritized indefinitely. This concern is credible, as it’s easy to build layers of unmaintainable technical debt by patching over problems instead of making real fixes. Managers and technical leaders play a key role in implementing true, long-term fixes by supporting and prioritizing potentially time-consuming long-term fixes even when the initial “pain”of paging subsides.

> It’s easy to overlook the fact that once you have encapsulated some task in automation, anyone can execute the task. Therefore, the time savings apply across anyone who would plausibly use the automation. Decoupling operator from operation is very powerful.

> The main upshot of this new automation was that we had a lot more free time to spend on improving other parts of the infrastructure. Such improvements had a cascading effect: the more time we saved, the more time we were able to spend on optimizing and automating other tedious work.

> “Why don’t we gate the code with a flag instead of deleting it?”

> If we release 100 unrelated changes to a system at the same time and performance gets worse, understanding which changes impacted performance, and how they did so, will take considerable effort or additional instrumentation. If the release is performed in smaller batches, we can move faster with more confidence because each code change can be understood in isolation in the larger system.

> There are many ways to simplify and speed troubleshooting. Perhaps the most fundamental are:
>
> Building observability—with both white-box metrics and structured logs—into each component from the ground up.
>
> Designing systems with well-understood and observable interfaces between components.

> Some on-call engineers simultaneously experienced what they believed to be a failure of the corporate network and relocated to dedicated secure rooms (panic rooms) with backup access to the production environment.

> Google relies upon our own tools. Much of the software stack that we use for troubleshooting and communicating lies behind jobs that were crash-looping. Had this outage lasted any longer, debugging would have been severely hindered.

> De facto, the commander holds all positions that they have not delegated.

> It is important to define postmortem criteria before an incident occurs so that everyone knows when a postmortem is necessary. In addition to these objective triggers, any stakeholder may request a postmortem for an event.

> Writing a postmortem also involves formal review and publication. In practice, teams share the first postmortem draft internally and solicit a group of senior engineers to assess the draft for completeness. Review criteria might include:
>
> Was key incident data collected for posterity?
>
> Are the impact assessments complete?
>
> Was the root cause sufficiently deep?
>
> Is the action plan appropriate and are resulting bug fixes at appropriate priority?
>
> Did we share the outcome with relevant stakeholders?

> Make sure that writing effective postmortems is a rewarded and celebrated practice, both publicly through the social methods mentioned earlier, and through individual and team performance management.

> one of SRE’s guiding principles is that “team size should not scale directly with service growth.”

> Performance Data describes how a service scales: for every unit of demand X in cluster Y, how many units of dependency Z are used? This scaling data may be derived in a number of ways depending on the maturity of the service in question. Some services are load tested, while others infer their scaling based upon past performance.

> When deploying approximation to help speed development, it’s important to undertake the work in a way that allows the team to make future enhancements and revisit approximation.

> By working one-on-one with early users, you can address those fears personally, and demonstrate that rather than owning the toil of performing a tedious task manually, the team instead owns the configurations, processes, and ultimate results of their technical work.

> Load test components until they break. As load increases, a component typically handles requests successfully until it reaches a point at which it can’t handle more requests.

> If you believe your system has proper protections against being overloaded, consider performing failure tests in a small slice of production to find the point at which the components in your system fail under real traffic

> Its authors point out \[Bur06\] that providing consensus primitives as a service rather than as libraries that engineers build into their applications frees application maintainers of having to deploy their systems in a way compatible with a highly available consensus service (running the right number of replicas, dealing with group membership, dealing with performance, etc.).

> Regardless of the source of the “thundering herd”problem, nothing is harder on cluster infrastructure and the SREs responsible for a cluster’s various services than a buggy 10,000 worker pipeline job.

> We don’t make teams “practice”their backups, instead:
>
> Teams define service level objectives (SLOs) for data availability in a variety of failure modes.
>
> A team practices and demonstrates their ability to meet those SLOs.

> Google has also found that the most devastating acute data deletion cases are caused by application developers unfamiliar with existing code but working on deletion-related code, especially batch processing pipelines

> The most important principle in this layer is that backups don’t matter; what matters is recovery.

> Was the ability to formulate such an estimate luck? No—our success was the fruit of planning, adherence to best practices, hard work, and cooperation, and we were glad to see our investment in each of these elements pay off as well as it did.

> In short, we always knew that adherence to best practices is important, and it was good to see that maxim proven true.

> At first, this race condition may occur for a tiny fraction of data. But as the volume of data increases, a larger and larger fraction of the data is at risk for triggering a race condition. Such a scenario is probabilistic—the pipeline works correctly for the vast majority of data and for most of the time. When such race conditions occur in a data deletion pipeline, the wrong data can be deleted nondeterministically.

> The Google Search SRE team structures this learning through a document called the “on-call learning checklist.”

> When standard operating procedures break down, they’ll need to be able to improvise fully.

> Because of the rapid change of production systems, it is important that your team welcome any chance to refamiliarize themselves with a system, including by learning from the newest, rather than oldest, members of the team.

> At some point, if you can’t get the attention you need to fix the root cause of the problems causing interrupts, perhaps the component you’re supporting isn’t that important.

> Once embedded in a team, the SRE focuses on improving the team’s practices instead of simply helping the team empty the ticket queue. The SRE observes the team’s daily routine and makes recommendations to improve their practices.

> A default to ops mode usually happens in response to an overwhelming pressure, real or imagined.

> Any serving-critical component for which the existing SREs respond to questions by saying, “We don’t know anything about that; the devs own it”
>
> To give acceptable on-call support for a component, you should at least know the consequences when it breaks and the urgency needed to fix problems.

> Usually, the SRE team establishes and maintains a PRR checklist explicitly for the Analysis phase.

> For example, SRE might help implement a “dark launch”setup, in which part of the traffic from existing users is sent to the new service in addition to being sent to the live production service. The responses from the new service are “dark”since they are thrown away and not actually shown to users.

> What happened
>
> The effectiveness of the response
>
> What we would do differently next time
>
> What actions will be taken to make sure a particular incident doesn’t happen again
