---
id: github:teqplay/portreporter-backend:issue:1286
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1286
title: Feature/Prp-1830 New Config Setting To Start From Minimum Invoice Number
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1286
labels: []
explicit_links: []
---
# Issue #1286: Feature/Prp-1830 New Config Setting To Start From Minimum Invoice Number

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1286  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [09811a686b8f...5757dd42daaa](https://github.com/teqplay/portreporter-backend/compare/09811a686b8f...5757dd42daaa)
**Merge commit:** [5757dd42daaa](https://github.com/teqplay/portreporter-backend/commit/5757dd42daaa)
**Author:** Shan Minh Nguyen
**Reviewers:** Joost Laurman, Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-1830_new_config_setting_to_start_from_minimum_invoice_number](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-1830_new_config_setting_to_start_from_minimum_invoice_number)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-08T07:48:18.111473+00:00
**Status:** MERGED

* Added new config setting to start from a minimum invoiceNumber instead of all the way from the start.
* Set starting number for config property to 0.
Currently in live there’s many unpaid invoices, more than the Daily limit of calls the Exact API allows.  
According to Richard some of them dates back from 2020, so a suggestion was made to add a config property for the starting invoiceNumber which he can set so it ignores a lot of old invoices in Exact.

