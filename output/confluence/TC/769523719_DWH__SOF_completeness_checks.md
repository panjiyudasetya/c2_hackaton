---
id: confluence:769523719
source: confluence
type: page
space: TC
title: '[DWH] SOF completeness checks'
author: Gavin den Hollander
date: '2025-07-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719
---
# [DWH] SOF completeness checks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719  

## Content

# Definition

The proportion of stored data against the potential of "100% complete".

# Completeness check by a specific time range

Figure 1 defines the visit data table completeness check formula, which compares the number of rows of the ODS table to the staging table in the given time range.

Figure 1 - Completeness checks by time range

Where:

* `ODS` → Refers to the Operational Data Source table
* `STG` → Refers to the Staging table
* `start_date` → Refers to the minimum date of the `ODS` or `STG` dataset that we want to compare
* `end_date` → Refers to the maximum date of the `ODS` or `STG` dataset that we want to compare

| **Scope** | **ODS Table** | **Comparison Dataset** |
| --- | --- | --- |
| **Port Visit** | ods\_port\_visit | stg\_statement\_of\_fact |
| **Terminal Visit** | ods\_terminal\_visit | stg\_statement\_of\_fact.terminal\_visits |
| **Berth Visit** | ods\_berth\_visit | stg\_statement\_of\_fact.berth\_visits |
| **CSI Ship** |  |  |
| **Poma Infra** |  |  |

## Example

* **Pre-condition**

  + Set parameters

    start\_date = '2025-01-01'
    end\_date = '2025-06-01'
    unlocodes = ('USCRP', 'USMSY', 'USHOU')
  + Count the ODS port visit data rows from {start\_date} to {end\_date} with port unlocode defined in {unlocodes}
  + Count the staging statement of fact data rows from {start\_date} to {end\_date} and with port unlocode defined in {unlocodes}
* **Post condition**

  + Positive test case

    - The ODS row count is equal to the staging row count, for example:

      ods\_count = 5
      staging\_count = 5
      completeness = ods\_count/staging\_count \* 100
      = 5/5 \* 100 = 100%
  + Negative test case

    - The ODS row count is not equal to the staging row count, for example:

      ods\_count = 4
      staging\_count = 5
      completeness = ods\_count/staging\_count \* 100
      = 4/5 \* 100 = 80%

# Completeness check by row count

Figure 2 defines the SOF complementary data tale completeness check formula, which compares the number of rows of the ODS table to the staging table based on a specific visit ID.

Figure 2 - Completeness checks by row count

Where:

* `ODS` → Refers to the Operational Data Source table
* `STG` → Refers to the Staging table
* `visit_id` → Refers to the `visit_id` column in the ODS table
* `entry_id` → Refers to the `entry_id` column in the staging statement-of-fact table
* `V1, V2, ..., Vn` → Refers to the list of visit IDs that we want to compare

| **Scope** | **ODS Table** | **Comparison Dataset** | **MVP required** |
| --- | --- | --- | --- |
| **Anchor Stops** | ods\_anchor\_stop | stg\_statement\_of\_fact. anchor\_stops | Yes |
| **Unclassified Stops** | ods\_unclassified\_stop | stg\_statement\_of\_fact. unclassified\_stops | No |
| **Encounters** | ods\_encounter | stg\_statement\_of\_fact. encounters | Yes |
| **Lock Stops** | ods\_lock\_stop | stg\_statement\_of\_fact. lock\_stops | No |
| **Visited Approach Areas** | ods\_visited\_approach\_area | stg\_statement\_of\_fact. approach\_area | No |
| **Ship-to-ship transfers** | ods\_ship\_to\_ship\_transfers | stg\_statement\_of\_fact. ship\_to\_ship\_transfer\_transfers | No |
| **Slow Moving Periods** | ods\_slow\_moving\_period | stg\_statement\_of\_fact. slow\_moving\_periods.inPort +  stg\_statement\_of\_fact. slow\_moving\_periods.arrival +  stg\_statement\_of\_fact. slow\_moving\_periods.departure | No |
| **Tug Events** | ods\_tug\_event | stg\_statement\_of\_fact. berthVisits[n].arrivalTugs +  stg\_statement\_of\_fact. berthVisits[n].departureTugs | Yes |
| CSI ship |  |  | Yes |
| Port infra |  |  | Yes |
| Terminal infra |  |  | Yes |

## Example

* **Pre-condition**

  + Set parameters

    start\_date = '2025-01-01'
    end\_date = '2025-06-01'
    unlocodes = ('USCRP', 'USMSY', 'USHOU')
  + Count the ODS anchor stop data rows from {start\_date} to {end\_date} with port unlocode defined in {unlocodes}
  + Sum of the length of anchor stops within the staging statement of fact data from {start\_date} to {end\_date} and with port unlocode defined in {unlocodes}
* **Post condition**

  + Positive test case

    - The ODS anchor stop rows count is equal to the sum of the length of anchor stops, for example:

      ods\_anchor\_stops\_count = 5
      sum\_anchor\_stops\_count = 5
      completeness = ods\_anchor\_stops\_count/sum\_anchor\_stops\_count \* 100
      = 5/5 \* 100 = 100%
  + Negative test case

    - The ODS anchor stop rows count is not equal to the sum of the length of anchor stops, for example:

      ods\_anchor\_stops\_count = 4
      sum\_anchor\_stops\_count = 5
      completeness = ods\_anchor\_stops\_count/sum\_anchor\_stops\_count \* 100
      = 4/5 \* 100 = 80%