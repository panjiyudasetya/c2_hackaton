---
id: confluence:812122114
source: confluence
type: page
space: TC
title: PTO-2086 One DAG Rule Them All
author: Ryan Kharisma Rakhmat
date: '2025-07-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/812122114
explicit_links:
- jira:PTO-2086
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/812122114
---
# PTO-2086 One DAG Rule Them All

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/812122114  

## Content

PTO-2086 One DAG Rule Them All

This Documents will be used for testing the Features of One DAG Rule Them All button.

| **DAG NAME** | **Descriptions** | **Sample Parameters** |
| --- | --- | --- |
| start\_etl\_pipeline | This is the DAG Rule Them All button. When the DAG is Started, it will be trigger other dags that starts from ingestions, transformations and calculate the dim and facts for our PTO Reports. | `{'unlocode': 'NLRTM', 'start_timestamp': '2025-06-01 00:00:00', 'end_timestamp': '2025-07-28 00:00:00', 'is_poma_included': True, 'is_csi_included': True, 'is_new_database': True}` |

DAG Parameters

| **Name** | **Type** | **Descriptions** |
| --- | --- | --- |
| unlocode | 5 Digit String | Port Codes |
| start\_timestamp | Timestamp | Start timestamp of the data that will be process. |
| end\_timestamp | Timestamp | End timestamp of the data that will be process. |
| is\_poma\_included | Boolean | Whether or not to include refresh the POMA data on the certain timeframe. |
| is\_csi\_included | Boolean | Whether or not to include refresh the CSI or SHIP data on the certain timeframe. |
| is\_new\_database | Boolean | Ignore it, it is only used for the first time creating database for datawarehouse or datamart. |

***Children DAGS***

| **Name** | **Descriptions** |
| --- | --- |
| Prepare Database DAG | This is for creating all new tables in datawarehouse and datamart |
| Staging Ingestion DAG | This is to ingest the staging data from API. whether it is come from POMA, CSI and Vessel Voyages. The data then stored to the Data Warehouse in Staging Table. |
| ODS Transformation DAG | This is to transform data from STAGING into ODS. Happen on Data Warehouse. |
| DIM Transformation DAG | This is to transform ODS into DIM. The Dimension tables will be needed in the BI Reports. |
| FACT Transformation DAG | This is to transform ODS into FACT. The Fact tables will be needed in the BI Reports. |

How to test this DAG

**Success Scenario**

1. Open Airflow and find the `start_etl_pipeline` DAG
2. Run it by clicking the `Play` button on the top right corner and fill the parameters as below:

matrix combinations of parameters

| **Name** | **is\_poma\_included** | **is\_csi\_included** | **is\_new\_database** | **Descriptions** |
| --- | --- | --- | --- | --- |
| Condition 1 | False | False | False | Refresh only Vessel Voyages data. |
| Condition 2 | True | False | False | Refresh POMA and Vessel Voyages data. |
| Condition 3 | True | True | False | Refresh POMA, CSI and Vessel Voyages data. |
| Condition 4 | True | True | True | Run database scripts and also Refresh POMA, CSI and Vessel Voyages data. |

3. Click Trigger
4. Wait for all of the tasks is completed and the status is `green` means successfully executed.

5. Check the Datamart db and refresh the dashboards BI reports.

**Edge Cases Scenario**

1. Sometimes the DAG or Task is failed to run, we can try to re-run it again.
2. But if it is not solve, we need to find out the root cause and discuss in PTO Channel.

*will be added more later…*