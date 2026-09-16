---
id: github:teqplay/portreporter-backend:issue:1047
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1047
title: 'Prp-704 : Shippingcompany.Nominationcollaborative Flag Into Two Independent
  Flags'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1047
labels: []
explicit_links: []
---
# Issue #1047: Prp-704 : Shippingcompany.Nominationcollaborative Flag Into Two Independent Flags

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1047  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [df98d374f4dd...ff4e9a556ed9](https://github.com/teqplay/portreporter-backend/compare/df98d374f4dd...ff4e9a556ed9)
**Merge commit:** [ff4e9a556ed9](https://github.com/teqplay/portreporter-backend/commit/ff4e9a556ed9)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-704/feat/invoicing_and_subscribing_based_on_nominations_managed_separatedly](https://github.com/teqplay/portreporter-backend/tree/PRP-704/feat/invoicing_and_subscribing_based_on_nominations_managed_separatedly)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-03-30T07:44:03.618173+00:00
**Status:** MERGED

**It’s all about splitting the Shippingcompany.nominationCollaborative flag into two independent ones for subscribing and invoicing independently.** 

1\) The **shippingCompany** flag '**NominationCollaborative**' is **refactored to** '**subscribeOnlyWithNomination**' and used just for managing Portcall subscriptions of ShippingCompanies only With nominations for those companies with that value set to true.

2\) **The former use of the flag for invoicing is replaced by** the new flag '**invoiceOnlyWithNomination**' in **invoiceOptions** for managing Invoicing portcalls to shippingCompanies which that flag in their invoiceOptions \(for that port\) is true. If not existing, then is set to false by default \(see constructor\). 

3\) Adapting unit tests to the two new flags and explicitly set options.

