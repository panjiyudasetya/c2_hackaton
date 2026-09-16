---
id: confluence:761593857
source: confluence
type: page
space: TC
title: VesselMatcher
author: Joost Laurman
date: '2025-09-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/761593857
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/761593857
---
# VesselMatcher

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/761593857  

## Content

VesselMatcher is an application facilitating vessel owners to go through all received mails with Cargo offers in order to suggest automatically the cargo’s fitting best to the fleet we’re looking cargo for.

Vesselmatcher has been co-developed with Vertom Vessel-owners team addressing the problem that 12 people searching for cargo were going daily through the same 20.000 E-mails received from Cargo owners and brokers.

The product is operationally in use and used by about 15 people at Vertom for dry bulk. Reselling to other vessel owners so far has never been successfull.

Relevant slack channels:

* #vesselmatcher

Design documentation [can be found here](https://docs.google.com/document/d/1YnXwbIL0BnOZc8763AoxQt_pcj_ZtxeZ8TvSiKiRJHg), in the [same folder there are also relevant resources like meeting minutes, mock-ups and architecture considerations](https://drive.google.com/drive/u/0/folders/1iZFYJDIQXhDMjzIpNKuz00j7Opa4LH-c). A high-level functional and technical introduction was provided, [a recording can be found here](https://www.youtube.com/watch?v=pTEIkXyLMyk).

Some short additional explanation that are good to know:

* Locations and ports in the system have been added by a colleague in the past, the system does not rely on POMA. In the import process, some location precision was lost, so some locations may be somewhat inaccurate
* Ships are added on request of Vertom, no automated process here
* Travel distances are calculated via RouteScout, and saved in the database for quick querying. In case Routescout is unavailable, a haversine calculation is used ('as the crow flies')

## Cleaning up mailboxes on the EC2 machine

Log on into the machine

In `/mnt/mail/` you can find all the mailboxes with archived mails.

Run this command inside to clean up mails older than 365 days.

wide760find /mnt/mail{cargo-list,incoming,planning,position-list} -ctime +365 -type f -delete