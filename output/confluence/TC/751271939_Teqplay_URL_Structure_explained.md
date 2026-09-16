---
id: confluence:751271939
source: confluence
type: page
space: TC
title: Teqplay URL Structure explained
author: Richard van Klaveren
date: '2025-06-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/751271939
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/751271939
---
# Teqplay URL Structure explained

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/751271939  

## Content

Within Teqplay, we currently use a few different domains to separate LIVE and DEV cluster, but also to indicate whether something is routed internally within the VPC or via external API.

In general the following rules are being applied in backend:

* \*.teqplay.nl is referring to a **LIVE** environment accessible from **outside the VPC**
* \*.dev.teqplay.com is referring to a **DEV** environment accessible from **outside the VPC**
* \*.teqplay.dev is referring to a **LIVE** environment accessible from **within the VPC**
* \*.dev.teqplay.dev is referring to a **DEV** environment accessible from **within the VPC**

in the future, the idea would be that also all External DNS entries will use teqplay.com extensions instead of [teqplay.nl](http://teqplay.nl). However, this will take a bit of time. Similar for the front-end, currently all front-ends (except for cargo-optima) is still using [teqplay.nl](http://teqplay.nl) extensions

The old structure was (only outside the VPC accessible):

* \*.teqplay.nl is referring to a LIVE environment
* \*dev.teqplay.nl referring to a DEV environment,

From a front-end perspective we are still following the old structure, but will probably migrate over to the new structure (only outside the VPC accessible).