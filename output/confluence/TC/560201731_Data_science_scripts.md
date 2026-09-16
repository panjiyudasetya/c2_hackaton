---
id: confluence:560201731
source: confluence
type: page
space: TC
title: Data science scripts
author: Michel Wilson
date: '2024-12-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/560201731
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/560201731
---
# Data science scripts

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/560201731  

## Content

On `opencpu.teqplay.nl` we have a collection of data science scripts written using R studio. Cron jobs are setup running them on a daily, weekly and/or monthly schedule. They rely on data from the PortReporter and Platform mongo databases (i.e., they do not use the API). Because of the legacy nature of these scripts, and because we had to migrate the databases they are connecting to, it has been decided to create a backwards-compatible database server specifically for these scripts, `opencpu-mongodb-compat`.

This server contains an `aiscom` and a `portReporter` database, to which the data science scripts have access. In these databases, only the collections to which the scripts need to have access are synchronized every night, *before* the scripts themselves are executed. This synchronization mechanism is initiated on `backend.teqplay.nl`, because it needs to have access to the `aiscom` database on that server. This script also connects to the MongoDb server in the `portcall` namespace to copy over the relevant collections from the `portreporter` database.