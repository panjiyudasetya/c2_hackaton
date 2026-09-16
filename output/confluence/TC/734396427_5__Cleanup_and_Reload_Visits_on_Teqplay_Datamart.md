---
id: confluence:734396427
source: confluence
type: page
space: TC
title: 5. Cleanup and Reload Visits on Teqplay Datamart
author: Panji Y. Wiwaha
date: '2025-06-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427
---
# 5. Cleanup and Reload Visits on Teqplay Datamart

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427  

## Content

The steps below will help you clean up and reload visits on the Teqplay data mart.

* Navigate to the “Filter DAGs by tag” input field and fill it with `reload-visits`.
* Clicking the “**Play**” button on the “Action” section to clean up and reload visits.

* Set up DAG parameters:

  + Fill in the port codes with the UNLOCODEs that you want to backfill, for example:

    USCRP
    USMSY
    USSAV
  + Fill in the start timestamp, for example:

    2024-01-01
  + Choose the schedule type, for example:

    @monthly
  + Click the “**Trigger**” button.
  + Navigate to the Airflow dashboard and ensure all of the associated DAGs in the data warehouse (staging-ods DAGs) and data mart (dim-fact DAGs) are successful.

### Quickstart