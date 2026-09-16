---
id: github:teqplay/portreporter-backend:issue:1151
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1151
title: Correcting Fetching Timestamps Issues
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1151
labels: []
explicit_links: []
---
# Issue #1151: Correcting Fetching Timestamps Issues

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1151  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4788801c79d5...9a2cdba33a56](https://github.com/teqplay/portreporter-backend/compare/4788801c79d5...9a2cdba33a56)
**Merge commit:** [9a2cdba33a56](https://github.com/teqplay/portreporter-backend/commit/9a2cdba33a56)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [feat/upgrade_spring_boot_fetching_timestamps](https://github.com/teqplay/portreporter-backend/tree/feat/upgrade_spring_boot_fetching_timestamps)
**Destination Branch:** [feat/upgrade_spring_boot](https://github.com/teqplay/portreporter-backend/tree/feat/upgrade_spring_boot)
**Closed On:** 2022-09-05T12:22:17.342377+00:00
**Status:** MERGED

This PR is about correcting the timestamp issues provoked by the `DateTimeFormatter`, which is unable to deal with partial or custom timestamps \(like “YYYY-'W’ww”\).

