---
id: github:teqplay/portreporter-backend:issue:1054
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1054
title: Prp-772/Feat/Improve Update Nomination By Matching Portcall
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1054
labels: []
explicit_links: []
---
# Issue #1054: Prp-772/Feat/Improve Update Nomination By Matching Portcall

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1054  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e0e81c90c666...bbb826be5146](https://github.com/teqplay/portreporter-backend/compare/e0e81c90c666...bbb826be5146)
**Merge commit:** [bbb826be5146](https://github.com/teqplay/portreporter-backend/commit/bbb826be5146)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-772/feat/improve_update_nomination_by_matching_portcall](https://github.com/teqplay/portreporter-backend/tree/PRP-772/feat/improve_update_nomination_by_matching_portcall)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-03-14T13:22:51.070021+00:00
**Status:** MERGED

Mainly **two things** here:

1. Improve **updateNominationByMatchingPortCall\(PortCall\)** checking that the given portcall is also the bestMatched for the best MatchedNomination for that portcall.
2. Refactoring methods:

    * `getMatchingPortCallByNomination(...)` → `getBestMatchingPortCallForNomination(...)`
    * `getMatchingNominationByPortCall(...)` → `getBestMatchingNominationForPortCall(...)`
    


