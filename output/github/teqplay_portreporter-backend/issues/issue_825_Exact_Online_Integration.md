---
id: github:teqplay/portreporter-backend:issue:825
source: github
type: issue
repo: teqplay/portreporter-backend
number: 825
title: Exact Online Integration
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/825
labels: []
explicit_links: []
---
# Issue #825: Exact Online Integration

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/825  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d5cbd71f08fe...c30ae611ec80](https://github.com/teqplay/portreporter-backend/compare/d5cbd71f08fe...c30ae611ec80)
**Merge commit:** [c30ae611ec80](https://github.com/teqplay/portreporter-backend/commit/c30ae611ec80)
**Author:** Former user
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [exact-integration](https://github.com/teqplay/portreporter-backend/tree/exact-integration)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2020-12-04T11:46:40.607501+00:00
**Status:** MERGED

This PR contains the Exact integration, Slack messaging via a webhook and a new DB collection for saving certain objects via keys \(currently only used for the Exact access and refresh tokens\). 

Exact uses a login mechanism that needs a user for authentication. To make this as easy to live with as possible the redirection mechanism has also been implemented in the backend. \(you need to run this at least at the start\)  
`GET <baseUrl>/exact/login` => you get redirected to the Exact Online login portal  
`GET <baseUrl>/exact/oauth?code=…` => Exact Online redirects here with the needed authorization code, the backend then authenticates against their API and redirects you to the PortReporter frontend to confirm it was successful, or you’ll see an error response.

When an invoice needs to be sent to Exact it is added to a queue, this queue contains all the invoices that need to be sent to them. This queue mostly makes sure the requests are correctly rate limited, but also takes care of using and renewing access tokens with refresh tokens.

The process of sending an invoice to Exact has different phases, all of which can fail at any point and can easily be resumed later:

* Initialize => checks if the required values in the invoice and company are set \(if not the check fails and the invoice/company needs to be updated, then the `POST <baseUrl>/exact/update/{id}` can be called to manually trigger this process again\)
* Get the general ledger account => a company needs a certain general ledger account \(grootboekrekening\), so for the company the id of this ledger is fetched from Exact
* Get or create account => first we check if the company already exists, if not it gets created
* Create sales entry => the sales entry/invoice itself gets added
* Create document => the document gets created, if a pdf attachment has been given
* Add document to sales entry => the document gets manually linked to the sales entry
* Create document attachment => the document attachment itself gets added
* Finished => this state does nothing, it only indicates the process has finished

After logging in, the process of sending invoices to Exact is automatically resumed but it can also be done manually with the following endpoint:  
`POST <baseUrl>/exact/restart` =>this manually restarts the Exact invoicing process

There are also some ‘miscellaneous’ endpoints:  
`GET <baseUrl>/exact/list/unfinished` => for retrieving all unfinished processes  
`GET <baseUrl>/exact/invoice/{referenceNumber}` => get the process by an invoice reference number  
`GET <baseUrl>/exact/list/company/{companyId}` => gets the processes for a certain company

**application.properties changes:**

```
externalConnection.exact.baseUrl=https://start.exactonline.nl/api/
externalConnection.exact.clientId=...
externalConnection.exact.clientSecret=...
externalConnection.exact.redirectUri=https://backendportreporterdev.teqplay.nl/exact/oauth
externalConnection.exact.maxRequestsPerMinute=300

internalConnection.backendBaseUrl=https://backendportreporterdev.teqplay.nl

slack.webhookUrl=...
```

**frontend changes:**  
the company model has changed, these fields are added:  
`address.countryCode` => country code for the company \(required for Exact\)  
`generalLedgerAccount` => on which general ledger account to place invoices for a given company \(required for Exact\)  
These fields must also be added to the frontend.

