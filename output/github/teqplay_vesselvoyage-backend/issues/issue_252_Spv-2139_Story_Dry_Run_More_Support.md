---
id: github:teqplay/vesselvoyage-backend:issue:252
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 252
title: Spv-2139 Story Dry Run More Support
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/252
labels: []
explicit_links:
- jira:SPV-2139
---
# Issue #252: Spv-2139 Story Dry Run More Support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/252  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [45b3a13837a3...c230ce64fd55](https://github.com/teqplay/vesselvoyage-backend/compare/45b3a13837a3...c230ce64fd55)
**Merge commit:** [c230ce64fd55](https://github.com/teqplay/vesselvoyage-backend/commit/c230ce64fd55)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2139-add-more-poma-infra](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2139-add-more-poma-infra)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-07T12:51:05.690437+00:00
**Status:** MERGED

* Added more poma infra that is used for showing poma entities in a dryrun story
* Added an id to each area activity which is always the start event id
* Also expose all ports that a ship is currently in the EOSP of
* Added missing anchor area ids when going through the anchor area but not going for anchor

