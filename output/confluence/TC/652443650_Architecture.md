---
id: confluence:652443650
source: confluence
type: page
space: TC
title: Architecture
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443650
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443650
---
# Architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443650  

## Content

architecture in a nutshell looks like this:

The Teqplay platform

And the connection to external components like the NEI and/or Pronto looks like:'

Where filtering/merging of AIS updates takes place:

# Platform Data Storage

## AIS storage

The Teqplay platform collects huge amounts of AIS data. Currently there are about 2 million data points collected every day, about 1GB per day (monitoring just a part of Europe). The database indexes required to enable searching through the data are almost as large as the data itself, doubling the amount of used disk space. MongoDB didn't perform well with these amounts of historic data (lots of very small documents, huge indexes). Part of the problem was too limited hardware (not enough RAM and IO).

To make a better scalable solution for the long term, the data points have been put into buckets. Each bucket has a fixed dimension and contains on average a few hundred AIS data points. Typical queries are retrieving AIS history of a single ship for a few days, or retrieving the AIS history of an area for a couple of hours or days. The buckets are set up in such a way that they seamlessly match the way the data is queried: typical queries require "just a handful" of buckets to be retrieved from the database.

The AIS data is stored in two different MongoDB collections (data is duplicated):

* Buckets containing historic AIS data **per ship per day**, stored in the collection `shiphistory`. Bucket id's are compound keys `"date,mmsi"`, for example `"2026-11-21,477684700"`.
* Buckets containing historic AIS data **per area per day**, stored in the collection `areahistory`. The size of the areas is 0.01x0.01 degrees. Bucket id's are compound keys `"date,longitude,latitude"`, for example `"2016-11-21,4.06,51.79"`.

This bucket solution turns the AIS database into a simple key/value store, which is extremely scalable. The data becomes easy to cache, repair, duplicate, shard, etc. And the performance is great. To retrieve data, there is no need to query anymore: you can just fetch the requested buckets by their id. Note that such a bucket solution is not always applicable: it can only work when querying data in a single way (like searching per ship per day), allowing to group the data in buckets.

## Event storage

Initially, the events where stored as individual documents in a single Mongo collection. Similar to AIS data, this became a bottleneck too, and the events are now stored in buckets.

Like with AIS data, the data queries boil down to two different types: queries by ship or infrastructure id, and queries by area. A second important difference is the category of events, and the buckets are grouped per category, which is based on their abstraction level.

There are three event categories:

* **BASIC** An event only involving the data of a single ship, infrastructure object, or sensor. Example events in this category are `SPEEDCHANGED`, `MOORED`, and `AISLOST`. This is the largest category which takes up about 65% of all events.
* **ENCOUNTER** An event involving two parties: two ships, a ship and an infrastructure like a bridge, or a ship and a defined area. Example events in this category are `PILOT`, `TUG`, and `BRIDGEENCOUNTER`. This category contains is about 30% of all events.
* **CONTEXT** An event involving context information like portcall, planning, schedules, aggregation of lower level events, etc. Example events in this category are `ETA`, `ETD`, `ATA`, `ATD`. This category contains is about 5% of all events.

Note that besides these categories, there is a group of events which form pairs: the start and stop of an action like bunkering or moving. These events are stored as regular, individual events in the buckets, and can be merged in the backend into "composed events" when fetching data.

The events are stored in two different MongoDB collections (data is duplicated):

* Buckets containing **events per entity per day per category**, stored in the collection `eventsByEntity`. Here, an entity can be a ship (mmsi), a bridge (isrs id), or any other infrastructure or sensors. Bucket id's are compound keys `"date,entityId,category"`, for example `"2016-11-25,244003000,ENCOUNTER"`. ENCOUNTER events are stored twice in this collection: one for both involved ships (both have their own daily buckets).
* Buckets containing events **per area per day per category**, stored in the collection `eventsByArea`. The size of the areas is 0.01x0.01 degrees. Bucket id's are compound keys `"date,longitude,latitude,category"`, for example `"2016-11-25,4.40,51.89,ENCOUNTER"`.

## Caching of data

There are two types of cache:

* Cache containing newly inserted data. This data isn't immediately written to database. Instead, this is done once in a while via a "flush" action.
* Cache containing data which is recently requested. This cache makes consecutive requests for the same data faster.

The two types of cache are explained in detail in the following two sections.

### Caching and flushing newly inserted data

Newly inserted datapoints (both of AIS and Events) are not immediately stored in the database, but added to a cache in the Java platform which is flushed once every 10 minutes. The cache consists of a hashmap with the bucketId as key and a bucket with the new data points as value.

The reason for caching and flushing is that saving a new datapoint is a relatively heavy. The data point must be added to an existing bucket which must be read, merged, and written to the database. Therefore, new data points are collected for some time, and saved to the database in batches.

The newly inserted data points are flushed to the database on one of the following triggers:

* Once every 10 minutes (configurable)
* When there are 1 million new items inserted since the last flush (configurable)

Flushing works as follows:

* Retrieve all buckets for which we have new data points from the database. When this bucket is already available in the request cache, the cached bucket is used.
* Append the new data points to the buckets.
* Write the updated bucket to the database.
* Remove the new data points from the newData cache

The flushing mechanism every 10 minutes causes a special pattern of server activity during the day: a spike with a duration of about one minute once every 10 minutes. Throughout the day, the buckets will grow, and it will take more time to read and write them from the database. This causes a daily, linear behavior of the server getting more busy towards the end of the day.

You can configure a larger flush interval to reduce load on the server (flushing is quite heavy). It's important though to realize that more new data needs to be kept in memory, so make sure there is enough RAM available.

Because flushing to database is relatively heavy, newly inserted data is kept in memory for a while. To prevent the risk of losing data when the server crashes, and to allow for a fast restart of the server, there is a mechanism which temporarily saves the newly inserted data on disk in the folder `~/data/newData` in two files: `ais.json` and `events.json`. This writing to disk is done once every three minutes (configurable), and when the server is shutting down. On startup, all data from these two files is loaded into the cache to restore the previous state.

### Caching of requested data

The request cache keeps a configured maximum number of buckets in cache. Buckets are added to the cache when they are requested, and are stored in an aging hashmap. Every time the bucket is requested, it is put in the request cache again in order to refresh it's age.

When new data is inserted in the platform for a bucket which is currently loaded in the request cache, the new data point will be added to the cached bucket. This way, the request cache is always up to date with newly inserted data (which isn't yet in the database), and using the request cache is a plain simple and highly optimized.

The request cache is optional, the server would function just fine without it. The size of this cache is configurable, and can be set larger when there is more memory available.