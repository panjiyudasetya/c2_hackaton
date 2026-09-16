---
id: github:teqplay/portreporter-backend:issue:957
source: github
type: issue
repo: teqplay/portreporter-backend
number: 957
title: Include Invoiced Flag To Filter Invoices Whether They Are Invoiced Or Not
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/957
labels: []
explicit_links:
- jira:PRP-47
---
# Issue #957: Include Invoiced Flag To Filter Invoices Whether They Are Invoiced Or Not

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/957  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e1c173c83a13...4ea7ec23cb74](https://github.com/teqplay/portreporter-backend/compare/e1c173c83a13...4ea7ec23cb74)
**Merge commit:** [4ea7ec23cb74](https://github.com/teqplay/portreporter-backend/commit/4ea7ec23cb74)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Former user
**Source Branch:** [PRP-47-ExtendingNominationSearchByInvoicedFlag](https://github.com/teqplay/portreporter-backend/tree/PRP-47-ExtendingNominationSearchByInvoicedFlag)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-09-30T08:38:42.926612+00:00
**Status:** MERGED

Given that the invoiced status of a Nomination is whether its invoiceId is filled with a valid \(not null, not empty and not blank\) value, this PR is about to adding a new boolean parameter “invoiced” which will:
* if not provided, not taking invoiced status into account.
* if provided and true, add to the filtering criteria the invoiced status.
* if provided and false, add to the filtering criteria the not-invoiced status.
Jira Ticket linked: [https://teqplaybv.atlassian.net/browse/PRP-47](https://teqplaybv.atlassian.net/browse/PRP-47)

