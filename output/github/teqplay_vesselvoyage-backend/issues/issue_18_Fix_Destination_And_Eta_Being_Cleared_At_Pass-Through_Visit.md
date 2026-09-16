---
id: github:teqplay/vesselvoyage-backend:issue:18
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 18
title: Fix Destination And Eta Being Cleared At Pass-Through Visit
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/18
labels: []
explicit_links: []
---
# Issue #18: Fix Destination And Eta Being Cleared At Pass-Through Visit

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/18  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [71c9b7c71fba...4d5308115445](https://github.com/teqplay/vesselvoyage-backend/compare/71c9b7c71fba...4d5308115445)
**Merge commit:** [4d5308115445](https://github.com/teqplay/vesselvoyage-backend/commit/4d5308115445)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/keep_destination_after_passthrough](https://github.com/teqplay/vesselvoyage-backend/tree/fix/keep_destination_after_passthrough)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-30T15:31:44.470718+00:00
**Status:** MERGED

The problem was that there was code in place to clear eta/destination when starting a new visit \(via `startVisit (event: PortEvent, currentVoyage: Voyage)`\). That is a problem when you’re only passing through a port.

We must have a way to get rid of outdated eta/destination information one way or another.

I have now implemented the following logic: destination and eta is always copied from one visit/voyage to the next, unless it is outdated. It is outdated when the time the eta/destination was last updated is before the start of the previous visit/voyage. Does that make sense?

An alternative approach can be to not copy eta/destination when starting a visit \(the old behavior\), and when deleting a pass-through visit, restore the eta/destination correctly.

