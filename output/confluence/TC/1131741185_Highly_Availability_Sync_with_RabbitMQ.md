---
id: confluence:1131741185
source: confluence
type: page
space: TC
title: Highly Availability Sync with RabbitMQ
author: Jamie de Leest
date: '2026-02-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1131741185
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1131741185
---
# Highly Availability Sync with RabbitMQ

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1131741185  

## Content

We use queues in RabbitMQ to synchronize data between HA applications:

* Processor
* API 1
* API 2
* API 3

as an example ship-history and csi

These queues are:

* Non-durable
* Auto-created
* Auto-deleted
* Instance-specific
* Used only for live synchronization (not persistence)

---

# Creating a Temporary Classic Queue

Each service instance should create its own queue like this:  
the exchange is predefined

kotlinwide760val declareOk = channel.queueDeclare(
"", // auto-generate unique name
false, // not durable
true, // exclusive (connection-scoped)
true, // autoDelete
null // classic queue (default)
)
val queueName = declareOk.queue
val exchangeName = properties.exchangeName
channel.queueBind(
queueName,
exchangeName,
""
)

our current skeleton plugin does not support this because you cant access the channels because they are private or protected