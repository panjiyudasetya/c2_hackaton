---
id: github:teqplay/portreporter-backend:issue:1392
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1392
title: Release/5.32.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1392
labels: []
explicit_links: []
---
# Issue #1392: Release/5.32.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1392  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ac255f96d24e...2c71a78ae89a](https://github.com/teqplay/portreporter-backend/compare/ac255f96d24e...2c71a78ae89a)
**Merge commit:** [2c71a78ae89a](https://github.com/teqplay/portreporter-backend/commit/2c71a78ae89a)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [release/5.32.0](https://github.com/teqplay/portreporter-backend/tree/release/5.32.0)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-09-18T08:47:57.814832+00:00
**Status:** MERGED

* Actuator implementation by PortReporter removed and now included through skeleton
    * Removed annotations that was working with the old actuator
    * Added 2 custom copies of skeleton actuator plugin to work with smartfleet and platform
    
* Metrics added for grafana
* Added PortCallMessageHandler handling of list of Portcall events instead of only singular portcalls to determine later the most likely portcall to process
* Vopak rabbitmq queue removed

