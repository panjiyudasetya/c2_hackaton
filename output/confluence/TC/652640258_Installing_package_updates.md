---
id: confluence:652640258
source: confluence
type: page
space: TC
title: Installing package updates
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652640258
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652640258
---
# Installing package updates

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652640258  

## Content

To install package updates on a Linux machine, run the following command:

sudo aptitude dist-upgrade

Check the list of suggested actions, in particular, pay attention to the packages that will be removed. If large numbers of packages are to be removed, don't press yes without understanding why `aptitude` thinks that this is needed, and knowing that this will not cause any problems.

When updating some packages, there might be configuration file conflicts. This happens when a configuration file is locally modified, and the package provides a new version. In almost all cases, you have to keep the existing configuration file (don't install the package maintainer version). If unsure, you can always print a diff between the two versions.

After doing an update, use the `checkrestart` command to see which services need to be restarted to make use of the new files. If a kernel has been upgraded, or the libc package, the system always needs to be restarted to make use of the new files.

---

A useful script for running a command on all backend servers:

#!/bin/bash
servers="backenddev backendprontodev backendnei backend backendglobal backendpronto aisdata"
for server in $servers; do
echo "==== $server ===="
ssh -t $server $\*
echo "============"
done

Save this as (for example) `~/bin/all-servers.sh`. To install updates on all servers, you can now run `all-servers.sh sudo aptitude dist-upgrade`.