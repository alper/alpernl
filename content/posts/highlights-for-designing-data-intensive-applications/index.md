---
_wpas_done_all: "1"
author: alper
categories:
  - english
  - reading
  - software-engineering
  - work
date: "2019-06-13T21:19:10+00:00"
guid: http://alper.nl/dingen/?p=15514
parent_post_id: null
post_id: "15514"
title: Highlights for Designing Data-Intensive Applications
aliases:
  - /dingen/2019/06/highlights-for-designing-data-intensive-applications/

---
> Amazon RedShift is a hosted version of ParAccel. More recently, a plethora of open source SQL-on-Hadoop projects have emerged; they are young but aiming to compete with commercial data warehouse systems. These include Apache Hive, Spark SQL, Cloudera Impala, Facebook Presto, Apache Tajo, and Apache Drill \[52, 53\].

> In these situations, as long as people agree on what the format is, it often doesn’t matter how pretty or efficient the format is. The difficulty of getting different organizations to agree on anything outweighs most other concerns.

> Therefore, to maintain backward compatibility, every field you add after the initial deployment of the schema must be optional or have a default value.

> That means you can only remove a field that is optional (a required field can never be removed), and you can never use the same tag number again (because you may still have data written somewhere that includes the old tag number, and that field must be ignored by new code).

> If you are using a system with multi-leader replication, it is worth being aware of these issues, carefully reading the documentation, and thoroughly testing your database to ensure that it really does provide the guarantees you believe it to have.

> Today, most data systems are not able to automatically compensate for such a highly skewed workload, so it’s the responsibility of the application to reduce the skew.

> Unfortunately, these tools don’t directly translate to distributed systems, because a distributed system has no shared memory—only messages sent over an unreliable network.

> Safety is often informally defined as nothing bad happens, and liveness as something good eventually happens.

> A much better solution is to build a brand-new database inside the batch job and write it as files to the job’s output directory in the distributed filesystem, just like the search indexes in the last section. Those data files are then immutable once written, and can be loaded in bulk into servers that handle read-only queries. Various key-value stores support building database files in MapReduce jobs, including Voldemort \[46\], Terrapin \[47\], ElephantDB \[48\], and HBase bulk loading \[49\].

> A complex system that works is invariably found to have evolved from a simple system that works. The inverse proposition also appears to be true: A complex system designed from scratch never works and cannot be made to work.
>
> John Gall, Systemantics (1975)

> When copies of the same data need to be maintained in several storage systems in order to satisfy different access patterns, you need to be very clear about the inputs and outputs: where is data written first, and which representations are derived from which sources? How do you get data into all the right places, in the right formats?

> It would be very natural to extend this programming model to also allow a server to push state-change events into this client-side event pipeline. Thus, state changes could flow through an end-to-end write path: from the interaction on one device that triggers a state change, via event logs and through several derived data systems and stream processors, all the way to the user interface of a person observing the state on another device.

> But this choice is not free either: if a service is so popular that it is “regarded by most people as essential for basic social participation”\[99\], then it is not reasonable to expect people to opt out of this service—using it is de facto mandatory.
