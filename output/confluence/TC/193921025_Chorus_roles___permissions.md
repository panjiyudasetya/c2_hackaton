---
id: confluence:193921025
source: confluence
type: page
space: TC
title: Chorus roles & permissions
author: Leon Joosse (Unlicensed)
date: '2023-07-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/193921025
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/193921025
---
# Chorus roles & permissions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/193921025  

## Content

17

# High level overview

This document describes the authorization in Chorus.

Chorus uses a Role Based Access Control (RBAC) system, where a user acquires permissions through an assigned role.

A permission is usually accompanied with business logic. For example, when a user has permission `NOMINATION_READ`, he should not be able to read all nomination of all companies. The business logic of `NOMINATION_READ` therefore ensures the user can only read nominations of his company (or corporation).

## User roles

A user is part of a vendor or a customer company. The user has a vendor role when part of a vendor company, or a customer role when part of a customer company. Vendor and customer roles cannot be mixed.

Chorus allows vendor companies to be grouped in a corporation.

### Normal roles

Vendor roles:

* Scheduler (planner/office type of user)
* Bunker captain
* Back office

Customer roles:

* Customer (planner/office type of user)
* Receiving captain

### Admin roles

Adjacent to the normal role, a user can be assigned an admin role.

* System admin (to manage companies, users)
* Corporate admin (to manage companies in the corporation)
* Vendor admin (to manage its own vendor company, and its customers)
* Customer admin (to manage its own customer company)

## Permissions and API endpoints

All endpoints are secured by permission checks. The system checks whether the user has the given permission and whether any additional business logic allows the user to call the endpoint.

Depending on the type of data, certain endpoints filter data to limit what the user is allowed to see, other endpoints deny access with a `403 Forbidden`.

# Authorization details

This section describes all object types in the back-end API, with its permissions per role, along with business logic per permission.

### Rules of thumb

When reasoning about authorization, we follow these rules of thumb:

1. Only vendor users can be part of a corporation
2. A user has either *customer* or *vendor* roles
3. Most of the time, a user can view things in his corporation, but can only create/update/delete things linked to his company (`user.company`)
4. A bunker/receiving captain can only read/write things when their vessel is linked to it
5. A back office user can only read things
6. Access to a nomination grants access to its documentation (IAPH, EBDN, SOF, etc) and PDFs, at least for viewing.

### How to read the tables

The first table defines the roles + permissions matrix. Each cell refers to `read`, `write` or `no`.

The second table defines the conditions of the business logic on the `read` / `write` statements.

## Types

### 1. Companies

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | read | read |
| **CREATE** | write | write | no | no | no | no | no | no | no |
| **UPDATE** | write | write | write | write | no | no | write | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | * Own company * Any companies in user’s corporation * Any company of type `CUSTOMER` | | | | | * Own company * All vendor companies | | |
| **WRITE** | No restrictions | * Own company * Companies in user’s corporation AND `company.type = VENDOR` * Customer companies of any of the vendor companies in the corporation | * Own company * Customer companies | * Own company * Customer companies where `user.company = company.vendorCompany` | no | no | Own company | no | no |

### 2. Contracts

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | read | read |
| **CREATE** | write | write | write | no | no | no | no | no | no |
| **UPDATE** | write | write | write | no | no | no | no | no | no |
| **DELETE** | write | write | write | no | no | no | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | `contract.vendorCompany` in user’s corporation companies | | | | | no | `contract.company` is user’s company | |
| **WRITE** | No restrictions | `contract` `.vendorCompany`  in user’s corporation companies | `contract` `.vendorCompany`  is user’s company | no | no | no | no | no | no |

### 3. Documents

To prevent confusion, a document consists of:

* a database entry for the metadata
* the document contents, stored in S3

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | read | read | read | read | read | read | read | read |
| **DOWNLOAD** | read | read | read | read | read | read | read | read | read |
| **CREATE / UPLOAD** | no | no | no | write | write | no | no | write | write |
| **UPDATE** | no | no | no | write | write | no | no | write | write |
| **DELETE** | write | write | write | write | write | no | write | write | write |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | `document.type` is not `ebdn_spreadsheet` or `voyage_orders` | | | | | | * `document.company = user.company` * `document.type` is not `ebdn_spreadsheet` or `voyage_orders` | | |
| **WRITE** | No restrictions | No restrictions | No restrictions | Only if user uploaded the document | | | | | |

### 4. Nominations

Nominations can be viewed in different ways:

* As a customer (customer roles, when user is in the same company)
* As a vendor/supplier (vendor roles, when user is in the same company or corporation)
* As a delegated supplier

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | Governed by non-admin role | read | read |
| **CREATE** | write | write | no | no | write | no |
| **UPDATE** | write | write | write | no | write | write |
| **ACCEPT** | write | write | no | no | write | no |
| **REJECT** | write | write | no | no | write | no |
| **COMPLETE** | write | write | no | no | no | no |
| **CANCEL** | write | write | no | no | write | no |
| **DELEGATE** | write | write | no | no | no | no |
| **ACT\_ON\_BEHALF** | write | write | no | no | no | no |

Checks for table below:

is customer: nomination.customerCompany = user.company
is vendor: nomination.vendorCompany = user.company
is corp(oration) vendor: nomination.vendorCompany is in users corporation.companies
is supplier: nomination.supplier = user.company

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Any of:   * is vendor * is corp vendor * is supplier | | | `nom.bunkership` = `user.bunkership` | Any of:   * is vendor * is corp vendor * is supplier | Governed by non-admin role | is customer | `nom.recvship` = `user.recvship` |
| **WRITE** | No restrictions | Any of:   * is vendor * is corp vendor * is supplier | Any of:   * is vendor * is supplier | Any of:   * is vendor * is supplier | `nom.bunkership` = `user.bunkership` | no | is customer |

### 5. IAPH

An IAPH object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | no | read | read |
| **READ\_** **DOCUMENT** | read | read | read | read | no | read | read |
| **CREATE** | write | no | write | no | no | no | no |
| **UPDATE** | write | no | write | no | no | no | write |
| **GENERATE\_** **DOCUMENT** | write | no | write | no | no | no | no |
| **INITIATE\_** **SIGNING** | write | no | write | no | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Same as `nomination → read` | | | | Same as `nomination → read` | no | Same as `nomination → read` | |
| **WRITE** | No restrictions | no | no | no | Same as `nomination → write` | no | no | no | Same as `nomination → write` |

### 6. EBDN

An ebdn object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | Governed by non-admin role | no | no |
| **READ\_** **DOCUMENT** | read | read | read | read | read | read |
| **CREATE** | write | write | write | no | no | no |
| **UPDATE** | write | write | write | no | no | no |
| **GENERATE\_** **DOCUMENT** | write | write | write | no | no | no |
| **INITIATE\_** **SIGNING** | write | write | write | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Same as `nomination → read` | | | | Same as `nomination → read` | no | Same as `nomination → read` | |
| **WRITE** | No restrictions | no | no | Same as `nomination → write` | | no | no | no | no |

### 7. SOF

A statement of facts (SOF) object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | Governed by non-admin role | no | no |
| **READ\_** **DOCUMENT** | read | read | read | read | read | read |
| **CREATE** | write | write | write | no | no | no |
| **UPDATE** | write | write | write | no | no | no |
| **GENERATE\_** **DOCUMENT** | write | write | write | no | no | no |
| **INITIATE\_** **SIGNING** | write | write | write | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | Same as `nomination → read` | | | | | no | Same as `nomination → read` | |
| **WRITE** | No restrictions | no | no | Same as `nomination → write` | | no | no | no | no |

### 8. Bunkership

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | no | read | read | read | no | read | read |
| **CREATE** | write | write | write | no | no | no | no | no | no |
| **UPDATE** | write | write | write | no | no | no | no | no | no |
| **EDIT\_LNG\_SPEC** | write | no | no | write | write | no | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | no | no | `ship.company` is in users corporation companies | | | no | No restrictions | |
| **WRITE** | No restrictions | `ship.company` in users corporation companies | `ship.company` = `user.company` | `ship` = `user.bunkership` | | no | no | no | no |

### 9. Receiving ship

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | no | no | read | read | read | no | read | read |
| **CREATE** | write | write | write | no | no | no | no | no | no |
| **UPDATE** | write | write | write | no | no | no | no | no | no |
| **EDIT\_LNG\_SPEC** | write | no | no | write | write | no | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions | no | no | `ship.company` is in users corporation companies | | | no | No restrictions | |
| **WRITE** | No restrictions | `ship.company` in users corporation companies | `ship.company` = `user.company` | `ship` = `user.receivingship` | | no | no | no | no |

### 10. Master’s Requisition Form (MRF)

An MRF object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | Governed by non-admin role | read | read |
| **READ\_DOCUMENT** | read | read | read | read | read | read |
| **GENERATE\_** **DOCUMENT** | write | no | no | no | no | write |
| **CREATE / UPDATE** | write | no | no | no | no | write |
| **INITIATE\_SIGNING** | write | no | no | no | no | write |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions |  | | Same as `nomination -> read` | | | | | |
| **WRITE** | No restrictions |  |  |  |  |  | Same as  `nomination -> read` |

### 11. Notice Of Readiness (NOR)

A NOR object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GENERATE\_** **DOCUMENT** | write | Governed by non-admin role | | no | write | no | Governed by non-admin role | no | write |
| **INITIATE\_SIGNING** | write | no | write | no | no | write |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **WRITE** | No restrictions |  |  |  | Same as  `nomination -> write` |  |  |  | Same as  `nomination -> write` |

### 12. Position Report

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | Governed by non-admin role | no | no |
| **CREATE** | read | no | write | no | no | no |
| **UPDATE** | write | no | no | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions |  | | Same as `nomination -> read` | | |  |  |  |
| **WRITE** | No restrictions |  | Same as  `nomination -> write` |  |  |  |  |

### 13. Quality Report

A Quality Report object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | read | Governed by non-admin role | | read | read | read | Governed by non-admin role | no | no |
| **CREATE** | read | write | write | no | no | no |
| **UPDATE** | write | no | no | no | no | no |
| **READ\_DOCUMENT** | read |  |  | read | read | read | read | read |
| **GENERATE\_** **DOCUMENT** |  |  |  | write | write | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions |  | | Same as `nomination -> read` | | |  |  |  |
| **WRITE** | No restrictions | Same as `nomination -> read` | | |  |  |  |

### 14. Delivery Plan

A NOR object / document is attached to a nomination. Access is therefore checked through the nomination.

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | write | Governed by non-admin role | | read | read | read | Governed by non-admin role | no | no |
| **CREATE** | write | write | no | no | no | no |

|  | **System admin** | **Corporate admin** | **Vendor admin** | **Scheduler** | **Bunker captain** | **Back office** | **Customer admin** | **Customer** | **Receiving captain** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **READ** | No restrictions |  |  | When allowed to view both given:   * customer company * vendor company | | |  |  |  |
| **WRITE** | No restrictions |  |  | `user.company = plan.vendor`  and  `nomination -> read` for all nominations in the plan |  |  |  |  |  |

.