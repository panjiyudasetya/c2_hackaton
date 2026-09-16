---
id: jira:TCC-21
source: jira
type: issue
key: TCC-21
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Michel Wilson
labels: []
components: []
title: Make sure that the pending buckets warning is not an indication of a bigger
  problem in the background
author: Richard van Klaveren
status: Done
date: '2025-03-26'
url: https://teqplaybv.atlassian.net/browse/TCC-21
explicit_links:
- jira:TCC-152
---
# [TCC-21] Make sure that the pending buckets warning is not an indication of a bigger problem in the background

**URL:** https://teqplaybv.atlassian.net/browse/TCC-21  
**Type:** Bug | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Michel Wilson  
**Created:** 2025-03-26 | **Updated:** 2025-05-28  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

There is a daily message in prio2, we now increased the limit, but want to make sure we understand why there is a peak in the amount of pending buckets. Is it a measurement issue, are bigger buckets scheduled first, or is this an indication something will go wrong in the future?

!image-20250326-162925.png|width=529,height=274,alt="image-20250326-162925.png"!

## Comments

### Richard van Klaveren — 2025-05-12

metrics generated for process of bucket archiving. Seems to point to ‘findBucketIds’….

### Michel Wilson — 2025-05-22

Indices added on dev + live, this fixes the problem. PR for this + the metrics is in review.

### Michel Wilson — 2025-05-26

PR merged to develop, still needs to be deployed to production. Not super urgent, the only thing that this adds is the metrics, the index has already been added manually. After deploying this, we need to remember to remove the old index on archive bucket id which is no longer used!!!
