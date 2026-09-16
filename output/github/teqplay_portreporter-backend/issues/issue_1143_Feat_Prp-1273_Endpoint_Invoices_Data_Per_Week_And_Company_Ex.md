---
id: github:teqplay/portreporter-backend:issue:1143
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1143
title: Feat/Prp-1273/Endpoint Invoices Data Per Week And Company Extension
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1143
labels: []
explicit_links: []
---
# Issue #1143: Feat/Prp-1273/Endpoint Invoices Data Per Week And Company Extension

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1143  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [63ffca3c3982...d276f0cbde70](https://github.com/teqplay/portreporter-backend/compare/63ffca3c3982...d276f0cbde70)
**Merge commit:** [d276f0cbde70](https://github.com/teqplay/portreporter-backend/commit/d276f0cbde70)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1273/endpoint_invoices_data_per_week_and_company_extension](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1273/endpoint_invoices_data_per_week_and_company_extension)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-08-29T08:13:26.393346+00:00
**Status:** MERGED

This new pull request for PRP-1273 includes some changes requested by @{557058:63a9abe4-1e1f-4d11-868f-93ad9505f219} after he came back from holidays.

* Week format doesn’t allow weeks with no leading 0s.
* Include in company totals \(considering all ports\) in CompanyInvoiceWeeklyTotalSummary.
* Provide a week range for weeks to obtain the invoice information by company and week.
* New separate endpoint to query by quarters the invoice information by company and range.


