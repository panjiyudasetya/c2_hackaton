---
id: github:teqplay/vesselvoyage-backend:pr:875
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 875
title: Keep a degraded ship history from stalling processing
author: TeqJoostD
state: open
date: '2026-09-04'
merged_at: null
base_branch: develop
head_branch: claude/shiphistory-trace-error-um4a99
url: https://github.com/teqplay/vesselvoyage-backend/pull/875
labels: []
linked_issues: []
explicit_links: []
---
# PR #875: Keep a degraded ship history from stalling processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/875  
**State:** open | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `claude/shiphistory-trace-error-um4a99`  
**Created:** 2026-09-04  

## Description

## Background

The restart on 2026-09-04 01:35 was not a crash — it was an external kill while a batch was in flight. The chain from the logs:

1. Ship history (`/v1/ship/history/mmsi`) degraded: calls either timed out (`HttpTimeoutException: Request cancelled`) or had their response stream closed mid-parse (`IOException: closed` inside Jackson).
2. `PostProcessingService` pinned its entire pool on those calls. With `post-processing.total-threads=2` and 71 queued entries (45 visits + 26 voyages), each burning 3 sequential read timeouts, both threads stayed blocked for the whole 01:30–01:35 window.
3. Actuator health contributors started taking 21–62s to answer.
4. `SpringApplicationShutdownHook` fired at 01:35:25. Nothing in-process calls `System.exit`, and `ProcessingService.onClose` is a `ContextClosedEvent` listener, so this came from outside — a probe timeout getting the pod killed is the only explanation consistent with the health-check delays.
5. The shutdown then dropped data: the AIS lane drain gave up after 30s and force-dropped **308 of 372** already-acked items, interrupting lane workers mid-Mongo-write (`MongoInterruptedException`).

## Changes

**Raise the AIS lane drain timeout from 30s to 120s** (`RabbitMqAisConsumerService`)

Lane items are acked as soon as they are routed, so anything still queued when the timeout elapses is genuinely lost. The pod is given `terminationGracePeriodSeconds: 240` precisely because this persistence "takes 2+ minutes" (per the comment in `helm/values.yaml`), so the old 30s handed back most of the budget it had. 120s leaves room for the consumer close that precedes the drain (which took ~80s during the incident) and for `onStopBackgroundProcessing` afterwards.

**Stop a failing ship history from occupying every post-processing thread** (`PostProcessingService`)

- Retries no longer recurse on the worker thread; the loop is flat and bounded.
- After six consecutive failed attempts (two entries exhausting their retries) ship history goes into a one-minute cooldown, during which fetching fails immediately without calling out. The threads are released and the affected entries stay queued for a later cycle instead of each one burning three read timeouts.
- **Behaviour change worth reviewing:** exhausted retries now throw instead of returning an empty trace. Previously the entry was persisted with `postProcessed = true`, no trace and no slow-moving periods, and then removed from the queue — so a transient ship-history outage produced *permanent* data gaps. Now the entry is left queued and retried next cycle. A legitimately empty trace (ship genuinely has no AIS history) is unaffected; only actual failures throw.
- The interrupt flag is preserved across the retry sleep, so a shutdown stops the workers promptly instead of being swallowed and retried.

**Give ship history a 25s read timeout instead of the shared 15s default** (new `ShipHistoryRestTemplateConfiguration`)

With the JDK `HttpClient` request factory the read timeout is a deadline for the *whole* response, and a long visit or voyage carries thousands of AIS messages — which is what produced `JSON parse error: closed`. The new template reuses the shared `@InternalApiRestTemplate` bean's interceptors, URI handling and error handler, so Keycloak auth and outgoing-request logging behave identically; only the request factory differs. The shared template is deliberately left untouched, so no other internal-API caller is affected.

## Verification

`./gradlew ktlintCheck` passes.

**`compileKotlin` and `test` could not be run here** — this environment cannot authenticate to `s3://repo.teqplay.nl`, so no `nl.teqplay.*` artifact resolves (`InvalidAccessKeyId`). Please let CI be the first real compile. Two things I could not verify locally and would flag for a reviewer's eye:

- `JdkClientHttpRequestFactory(HttpClient)` + `setReadTimeout(Duration)` — correct for the Spring Framework 6.2 that Boot 3.5.16 pulls in, but unexercised here.
- That the shared internal-API template carries its base URL via `uriTemplateHandler` (which the new template copies). The incident log resolving `https://internalapi.teqplay.dev/v1/ship/history/mmsi` from a relative path says it does, but a 404 on ship history after deploy would be the symptom if that assumption is wrong.

## Tests

- `should handle AIS fetch failure after retries without exceptions and no trace recalculation` asserted the old behaviour (`verify(dataSource).remove(entryId)`) and is rewritten as `should leave the entry queued when the AIS fetch keeps failing`, now asserting nothing is persisted or removed.
- Added `should stop calling ship history once it keeps failing and skip the remaining entries`: three failing entries produce six calls, not nine, and none are removed.

## Not addressed

The k8s probe side of the chain. There is no `livenessProbe`/`readinessProbe` config in this repo (`helm/values.yaml` is consumed by an external shared chart), so I could not confirm the thresholds. Worth checking separately whether a 20–60s health-check stall should really cost a restart, and whether the actuator contributors should be insulated from a slow downstream.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_013exyhWpZbEyrHaetsxynxc

---
_Generated by [Claude Code](https://claude.ai/code/session_013exyhWpZbEyrHaetsxynxc)_

## Commits

- `befabe5e` **Claude** (2026-09-04): Keep a degraded ship history from stalling processing
  The pod restart on 2026-09-04 01:35 started with the ship history
  endpoint going slow: calls to /v1/ship/history/mmsi either timed out or
  had their response stream closed mid-parse. Post-processing then pinned
  its whole (2 thread) pool on those calls for minutes, actuator health
  contributors started taking 20-60s to answer, and the pod was killed
  while a batch was in flight.
  
  Three changes, none of which depend on ship history recovering:
  
  - Raise the AIS lane drain timeout from 30s to 120s. Lane items are
    already acked, so whatever is still queued when it elapses is lost -
    the incident dropped 308 of 372 pending items. The pod gets a 240s
    termination grace period, so the old 30s gave away most of the budget
    it had to persist that work.
  
  - Stop a failing ship history from occupying every post-processing
    thread. Retries no longer recurse on the worker thread, and once six
    attempts have failed in a row the endpoint goes into a one minute
    cooldown during which fetching fails immediately, freeing the threads
    and leaving the entries queued. Exhausted retries now throw instead of
    returning an empty trace: previously the entry was persisted as
    postProcessed with no trace and no slow moving periods, permanently,
    which is why a transient outage produced permanent data gaps. Also
    keep the interrupt flag intact so a shutdown stops the workers
    promptly instead of being swallowed by the retry loop.
  
  - Give ship history its own internal API template with a 25s read
    timeout instead of the shared 15s default. With the JDK HttpClient
    factory the read timeout is a deadline for the entire response, and a
    long visit or voyage carries thousands of AIS messages. The template
    reuses the shared bean's interceptors and URI handling, so auth and
    request logging are unchanged and no other internal API caller is
    affected.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_013exyhWpZbEyrHaetsxynxc

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F875%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-04)

### 🟡 Changes recommended

The cooldown/failure-streak logic in `PostProcessingService` has edge cases that can undermine the intended “fail fast after repeated ship-history failures” behavior and should be tightened before approval.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR hardens background post-processing against a degraded internal ship-history endpoint so that post-processing threads don’t stall for minutes and shutdown drains are less likely to drop already-acked AIS lane items.

**Changes:**
- Increase AIS lane shutdown drain timeout from 30s to 120s to better fit the pod termination budget.
- Refactor ship-trace fetching in `PostProcessingService` to bounded retries + a global cooldown after repeated failures, and leave entries queued instead of persisting “postProcessed=true” with missing trace.
- Introduce a ship-history-specific `RestTemplate` with a longer read timeout and wire `AisHistoryClient` to use it.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt | Updates behavior assertions (leave queued on repeated failures) and adds cooldown-skipping coverage. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/RabbitMqAisConsumerService.kt | Raises lane drain timeout constant and documents the shutdown-budget rationale. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt | Implements bounded retries, cooldown, and failure signaling to avoid permanently persisting entries without ship traces during outages. |
| src/main/kotlin/nl/teqplay/vesselvoyage/config/ShipHistoryRestTemplateConfiguration.kt | Adds a dedicated ship-history `RestTemplate` with a 25s read timeout while reusing internal-api interceptors/URI/error handling. |
| src/main/kotlin/nl/teqplay/vesselvoyage/config/PlatformClientAutoConfiguration.kt | Wires `AisHistoryClient` to the ship-history-specific `RestTemplate`. |
| src/main/kotlin/nl/teqplay/vesselvoyage/client/AisHistoryClient.kt | Switches injection qualifier to the ship-history-specific `RestTemplate`. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 6/6 changed files
- **Comments generated:** 2
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

## Review Comments

### Copilot — 2026-09-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

`onShipHistorySuccess()` resets the shared consecutive-failure counter/cooldown on any non-throwing return from `aisFetchingService.getShipTrace(...)`. Because `AisFetchingService.getShipTrace` can return `emptyList()` without ever calling ship history (e.g. max-request-length guard, missing MMSI/IMO mapping), those “local skips” can break an otherwise consecutive failure streak and delay/avoid entering cooldown when ship history is actually unhealthy.

### Copilot — 2026-09-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Cooldown is only checked once at the start of `getShipTraceWithRetries`. If ship history enters cooldown due to failures mid-loop, this invocation can still keep retrying (and sleeping) up to `MAX_SHIP_TRACE_ATTEMPTS`, keeping a post-processing thread busy longer than necessary. Consider aborting remaining retries immediately once cooldown is activated.

## Comments
