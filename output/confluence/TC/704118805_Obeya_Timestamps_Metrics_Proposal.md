---
id: confluence:704118805
source: confluence
type: page
space: TC
title: Obeya Timestamps Metrics Proposal
author: Darius Wattimena
date: '2025-04-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/704118805
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/704118805
---
# Obeya Timestamps Metrics Proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/704118805  

## Content

## When is a timestamp correct

When checking timestamps the VesselVoyage PTO SOF is always used to track the correctness of timestamps. Tooling like timeline are used to manually verify the expected time something happens based on the AIS data we have.

Criteria to mark a timestamp as correct:

1. Detected time should be within 6 minutes of expected time.
2. All instances of said category of timestamp was detected.
3. The AIS shows the activity never happened. So we expected no timestamp.

## Timestamps to check

1. Drifting (Slow moving)
2. Anchor Down
3. Anchor up
4. Port ATA
5. Port ATD
6. Lock ATA
7. Lock ATD
8. Terminal ATA
9. Terminal ATD
10. Berth ATA
11. Berth ATD
12. Pilot on board
13. Arrival tugs
14. Bunker alongside
15. Bunker departed
16. Departure tugs
17. Pilot disembarked

## Metrics

### Per-Ship Accuracy Metric:

For each ship, define **Timestamp Accuracy Score (TAS):**

n / t \* 100

This means if we can have the following:

`n` = The total amount of timestamp types that are correct.  
`t` = Always 1the total amount of types we check.

So lets say we have 14 timestamp types correct out of the 17 we now have in total, that means we have a TAS of 82% for this ship.

This can be shown in a metric which takes an average of the TAS of all ships we are testing. An example metric could be as follows:

### Incorrect Timestamps Focus Area Metric:

For each timestamp type, define **Incorrect %.**

This can be something as the below table:

| Timestamp Type | Incorrect % |
| --- | --- |
| Port ATA | 5% |
| Port ATD | 12% |
| Berth ATA | 2% |
| Berth ATD | 18% |

With this data we can create a metric where we show the Incorrect % in a proportional bar chart to show the timestamp where the most room to grow resides.