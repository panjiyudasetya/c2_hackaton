---
id: github:teqplay/portreporter-backend:issue:850
source: github
type: issue
repo: teqplay/portreporter-backend
number: 850
title: Develop
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/850
labels: []
explicit_links: []
---
# Issue #850: Develop

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/850  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [5378f6785671...1b7345dfaf93](https://github.com/teqplay/portreporter-backend/compare/5378f6785671...1b7345dfaf93)
**Merge commit:** [1b7345dfaf93](https://github.com/teqplay/portreporter-backend/commit/1b7345dfaf93)
**Author:** Shravan Shetty
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2021-01-28T12:19:28.420738+00:00
**Status:** MERGED

* bumped version to 4.2.0
* update: refactor. Split ship received in portcallEvent to ship in portcall. Split portcallEvent from PilotAvailabilityEvent
* Add exactName to company model & update INIT\_COMPANY states upon restart
* Added reset password via platform
* Some updates for the reset password call
* Revert code change in Communication
* update: review feedback
* PR Feedback: use invoiceName for exactName if non-existent
* fix: handle pilotAvailabilityEvent in a better way
* update: added Vessel is called in notification
* unit test fixes
* fix: GET instead of POST for getVopakNomination
* fix: start server even when rabbitmq connection fails
* Send Slack message when Exact process is finished


