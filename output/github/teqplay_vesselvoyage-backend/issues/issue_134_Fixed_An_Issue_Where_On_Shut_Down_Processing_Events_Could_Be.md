---
id: github:teqplay/vesselvoyage-backend:issue:134
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 134
title: Fixed An Issue Where On Shut Down Processing Events Could Be Start Again, Resulting
  In Unexpected Behaviour
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/134
labels: []
explicit_links: []
---
# Issue #134: Fixed An Issue Where On Shut Down Processing Events Could Be Start Again, Resulting In Unexpected Behaviour

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/134  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d4beb15f10b5...4b3895e3cac4](https://github.com/teqplay/vesselvoyage-backend/compare/d4beb15f10b5...4b3895e3cac4)
**Merge commit:** [4b3895e3cac4](https://github.com/teqplay/vesselvoyage-backend/commit/4b3895e3cac4)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Joost Laurman
**Source Branch:** [fix/close_processing](https://github.com/teqplay/vesselvoyage-backend/tree/fix/close_processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-06-28T08:36:07.936516+00:00
**Status:** MERGED

On shutdown, it tries to start processing again because the following scheduled task always runs every 10 seconds:
```
@Scheduled(fixedDelayString = "PT10S")
fun shouldKeepProcessing()
```
It always tried to start processing again if the processing wasn’t running and platform was healthy. This change makes sure we don’t do this when entering shutdown mode. So with unfortunate timing, this could trigger. The following logs indicate this behaviour, which will not start again on shutdown.
```
2023-06-28 05:32:56,580 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.s.ProcessingService[0;39m: Shutting down all processing and trace service
2023-06-28 05:32:56,581 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.s.ProcessingService[0;39m: Stop processing
2023-06-28 05:32:56,581 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Stopping TeqplayEvents RabbitMQ listener
2023-06-28 05:32:56,587 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Waiting for workers to finish.
2023-06-28 05:32:59,225 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.s.ProcessingService[0;39m: Start processing
2023-06-28 05:32:59,225 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Starting TeqplayEvents RabbitMQ listener
2023-06-28 05:32:59,225 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Started TeqplayEvents RabbitMQ listener
2023-06-28 05:32:59,225 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Starting AisStreaming RabbitMQ listener
2023-06-28 05:32:59,225 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Started AisStreaming RabbitMQ listener
2023-06-28 05:32:59,225 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.s.RecalculationService[0;39m: Automatic recalculation enabled
2023-06-28 05:33:00,627 [34mINFO [0;39m [[36mscheduling-8[0;39m] [33mn.t.v.s.RecalculationService[0;39m: Refreshed recalculable ships in 1401 ms: 128963 ships in total, 866 deleted ships, 58864 calculated ships, 70104 recalculable ships. With the configured interval of recalculating one ship every PT5S, we will be done by 2023-07-02T06:55:00.626948334Z[Etc/UTC]. Don't forget to bring cake
2023-06-28 05:33:01,588 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Workers not finished.
2023-06-28 05:33:01,588 [31mWARN [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Closing channel for unresponsive consumer: Consumer@7c27ed2f: tags=[[amq.ctag-sHprJ37tM_Q5N8FKM_1cUA]], channel=AMQChannel(amqp://VesselVoyage@172.31.23.106:5671/TeqplayEvents,3), acknowledgeMode=AUTO local queue size=9
2023-06-28 05:33:01,589 [31mWARN [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Closing channel for unresponsive consumer: Consumer@310db5c4: tags=[[amq.ctag-w7icW5gNvKz1KgH1cfa8_w]], channel=AMQChannel(amqp://VesselVoyage@172.31.23.106:5671/TeqplayEvents,1), acknowledgeMode=AUTO local queue size=9
2023-06-28 05:33:01,589 [31mWARN [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Closing channel for unresponsive consumer: Consumer@3503e68e: tags=[[amq.ctag-CRzZYEoVsTB8VYgOuocCJw]], channel=AMQChannel(amqp://VesselVoyage@172.31.23.106:5671/TeqplayEvents,4), acknowledgeMode=AUTO local queue size=9
2023-06-28 05:33:01,590 [31mWARN [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Closing channel for unresponsive consumer: Consumer@7c2d4398: tags=[[amq.ctag-FtRubIt7qR4qIu1W2DTilA]], channel=AMQChannel(amqp://VesselVoyage@172.31.23.106:5671/TeqplayEvents,2), acknowledgeMode=AUTO local queue size=9
2023-06-28 05:33:01,591 [31mWARN [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Closing channel for unresponsive consumer: Consumer@160b7ccd: tags=[[amq.ctag-dYk2XIDoba6AmrC9z_Qq3A]], channel=AMQChannel(amqp://VesselVoyage@172.31.23.106:5671/TeqplayEvents,5), acknowledgeMode=AUTO local queue size=9
2023-06-28 05:33:01,593 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Stopped TeqplayEvents RabbitMQ listener
2023-06-28 05:33:01,593 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Stopping AisStreaming RabbitMQ listener
2023-06-28 05:33:01,594 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Waiting for workers to finish.
2023-06-28 05:33:02,237 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mo.s.a.r.l.SimpleMessageListenerContainer[0;39m: Successfully waited for workers to finish.
2023-06-28 05:33:02,237 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.c.RabbitMqInitializer[0;39m: Stopped AisStreaming RabbitMQ listener
2023-06-28 05:33:02,237 [34mINFO [0;39m [[36mSpringApplicationShutdownHook[0;39m] [33mn.t.v.s.RecalculationService[0;39m: Shutting down recalculation
```

