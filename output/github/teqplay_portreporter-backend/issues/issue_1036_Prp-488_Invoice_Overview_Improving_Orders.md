---
id: github:teqplay/portreporter-backend:issue:1036
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1036
title: Prp-488 Invoice Overview Improving Orders
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1036
labels: []
explicit_links: []
---
# Issue #1036: Prp-488 Invoice Overview Improving Orders

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1036  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [997f13258cf0...7a9a1621fbaa](https://github.com/teqplay/portreporter-backend/compare/997f13258cf0...7a9a1621fbaa)
**Merge commit:** [7a9a1621fbaa](https://github.com/teqplay/portreporter-backend/commit/7a9a1621fbaa)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop
**Source Branch:** [PRP488_invoice-overview-improving-orders](https://github.com/teqplay/portreporter-backend/tree/PRP488_invoice-overview-improving-orders)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-01-28T14:27:59.627622+00:00
**Status:** MERGED

* Fixed an issue where invoice orders of blacklisted vessels wouldn't be taken into account when calculating the statistics
* Made an exception how orders are calculated in the spreadsheet
* Added support for indirect shippinglines


