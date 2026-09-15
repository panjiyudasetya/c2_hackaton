---
id: confluence:109838337
source: confluence
type: page
space: TC
title: Teqplay Nominations
author: Joaquin Marquez Bugella
date: '2022-05-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/109838337
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/109838337
---
# Teqplay Nominations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/109838337  

## Content

Work in progress page, please, be patient

# Introduction/context

In Port Reporter, some customers (so far Shipping Companies) notify us about the portcalls they will recognized as theirs. This help us to create subscriptions and invoices based on them.

# Nomination

A nomination is just an in-advance notification of an incoming portcall.

It basically consist of the following fields:

| **Field** | **Description** |
| --- | --- |
| Shipping Company Id | Id of the shipping company.  It needs to be linked to a shipping line. |
| Port | The shipping line It should operate in this port. |
| IMO | … of the portcall’s ship. |
| ETA | Estimated time of arrival of the ship to this port.  It’s likely to be updated when the eta approaches being more and more accurate. |
| Portcall Id | Id of the portcall that matches the nomination.  There’s a double matching mechanism between portcalls and nominations.  More details here **TBC**. |
| Invoice Id | Id of the invoice related to the portcall Id, once it’s completed.  This field is populated when the related portcall is invoiced. |

# Nomination handling

Currently, shipping companies notify us about nominations via email (**TBC**: email account where they are received), out of which, nominations can be created or updated manually or automatically.

## Manual management

Port Reporter has a section where to manage (create, update or delete) nominations: [Main menu → Nominations](https://portreporter.teqplay.nl/nominations), only accessible by Teqplay admins:

|  |
| --- |
|  |
| Access to Nomination management in Port Reporter |

## Automatic management

Automatic management of nominations is done via a internal process in which participates:

* ***Scrape Shark***, which checks on a regular basis the email account for new messages, scraping them to send potential nominations to a queue (see more details here - **TBC**)
* ***Port Reporter***, which has a module subscribed to the mentioned queue that attempts to digest scraped nominations and create or update nominations out of them.

|  |
| --- |
|  |
| Automatic nomination management |

### Issues

Sometimes, a scraped nomination doesn’t contain enough information to create a nomination or there’s an issue with it.

Then, a message is sent to the Slack channel [#nomination-scraping](https://teqplaydev.slack.com/archives/C03AV4JELQM) with the raw data received by Port Reporter and the resolved fields:

|  |
| --- |
|  |
| Example of a slack message notifying of an error in the automatic nomination management. |

Here is the list of identified cases so far:

| **Case** | **Description** | **What to do** |
| --- | --- | --- |
| Case 1 | The data received as a scraped nomination didn't match the *ScrapedNomination*'s model. | Scrape Shark has produced a nomination but it doesn’t match the expected data model.  **Please, ask** ***Scrape Shark*****’s and** ***Port Reporter*****’s responsible about it.** |
| Case 2 | The given company is not existent in *Port Reporter* or does not operate in the given port. | Scrape Shark has produced a nomination for a shipping company that wasn’t identified in Port Reporter.  **It’s likely there’s a typo.** Be it the case, please identify the correct shipping company and create the nomination manually.  Also, if this became a recurrent case, please, contact ***Scrape Shark*****’s and** ***Port Reporter*****’s responsible about it.** |
| Case 3 | The ship returned by Platform had no imo. | The returned ship from Platform had no IMO, very unlikely because the search is by that field).  **Please, ask** ***Platform*****’s and** ***Port Reporter*****’s responsible about it.** |
| Case 4 | No ship has been found in Platform by the given IMO. | Ship wasn’t found in Platform by the given IMO.  **Please, ask** ***Platform*****’s and** ***Port Reporter*****’s responsible about it.** |
| Case 5 | The identified ship (by the name) is in the company’s fleet, but had no IMO. | That’s a potential *Port Reporter*’s issue (with a wider scope). **Please, ask** ***Port Reporter*****’s responsible about it.** |
| Case 6 | The scraped nomination had no IMO and there’s no ship with the given name in the shipping company’s fleet. | **Please, ask** ***Scrape Shark*****’s and** ***Port Reporter*****’s responsible about it.** |
| Case 7 | Neither IMO nor ship name was provided in the scraped nomination. | **Please, ask** ***Scrape Shark*****’s responsible about it.** |
| Uncategorized | Unexpected error that needs to be checked technically. | **Please, ask** ***Port Reporter*****’s responsible about it.** |

### Additional notifications

Port Reporter sends an additional slack message when:

* A ship has been added to a shipping company’s fleet.
* A ship’s time-charter’s end-time has been modified.

To finish, there’s a scheduled task at 4AM that monitors the creation of nominations that sends an e-mail to ([developer@teqplay.nl](mailto:developer@teqplay.nl)) whenever less than 2 nominations were created in the last 24 hours.

# Additional info

Links for further info