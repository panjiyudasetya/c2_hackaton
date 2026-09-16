---
id: github:teqplay/portreporter-backend:issue:993
source: github
type: issue
repo: teqplay/portreporter-backend
number: 993
title: 'Prp-189 : Two Modifications For User-Error Prevention:'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/993
labels: []
explicit_links:
- jira:PRP-189
---
# Issue #993: Prp-189 : Two Modifications For User-Error Prevention:

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/993  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [364d6a1445f3...27a565005c80](https://github.com/teqplay/portreporter-backend/compare/364d6a1445f3...27a565005c80)
**Merge commit:** [27a565005c80](https://github.com/teqplay/portreporter-backend/commit/27a565005c80)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman
**Approvers:** Joost Laurman
**Source Branch:** [PRP-189/fix/prevent_empty_roles_error_and_filter_empty_documents](https://github.com/teqplay/portreporter-backend/tree/PRP-189/fix/prevent_empty_roles_error_and_filter_empty_documents)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-11-22T15:59:26.241937+00:00
**Status:** MERGED

* Prevent empty documents to be treated \(when the documents parameter is set but there are no files, an empty file is put automatically in the request\).
* Prevent changelogEntries to be created with an empty roles array \(not allowed\).


