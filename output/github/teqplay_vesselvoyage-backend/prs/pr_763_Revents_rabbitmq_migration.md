---
id: github:teqplay/vesselvoyage-backend:pr:763
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 763
title: Revents rabbitmq migration
author: TeqJoostD
state: closed
date: '2026-04-20'
merged_at: '2026-04-23'
base_branch: develop
head_branch: revents-rabbitmq
url: https://github.com/teqplay/vesselvoyage-backend/pull/763
labels: []
linked_issues: []
explicit_links: []
---
# PR #763: Revents rabbitmq migration

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/763  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `revents-rabbitmq`  
**Created:** 2026-04-20  
**Merged:** 2026-04-23  

## Description

_No description._

## Commits

- `80f92219` **TeqJoostD** (2026-04-18): Converse NATS to RabbitMQ
- `644a4589` **TeqJoostD** (2026-04-19): Change subject and make a fix for it
- `5db5f05e` **TeqJoostD** (2026-04-19): Fix poison pill mechanism
- `7f23beac` **TeqJoostD** (2026-04-19): fix test
- `adf275d7` **TeqJoostD** (2026-04-19): fix test
- `1b002e2d` **TeqJoostD** (2026-04-21): PR Feedback
- `589ddf08` **TeqJoostD** (2026-04-21): PR Feedback
- `d6655b93` **TeqJoostD** (2026-04-21): ktlint formatting 0-0
- `f682253e` **TeqJoostD** (2026-04-23): aisengine stable version

## Reviews

### Darius-Wattimena — CHANGES_REQUESTED (2026-04-21)

_No comment._

### TeqJoostD — COMMENTED (2026-04-21)

_No comment._

### TeqJoostD — COMMENTED (2026-04-21)

_No comment._

### TeqJoostD — COMMENTED (2026-04-23)

_No comment._

### Darius-Wattimena — APPROVED (2026-04-23)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/config/ReventsRabbitMqConfiguration.kt`

Is this annotation needed?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsReventsMessageProcessor.kt`

Annotation not needed?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsReventsMessageProcessor.kt`

What is this magic number? Would move `999` to a constant so it makes more sense?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/VesselVoyageRabbitMqEventConsumerService.kt`

This annotation shouldn't be needed?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/VesselVoyageRabbitMqEventConsumerService.kt`

Can't we provide a class reference here instead of directly using the name of the bean?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/VesselVoyageRabbitMqEventConsumerService.kt`

Is this really needed? This `EventStreamService.MessageContext` interface is from NATS related code? Should not be needed if we just use the RabbitMQ related code?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/revents/VesselVoyageChangePublisher.kt`

Do we need to override this here when we already provide the `reventsRabbitMqProperties` in the contructor and assumingly set the `uri` and `exchange` with the provided properties?

### Darius-Wattimena — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/revents/VesselVoyagePoisonPillPublisher.kt`

Why is this all in a companion object? Don't think you need static methods and the `log` can just be initialised when we create the `VesselVoyagePoisonPillPublisher` class like we normally do for other classes?

### Darius-Wattimena — 2026-04-21 on `src/main/resources/application-revents.yml`

This shouldn't be needed as the name of the file `application-revents.yml` already only loads in when the `revents` profile is active

### Darius-Wattimena — 2026-04-21 on `src/test/kotlin/nl/teqplay/vesselvoyage/ApplicationTest.kt`

This can also go?

### Darius-Wattimena — 2026-04-21 on `src/test/resources/application-revents.yml`

This is also not needed to have the active on profile part

### Darius-Wattimena — 2026-04-21 on `build.gradle`

Please make a release version for this

### TeqJoostD — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/VesselVoyageRabbitMqEventConsumerService.kt`

Sadly, no

### TeqJoostD — 2026-04-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/VesselVoyageRabbitMqEventConsumerService.kt`

Will be removed in nats removal PR

### TeqJoostD — 2026-04-23 on `src/test/kotlin/nl/teqplay/vesselvoyage/ApplicationTest.kt`

Different pr

## Comments
