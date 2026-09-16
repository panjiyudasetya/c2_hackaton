---
id: github:teqplay/portreporter-backend:issue:1069
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1069
title: Prp-954/Feat/Send Notification When Nominationmessagehandler Fails
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1069
labels: []
explicit_links: []
---
# Issue #1069: Prp-954/Feat/Send Notification When Nominationmessagehandler Fails

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1069  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [cc28da365346...ce6306850420](https://github.com/teqplay/portreporter-backend/compare/cc28da365346...ce6306850420)
**Merge commit:** [ce6306850420](https://github.com/teqplay/portreporter-backend/commit/ce6306850420)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Berend
**Approvers:** Berend
**Source Branch:** [PRP-954/feat/send_notification_when_nominationMessageHandler_fails](https://github.com/teqplay/portreporter-backend/tree/PRP-954/feat/send_notification_when_nominationMessageHandler_fails)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-04-11T16:11:21.928575+00:00
**Status:** MERGED

* PRP-954: Implement a slack notification on failing parsing of a nomination message received via rabbitmq:

    * Send Slack message when an automatic creation of a nomination fails.
    * Relocate Nomination class \(from external to internal package\).
    * Generalize SlackConnection class so to use it not just for Exact notifications.
    * Some reformatting.
    


