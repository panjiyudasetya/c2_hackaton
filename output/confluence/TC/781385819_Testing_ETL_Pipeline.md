---
id: confluence:781385819
source: confluence
type: page
space: TC
title: Testing ETL Pipeline
author: Gavin den Hollander
date: '2025-07-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/781385819
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/781385819
---
# Testing ETL Pipeline

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/781385819  

## Content

# Higher overview

**Black box testing**, a form of testing performed without knowledge of a system’s internals, can evaluate an application's functionality, security, performance, and other aspects.

For this higher overview here, we expect the CSV results as a source of truth of the data that needs to be ready on the Datamart. Imagine there is some data that we are ingesting from the data source (e.g, vessel voyage data) through the VV Internal API, then we put it on our Data Warehouse. After that, we transform that data and put it back in the Datamart. The end results of the data should be similar to the expected results. The .csv files that are provided.

Some guidelines here, the **csv** files should consist of the information below:

* Visit IDs of the vessel A that visits port B
* List of berth visit IDs that belong to the vessel A visit ID
* List of terminal visit id that belongs to the vessel A visit ID
* Some important fields that are calculated for port visits, terminal visits, and berth visits. e.g (total berth visit, shifting between terminals duration, total cargo operation durations, etc.)
* The timestamp for the start and end of the visits (e.g, eos-entry timestamp, eos-exit timestamp, etc.)
* and many more.

Testcases

| **Test case** | **Input** | **Output** | **Required** |
| --- | --- | --- | --- |
| Waiting duration correctly calculated |  |  | Yes |
| Steaming in duration correctly calculated |  |  | Yes |
| Sailing in duration correctly calculated |  |  | Yes |
| Drifting duration correctly calculated |  |  | Yes |
| Steaming out correctly calculated |  |  | Yes |
| Waiting in port correctly calculated |  |  | Yes |
| Terminal stay correctly calculated |  |  | Yes |
| PTT stay correctly calculated |  |  | Yes |
| Tug encounters added to tug fact table |  |  | Yes |
| Pilot encounters added to pilot fact table |  |  | Yes |
| Anchorage added to anchorage fact table |  |  | Yes |
| Anchorage split into 3 phases |  |  | Yes |
| Ship-to-ship added to sts fact table |  |  | No |