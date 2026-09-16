---
id: github:teqplay/vesselvoyage-backend:issue:2
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 2
title: Feat/Linked Entries
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/2
labels: []
explicit_links: []
---
# Issue #2: Feat/Linked Entries

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/2  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [93bcad1f8b5c...3c40d6ad4760](https://github.com/teqplay/vesselvoyage-backend/compare/93bcad1f8b5c...3c40d6ad4760)
**Merge commit:** [3c40d6ad4760](https://github.com/teqplay/vesselvoyage-backend/commit/3c40d6ad4760)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/linked_entries](https://github.com/teqplay/vesselvoyage-backend/tree/feat/linked_entries)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-07-13T08:31:10.486448+00:00
**Status:** MERGED

* Implement previousEntryId and nextEntryId and endpoints to fetch entries by their id
* Remove workaround to delete historic trace of previous entry when an entry is deleted
* Give all entry id's a suffix ".VISIT" or ".VOYAGE", utilize this knowledge when querying
* Refactor some of the util functions

@{5c57efac4912b735b9e0646c} can you have a high level look at this PR? It’s very big because of refactoring. I can explain you the gist of it if that’s handier.

