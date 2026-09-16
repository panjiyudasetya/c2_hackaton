---
id: github:teqplay/portreporter-backend:issue:1390
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1390
title: Interceptor Fixes And Logging And Skeleton Version Increased
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1390
labels: []
explicit_links: []
---
# Issue #1390: Interceptor Fixes And Logging And Skeleton Version Increased

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1390  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d5c0ad34c8c5...b50678e4663e](https://github.com/teqplay/portreporter-backend/compare/d5c0ad34c8c5...b50678e4663e)
**Merge commit:** [b50678e4663e](https://github.com/teqplay/portreporter-backend/commit/b50678e4663e)
**Author:** Shan Minh Nguyen
**Reviewers:** Michel Wilson, Darius Wattimena, Joost Dambrink
**Approvers:** Darius Wattimena
**Source Branch:** [feature/actuator_interceptor_fixes](https://github.com/teqplay/portreporter-backend/tree/feature/actuator_interceptor_fixes)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-09-11T08:58:57.537258+00:00
**Status:** MERGED

Same as skeleton actuator plugin:  
- Added more logging  
- Better exception handling with one method  
- Exception handling based on status code in case of no failure received from external request

