---
id: confluence:705233041
source: confluence
type: page
space: TC
title: 3. Backfilling Teqplay Data Warehouse
author: Panji Y. Wiwaha
date: '2025-05-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/705233041
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/705233041
---
# 3. Backfilling Teqplay Data Warehouse

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/705233041  

## Content

# **Introduction**

Backfilling data is needed when we want to obtain missing data or even older data within a specific time range, such as the vessel voyage’s statement of facts and voyage data. For now, only the **Vessel Voyage** and **Voyage** services have this backfilling feature. As for **POMA** and **CSI** data, we can always backfill the data by running DAGs to get a staging dataset once a week in one go. This is possible because their data volumes are relatively small.

# **Backfilling Vessel Voyage**

### **Statement of facts**

#### Manual backfilling

* Select the DAG with ID [**staging\_sof\_by\_port**](https://airflowdev.teqplay.dev/dags/staging_sof_by_port/grid).
* Click the “**Play**” button to trigger it manually.

* Set up DAG parameters.

  + Fill in the port code with the UNLOCODE that we want to backfill.
  + Fill in the start and end timestamps.
  + Click the “**Trigger**” button.

### Automatic backfilling

* Disable DAG with ID [**backfill\_staging\_sof\_by\_ports**](https://airflowdev.teqplay.dev/dags/backfill_staging_sof_by_ports/grid).
* Remove DAG run history by following these steps (if any).

  + Clicks the number of successful or failed runs.
  + Select all histories, and then delete them.
* Click the “**Admin**” menu → Select “**Variables**” → Set the backfill variables.

  + `STAGING_SOF__BACKFILL_SCHEDULE` → Used to define a backfilling schedule.  
    You can set the value with `@daily`, `@weekly`, or `@monthly` schedule (it depends on the port’s data volume per day/week/month).
  + `STAGING_SOF__BACKFILL_START_DATE` → Used to define the start date of a backfilling schedule. You must set the date in this format: `YYYY-MM-DD`.
  + `STAGING_SOF__BACKFILL_UNLOCODES` → Used to define specific ports that you want to backfill.
* Refresh the Airflow App and make sure the [**backfill\_staging\_sof\_by\_ports**](https://airflowdev.teqplay.dev/dags/backfill_staging_sof_by_ports/grid) DAG parameters are updated by checking the dashboard.
* Once everything is set, enable the DAG and ensure it runs successfully.

# **Backfilling Voyage**

* Disable DAG with ID [**backfill\_staging\_voyage\_by\_ports**](https://airflowdev.teqplay.dev/dags/backfill_staging_voyage_by_ports/grid).
* Remove DAG run history by following these steps (if any).

  + Clicks the number of successful or failed runs.
  + Select all histories and delete them.
  + Click the “**Admin**” menu → Select “**Variables**” → Set the backfill variables.

    - `STAGING_VOYAGE__BACKFILL_SCHEDULE` → Used to define a backfilling schedule.  
      You can set the value with `@daily`, `@weekly`, or `@monthly` schedule (it depends on the port’s data volume per day/week/month).
    - `STAGING_VOYAGE__BACKFILL_START_DATE` → Used to define the start date of a backfilling schedule. You must set the date in this format: `YYYY-MM-DD`.
    - `STAGING_VOYAGE__BACKFILL_UNLOCODES` → Used to define specific ports that you want to backfill.
* Refresh the Airflow App and make sure the [**backfill\_staging\_voyage\_by\_ports**](https://airflowdev.teqplay.dev/dags/backfill_staging_voyage_by_ports/grid) DAG parameters are updated by checking the dashboard.
* Once everything is set, enable the DAG and ensure it runs successfully.