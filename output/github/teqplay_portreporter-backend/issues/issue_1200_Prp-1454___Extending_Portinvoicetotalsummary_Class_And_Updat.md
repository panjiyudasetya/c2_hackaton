---
id: github:teqplay/portreporter-backend:issue:1200
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1200
title: 'Prp-1454 : Extending Portinvoicetotalsummary Class And Update Its Content
  (Separate Portcall Invoices And Portcall Order Invoices).'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1200
labels: []
explicit_links:
- jira:PRP-1454
---
# Issue #1200: Prp-1454 : Extending Portinvoicetotalsummary Class And Update Its Content (Separate Portcall Invoices And Portcall Order Invoices).

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1200  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [828864db7fe1...0a441b4d45f7](https://github.com/teqplay/portreporter-backend/compare/828864db7fe1...0a441b4d45f7)
**Merge commit:** [0a441b4d45f7](https://github.com/teqplay/portreporter-backend/commit/0a441b4d45f7)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [fix/PRP-1454/extending_PortInvoiceTotalSummary_class_data_model_and_content](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1454/extending_PortInvoiceTotalSummary_class_data_model_and_content)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-01-31T16:59:23.829081+00:00
**Status:** MERGED

Extending the data model `PortInvoiceTotalSummary` to include a new classification of credit and debit new sub totals \(see auxiliary class `DetailedInvoiceInfo`\). Also, some fields have been renamed.
Together with this, the `CompanyInvoicePeriodTotalSummary` has also been adapted.

