---
id: github:teqplay/portreporter-backend:issue:1219
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1219
title: Feature/Prp-1531 Bugfix
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1219
labels: []
explicit_links: []
---
# Issue #1219: Feature/Prp-1531 Bugfix

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1219  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [40096fd77c20...b902a4003c4a](https://github.com/teqplay/portreporter-backend/compare/40096fd77c20...b902a4003c4a)
**Merge commit:** [b902a4003c4a](https://github.com/teqplay/portreporter-backend/commit/b902a4003c4a)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Wouter Naloop
**Source Branch:** [feature/PRP-1531_changePassword_bugfix](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-1531_changePassword_bugfix)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-03-06T10:55:51.153760+00:00
**Status:** MERGED

* Added a check to the changePassword endpoint function to check if username is provided and check if username matches your own user profile else raise badrequest.

