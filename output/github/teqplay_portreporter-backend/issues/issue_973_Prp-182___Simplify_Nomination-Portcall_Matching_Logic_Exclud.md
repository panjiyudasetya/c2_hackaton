---
id: github:teqplay/portreporter-backend:issue:973
source: github
type: issue
repo: teqplay/portreporter-backend
number: 973
title: 'Prp-182 : Simplify Nomination-Portcall Matching Logic Excluding The Shippinglineid'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/973
labels: []
explicit_links:
- jira:PRP-182
---
# Issue #973: Prp-182 : Simplify Nomination-Portcall Matching Logic Excluding The Shippinglineid

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/973  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [a86342c2598d...09e800461846](https://github.com/teqplay/portreporter-backend/compare/a86342c2598d...09e800461846)
**Merge commit:** [09e800461846](https://github.com/teqplay/portreporter-backend/commit/09e800461846)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Joost Laurman
**Source Branch:** [PRP-182-use-portcall-nomination-matching-on-portcall-record](https://github.com/teqplay/portreporter-backend/tree/PRP-182-use-portcall-nomination-matching-on-portcall-record)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-10-26T16:12:23.569687+00:00
**Status:** MERGED

As the title says, attempting to match a nomination to a portcall when the second gets updated its shippinglineid \(needed for properly matching a nomination\).

