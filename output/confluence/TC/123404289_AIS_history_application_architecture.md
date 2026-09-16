---
id: confluence:123404289
source: confluence
type: page
space: TC
title: AIS history application architecture
author: Michel Wilson
date: '2022-07-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/123404289
explicit_links: []
---
# AIS history application architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/123404289  

## Content

The AIS history application is in control of the storage of all received AIS data, and offers a scalable API to support retrieving this history. It consists of several separate services:

* **incoming**: a service that listens on the full update queue and stores newly received data in the database. This is the equivalent of the `new_data` storage in the old platform.
* **bucketing**: a service that takes newly received data that is older than a configurable threshold and stores it in *buckets* in the database. The bucketing mechanism is described below.
* **archival**: a service that retires old buckets to the S3 data archive.
* **api**: a horizontally-scalable service that allows clients to retrieve data using several different types of queries.
* **converter**: temporary service to convert data from the old Mongo archive to the new format.

This article will first describe the data format used to store the AIS data itself, and then the bucketing mechanism, which is key to providing both good performance when storing data as well as when retrieving the data using the supported queries.

## Data format

As the AIS history application will store very large amounts of data for considerable periods of time, it is worthwhile to briefly assess the impact of different storage options, based on how MongoDB stores data.

The data that needs to be stored are a series of AIS messages, of which we have four different types. The first choice that needs to be made is whether to store all four messages in a single list, and use polymorphism based on a type field to deserialize them, or to keep the messages in separate lists. This is a relatively simple choice: if a type field is used, this field (and its value) will be present in *every* message that is stored. Using a list per type completely avoids storing this data! The downside is that converting the data into a single stream (with multiple types) is slightly more difficult.

To store the data in the lists itself, some thought can also save a significant amount of storage. MongoDB does not record any type information in the list itself, meaning that for *every* entry in the list, *all* the field names have to be stored. If we consider a single ship, sending out position updates every 20 seconds for a full year, if we store the position data using the following format:

json{
"position": {
"latitude": 12.34567,
"longitude": -3.4567
}
}

this means we have to store the field names `position` (8 bytes), `latitude` (8 bytes) and `longitude` (9 bytes), a total of 25 bytes, for every update. Since we have 3 updates times 60 minutes times 24 hours times 365 days, we have 1.576.800 updates in total. Given 25 bytes for the field names, this equates about 37.6MB *just* for storing the field names. Of course compression can reduce this overhead, but it is still a considerable amount of data to store, and it also has impact on serialization and deserialization performance.

Given the above, there are some simple options to reduce data storage:

* **abbreviated field names**: instead of using `position`, `latitude` and `longitude`, the data can be serialised as `"p": [12.34567, -3.4567]`, for example. Similar abbreviations can be made for all the other fields.  
  This is a relatively simple solution, it allows for easy inspection of data in the database (given that the abbreviations are easy to remember), and it allows for easy model updates as well. The downside is that there is of course still some overhead (but much less).
* **differential updates**: similar to the `diff` stream, it is possible to first store the complete data structure, and subsequently to only store the difference with the previous element in the list (also known as *delta encoding*). For data streams where a lot of fields do not change, this can save an enormous amount of data.  
  Data inspection is more difficult using this format, and when a specific time slice needs to be retrieved, reconstruction has to start at the beginning of the stream, where the initial state is recorded, ant to apply all the diff updates until the start time of the request has been reached. One way to mitigate this is to regularly have a full update in the list, so that fewer diffs have to be processed. Note that this is a similar principle as MPEG video streams, with I (complete) and P (differential) frames.
* **array encoding**: instead of always recording the field names, it is also possible to serialize the elements of the object as an arary, using a known order. Without further measures, this disallows any model changes, as this method relies on a known ordering. To allow model changes, a simple trick is to start the list with an array of field names, which describes the ordering of all the data in the list.  
  Data inspection is almost impossible using this format, and it might not play well with the differential update idea: it could lead to very sparse arrays, which will not be very efficient.

TBD: we need to determine how big the difference is between “just” using abbreviated field names with differential updates and also using array encoding. I have the feeling it might not be worth the trouble, but it would be good to have the data to back this up.

## Bucket mechanism

To facilitate quick data access, data is stored in two daily *buckets*, one indexed by MMSI, and the other by location (squares based on latitude and longitude).

TBD: this is basically identical to the existing mechanism, so not going to explain any further now, section should be expanded

## Incoming

The `incoming` service persists the newly received updates in an efficient way in the database. The bucketing mechanism cannot be used directly here, as it has been determined that continously retrieving, re-ordering, and writing existing buckets has a prohibitive impact on performance. The approach that is used instead is that the `incoming` service collects new data for a given period of time (10 minutes? check existing platform, do tuning!), and then stores the data into temporary buckets. These buckets are, contrary to the main mechanism, *not* unique. This allows the `incoming` service to just append data to the collection, instead of reading, merging, and then storing the data. The downside is that, when satisfying API requests, multiple buckets have to be sorted and merged.

## Bucketing

The `bucketing` service combines data that has been stored by the `incoming` service into daily buckets, and either adds those to the history database, or combines them with any existing buckets for that key. Note that only data that has been received at least a day ago should be processed by this service, otherwise a lot of bucket updates have to be made which slows down performance considerably.

## Archival

To limit the amount of data stored in the database, buckets that are older than a given time are retired to S3 for long-term storage.

TBD: have a discussion/brainstorm about the best storage format to use here. BSON? Gzipped JSON? Also see what is currently used.

## API

The `api` service is used to retrieve data from the storage. Requests are satisfied from multiple data sources:

* The incoming collection, if applicable given the time period of the request
* Buckets in the Mongo database
* Buckets in the old Mongo database, these are to be converted on the fly to the new format
* S3 storage, both old format and new format

Since we are also slowly converting data from the old to the new database, we need some logic to ensure that no data is missed, i.e., we need to know where to look for the data. This can be achieved very simply: if a bucket key is found in the new Mongo database, we can assume it has been converted. If it’s not there, only then do we have to go to the old Mongo database. If data is still not found, we go to the new S3 storage, and then to the old format

The service should be built using a stateless architecture, so that it is easy to scale it horizontally.

## Converter

After the old platform data storage has been disabled, we can run a service in the background that slowly converts stored data from the old MongoDB to the new MongoDB. It seems most efficient to start at the newest data, and to slowly work our way back in history. Note that some form of locking is needed here, the bucketing service can (and will) modify buckets in parallel with the conversion process. Care needs to be taken that only one of them is updating a bucket at the same time.

At the current time, we only envision a need to convert the Mongo database to the new format. Converting all of the data stored in S3 is probably not necessary.