---
id: confluence:652509186
source: confluence
type: page
space: TC
title: Streaming AIS Updates
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652509186
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652509186
---
# Streaming AIS Updates

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652509186  

## Content

# Streaming AIS Updates

## Overview

## Flow of streaming

### Technical details

#### Producer

* Ship updates are queued and are sent in bulk (per second) to the exchange, with the following model:

  {
  updates: List<ShipInfo>
  }
* `ShipInfo` has a special field for streaming: `streamingIsNewUpdate`, it indicates if the update for that specific ship was new or not. This is determined by comparing the latest `timeLastUpdate` of the already sent updates of that ship with the current (to be sent) `ship.timeLastUpdate`. This mostly comes into play when there is an outage for a specific data source, and it's catching up by sending loads of old updates. These are still relevant, so they should be propagated, but they aren't new anymore so they have to be distinguished.
* If for some reason the updates can't be sent to the exchange, the updates get remembered and it will keep trying to send the updates until it received a confirmation that they have been received properly.
* Rate limiting and merging of updates is also used. Ship updates are rate limited by sending updates for a specific ship only once per 20 seconds (configurable). This means that a backend will only receive an update of ship A, once per 20 real-time seconds. All updates for ship A that are kept back/rate limited, will be saved until the time period has expired, the updates will then be sorted in order by `timeLastUpdate` and will be merged into 1 update.
* The merging of updates also takes care of outages/quick flushing of old data. So.. while there is a rate limit of 1 update of ship A per 20 seconds real-time (and intermediate updates getting merged), the updates for ship A are also merged in blocks of 20 seconds determined by the `ship.timeLastUpdate`. So this means, if for example 30 minutes of updates for ship A comes in within the rate limited 20 seconds, these updates will not be merged into just 1 update (because this would result into data loss). So we sort all the saved updates and merge them in blocks of 20 seconds (so we will send ~90 updates for ship A, to ensure no data is lost and it's still correctly spaced).

#### Consumer

* a consuming backend receives updates for the whole world per second, so it applies a geo-filter to ensure only relevant data for that backend is propagated through the system
* the consumer will look at the `streamingIsNewUpdate` from the `ShipInfo` to determine if the update should be considered an update of the current state or an historical update
* the queue for the consumer can hold 30 minutes of updates, if the queue has filled up too much it will start dropping the oldest data

#### Both Producer+Consumer

* the ship updates are also propagated internally via internal topics for current and historical updates
* these updates can be used by adapters/monitors/etc. to subscribe on real-time updates (e.g. StreamingAreaMonitor and real-time updates via a websocket)

## RabbitMQ setup

### RabbitMQ Live

`URI = amqps://AisStreaming:<password>@rabbitmq.teqplay.nl:5671/AisStreaming`

| field | value | note |
| --- | --- | --- |
| *Virtual Host:* | AisStreaming |  |
| *User:* | AisStreaming | virtual host=`AisStreaming` |
| *Exchange:* | AisStreaming-updates | fanout to bound queues |
| *Queues:* | AisStreaming-backend\* | * one queue per backend instance (where `*` can indicate a suffix, like backendpronto, backendglobal, etc.) |
|  |  | * bound to `AisStreaming-updates` exchange |
|  |  | * saves messages up to 30 minutes (`x-message-ttl: 1800000`) |

### RabbitMQ Dev

`URI = amqps://AisStreamingDev:<password>@rabbitmqdev.teqplay.nl:5671/AisStreaming`

| field | value | note |
| --- | --- | --- |
| *Virtual Host:* | AisStreaming |  |
| *User:* | AisStreamingDev | virtual host=`AisStreaming` |
| *Exchange:* | AisStreaming-updates | fanout to bound queues |
| *Queues:* | AisStreaming-backend\* | * one queue per backend instance (where `*` can indicate a suffix, like backenddev, backendprontodev, etc.) |
|  |  | * bound to `AisStreaming-updates` exchange |
|  |  | * saves messages up to 30 minutes (`x-message-ttl: 1800000`) |

### Creating this setup from scratch

1. Go to RabbitMQ Live or Dev
2. Setting up a virtual host

   1. Go to `Admin > Virtual Hosts`
   2. Set the name to `AisStreaming`
   3. Press `Add virtual host`
3. Setting up a user

   1. Go to `Admin > Users`
   2. Set the username to `AisStreaming`
   3. Set the password and save in Lastpass
   4. Press `Add user`
   5. In the table under `All users`, click on the newly created username (`AisStreaming`)
   6. Go to `Set permission`section
   7. Change `Virtual host:` from `/` to `AisStreaming`
   8. Press `Set permission`
4. Setting up the exchange

   1. Go to `Exchanges`
   2. Go to `Add a new exchange` section
   3. Set `Virtual host:` to `AisStreaming`
   4. Set `Name` to `AisStreaming-updates`
   5. Set `Type` to `fanout`
   6. Press `Add exchange`
5. Setting up a queue

   6. Go to `Queues`
   7. Go to `Add a new queue` section
   8. Set `Virtual host:` to `AisStreaming`
   9. Set `Name:` to `AisStreaming-backend*` (e.g. for `backendprontodev` this would be `AisStreaming-backendprontodev`)
   10. Click on `Add Message TTL` (or manually add `x-message-ttl` under `Arguments`)
   11. Set the TTL to 30 mins in millis ([1800000](https://bitbucket.org/teqplay/teqplay-wiki/commits/1800000))
   12. Press `Add queue`
   13. In the table under `All queues (n)`, click on the newly created queue (`AisStreaming-backend*`)
   14. Go to `Bindings` section
   15. Set `From exchange:` to `AisStreaming-updates`
   16. Press `Bind` (all messages that will be sent to the exchange, will now fanout to this queue)

## Platform setup / configuring streaming

### defaults for `system.conf`

streaming {
enabled = false
uri = ""
producing {
enabled = false
updateRateInSeconds = 20
exchange = ""
}
consuming {
enabled = false
queue = ""
}
internal {
websockets = false
}
}
...
areamonitor.streamingEnabled = false

With the`streaming`section in the`system.conf`you can configure the streaming settings.

| section | usage |
| --- | --- |
| producing | settings for producing/sending updates to a configured exchange to be shared with other queues/backend instances |
| consuming | this backend instance will consume/receive messages from the queue |
| internal | settings for enabling different internal parts that utilize streaming ship updates |

### Setting up a producer

1. Open the `system.conf`
2. Add the following:

   streaming {
   enabled = true
   uri = "<set URI here>"
   producing {
   enabled = true
   exchange = "<set exchange here>"
   }
   }

   *Optionally you could add a custom update rate, but the default is already set, so you don't need to add/change it here*

3. If the configuration is correct you can just restart the platform and ship updates will be sent per second to the exchange.

### Setting up a consumer

1. Open the `system.conf`
2. Add the following:

   streaming {
   enabled = true
   uri = "<set URI here>"
   consuming {
   enabled = true
   queue = "<set queue here>"
   }
   }

3. If the configuration is correct you can just restart the platform and ship updates will be received from the queue.

**IMPORTANT NOTE:** please be aware that by enabling this you will only receive ship updates via the streaming. So if the queue isn't connected to an exchange or the exchange isn't filled with updates from a producing platform, then you WILL NOT RECEIVE UDPATES.

**ANOTHER IMPORTANT NOTE:** if the producing platform, exchange and the bound queue were already setup then the targeted queue is/was already filling up with updates. To ensure the consuming platform won't receive duplicate data because of consuming these saved updates after a restart, you have to purge the messages of the queue while the platform is restarting.

Steps:

1. Setup the `system.conf` so it consumes from the queue and save the file
2. Go to the RabbitMQ management page for either live or dev
3. Go to `Queues` and select the queue you added under `streaming.consuming.queue`
4. Go to `Purge` section (you will need to go here again after you've started the restart)
5. Now go back to the platform and restart it
6. While it's restarting go back to the `Purge` section and press `Purge Messages`, you will receive a popup asking if this is OK, just accept this because we are sure we want to purge the messages.
7. Now sit back while the platform is still restarting, new messages will come in on the queue and the platform will just pick them up after it's done with restarting. You can see the messages build up during the restart, and when the platform starts consuming, they will go down again.

### Setting up the internal streaming parts

You can enable/disable the individual internal settings. An explanation of what these settings do are given below.

| field | value | explanation |
| --- | --- | --- |
| areamonitor.streamingEnabled | false | for every area that needs to be monitored, an `AreaMonitor` gets created which runs per `x` seconds, monitoring the specified area |
|  | true | instead of multiple `AreaMonitor` being created, just one `StreamingAreaMonitor` gets created monitoring all the areas. |
|  |  | The `StreamingAreaMonitor` listens for current ship updates and will run per ship: |
|  |  | * checks in which areas this ship has already been seen |
|  |  | * checks in which areas this ship is currently inside (with a RTree for the bounding boxes of all monitored areas) |
|  |  | * for every area the ship is/was in, events get fired where applicable |
| websockets | false | (nothing happens) |
|  | true | you can create a websocket connection to the platform, subscribing to a bounding box and receiving all ship updates real-time |
|  |  | 1. connect: `url = /websocket/aisUpdates?token=<auth token>` |
|  |  | 2. send bounding box over websocket (only after initial set you'll receive ship updates, you can update the bounding box at any time) |
|  |  | 3. receive ship updates in this format: `{ "status": "ADD" / "UPDATE" / "REMOVE", "ship": ShipInfo }` (the status indicates whether this ship was added, updated or removed from the view/bounding box) |