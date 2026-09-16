---
id: confluence:666730512
source: confluence
type: page
space: TC
title: Initial researching notes
author: Joaquin Marquez Bugella
date: '2025-03-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/666730512
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/666730512
---
# Initial researching notes

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/666730512  

## Content

26falsenonelisttrue

# Description

# Notes

Interaction of the Sedna integration

* The User interface <https://teqplaysandbox.sednanetwork.com/> displays a sidebar on the right like this:

|  |
| --- |
|  |
| Sedna inbox user interface |

* When clicking on the app (right side list) Sedna backend invokes a [POST] call to the provided integration url (<https://sednaintegration.dev.teqplay.com>). The Post body follows this json schemas:

  + <https://app.sednanetwork.com/mikit/2020-07-07/definitions.schema.json>
  + [app.sednanetwork.com/mikit/2020-07-07/request.schema.json](https://app.sednanetwork.com/mikit/2020-07-07/request.schema.json)
  + [app.sednanetwork.com/mikit/2020-07-07/response.schema.json](https://app.sednanetwork.com/mikit/2020-07-07/response.schema.json)
* There are two type of post calls: READ and COMPOSE.

  + READ is for when the POST call is triggered when opening(reading) an email
  + COMPOSE is for when the POST call is triggered when composing an email (new or saved draft)

## Interaction diagrams

Add a diagram of the interaction between the two systems

Add a diagram of sednaintegration.dev.teqplay.com

## Teqplay Sedna Integration component

* models (request, response, templates)
* identification of template
* Teqplay placeholders to compose reponse data

## How to create a Sedna application

Go to this [link](https://24ced5c9-0e3f-45c5-9601-977794509949.trayapp.io/) and fill the data.

## How to delete a Sedna application

There’s no specific web interface for this. It must be done via Postman to this url:

`[DELETE] https://teqplaysandbox.sednanetwork.com/platform/application-configuration/application_configuration_id`

The application\_configuration\_id is obtained by calling:

`[GET] https://teqplaysandbox.sednanetwork.com/platform/application`

Note that you’d need basic authorization with the credentials in the bitwarden entry “Teqplay Sandbox Sedna Network (api credentials)”

# Links and bibliography

* Inbox sandbox: <https://teqplaysandbox.sednanetwork.com/>
* <https://developers.sedna.com/>
* <https://sedna.com/connected-apps>
* <https://github.com/sednasystems/sedna-mikit-sample-node/blob/master/src/sedna.js>
* Main Jira tasks:

  + PRP-25475c406517-69e9-3c5d-b831-d2bed7d442a4System Jira
  + PRP-25775c406517-69e9-3c5d-b831-d2bed7d442a4System Jira
* Github repo: [teqplay/sednaintegration-backend](https://github.com/teqplay/sednaintegration-backend)
* Sedna platform swagger:

  + <https://sed.sednanetwork.com/platform/swagger>
  + <https://teqplaysandbox.sednanetwork.com/platform/swagger>