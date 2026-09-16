---
id: github:teqplay/vesselvoyage-backend:issue:342
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 342
title: Spv-2313 Stop Jitter
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/342
labels: []
explicit_links: []
---
# Issue #342: Spv-2313 Stop Jitter

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/342  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [293bf0c43c64...7d81e215dae4](https://github.com/teqplay/vesselvoyage-backend/compare/293bf0c43c64...7d81e215dae4)
**Merge commit:** [7d81e215dae4](https://github.com/teqplay/vesselvoyage-backend/commit/7d81e215dae4)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse, Joost Dambrink
**Approvers:** Michel Wilson
**Source Branch:** [SPV-2313-stop-jitter](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2313-stop-jitter)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-23T13:51:50.953330+00:00
**Status:** MERGED

Adds some basic merging tactics to fix stops real-time. They have almost no impact so there is almost no performance impact.
I do still have to do some manual testing to ensure all cases are merged correctly. But finding ships that stop in a certain pattern are not really that easy to find without going years back which we sadly don’t have stop events for :confused:

