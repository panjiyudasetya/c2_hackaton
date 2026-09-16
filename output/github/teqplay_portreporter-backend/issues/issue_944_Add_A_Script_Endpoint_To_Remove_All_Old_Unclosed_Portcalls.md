---
id: github:teqplay/portreporter-backend:issue:944
source: github
type: issue
repo: teqplay/portreporter-backend
number: 944
title: Add A Script Endpoint To Remove All Old Unclosed Portcalls
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/944
labels: []
explicit_links: []
---
# Issue #944: Add A Script Endpoint To Remove All Old Unclosed Portcalls

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/944  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [3a485b796d08...4bcf333e2984](https://github.com/teqplay/portreporter-backend/compare/3a485b796d08...4bcf333e2984)
**Merge commit:** [4bcf333e2984](https://github.com/teqplay/portreporter-backend/commit/4bcf333e2984)
**Author:** Wouter Naloop
**Reviewers:** Joost Laurman, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/portcall_end_script](https://github.com/teqplay/portreporter-backend/tree/feat/portcall_end_script)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-09-08T12:25:41.373115+00:00
**Status:** MERGED

In portreporter there are alot of open portcalls, with this script you can close them up to 2 months ago. these 2 months are a sort of safety measure to not remove portcalls that could still happen in the near future, or have been reopened

