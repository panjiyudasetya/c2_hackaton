---
id: github:teqplay/portreporter-backend:issue:1251
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1251
title: Prp-1830 Bugfix A Cron For Exact Where A Cron Is Stopped When Error Occurs
  And Extended Cron With Some Other Checks For More Robustness.
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1251
labels: []
explicit_links: []
---
# Issue #1251: Prp-1830 Bugfix A Cron For Exact Where A Cron Is Stopped When Error Occurs And Extended Cron With Some Other Checks For More Robustness.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1251  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [fb72f1c64551...df45a9a2cdb5](https://github.com/teqplay/portreporter-backend/compare/fb72f1c64551...df45a9a2cdb5)
**Merge commit:** [df45a9a2cdb5](https://github.com/teqplay/portreporter-backend/commit/df45a9a2cdb5)
**Author:** Shan Minh Nguyen
**Reviewers:** Darius Wattimena, Joaquin Marquez Bugella, Gavin den Hollander
**Approvers:** Former user
**Source Branch:** [feature/PRP-1830_bugfix_invoicing_cron_with_exact](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-1830_bugfix_invoicing_cron_with_exact)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-04-19T07:43:19.000846+00:00
**Status:** MERGED

* Changed level of log from WARNING to SEVERE
* Put the try/catch in the while loop so the loop isn’t stopped prematurely
* Changed a data class property from non null to optional string
* Added a log WARNING in case a property is missing retrieved from Exact

