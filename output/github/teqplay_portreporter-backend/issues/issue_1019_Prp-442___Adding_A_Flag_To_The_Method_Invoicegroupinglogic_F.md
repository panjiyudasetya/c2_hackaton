---
id: github:teqplay/portreporter-backend:issue:1019
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1019
title: 'Prp-442 : Adding A Flag To The Method Invoicegroupinglogic.Fetchgroupingbyportcalls(...)
  So To Returns Portcalls To Invoice With The Portcall Liases Or Teqplay Portcalls'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1019
labels: []
explicit_links: []
---
# Issue #1019: Prp-442 : Adding A Flag To The Method Invoicegroupinglogic.Fetchgroupingbyportcalls(...) So To Returns Portcalls To Invoice With The Portcall Liases Or Teqplay Portcalls

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1019  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [1071d350be2b...151df2747383](https://github.com/teqplay/portreporter-backend/compare/1071d350be2b...151df2747383)
**Merge commit:** [151df2747383](https://github.com/teqplay/portreporter-backend/commit/151df2747383)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Joost Laurman
**Source Branch:** [PRP-442/fix/Nominations_for_Portcalls_with_aliases_not_found_in_invoicing_process](https://github.com/teqplay/portreporter-backend/tree/PRP-442/fix/Nominations_for_Portcalls_with_aliases_not_found_in_invoicing_process)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-12-30T18:28:36.259644+00:00
**Status:** MERGED

I’ve added the flag `portcallsByAliasWhenTheyExist` to the method `invoiceGroupingLogic.fetchGroupingByPortcalls(...)` \(defaulted to true to maintain current behaviour\) so when false, it doesn’t return the portcallAliases, but the Teqplay portcalls.
Then, when fetching the portcalls to liable to invoicing for exporting the CSV, this flag is set to false.
This way, nominations can match properly and the column isNominated is correctly set in the case of portcallaliases.

