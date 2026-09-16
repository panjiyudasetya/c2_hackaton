---
id: github:teqplay/portreporter-backend:issue:1203
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1203
title: 'Prp-1522 : Use Poma Instead Of Platform To Get Port Locations And Berths.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1203
labels: []
explicit_links:
- jira:PRP-1522
- jira:PRP-1521
---
# Issue #1203: Prp-1522 : Use Poma Instead Of Platform To Get Port Locations And Berths.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1203  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b4a2c558bfae...97291e676fe1](https://github.com/teqplay/portreporter-backend/compare/b4a2c558bfae...97291e676fe1)
**Merge commit:** [97291e676fe1](https://github.com/teqplay/portreporter-backend/commit/97291e676fe1)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [feat/PRP-1522/use_poma_instead_of_platform_to_get_port_locations_and_berths](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1522/use_poma_instead_of_platform_to_get_port_locations_and_berths)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-02-03T11:46:26.363000+00:00
**Status:** MERGED

Using Poma instead of Platform to get the port and berth information.
For this, I’ve stopped using the class `UnlocodePort`class in favor for `Port`, from Platform and Poma, respectively.
Therefore I was for forced to modify \(and limiting the changes to\) the data class `SmartFleetState` and `SFPort`.
:warning: I was about to replace any Platform Location instances by Poma Location ones \(i.e. the `SFVisit` class fields' `ataLocation` and `atdLocation`\), as but I was warned by @{5c57efac4912b735b9e0646c} about the scope being bigger than this card \(and he’s right, but I’m having two thought-flows\).  
I foresee potential issues when having to make any logic between `SFVisit.ataLocation` and `SFVisit.port.location`, as being the whole point of the card replacing poma by platform to avoid smartfleet issues \(see description of the user story [https://teqplaybv.atlassian.net/browse/PRP-1521](https://teqplaybv.atlassian.net/browse/PRP-1521) \).

