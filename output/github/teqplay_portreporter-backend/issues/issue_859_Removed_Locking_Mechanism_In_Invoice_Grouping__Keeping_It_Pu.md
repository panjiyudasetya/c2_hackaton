---
id: github:teqplay/portreporter-backend:issue:859
source: github
type: issue
repo: teqplay/portreporter-backend
number: 859
title: Removed Locking Mechanism In Invoice Grouping. Keeping It Pure Coroutine
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/859
labels: []
explicit_links: []
---
# Issue #859: Removed Locking Mechanism In Invoice Grouping. Keeping It Pure Coroutine

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/859  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [be5148c2052a...54c82d7d9b04](https://github.com/teqplay/portreporter-backend/compare/be5148c2052a...54c82d7d9b04)
**Merge commit:** [54c82d7d9b04](https://github.com/teqplay/portreporter-backend/commit/54c82d7d9b04)
**Author:** Shravan Shetty
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [fix/improveInvoiceCSVExport](https://github.com/teqplay/portreporter-backend/tree/fix/improveInvoiceCSVExport)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:40.695355+00:00
**Status:** MERGED

Cleaned up things where XSync locks were used. Now its pure coroutine version

