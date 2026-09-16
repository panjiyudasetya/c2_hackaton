---
id: github:teqplay/vesselvoyage-backend:issue:263
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 263
title: Spv-2050 Sof Api Scaffolding (1/9)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/263
labels: []
explicit_links: []
---
# Issue #263: Spv-2050 Sof Api Scaffolding (1/9)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/263  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b21302512223...d70ebca66d65](https://github.com/teqplay/vesselvoyage-backend/compare/b21302512223...d70ebca66d65)
**Merge commit:** [d70ebca66d65](https://github.com/teqplay/vesselvoyage-backend/commit/d70ebca66d65)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [SPV-2050-sof-api-scaffolding](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2050-sof-api-scaffolding)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:35.721680+00:00
**Status:** MERGED

The first of several PRs to serve the ‘interpreted/explicit’ statement of facts from the vesselvoyage api. Explicit in the sense that we try to interpret the port visits, berth visits, terminal visits, etc. This SOF is supposed to replace PTO at some point. I separated the code into several PRs to keep it readable.
This first PR adds:
* Common interface for statement of facts classes served by the API, so we can use the same endpoint.   
  The finally served type is determined by the `view` parameter in the API request
* Updates the existing Port- and TerminalStatementOfFacts models to extend from the common interface
* Added components that generate this explicit SOF: model, mapper
If you have a suggestion for a better name than `ExplicitStatementOFacts`, please give them, I find it hard to come up with a proper name. We may opt for something like PtoStatementOfFacts, but that kind of loses its meaning once we replaced it.
Coming PRs will build upon this PR, so this may seem a bit empty for now :wink:

