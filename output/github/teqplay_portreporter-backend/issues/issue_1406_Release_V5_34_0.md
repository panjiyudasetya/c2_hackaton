---
id: github:teqplay/portreporter-backend:issue:1406
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1406
title: Release/V5.34.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1406
labels: []
explicit_links: []
---
# Issue #1406: Release/V5.34.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1406  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [9b842221c8dc...b5952aca8be7](https://github.com/teqplay/portreporter-backend/compare/9b842221c8dc...b5952aca8be7)
**Merge commit:** [b5952aca8be7](https://github.com/teqplay/portreporter-backend/commit/b5952aca8be7)
**Author:** Shan Minh Nguyen
**Reviewers:** Michel Wilson, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [release/v5.34.0](https://github.com/teqplay/portreporter-backend/tree/release/v5.34.0)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-11-08T07:44:08.214524+00:00
**Status:** MERGED

* Merged in feat/[PRP-2490](https://teqplaybv.atlassian.net/browse/PRP-2490)/handle\_missing\_ship\_in\_csi \([pull request #785](https://github.com/teqplay/portreporter-backend/issues/785)\)
    [PRP-2490](https://teqplaybv.atlassian.net/browse/PRP-2490) : try-catching CSI ships not found http exceptions and returning null. Adding a schduled report in slack of these missing ships detected by PortReporter.

    * [PRP-2490](https://teqplaybv.atlassian.net/browse/PRP-2490) : try-catching CSI ships not found http exceptions and returning null. Adding a schduled report in slack of these missing ships detected by PortReporter.
    
    Approved-by: Joost Laurman

* Merged in feature/[PRP-2473](https://teqplaybv.atlassian.net/browse/PRP-2473)\_invalidating\_csi\_cache\_keys\_upon\_update \([pull request #789](https://github.com/teqplay/portreporter-backend/issues/789)\)
    * refresh portcall fetch latest dwt and shipname from csi
    
    Approved-by: Joaquin Marquez Bugella

* Merged in bugfix/try\_catch\_portcall\_message\_handler\_list\_events \([pull request #791](https://github.com/teqplay/portreporter-backend/issues/791)\)
    Bugfix/try catch portcall message handler list events

    * Added a try/catch in the forEach to not cause iteration to stop
    
    Approved-by: Joaquin Marquez Bugella



[PRP-2490]: https://teqplaybv.atlassian.net/browse/PRP-2490?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
[PRP-2490]: https://teqplaybv.atlassian.net/browse/PRP-2490?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
[PRP-2490]: https://teqplaybv.atlassian.net/browse/PRP-2490?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
