---
id: confluence:28049409
source: confluence
type: page
space: TC
title: Charterer/ship-owner read-only access  - Technical description
author: Daan Spikker (Unlicensed)
date: '2021-08-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/28049409
explicit_links: []
---
# Charterer/ship-owner read-only access  - Technical description

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/28049409  

## Content

In the current implementation, the operating party (charterer) has full access to nomination details for a ship in their fleet. It is desirable for the actual owners of the ship to also have read-only access to the nominations for the ships in their fleet, for example to be aware of planned bunker operations and to monitor fuel ~~qualities~~quantities used.

At a high level, the following functionality will be added:

* As charterer/operator it will be possible to select an owner company for each individual vessel in ~~the~~their company fleet. Per vessel, only one owner company can be selected. Any customer company in FuelBoss can be selected as owner company. In particular, it is possible that the owner company also has the same vessels in their company fleet (to purchase LNG for them whenever charterer/operator is not).
* As owner company (i.e. added in by a charterer/operator), all nominations for~~on~~ vessels where charterer/operator have added the owner company~~owned vessels~~ are available via the normal overview list etc, but they can only be viewed, not edited in any way.

* If the charterer/operator of a vessel changes, the new operator adds the vessel to their fleet as usual. Then, the owner company can be selected again, if desired.
* Currently, this functionality is only intended to be available for receiving vessels, not for bunker vessels.

Backend tasks

**Model updates (4h)**

* Add a field for the owner company id to the receiving vessel

* Updates to this field invalidate any relevant caches
* Ensure that the collection has an index on this field, and that the query to retrieve vessels per owner company is cached

**Nomination retrieval update (12h)**

When retrieving the schedule for a user, also fetch the receiving vessels for which the user’s company is the owner company, and retrieve nominations on those vessels as well. Note that the schedule collection should have an index on receiving vessel id for this. There should also be a form of caching such that the list of owned vessels for a user can be retrieved quickly.

The permission check for a nomination should also be updated to take the owner company vessel list into account: if the receiving vessel is on that list, read-only access should be granted.

Add an indication to the attributes map to indicate that a nomination is for a vessel that is not part of the own fleet and thus read-only.

Update the “action needed” flag to never be true if the nomination is read-only

Frontend tasks

**Nomination form (4h)**

Update action button logic to ensure that accept/reject/edit buttons etc are not shown if the nomination is read-only because the viewer is part of the owner company.

Optional (TBD): indicate clearly that the nomination is read-only, for a vessel not under control of the viewer

DNV tasks

**Fleet management**

For the vessel operator users, indicate in the Company fleet management page if a vessel is owned (and viewable) by another company. In the edit component, allow the operator of a vessel to select the owner company.

**Nomination overview lists**

~~Optional: f~~For the owner company users, in the nomination overview lists, lighter and italic font to be used (get specific recommendation from Heinke) ~~add an indicator~~to reflect the fact that a nomination is read-only because it is for a vessel not under control of the user viewing the list. Also note the above described need to change the “Action required” status to Pending status (if this is really complex we are open to reconsider).