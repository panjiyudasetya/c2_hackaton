---
id: github:teqplay/portreporter-backend:issue:954
source: github
type: issue
repo: teqplay/portreporter-backend
number: 954
title: Prp-6 Extendnominationsearchbycontainingstring
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/954
labels: []
explicit_links: []
---
# Issue #954: Prp-6 Extendnominationsearchbycontainingstring

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/954  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d6e6e3d50d7f...fbd534c28407](https://github.com/teqplay/portreporter-backend/compare/d6e6e3d50d7f...fbd534c28407)
**Merge commit:** [fbd534c28407](https://github.com/teqplay/portreporter-backend/commit/fbd534c28407)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-6-extendNominationSearchByContainingString](https://github.com/teqplay/portreporter-backend/tree/PRP-6-extendNominationSearchByContainingString)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-09-29T09:45:35.730462+00:00
**Status:** MERGED

**What it is about:**

Making possible to search nominations based on a containing pattern, i.e., searching all nominations which port contains “NL”.  
  
**Consisting in:**

* Enabling containing search \(using regex\) for the nominations/get endpoint criteria
* Skipping blank parameters
* Setting default values for NominationLogic.getNominations' parameters


