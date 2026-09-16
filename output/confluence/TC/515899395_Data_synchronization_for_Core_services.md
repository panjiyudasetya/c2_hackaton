---
id: confluence:515899395
source: confluence
type: page
space: TC
title: Data synchronization for Core services
author: Richard van Klaveren
date: '2024-12-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/515899395
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/515899395
---
# Data synchronization for Core services

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/515899395  

## Content

Core services are the services holding the master data used by many other systems to properly execute their function. Example of core services holding master data are:

* CSI - holding master data on all vessel specifications
* POMA - holding master data on port infrastructure
* RouteScout- holding master data on routes possible to sail with a boat.

Master data needs to be available in a live production environment continuously and up-to-date to make sure all services dependent on such master data will generate a coherent picture. At the same time, we want to be able to extend master data with new data and validate that such extension is valid and correct, before applying it to the production systems. Therefore, within Teqplay we envision to use the following 4 environments for the following purposes:

1. **Production data:** Here we have the guarantee that all systems and all data are always stable and up-to-date. This environment is being used to serve our customers the best experience. Both, services and data stores are typically setup in a highly available way (multiple instances of either application and/or data) to make sure they are robust.
2. **Data Validation:** In this environment we have the production data and the production systems, but since this environment is only used to update the data and validate updated data is improving our systems, no high availability is needed.
3. **Development (Data stable)**: Here we run the development of all systems, but that means they should be able to trust that core services are available all the time with relevantly up-to-date data
4. **Sandbox:** In the sandbox there are no guarantees at all, here the core-services development itself takes place before it is moved to Development.

Both `Production data` and `Data Validation` are running in the production cluster. The `Development (data stable)` and `Sandbox` are running in the development cluster. The distinction between them is that they are running in different namespaces and that the `Sandbox` and `data validation` are using a single database server within their namespace instead of clusters of databases.

The process to update the data in these systems consists of 3 steps:

1. Someone within the Teqplay team (normally context mapper) with relevant knowledge on shipping will update the core service with new information in the `Data validation` environment and validate the data is updated correct by e.g. running a data validation run in the data platform to see whether all detections are forming a coherent picture.
2. When the context mapper is happy about the data quality, the context mapper will export the data per port to the production environment, where it is being used in all detection systems directly. No data updates will take place in this environment directly anymore, all data updates should come from `Data Validation` environment.
3. In order to get the `Development (Data stable)` environment up-to-date an automated daily synchronization will happen. This way developer do always have up-to-date master data to run their systems against. It is allowed to make direct updates in the `Development (data stable)` environment, however, all data updated in this environment will be overwritten by the production data on the next run.
4. The data in the sandbox environment is updated manually at convenience of the developer, no processes apply here and no guaranteed on correctness apply here.

The different master data applications can be reached via the following URLs:

* Production

  + CSI: <https://csi.teqplay.nl>
  + Poma: <https://poma.teqplay.nl>
  + Routescout: <https://routescoutv2.teqplay.nl>
* Data Validation

  + CSI: <https://csidata.teqplay.nl>
  + Poma: <https://pomadata.teqplay.nl>
  + Routescout: T.B.D.
* Development

  + CSI: <https://csidev.teqplay.nl>
  + Poma: <https://pomadev.teqplay.nl>
  + Routescout: <https://routescoutv2dev.teqplay.nl>