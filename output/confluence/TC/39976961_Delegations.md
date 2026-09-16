---
id: confluence:39976961
source: confluence
type: page
space: TC
title: Delegations
author: Joost Dambrink (Unlicensed)
date: '2023-08-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/39976961
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/39976961
---
# Delegations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/39976961  

## Content

There is party A, B and C. A wants LNG from B, B has no shippie in that area, so delegates it to C.

* A = customer
* B = contract holding supplier
* C = executing supplier

Then there's two separate negotiations going on:

* nomination 1 between A + B
* nomination 2 between B + C

The system implements it as follows (this is what party you are to the nomination, not your `user.role`):

* For nomination 1: party A is customer and party B supplier
* For nomination 2: party B is customer and party C is supplier

The naming also a bit mixed up sometimes. We refer to: (DNV language in *italics*)

* party A: customer, *buyer*
* party B: the middle man, contract party, *contract holding party*
* party C: actual supplier, *executing supplier*

And for the nominations:

* nomination 1: origin nomination
* nomination 2: delegated nomination

Only the *contract party* (party B) can see both nominations side by side. Other parties see either the left or right nomination.  
I usually refer to party A, B and C:

**Party A** (customer type company, regular customer edit permissions apply):

* `CUSTOMER`: can see and edit the left nomination
* `RECEIVING_CAPTAIN`: can see the left nomination when `nomination.receivingVessel = user.receivingVessel`

**Party B** (vendor type company):

* `SCHEDULER` can **see and edit** left + right nomination
* `BACK_OFFICE` can **only read** left + right nomination
* other roles should not have access, as this company is purely doing negotiations, other roles should not see this nomination (relevant captains/terminal operators are always from party A or C)

**Party C** (vendor type company, regular vendor edit permissions apply):

* `SCHEDULER`, `BACK_OFFICE` can see right nomination
* `SCHEDULER_CAPTAIN`, `CAPTAIN` can see right nomination when `nomination.bunkerShip = user.bunkerShip`
* `TERMINAL_OPERATOR` can see right nomination when `nomination.pipeline = user.pipeline`
* because the executing supplier is **not** allowed to see price information between Party A & B, the **order confirmation** PDF is not visible for all party-c users. users are also not allowed to create an **order confirmation**.