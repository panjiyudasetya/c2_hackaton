---
id: github:teqplay/vesselvoyage-backend:issue:373
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 373
title: Spv-2424 Speed Up Sof Loading
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/373
labels: []
explicit_links: []
---
# Issue #373: Spv-2424 Speed Up Sof Loading

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/373  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6fb45d37f66c...82d32db41ac3](https://github.com/teqplay/vesselvoyage-backend/compare/6fb45d37f66c...82d32db41ac3)
**Merge commit:** [82d32db41ac3](https://github.com/teqplay/vesselvoyage-backend/commit/82d32db41ac3)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2424-speed-up-sof-loading](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2424-speed-up-sof-loading)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-22T15:24:01.872973+00:00
**Status:** MERGED

Reworked loading of the esof to be done in one go instead of one by one. This does make loading in SOF by port much faster as they generally have a bunch more visits, meaning a lot more times we have to go to the database for 1 esof.

