---
id: github:teqplay/portreporter-backend:issue:1169
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1169
title: Develop
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1169
labels: []
explicit_links: []
---
# Issue #1169: Develop

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1169  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [efaf87487ae9...34a33d805c4c](https://github.com/teqplay/portreporter-backend/compare/efaf87487ae9...34a33d805c4c)
**Merge commit:** [34a33d805c4c](https://github.com/teqplay/portreporter-backend/commit/34a33d805c4c)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2022-10-04T08:33:01.392078+00:00
**Status:** MERGED

* PRP-974: inbetween commit singapore fallback reformat

* PRP-974: split up scheduler into subscription based and non subscription based, make the tests work, remove unused functions

* PRP-974: store the fallback event as portcallEvent before doing the full restructure, as this restructure fetches all portcallEvents and rebuilds it from that.

* PRP-974: small changes can cause big build fails

* PRP-974: start of adding unittests sgsin fallback

* PRP-974: add more tests

* PRP-974: add more tests

* PRP-974: parse the statusevents once into a combined list and only then check the portcallevent type, to reduce the amount of times we loop over all statusevents

* PRP-974: use vararg and SortedSet instead of list and treeset

* PRP-974: fix tests and the code based on what is modelled in the tests

* PRP-971: remove the specific line that accepts all events for singapore, and ignore pilotboarding place ata and atd events. This works because in the formattedEvents for singapore it is not resolved to the corresponding types but kept as raw

* PRP-971: sgsin can process multiple pilot events per portcall, fix tests to reflect that the pilot atae and atde are ignored, write the shouldStatusBeAdded fully as when

* PRP-974: introduce a function which explains the why

* PRP-974: merge develop into this branch and clean up imports

* PRP-974: fix build

* PRP-974: add error logging spring boot properties to show the message

* PRP-974: apparently spring did not like one of the values i gave to a spring property

* Upgraded spring boot on top of the pilot fallback branch, changed from springfox swagger to springdoc

* Allow access to v3 api docs

* PRP-1240: start of eks changes

* PRP-1240: date to instant start but does not work yet

* PRP-1240: make instants work by removing the kmongo configuration, cleanup, remove portcallplus Date converter, remove all DateTimeFormat annotations

* PRP-1240: I know this still fails, but fixed the date to long bug

* PRP-1240: resolve merge conflicts and make sure it can run on beanstalk again

* PRP-1240: downgrade gradle

* PRP-1240: trying to get portreporter to build on circleCi

* PRP-1240: re add git properties

* PRP-1240: override mongo client instead of settings only

* PRP-1240: add skeleton to portreporter

* PRP-1240: attempt to fix deploy exception

* PRP-1240: fix null

* PRP-1240: attempt 3 but now aligned with other beanstalk projects

* PRP-1240: fix build issue

* PRP-1240: Remove Literals, add skeleton mongo authDb property, fix mongo allowed regex pattern,

* PRP-1240: add specific duration serializer to the objectmappers

* PRP-1240: change the durations to strings

* PRP-1240: fix tests duration

* PRP-1240: use skeleton's mongo config to print in the logs

* PRP-1240: remove the old authdb entry

* PRP-1240: applied pr feedback in doing that found a timezoning issue where dates in a different timezone were shown as Z(UTC) but should have their timezone attached

* PRP-1240: removed the string to timestamp with minutes added method

* PRP-1240: removed indentation because Retrofit2 doesn’t like pretty-printed JSON, this was no problem before because the bean was not spring wide

* PRP-1240: merge develop into this

* PRP-1240: warn to not use this objectmapper, as we want to remove it soonish

* PRP-1240: eks upgrade

* PRP-1240: change the docker image name to what is in ecr

* PRP-1240: make the error level slack logging configurable and default to ERROR

* PRP-1240: set default actuator settings, remove the repo name info from the circle ci and hardcode it

* PRP-1240: hard hard code it

* PRP-1240: locally disable the slack webhook, disable the default rabbitmq health check of spring

* PRP-1240: remove the exclude by default config of the actuator and include the liveness and readiness states in the actuator

* PRP-1240: allow access without auth to every actuator endpoint

* PRP-1240: remove ebs folders, apply the liveness and readiness as group when locally using portreporter

* PRP-1240: add the publish library step to circleCi

* PRP-1240: test publish library when this branch is pushed

* PRP-1240: revert test setup for portcall library publish, upgrade gradle wrapper to 7.4.1, remove git properties

* PRP-1240: Feedback on the main PR, Instant.from removal, duration parse without catching the exception to make sure it does not run whenever the duration is wrong

* PRP-1240: make the last duration in a constructor into a String since mongo does not provide support for durations since 3.7

* PRP-1240: apparently there is a json creator annotated method that still had a duration

* PRP-1240: change durations of infeasible task

* PRP-1240: only convert duration into a string if it actually contains a duration, null.toString results in "null"

* New snapshot version 5.19.0-SNAPSHOT

* PRP-1240: move portreporter to the normal develop url

* PRP-1240: change the circleci to not reuse helm values, change the cpu request to 0.1 it almost never goes over that, half the memory limits, also based on usage of the last 14 days

* PRP-1240: merge develop into the eks branch

* Merged in feat/upgrade_spring_boot_fetching_timestamps (pull request #513)

    Correcting fetching timestamps issues

    * EKS - Correcting fetching timestamps issues.

    Approved-by: Maurice van Veen

* Merged in feat/PRP-300/new_esof_pdf_export (pull request #502)

    PRP-300: Adding two new endpoints for downloading the new E-SoF in PDF and JSON format (first version).

    Approved-by: Joost Laurman

* PRP-1404 : Upgrading platform version (currently snapshot) to use new EKS nexmo gateway. To be updated after platform version is live released).

* Resetting to empty notification.alertEmails in application.properties to avoid mistaken alert notifications from local.

* Merged in feat/PRP-1465/extend_invoice_search (pull request #516)

    PRP-1465 : Extend invoice search with arguments for billing mode and shipping line Id.

    Approved-by: Maurice van Veen

* fixing merge of develop (PRP-1465): conflict resolved missing a @Parameter's parameter 'description'.

* PRP-1465 : Extend invoice search with debit/credit param.

* PRP-1404: Upgrading platform version to 8.76.0

* Add try/catch to Exact status check scheduled task

* PRP-1429 : Remove invoice_options parameter from body in /v1/invoices/generateNew endpoint.

* PRP-1320: Correcting the obtention of the week for the backend stats generation.

* Updating CHANGELOG.md to state previous commit's change: EKS version merged.

* Merged in feat/PRP-558/calculate_invoice_kickback (pull request #523)

    PRP-558 : Adding the following endpoints for:

    * PRP-558 : Adding the following endpoints for:
    - Get spreadsheet about shippingLine overviews in a given range.
    - Send by email the mentioned spreadsheet (same paramaters) to a
    list of recipients.
    - Two homologous endpoints for agencies.

    * Apply feedback and some adaptations to the eks version.

    * Cleaning commented lines

    * Cleaning commented line


    Approved-by: Maurice van Veen

* Merged in fix/PRP-1471/nomination_matching_by_reference (pull request #524)

    PRP-1471 : Make sure that a close nomination in time for the same vessel, company and port but a different

    * PRP-1471 : Make sure that a close nomination in time for the same vessel, company and port but a different
    reference produces a new nomination instead of updating it (by mistake as the eta's timerange is close enough).

    * Using this and making sure searching for reference when it's provided.

    * Making sure searching for reference when it's provided (not null and not blank).


    Approved-by: Darius Wattimena

* PRP-1240: remove the bootstrap properties slackwebhook value and remove the default from application.properties

* Merged in logging_all_papertrail_alerts (pull request #526)

    making sure that we do not lose the useful alerts from papertrail when we deprecate that

    * making sure that we do not lose the useful alerts from papertrail when we deprecate that

    Approved-by: Joaquin Marquez Bugella

* Not logging rejected portcallcallevent messages.

* reducing some Severe level logs to WARN, apply the objectmapper that is autowired instead of the deprecated objectmapper for all connections and interceptors. This is to fix a date parse issue

* some more deprecated objectmappers removed

* add the mockbean of objectmappers, validated is not supposed to be known by the frontend

* Modifying the default dev webhook for error-logging.

* Merged in tests/fix_timestamp_format_in_application (pull request #528)

    Tests/fix timestamp format in application
    - Format applied in the application.properties
    - Log number of portcalls returned by portcallPlus's getUpdateSince(...).
    - Adding an explaining comment for spring.jackson.date-format

    Approved-by: Wouter Naloop

* Adding specific email address for vopak EDI invoices for the port of Vlissingen.

* up the limit of active portcalls fetch, no port has 10000 portcalls going on at the same time so should be enough

* This is used by isps and that wants the current active portcalls, not the portcalls of 14 days ago

