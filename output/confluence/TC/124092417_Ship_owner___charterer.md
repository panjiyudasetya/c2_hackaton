---
id: confluence:124092417
source: confluence
type: page
space: TC
title: Ship owner / charterer
author: Leon Joosse (Unlicensed)
date: '2022-11-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/124092417
explicit_links: []
---
# Ship owner / charterer

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/124092417  

## Content

This document was proposed to DNV and agreed on. We added the scenarios and technical description later on.

# Extending ship owner / charterer connection for captains

Version 3, October, LeonJ

* Technical description

Version 2, July 8, Daan, Gavin, LeonJ

* Ship owner can set ‘available for chartering’ for his vessels
* Charterer links the vessel to his fleet (instead of ship owner allowing it first)

Version 1, June 24, LeonJ

* Initial version

### **Terminology**

To prevent confusion: A ship owner owns the ship and charters (rents out) it out to a *charterer*. A chartered vessel can be a bunker or receiving vessel.

### **Current situation**

Fuelboss exposes nominations to ship owners, so they can see what happens with their ship. The ship owner does not see commercial information (e.g. price) on these nominations.

The charterer creates the ship in its company and assigns the ship owner company as ‘owner’. This connection allows the shipowner to see the nominations linked to that ship. The functionality works for both bunker and receiving vessels.

## **Problem description**

The described functionality requires the captain to be moved from the shipowner to the charterer company. This is a cumbersome process and needs to be done by a system admin.

As Martin describes it:

*In the offshore industry there are many different buyers of fuel for the same vessel, and it can change on a short notice/monthly basis. This creates a problem for the onboard processes where the RV crew user role is involved (digital signing in particular, but in theory also the safety checklist). The problem is that the RV user must be attached to the Buyer company which makes the nomination, and moving a user between companies can only be done by System admins as of now. We want to avoid a solution where the users need to contact DNV to move users to fix the issue.*

*The Add Shipowner functionality is today used to loop in onshore users and keep them informed about upcoming bunker events.*

## **Proposal to improve**

This proposal discusses how a company charters a vessel in Fuelboss. We assume that the chartering is already arranged outside of Fuelboss. The chartered vessel must be visible in the charterer company fleet in order to create nominations with that vessel.

This used to work by adding the ship to every charterer company and then moving around the captain.

*The proposal is to let the vessel and captain reside within the ship owner company.* The charterer company then gets access to the charterers vessel by linking it to the charterer’s fleet. The captain gets access to the ‘chartered nominations’ because his vessel is set as the bunker/receiving vessel.

On a technical note: the vessel resides in the ship owner company, the charterer fleet has a *reference* to the chartered vessel. These references are saved in the vessel’s object.

### **Ship owner: opening vessels for chartering**

All vessels are open for chartering, there is no restriction. An (shipowner) admin can limit the charterability (visibility of the vessel) of the vessel in the company fleet screen. By default the vessels are open for chartering.

### **Charterer: link vessel to his fleet**

Looking from the charterer’s perspective: he is now able to find all charterable vessels. The charterer will see his own vessels and the chartered vessels in the  company fleet screen.. The charterer can search for a charterable vessel and link it to his own fleet. Upon linking the vessel, the charterer defines this vessel chartered by his company. Charterer can also disable the chartering in the company fleet screen. Creating a nomination can only be done when this vessel is chartered.

The current functionality, where an onshore user of the ship owner company, can view nominations of their chartered vessels, keeps working as is.

### **Captain**

The captain of the chartered vessel resides in the ship owner company. This user has access to all nominations where the chartered vessel is set as a bunker or receiving vessel.

‘Access’ in this case means viewing and editing the nomination (same as a captain can in a non-charterer scenario), access to the documentation (safety checklist, SOF and eBDN) and all documents attached to the nomination. The captain will also receive all ‘captain’ emails.

This captain does not have access to any other nominations in the charterer companies.

In case the user is a scheduler captain, then the scheduler rights only apply to the captain’s own company.

### **Captain scheduler**

The RVSC remains functional, meaning that the captain activities can be performed on the chartered out vessel. The scheduling activities (creating/editing nominations for the captain’s vessel) can only be done within his *own* company. Meaning he can’t make new nominations in the company his vessel was chartered out to.

### **Impact on Chorus**

The complexity of this proposal does not increase because of Chorus, as Chorus does not use the concept ship owner / charterer as depicted here. This functionality touches on permission to access a nomination, so we need to take care not to change functionality for Chorus here.

### **Who does what**

Teqplay implements backend, exposes endpoints

DNV does frontend, as most of these screens are already done by DNV.

# Scenarios

To keep in mind with testing

1. Ship owner admin opens a vessel for chartering
2. Ship owner admin closes a vessel for chartering
3. Ship owner admin adds a captain for a charterable vessel
4. Ship owner admin removes a captain for a chartable vessel
5. Charterer adds a chartered vessel
6. Charterer removes a chartered vessel
7. Charterer creates a nomination with a chartered vessel

   1. Captain of chartered vessel can view and update a nomination with its vessel
   2. Captain of chartered vessel can use the safety checklist / SOF / EBDN
   3. Captain of chartered vessel receives email notifications about a nomination that has the chartered vessel

## 1. Ship owner admin opens a vessel for chartering

This applies to both supplier and customers.

The ship model has a field that indicates whether the vessel is open for chartering: `charterable: Boolean`.

# Technical

Some things to keep in mind:

* The `charterable` flag is only meant to show/hide the ship to/from potential charter companies.
* A company being listed in the `ship.charterers` list is only important at the moment of **creating** the nomination. If the company is removed from the charterers list in the future, that nomination in history was still validly created as charterer!

## Differences to the previous implementation of chartering

This applies to both bunker and receiving ships. A ship is always linked to the ship owner (that is different from the previous `ownerCompanyId` solution!).

When chartering a ship, the charter gets a **link** to the ship, it is not copied into his list of ships (which was the previous solution).

Using a chartered ship now solely relies on the charter link. The ship owner has control over when and to whom the ship is chartered.

## Access rules for nominations with a chartered ship

A nomination can have a chartered bunker **and/or** receiving ship. The ship must be chartered first before it can be used in the nomination creation form. The chartered ship is then returned in the companies list of vessels using `/v1/(bunker)ship/[companyId]?includeCharteredVessels=true`.

Access rules to the nomination follow these rules:

* A captain sees nominations for his ship. So we drop the ‘ship must be from your own company’ requirement. All we require now is `ship.companyId == captain.bunkerShipId` for supplier companies or `receivingShipId` for customer companies.
* For a scheduler captain, it works the same as a captain, but he can create nominations for his ship **in his own company**.
* Any other role from the shipowner company can only **view** nominations where one of their chartered ships is being used. That boils down to: `nomination.bunkerShip.companyId == user.companyId` for supplier companies or `nomination.receivingShip.companyId == user.companyId`.   
  Note that these users can only see **non-commercial** information.

Updating the nomination when it has the chartered ship

* A captain can update parts of the nomination as with a normal nomination (e.g. ETA)
* A scheduler captain:

  + when his company is customer or supplier, he can do all scheduler captain actions and updates
  + when his company is only ship owner (so the ship is chartered for this nomination), he acts as a normal captain
* Other users can only read the nomination

## Open/close a ship for chartering

The ship owner indicates whether the ship is open for chartering, using the `charterable` flag on the ship object, using the ship’s update endpoint. Only when the flag is set to `true`, the ship can chartered by other companies.

Changing this value to `false` does not delete the list of `charterers`.

## Chartering a ship

Charters can find the ship using `/v1/ship/charterable` or `/v1/bunkership/charterable`. They can add themselves as charterer using `PUT /v1/(bunker)ship/charterers`.

The charterer stays in the list until they remove themselves OR the ship owner removes them.

Trying to charter a ship that has `charterable` set to false results into an error.

The charter entry is not removed when the `charterable` flag’s value is changed.