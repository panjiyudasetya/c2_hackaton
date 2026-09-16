---
id: github:teqplay/vesselvoyage-backend:issue:369
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 369
title: Spv-2323 Post Processing Service
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/369
labels: []
explicit_links: []
---
# Issue #369: Spv-2323 Post Processing Service

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/369  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [63c07d0f37da...b5f12c332248](https://github.com/teqplay/vesselvoyage-backend/compare/63c07d0f37da...b5f12c332248)
**Merge commit:** [b5f12c332248](https://github.com/teqplay/vesselvoyage-backend/commit/b5f12c332248)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2323-post-processing-service](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2323-post-processing-service)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-12-02T13:25:44.963745+00:00
**Status:** MERGED

This PR contains Rowdey his intial work on the post-processing service \+ some adjusted by me to finalise the feature
So in short this PR adds the following:
1. Service that can schedule post processing steps in the background \(e.g. calculating the slow moving periods\)
2. Post processing steps inside the real-time processing.
3. The triggers when to actually call the post processing service which are as followed:
    1. When we create a new Visit, meaning we should calculate the drifting for the finished Voyage
    2. When we create a new Voyage, meaning we should calculate the drifting for the finished Visit
    3. When we create a new 0-second Voyage and new Visit, meaning we should calculate the drifting for the finished Visit before the 0-second Voyage.
    

