---
id: github:teqplay/portreporter-backend:issue:1215
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1215
title: 'Prp-1550 : Ensure Kickbacks From Indirect Invoices Are Properly Categorised
  To Shippinglines Companies.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1215
labels: []
explicit_links: []
---
# Issue #1215: Prp-1550 : Ensure Kickbacks From Indirect Invoices Are Properly Categorised To Shippinglines Companies.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1215  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e5ee49e0e861...6fd036021046](https://github.com/teqplay/portreporter-backend/compare/e5ee49e0e861...6fd036021046)
**Merge commit:** [6fd036021046](https://github.com/teqplay/portreporter-backend/commit/6fd036021046)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [fix/PRP-1550/ensure_kickbacks_from_indirect_invoices_are_properly_categorised_to_shippingLines_companies](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1550/ensure_kickbacks_from_indirect_invoices_are_properly_categorised_to_shippingLines_companies)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-02-21T11:35:53.501166+00:00
**Status:** MERGED

Problem was that invoices which invoiceMode were INDIRECT\_VIA\_AGENCY, the actual payer is not the agency, but the ShippingCompany linked to the invoiceRows.shippingLine.
Therefore, the invoice grouping and calculation must be done according to that custom case.

