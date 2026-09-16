---
id: github:teqplay/portreporter-backend:issue:1063
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1063
title: 'Prp-726 : Automatic Ingestion Of Nominations From Queue'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1063
labels: []
explicit_links: []
---
# Issue #1063: Prp-726 : Automatic Ingestion Of Nominations From Queue

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1063  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [17257c975d2d...9f4a68fa155e](https://github.com/teqplay/portreporter-backend/compare/17257c975d2d...9f4a68fa155e)
**Merge commit:** [9f4a68fa155e](https://github.com/teqplay/portreporter-backend/commit/9f4a68fa155e)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-726/feat/automatic_creation_of_nominations_from_queue](https://github.com/teqplay/portreporter-backend/tree/PRP-726/feat/automatic_creation_of_nominations_from_queue)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-04-07T15:39:33.803134+00:00
**Status:** MERGED

I saw repeating myself in the class `RabbitMqEventHandler`: I had to create a new set of methods \(fairly the same\). With my changes, there would have been in total 3 sets of similar methods!

**So I took the liberty to re-engineer** it \(just a bit\) and created two new classes:

* RabbitMQStream: encapsulating the channel and connection, as well as the methods to create and maintain them up and running.
* RabbitMQSettings: encapsulating the queue settings.

**After that, I did the actual job**: **setting up a new QueueStream** to consume nominations from the new queue.

**Also I small-patched** some things like:

* Linking the property `rabbitmq.monitorQueueInMinutes` to the actual monitor \(it was not used at all\).
* Declare a `rabbitmq.vopakMonitorQueueInMinutes` matching the current monitor for Vopak messages.


