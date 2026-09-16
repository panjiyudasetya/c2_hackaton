---
id: github:teqplay/portreporter-backend:issue:1199
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1199
title: 'Prp-1453 : Automatically Calculate Week Start For Invoice Reporting Based
  On The Cron Expression In ''Schedule.Invoicing'' Property.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1199
labels: []
explicit_links: []
---
# Issue #1199: Prp-1453 : Automatically Calculate Week Start For Invoice Reporting Based On The Cron Expression In 'Schedule.Invoicing' Property.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1199  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [47a35eaf97a1...5cfd6a6fed81](https://github.com/teqplay/portreporter-backend/compare/47a35eaf97a1...5cfd6a6fed81)
**Merge commit:** [5cfd6a6fed81](https://github.com/teqplay/portreporter-backend/commit/5cfd6a6fed81)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Darius Wattimena, Gavin den Hollander
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1453/calculate_automatically_week_start_for_invoice_reporting](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1453/calculate_automatically_week_start_for_invoice_reporting)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-02-01T13:10:13.507346+00:00
**Status:** MERGED

Given the _**cron**_ expression in schedule.invoicing, I get the amount of seconds to add to the week limits \(Monday to Monday\) so the invoicing week limits are shifted accordingly and the invoices fall in the right _week bucket_.
This is, given:
* The invoicing cron expression `0 11  * * * TUE`
* An invoice manually created on **Monday of \(natural\) week 32**.
**As a result, this invoice would count on the \(invoicing\) week 31** :slight_smile: 
For this, the helper function … has been replaced by `getWeeklySecondsShift(cronDef)` which returns the mentioned amount.
This value is passed to any method that, given a week returns a pair of from-to Instants.
**Note of warning!**  
I use a simplification of regular expressions for parsing the `schedule.invoicing` property. Considering that we invoice weekly, not every 2 minutes, for instance. So please, be easy on that :slight_smile:

