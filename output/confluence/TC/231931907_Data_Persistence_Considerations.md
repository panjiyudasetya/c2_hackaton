---
id: confluence:231931907
source: confluence
type: page
space: TC
title: Data Persistence Considerations
author: Richard van Klaveren
date: '2023-11-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/231931907
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/231931907
---
# Data Persistence Considerations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/231931907  

## Content

Traditionally Teqplay has been focusing on a centralized approach, with a monolithically oriented platform and a central database server hosting the mongo with many application specific databases. On the re-engineering of the platform into AIS Engine (semi-)micro services, also the persistence approach was reconsidered and designed to be split down up to the level of having a database instance per application.

During the development of the Ais Engine project this ‘puristic’ approach was already ‘optimized’ for services that only use the database as a long term state. Those all together used one database server, whereas all end-user applications were using standalone database servers.

Therefore a discussion was held on how to deal with data persistence in the future to set a clear guidance on when to use what. The following 3 proposals have been discussed in detail:

1. Back to the focus of having one database server
2. Defaulting to a database per application, but when only state is stored we could deviate to use a single server
3. Defaulting for using a single database server (highly available where relevant) per namespace, with optional own database per application if there is a relevant need from either a performance or security perspective.

It was quickly agreed that from a development perspective all options are easily possible and no real clear preference was made. Therefore these options were discussed from a DevOps and a security perspective.

**Option 1: One central database server**

Going back to one central database server would clearly have advantages from a DevOps perspective. Only a single database server would need to be maintained, and the location is just a single location. Also making this database server highly available would be just once the work, with added value for all applications. However, when down-time is needed to install updates, this would effect all applications at the same time, and make such upgrades very ‘risky’.

Also from a security perspective this approach is less favorable, since data from competitors is co-hosted and having access at the right level to a database server would make you king of all our data. The latter is clearly contradicting the direction of introducing more granularity in namespaces in our cluster per application group. Also the impact of applications requiring lot of read / write bandwidth will impact other applications running on the same database server.

**Option 2: Default a database server per application**

Continuing the approach of taking a database server per application makes it very clear where to search for the database. Also from a security perspective this gives a lot of freedom, access to 1 database = access to 1 database. From a development perspective it is nice to always have the packaging of the database and the application in 1 Helm chart.

From a devOps perspective this would mean that each and every application database needs to be monitored. Also executing updates becomes more ‘complex’ since there will be many nodes with a database after some time. Although selecting the Bitnami Helm chart would help here, since then instances could be updated via KubeApps. The overhead of all the small databases is considered to be small since running in a cluster, and also the impact of running a heavy query on a database is expected to be minimal on other databases.

It would be possible still to optimize and bring multiple small databases together, however, who is going to take the decision on that? That would be the developer, but is he also expected to support the maintenance on this new central database node? Somehow grouping the database together with the application seems to insinuate that the database maintenance also is responsibility of the developer.

In the end, moving to start using highly available databases is expected to happen less quickly in this approach.

All in all an option that would be much more favorable than option 1.

**Option 3: Default a database server per namespace**

Hosting a database server per namespace in basic would make it clear that all databases are supported in the basis by the DevOps team. Clear disadvantage here is that if there is no ‘namespace database server’ yet that would require it to be setup (by DevOps). This option would tick all boxes on security though and be more clear on who should ‘maintain’ the database servers. Also, the amount of nodes to be updated scales less quickly that in option 2.

In case there is expected to have multiple databases that might influence each other, we can still deviate from the ‘database server per namespace’ approach. Trigger for that one will be clear: performance or security issues are being detected or experienced.

## Conclusion

It was decided to go for option 3, mainly because this would make it clear that database management / updates etc is a job for DevOps rather than for the developer, and the devops task to maintain these databases will be more scalable.