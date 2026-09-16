---
id: github:teqplay/portreporter-backend:issue:1227
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1227
title: Feat/Prp-1552/Invoice Summarized Search Endpoint
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1227
labels: []
explicit_links:
- jira:PRP-1552
---
# Issue #1227: Feat/Prp-1552/Invoice Summarized Search Endpoint

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1227  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4d5d800af9d1...d7f81fe6fde7](https://github.com/teqplay/portreporter-backend/compare/4d5d800af9d1...d7f81fe6fde7)
**Merge commit:** [d7f81fe6fde7](https://github.com/teqplay/portreporter-backend/commit/d7f81fe6fde7)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Michel Wilson, Wouter Naloop, Darius Wattimena, Gavin den Hollander
**Approvers:** Michel Wilson
**Source Branch:** [feat/PRP-1552/invoice_summarized_search_endpoint](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1552/invoice_summarized_search_endpoint)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-03-02T10:50:07.299770+00:00
**Status:** MERGED

1. [PRP-1552](https://teqplaybv.atlassian.net/browse/PRP-1552) : Including sorting options.
2. Removing deprecated methods:
    * \[GET\]/v1/invoices
    * \[GET\]/v1/invoices/\{companyId\}
    
3.  Addition of the endpoint \[GET\]/v1/invoices to retrieve the same results as /v1/invoices/search, but including the totals.
4. Marking as deprecated the endpoint \[GET\]/v1/invoices/search until FE uses the new added endpoint.
5. Authorization logic is moved to the data layer when querying a list of invoices \(canRead\(\) method\). This way pagination is not affected and totals are correctly calculated.


[PRP-1552]: https://teqplaybv.atlassian.net/browse/PRP-1552?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
