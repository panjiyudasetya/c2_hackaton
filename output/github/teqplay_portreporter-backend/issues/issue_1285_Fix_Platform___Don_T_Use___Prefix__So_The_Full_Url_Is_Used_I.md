---
id: github:teqplay/portreporter-backend:issue:1285
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1285
title: 'Fix(Platform): Don''T Use / Prefix, So The Full Url Is Used Instead Of Just
  The Base'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1285
labels: []
explicit_links:
- jira:PRA-649
---
# Issue #1285: Fix(Platform): Don'T Use / Prefix, So The Full Url Is Used Instead Of Just The Base

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1285  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [86215ce5cd35...09811a686b8f](https://github.com/teqplay/portreporter-backend/compare/86215ce5cd35...09811a686b8f)
**Merge commit:** [09811a686b8f](https://github.com/teqplay/portreporter-backend/commit/09811a686b8f)
**Author:** Former user
**Reviewers:** Joost Laurman, Joaquin Marquez Bugella, Shan Minh Nguyen
**Approvers:** Joaquin Marquez Bugella, Shan Minh Nguyen
**Source Branch:** [PRA-649-api-support](https://github.com/teqplay/portreporter-backend/tree/PRA-649-api-support)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-07T15:13:23.529926+00:00
**Status:** MERGED

> **Context:**
>
> PortReporter will not be connecting to backendpronto\(dev\) anymore. It will need to go through the internal API, so it can be directed to get ship history from ship-history instead of from backendpronto\(dev\) itself.
When using `https://backendprontodev.teqplay.nl/` as the url, nothing goes wrong.
But when using `https://internalapidev.teqplay.dev/v0` then it wouldn’t work. The prefixed `/` would instruct retrofit to use the base url of `https://internalapidev.teqplay.nl` instead of just appending it after the `/v0`.

