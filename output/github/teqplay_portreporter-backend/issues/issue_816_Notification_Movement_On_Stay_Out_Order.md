---
id: github:teqplay/portreporter-backend:issue:816
source: github
type: issue
repo: teqplay/portreporter-backend
number: 816
title: Notification Movement On Stay Out Order
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/816
labels: []
explicit_links: []
---
# Issue #816: Notification Movement On Stay Out Order

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/816  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [02462843148c...c965507a6b1c](https://github.com/teqplay/portreporter-backend/compare/02462843148c...c965507a6b1c)
**Merge commit:** [c965507a6b1c](https://github.com/teqplay/portreporter-backend/commit/c965507a6b1c)
**Author:** Former user
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [notification-movement-on-stay-out-order](https://github.com/teqplay/portreporter-backend/tree/notification-movement-on-stay-out-order)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2020-11-09T09:38:54.215504+00:00
**Status:** MERGED

* Notify subscribers for movement on stay out order
* Upped default subscriptions number for tests

When an `anchorArea.atd.vessel` is encountered and notifications are being sent, there is a check if the most recent order is a stay out order for that given portcall. If that’s so, another notification will be triggered under the `MOVEMENT_ON_STAY_OUT_ORDER` subscription.

I’m not really sure what the precise content of the notification should be, so for now I added: `Vessel starting moving, but must stay out of port according to given stay out order`

