---
id: github:teqplay/vesselvoyage-backend:issue:205
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 205
title: 'Fix: Include Ongoing Visits When Recalculating By Port'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/205
labels: []
explicit_links: []
---
# Issue #205: Fix: Include Ongoing Visits When Recalculating By Port

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/205  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [94f04f3d04ec...e5f278e463d3](https://github.com/teqplay/vesselvoyage-backend/compare/94f04f3d04ec...e5f278e463d3)
**Merge commit:** [e5f278e463d3](https://github.com/teqplay/vesselvoyage-backend/commit/e5f278e463d3)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2030-recalcule--by-port-should-include-ongoing-visits](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2030-recalcule--by-port-should-include-ongoing-visits)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-15T13:43:06.310943+00:00
**Status:** MERGED

When recalculating by port for a given time frame, you’d like to also include visits that are on the edges. If you don’t include these you’ll run into the following issue:
* a ship enters the port in late December 2022 and exits the port in early January 2023
* recalculate by port for January-December 2022
* recalculate by port for January-December 2023
The ship’s visit is overlapping both, but is not exactly inside the time window for either..
PTO has this same issue but handles it in a different way: [https://bitbucket.org/teqplay/ais-engine/pull-requests/992](https://bitbucket.org/teqplay/ais-engine/pull-requests/992)   
Just returning all ships that are inside even if that results in partial data being available. This is fine for PTO since they can check if all relevant data is available themselves.
VesselVoyage would not be able to cope with this, since you’d then try to merge incomplete data. Having visits that are missing data at the start or end, depending on which edge the ship enters/exits. VesselVoyage requires \(r\)events' guarantee of having complete data available.
Therefore, for now this problem can be fixed by allowing a certain degree of margin around the recalculation time frame. Enlarging the time window by 1 month on both sides for now.
From the PTO-end they are also going to check if this partial interests flag works fully for them or if they also need to introduce this additional margin. Depending on what they decide is a proper margin, we could take that same margin in VesselVoyage \(or move the margin into \(r\)events itself\). But for now, let’s just take an educated guess.

