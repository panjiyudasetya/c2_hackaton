---
id: github:teqplay/vesselvoyage-backend:issue:300
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 300
title: 'Fix: Out-Of-Order Processing'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/300
labels: []
explicit_links: []
---
# Issue #300: Fix: Out-Of-Order Processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/300  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [52519adc8369...48e5ea27792e](https://github.com/teqplay/vesselvoyage-backend/compare/52519adc8369...48e5ea27792e)
**Merge commit:** [48e5ea27792e](https://github.com/teqplay/vesselvoyage-backend/commit/48e5ea27792e)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/out-of-order-processing](https://github.com/teqplay/vesselvoyage-backend/tree/fix/out-of-order-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-30T08:19:37.201446+00:00
**Status:** MERGED

No locking was applied before sending the message into the thread pool. Which meant that during \(r\)events when loads of messages from the same ship come in, they could be processed out-of-order due to them being handled in separate threads.
There was locking to guarantee multiple threads don’t both edit the ship at the same time, but without this lock there would be no ordering guarantees.

