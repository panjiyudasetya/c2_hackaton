---
id: confluence:225411073
source: confluence
type: page
space: TC
title: Bucketing in ais-engine
author: Michel Wilson
date: '2023-11-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/225411073
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/225411073
---
# Bucketing in ais-engine

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/225411073  

## Content

AIS data is stored in *buckets* that can be quickly accessed by their *bucket key*. Each data point is stored in two buckets: one bucket has a key based on location, the other bucket uses the MMSI as key. This allows us to quickly retrieve data based on area/location, while also allowing us to retrieve all the data from one particular ship without knowing the area in which it was sailing.

This document will describe how the data flows through the various bucketing stages. Per stage, performance considerations are briefly highlighted that explain why/how the amount of data in this stage has to be limited (if so), and the reason for having this stage is highlighted.

# Buffer stage

The very first stage is a simple buffer stage in which all incoming ship data is (almost) immediately written to the database for persistence. Data is not yet grouped together in a bucket, only the bucket keys are computed for every data point. For every bucket key field, an index exists to allow the data to be quickly retrieved.

A major concern for this stage with respect to performance is the collection (and index) size: the more data is contained within the buffer stage the slower performance will be. This means that the data in the buffer stage must be collected with a regular interval and stored in the next stage. To ensure that no race conditions occur between writing new data and purging data that has been collected and written to the next stage, the data rows in the buffer stage have a *generation* key. This is essentially the time at which the previous collection run has been started: at the start of the collection run, the current time is used as the new generation key for any new data that is written to the buffer. Only data with a generation key older than the current generation key is collected, stored in the next stage, and then purged.

The reason for having a buffer stage is twofold: it is desireable to immediately persist data to ensure that we don’t lose any state when the ship history processor crashes, and secondly, persisting the state immediately allows the ship history api access to the most recent data. A third bonus reason is that a restart of the ship history processor is much quicker, as the state doesn’t need to be written out to the database first.

# Unordered buckets

The next stage is the first stage that contains actual buckets of data: every bucket key can have one or more data points for that key. There can be multiple buckets for each key, i.e., the bucket key is not yet a unique key. Also, the data in the buckets itself is not yet deduplicated and chronologically ordered (hence the name unordered buckets).

The performance limitation for the unordered buckets lie in having to sort and deduplicate data for every read request. If the time span for the unordered buckets exceeds multiple days this will turn into a major performance bottleneck. Hence, every day, unordered buckets older than *x* days are collected, sorted, deduplicated, and written to the next stage.

The reason for having the unordered buckets is also performance-related: when new data still comes in regularly, constantly keeping the data ordered and deduplicated is very time-consuming. Only after *x* days it is assumed that read requests will greatly outnumber write requests for the buckets, meaning that at this point we *can* order/dedupe the data.

# Ordered buckets

This is the final stage in terms of storage: every bucket key is now unique, and the data in the buckets is ordered, meaning that read requests can be served very quickly without having to do any data manipulation at all.

Note that the ordered buckets are stored twice: once in the Mongo database for quick access, and once in S3 for long-term storage. This is done for the obvious performance/cost reasons: recent data is accessed more often than older data.