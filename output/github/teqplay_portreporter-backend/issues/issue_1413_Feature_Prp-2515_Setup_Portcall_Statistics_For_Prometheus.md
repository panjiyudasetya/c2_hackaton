---
id: github:teqplay/portreporter-backend:issue:1413
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1413
title: Feature/Prp-2515 Setup Portcall Statistics For Prometheus
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1413
labels: []
explicit_links: []
---
# Issue #1413: Feature/Prp-2515 Setup Portcall Statistics For Prometheus

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1413  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [c891e365ce48...878607a7b324](https://github.com/teqplay/portreporter-backend/compare/c891e365ce48...878607a7b324)
**Merge commit:** [878607a7b324](https://github.com/teqplay/portreporter-backend/commit/878607a7b324)
**Author:** Shan Minh Nguyen
**Reviewers:** Michel Wilson, Joost Dambrink, Joaquin Marquez Bugella
**Approvers:** Joost Dambrink
**Source Branch:** [feature/PRP-2515_setup_portcall_for_prometheus](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2515_setup_portcall_for_prometheus)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2025-01-06T07:37:38.579929+00:00
**Status:** MERGED

* Added merics for portcalls per port and with/without agent per time range
* Added braces to a filter for clear code
* KTLint
* Reworked code to be more event based for metrics using the cron as the trigger

