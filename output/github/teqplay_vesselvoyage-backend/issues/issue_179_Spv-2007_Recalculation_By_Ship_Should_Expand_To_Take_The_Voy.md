---
id: github:teqplay/vesselvoyage-backend:issue:179
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 179
title: Spv-2007 Recalculation By Ship Should Expand To Take The Voyages Into Account
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/179
labels: []
explicit_links: []
---
# Issue #179: Spv-2007 Recalculation By Ship Should Expand To Take The Voyages Into Account

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/179  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [361730d2835b...725233a275af](https://github.com/teqplay/vesselvoyage-backend/compare/361730d2835b...725233a275af)
**Merge commit:** [725233a275af](https://github.com/teqplay/vesselvoyage-backend/commit/725233a275af)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2007-recalculation-by-ship-should-expand-to-take-the-voyages-into-account](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2007-recalculation-by-ship-should-expand-to-take-the-voyages-into-account)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-25T10:28:03.521573+00:00
**Status:** MERGED

* fix: recalculating by ship should expand window
* feat: enlarge TimeWindow based on voyages
* feat: implement way to get voyage before time and after time

If a user would regenerate the selected visit below, the data in POMA could have been updated in such a way \(for instance by enlarging the port\) that the start and end times of the port entry exceed the `start` and `end` time of the recalculation. Which would result in not being able to merge back the results.
Therefore, we need to expand the `start` to the `startTime` of the previous voyage and the `end` to the `endTime` of the next voyage. That ensures we can fully regenerate a visit, even if POMA definitions have changed.

[https://vesselvoyagedev.teqplay.nl/#/ships/9211535/story/c5fe8b59-42a2-4385-9171-c0dbd99e27d3.VISIT](https://vesselvoyagedev.teqplay.nl/#/ships/9211535/story/c5fe8b59-42a2-4385-9171-c0dbd99e27d3.VISIT) 
![](https://bitbucket.org/repo/k5G8e7j/images/3368898720-image.png)

