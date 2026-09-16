---
id: github:teqplay/vesselvoyage-backend:issue:133
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 133
title: Spv-1633 Concurrent Rabbitmq For Events
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/133
labels: []
explicit_links: []
---
# Issue #133: Spv-1633 Concurrent Rabbitmq For Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/133  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b83afd3932d1...5bdee20df849](https://github.com/teqplay/vesselvoyage-backend/compare/b83afd3932d1...5bdee20df849)
**Merge commit:** [5bdee20df849](https://github.com/teqplay/vesselvoyage-backend/commit/5bdee20df849)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Gavin den Hollander
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1633_concurrent_rabbitmq_for_events](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1633_concurrent_rabbitmq_for_events)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-06-27T15:43:25.170028+00:00
**Status:** MERGED

* Made it so all RabbitMQ consuming is done via the SimpleMessageListenerContainer that Spring provides and added a configuration option to process TeqplayEvents with multiple consumers
* ktlint
* Added missing configuration in context loading test

