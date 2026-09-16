---
id: github:teqplay/portreporter-backend:issue:1123
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1123
title: 'Prp-1351 : E&S Pilot. Don''T Create Portcall Subscriptions For Participating
  Agents When The Shippingcompany Is Not Informing Agents That Blacklisted The Shippingcompany.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1123
labels: []
explicit_links: []
---
# Issue #1123: Prp-1351 : E&S Pilot. Don'T Create Portcall Subscriptions For Participating Agents When The Shippingcompany Is Not Informing Agents That Blacklisted The Shippingcompany.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1123  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [245a8c82af39...fbfd2f54e054](https://github.com/teqplay/portreporter-backend/compare/245a8c82af39...fbfd2f54e054)
**Merge commit:** [fbfd2f54e054](https://github.com/teqplay/portreporter-backend/commit/fbfd2f54e054)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman
**Approvers:** Joost Laurman, Former user
**Source Branch:** [feat/PRP-1351/E_and_S_pilot/new_case_for_not_creating_agent_subscriptions](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1351/E_and_S_pilot/new_case_for_not_creating_agent_subscriptions)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-07-18T08:40:00.211708+00:00
**Status:** MERGED

For context, the one of the main purposes of the method `SubscriptionLogic.isShipKnown(...)` is to decide whether creating subscriptions for the portcall’s agent users \(see `SubscriptionLogic.assignSubscriptionProfileForAgency(...)` method\).

