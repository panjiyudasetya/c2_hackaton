---
id: github:teqplay/portreporter-backend:issue:1244
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1244
title: 'Hotfix V5.23.4: Creation Of A Invoice-Sending Flow Similar To Vopak For Wilhelmsen.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1244
labels: []
explicit_links: []
---
# Issue #1244: Hotfix V5.23.4: Creation Of A Invoice-Sending Flow Similar To Vopak For Wilhelmsen.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1244  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [f16e1672893d...6f900e68591f](https://github.com/teqplay/portreporter-backend/compare/f16e1672893d...6f900e68591f)
**Merge commit:** [6f900e68591f](https://github.com/teqplay/portreporter-backend/commit/6f900e68591f)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Gavin den Hollander
**Approvers:** Joost Laurman
**Source Branch:** [hotfix/add_new_edi_flow](https://github.com/teqplay/portreporter-backend/tree/hotfix/add_new_edi_flow)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2023-04-03T08:20:11.409707+00:00
**Status:** MERGED

As Wilhelmsen has bought Vopak agencies, they’re in the transfer process, so a new set of Wilhelmsen agencies have been created in PortReporter.
They should be receiving their invoices to their own EDI mail addresses, but the agencies transfer is still not 100% done \(on their side\).  
So some Vopak agencies still need to get their invoices in their EDI email addresses while Wilhelmsen ones theirs.
Eventually, Vopak flow will disappear, so, there’s no new reason to develop a more configurable flow for this feature.

