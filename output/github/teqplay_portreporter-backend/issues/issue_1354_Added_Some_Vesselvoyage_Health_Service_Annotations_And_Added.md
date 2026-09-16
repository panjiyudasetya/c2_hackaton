---
id: github:teqplay/portreporter-backend:issue:1354
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1354
title: Added Some Vesselvoyage Health Service Annotations And Added Defaults To Config
  So That A Developer Doesn'T Send Notifications By Accident Without Having Some Identifications
  From The User Sending In Notifications
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1354
labels: []
explicit_links: []
---
# Issue #1354: Added Some Vesselvoyage Health Service Annotations And Added Defaults To Config So That A Developer Doesn'T Send Notifications By Accident Without Having Some Identifications From The User Sending In Notifications

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1354  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [9f4625651ecd...6e2773d04947](https://github.com/teqplay/portreporter-backend/compare/9f4625651ecd...6e2773d04947)
**Merge commit:** [6e2773d04947](https://github.com/teqplay/portreporter-backend/commit/6e2773d04947)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Former user
**Source Branch:** [feature/PRP_added_some_config_defaults_and_extra_vesselvoyage_service_annotations](https://github.com/teqplay/portreporter-backend/tree/feature/PRP_added_some_config_defaults_and_extra_vesselvoyage_service_annotations)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-12-06T08:08:02.756910+00:00
**Status:** MERGED

Created a separate PR instead of another one.  
Mostly things related to possibly me accidentally sending out invoices to portreporter during testing all endpoints.  
These changes should allow for others to see it’s from testing since it didn’t had any prefixes before.

