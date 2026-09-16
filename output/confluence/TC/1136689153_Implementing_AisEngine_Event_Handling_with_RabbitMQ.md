---
id: confluence:1136689153
source: confluence
type: page
space: TC
title: Implementing AisEngine Event Handling with RabbitMQ
author: Darius Wattimena
date: '2026-02-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1136689153
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1136689153
---
# Implementing AisEngine Event Handling with RabbitMQ

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1136689153  

## Content

## Getting started

Load in the needed dependency.

Dependency when in AisEngine:

kotlinwide760dependencies {
implementation(project(":api:nats-stream-event"))
implementation(project(":api:rabbitmq-event")) <-- should be added

Dependency when using as an external library:

groovywide760 implementation "nl.teqplay.aisengine:nats-stream-event:$aisengine\_version"
implementation "nl.teqplay.aisengine:rabbitmq-event:$aisengine\_version"

The version which includes the `rabbitmq-event` library is version `master-2.10.0`.

With this library you can do 2 things:

* Consuming events by extending the `EventConsumerService<T>` abstract class.
* Publishing events by loading the `EventPublisherService` bean in the service where you need the events.

## Consuming

### Code Changes

Create a new service (or extend an existing one) by implementing the `EventConsumerService<T>` class.

kotlinwide760@ConditionalOnProperty(
prefix = "rabbitmq.event.consume",
name = ["enabled"],
havingValue = "true",
)
@Service
class AreaEventHandlerService(
objectMapper: ObjectMapper,
): EventConsumerService<Event>(
objectMapper = objectMapper,
typeReference = object : TypeReference<Event>() {},
) {
override fun processMessage(message: Event) {
// The default flow of processing events
// Jackson already converted the payload string to the event model that you want in here
// Exception handling is already done to ensure things don't explode
}
}

If you want a specific type of event you can do so by directly setting the type. This does require the correct set up in RabbitMQ where only those events are given to your queue.

kotlinwide760@ConditionalOnProperty(
prefix = "rabbitmq.event.consume",
name = ["enabled"],
havingValue = "true",
)
@Service
class AreaEventHandlerService(
objectMapper: ObjectMapper,
): EventConsumerService<AreaEvent>(
objectMapper = objectMapper,
typeReference = object : TypeReference<AreaEvent>() {},
) {
override fun processMessage(message: AreaEvent) {
if (message.area.type == AreaIdentifier.AreaType.BERTH) {
// Do something with the area event
when (message) {
is AreaStartEvent -> {
// Handle start event
}
is AreaEndEvent -> {
// Handle end event
}
}
}
}
}

If you need to directly use the `message` body from RabbitMQ without the type safety the library provides, then you can do so by overriding the accept function.

kotlinwide760@ConditionalOnProperty(
prefix = "rabbitmq.event.consume",
name = ["enabled"],
havingValue = "true",
)
@Service
class AreaEventHandlerService(
objectMapper: ObjectMapper,
): EventConsumerService<Event>(
objectMapper = objectMapper,
typeReference = object : TypeReference<Event>() {},
) {
override fun processMessage(message: Event) {
// Unused
}
override fun accept(payload: String) {
// Something custom goes here, processMessage will never get called
}
}

### Configuration

Once you made the code changes you also need to configure the correct properties.

yamlwide760rabbitmq:
event:
consume:
enabled: false
uri: amqps://localhost:5671
queue: YourQueueName
qos: 10note4076875ce583

The `RabbitMqEventHandler` is not available when the `rabbitmq.event.consume.enabled` is set to `false`.

The `RabbitMqEventHandler` is not available when the `rabbitmq.event.consume.enabled` is set to `false`.

## Publishing

### Code Changes

If you want to publish events load in the `EventPublisherService` bean.

kotlinwide760@Service
class EventHandlerService(
private val eventConsumerStream: NatsConsumerStream<Event>,
private val eventStreamService: EventStreamService, // This is the old NATS service, very similar
private val eventPublisherService: EventPublisherService?, // We add the new RabbitMQ publishing service here
) {
fun publish(events: List<AreaEvent>) {
events.forEach {
// NATS publishing
eventStreamService.publish(it)
// RabbitMQ publishing
eventPublisherService?.publish(it, "some-routing-key-can-go-here")
}
}

### Configuration

Once you made the code changes you also need to configure the correct properties.

yamlwide760rabbitmq:
event:
publish:
enabled: false
uri: amqps://localhost:5671
exchange: YourExchangenote5b58130a-b784-45aa-a38a-5303875b9dfa

The `EventPublisherService` bean is not created when the `rabbitmq.event.publish.enabled` is set to `false`.

This means you need to handle yourself if you want support for setting the flag to false.

The `EventPublisherService` bean is not created when the `rabbitmq.event.publish.enabled` is set to `false`.

This means you need to handle yourself if you want support for setting the flag to false.

### Retry mechanism

In the publishing mechanism we made it so it will auto-retry when publishing fails. This ensures that if RabbitMQ goes down that you won’t lose any data.

To configure the retry mechanism you can adjust the following configuration properties:

yamlwide760rabbitmq:
retry:
max-attempts: 10
initial-delay-ms: 500
max-delay-ms: 30000
backoff-multiplier: 2.0

You can also not do any retrying by calling the following when calling the `publish` method in the `EventPublisherService`:

kotlinwide760eventPublisherService.publish(
event = it,
routingKey = "some-routing-key-can-go-here",
enableRetry = false // By default this is `true`
)

When you do this you are expected to catch any exceptions that may occur.