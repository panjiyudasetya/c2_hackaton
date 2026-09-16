---
id: confluence:122486785
source: confluence
type: page
space: TC
title: AIS stream application architecture
author: Michel Wilson
date: '2022-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/122486785
explicit_links: []
---
# AIS stream application architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/122486785  

## Content

The `ais-stream` application is responsible for ingesting AIS data from various sources, processing it, and converting it to AIS events on the bus. This page will first describe the overall data flow, the data representation, and then it will proceed to describe the various subsystems in the `ais-stream` application that support this data flow.

## Data sources

AIS data is transmitted by transponders on maritime vessels, each identified by their MMSI, and captured by antennas or satellites, and distributed by various commercial parties. To learn more about the technical details of AIS message types, the US Coast Guard has a nice overview here: <https://www.navcen.uscg.gov/automatic-identification-system-overview>.

Ingestion of AIS messages is performed using implementations of the `AisReceiver` interface in `ais-stream`. There are currently three different variants of the `AisReceiver`:

* A TCP/IP socket-based receiver, which connects to a given port on a given server using TCP/IP. Optionally, an authentication token can be sent after the connection is established; this functionality is used for the Spire AIS feed. Messages are encoded using the <https://en.wikipedia.org/wiki/NMEA_0183> protocol.  
  The TCP/IP receiver is used to receive messages from Spire as well as AisHub.
* An MQTT-based receiver, which receives JSON-encoded messages from an MQTT broker. This is used to receive AIS data for the port of Helsinki in Finland.
* Another JSON-based receiver, used for the port of Singapore. TBD: add more details.

## Data formats

Internally, AIS data is categorised in four different message types, which contain the fields we need to send information downstream:

* **Position**: message containing the current position, course and speed, among some other things, of a ship.
* **Static**: message containing information of a more static nature, such as the vessel name, IMO number, destination.
* **Long range**: smaller version of the position message with lower accuracy. Currently not used to update the state of a ship.
* **Station**: information about AIS base stations, such as their name and position

## Message streams

After processing all the AIS data, `ais-stream` sends data to two different message streams, `ais-stream:history` and `ais-stream:diff`.

The `history` stream is a stream containing complete updates for all (relevant) messages that are ingested. For all four message types, all fields are sent in every message, contained in a wrapper that provides the message source and timestamp. Note that in some cases, this might not be the latest message transmitted by the ship, since in particular the Spire data source often sends historical updates at a later point in time. It is important to emphasize this again: the `history` stream is not guaranteed to be in order, there will be out-of-order messages and any consumer of this stream should be able to cope with this.

The `diff` stream, on the other hand, *does* guarantee message ordering: every update in this stream is guaranteed to be more recent than the previous update. In this version of the message stream, only the fields that have *changed* since the last update are contained in the message. Both the previous as well as the current value are provided. This has the benefit of needing much less data than the full update, as well as enabling stateless operation for some consumers.

## Filtering

Before actually processing AIS data, some filtering is performed first. There are two different filters in `ais-stream`: the first filter to be applied to the data is the “ghost ship” filter, which weeds out fake AIS data. The second filter is a basic filter to weed out “impossible” updates.

### Ghost ship filter

It has been found that relatively often some fake AIS data is present in the streams: a very limited number of position updates for a given MMSI, sometimes spread out geographically over a very large area. The ghost ship filter tries to weed out this information before an MMSI is accepted as a “valid” ship, by ensuring that at least ten plausible updates (i.e., with a low geographical distance between them) have been received over a given time frame. Once this check is passed, the MMSI is taken out of “quarantine” by adding it to the current state map. After that, the ghost ship filter check is no longer performed for that particular MMSI.

### Update filter

The other filter is applied to all valid ships. It checks whether the reported heading and distance since last update are feasible. This is a simple way to remove some invalid updates due to AIS jitter.

## Processing flow

Data processing in `ais-stream` is done using four different threads. For each of them, the general flow will be described below. Throughout the discussion, it is important to keep the concept of *back pressure* in mind. This concept refers to the fact that we want to “transfer” any flow restriction on the side where data is being *sent* (due to for example CPU usage in the message broker to which we send data) to the side where data is being *received*, to slow down data ingestion to match the speed at which we send the data out. If we fail to do this, the result is that we must store the data in memory, and this will guarantee that eventually the application will go out of memory.

### AIS receiver

The AIS receiver thread is not an actual thread, but code running in the message handlers that process incoming data over the connections to the AIS data sources. For every update received, the filter logic is triggered first. If the message gets past the filters, a check is performed to see if the update is newer than the current state (i.e., it is live data or historic data).

If live data is received, the data is stored in the state for the associated MMSI, in which the latest received message of the four different message types is kept. Then, the MMSI is added to two sets of MMSIs for which we have received updates: one for managing the sending of diff updates, and one for managing the flushing of state to the database.

If historical data is received, the message is appended to a queue containing full updates. This queue is blocking, and has a limited size: sending the full updates to the message broker is the most work-intensive operation, and this is used to apply back pressure to the sending side. If the queue is full, the handler code will block, and this will cause the TCP/IP connection to be throttled, reducing the sending rate.

Process flow for AIS receiver event handlers

### Live data handling

The processing of live data is controlled by a set that contains MMSIs for which a receiver has received one or more updates. The thread continuously tries to take an MMSI from the set, and if one is available, it checks whether the current (combined) state is different from the previously sent combined state. If this is true, *and* a diff update has been sent at least 20 seconds ago, a new diff update is sent based on the previous and current combined state, and the combined state is updated.

Then, this process repeats for the individual message types: if the current newest message is newer than the one previously sent by more than 20 seconds, the message is sent to the full update queue and the timestamp for that message type is updated.

The process above ensures that both diff updates and full udpates are rate-limited: only every 20 seconds a message is sent for either of those message types.

Process flow for live AIS data handler thread

### Historical data handling

Processing historical updates is complicated by the fact that we want to rate-limit the data to have only one update roughly 20 seconds, but data can arrive out-of-order. The solution to this problem is to collect data in a buffer, and to process the messages in batches. All messages that are older than 1 minute are “pruned” to remove updates if there are less than 20 seconds between them, and then sent to the full update queue. To apply back pressure to the receiving thread, we start limiting how much messages we store in the buffer when the previous iteration has not finished when the next iteration is due to start.

The process is repeated every 20 seconds and consists of the following steps:

* Consume messages from the history queue, together with the messages from the current buffer (“kept messages”)
* If a message was received more than a minute ago, store it in the “to be processed” pile. If a message was received less than a minute ago, store it in the current buffer (“kept messages”)
* Group the messages by MMSI and message type, and apply the rate limit, discarding messages until there are at least 20 seconds between ech update
* Send the messages to the full update queue

When this process is completed, a check is done whether it took more than 20 seconds. If this is true we cannot send the data fast enough and we have to appy back pressure. This is done by taking only that many messages from the history queue as we’ve been able to send out in the previous iteration. This way, the history queue will start to fill up and eventually block the receiver threads.

Process flow for historical AIS data handler thread

## State storage

The final thread in the system ensures that the current state is persisted in the database. This is also drive by a set of MMSIs which have been updated (these are set in the receiver threads). The flush thread wakes up at a regular interval, and copies the state for all the MMSIs in the set to a separate variable. Then, all this information is written to the database.