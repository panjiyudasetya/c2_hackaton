---
id: github:teqplay/portreporter-backend:issue:1416
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1416
title: Dev-448 Updating To Spring 3.1 Bitbucket Pipeline Fix
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1416
labels: []
explicit_links:
- jira:DEV-448
- jira:PRP-2515
---
# Issue #1416: Dev-448 Updating To Spring 3.1 Bitbucket Pipeline Fix

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1416  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [18aaec8153bd...fda7145e0f67](https://github.com/teqplay/portreporter-backend/compare/18aaec8153bd...fda7145e0f67)
**Merge commit:** [fda7145e0f67](https://github.com/teqplay/portreporter-backend/commit/fda7145e0f67)
**Author:** Jamie de Leest
**Reviewers:** 
**Approvers:** Joaquin Marquez Bugella, Shan Minh Nguyen
**Source Branch:** [DEV-448-updating-to-spring-3.1-bitbucket-pipeline-fix](https://github.com/teqplay/portreporter-backend/tree/DEV-448-updating-to-spring-3.1-bitbucket-pipeline-fix)
**Destination Branch:** [DEV-448-updating-to-spring-3.1](https://github.com/teqplay/portreporter-backend/tree/DEV-448-updating-to-spring-3.1)
**Closed On:** 2025-01-13T13:14:01.349661+00:00
**Status:** MERGED

* Merged in feature/PRP-2515\_setup\_portcall\_for\_prometheus \(pull request #800\)
    Feature/PRP-2515 setup portcall statistics for prometheus

    * Added merics for portcalls per port and with/without agent per time range
    * Merged develop into feature/PRP-2515\_setup\_portcall\_for\_prometheus
    * Merged develop into feature/PRP-2515\_setup\_portcall\_for\_prometheus
    * Merge branch 'develop' into feature/PRP-2515\_setup\_portcall\_for\_prometheus
    * Merged develop and fixed conflicts
    * Added braces to a filter for clear code
    * KTLint
    * Reworked code to be more event based for metrics using the cron as the trigger
    * Reverted function type to List instead of MutableList
    * Added braces to a statement for clearer format
    
    Approved-by: Joost Dambrink

* Release version 5.35.0
* Setting snapshot version
* test: adding stack trace to bitbucket pipelines for testing purposes
* fix: added the schedule.portCallStatistics for the test properties

