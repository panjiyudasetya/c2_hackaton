---
id: confluence:799440897
source: confluence
type: page
space: TC
title: AlongsideMonitor
author: Richard van Klaveren
date: '2025-07-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/799440897
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/799440897
---
# AlongsideMonitor

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/799440897  

## Content

AlongsideMonitor (also known as ShipSpareLogistics) helps to provide insights to teams providing alongside operations to Sea-vessels. The application maps the planning of the alongsideprovider on the actual state of the vessels to be served and allows this way insight in what requires attention right now. Ideally the alongsideprovider is using barges equipped with AIS, but also truck support is provided.

Users of the AlongsideMonitor are either the planners / coordinators overlooking the full operations, or the barge captain using it to overlook their own operations.

* Main Goal(s): Provide Visibility for alongside providers on where the vessels are, where they need to provide alongside services
* Scope: Rotterdam, Amsterdam
* Users: 31
* Main Development: 2019
* Team involved: JoostL (BE), Damon (FE), David (FE), Richard / Daan (PO)
* Product / project: Project for ShipSpareLogistics.
* Active knowledge required: yes
* Tech stack: Kotlin, Mongo, RabbitMQ, React + Typescript, react native app

An explanation of the AlonsideMonitor application and its use [can be found here](https://www.youtube.com/watch?v=CfYXoCP4LmY).

## Productizing

Alongsidemonitor has started as an experiment with ShipSpareLogistics (SSL, a company in Rotterdam) and is continued to be used in operations after the experiment. After the successful experiment, it has been converted into a multi-tenant architecture, called PortSupport. This product has been piloted with multiple other alongside providers, but never was successfully launched.

## Technical

It has an integration with the planning at SSL which is being exposed via RabbitMQ (in CloudAMQP) to the backend. SSL shares the planning in Json on this queue every 15 minutes. Also, the state of the stores is being shared every hour, which allows Alongside monitor to detect there is a package in stores that has to be delivered to one of the vessels visiting the port in the next 2 days. Also this state is shared via RabbitMQ (CloudAMQP).

Implementation of the backend in AlongsideMonitor is pretty stateless (except for the customer provided data). It requests all data to original systems (like AisEngine) every time the data is being requested by the user.

Front-end: There is a [web version](https://alongsidemonitor.teqplay.nl/) of the app, but also a React Native version.