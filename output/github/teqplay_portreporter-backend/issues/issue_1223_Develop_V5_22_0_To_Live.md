---
id: github:teqplay/portreporter-backend:issue:1223
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1223
title: Develop V5.22.0 To Live
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1223
labels: []
explicit_links: []
---
# Issue #1223: Develop V5.22.0 To Live

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1223  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [6256efd23811...4ab2fcac9f49](https://github.com/teqplay/portreporter-backend/compare/6256efd23811...4ab2fcac9f49)
**Merge commit:** [4ab2fcac9f49](https://github.com/teqplay/portreporter-backend/commit/4ab2fcac9f49)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2023-02-23T10:04:16.837978+00:00
**Status:** MERGED

* [**PRP-1249**](https://teqplaybv.atlassian.net/browse/PRP-1249) **:** move the port endpoints to the static controller, keeping the old stuff for backwards compat in the frontend.
    Approved-by: Joaquin Marquez Bugella

* [**PRP-1611**](https://teqplaybv.atlassian.net/browse/PRP-1611) **:** Extend UserProfile model with Units field.
    Approved-by: Wouter Naloop

* [**PRP-1591**](https://teqplaybv.atlassian.net/browse/PRP-1591) **:** Expose new csi endpoints in ship controller.
    Approved-by: Wouter Naloop

* [**PRP-1468**](https://teqplaybv.atlassian.net/browse/PRP-1468) **:** Extending unpaid invoices' endpoint with the parameters: searchPattern, from, to, isoWeek and port.
    Approved-by: Joost Laurman

* **fix :** removing the loading of the file version.properties: it's misleading when including skeleton properties \(not considered\). So better to dismiss its use.
* [**PRP-1454**](https://teqplaybv.atlassian.net/browse/PRP-1454) **:** Extending PortInvoiceTotalSummary class and update its content \(separate portcall invoices and portcall order invoices\).
    Approved-by: Wouter Naloop

* [**PRP-1635**](https://teqplaybv.atlassian.net/browse/PRP-1635) **:** fixing 'invoicingLogic.withPortCallAlias\(\)' method failed when invoice relates to a non-existent company.
    Approved-by: Wouter Naloop

* [**PRP-1459**](https://teqplaybv.atlassian.net/browse/PRP-1459) **:** Credit invoice overview based on their debit inovice dates.  
  Approved-by: Gavin den Hollander
* [**PRP-1453**](https://teqplaybv.atlassian.net/browse/PRP-1453) **:** Automatically calculate week start for invoice reporting based on the cron expression in 'schedule.invoicing' property.
    Approved-by: Wouter Naloop

* [**PRP-1522**](https://teqplaybv.atlassian.net/browse/PRP-1522) **:** Use POMA instead of platform to get port locations and berths.
    Approved-by: Maurice van Veen

* **clean :** Remove unused enpoints in staticV2 and port controllers.
    Approved-by: Wouter Naloop

* [**PRP-1249**](https://teqplaybv.atlassian.net/browse/PRP-1249) **:** querying berths from poma in classes NoConfirmationOnDepartOrderTask and NoMovementOnDepartOrderTask.
    Approved-by: Wouter Naloop

* [**PRP-1522**](https://teqplaybv.atlassian.net/browse/PRP-1522) **:** take displayName instead of name from Poma Port class.
* [**PRP-1490**](https://teqplaybv.atlassian.net/browse/PRP-1490) **:** reworking shouldProcessEvent to consider differently if the teqplay event is seen, based on the portcallEvent source to be processed and remove all flipflop test.
    Approved-by: Darius Wattimena

* [**PRP-1612**](https://teqplaybv.atlassian.net/browse/PRP-1612) **:** Create a backend call to retrieve previous N ports and next N ports from VesselVoyage using a ship identifier or portcall ID
    Approved-by: Joaquin Marquez Bugella

* **clean:** feat/small\_cleanup \([pull request #571](https://github.com/teqplay/portreporter-backend/issues/571/remove-tma-external-connection-remove-s5)\)
    remove TMA external connection, remove S5 external connection, remove unused poma, csi and keycloak properties, removed the keycloak interceptor and auth logic as that is already done in skeleton

    Approved-by: Joaquin Marquez Bugella

* [**PRP-1457**](https://teqplaybv.atlassian.net/browse/PRP-1457) **:** Extending DetailedInvoiceInfo model with amount of direct and indirect invoices. Also, correcting a related bug: PortInvoiceTotalSummary model was taking the debit info to build the credit.
    Approved-by: Wouter Naloop

* **Merged in** [**SPV-1178**](https://teqplaybv.atlassian.net/browse/SPV-1178)**-extend-esof \(**[**pull request #580**](https://github.com/teqplay/portreporter-backend/issues/580/smartfleet-extend-esof)**\)**
    SmartFleet: extend ESOF

    Approved-by: Darius Wattimena Approved-by: Wouter Naloop

* [**PRP-1550**](https://teqplaybv.atlassian.net/browse/PRP-1550) **:** Ensure kickbacks from indirect invoices are properly categorised to shippingLines companies.
    Approved-by: Wouter Naloop

* [**PRP-1460**](https://teqplaybv.atlassian.net/browse/PRP-1460)**:** New endpoint for getting the payment delay statistics given a period of time.
    Approved-by: Wouter Naloop

* **fix:** logback spring slack appender
    Approved-by: Michel Wilson


