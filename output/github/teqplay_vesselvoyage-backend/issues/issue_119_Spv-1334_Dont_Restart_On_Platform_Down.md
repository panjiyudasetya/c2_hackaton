---
id: github:teqplay/vesselvoyage-backend:issue:119
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 119
title: Spv-1334 Dont Restart On Platform Down
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/119
labels: []
explicit_links: []
---
# Issue #119: Spv-1334 Dont Restart On Platform Down

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/119  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ca15403267fb...ef9be800cf53](https://github.com/teqplay/vesselvoyage-backend/compare/ca15403267fb...ef9be800cf53)
**Merge commit:** [ef9be800cf53](https://github.com/teqplay/vesselvoyage-backend/commit/ef9be800cf53)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson
**Approvers:** Michel Wilson
**Source Branch:** [SPV-1334_dont_restart_on_platform_down](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1334_dont_restart_on_platform_down)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-03-20T15:01:35.114258+00:00
**Status:** MERGED

* Make it so VesselVoyage doesn't restart and stops processing when global is down
* Changed the logic to be instead check every minute without relying on the health check
* Fixed an issue where the ProcessingService bean couldn't be initialized correctly
* Cleaned up the code
* Catch all exceptions as we don't do anything with the result
* Code cleanup
* More code cleanup
* Some minor rewording

