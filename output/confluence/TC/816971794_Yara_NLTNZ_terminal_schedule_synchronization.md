---
id: confluence:816971794
source: confluence
type: page
space: TC
title: Yara NLTNZ terminal schedule synchronization
author: Joaquin Marquez Bugella
date: '2025-08-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816971794
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816971794
---
# Yara NLTNZ terminal schedule synchronization

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816971794  

## Content

Yara, an important client in Terminal Planner, has an integration of their terminal visits planning for the terminal of `nltnz_yara` (currently hardcoded) in the application’s.

It consists on a scheduled task in spring, defined in the class `SyncService` that collects the terminal planning for the future N days via a given url, dynamically built based on `yara-schedule` properties set.

**Note** that the Yara service token is exposed in the GET *query params*, which is highly insecure.