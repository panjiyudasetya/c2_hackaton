---
id: github:teqplay/portreporter-backend:issue:1257
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1257
title: 'Prp-1865 : Send Slack Message Via Logs When Any Vopakportcalldetail Don''T
  Process Properly.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1257
labels: []
explicit_links: []
---
# Issue #1257: Prp-1865 : Send Slack Message Via Logs When Any Vopakportcalldetail Don'T Process Properly.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1257  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4cec1822310c...2bf11f79f9f7](https://github.com/teqplay/portreporter-backend/compare/4cec1822310c...2bf11f79f9f7)
**Merge commit:** [2bf11f79f9f7](https://github.com/teqplay/portreporter-backend/commit/2bf11f79f9f7)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/PRP-1865/send_slack_message_when_something_is_wrong](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1865/send_slack_message_when_something_is_wrong)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-02T08:44:14.758129+00:00
**Status:** MERGED

To avoid silently failings, just adding a last step in the process\(\) for logging as severe \(thus, slack message sent\) when something is wrong.

