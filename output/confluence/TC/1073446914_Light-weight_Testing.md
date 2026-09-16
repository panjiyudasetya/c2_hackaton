---
id: confluence:1073446914
source: confluence
type: page
space: TC
title: Light-weight Testing
author: Daan Spikker (Unlicensed)
date: '2026-01-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1073446914
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1073446914
---
# Light-weight Testing

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1073446914  

## Content

Testing in Chorus nowadays consists of light-weight testing.

Given the changes are mostly vulnerabilities - library updating - the Chorus testing consists of going over the used features. In this doc we describe shortly how that could be done.

* Authentication
* Navigating the tool itself, all pages are shown
* Creating, editing, approving a nomination (on behalf) and have it shown by the users active (bunkercaptains)
* Creating an event (i.e. Loading event) and amending it through the detailed timeline view.
* Delegating a nomination
* Add documents to nomination and have it available for all connected users (planner and bunkercaptain)
* Bunkercaptains position report is working (able to create new records to positino report and share it)
* Receiving notifications (emails) after update.
* Customers: Receiving Captain and Bunker Captain are able to see the nominations and follow the negotiation flow.

* Creating, editing, approving a nomination / Add documents to nomination / Creating and managing Events (make sure all fields are working, all contracts are there and can be assigned and the approval workflow is working well). Also check if timeline dispalys correctly the settings of the nomination.

<https://drive.google.com/file/d/13dOZYI0fXQCAeQW2PB7Wtx4FS3i7pDBt/view?usp=drive_link>

* Receive mails  
  <https://drive.google.com/file/d/1zkzlx4WZpJzNhzQ46NBS7fa6AvsaIUek/view?usp=drive_link>
* Bunkercaptain - seeing nominations, seeing activity board
* <https://drive.google.com/file/d/1FLjS82_Z3w21Q_44ikkBStLPtsME3v3B/view?usp=drive_link>

<https://drive.google.com/file/d/1Pn2g1dIpc7Pafdm64METR6c-TlP44zBM/view?usp=drive_link>

* Bunkercaptains position report is working (able to create new records to positino report and share it)
* <https://drive.google.com/file/d/1QaLS0kg9ubLUA3Ie8EiwBksXNGN1YuN9/view?usp=drive_link>
* Customers (planner) are able to view the nomination for their companies vessels on the timeline and in the nominatino search. And able to participate in negotiation.
* Customer (captain) is able to view the nomination for his vessel on the timeline and in the nomination search.

It means that we don’t test the following;

* Complicated docs (IAPH, eBDN, MRF, NOR) → it’s not used
* ADP - not used
* Contracts - seldom changed especially given they’re almost end-of-live
* Configuration - seldom change given they’re almost end-of-live
* Bulk/add edit of nominations - not used
* Sandbox - not used
* Assign nominations to contract- not used
* Action Overview - not used.