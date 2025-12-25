---
author: alper
categories:
  - english
  - reading
  - work
date: "2017-10-27T08:56:53+00:00"
guid: http://alper.nl/dingen/?p=5823
parent_post_id: null
post_id: "5823"
title: Highlights from The Principles of Product Development Flow
aliases:
  - /dingen/2017/10/notes-from-the-principles-of-product-development-flow/

---
> "I believe that the dominant paradigm for managing product development is fundamentally wrong."

> In practice, sensible behavior prevails, despite the presence of a dysfunctional formal procedure.

> Third, with a little help from option pricing theory, we will discover that we can actually design development processes such that increases in variability will improve, rather than worsen, our economic performance.

> We favor highly granular planning because we don’t understand the statistics of variability.

> We value flexibility, and we pay for it. In contrast, most product development organizations exclusively reward specialization.

> One of the most interesting examples of decentralizing control without losing alignment is the way the military deals with the uncertainty of warfare.

> If you only quantify one thing, quantify the cost of delay.

> As this book progresses, you will see that the economics of flow is almost always dominated by the cost of queues. If we cannot quantify the cost of a queue on the critical path, then we cannot quantify the benefit of reducing this queue. If we cannot quantify the benefit, we can’t generate support for major changes.

> Reducing risk, which is the primary mission of testing, clearly creates economic value for product developers. In fact, reducing risk is so centrally important to product development that it is indispensable for us to quantify its economic impact.

> In product development, our greatest waste is not unproductive engineers, but work products sitting idle in process queues.

> In product development, our problem is virtually never motionless engineers. It is almost always motionless work products.

> We can create enormous improvements in decision making with surprisingly imperfect answers. Do not let fear of inaccuracy prevent you from creating economic frameworks.

> This leads to what we might call the Pareto Paradox: There is usually more actual opportunity in the undermanaged 80 percent than the overmanaged 20 percent.

> Some product developers aspire to use the same approach in product development. They prepare a minutely detailed plan at the beginning of the project and measure performance against this plan. When they deviate from this plan, they take corrective action. They aspire to front-load their decisions. While this is a superb strategy in repetitive environments like manufacturing, it is a terrible one in product development.

> Not only do these emergent opportunities arrive continuously and randomly, but they are also quite perishable. Opportunities get smaller with time, and obstacles get larger.

> It is always useful to look for a way to reshape a bad choice into a better one. Decompose the choice into its pieces and keep the good parts.

> The general principle is that we should make each decision at the point where further delay no longer increases the expected economic outcome.

> The value of information is its expected economic value.

> Low-cost activities that remove a lot of risk should occur before high-cost activities that remove very little risk.

> Such aggressive filtering, before acquiring sufficient information to make a good economic choice, would eliminate all uncertain and poorly understood opportunities. However, it is precisely these uncertain opportunities that have large payoff asymmetries, making them the best sources of new drugs. Opening the filter to pass these asymmetric opportunities actually increases economic value.

> In my experience, most managers make amazingly fast decisions when they are presented with compelling economic arguments.

> Product development inventory is observable through its effects: increased cycle time, delayed feedback, constantly shifting priorities, and status reporting.

> The more projects we have in process, the more projects we have to track and report status on.

> This is actually a more serious problem than most developers realize because the waste created by following a bad path typically increases exponentially, not linearly, as we progress down the path.

> Widespread queues demotivate workers and undermine initiative.

> Managing the process upstream of the bottleneck is a valuable tool for improving flow at the bottleneck.

> We simply cannot rely on randomness to correct the problems that randomness creates.

> Waiting for complete information improves efficiency, but it leads to queueing.

> Product development creates economic value by producing the recipes for products, information, not by creating physical products.

> Risk-taking is central to value creation in product development.

> We frequently encounter strongly asymmetric payoffs in product development. The value of a success can be much higher than the cost of a failure.

> Either excessive or insufficient probability of failure reduces the efficiency with which we generate information.

> Repeating the same failures is waste, because it generates no new information. Only new failures generate information.

> Product developers should clearly distinguish exploratory testing, which should be optimized for information generation, and validation testing, which should be optimized for high success rates.

> When our task list becomes very granular, the noise in each estimate is very high compared to the signal. Granular estimates produce good estimates of aggregate scope, but we should never schedule tasks at this level of detail. Instead, it makes more sense to aggregate many small tasks and to schedule them as a group.

> The irony of this is that many companies try to reduce the risk of poor forecasts by taking more time to do a careful forecast.

> A buffer converts uncertain earliness to certain lateness.

> In product development, “left side”outcomes represent bad variability, but “right side”outcomes represent good variability.

> Each engineering decision acts as a predecessor for many subsequent decisions. The number of dependent decisions generally grows geometrically with time. Consequently, a single incorrect assumption can force us to change hundreds of later decisions. When we delay feedback, rework becomes exponentially more expensive.

> When engineers are experimenting with a new idea, rapid feedback is enormously energizing. Rapid feedback quickly supplies the positive reinforcement of success, and fast positive reinforcement always increases motivation.

> It is generally safe to assume that we really don’t know where the optimum point is on the batch size response surface. As a result, we must test the response of the product development process to batch size reduction by reducing batch size and measuring the results.

> Sequence activities to create maximum value for minimum cost, and remember that removing risk from a project is a key way to increase the expected value of the project.

> Since it takes almost equal effort to ask for a big bag of money as a small one, people prefer to ask for big bags of money.

> the practice of working in one phase at a time is so devoid of common sense that engineers seldom follow it, even when it is required by their procedures.

> If a simple kanban system was trying to limit the WIP between two processes to 30 items, it might use six pallets that could each hold five parts as physical kanbans. The downstream process would take parts off a pallet and when it was empty, send it back to the upstream process. This empty pallet would signal the upstream process to make more parts. The upstream process is not allowed to make parts unless it has an empty pallet to put them on. This sets an upper limit on the amount of WIP between the two processes.

> Toyota further enhances the effectiveness of this WIP constraint by cross-training workers at adjacent work stations.

> A smaller batch size approach to WIP purging is to shed requirements during periods of congestion.

> It is best to identify in advance which requirements we would consider eliminating or relaxing. We do this for two reasons. First, we can make a more well-reasoned decision before the pressure of a congestion crisis occurs. Second, if we preplan which requirements might be jettisoned, we can structure our product architecture to make it easy to jettison them. We do so by loosely coupling these elements to the rest of the system, so that we can cut them loose quickly.

> A simple way to do this is for the development team to pay for variances during manufacturing ramp. Once the product has been in manufacturing for a fixed amount of time, responsibility for these variances can be transferred to manufacturing.

> Which project activities are most suited for part-time resources? Those that are most prone to expensive congestion. These are high-variability tasks on the critical path. Activities that are more predictable can be handled with full-time resources, since such activities experience less congestion.

> Unfortunately, most organizations love to load these highly productive resources to very high utilization rates. We need to change this mind-set. The big guns are not most valuable as an efficient substitute for small guns, they are most valuable for handling situations that the small guns cannot handle.

> Experts allow us to apply tremendous problem-solving power to a bottleneck. Generalists can be easily shifted to any place they are needed. Is there a way to get both these benefits from the same person? Some organizations believe this is possible, and they characterize the people they are trying to create as T-shaped resources.

> The ideal resource is a jack-of-all-trades and a master-of-one.

> It takes advanced planning to do cross-training and to create T-shaped resources. It takes discipline to load experts to less-than-full utilization. The decision to use part-timers must be made early.

> Detailed planning is very perishable, and this perishability increases with the distance to the planning horizon.

> When we cram too many projects into the product development pipeline, we create queues. These queues create a frictional drag on throughput as developers spend more time expediting and less time adding value. The added load reduces output instead of increasing it.

> Whenever we have any flexible customers, we can use pricing to reduce congestion. Because of the steepness of the queueing curve, even a small shift in demand can make a big difference in flow time.

> We monitor the queue and intervene to restore it to the center of its target range, not to simply bring it back within bounds.

> Cadence inherently makes activities automatic and routine. This lowers transaction overhead and makes it economical to use smaller batches.

> This is an interesting case where the heirs of a brilliantly designed system failed to understand the underlying logic of the system.

> When all jobs have the same delay cost, the preferred scheduling strategy is to do the shortest job first (SJF).

> Projects should only visit nodes that add economic value. They should visit these nodes in the specific sequence that adds economic value most cost-effectively.

> As a general rule, any inexpensive step that eliminates a lot of risk should occur early.

> Instead, it is usually better to maintain a trickle flow of work through the alternate route, even when the primary route is under-utilized.

> Decisions are made at a synchronous, cadenced meeting where people from adjacent processes can easily interact.

> The curtain between adjacent processes does not have to be completely opaque. As work nears completion, we should make its character visible to downstream resources.

> They assume that the plan is correct, and a deviation is always bad. Therefore, they try to close the gap between the two by making results closer to the plan. They often discover it is cheaper to prevent deviations than it is to correct them, so they also emphasize preventing deviations.

> When goals are dynamic, we need different control systems. If we have stable goals, we try to prevent deviations, often by increasing inertia and avoiding risk. If we have dynamic goals, we try to quickly correct deviations, often by decreasing inertia.

> Not all deviations have negative economic consequences.

> By accelerating feedback, we can design processes with less WIP, thereby lowering delay times.

> Whenever we have a short turning radius and a quick reaction time, we can proceed safely at a higher speed.

> This develops a culture of magical decision making, where everybody feels they can make great decisions unencumbered by either analysis or facts.

> When people see that their actions cause consequences, it changes their behavior. They feel a sense of control, and this causes them to take even more control of the system.

> Under dynamic conditions, we need to pay attention to the timing of the revenue associated with the inventory. When revenue is growing rapidly, we may need more DIP to support this growth.

> The Marines believe orders are incomplete without this information. They believe that intent needs to be understood deeply through the organization. They believe that when intent is clear, Marines will be able to select the right course of action.

> In product development, we can change direction more quickly when we have a small team of highly skilled people instead of a large team. We can change direction more quickly when we have a product with a streamlined feature set, instead of one that is bloated with minor features. We can change direction more quickly when we have reserve capacity in our resources.

> Since the Marines expect plans to change, they focus on simple, modular, and flexible plans. Simplicity leads to fast adaptation. Modularity solves the problem of adaptation because different modules can be configured many different ways. Flexibility is achieved by preplanning “branches”and “sequels.”

> There is no substitute for moving to a quick proof-of-concept. There is no substitute for early market feedback.

> They believe that one of the biggest mistakes a leader could make is to stifle initiative.
