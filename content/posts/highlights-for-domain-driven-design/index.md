---
author: alper
categories:
  - english
  - reading
  - software-engineering
date: "2022-09-15T22:17:30+00:00"
guid: https://alper.nl/dingen/?p=16850
parent_post_id: null
post_id: "16850"
title: Highlights for Domain Driven Design
aliases:
  - /dingen/2022/09/highlights-for-domain-driven-design/

---
> Good programmers will naturally start to abstract and develop a model that can do more work. But when this happens only in a technical setting, without collaboration with domain experts, the concepts are naive. That shallowness of knowledge produces software that does a basic job but lacks a deep connection to the domain expert's way of thinking.

> And with typical design approaches, the code and documents don't express this hard-earned knowledge in a usable form, so when the oral tradition is interrupted for any reason, the knowledge is lost.

> Use the model as the backbone of a language. Commit the team to exercising that language relentlessly in all communication within the team and in the code. Use the same language in diagrams, writing, and especially speech.

> Object-oriented programming is powerful because it is based on a modeling paradigm, and it provides implementations of the model constructs.

> If the people who write the code do not feel responsible for the model, or don't understand how to make the model work for an application, then the model has nothing to do with the software. If developers don't realize that changing code changes the model, then their refactoring will weaken the model rather than strengthen it.

> But it is the crucial separation of the domain layer that enables MODEL-DRIVEN DESIGN.

> Even deficiencies in requirements analysis can be overcome by releasing a prototype to users and then quickly changing the product to fit their requests.

> Most flexible languages (such as Java) are overkill for these applications and will cost dearly. A 4GL-style tool is the way to go.

> For example, a one-to-many association might be implemented as a collection in an instance variable. But the design is not necessarily so direct. There may be no collection; an accessor method may query a database to find the appropriate records and instantiate objects based on them. Both of these designs would reflect the same model.

> Worse, as client code uses the database directly, developers are tempted to bypass model features such as AGGREGATES, or even object encapsulation, instead directly taking and manipulating the data they need.

> The sheer technical complexity of applying most database access infrastructure quickly swamps the client code, which leads developers to dumb down the domain layer, which makes the model irrelevant.

> You may find that the framework provides services you can use to easily create a REPOSITORY, or you may find that the framework fights you all the way. You may discover that the architectural framework has already defined an equivalent pattern of getting persistent objects. Or you may discover that it has defined a pattern that is not like a REPOSITORY at all.

> A MODEL-DRIVEN DESIGN stands on two legs. A deep model makes possible an expressive design. At the same time, a design can actually feed insight into the model discovery process when it has the flexibility to let a developer experiment and the clarity to show a developer what is happening.

> But moving the rules out of the domain layer is even worse, since the domain code no longer expresses the model.

> Here we have an example of a "simplest thing that could possibly work" that actually becomes possible because of a more sophisticated model. We can have a functioning prototype of a very complex component in a couple dozen lines of easily understood code.

> A lot of overengineering has been justified in the name of flexibility. But more often than not, excessive layers of abstraction and indirection get in the way. Look at the design of software that really empowers the people who handle it; you will usually see something simple.

> If a developer must consider the implementation of a component in order to use it, the value of encapsulation is lost. If someone other than the original developer must infer the purpose of an object or operation based on its implementation, that new developer may infer a purpose that the operation or class fulfills only by chance. If that was not the intent, the code may work for the moment, but the conceptual basis of the design will have been corrupted, and the two developers will be working at cross-purposes.

> I'm all in favor of learning advanced technology and design concepts, but we have to soberly assess the skills of a particular team, as well as the likely skills of future maintenance teams.

> If you wait until you can make a complete justification for a change, you've waited too long. Your project is already incurring heavy costs, and the postponed changes will be harder to make because the target code will have been more elaborated and more embedded in other code.

> Sometimes we overestimate the value or underestimate the cost of such a dependency.

> Declare a BOUNDED CONTEXT to have no connection to the others at all, allowing developers to find simple, specialized solutions within this small scope.

> Once they have been separated, give their continuing development lower priority than the CORE DOMAIN, and avoid assigning your core developers to the tasks (because they will gain little domain knowledge from them). Also consider off-the-shelf solutions or published models for these GENERIC SUBDOMAINS.

> Not knowing what would be needed, it was assumed that it should be flexible enough to handle anything.

> He had dutifully set out to build a time zone model a priori.

> Reuse does happen, but not always code reuse. The model reuse is often a better level of reuse, as when you use a published design or model.

> A team that uses the code as the sole repository of the model might use comments, maybe structured as Java Doc, or might use some tool in its development environment.

> People knew roughly where to look for a particular function. Individuals working independently could make design decisions that were broadly consistent with each other. The complexity ceiling had been lifted.
