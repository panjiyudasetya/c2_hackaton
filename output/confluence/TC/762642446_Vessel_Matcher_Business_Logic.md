---
id: confluence:762642446
source: confluence
type: page
space: TC
title: Vessel Matcher Business Logic
author: Fauzan Rifqy
date: '2025-06-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/762642446
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/762642446
---
# Vessel Matcher Business Logic

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/762642446  

## Content

1. If two emails from different brokers mention cargo with the same:

   1. Load ports
   2. Discharge ports
   3. Laycan dates (loading window)
   4. Quantity range
   5. Company, They will generate the same order ID and be treated as the same order.
2. Multiple Matching: An order can be matched to multiple vessels if it meets the criteria for each ship
3. Matching Criteria:

   * Geographic proximity: Distance between vessel's current location and the order's load port
   * Ship capacity vs order quantity
   * Laycan dates (loading window): Time window when vessel must arrive for loading
   * Port compatibility: Match between vessel's capabilities and port requirements