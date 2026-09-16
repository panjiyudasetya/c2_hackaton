---
id: confluence:708345857
source: confluence
type: page
space: TC
title: 4. Backfilling POMA and CSI Data
author: Panji Y. Wiwaha
date: '2025-05-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/708345857
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/708345857
---
# 4. Backfilling POMA and CSI Data

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/708345857  

## Content

# Introduction

Backfilling data is needed when we want to obtain missing data or maybe older data within a specific time range. Currently, POMA and CSI data changes are relatively small and scheduled to run once a week, but if we want to do the backfilling outside that schedule due to the requirements, this document will explain how to do that.

## POMA

Backfilling step-by-step

1. Go to the Airflow DAGs page and input the POMAYellow tag in the “Filter DAGs by tag”.

2. Start opening the `staging_port` dag to backfill **POMA - Ports**.

3. `CLEAR` (***Clear existing tasks***) the latest DAGs to re-run the backfilling.

4. Backfiling staging data is done when all the tasks on this DAG are running successfully, and the dataset event named `x-poma://staging-ports/loaded` is automatically created.
5. Continue to the ODS table, which is automatically triggered by the dataset.

6. Continue to the dimension table, and find the `dim_maritime_base` DAG.
7. If these loaded events are already updated:

   x-csi://ods-ship-mappings/loaded
   x-poma://ods-berths/loaded
   x-poma://ods-ports/loaded
   x-poma://ods-terminals/loaded

   Then the `dim_maritime_base` DAG will be run automatically.
8. Otherwise, run it manually to update the dimension data in the datamart.
9. The backfilling of the **POMA - Ports** data is done.

Repeat the same steps for the other **POMA** data, such as: **TERMINAL**, **BERTH**, **ANCHORAGE**, **LOCK,** and **APPROACH AREA**.

## CSI

Backfilling step-by-step

1. Go to the Airflow DAGs page and input the CSIYellow tag in the “Filter DAGs by tag”.

2. Start opening the `staging_ship` dag to backfill CSI - Ships.

3. `CLEAR` (***Clear existing tasks***) the latest DAGs to re-run the backfilling.

4. Backfiling staging data is done when all the tasks on this DAG are running successfully, and the dataset event named `x-csi://staging-ships/loaded` is automatically created.
5. Continue to ODS table, this is automatically triggered by the dataset.

6. Continue to the dimension table, and find the `dim_maritime_base` DAG.
7. If these loaded events are already updated:

   x-csi://ods-ship-mappings/loaded
   x-poma://ods-berths/loaded
   x-poma://ods-ports/loaded
   x-poma://ods-terminals/loaded

   Then the `dim_maritime_base` DAG will be run automatically.
8. Otherwise, run it manually to update the dimension data in the datamart.
9. The backfilling of the **CSI - Ships** data is done.

Repeat the same steps for the other **CSI** data, such as **SHIP MAPPING**.