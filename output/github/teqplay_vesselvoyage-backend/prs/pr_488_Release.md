---
id: github:teqplay/vesselvoyage-backend:pr:488
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 488
title: Release
author: TeqJoostD
state: closed
date: '2025-04-30'
merged_at: '2025-05-07'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/488
labels: []
linked_issues: []
explicit_links: []
---
# PR #488: Release

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/488  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-04-30  
**Merged:** 2025-05-07  

## Description

_No description._

## Commits

- _… 7 earlier commits not shown_
- `d0610707` **leonj** (2025-04-14): Only log when the squashed visit actually has a value
- `9112dc8c` **leonj** (2025-04-14): Log more stuff on switching main ports, seems to go south there
- `a2ceef7c` **leonj** (2025-04-14): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `1b579149` **Pim van den Toorn** (2025-04-22): Updated kotlin, platform, spring and kotlin logging
- `a40d45f9` **Pim van den Toorn** (2025-04-22): Updated gradle, kotlin csv, dockerapi and cyclonedxBom
- `952f8348` **leonj** (2025-04-23): Add processing logs to the database, so we can query it easier than log files
- `2200bb09` **TeqJoostD** (2025-04-23): feat: add tolerance to qualification of arrival/departure tugs
- `6d011b31` **leonj** (2025-04-23): Limit retrieving AIS to max 90 days (also chunked requests total days cannot be longer)
- `ab9b97ad` **leonj** (2025-04-23): Merge branch 'develop' into SPV-2585-aisdata-limit-3months
- `700ba6cc` **TeqJoostD** (2025-04-23): feat: add tolerance to qualification of arrival/departure tugs
- `da20e9ec` **TeqJoostD** (2025-04-23): fix: ktlint
- `d1314bb0` **TeqJoostD** (2025-04-23): fix: add missing annotation
- `4be80324` **TeqJoostD** (2025-04-23): fix: add missing annotation
- `1d8d493d` **TeqJoostD** (2025-04-23): fix: fix test
- `e9f16440` **leonj** (2025-04-24): Log statements to debug, not warn. Remove comment
- `843a0b18` **Leon Joosse** (2025-04-24): Fix potential NPE in AisFetchingService
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `01fd9df3` **leonj** (2025-04-24): Fix profile for ProcessorLogDatasource
- `4809aeb7` **leonj** (2025-04-24): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `1df49ef1` **leonj** (2025-04-24): Add flag to enable event processing logs (default=false), as this may result in a big database collection
- `7fe1d7b0` **Bugella** (2025-04-24): PRP-2675: Replacing the @Configuration annotation by the correct @AutoConfiguration, so to make it autodiscoverable when booting.
- `8df54ace` **leonj** (2025-04-24): Merge remote-tracking branch 'origin/blacklist' into SPV-2566-eventprocessor-log-decisions
- `be610ff4` **leonj** (2025-04-24): Fix insert of log
- `e95164c9` **Joaquin M Bugella** (2025-04-28): Merge pull request #485 from teqplay/maintenance/prp-2675/fixClientConfiguration
  PRP-2675: Replacing the @Configuration annotation by the correct @AutoConfiguration, so to make it autodiscoverable when booting.
- `425d7356` **Darius Wattimena** (2025-04-28): fix: update coverage workflow to use the latest master branch
- `003f22b4` **Darius Wattimena** (2025-04-28): Merge pull request #486 from teqplay/codecov-reusable-action
  fix: update coverage workflow to use the latest master branch
- `8d8a6631` **PimTeqplay** (2025-04-28): Merge pull request #481 from teqplay/SEC-141-dependency-updates
  Sec 141 dependency updates
- `6f4cceff` **Leon Joosse** (2025-04-29): Merge pull request #484 from teqplay/SPV-2585-aisdata-limit-3months
  SPV-2585: Limit AIS data retrieval to max 3 months
- `29ddd47b` **TeqJoostD** (2025-04-30): fix: change feedback
- `2b69598b` **TeqJoostD** (2025-04-30): fix: add try catch
- `ea597cc0` **TeqJoostD** (2025-04-30): fix: add stacktrace
- `740e4253` **TeqJoostD** (2025-04-30): fix: add stacktrace
- `f09183d0` **Joost Dambrink** (2025-04-30): Merge pull request #482 from teqplay/SPV-2560
  SPV-2560 add tolerance to qualification of arrival/departure tugs
- `2beca555` **Joost Dambrink** (2025-04-30): Merge pull request #483 from teqplay/blacklist
  Added ship blacklist
- `9302e784` **Joost Dambrink** (2025-04-30): Merge pull request #487 from teqplay/SPV-2612
  fix: add try catch
- `09c73ff9` **leonj** (2025-04-30): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `235c2b44` **Darius Wattimena** (2025-04-30): Try to fix an issue where pushing a docker image doesn't seem to work
- `6c80513c` **Darius Wattimena** (2025-04-30): Try to fix an issue where pushing a docker image doesn't seem to work
- `5f593b6c` **Darius Wattimena** (2025-04-30): Revert gradle version and docker api version
- `b42d2ea3` **Darius Wattimena** (2025-04-30): Upped gradle to first 7.6 compatible version
- `5f841d59` **Darius Wattimena** (2025-04-30): Remove bom support as it doesn't seem to work
- `9b707500` **Darius Wattimena** (2025-05-01): Merge pull request #490 from teqplay/fix-gradle
  Fix gradle
- `844e19d9` **Leon Joosse** (2025-05-01): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `92d7cdd8` **leonj** (2025-05-01): Fetching ais data, reduce certain log levels from DEBUG -> TRACE
- `2d433341` **leonj** (2025-05-01): Fix import
- `e111e077` **Leon Joosse** (2025-05-01): Merge pull request #472 from teqplay/SPV-2566-eventprocessor-log-decisions
  SPV-2566: eventprocessor log decisions
- `a7225349` **Leon Joosse** (2025-05-01): Merge pull request #491 from teqplay/ais-fetching-logs
  Fetching ais data, reduce certain log levels from DEBUG -> TRACE
- `5cc897bb` **leonj** (2025-05-02): Enhance logs for traces. Reduce logging level for 'post-processing done' messages, spamming too much
- `2febc304` **Darius Wattimena** (2025-05-02): Changed direct memory size to 50m instead of the default 10m to solve an issue where VesselVoyage processing crashes because there is not enough native memory available
- `72f9cdd9` **Darius Wattimena** (2025-05-02): Merge pull request #493 from teqplay/bigger-buffer
  bigger buffer
- `3e1f9665` **Leon Joosse** (2025-05-06): Merge pull request #492 from teqplay/enhance-some-logs
  Enhance logs for traces.
