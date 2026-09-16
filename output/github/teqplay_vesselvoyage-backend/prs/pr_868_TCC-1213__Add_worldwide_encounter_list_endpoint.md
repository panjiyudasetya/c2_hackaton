---
id: github:teqplay/vesselvoyage-backend:pr:868
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 868
title: 'TCC-1213: Add worldwide encounter list endpoint'
author: michel-teqplay
state: open
date: '2026-09-01'
merged_at: null
base_branch: develop
head_branch: TCC-1213-encounter-list
url: https://github.com/teqplay/vesselvoyage-backend/pull/868
labels: []
linked_issues: []
explicit_links: []
---
# PR #868: TCC-1213: Add worldwide encounter list endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/868  
**State:** open | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-1213-encounter-list`  
**Created:** 2026-09-01  

## Description

Closes [TCC-1213](https://teqplaybv.atlassian.net/browse/TCC-1213).

The encounter API could only be queried per ship, but the PTO team needs to ingest bunker encounters worldwide. This adds:

```
GET /v2/encounter/list?start&end[&type][&afterId][&limit]
```

`SHIP:READ`, same as the existing encounter endpoints. `type` is optional — omitting it returns all encounter types. Default limit 1000, max 10000.

## Semantics

- **Time matching** is point-in-range on the encounter start, matching what the existing per-ship encounter endpoints already do. Note this deliberately differs from visits/voyages, which use true interval overlap.
- **Completed only** — encounters without an end are excluded.

Together these mean a consumer walking consecutive ranges never receives the same encounter twice, which is what the bulk-ingest use case needs.

## Pagination

Keyset cursor over `(start.time, _id)`, following the `afterId` + `PaginationMetadata` shape of `/v2/paginated/backfillData`. Not `_id` alone: encounter ids are `"{entryId}:{startEventId}"` and carry no time ordering, so paging on the id would rescan the whole window for every page. A response without an `afterId` is the last page.

The cursor encodes the time as ISO-8601 rather than epoch millis so the round trip is lossless regardless of the precision encounters were stored with.

## Response model

New flat model — `ShipEncounterResponse` is built around a single subject ship, which a worldwide list doesn't have. Each row names both ships.

Encounters only store their `entryId`, so the ship an encounter was recorded for (and, for visits, the port) is resolved per page via lightweight projections on the visit and voyage collections rather than by hydrating full entries. Ship-name enrichment is free — `StaticShipInfoService` is an in-memory cron-refreshed cache.

## Indexes — please read before merging

Two indexes are added to `encountersV2`: `(type, start.time, _id)` for the typed query and `(start.time, _id)` for the untyped one. Both end in `_id` to cover the pagination tiebreaker.

**`encountersV2` is a worldwide collection, so the first startup after this deploys will kick off two index builds.** Worth coordinating with whoever watches the Mongo cluster rather than letting it land unannounced.

The second commit also changes how *all three* encounter indexes are created — now `ensureIndex` inside a named thread, matching the visit and voyage datasources. `background(true)` was removed because it does nothing: deprecated in MongoDB 4.2, and even before that it only relaxed server-side locking during the build, never made `createIndex` return early. The command is synchronous either way, so the thread is what actually keeps the build off the startup path. This does add `ensureIndex`'s drop-and-recreate-on-spec-change behaviour to the pre-existing `(entryId, type)` index — a no-op while the spec is unchanged, but a real change in blast radius if someone edits that index later.

No partial index for the completed-only filter: Mongo's `partialFilterExpression` doesn't support `$ne`, so `end != null` is a residual filter after the indexed range.

## Not included

No `client` module changes — PTO calls this over plain HTTP, so no version bump or S3 publish. Note the client has no encounter coverage at all today, if we ever want to close that gap.

## Testing

`./gradlew test ktlintCheck` green. New tests: 9 cursor, 7 datasource, 9 service, 7 controller.

One thing reviewers should know: moving index creation onto a thread exposed a Mockito race in a pre-existing datasource test — the index thread invokes `createIndex` on the same mock while a test stubs `find`, and Mockito's stubbing state isn't thread-safe. Fixed with the `CountDownLatch` fence `VoyageV2DataSourceTest` already uses. `VisitV2DataSourceTest` may carry the same latent race for the visit datasource's five indexes; I haven't checked, happy to sweep it if wanted.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

[TCC-1213]: https://teqplaybv.atlassian.net/browse/TCC-1213?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

## Commits

- `8905b31f` **Michel Wilson** (2026-08-31): Add worldwide encounter list endpoint
  The encounter API could only be queried per ship, but the PTO team needs
  to ingest bunker encounters worldwide. Adds GET /v2/encounter/list, which
  returns the completed encounters of all ships whose start time falls in
  the requested range, optionally narrowed to a single type.
  
  Time matching is point-in-range on the encounter start, as the existing
  per-ship encounter endpoints already do, and ongoing encounters are
  excluded. Together this means a consumer walking consecutive ranges never
  receives the same encounter twice.
  
  Pages are walked with a keyset cursor over (start.time, _id) rather than
  _id alone: encounter ids are "{entryId}:{startEventId}" and carry no time
  ordering, so paging on the id would rescan the whole window per page. Two
  supporting indexes are added, one for the typed and one for the untyped
  query, and index creation moves to a background thread so an index build
  on this worldwide collection can no longer block API startup.
  
  The response is a new flat model, since ShipEncounterResponse is built
  around a single subject ship. Encounters only store their entry id, so the
  ship an encounter was recorded for and the port it happened in are
  resolved per page through lightweight projections on the visit and voyage
  collections rather than by hydrating full entries.
  
  Co-Authored-By: Claude <noreply@anthropic.com>
- `cb829e58` **Michel Wilson** (2026-08-31): Build encounter indexes with ensureIndex, matching visit and voyage
  Aligns the encounter datasource with the pattern the visit and voyage
  datasources already use: ensureIndex inside a named thread, without the
  background option.
  
  background(true) was doing nothing. It was deprecated in MongoDB 4.2, and
  even before that it only relaxed server-side locking during the build --
  it never made createIndex return early. The command is synchronous either
  way, so the thread is what actually keeps a build off the startup path.
  
  Fencing the index thread in the test with a latch, the way
  VoyageV2DataSourceTest does. Mockito's stubbing state is not thread safe,
  so an index build still running while a test stubs a call corrupts it --
  which surfaced as a null from a stubbed find().
  
  Co-Authored-By: Claude <noreply@anthropic.com>
- `94941457` **Michel Wilson** (2026-09-02): Fix workflow

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-01)

Review completed. 4 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F868%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — DISMISSED (2026-09-02)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-02)

### 🟡 Changes recommended

Several newly added docs/tests claim the API can reject cursors not issued by the endpoint, but the cursor implementation only validates format, making the published contract misleading.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

Adds a new worldwide encounter listing API (`GET /v2/encounter/list`) to support bulk ingestion use cases, including keyset pagination via a `(start.time, _id)` cursor and datasource/query support (including new indexes) while keeping the endpoint under the existing `SHIP:READ` permission model.

**Changes:**
- Introduces a new `/v2/encounter/list` endpoint with optional `type`, validated `limit`, and keyset pagination using an `afterId` cursor.
- Adds datasource support for worldwide encounter listing, including query logic, pagination sort order, and new compound indexes.
- Adds new API response models and a comprehensive set of unit/controller/datasource tests for cursor behavior, pagination, and enrichment.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/EncounterCursor.kt | Adds base64url cursor encoding/decoding for keyset pagination. |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EncounterCursorTest.kt | Tests cursor round-tripping, url-safety, and invalid inputs. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NormalizedEncounterDataSource.kt | Adds worldwide list query + moves/extends index creation to a background thread. |
| src/test/kotlin/nl/teqplay/vesselvoyage/datasource/NormalizedEncounterDataSourceTest.kt | Adds query/filter/sort/limit tests and fences async index creation for determinism. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EncounterV2Service.kt | Implements worldwide list service, subject resolution, ship/port enrichment, and cursor emission. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/EncounterV2ServiceTest.kt | Adds service-level tests for list behavior, enrichment, cursor decoding/returning, and empty-page behavior. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEncounterV2Controller.kt | Exposes `GET /v2/encounter/list` with parameter validation and Swagger metadata. |
| src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEncounterV2ControllerTest.kt | Adds controller tests for list endpoint success, validation, and auth. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/EncounterListResponse.kt | Introduces flat worldwide list response DTOs (entries + pagination metadata). |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/EntryDataSourceSupport.kt | Adds `EntrySubjectReference` projection for lightweight entry-to-ship/port resolution. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/VisitV2DataSource.kt | Adds `findSubjectReferencesByIds` projection query for visits. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/VoyageV2DataSource.kt | Adds `findSubjectReferencesByIds` projection query for voyages. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt | Exposes visit subject-reference lookup via service layer. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VoyageV2Service.kt | Exposes voyage subject-reference lookup via service layer. |
| .github/workflows/main.yml | Adds explicit GitHub Actions permissions (including `id-token: write`). |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 15/15 changed files
- **Comments generated:** 4
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

## Review Comments

### Copilot — 2026-09-02 on `.github/workflows/main.yml`

This workflow adds `id-token: write`, which broadens GitHub Actions token permissions and is unrelated to the encounter endpoint change described in the PR. If OIDC is required by the referenced reusable workflow, consider documenting that here (or in the PR description); otherwise, drop the extra permission to keep least-privilege.

### Copilot — 2026-09-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEncounterV2Controller.kt`

The 400-response description says afterId must be a cursor "returned by this endpoint", but the implementation only checks cursor format (base64 + parseable Instant + non-empty id) and cannot verify provenance. This wording is misleading for API consumers; describe it as "valid pagination cursor" instead.

### Copilot — 2026-09-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/EncounterCursor.kt`

The KDoc claims decode() rejects cursors that were not handed out by the API, but the implementation only validates base64 + basic structure/time parsing. Clients can still craft a syntactically valid cursor, so the comment is misleading; either sign/encrypt the cursor or adjust the wording to match the actual validation.

### Copilot — 2026-09-02 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/EncounterV2ServiceTest.kt`

This test name implies the service can detect whether a cursor was actually issued by the API, but the current behavior only rejects malformed values (e.g., not base64 / not parseable). Renaming avoids asserting stronger guarantees than the code provides.

## Comments
