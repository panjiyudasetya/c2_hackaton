---
id: confluence:796426250
source: confluence
type: page
space: TC
title: '[DWH] Data duplication test report'
author: Panji Y. Wiwaha
date: '2025-07-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796426250
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796426250
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796426250/DWH+Data+duplication+test+report#SQL-Command-to-move-duplicated-visits-into-the-staging-deleted-table
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427/5.+Cleanup+and+Reload+Visits+on+Teqplay+Datamart?atlOrigin=eyJpIjoiNTIyMWY5ZDU0Mjg3NDlhODk1ODg5MThhODEyNjAyZWYiLCJwIjoiYyJ9
---
# [DWH] Data duplication test report

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796426250  

## Content

## Mitigation steps

1. Find the Visit IDs of the duplicated data from the ODS table.
2. Check whether those Visit IDs are in the Vessel Voyage via this endpoint.

GET https://[URL]/v2/sof/byVisit/[duplicated-visit-id]?view=PTO

| **Environment** | **URL** |
| --- | --- |
| DEV | `https://backendvesselvoyage.dev.teqplay.com` |
| LIVE | `https://backendvesselvoyage.teqplay.nl` |
| CM | `https://backendvesselvoyagedata.teqplay.nl` |

3. If the endpoint returns a statement-of-fact of the Visit ID that you want to investigate:

   1. Compare the ODS data with the one that is present in the SOF JSON field.  
      Please do take note that the field name might be slightly different.
   2. If the data is also duplicated in the JSON field.

      1. Required actions

         1. Mention this problem to the Core Component team via [#pto](https://teqplaydev.slack.com/archives/C04DLAXFVCG) Slack channel.
   3. Otherwise, create a bug card on the data platform board.

      1. Required actions:

         1. Ensures the RabbitMQ SOF delete handler DAG is enabled in Airflow.
         2. Ensures the RabbitMQ SOF subscriber DAG is enabled in Airflow.
         3. If both are enabled, but the invalid Visit ID is still present in the staging SOF table:

            1. Move the duplicated visits into the staging deleted table by executing [this query](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796426250/DWH+Data+duplication+test+report#SQL-Command-to-move-duplicated-visits-into-the-staging-deleted-table.).
         4. Cleanup and reload visits

            1. List all the port UNLOCODEs that are associated with the invalid Visit IDs.
            2. Follow <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427/5.+Cleanup+and+Reload+Visits+on+Teqplay+Datamart?atlOrigin=eyJpIjoiNTIyMWY5ZDU0Mjg3NDlhODk1ODg5MThhODEyNjAyZWYiLCJwIjoiYyJ9> guideline.
4. Otherwise, inform the team that the Visit ID is no longer valid.

   1. Create a bug card on the data platform board.

      1. Required actions

         1. Ensures the RabbitMQ SOF delete handler DAG is enabled in Airflow.
         2. Ensures the RabbitMQ SOF subscriber DAG is enabled in Airflow.
         3. If both are enabled, but the invalid Visit ID is still present in the staging SOF table:

            1. Move the duplicated visits into the staging deleted table by executing [this query](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796426250/DWH+Data+duplication+test+report#SQL-Command-to-move-duplicated-visits-into-the-staging-deleted-table.).
         4. Cleanup and reload visits

            1. List all the port UNLOCODEs that are associated with the invalid Visit IDs.
            2. Follow <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427/5.+Cleanup+and+Reload+Visits+on+Teqplay+Datamart?atlOrigin=eyJpIjoiNTIyMWY5ZDU0Mjg3NDlhODk1ODg5MThhODEyNjAyZWYiLCJwIjoiYyJ9> guideline.

#### SQL Command to move duplicated visits into the staging deleted table.