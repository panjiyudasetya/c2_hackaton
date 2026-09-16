---
id: github:teqplay/csi-backend:issue:2
source: github
type: issue
repo: teqplay/csi-backend
number: 2
title: Creating Tickets
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/2
labels: []
explicit_links: []
---
# Issue #2: Creating Tickets

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/2  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [3e85a8201131...38f9b8fc388c](https://github.com/teqplay/csi-backend/compare/3e85a8201131...38f9b8fc388c)
**Merge commit:** [38f9b8fc388c](https://github.com/teqplay/csi-backend/commit/38f9b8fc388c)
**Author:** Former user
**Reviewers:** Michel Wilson
**Approvers:** Michel Wilson
**Source Branch:** [createTicket](https://github.com/teqplay/csi-backend/tree/createTicket)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2019-05-14T09:33:01.450721+00:00
**Status:** MERGED

* Added ticket creation template and simplified create ticket
* Wrote tests for ticket creation and template
* Made changes according to feedback pull-request

Tickets will be able to be created by the frontend. To do this the frontend will need to know the mapping between the fields in the JSON and the types used in the backend \(`ShipFieldType`\).

For this the `TicketCreationTemplate` is used, it returns the requested ship for a given `shipId` and lists all available `fieldTypes`. The frontend can use this to create and send a ticket to the backend. The sent ticket is described in `TicketUserCreateInput`, it minimizes the amount of information the frontend needs to send to its minimum. Only a `shipId` and a list of `changes` is needed. This list of changes will then hold a `newValue` and a `fieldType`. The backend can then convert these ticket to include meta-data like: ticket source & ticket item status.

