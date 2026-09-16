---
id: github:teqplay/vesselvoyage-backend:issue:376
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 376
title: Spv-2412 Rabbitmq Publishing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/376
labels: []
explicit_links:
- jira:SPV-2412
---
# Issue #376: Spv-2412 Rabbitmq Publishing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/376  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b5f12c332248...0cf9b33a772c](https://github.com/teqplay/vesselvoyage-backend/compare/b5f12c332248...0cf9b33a772c)
**Merge commit:** [0cf9b33a772c](https://github.com/teqplay/vesselvoyage-backend/commit/0cf9b33a772c)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2412-rabbitmq-publishing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2412-rabbitmq-publishing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-12-02T13:40:07.531306+00:00
**Status:** MERGED

* Made it so we can publish V2 changes on RabbitMQ and merged configuration of V1 and V2 in the shared event-publishing property group
* ktlint
* split the V1 and V2 exchange so they are fully split

