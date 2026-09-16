---
id: github:teqplay/vesselvoyage-backend:issue:174
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 174
title: 'Feat(Trace): Use Ais-Stream:History For Traces'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/174
labels: []
explicit_links:
- jira:SPV-1992
---
# Issue #174: Feat(Trace): Use Ais-Stream:History For Traces

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/174  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0ea49faa85ee...b5c33d1988c1](https://github.com/teqplay/vesselvoyage-backend/compare/0ea49faa85ee...b5c33d1988c1)
**Merge commit:** [b5c33d1988c1](https://github.com/teqplay/vesselvoyage-backend/commit/b5c33d1988c1)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-1992-consume-ship-history-from-nats-instead-of-rabbit-mq](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1992-consume-ship-history-from-nats-instead-of-rabbit-mq)
**Destination Branch:** [feat/switch-to-ais-engine](https://github.com/teqplay/vesselvoyage-backend/tree/feat/switch-to-ais-engine)
**Closed On:** 2024-03-13T08:52:07.273951+00:00
**Status:** MERGED

This PR removes consuming AIS traces from RabbitMQ and instead gets them from NATS.
Already discussed with @{5e37d9154512b80ca4319871} to not have a pre-review meeting, since the changes are light enough. Feel free to schedule a chat if you have any comments that you’d like to discuss!

