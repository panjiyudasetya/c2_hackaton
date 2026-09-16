---
id: github:teqplay/vesselvoyage-backend:issue:308
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 308
title: 'Feat: Create New Traces On Demand When They Don''T Exist, Only When Requesting
  Story For Now'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/308
labels: []
explicit_links:
- jira:SPV-2286
---
# Issue #308: Feat: Create New Traces On Demand When They Don'T Exist, Only When Requesting Story For Now

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/308  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6500f5c79668...9826b184bafe](https://github.com/teqplay/vesselvoyage-backend/compare/6500f5c79668...9826b184bafe)
**Merge commit:** [9826b184bafe](https://github.com/teqplay/vesselvoyage-backend/commit/9826b184bafe)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2286-create-new-traces-on-demand-after-merging](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2286-create-new-traces-on-demand-after-merging)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-21T10:23:36.792393+00:00
**Status:** MERGED

When merging back data for V2 all traces of the merged entries are removed. They need to be regenerated at some point.
For now only doing this recalculation when the story endpoint is called. This allows us to request and see the trace in the VesselVoyage frontend.
Later on this should be extended further to not rely on just the frontend or someone calling this specific endpoint.


There are some glaring issues with just this implementation though:
* it’s pretty slow when opening for the first time.. but once the traces are generated it’s fast of course
* traces are not connected properly, see image 1
* traces that were already ongoing are not refreshed since they already existed, missing potentially large parts of the trace, see image 2
1. ![](https://bitbucket.org/repo/k5G8e7j/images/3010801628-image.png)
2. The voyage is from NLRTM up to now. It should contain a trace starting from the NLRTM EOS exit.
    ![](https://bitbucket.org/repo/k5G8e7j/images/3966960318-image.png)

