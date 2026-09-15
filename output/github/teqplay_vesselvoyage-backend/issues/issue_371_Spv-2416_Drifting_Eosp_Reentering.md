---
id: github:teqplay/vesselvoyage-backend:issue:371
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 371
title: Spv-2416 Drifting Eosp Reentering
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/371
labels: []
explicit_links: []
---
# Issue #371: Spv-2416 Drifting Eosp Reentering

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/371  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [82d32db41ac3...155f97aa2f4d](https://github.com/teqplay/vesselvoyage-backend/compare/82d32db41ac3...155f97aa2f4d)
**Merge commit:** [155f97aa2f4d](https://github.com/teqplay/vesselvoyage-backend/commit/155f97aa2f4d)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2416-drifting-eosp-reentering](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2416-drifting-eosp-reentering)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-22T15:24:07.480572+00:00
**Status:** MERGED

Made it so we resume a previously finished visit when going back to the same EOSP but never entering a port.
Example case [https://vesselvoyagedev.teqplay.nl/#/ships/9511442/story/048c9ef3-f884-4815-aae9-13e3ec5a1357.VOYAGE](https://vesselvoyagedev.teqplay.nl/#/ships/9511442/story/048c9ef3-f884-4815-aae9-13e3ec5a1357.VOYAGE).
NOTE: this does go wrong when the next port isn’t drawn in and we come back to the same port eosp. I did talk about this with Gavin if that was a problem \(as he initially asked for this functionality\) but we decided that it isn’t an issue as the context mapping is then just not on par, meaning that should just be improved.

