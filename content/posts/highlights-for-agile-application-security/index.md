---
_wpas_done_all: "1"
author: alper
categories:
  - agile
  - english
  - reading
  - software-engineering
date: "2019-08-21T20:54:37+00:00"
guid: http://alper.nl/dingen/?p=15635
parent_post_id: null
post_id: "15635"
title: Highlights for Agile Application Security
url: /dingen/2019/08/highlights-for-agile-application-security/

---
> Don’t wait for the perfect time, tool or training course to get started. Just do something.

> Lean as a methodology prioritises the principle cycle of “Build”â†’ “Measure”â†’ “Learn”.

> Many security professionals have a hard time adapting their existing practices to a world where requirements can change every few weeks, or where they are never written down at all. Where design and risk management decisions are made by the team just in time, instead of being planned out and directed from top down. And where manual testing and compliance checking cannot possibly keep up with the speed of delivery.

> Agile practitioners argue that while this rule is broadly speaking true, catching a defect later is more expensive than catching one earlier, the solution is not to attempt the impossible task of catching all defects earlier, but instead to focus on reducing the cost of fixing defects by making change safer and easier.

> instead you need to be thinking about secure service design, trust modeling, and secure architecture patterns.

> The design team should have access to security training or security expertise to ensure that the service they are designing enables security through the user experience.

> Security teams should be providing tooling, processes and guidance that helps product managers, architects and developers follow good security practice while designing a new system.

> Security checks that happen at this stage need to be automatable, reliable, repeatable and understandable in order for a team to adopt them.

> The security team should do everything that they can to ensure that the easiest way to build something inside the organisation is the safe and secure way, by providing teams with secure headers, hardened run-time configuration recipes and playbooks, and vetted third party libraries and images that are free from vulnerabilities which teams can grab and use right away.

> When security stops being the team that says no, and becomes the team that enables reliable code to ship, then that’s true agile security.

> Truly agile security teams measure themselves on what they can enable to happen, rather than the security issues they have blocked from going out of the door.

> or they could be taken care of by training the team in secure coding so that they know know how to do things properly from the start.

> Another way to include security in requirements is through attacker stories or misuse cases (instead of use cases). In these stories the team spends some time thinking through how a feature could be misused by an attacker or by another malicious - or even a careless - user.

> We’ve had experience in at least one company where the attack trees are stored electronically in a wiki, and all of the controls are linked to the digital story cards, so the status of each story is recorded in a live view. This shows the security team the current state of the threat tree, any planned work that might affect it, and allows compliance officers to trace back from a work order to find out why it was requested and when it was completed.

> this kind of interlinking is very valuable for high performing and fast moving teams to give them situational awareness to help in making decisions.

> As we’ve seen throughout this book, the speed of agile development creates new security risks and problems. But this speed and efficiency can also offer an important edge against attackers, a way to close vulnerability windows much faster.

> Security should be about enabling the organisation to carry out its goals in the most safe and secure manner possible. This means that an effective risk management process should be about enabling people in the organisation to take appropriate risks in an informed manner. The key here being informed: risk management is not all about avoidance but the mindful understanding, reduction, sharing and acceptance of risk as appropriate.

> But with an agile team continuously changing the system in response to new information, the context in which a risk is accepted can change dramatically in a fairly short time.

> Common change control practices, such as specified by ITIL or COBIT, are designed to deal with waterfall projects that push large change sets a handful of times per year, and cannot possibly keep up with Continuous Delivery or Continuous Deployment approaches.

> This means that unlike in some more traditional software engineering shops, Agile teams may resist or avoid review boards, design authorities and other control mechanisms imposed from outside if they believe that these outside forces will get in the way of delivery. This is a problem for security professionals who are used to working with architecture review boards and other central authorities to set guiding principles and rules to ensure the security of all systems.

> In a traditional software development lifecycle, risk assessment is done based on the system requirements and design specifications and models created up front. A risk analyst uses those documents to identify the risks that will reside in the system, and puts together a plan to monitor and mitigate these risks. Then audits are done to ensure that the system built matches the documented design specifications and that the risk management plan is still valid.

> Nation state attack teams looking to steal data or IP, or conducting reconnaissance or sabotage for cyber warfare (for a vast majority of situations these will be well outside of your threat model and would not be something you would likely be able to discover or prevent).

> There are different sources of information about threats to help you understand threat actors and the risks that they pose to your organization. While this is an area of the security industry that is widely considered to be over-hyped and to have not returned on the promises of value that have been made (See Threaty Threats boxout), it can still have a place in your security program.

> Some platforms for reporting, detecting, collecting and aggregating threat intelligence include:
>
> Open Threat Exchange (https://www.alienvault.com/open-threat-exchange)
>
> Open TPX (https://www.opentpx.org/)
>
> Passive Total (https://www.passivetotal.org/)
>
> Critical Stack (https://intel.criticalstack.com/)
>
> Facebook’s Threat Exchange (https://www.facebook.com/threatexchange)

> Does a change fundamentally change the architecture or alter a tryst boundary? These types of changes should trigger a risk review (in design or code or both) and possibly some kind of compliance checks.

> Quick and dirty threat modelling done often is much better than no threat modelling at all.

> Each time that you come back again to look at the design and how it has been changed, you’ll have a new focus, new information and more experience, which means that you may ask new questions and find problems that you didn’t see before.

> Because the attack surface is continuously changing, you need to do threat modeling on a continuous basis. Threat modeling has to be done a lightweight, incremental and iterative way.

> People (including attackers) are like water when it comes to protective controls that get in their way. They will work around them and come up with pragamtic solutions to get themselves moving again.

> You can’t secure what you don’t understand
>
> Bruce Schneier

> A clean architecture with well-defined interfaces and a minimal feature set is not the same as a simplistic and incomplete design that focuses only on implementing features quickly, without dealing with data safety and confidentiality, or providing defense against run-time failures and attacks.

> In many environments, enforcing code reviews upfront is the only way to ensure that reviews get done at all: it can be difficult to convince developers to make code changes after they have already checked code in and moved on to another piece of work.

> Probably the best reference for a security code review checklist is OWASP’s ASVS project.

> Acceptance tests may also be done manually, in demos with the customer, especially where the tests are expensive or inconvenient to automate.

> The advantages to an agile development team of being able to self-provision development and test environments like this are obvious. They get control over how their environments are set up and when it gets done. They don’t have to wait days or weeks to hear back from ops.

> Before adding security testing into your pipeline, make sure that the pipeline is set up correctly, and that the team is using it correctly and consistently.
>
> all changes are checked into the code repository
>
> team members check in frequently
>
> automated tests run consistently and quickly
>
> when tests fail, the team stops and fix problems imemdiately before making more changes

> But instead of treating pen testing as a gate, think of it more as a validation and a valuable learning experience for the entire team.

> OpenSCAP (https://www.open-scap.org/) scans specific Linux platforms and other software against hardening policies based on PCI DSS, STIG, and USGCB and helps with automatically correcting any deficiencies that are found.
>
> Lynis (https://cisofy.com/lynis/) is an open source scanner for Linux and Unix systems that will check configurations against CIS, NIST and NSA hardening specs, as well as vendor-supplied guidelines and general best practices.

> One of the best examples is Dev-Sec (https://github.com/dev-sec), a set of open source hardening templates originally created at Deutsche Telekom, and now maintained by contributors from many organizations.

> Security Monkey (https://github.com/Netflix/security\_monkey) automatically checks for insecure policies, and records the history of policy changes

> Conformity Monkey (https://github.com/Netflix/SimianArmy/wiki/Conformity-Home) automatically checks configuration of a run-time instance against pre-defined rules and alerts the owner (and security team) of any violations

> build chains can become highly customized and fragile over time.

> 6.5 train the development team in secure coding at least annually, and provide them with secure coding guidelines.

> Many of the ideas about automating compliance in this chapter are based on the DevOps Audit Defense Toolkit, a free, community-built process framework written by compliance and IT governance experts James DeLuccia IV, Jeff Gallimore, Gene Kim, and Byron Miller.

> Reviewers follow checklists to ensure that all code meets the team’s standards and guidelines, and to watch out for unsafe coding practices. Management periodically audits to make sure that reviews are done consistently, and that engineers aren’t rubber stamping each other’s work.

> While ITIL change management is designed to deal with infrequent, high-risk “big bang”changes, most changes by Agile and DevOps teams are small and low-risk, and can flow under the bar. They can be treated as standard or routine changes that have been preapproved by management, and that don’t require a heavyweight change review meeting.

> Auditors like this a lot. Look at all of the clear, documented hand offs and reviews and approvals, all of the double checks and opportunities to catch mistakes and malfeasance.
>
> But look at all the unnecessary delays and overhead costs, and the many chances for misunderstandings and miscommunication. This is why almost nobody builds and delivers systems this way any more.

> For teams, compliance should - and has to - build on top of the team’s commitment to doing things right and delivering working software. Teams that are already working towards zero defect tolerance, and teams that are following good technical practices including Continuous Integration should be more successful in meeting compliance.

> 'Effective security teams should measure themselves by what they enable,
>
> not by what they block'

> Lazy security teams default to No as it is a get out of jail free card for any future negative impact that may come from the project they opposed. Ineffective security teams want the risk profile of a company to stay the same so that they do not have to make hard choices between security and innovation.

> A security team who can default to openness and only restrict as the exception will do a far better job at spreading knowledge about what they do, and most importantly, why they are doing it.
