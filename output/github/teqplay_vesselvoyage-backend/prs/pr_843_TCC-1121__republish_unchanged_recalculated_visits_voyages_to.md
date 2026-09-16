---
id: github:teqplay/vesselvoyage-backend:pr:843
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 843
title: 'TCC-1121: republish unchanged recalculated visits/voyages to PTO'
author: TeqJoostD
state: closed
date: '2026-08-05'
merged_at: '2026-08-06'
base_branch: develop
head_branch: TCC-1121-2
url: https://github.com/teqplay/vesselvoyage-backend/pull/843
labels: []
linked_issues: []
explicit_links: []
---
# PR #843: TCC-1121: republish unchanged recalculated visits/voyages to PTO

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/843  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-1121-2`  
**Created:** 2026-08-05  
**Merged:** 2026-08-06  

## Description

## What

In the revents scenario **merge-back**, a recalculated visit/voyage that is **exactly the same** as the version already stored (ignoring `updatedAt`/`regenerated`) is no longer treated as a normal update. It is now:

- **still persisted** — so `updatedAt` is bumped and `regenerated` stays `true`;
- **published to PTO only**, under a dedicated routing key `SOFVIEW.PTO.<status>.RECALCULATE_UNCHANGED.<imo>` (a new `Action.RECALCULATE_UNCHANGED`), instead of a regular `UPDATE` across all views.

This lets PTO consumers tell a no-op reconfirmation apart from a genuine change, and gives every recalculated entry a fresh `updatedAt` even when nothing changed.

## How

- `Action.RECALCULATE_UNCHANGED` added (with docs).
- `ReventsRecalculationService.persistMergeResultV2` compares each merged entry to the stored one it replaces (`mergeResult.overwrittenEntries`), ignoring `updatedAt`/`regenerated`; identical entries are flagged `RECALCULATE_UNCHANGED` and get a bumped `updatedAt`.
- `ChangesPublisherService` emits **only** the PTO SOF view for `RECALCULATE_UNCHANGED` (suppressing the entry change and the PortReporter view).
- Visit/Voyage/Esof `V2DataSource` persist the new action as an upsert; `ReplayEntryResolver` treats it like an update.

## Notes for review

- **Comparison is entry-only** — the ESoF is deliberately excluded, because at merge time it is still incomplete (drift/slow-moving/traces are computed by the later post-processing step), so comparing it would make the check never fire.
- **Voyages have no PTO view**, so an unchanged voyage is persisted but publishes nothing.
- The new routing key is **not** added to the outgoing-change audit log (these are no-ops); say the word if it should be.

## Tests

- `ChangesPublisherServiceTest`: identical visit -> PTO-only on the new key; identical voyage -> nothing published.
- `ReventsRecalculationServiceTest`: identical merged visit is flagged `RECALCULATE_UNCHANGED`.
- `./gradlew compileKotlin compileTestKotlin ktlintCheck` and both test classes pass.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `68419606` **TeqJoostD** (2026-08-05): TCC-1121: republish unchanged recalculated visits/voyages to PTO
  In the revents scenario merge-back, a recalculated visit/voyage that is
  identical to the version already stored (ignoring updatedAt/regenerated)
  is now still persisted - bumping updatedAt and keeping regenerated=true -
  and published to PTO only, under a dedicated RECALCULATE_UNCHANGED
  routing key (SOFVIEW.PTO.<status>.RECALCULATE_UNCHANGED.<imo>), instead
  of a regular UPDATE across all views. This lets PTO consumers tell a
  no-op reconfirmation apart from a genuine change.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `6636560b` **TeqJoostD** (2026-08-06): TCC-1121: route unchanged recalcs via routing-key prefix, not a new Action
  Revert the Action.RECALCULATE_UNCHANGED enum value (and its datasource /
  ReplayEntryResolver ripples) - Action ships in the published client
  artifact and has no @JsonEnumDefaultValue fallback, so a new value breaks
  consumers deserializing it.
  
  Instead, unchanged recalculated entries keep a regular UPDATE action and
  are published to PTO only on a dedicated routing key carrying a hardcoded
  prefix (RECALCULATE_UNCHANGED.SOFVIEW.PTO.<status>.UPDATE.<imo>), via a
  recalculateUnchanged flag threaded through the publisher and a new
  PersistChangesService.persistAndPublishUnchangedRecalculation. Message
  bodies are unchanged, so no consumer breaks; consumers opt in by binding
  the prefixed namespace.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `a833cb2d` **TeqJoostD** (2026-08-06): TCC-1121: publish unchanged recalcs as FINAL to PTO, from finalized data
  PTO binds SOFVIEW.PTO.FINAL.# (finished info only), but the merge-back
  publish was LIVE, so the unchanged reconfirmations never reached them and
  would have carried an incomplete merge-time ESoF.
  
  Now an entry is only treated as an unchanged reconfirmation when it is
  identical to the stored one AND that stored version is already finalized
  (esof.postProcessed). Such entries are published as FINAL, to PTO only, on
  RECALCULATE_UNCHANGED.SOFVIEW.PTO.FINAL.UPDATE.<imo>, reusing the finalized
  stored ESoF instead of the incomplete merged one. Trace recalculation and
  post-processing are skipped for them, so post-processing no longer also
  republishes them on the normal FINAL keys.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `d07b5edc` **TeqJoostD** (2026-08-06): TCC-1121: fix build - keep tryPublishNewChanges signature intact
  Adding a recalculateUnchanged parameter to the public tryPublishNewChanges
  broke every matcher-based verify of it (InvalidUseOfMatchersException in
  EntryProcessingService/PersistChangesService/ManualRecalculation/StoryRepair
  tests): mixing Mockito matchers with the Kotlin default value is illegal.
  
  Keep tryPublishNewChanges at its original signature and extract the shared
  loop into a private publishChanges; add a dedicated public
  publishUnchangedRecalculation for the PTO-only FINAL prefixed path, which
  PersistChangesService now calls. Full test suite passes.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-05)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F843%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — CHANGES_REQUESTED (2026-08-06)

Could you check if this also covers the usecase which PTO actually needs.

They currently use the following routing keys:
- SOFVIEW.PTO.FINAL.#
- SOFVIEW.PTO.LIVE.DELETE.#

Here `SOFVIEW.PTO.FINAL.#` is important given they only want finished information, or when thing should be removed.

Anyhow, does this create the `RECALCULATE_UNCHANGED.SOFVIEW.PTO.FINAL.#` for the PTO team to use? Given we don't want to provide them with unfinished information?

### Darius-Wattimena — APPROVED (2026-08-06)

_No comment._

## Review Comments

## Comments
