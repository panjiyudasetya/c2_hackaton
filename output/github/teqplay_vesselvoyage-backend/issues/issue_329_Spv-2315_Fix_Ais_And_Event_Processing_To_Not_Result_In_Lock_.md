---
id: github:teqplay/vesselvoyage-backend:issue:329
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 329
title: Spv-2315 Fix Ais And Event Processing To Not Result In Lock Contentions
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/329
labels: []
explicit_links: []
---
# Issue #329: Spv-2315 Fix Ais And Event Processing To Not Result In Lock Contentions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/329  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [362367cd6c1a...3348e6e186c8](https://github.com/teqplay/vesselvoyage-backend/compare/362367cd6c1a...3348e6e186c8)
**Merge commit:** [3348e6e186c8](https://github.com/teqplay/vesselvoyage-backend/commit/3348e6e186c8)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Leon Joosse, Michel Wilson
**Source Branch:** [fix-deadlock](https://github.com/teqplay/vesselvoyage-backend/tree/fix-deadlock)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-03T15:22:57.100887+00:00
**Status:** MERGED

After reworking this quite a bit, vesselvoyage is somewhat stable now, on more memory leaks or dead locks on this part \(although time will tell\).
Please have a look now at the PR, and if it is too much then lets maybe plan a session where we go over the overall changes functional wise.
That being said, the key changes are:
1. Locking is now done in one place by the `ImoLockService`.
    1. This mechanism uses a spin lock, fully replacing the mutex library that was used first.
    2. This locks for both V1 and V2 at the same time.
    3. This does not cover the locking for V1 automatic processes, so this might need some more work here depending on the side effects it has.
    
2. Add support for buffering when revents is merging back and event process and ais processing is blocked.  
  \(This might need some good checks if it actually works but it is hard to test \+ with the latest changes this logic might never be able to trigger\)
3. On start up load all ships that got switch from visit/voyage in the last 24 hours to load the “most recent“ ships before doing any processing.
4. AIS processing is now a push consumer instead of it being a fetch \(pull\) consumer.
5. AIS processing is now done in parallel, this improves the throughput to ~10k msg/s from the old ~1.5k msg/s which was just enough to keep up with the amount of historic messages.

