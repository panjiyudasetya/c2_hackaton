---
id: github:teqplay/portreporter-backend:issue:1405
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1405
title: Bugfix/Try Catch Portcall Message Handler List Events
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1405
labels: []
explicit_links: []
---
# Issue #1405: Bugfix/Try Catch Portcall Message Handler List Events

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1405  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [a6e699989941...e59437b8ec60](https://github.com/teqplay/portreporter-backend/compare/a6e699989941...e59437b8ec60)
**Merge commit:** [e59437b8ec60](https://github.com/teqplay/portreporter-backend/commit/e59437b8ec60)
**Author:** Shan Minh Nguyen
**Reviewers:** Michel Wilson, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [bugfix/try_catch_portcall_message_handler_list_events](https://github.com/teqplay/portreporter-backend/tree/bugfix/try_catch_portcall_message_handler_list_events)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-11-07T12:11:27.205804+00:00
**Status:** MERGED

* Added a try/catch in the forEach to not cause iteration to stop
Added this in a branch bug fix instead of a hotfix as the master branch has different code and didn’t see it working for some reason \(using the master branch on develop\) and this does in develop after checking logs and we’re going to release most likely on Thursday so this can come along.

