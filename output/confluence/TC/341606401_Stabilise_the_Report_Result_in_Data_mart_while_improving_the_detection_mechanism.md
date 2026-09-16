---
id: confluence:341606401
source: confluence
type: page
space: TC
title: 'Stabilise the Report Result in Data mart while improving the detection mechanisms
  in Revent, PTO, and Vessel voyage:'
author: Richard van Klaveren
date: '2024-04-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/341606401
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/341606401
---
# Stabilise the Report Result in Data mart while improving the detection mechanisms in Revent, PTO, and Vessel voyage:

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/341606401  

## Content

Typically there a are parameters that introduce changes over time in the measured values inside PTO:

1. The users have applied changes in the operational process after learning from the PTO dashboards
2. The context data has changed (ship or port infrastructure), since we did not have the right knowledge before
3. The Definitions / Algorithms how to calculate timestamps / durations have changed.

When discussing this with APMT, they have indicated the following elements to be important, while improving on context data (2) or the Algorithms (3) to make sure operational users will see the impact of their actions:

* the data for a terminal ALWAYS will need to be consistent (so old and new data needs to be taken through the algorithm change), no improvements introduced half way
* Improvements will need to be transparently communicated to the end users

Reasoning through this means that:

1. you don't want to be forced to go for the big-bang approach, but want to be able to do this per port.
2. Since recalculating all data will take up to 100 hours and since we want to try out things on a subset of terminals, there will be a situation where some ports are in CURRENT version, and some are in NEXT version.

**Challenge:**

Continuous updates to various components for enhancement purposes lead to inconsistency in generated reports in PTO. These inconsistency often make it difficult to trace the origin of modification.

**Challenge 1**: Upon report modifications, access to prior versions is unavailable.

**Challenge 2**: Customers lack awareness of changes and lack mechanisms to validate or reject them.

**Challenge 3**: Reverting all data in the live version due to unvalidated changes is both time-consuming and costly.

**Proposed Solution:**

**Introducing the acceptance environment:**

**Regarding Challenge 1:**

In order to streamline data history management, maintaining only two versions (the new version and the previous one) suffices and remains manageable. The new version can reside in the acceptance environment (ACC) while the previous version remains in production (PROD).

**Regarding Challenge 2:**

A restricted number of customers will have access to the new version for data validation purposes. Once validated in the acceptance environment, the new version can be deployed to production. By implementing a gateway between the Data Warehouse (DWH) and Data Mart, we can control which version of data is presented to customers.

**Regarding Challenge 3:**

The update will only be applied to a limited dataset, which is more efficient.

\*\*\* During the gap between deployments, event processing must be suspended and queued events must be consumed afterward to ensure continuity.