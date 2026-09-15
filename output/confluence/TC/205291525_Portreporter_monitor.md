---
id: confluence:205291525
source: confluence
type: page
space: TC
title: Portreporter monitor
author: Gavin den Hollander
date: '2023-09-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/205291525
explicit_links: []
---
# Portreporter monitor

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/205291525  

## Content

One of the Items rebuilt because of the platform rebuild is the Portreporter monitor. This is a component of platform to convert detected events into events in portcall context.

**Redesign**

For this component a new application is created inside the ais-engine project. The application listens to events on nats converting them and putting them on a rabbitMQ stream for portreporter to ingest.

NOTE: In the image above, the portreporter outputs event's on nats. this is currently not the case for backwards compatibility with portreporter. While writing the portreporter monitor publishes the events to RabbitMQ

**Architecture Portreporter monitor**

The portreporter monitor is split up in different components. The flow of components can be explained by the following image.

Messages come in through nats and are handled by the Message handler. The messages handler passes the message on through the event enricher together with a callback to finish and publish the event.

The event enricher will handle the flow of the event, first looking if it has a converter for the event. When there is a converter, the enricher will enrich the event with additional information. To do this it uses information from Poma and CSI. This information is required to know if the event can be transformed into a portreporter event (A Port and ship are required. since the event is in port context).

After enriching the event with additional data, the monitor will try to convert the event to a portreport event. Picking the correct converter in case of exceptions on the event enriching.

After converting the event to a portreporter event, the enricher will try to enrich the event with a portcall id and/or a smartfleet id through a request/reply nats protocol.

**Components**

EventConverterService

This service has a big switch statement which will choose a converter picker bean. The decision was made to make this a big list to improve readability, making the decision verbose and easier to debug. Since the order of the checks could differ outcome, injecting a list of beans could have unexpected behavior.

ConversionPicker

Different events could have exceptions for specific ports. The conversion picker extends the PortConversionPicker to assign default behavior and make sure all ConversionPickers adhere to the same contract. By default there is only one converter and this will be returned. If there are exceptions for specific ports the getPortSpecificConverter can be overwritten. It might be possible that the event has multiple ports (ports can be overlapping). By default the first port is chosen, to change this the chooseBetweenMultiplePorts function can be overwritten.

EventConverter 

The bean actually converts the event, extends Converter<T >. This abstract class contains all the default behavior for creating a portreporter event from a Teqplay event. Most logic can be overwritten. This class also contains a function to call after generating part of the event. For example one additional field has to be added to the context of the event. in this case the afterGenerateContext can be used to update one field on the already generated context. This removed the need to rewrite the generateContext function and only added one field.