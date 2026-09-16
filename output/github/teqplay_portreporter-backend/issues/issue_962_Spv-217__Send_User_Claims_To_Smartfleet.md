---
id: github:teqplay/portreporter-backend:issue:962
source: github
type: issue
repo: teqplay/portreporter-backend
number: 962
title: 'Spv-217: Send User Claims To Smartfleet'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/962
labels: []
explicit_links: []
---
# Issue #962: Spv-217: Send User Claims To Smartfleet

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/962  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [a8bd8e4a74ef...20ee647a21e8](https://github.com/teqplay/portreporter-backend/compare/a8bd8e4a74ef...20ee647a21e8)
**Merge commit:** [20ee647a21e8](https://github.com/teqplay/portreporter-backend/commit/20ee647a21e8)
**Author:** Former user
**Reviewers:** Jos de Jong, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Jos de Jong
**Source Branch:** [SPV-217-add-a-role-field-between-the-com](https://github.com/teqplay/portreporter-backend/tree/SPV-217-add-a-role-field-between-the-com)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:39.458180+00:00
**Status:** MERGED

Jira issue:  
[https://teqplaybv.atlassian.net/browse/SPV-217](https://teqplaybv.atlassian.net/browse/SPV-217)
**Before this PR:**  
Once you get hold of a fleet ID or company ID, you can make any calls you like to make changes in SmartFleet. Since SmartFleet doesn’t perform any user or company management, this wasn’t done before.
**After this PR:**  
Every \(v1\) controller has been deprecated and new v2 controllers are added so all requests must contain `SmartFleetUserClaims`, which contains the `userId`, `companyIds` and `role` of the user doing the request. This information is provided by PortReporter, so the flow is as follows:
* PortReporter is authorized to make calls in SmartFleet \(so PortReporter is allowed to make any change to any fleet\)
* PortReporter must pass the `userId`, `companyIds` and `role` of the user that is authorized on the PortReporter end
* SmartFleet will verify that those fields match with the `fleet.userId` and `fleet.companyId`, to ensure that only the right users can update \(or it’s an ADMIN user in PortReporter\)
The v1 endpoints are still available and backwards compatible, so no breaking changes. After this PR is merged and deploy, only then will SmartFleet start fully deprecating the v1 endpoints.

