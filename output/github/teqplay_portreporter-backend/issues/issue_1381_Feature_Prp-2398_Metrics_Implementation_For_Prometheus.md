---
id: github:teqplay/portreporter-backend:issue:1381
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1381
title: Feature/Prp-2398/Metrics Implementation For Prometheus
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1381
labels: []
explicit_links:
- jira:PRP-2398
---
# Issue #1381: Feature/Prp-2398/Metrics Implementation For Prometheus

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1381  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [cae56f41a604...388ec6c6a0f1](https://github.com/teqplay/portreporter-backend/compare/cae56f41a604...388ec6c6a0f1)
**Merge commit:** [388ec6c6a0f1](https://github.com/teqplay/portreporter-backend/commit/388ec6c6a0f1)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Darius Wattimena, Shan Minh Nguyen
**Approvers:** Darius Wattimena
**Source Branch:** [feature/PRP-2398/metrics_implementation_for_prometheus](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2398/metrics_implementation_for_prometheus)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-09T15:24:11.813185+00:00
**Status:** MERGED

Sending the following metrics:
* Amount of created portcalls per port
* Amount of created portcalls without an agent
* Amount of subscriptions created per agency
* Amount of subscriptions created per terminal
* Amount of notifications per agency
* Amount of notifications per terminal
PS: Not sure what additional application properties should be set up.

