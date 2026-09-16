---
id: github:teqplay/portreporter-backend:issue:846
source: github
type: issue
repo: teqplay/portreporter-backend
number: 846
title: Add Exactname To Company Model & Update Init_Company States Upon Restart
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/846
labels: []
explicit_links: []
---
# Issue #846: Add Exactname To Company Model & Update Init_Company States Upon Restart

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/846  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [7a411b75b18e...3912ca071eeb](https://github.com/teqplay/portreporter-backend/compare/7a411b75b18e...3912ca071eeb)
**Merge commit:** [3912ca071eeb](https://github.com/teqplay/portreporter-backend/commit/3912ca071eeb)
**Author:** Former user
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [company-exact-name](https://github.com/teqplay/portreporter-backend/tree/company-exact-name)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-01-18T11:05:32.698164+00:00
**Status:** MERGED

Added `exactName` to the company model, so from now on for Vertom etc. we can just set the `exactName` to the correct variant of the company name and we don’t have to change the `invoiceName`.  
  
Also removed the need for us to do manual changes in the DB with this PR.

When it’s a new company and we want to add it:

* we just set the general ledger account and country code and restart the Exact process as we are used to already

When the company needs another name:

* we now use the `exactName` to indicate the name that is already in Exact, now we don’t need to change this name in the DB and the phase to `INIT` anymore, because upon calling the restart process this is done for you now :slight_smile: 

Only thing that’s missing currently is the option to change the `exactName` in the frontend ofcourse.


