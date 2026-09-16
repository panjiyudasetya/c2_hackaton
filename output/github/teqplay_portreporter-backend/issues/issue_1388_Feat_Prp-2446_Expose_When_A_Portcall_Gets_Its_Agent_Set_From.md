---
id: github:teqplay/portreporter-backend:issue:1388
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1388
title: Feat/Prp-2446/Expose When A Portcall Gets Its Agent Set From Null To A Non
  Null Value
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1388
labels: []
explicit_links:
- jira:PRP-2446
---
# Issue #1388: Feat/Prp-2446/Expose When A Portcall Gets Its Agent Set From Null To A Non Null Value

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1388  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b5f03492988b...e1e286ecc389](https://github.com/teqplay/portreporter-backend/compare/b5f03492988b...e1e286ecc389)
**Merge commit:** [e1e286ecc389](https://github.com/teqplay/portreporter-backend/commit/e1e286ecc389)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Leon Joosse
**Approvers:** Joost Laurman
**Source Branch:** [feat/PRP-2446/expose_when_a_portcall_gets_its_agent_set_from_null_to_a_non_null_value](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2446/expose_when_a_portcall_gets_its_agent_set_from_null_to_a_non_null_value)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-09-03T08:38:50.968748+00:00
**Status:** MERGED

Changes:
* fix notification metric not being sent.
* report to prometheus when a portcall's agent is set when it was null before.

