---
id: confluence:652443670
source: confluence
type: page
space: TC
title: Developing a new adapter / monitor
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443670
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443670
---
# Developing a new adapter / monitor

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652443670  

## Content

# Introduction

This page describes the process through which a new adapter object can be written within the teqplay platform. It will provide the general structure of an adapter and the relationship it has with other key components in the platform. Once that has been done the focus will be on the architectural position of the adapter within the platform. This will cover topics such as:

* Getting your adapter running by the platform during the booting sequence.
* Extending the adapter system to be able to mutate the state of your new adapter.

# Writing the adapter

Within the teqplay platform and adapter is defined as:

**A component that is able periodically run and retrieve external information**

That sounds simple enough but an adapter also needs something to manage it. Something which monitors the adapter. It provides information such as:

* Is the adapter still healthy?
* When was the last time the adapter ran?
* When was the last time a successful run took place?

The following diagram shows the various components and how they relate to each other:

There are two key components involved in the adapter creation process. In the diagram they're shown as type I and type II.

**Type I: Monitored Object**

This is the control object. This has a reference to an adapter which performs the actual logic. This object is called a monitored object. It monitors some data of an adapter and allows certain operations on it:

1. Name
2. Type
3. Whether it's active or not
4. Whether it's healthy or not
5. The last time it successfully ran
6. The last time it ran
7. Restarting the adapter
8. Stopping the adapter
9. Starting the adapter

There are already 2 implementations which do this:

1. BaseMonitoredObject. This is the general use one. This should work nicely for most adapters that are timer based.
2. EventProducingMonitoredObject. This is a specialized variation used by adapters which produce events.

If the adapter you are building does not fit in both these categories you will need to write your own MonitoredObject implementation. It should include all the points detailed above if possible.

The main reason for separating the monitored object logic from the actual implementation is that some control mechanisms (like the time) do not allow to reuse a 'crashed' adapter. Therefore the object being monitored (which you typically want to reuse) needs to be separate from the actual executed logic.

**Type II: Adapter functional implementation**

This is the component which runs the adapter logic. It should contain a reference to its MonitoredObject, in order to update it regularly. The adapter is in most cases a subclass of TimerTask. This is so that it can be scheduled to run regularly in its own thread. Some adapter implementations are triggers only by events arriving, these are typically not timer triggered. The adapter should also update its MonitoredObject with information such as:

1. At which time it started its last run
2. When the last successful run happened
3. Its name

There are already two designs for this

1. Monitor. The general abstraction to use for your adapter.
2. EventProducingMonitor. If you need to produce events this would be your choice

In contrast to Type I these are not implementations! They are abstract classes and you will have to extend one of them in order to write your adapter. If both of them are not what you are looking for then you should write your adapter independently.

If you used one of the two above choices above you will have to add logic to the relevant factory class. The new method should return an instance of your new adapter. In order for this to work you will need to add an identifier for your adapter. You will need to add this to:

1. MonitoredObjectType
2. MonitorType/EventProducingMonitorType/none

All adapters should have a type in monitoredObjectType. Depending on what factory you use you need to add it to MonitorType or EventProducingMonitorType or nothing at all.

# How to have your adapter start on boot

**nl.teqplay.platform.AdapterAndMonitorInitializer.java** During the boot sequence of the platform the AdapterAndMonitorInitilizer class will start up the adapters en monitors. These will be wrapped into monitoredobjects before they are passed through the system. It calls a static method from the AdapterMonitorCreationLogic class. It will receive a monitoredobject from this method call. This object will then be added to the system.

**nl.teqplay.system.AdapterMonitorCreationLogic.java** This class contains all logic related to creating any monitoredobject defined in the platform. You will need to add a public static method here. It should be able to read the needed values from the config file and create the monitoredobject. After that the monitoredobject should be returned.

# How to integrate your adapter with the MonitoredObjectSubSystem

The MonitoredObjectSubSystem is responsible for starting, stopping and restarting monitoredobjects. The startAdapter method works based on MonitoredObjectType. Therefore you need to add logic on how to recognize and use your new adapter type.