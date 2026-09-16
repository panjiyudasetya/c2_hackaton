---
id: confluence:652115972
source: confluence
type: page
space: TC
title: Platform (old) High-level Description
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652115972
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652115972
---
# Platform (old) High-level Description

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652115972  

## Content

## Vision

Efficiency and effectiveness of business in the Port of Rotterdam will be enhanced by collecting both real-time and non-real-time data feeds, and deriving new information by combining both

* Similar types of feeds in real-time to increase information quality,
* Different types of feeds in real-time to increase scope
* Feeds over time to learn and identify patterns and combined patterns

This new information will be shared to increase overall situational awareness, and stimulate collaboration. We believe that the experiment in collaboration with the Port Community is essential in developing the right products for effective collaboration. Various experiments will be constructed in collaboration with the community and with education.

## Ambition

TeqPlay will develop a decentralized big data platform that collects different data feeds both real-time and non-real-time, enabling subscription to specific real-time data-feeds, by combining multiple data-feeds, and generating multi-channel event based notifications.

A user in the system will be able to:

* Collect real-time data, e.g. position of a ship, content of a container
* Search and find non-real-time static data (e.g. map) and link them to real-time data
* Share available information with other users in a de-central manner and allow collaboration
* Implement predictive analysis on data collected
* Implement augmentation enriching feeds with each other, e.g. container contains box X, Container is on boat Y, Boat Y is at location Z and has ETA 10:15 so box X has ETA 10:15 + "normal handling process of in the port" = 13:15 The type of information exchange and information sharing in such scenario is visualised in the diagram below:

## Use cases

The TeqPlay platform will be developed in a bottom-up manner, starting with the collection of different data feeds and enabling the identification of events In order to get a more tangible understanding of the platform, some initial use-cases have been identified:

* Sharing ETA: When ships arrive in the port, the exact ETA gets relevant since there will be many parties involved at the time when the ship is anchored, and this timespan should be reduced to the minimum, to reduce overall costs. When location of anchoring and ETA are shared upfront in an electronic manner, all involved parties could optimize their schedule for it.
* Facebook timeline: Lots of information about entities (e.g. ships, anchor places, containers, agents, tug-boats, pilot ship, tie-up team, customs, …), in the port of Rotterdam is available, but scattered over different sources. If such information will be collected and coherently presented like in a Facebook timeline, new opportunities could be identified. Filters could be applied and specific KPI’s could be filled with information, enabling also a dashboard type of overview.
* Alerting platform: Platform allowing participants to be alerted via different media (E-mail, SMS, Push notification, Phone call, …) about a variety of data-event categories including:

> * Manually entered data deviating from automatic data. E.g. a ship indicates its target is London, but movements point out it >\* moved from Rotterdam to Antwerp.
> * Derivable data on e.g. the ETA of a ship, an anchoring place becoming available, warnings about waiting time at the envisioned anchor place enabling the shipper to slow down and save fuel.
> * Notification to authorities about ‘suspect’ containers getting close or ships speeding, introducing dangerous situations or other pattern deviations.
> * ….

* Coordination: When phone numbers will be registered for shippers and linked to AIS transceivers, this will enable the communication link back to the AIS node. Numerous relevant use cases could be identified for that including providing feed-back on the AIS signal, enabling warnings for dangerous situations, but also introducing business opportunities by knowing certain boats are not occupied yet in certain time-periods

## Scoping and Focus

The initial focus of the development for the platform will be focused on learning. Therefore, initial ideas in the area of time-bound and position related (both fixed and variable) entities will be realized in a bottom-up and experimental manner, aiming to learn for the architecture and design of a final platform and to identify a more strict scope. Initial scope will be on collecting data sources and feeds in the real-time domain in the Rotterdam harbour. It is believed that capturing intention of each real-life entity will help to realize more high-level reasoning and creation of intelligent solutions.