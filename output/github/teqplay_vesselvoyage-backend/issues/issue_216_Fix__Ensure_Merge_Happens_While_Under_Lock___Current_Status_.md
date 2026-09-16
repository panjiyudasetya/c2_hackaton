---
id: github:teqplay/vesselvoyage-backend:issue:216
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 216
title: 'Fix: Ensure Merge Happens While Under Lock & Current Status Is Refreshed'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/216
labels: []
explicit_links:
- jira:SPV-2086
- jira:SPV-2076
---
# Issue #216: Fix: Ensure Merge Happens While Under Lock & Current Status Is Refreshed

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/216  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [68681a0dc605...babf383f3cbc](https://github.com/teqplay/vesselvoyage-backend/compare/68681a0dc605...babf383f3cbc)
**Merge commit:** [babf383f3cbc](https://github.com/teqplay/vesselvoyage-backend/commit/babf383f3cbc)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2086-ensure-locking-is-used-when-merging](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2086-ensure-locking-is-used-when-merging)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-04-24T07:20:06.690193+00:00
**Status:** MERGED

Merging V1/V2 requires us to lock, we don’t want to be updating data while another thread is making updates as well. Also, we need to make sure to reset the status, previous/current visit/voyage, to ensure any updates we make while merging are also reflected in the status. Otherwise this could lead into desyncs between the database and the in-memory state.

