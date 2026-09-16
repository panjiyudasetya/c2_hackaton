---
id: github:teqplay/portreporter-backend:issue:1024
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1024
title: Prp-488 Initial Invoice Overview Implementation
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1024
labels: []
explicit_links: []
---
# Issue #1024: Prp-488 Initial Invoice Overview Implementation

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1024  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [8a21f6f7d8dc...364ff957fc6a](https://github.com/teqplay/portreporter-backend/compare/8a21f6f7d8dc...364ff957fc6a)
**Merge commit:** [364ff957fc6a](https://github.com/teqplay/portreporter-backend/commit/364ff957fc6a)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-488_initial-invoice-overview-implementation](https://github.com/teqplay/portreporter-backend/tree/PRP-488_initial-invoice-overview-implementation)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-01-14T14:34:32.618718+00:00
**Status:** MERGED

Adds a new `/v1/invoices/exportOverview` call which lets you download a spreadsheet that will be later used by Richard and Christina.

NOTE: all the code in `InvoiceOverviewSheetExportLogic` is currently put in a separate class as the plan is to eventually remove the whole process with exporting it as a sheet, and instead have it in the front-end itself.

