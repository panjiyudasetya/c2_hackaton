---
id: confluence:755007506
source: confluence
type: page
space: TC
title: TerminalPlanner / MarinePlanner
author: Richard van Klaveren
date: '2025-06-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/755007506
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/755007506
---
# TerminalPlanner / MarinePlanner

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/755007506  

## Content

MarinePlanner (also known as TerminalPlanner) helps a Terminal to visually plan a terminal, share the up-to-date terminalplanning with relevant colleagues (real-time updated) and allow automated monitoring of the vessel ETA and arrival.

An explanation on the Terminalplanner as functional and technical high-level introduction [can be found here](https://www.youtube.com/watch?v=MF5y5oI22zE).

* Scope: Global, used in Rotterdam, Terneuzen and Corpus Christ
* Users: 108 user (al at terminals)
* Main Development: 2019 - 2020 (Kotlin version, 2016-2018 for Java version)
* Team involved: Knowledge in team: Gavin (BE), Michel (BE), Fauzan (FE), Joaquin (BE), Gavin (FE), Richard (PO)
* Product / project: Product (4 customers)
* Active knowledge required: Yes
* Tech stack: Kotlin, Mongo, RabbitMq, React + JavaScript

## Data model

The simplified data model has the `terminal` entity in the center, together with the terminalVisit model. Each visit of a vessel to a terminal is one terminalvisit. When a change happens on a `terminalvisit` the old visit is stored as a `TerminalVisit_v2_history` entry. Maintenance blocks for a terminal are stored in `TerminalMaintenance`.

The `terminal` specific quay layout, products and cargo loading speeds etc are stored in `TerminalConfig`. And the users can access 1 or multiple terminals, are stored in the `users_v2` table, where also authorization per terminal is organized via 1 of the 3 types:

* Read only: only able to read the data, not allowed to change anything
* Order Admin: only allowed to update order and administrative details, no influence on quay planning etc.
* Quay Coordinator: Allowed to update the location of vessel on the quay but no other details of the orders.
* Planner: Allowed to update and change anything in that terminal

## System Architecture

The high-level Architecture looks straight forward:

When putting also the environment into context, the target architecture looks like:

However, not all components have migrated yet (June 2025) from the old architecture

And therefore the current (June 2025) architecture looks like:

diagrams can be updated [here](https://drive.google.com/file/d/1kV9JtbtQq79IaNbQKTIB56p_p2d4c71-/view?usp=drive_link)