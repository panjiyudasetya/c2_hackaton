---
id: confluence:779845637
source: confluence
type: page
space: TC
title: '[DM] Fact table uniqueness checks'
author: Panji Y. Wiwaha
date: '2025-06-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/779845637
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/779845637
---
# [DM] Fact table uniqueness checks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/779845637  

## Content

# Definition

No thing will be recorded more than once if that thing is already identified.

# Uniqueness checks

Figure 1 defines the percentage of duplicated data within the fact table based on a specific column. This check compares the sum of the unique fact data count and the sum of the unique + duplicated data count, aggregated by particular columns.

Figure 1 - Duplication checks within the fact data table

Where:

* `F` → Refers to the fact table
* `V1, V2, ..., VN` → Refers to the list of visit IDs that we want to compare
* `C1, C2, ..., CN` → Refers to the column that we want to aggregate

| **Scope** | **ODS Table** | **Group By Columns** |
| --- | --- | --- |
| **Fact anchorages** | fact\_anchor | visit\_id, area\_id, area\_name, area\_type, start\_timestamp,  end\_timestamp, start\_location\_lat, start\_location\_lon, end\_location\_lat, end\_location\_lon |
| **Fact pilots** | fact\_pilot | visit\_id, vessel\_ship\_id,  service\_ship\_imo,  service\_ship\_mmsi, timestamp, fallback\_type, type |
| add more… | add more… | add more… |

## Example

* **Pre-condition**

  + Set parameters

    columns = (
    'visit\_id',
    'vessel\_ship\_id',
    'service\_ship\_imo',
    'service\_ship\_mmsi',
    'timestamp',
    'fallback\_type',
    'type'
    )
    visit\_ids = (
    'xxxxxxxxxxxxxxxxxxxx.VISIT',
    'xxxxxxxxxxxxxxxxxxxy.VISIT',
    'xxxxxxxxxxxxxxxxxxxz.VISIT',
    )
  + Sum the number of unique fact pilot data with visit IDs defined in {visit\_ids} GROUP BY {columns}
  + Sum the number of unique + duplicated fact pilot data with visit IDs defined in {visit\_ids} GROUP BY {columns}
* **Post condition**

  + Positive test case

    - The sum of unique row count is equal to the sum of unique + duplicated row count in the fact pilot data, for example:

      sum\_unique\_count = 5
      sum\_duplicate\_count = 0
      uniqueness = sum\_unique\_count/(sum\_unique\_count + sum\_duplicate\_count) \* 100
      = 5/(5+0) \* 100 = 100%
  + Negative test case

    - The sum of unique row count is not equal to the sum of unique + duplicated row count in the fact pilot data, for example:

      sum\_unique\_count = 5
      sum\_duplicate\_count = 0
      uniqueness = sum\_unique\_count/(sum\_unique\_count + sum\_duplicate\_count) \* 100
      = 5/(5+2) \* 100 = 71.43%