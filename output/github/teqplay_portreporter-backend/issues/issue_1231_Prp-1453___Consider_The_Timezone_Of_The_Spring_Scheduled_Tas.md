---
id: github:teqplay/portreporter-backend:issue:1231
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1231
title: 'Prp-1453 : Consider The Timezone Of The Spring Scheduled Tasks In The Calculation
  Of Week-Shifting Seconds.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1231
labels: []
explicit_links: []
---
# Issue #1231: Prp-1453 : Consider The Timezone Of The Spring Scheduled Tasks In The Calculation Of Week-Shifting Seconds.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1231  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [2e5e8a5a3cc7...b7cfd945fd00](https://github.com/teqplay/portreporter-backend/compare/2e5e8a5a3cc7...b7cfd945fd00)
**Merge commit:** [b7cfd945fd00](https://github.com/teqplay/portreporter-backend/commit/b7cfd945fd00)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Michel Wilson, Wouter Naloop, Darius Wattimena, Gavin den Hollander
**Approvers:** Michel Wilson
**Source Branch:** [fix/PRP-1453/consider_timezone_in_scheduled_tasks](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1453/consider_timezone_in_scheduled_tasks)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-03-09T16:19:46.512249+00:00
**Status:** MERGED

Setting Darius and Michel just in case they see/know any problem with parametrizing the timezone in the @Scheduled spring annotation.

