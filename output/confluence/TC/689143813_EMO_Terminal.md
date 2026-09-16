---
id: confluence:689143813
source: confluence
type: page
space: TC
title: EMO Terminal
author: Joaquin Marquez Bugella
date: '2025-04-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813/EMO+Terminal#EMO-Queue-Consumer
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813/EMO+Terminal#EMO-Queue-Publisher
---
# EMO Terminal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813  

## Content

#FFF0B3

Work in progress

16falsenonelisttrue

# Introduction

Here it is the description and technical details of the EMO Terminal feature in SmartFleet.

# Components

## EMO Queue Configuration

### Queue Properties

There are two property subsets regarding the EMO Queue components:

**Queue Consumer properties** can be found in the class `QueueProperties`, field `emoTerminal`.

**Queue Publisher properties** can be found in the class `PublishingProperties` , field `emoTerminal`.

They follow the standard use of queues and their names are quite self-explanatory.

### Queue Beans

The class `AmqpConfiguration` creates two beans to handle the Queue component:

A `EmoTerminalMessageHandler` **Bean** named `emoTerminalNominationsAmqp`, using the `QueueProperties.emoTerminal`, which is just in charge of consuming the incoming messages, explained in the section [EMO Queue Consumer](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813/EMO+Terminal#EMO-Queue-Consumer)

A `RabbitMqEventSender` **Bean** named `emoTerminalPublishingAmqp`, using the `PublishingProperties.emoTerminal`, which is used in the Component Bean `EmoTerminalMessageSender` that it’s in charge of publishing in the exchange.

Eventually, the `EmoTerminalMessageSender` is used in the `FleetPublishingSchedulerService`, as explained in the section [EMO Queue Publisher](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/689143813/EMO+Terminal#EMO-Queue-Publisher).

## EMO Queue Consumer

A Message Queue Consumer Bean will be created in the Configuration Bean `AmqpConfiguration` (follow annotation `EmoTerminalNominationsAMQP`, using the qualifier `emoTerminalNominationsAmqp`), following the settings indicated in the `QueueProperties.emoTerminal` fields (standard for Ci.

This consumer will receive Nominations (`DbEmoTerminalNomination` model) published by EMO Terminal on their side. This nomination will be saved via the `EmoTerminalNominationsService.save(DbEmoTerminalNomination)` method, that will:

* **Load** the ***existentNomination*** (if any).
* **Persist** the ***incomingNomination***.
* ***Denominate ¹*** the ***existentNomination*****,** if the it (compared to the ***incomingNomination***) changed the `imo`**²** or the `cargoActionType`**³**.
* ***Denominate ¹*** the ***incomingNomination*** if the status is `DENOMINATED`.
* **Load** the (***relevantNomination***) latest (by eta) nomination given the ***incomingNomination***’s `imo`

  + (maybe the incoming nomination didn’t relate to the earliest?)
* ***Nominate*** ***¹*** the ***relevantNomination***
* Save **⁴** the fleets changes.
* Update the planning based on the ***relevantNomination***

  + If that ***incomingNomination*** changed the planning (based on the ***relevantNomination*** changes).

**Notes:**

1. *Nominate*/*denominate* means the addition/removal of the ship (indicated by the nomination’s `imo`) from the corresponding fleets (indicated by the nomination’s `CargoActionType`)  
   Note that this doesn’t actually remove it from the fleet until saving it (**see point 4**).
2. If the nomination changed the imo (from the persisted to the incoming), then the existing one should be denominated (assuming that the nominations has got corrected).
3. If the nomination change the action (i.e. loading to discharge), then the ship should moved to the corresponding fleets were it was by `cargoActionType`.
4. This is, what was nominated and denominated gets updated in the fleets.

## EMO Queue Publisher

In essence, and regarding the EMO Terminal fleets, it publishes the current predictions of the fleets' ships at the Exchange.

The Bean `FleetPublishingSchedulerService` has a scheduled method `scheduledPublishing` that goes through all publishing fleets (`publish` not empty).

Then, it gets the ships in fleet, then the fleet predictions and publish them using the queue publisher according to the the `Fleet.publish` list.

The publishing is done through the **Queue Publisher Bean**

# Health report

When authorized**¹**, the health actuator (baseUrl/actuator/health) will report the following points:

* `components.rabbit.details.components.rabbitEmoTerminalNominations`
* `components.rabbitEmoTerminalNominations`
* `components.rabbitMqEventSenderEmoTerminal`

In example:

{
...
"components": {
...
"rabbit": {
"status": "UP",
"details": {
"rabbitEmoTerminalNominations": "UP"
}
},
"rabbitEmoTerminalNominations": {
"status": "UP",
"details": {
"host": "crow.rmq.cloudamqp.com",
"queue.name": "emo-output",
"queue.last-received": "2025-04-04T15:21:18.183275691Z",
"queue.last-handled": "2025-04-04T15:21:18.190914866Z"
}
},
"rabbitMqEventSenderEmoTerminal": {
"status": "UP",
"details": {
"host": "crow.rmq.cloudamqp.com"
}
}
...
}
}

**Notes:**

1. The SmartFleet authorization is based on the following Headers:

* `Authorization`: Api Authorization token, as custom encoded shared key, see `SmartFleetInterceptor` in PortReporter for details.
* `SmartFleet-Claims`, which value is a json-serialized `UserClaims` object.

# Further readings and links