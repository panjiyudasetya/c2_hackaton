---
id: github:teqplay/portreporter-backend:issue:991
source: github
type: issue
repo: teqplay/portreporter-backend
number: 991
title: 'Prp-54 : Generating The ''Nominated'' Field With Different Flows For Directbilling
  And Viaagent Invoiceoptions'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/991
labels: []
explicit_links: []
---
# Issue #991: Prp-54 : Generating The 'Nominated' Field With Different Flows For Directbilling And Viaagent Invoiceoptions

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/991  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [1ba938e99025...364d6a1445f3](https://github.com/teqplay/portreporter-backend/compare/1ba938e99025...364d6a1445f3)
**Merge commit:** [364d6a1445f3](https://github.com/teqplay/portreporter-backend/commit/364d6a1445f3)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Richard van Klaveren
**Source Branch:** [PRP-54/fix/Different_flows_for_DirectBilling_and_ViaAgent](https://github.com/teqplay/portreporter-backend/tree/PRP-54/fix/Different_flows_for_DirectBilling_and_ViaAgent)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-11-22T14:33:35.574568+00:00
**Status:** MERGED

Based on a new description, the Nominated column value is set slightly differently when the invoicing Options is **Direct Billing** or **Via Agent.**

When is **Direct Billing**, the company to check on to be participating is from the _**InvoiceGroup**_.  
Whereas when is **Via Agent**, the company to check on to be participating is from the _**InvoiceOption**_.

