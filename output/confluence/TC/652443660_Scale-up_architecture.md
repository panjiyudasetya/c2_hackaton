---
id: confluence:652443660
source: confluence
type: page
space: TC
title: Scale-up architecture
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443660
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443660
---
# Scale-up architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443660  

## Content

To allow the Teqplay platform to scale to a global level, and have a well maintainable and reusable platform for operational use, multiple steps are foreseen to be executed. The envisioned steps are composed of changes in architecture and modification of the development process. In order of priority, these steps are from a high-level perspective:

1. [DONE] Change architecture to have world-wide feed available, Hamis feed accessible from anywhere and have no/minimal chained dependencies between the platforms.
2. [DONE] Redevelop mechanism of historical AIS data storage in a scalable manner
3. [DONE] Continuous monitoring and auto-recover of all components. Also all dependencies should be monitored, either via the adapter using the feed, or via a separate process. (PLATFORM and FRONTEND PROJECTS, e.g. rollbar)
4. [DONE] Redevelop mechanism for events storage in a scalable manner.
5. [DONE --> luxspace] Find a connection to a worldwide AIS feed, being composed of:

   1. Terrestrial data
   2. Satellite data
6. Platform configurable via REST API, no need for a configuration file, but hosting the configuration in a database, and each extension will write its own defaults to the database
7. [DONE] Platform scalable to process all world-wide AIS data and maintain historical information for all vessels.
8. Scalable REST API for the users, which can properly scale out when more users are requesting the information
9. [DONE] Include Authorisation per application running on top of the platform
10. Enhanced Monitoring of the platform in a single dashboard.
11. AIS History to be stored in a cloud key-value store
12. Using a single AIS History instance giving access to all platforms to global AIS
13. Allow for recalculation of the events
14. Configuration of the basic event detections
15. Code quality more under control, using continuous integration on all processes, thorough unit-testing (PLATFORM and FRONTEND PROJECTS), shared code coverage, Automated code style checks
16. Platform and front-end components deployable with one click, including distributed deployments, version number in the API etc. (PLATFORM and FRONTEND PROJECTS)
17. Code re-use between frontend projects, using reusable snippets and util libraries.

    * [DONE] create a geolocation-utils library for conversion and calculations with geolocations in the frontend
    * [DONE] create a util library for various types of markers on the map.
    * [DONE] create a Client SDK library to make it easier to work with the platform backend. This library will start getting real added value as soon as we enrich it with for example logic for searching and filtering inside fetched data, and smartly caching fetched data.

For details for each of these bullets, a more detailed explanation is provided below.

## Ad 1: Global architecture

This step has been executed in the meantime. The global AIS feed is available from [aisdata.teqplay.nl](http://aisdata.teqplay.nl), which is also the node where port ATA / ATD events are being fired and being fed into cloudAMQP, which can be read from one or multiple local operational platform nodes.

The Hamis feed is not forwarded from one to another node anymore, but retrieved from each node individually. Therefore the only dependency between systems is the availability of the global AIS node.

## Ad 2: AIS stored in a scalable manner

The Teqplay platform collects huge amounts of AIS data. Currently there are about 2 million data points collected every day, about 1GB per day (monitoring just a part of Europe). The database indexes required to enable searching through the data are almost as large as the data itself, doubling the amount of used disk space. MongoDB didn't perform well with these amounts of historic data (lots of very small documents, huge indexes). Part of the problem was too limited hardware (not enough RAM and IO).

To make a better scalable solution for the long term, the data points have been put into buckets. This is explained in detail on the wiki page [Platform Data Storage](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Platform%20Data%20Storage).

## Ad 3: Continuous monitoring and auto-recover

All backend systems are continuously monitored and a platform monitor has been developed. The platform monitor reports about adapters / monitors that are not properly running. Additional steps to be taken:

* Monitor our platform dependencies, e.g. weather services, Hamis, tide services etc
* Monitor the use of our front-end applications
* Monitor the problems occurring in the browser, e.g. via Rollbar like mechanisms

## Ad 4: Scalable event storage

Initially, the events where stored as individual documents in a single Mongo collection. Similar to AIS data, this became a bottleneck too, and the events are now stored in buckets. This is explained in more detail on the wiki page [Platform Data Storage](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Platform%20Data%20Storage).

## Ad 5: Global AIS feed

In order to scale globally, a global AIS feed is required. Some research has been done on this subject (see also the global document) with following conclusions:

* AisHub is pretty unique, hardly any other fee data-sharing services are available
* One Aishub alternative is Volpe, setup for Maritime safety and security. An account has been requested on name of Bob Madlener, with Richard as the technical person, backed up by port of Rotterdam. See also: <https://mssis.volpe.dot.gov/Main/>
* For The Netherlands, a collaboration with Cofano and AisHub has been started to cover the non-covered areas.
* All other global AIS feed providers will require a partnership, since selling the AIS data for huge amounts of data. Together with RLL a partnership with Marinetraffic might be started on this.

## Ad 6 and 7: Scalable REST API and separation processing / data retrieval

When scaling, the number of ships on the world will not endlessly grow. Therefore, throwing iron at it might be the right approach for the data processing part. For the request part however, the number of users might grow a lot. In order to cope with that, a clear cut between the data processing part and the users requesting data should be introduced. The data processing part will be scaled vertically and the user API will be scaled horizontally.

Current architecture when linking 2 nodes together looks like the diagram below:

In current architecture, adapter do have knowledge about the specific worldmodel they will be updating, and they only update the local world-model. There are no events involved in updating the local world-model. The updated world-model is consulted once in a while by the different monitors, which detect higher level changes (e.g. encounters between a vessel and a bridge) and will fire events for that. Such events will be made available on the local bus, and stored in the World-model. When connecting 2 Teqplay nodes to each other, there are 2 possible uses:

1. The API of the other platform is used, and all data is duplicated to the second platform
2. Externalizing the eventBus, using an CloudAMQP connection to pass events from one to another node.

In order to scale-up properly, the architecture will need to be able to handle world-wide AIS data and be able to handle a huge amount of user requests. For the scaling of the processing part (deriving new events etc) the limits are set by the current amount of vessels around the globe, combined with a multitude of the areas currently being monitored. Currently it does not yet seem necessary to do a proper scale-out for such level of scaling, probably throwing more iron at it, and separating the world in continents is expected to be enough to scale worldwide. For the user demand side however, quite an increase in requests could be foreseen. Therefore, this part needs to properly scale-out. The foreseen architecture for this is visualized in the diagram below.

In this architecture there is a distinction between 3 different types of nodes:

* **Data-source node(s)**: responsible to parse one or multiple data-sources, verifying the results against the local world-model and sharing the identified updates on the Teqplay platform wide event-bus
* **Processing node(s)**: Responsible to run the monitors and predictors, identifying the events and storing such into the world-model, which is being synched to the mongo cluster data persistence node
* **Output API node(s)**: Responsible to expose the results of all parsing via the API to the users via direct system connections, Web-apps and mobile apps.

As long as the event bus is shared among all components, multiple instances of each node-type can independently scale, depending on e.g. amount of input sources (for data source nodes), amount of events to be monitored / generated per geographical area (for processing nodes) and number out end-users requesting data from the system (for output API nodes). For the latter, the idea would be to have always one master node, being fully up-to-date, which can be used to replicate all current states to a brand-new node as initialization for such node when scaling up. For historical data each node is connected to the mongo Cluster.

The underlying data-source might be based on Mongo, which will use sharding to scale-out. However, the event and ais data might also be stored in a cloud based key value map store solution, such as Google Cloud datastore.

Please note that with such high dependency on the event bus, another event bus mechanism than the current CloudAMQP and Apache ActiveMQ should be considered. One thing to research would be apache Kafka, but also consider others.

## Ad 8: Platform fully configurable via the REST API

Currently the platform depends on multiple configuration files, which are read during startup of the system. When changing the configuration of one or multiple adapters or monitors, this requires a platform restart in the current setup. Changes expected in this area are:

* Configurations are stored in the database. On startup these values will be read from the database, and for each configuration a fail-safe default value is defined.
* The configuration objects can be changed in the database via the REST API.
* Each of the monitors and adapters can be restarted, which will result into a re-read of the configuration
* Make sure the system can be re-configured via a GUI

This will allow for a fully configurable system, that can be properly reconfigured without any user disruption

## Ad 9: Authorisation per application

Since there was no real need for authorization thus far, authorisation has not been fully implemented in the platform. The limited authorization available right now is: each user is either a normal user of an admin user. For each of the applications supported by the platform, a user authorization profile should be associated to the userProfile. This is currently not foreseen to be any rocket science, but just implement a role-based authorization.

## Ad 10: Monitoring in a single dashboard

Monitoring has been implemented in the platform, and loads of information on performance, events, logs, etc is available. At this moment in time, the platform is monitored in 4 different ways:

1. At the infrastructure level, monitoring performed by AWS, DevOps team updated via E-mails
2. As a blackbox API by <http://updown.io> monitoring latencies from 5 different continents, notifications sent via E-mail and Slack.
3. Functionally, all adapters and monitors to be up, notifying the DevOps team via E-mail.
4. On specific Pronto events still being sent to Pronto, if certain events are not detected for longer than X hours DevOps team is alerted via E-mail.

In addition to these pro-active monitors, there is many log-files available:

1. errors/bucketslog capturing all errors on buckets (AIS / Events) to be stored
2. prontolog.log capturing all events sent to pronto
3. perflog.txt dumping the memory use and claims every x minutes
4. monitor.log holding the logging of the monitor watching the platform
5. platformmonitor.0.log.0 holding the generic platform logging

Finally there is a bunch of tools typically used to analyse issues at the platform:

1. htop to see current performance issues on memory and cpu
2. jstack to identify which thread is involved in what, to nail down the most busy thread
3. aws User interface to see trends in performance
4. grep to filter log files
5. .... and many more

There is a need for a logging dashboard that reduces the learning curve and allows to get in an easy way a total overview on the platform status, enabling faster trouble shooting and easier monitoring. A first step to get towards such solution would be to get insight in what logs / tools / monitors are currently in place. Above documentation gives a first attempt for that.

## Ad 11: AIS History to be stored in a cloud key-value store

The underlying data-source for AIS so far is based on MongoDb. Main issue in the scalability is in the storage of AIS data and event data. Most probably the most simple and cost effective apprach to make this scaleable is to use an online key-value store that already addresses full scaling, such as Google Cloud datastore.

Most of such key-value stores bill the user mostly for the data-transfer, and limited for the data storage. Combining this solution with a 1 or 2 month Mongo solution, and data older than 2 months will be retrieved from the key-value store is a direction to be further explored.

## Ad 12: Using a single AIS History instance giving access to all platforms to global AIS

When all data is retrieved from one place, there will be a more clear and less expensive architecture. Combined with the previous item, this might be a very nice architecture.

## Ad 13: Allow for recalculation of the events

Currently events are based to often of 'System.currentTimeMillis()', which makes it impossible to recalculate events. Since events are derived data, it would be great to derive such data at any later moment. This will also allow for fixes afterwards, are simulation to compare events in one situation compared with the same situation and other event triggers.

## Ad 14: Configuration of the basic event detections

Current basic event detections (encounters for vessels, bridges, locks etc) are currently configured via a global setting. Since these detection criteria might not be the same for all ports and areas on earth, a mechanism should be implemented where such default rules will apply to all places in the world unless an exceptional rule / detection is implemented for a specific area. This will make the detection mechanism fully configurable and flexible for all locations on the globe.

## Ad 15: Code quality more under control

In order to continuously increase code-quality, there will be multiple mechanisms that will need to always run: \* Each project (backend and front-end) should implement unit-testing \* Backend projects will require proper integration testing where possible. Such integration tests should mainly run in the development environments, no data in the live systems should be touched by such systems. \* Front-end projects should implement where possible more automated user tests, using for example Robolectric or any other appropriate framework. \* Both backend and frontend projects should be properly documented, with all information available via the Readme page in bitBucket.

## Ad 16: Continuous deployment with man in the loop

All projects (both backend and frontend) should be deployable with a single click. No manual configuration should be required, except for the configuration via the REST API. REST API should include version numbers, and even when a deployment is composed of a distributed deployment (e.g. NEI depends on both the Teqplay Backend, NEI backend and the NEI frontent), it should be possible to execute such in an automated manner, with a single click.

## Ad 17: Code re-use between frontend projects

More and more frontend components will be reused from other projects. The envisioned approach is to use snippets from other projects, and share those snippets again for other projects. An initial start on this has been made in the wiki, where for each front-end project a short description is provided which components (map, timeline, list view) are included, and which technical frameworks have been used as a basis (e.g. Angular, React).

Some ideas for a Client SDK library: As long as this is a simple wrapper for the REST API, there is not that much added value. Things start becoming interesting when implementing things like caching and logic for filtering fetched data. This is something many apps need. Many apps do something with displaying ships in time on a map. This requires fetching data of an area of the last few days for example. This requires a lot of data to be fetched, which has it's limitations. It can be interesting to develop a way to get the state of all ships in an area at a specific time in the past directly from the server. Or get the historic data of an area in small chunks which are cached and complemented as soon as the user actually needs data at that point in time (sort of like the tiles of google maps are only fetched as soon as you need them).