---
id: confluence:214269982
source: confluence
type: page
space: TC
title: World of Port available endpoints for run update process manually
author: Maryam Tavakoli (Unlicensed)
date: '2023-09-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214269982
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214269982
---
# World of Port available endpoints for run update process manually

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214269982  

## Content

this document provides an overview of how the project retrieves, converts, and merges data from external resources (Wop) into the Poma system. It also outlines both automated and manual methods of triggering this process. The merging strategy highlights the criteria for determining which data source (Poma or Wop) to use for each port.

1. Data Retrieval and Persistence:

* The first step involves fetching raw data from the Wop API.
* This raw data is then persisted in an external view of the Poma system, specifically in the "wop-port" collection.

1. Data Conversion to Poma Model:

* After the raw data is successfully persisted, the application triggers an event to convert this data into the Poma data model, which includes entities like Ports, Terminals, and Berths.
* The conversion process can be observed in the `nl.teqplay.poma.feature.worldofports.WopDataTransactionListener` and `nl.teqplay.poma.feature.worldofports.WopRawDataPersistEvent` components.

1. Database Merging:

* Once the conversion is completed, another event is raised to merge the Poma database with the external resources.
* The merged data is stored in the "poma-merged" database.
* The merging strategy involves using a whitelist, where if the "unlocode" (a unique identifier for ports) of a port is present in the whitelist, the entire port information comes from Poma. For all other ports, the information is sourced from the Wop data.

**Initiation of the Process:**

* The process is typically initiated on a weekly basis by a job within the Poma system.
* However, there are also endpoints available for manual triggering of the process:

  + A GET request to `https://backendpomasandbox.teqplay.nl/Wop/import/start` triggers the entire process, including data retrieval, conversion, and database merging.
  + A GET request to `https://backendpomasandbox.teqplay.nl/Wop/convert/start` initiates only the conversion process and performs database merging at the end.
  + A GET request to `https://backendpomasandbox.teqplay.nl/v1/all/mergedatabases` merges all data models in the databases.
  + A GET request to `https://backendpomasandbox.teqplay.nl/v1/all/mergedatabases/mergedatabases/worldofports` specifically merges databases for Port, Terminal, and Berth data models.