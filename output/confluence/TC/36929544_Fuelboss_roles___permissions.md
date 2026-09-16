---
id: confluence:36929544
source: confluence
type: page
space: TC
title: Fuelboss roles & permissions
author: Leon Joosse (Unlicensed)
date: '2023-07-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/36929544
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/36929544
---
# Fuelboss roles & permissions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/36929544  

## Content

| **Some items are marked yellow** |
| --- |
| That means LeonJ thinks that the permissions is incorrect / not secure enough.  These items must be re-evaluated. |

17

# Intro

This document describes the layers of authorization in bunkerplanner. It gives an outline of all layers, then goes into full detail for every object type.

# Layers of authorization

The application has multiple layers to allow or deny access to data for a given user:

* Roles with permissions
* Business logic (e.g. is `user.company` equal to `object.company`)
* REST API *scrubbers*: some fields are hidden for given users (e.g. `price` or `contract` fields are hidden for captains)

## Roles with permissions

A user has a list of roles (at least 1 role). A role maps to a list of permissions. These checks are implemented in the back-end in the `PermissionEvaluatorImpl`.

Every API endpoint defines a set of permissions. The user must have a role that includes this permission. The system will return an error (`403 Forbidden`) if the user does not have the sufficient permission.

Some endpoints only require the user to be logged in (instead of a permission, the endpoint defines `IS_AUTHENTICATED_FULLY`).

**Example**: let’s say we have a user with role `SCHEDULER`. Role `SCHEDULER` has permission `NOMINATION_READ`. Then there’s endpoint `getNominations()`. This endpoint requires permission `NOMINATION_READ`. The user is then allowed by the system to call `getNominations()`, because his role is `SCHEDULER`, which satisfies the `NOMINATION_READ` permission.

## Business logic

This is more complex logic and is not captured in the roles and permissions. Let’s explain this with an example:

There is a user with role `SCHEDULER`, having permission `NOMINATION_READ`. That gives the user the possibility to read ***ALL*** nominations in the system. That is not desired, as he can also read nominations of other companies. So the business logic limits the user to only read nominations.

This layer is not always fully separate in the back-end implementation. For most API endpoints that include an id in the path, the `PermissionEvaluator` already validates if the user has access to the given object.

## Scrubbing

Scrubbing means not returning certain properties. This is usually based on the user role. For example on nominations: schedulers (office people) usually handle negotiations, captains (operational people) usually have nothing to do with price or contract information.

**Example:** let’s say we have the endpoint `getNominations()`. Calling this as a `SCHEDULER`, the endpoint will return all price and contract information. Calling this as a `CAPTAIN`, the endpoint does not include the price and contract information.

# Authorization per type

## Intro

### Types

1. Management

   1. Users
   2. Fleets
   3. Locations
2. Companies
3. Contracts
4. Documents
5. Nominations
6. IAPH
7. EBDN
8. SOF
9. Bunker ship
10. Receiving ship
11. Pipeline
12. Spot events
13. Third party contacts

These permissions are not documented yet, so not included with a table below:

1. Locations
2. Settings

### General rules

To make it easier to reason about things:

1. A user has either *customer* or *vendor* roles
2. Usually, a vendor can view most customer objects, such as listing all customers, but is not allowed to view other vendors. Same goes for customers but then towards vendors.
3. A bunker/receiving captain can only read/write things when their vessel is linked to it. In addition, a *scheduler* *captain* can plan events for his/her vessel.
4. A terminal operator can only read/write things when their pipeline is linked to it
5. A back office user can only read things
6. Price/contract type of fields are hidden for users with an operational role (bunker captain, terminal operator)

### Admin roles

A user always needs a non-admin role. An adjacent admin role can be set if needed. Note that customer/vendor roles can not be mixed.

### How to read the tables

The first table defines the roles + permissions matrix. Each cell refers to `read`, `write` or `no`.

The second table defines the conditions of the business logic on the `read` / `write` statements.

Yellow labeled cells should be re-evaluated by the team.

## 1. Management

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **USERS** | Not implemented yet / only in use by the front-end | | | | | | | | | | |
| **CUSTOMER\_** **USERS** |
| **VENDOR\_USERS** |
| **COMPANY\_FLEET** |
| **BUNKERSHIPS** |
| **LOCATIONS** |

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | Not implemented yet / only in use by the front-end | | | | | | | | | | |
| **WRITE** |

## 2. Companies

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | read | read | read | read |
| **CREATE** | write | no | no | no | no | no | no | no | no | no | no |
| **UPDATE** | write | write | no | no | no | no | no | write | no | no | no |

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions |  |  |  |  |  |  | * Own company * All vendor companies | | | |
| **WRITE** | No restrictions | Own company | no | no | no | no | no | Own company | * Own company * But should be only CUSTOMER\_ ADMIN??? | no | |

## 3. Contracts

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | no | read | read | read |
| **CREATE** | write | write | no | no | no | no | no | no | no | no | no |
| **UPDATE** | write | write | no | no | no | no | no | no | no | no | no |
| **DELETE** | write | write | no | no | no | no | no | no | no | no | no |

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ vendor** | No restrictions |  |  |  |  |  |  | no | `contract.company` is user’s company | | |
| **WRITE** | No restrictions | `contract` `.vendorCompany`  is user’s company | no | no | no | no | no | no | no | no | no |

## 4. Documents

To prevent confusion, a document consists of:

* a database entry for the metadata
* the document contents, stored in S3

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | read | read | read | read |
| **DOWNLOAD** | read | read | read | read | read | read | read | read | read | read | read |
| **CREATE** | no | no | write | write | write | no | no | no | write | write | write |
| **UPDATE** | no | no | write | write | write | no | no | no | write | write | write |
| **DELETE** (for everyone?!) | write | write | write | write | write | write | write | write | write | write | write |

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions  This gives access to **all** documents of **all** companies (as long as you know the document id)?! | | | | | | | * `document.company` is user’s company * `document.type` is not `ebdn_spreadsheet` or `voyage_orders` | | | |
| **WRITE** | No restrictions  This gives access to **all** documents of **all** companies (as long as you know the document id)?! | | | | | | | * `document.company` is user’s company * `document.type` is not `ebdn_spreadsheet` or `voyage_orders` | | | |

## 5. Nominations

Nominations can be viewed in a lot of ways:

* As a customer (customer roles, when user is in the same company)
* As a vendor/supplier
* As a delegated supplier
* As ship owner / charterer (customer or vendor roles, when user is not the customer/vendor company)

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | read | read | read | read | no | read | read | read |
| **CREATE** | write | no | write | no | write | no | no | no | write | no | write |
| **UPDATE** | write | no | write | write | write | write | no | no | write | write | write |
| **ACCEPT** | write | no | write | no | write | no | no | no | write | no | write |
| **REJECT** | write | no | write | no | write | no | no | no | write | no | write |
| **COMPLETE** | write | no | write | no | write | no | no | no | no | no | no |
| **CANCEL** | write | no | write | no | write | no | no | no | write | no | write |
| **DELEGATE** | write | no | write | no | no | no | no | no | no | no | no |
| **ACT\_ON\_BEHALF** | write | no | write | no | write | no | no | no | no | no | no |

Checks for table below:

is customer: nomination.customerCompany = user.company
is vendor: nomination.vendorCompany = user.company
is supplier: nomination.supplier = user.company
is charterer: nomination.bunkerShip.company = user.company OR
nomination.receivingShip.company = user.company

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Any of:   * is vendor * is charterer * is supplier | | `nom.bunkership` = `user.bunkership` | `nom.bunkership` = `user.bunkership`  Or one of   * is vendor * is charterer * is supplier | `nom.pipeline`= `user.pipeline` | Any of:   * is vendor * is charterer * is supplier | no | Any of:   * is customer * is charterer | `nom.recvship` = `user.recvship` | |
| **WRITE** | No restrictions | Any of:   * is vendor * is supplier | Any of:   * is vendor * is supplier | `nom.bunkership` = `user.bunkership` | `nom.bunkership` = `user.bunkership` | `nom.pipeline` = `user.pipeline` | no | no | Any of:   * is customer * is charterer |

## 6. IAPH

An IAPH object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | read | read | no | read | no | read | read | read |
| **READ\_** **DOCUMENT** | read | no | read | read | read | no | read | no | read | read | read |
| **CREATE** | write | no | no | write | write | no | no | no | no | no | no |
| **UPDATE** | write | no | no | write | write | no | no | no | no | write | write |
| **GENERATE\_** **DOCUMENT** | write | no | no | write | write | no | no | no | no | no | no |
| **INITIATE\_** **SIGNING** | write | no | no | write | write | no | no | no | no | no | no |

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Same as `nomination → read` | | | | no | Same as `nomination → read` | no | Same as `nomination → read` | | |
| **WRITE** | No restrictions | no | no | Same as `nomination → write` | | no | no | no | no | Same as `nomination → write` | |

## 7. EBDN

An ebdn object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | read | read | read | read | no | no | no | no |
| **READ\_** **DOCUMENT** | read | no | read | read | read | read | read | no | read | read | read |
| **CREATE** | write | no | write | write | write | write | no | no | no | no | no |
| **UPDATE** | write | no | write | write | write | write | no | no | no | no | no |
| **GENERATE\_** **DOCUMENT** | write | no | write | write | write | write | no | no | no | no | no |
| **INITIATE\_** **SIGNING** | write | no | write | write | write | write | no | no | no | no | no |

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Same as `nomination → read` | | | | | Same as `nomination → read` | no | Same as `nomination → read` | | |
| **WRITE** | No restrictions | no | Same as `nomination → write` | | | | no | no | no | no | no |

## 8. SOF

A statement of facts (SOF) object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | read | read | read | read | no | no | no | no |
| **READ\_** **DOCUMENT** | read | no | read | read | read | read | read | no | read | read | read |
| **CREATE** | write | no | write | write | write | write | no | no | no | no | no |
| **UPDATE** | write | no | write | write | write | write | no | no | no | no | no |
| **GENERATE\_** **DOCUMENT** | write | no | write | write | write | write | no | no | no | no | no |
| **INITIATE\_** **SIGNING** | write | no | write | write | write | write | no | no | no | no | no |

.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Same as `nomination → read` | | | | | Same as `nomination → read` | no | Same as `nomination → read` | | |
| **WRITE** | No restrictions | no | Same as `nomination → write` | | | | no | no | no | no | no |

## 9. Bunkership

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | read | read | read | read | no | read | read | read |
| **CREATE** | write | write | no | no | no | no | no | no | no | no | no |
| **UPDATE** | write | write | no | no | no | no | no | no | no | no | no |
| **EDIT\_LNG\_SPEC** | write | no | write | write | write | no | no | no | no | no | no |

.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | no | * `user.company = ship.company` * `user.company in ship.charterers` | | | | | no | No restrictions | | |
| **WRITE** | No restrictions | `ship.company` = `user.company` | `ship` = `user.bunkership` | | | no | no | no | no | no | no |

## 10. Receiving ship

**These permissions are not in the back-end yet! It instead relies now on your role + business logic only.**

| **Not implemented yet!** | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | read | read | read | read | no | read | read | read |
| **CREATE** | write | write | no | no | no | no | no | no | no | no | no |
| **UPDATE** | write | write | no | no | no | no | no | no | no | no | no |
| **EDIT\_LNG\_SPEC** | write | no | write | write | write | no | no | no | no | no | no |

.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | no | * `user.company` = `ship.company` * `user.company` in `ship.charterers` | | | | | no | No restrictions | | |
| **WRITE** | No restrictions | `ship.company` = `user.company` | `ship` = `user.receivingship` | | | no | no | no | no | no | no |

## 11. Pipeline

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | read | read | read | read |
| **CREATE** | write | write | no | no | no | no | no | no | no | no | no |
| **UPDATE** | write | write | no | no | no | write | no | no | no | no | no |
| **EDIT\_LNG\_SPEC** | write | no | write | no | no | write | no | no | no | no | no |

.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | no | `user.company` = `pipeline.company` | | | | | no | No restrictions | | |
| **WRITE** | No restrictions | `pipeline.company`= `user.company` | `pipeline.company`= `user.company` | no | no | `pipeline`= `user.pipeline` | no | no | no | no | no |

## 12. Spot events (request for quotation)

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | read | no | no | no | read | no | read | no | no |
| **ENQUIRY\_CREATE** | write | no | no | no | no | no | no | no | write | no | no |
| **UPDATE** | write | no | write | no | no | no | no | no | write | no | no |
| **ACCEPT** | write | no | write | no | no | no | no | no | write | no | no |
| **REJECT** | write | no | write | no | no | no | no | no | write | no | no |
| **CANCEL** | write | no | write | no | no | no | no | no | write | no | no |
| **FINALISE** | write | no | no | no | no | no | no | no | write | no | no |
| **ADD\_CONTRACT** | write | no | write | no | no | no | no | no | no | no | no |

.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | no | Permission given, but nowhere used | no | no | no | Read is allowed, but nowhere used? | no | `enquiry.company` = `user.company` | no | no |
| **WRITE** | No restrictions | no | Permission given, but nowhere used | no | no | no | no | no | `enquiry.company` = `user.company` | no | no |

## 13. Third party contacts

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LIST** | read | read | read | read | read | read | read | read | read | read | read |
| **READ** | read | read | read | read | read | read | read | read | read | read | read |
| **ADD** | write | write | write | write | write | write | write | write | write | write | write |
| **UPDATE** | write | write | no | no | no | no | no | write | no | no | no |

.

|  | **System admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Scheduler captain** | **Terminal operator** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** | **RV Scheduler Captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | | | | | | | | | | |
| **WRITE** | No restrictions | `contact.company` = `user.company` | no | no | no | no | no | no | `contact.company` = `user.company` | no | no |

.