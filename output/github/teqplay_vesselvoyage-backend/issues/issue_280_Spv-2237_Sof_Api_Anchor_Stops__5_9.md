---
id: github:teqplay/vesselvoyage-backend:issue:280
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 280
title: Spv-2237 Sof Api Anchor Stops (5/9)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/280
labels: []
explicit_links: []
---
# Issue #280: Spv-2237 Sof Api Anchor Stops (5/9)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/280  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [353429c66949...bf07e970d5e3](https://github.com/teqplay/vesselvoyage-backend/compare/353429c66949...bf07e970d5e3)
**Merge commit:** [bf07e970d5e3](https://github.com/teqplay/vesselvoyage-backend/commit/bf07e970d5e3)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [SPV-2237-sof-api-anchor-stops](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2237-sof-api-anchor-stops)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-18T08:40:46.493361+00:00
**Status:** MERGED

Added anchor stops to the SOF pto view.
Also moved `Timeline` to its own file
Several POMA models have a`ports` list, but that is not captured in an interface. I created util function to work around that, including a unit test.

