---
id: github:teqplay/vesselvoyage-backend:issue:303
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 303
title: 'Fix: Don''T Expose Finished/Ongoing Fields'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/303
labels: []
explicit_links: []
---
# Issue #303: Fix: Don'T Expose Finished/Ongoing Fields

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/303  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [f458d767a492...ce24f099c111](https://github.com/teqplay/vesselvoyage-backend/compare/f458d767a492...ce24f099c111)
**Merge commit:** [ce24f099c111](https://github.com/teqplay/vesselvoyage-backend/commit/ce24f099c111)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena, Leon Joosse
**Source Branch:** [fix/dont-expose-finished-ongoing-fields](https://github.com/teqplay/vesselvoyage-backend/tree/fix/dont-expose-finished-ongoing-fields)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-30T11:32:07.709964+00:00
**Status:** MERGED

Opted for a simple `@JsonIgnore` since there are no utils in the API package.

