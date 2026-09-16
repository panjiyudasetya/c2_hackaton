---
id: github:teqplay/portreporter-backend:issue:1268
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1268
title: 'Prp-1983 : Getting A Smartfleet Subscription Takes Into Account The Requesting
  User (Logged-In Or Impersonated).'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1268
labels: []
explicit_links: []
---
# Issue #1268: Prp-1983 : Getting A Smartfleet Subscription Takes Into Account The Requesting User (Logged-In Or Impersonated).

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1268  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [da133b0cad5c...e4f4783c8ea0](https://github.com/teqplay/portreporter-backend/compare/da133b0cad5c...e4f4783c8ea0)
**Merge commit:** [e4f4783c8ea0](https://github.com/teqplay/portreporter-backend/commit/e4f4783c8ea0)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [fix/PRP-1983/smartfleet_subscription_should_subscribe_for_logged_in_user_or_impersonated](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1983/smartfleet_subscription_should_subscribe_for_logged_in_user_or_impersonated)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-11T14:10:48.235137+00:00
**Status:** MERGED

In a nutshell the changes are about:
1. In the controller endpoint, pass over the email \(whether logged in or impersonated\) to the logic layer method.
2. In the logic layer, pass over the email to the data layer method.
3. Use the email to get the right subscription \(by fleetId and email\) \(Using the correct method\).
4. Additional adaptations of related code \(to link/unlink\) and clean up.

