---
id: confluence:770965511
source: confluence
type: page
space: TC
title: '[DWH] ODS table uniqueness checks'
author: Panji Y. Wiwaha
date: '2025-06-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/770965511
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/770965511
---
# [DWH] ODS table uniqueness checks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/770965511  

## Content

# Definition

No thing will be recorded more than once if that thing is already identified.

# Uniqueness checks

Figure 1 defines the percentage of duplicated data within the ODS table based on a specific column. This check compares the sum of the ODS unique data count and the sum of the unique + duplicated data count, aggregated by particular columns.

Figure 1 - Duplication checks within the ODS data table

Where:

* `ODS` → Refers to the Operational Data Source table
* `V1, V2, ..., VN` → Refers to the list of visit IDs that we want to compare
* `C1, C2, ..., CN` → Refers to the column that we want to aggregate

| **Scope** | **ODS Table** | **Group By Columns** |
| --- | --- | --- |
| **Port Visit** | ods\_port\_visit | port\_id, ship\_imo, ship\_mmsi, start\_timestamp, end\_timestamp |
| **Terminal Visit** | ods\_terminal\_visit | port\_id, terminal\_id, ship\_imo, ship\_mmsi, start\_timestamp, end\_timestamp, terminal\_visit\_ref |
| **Berth Visit** | ods\_berth\_visit | port\_id, berth\_id, ship\_imo, ship\_mmsi, start\_timestamp, end\_timestamp, berth\_visit\_ref, terminal\_visit\_ref |
| add more… | add more… | add more… |

## Example

* **Pre-condition**

  + Set parameters

    columns = (
    'port\_id',
    'ship\_imo',
    'ship\_mmsi',
    'start\_timestamp',
    'end\_timestamp'
    )
    visit\_ids = (
    'xxxxxxxxxxxxxxxxxxxx.VISIT',
    'xxxxxxxxxxxxxxxxxxxy.VISIT',
    'xxxxxxxxxxxxxxxxxxxz.VISIT',
    )
  + Sum the number of unique ODS port visit data with visit IDs defined in {visit\_ids} GROUP BY {columns}
  + Sum the number of unique + duplicated ODS port visit data with visit IDs defined in {visit\_ids} GROUP BY {columns}
* **Post condition**

  + Positive test case

    - The sum of unique row count is equal to the sum of unique + duplicated row count in the ODS port visit data, for example:

      sum\_unique\_count = 5
      sum\_duplicate\_count = 0
      uniqueness = sum\_unique\_count/(sum\_unique\_count + sum\_duplicate\_count) \* 100
      = 5/(5+0) \* 100 = 100%
  + Negative test case

    - The sum of unique row count is not equal to the sum of unique + duplicated row count in the ODS port visit data, for example:

      sum\_unique\_count = 5
      sum\_duplicate\_count = 2
      uniqueness = sum\_unique\_count/(sum\_unique\_count + sum\_duplicate\_count) \* 100
      = 5/(5+2) \* 100 = 71.43%