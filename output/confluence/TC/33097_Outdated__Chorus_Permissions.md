---
id: confluence:33097
source: confluence
type: page
space: TC
title: '[Outdated] Chorus Permissions'
author: Daan Spikker (Unlicensed)
date: '2022-12-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/33097
explicit_links: []
---
# [Outdated] Chorus Permissions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/33097  

## Content

(too add: permissions on documentation, who can start signing, who should sign what etc.)

Document focuses mainly on differences between admins in Chorus.

Full permisionmatrix can be found here:

<https://docs.google.com/spreadsheets/d/1qfSysPYZBc1PbUG9NybmDeE2Izz7IfiRRs17fuvGxIA/edit#gid=0>

Main differences between admin roles lie within the control over *assets*:

* Company assets

  + Bunker vessels (create/edit/delete)
  + Scheduler user?? (create/edit/delete)
* Customer assets

  + Customer User (create/edit/delete)
  + Vessels / Pipeline (create/edit/delete)
* Global Assets

  + Company’s (create/edit/delete)

The following ‘admin’ roles are present in either Chorus and/or Fuelboss.

* **System Admin** (Fuelboss-Only)
* **Corporate Admin** (chorus-only): used to allow an admin in one company managing another company in the same corporation
* **Admin** (buth FB and company admin in Chorus):  allows a user in a vendor company to manage users and asset.
* **Customer Admin** (**Fuelboss-only**): can view and update own company details, documents, manages users , vessels own company.

  + *proposal is to use that in the chorus version too*

Below you find the permissions matrix for corp admin, admin and cust. admin. Some additional explanation on actions:

* manage\_users: ability to add/edit users, as you'd expect i guess
* manage\_company\_fleet: ability to modify receiving vessels at the customer side i believe
* manage\_bunkerships: the same but for bunkerships at the supplier side

For **Chorus** this means we should do the following checks:

The permission matrix is deleted awaiting  documentation on permissions.

The following Role aliases are used by DNV in FuelBoss