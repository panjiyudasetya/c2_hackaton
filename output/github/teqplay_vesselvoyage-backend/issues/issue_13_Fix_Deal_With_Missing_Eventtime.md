---
id: github:teqplay/vesselvoyage-backend:issue:13
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 13
title: Fix/Deal With Missing Eventtime
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/13
labels: []
explicit_links: []
---
# Issue #13: Fix/Deal With Missing Eventtime

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/13  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0027f16a1ca2...8b0be1aa4156](https://github.com/teqplay/vesselvoyage-backend/compare/0027f16a1ca2...8b0be1aa4156)
**Merge commit:** [8b0be1aa4156](https://github.com/teqplay/vesselvoyage-backend/commit/8b0be1aa4156)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/deal_with_missing_eventtime](https://github.com/teqplay/vesselvoyage-backend/tree/fix/deal_with_missing_eventtime)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-23T08:51:45.691372+00:00
**Status:** MERGED

Old teqplay events do not have the property `eventTime`. With this PR, `datetime` will now be used when `eventTime` is missing.

I spend some time writing unit tests for all these util functions.

