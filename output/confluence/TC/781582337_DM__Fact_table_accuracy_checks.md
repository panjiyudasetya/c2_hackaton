---
id: confluence:781582337
source: confluence
type: page
space: TC
title: '[DM] Fact table accuracy checks'
author: Ryan Kharisma Rakhmat
date: '2025-06-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/781582337
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/781582337
---
# [DM] Fact table accuracy checks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/781582337  

## Content

# Definition

The degree to which data correctly describes the “real world” object or event being described.

# Accuracy checks

Figure 1 defines the percentage of accurate data within the fact column compared to all data (inaccurate + accurate data).

Figure 1

Where:

* `F` → Refers to the fact table
* `V1, V2, ..., VN` → Refers to the list of visit IDs that we want to compare
* `C1, C2, ..., CN` → Refers to the column that we want to do some accuracy checks
* Pass → Refers to accurate data
* Failed → Refers to inaccurate data

| **Scope** | **Table** | **Columns** | **Formula** | **Constraints** |
| --- | --- | --- | --- | --- |
| **Total Berth Visit** | fact\_port\_visit | total\_berth\_visit | count of all berth visits occur on specific visit\_id.  count(berth\_visits) | Value minimum is 0 and others is a positive. Non negative allowed for this. |
| **Cargo / non-cargo Operations** | fact\_port\_visit | total\_cargo\_operation  total\_non\_cargo\_operation  total\_cargo\_operation\_duration  total\_non\_cargo\_operation\_duration | cargo operation  count of all berth visits where is\_cargo\_operation : **true**  cargo operation duration  sum all of the moored duration in berth visits where is\_cargo\_operation : **true**  non-cargo operation  count of all berth visits where is\_cargo\_operation : **false**  non-cargo operation duration  sum all of the moored duration in berth visits where is\_cargo\_operation : **false** | Value minimum is 0 and others is a positive. Non negative allowed for this. |
| add more… | add more… | add more… |  |  |

## Example

* **Pre-condition**

  + Set parameters

    columns = (
    'visit\_id',
    'total\_berth\_visit',
    'total\_cargo\_operation',
    'total\_cargo\_operation\_duration',
    'total\_non\_cargo\_operation',
    'total\_non\_cargo\_operation\_duration',
    )
    visit\_ids = (
    'xxxxxxxxxxxxxxxxxxxx.VISIT',
    'xxxxxxxxxxxxxxxxxxxy.VISIT',
    'xxxxxxxxxxxxxxxxxxxz.VISIT',
    )
  + Sum the number of accurate fact port visit data with visit IDs defined in {visit\_ids} GROUP BY {columns}
  + To check the accurate columns:

    - e.g columns *total\_berth\_visit*
    - do a query to the datamart and compare with the *fact\_port\_visit.total\_berth\_visit*
    - select
      visit\_id
      , count(berth\_visit\_id) as total\_berth\_visit
      from
      fact\_berth\_visit
      group by
      visit\_id
  + Sum the number of accurate + inaccurate fact port visit data with visit IDs defined in {visit\_ids} GROUP BY {columns}
* **Post condition**

  + Positive test case

    - The sum of unique row count is equal to the sum of unique + duplicated row count in the fact pilot data, for example:

      sum\_accurate\_count = 5
      sum\_inaccurate\_count = 0
      accuracy = sum\_accurate\_count/(sum\_accurate\_count + sum\_inaccurate\_count) \* 100
      = 5/(5+0) \* 100 = 100%
  + Negative test case

    - The sum of unique row count is not equal to the sum of unique + duplicated row count in the fact pilot data, for example:

      sum\_accurate\_count = 5
      sum\_inaccurate\_count = 1
      accuracy = sum\_accurate\_count/(sum\_accurate\_count + sum\_inaccurate\_count) \* 100
      = 5/(5+1) \* 100 = 83.33%