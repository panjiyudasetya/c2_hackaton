---
id: github:teqplay/portreporter-backend:issue:1154
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1154
title: 'Prp-1465 : Extend Invoice Search With Arguments For Billing Mode And Shipping
  Line Id.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1154
labels: []
explicit_links:
- jira:PRP-1465
---
# Issue #1154: Prp-1465 : Extend Invoice Search With Arguments For Billing Mode And Shipping Line Id.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1154  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [63a6967d2e87...3b0ac2074cc1](https://github.com/teqplay/portreporter-backend/compare/63a6967d2e87...3b0ac2074cc1)
**Merge commit:** [3b0ac2074cc1](https://github.com/teqplay/portreporter-backend/commit/3b0ac2074cc1)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Darius Wattimena
**Approvers:** Former user
**Source Branch:** [feat/PRP-1465/extend_invoice_search](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1465/extend_invoice_search)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-12T12:56:01.956849+00:00
**Status:** MERGED

The new two arguments are:

* shippingLineId \(for filtering by `invoiceRows.shippingLineId`\)
* mode \(for direct or indirect modes\).


