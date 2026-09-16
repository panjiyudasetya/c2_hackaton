---
id: github:teqplay/portreporter-backend:issue:1225
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1225
title: Feature/Prp-1499 Bugfix Check For Invalid Email
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1225
labels: []
explicit_links: []
---
# Issue #1225: Feature/Prp-1499 Bugfix Check For Invalid Email

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1225  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4c3a7471ef13...20e05ecd04c4](https://github.com/teqplay/portreporter-backend/compare/4c3a7471ef13...20e05ecd04c4)
**Merge commit:** [20e05ecd04c4](https://github.com/teqplay/portreporter-backend/commit/20e05ecd04c4)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Wouter Naloop
**Source Branch:** [feature/PRP-1499_bugfix_check_for_invalid_email](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-1499_bugfix_check_for_invalid_email)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-03-06T14:55:19.621847+00:00
**Status:** MERGED

I’ve tested the endpoint under the following scenario’s in Postman of which first two were the original code:
* Sending no e-mail → 200 success send sof to logged in user
* Providing a valid e-mail → 200 success send sof to provided e-mail
* Providing invalid e-mail → 400 Bad Request instead of the first scenario

