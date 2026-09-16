---
id: github:teqplay/vesselvoyage-backend:pr:862
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 862
title: 'TCC-1180: Merge revents scenarios back in parallel on their own threads'
author: Darius-Wattimena
state: closed
date: '2026-08-21'
merged_at: '2026-08-27'
base_branch: develop
head_branch: TCC-1180-parallel-scenario-merging
url: https://github.com/teqplay/vesselvoyage-backend/pull/862
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1180
---
# PR #862: TCC-1180: Merge revents scenarios back in parallel on their own threads

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/862  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1180-parallel-scenario-merging`  
**Created:** 2026-08-21  
**Merged:** 2026-08-27  

## Description

[TCC-1180](https://teqplaybv.atlassian.net/browse/TCC-1180)

## Why

Merging a finished (r)events scenario back was fully sequential. `checkScenarioProgress` walked `runningScenarios` one scenario at a time and merged every ship inline before looking at the next one, so one big scenario blocked everything behind it.

It also ran on Spring's scheduler, whose pool is 1 and shared with seven other `@Scheduled` methods. While a merge ran, `PostProcessingService.executePostProcessing`, `TraceService.generateTraces` and the automatic-recalculation tasks could not run at all — the very steps that finish the data the merge just wrote.

## What changed

**Tracking moved off the scheduler.** `ReventsScenarioTracker` owns a `revents-tracker` daemon thread that runs the tracking passes. `checkScenarioProgress()` keeps its name and signature and is now simply "one pass"; only the `@Scheduled` annotation is gone. `ReventsTrackerSignal` is the wake-up channel (its own bean, to avoid a dependency cycle), so a scenario queued right after a pass is picked up in seconds instead of waiting out the poll interval — manual merges via the `mergeShipRecalculation` endpoints benefit most.

**Merging runs on two bounded pools.** `ThreadPoolReventsMergeExecutor` fans scenarios out over `revents-merge-scenario-` threads and the ships of each scenario over `revents-merge-ship-` threads. The pools are deliberately separate: a scenario thread waits for its own ships, so sharing one pool would deadlock. A pass only polls and submits, so it stays short even while a very large scenario merges.

The ticket asked for low-priority threads. `Thread.MIN_PRIORITY` is a no-op on Linux without `-XX:+UseThreadPriorities` and elevated privileges, so pool capacity is the throttle instead: the ship pool is small and separate from both the RabbitMQ AIS lanes and the post-processing pool.

**Ships are now concurrent, so:**
- the ship lock (`ShipLockService`) is taken for the **whole** per-ship merge, serialising a ship against both other scenarios and live AIS processing. The merge that used to be computed twice — once unlocked, then thrown away and recomputed under the lock when it touched the ship status — is now computed once. That is a second speed-up on top of the parallelism, and it closes the window between the two merges;
- the error, merge-failure and statistics collectors are lock-guarded and report in sorted rather than completion order, so a scenario's status document is reproducible.

Verified as already thread-safe, no change needed: `EntriesMergeV2Service`, `EntryProcessingService.replayDryRun`, `EventProcessingService`, `ProcessingShipStatusService`, `ShipChangeStatisticsService`, `MeasuringService`, `ScenarioLoggingContext`.

**Drive-by fix:** `EndMergeEvent` was not published when fetching the ships to merge failed retryably, leaving `ScenarioMeasurement` with an open merge. That measurement is how this ticket's improvement is judged, so it is now published in a `finally`.

## Config

```
recalculation.tracker-poll-interval=PT1M
recalculation.merge-ship-threads=4
recalculation.merge-ship-queue-capacity=10000
recalculation.max-concurrent-scenarios=3
```

`merge-ship-threads=1` with `max-concurrent-scenarios=1` reproduces the old sequential behaviour — the rollback switch.

## Behaviour changes worth reviewing

Two existing tests changed expectations, both intentional:
- two asserted `entriesMergeV2Service.merge` ran twice per ship+window; the collapsed double merge makes that once;
- one asserted `mergeFailureSummary.reasons` in first-failure order; with concurrent ships that order is nondeterministic, so reasons now sort by declaration order.

## Testing

`./gradlew ktlintCheck test` passes. 66 existing + 14 new tests in the recalculation package, and the `@SpringBootTest` context test for the `processing` profile still boots, so the new beans wire and the properties bind.

New coverage: the tracker keeps running passes and survives a failing one, a signal wakes it early, shutdown stops it; the executor refuses a scenario that is already merging and beyond the configured maximum, returns ship results in input order, finishes every ship before surfacing a failure, and merges on the caller rather than dropping ships when the queue is full; a scenario's ships all merge in parallel, the same ship in two scenarios never merges concurrently, a scenario still merging is not picked up by the next pass, and `EndMergeEvent` fires on the retryable path.

## Not yet verified

The thread defaults are reasoned, not measured. Before this is called done, a large and a small scenario should be triggered together on dev to confirm the small one finishes without waiting, and the before/after wall-clock read from the `ScenarioMeasurement` documents (`startMergeTime`/`endMergeTime`) against a comparable scenario merged before this change. The new gauges (in-flight scenarios, active and queued ship merges) are there to tune `merge-ship-threads`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


[TCC-1180]: https://teqplaybv.atlassian.net/browse/TCC-1180?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

## Commits

- `f012d78d` **Darius Wattimena** (2026-08-21): Merge revents scenarios back in parallel on their own threads
  Merging a finished scenario back was fully sequential: checkScenarioProgress
  walked runningScenarios one scenario at a time and merged every ship inline
  before looking at the next one, so one big scenario blocked everything behind
  it.
  
  It also ran on Spring's scheduler, whose pool is 1 and shared with seven other
  @Scheduled methods, so a long merge starved post-processing and trace
  generation - the very steps that finish the data the merge just wrote.
  
  Tracking now owns a revents-tracker thread (ReventsScenarioTracker), and a
  pass only polls and submits: scenarios and the ships inside them merge on two
  bounded pools (ThreadPoolReventsMergeExecutor). The pools are separate because
  a scenario thread waits for its own ships, which would deadlock on one pool.
  Pool capacity is the throttle that keeps merging away from real-time
  processing; Thread.MIN_PRIORITY would be a no-op on Linux without
  -XX:+UseThreadPriorities and privileges.
  
  Because ships now run concurrently:
   - the ship lock is taken for the whole per-ship merge, serialising a ship
     against both other scenarios and live AIS processing. The merge that used
     to be computed twice (once unlocked, once again under the lock) is now
     computed once;
   - the error, merge-failure and statistics collectors are lock-guarded, and
     report sorted rather than in whichever order the ships finished, so a
     scenario's status is reproducible.
  
  Also fixes EndMergeEvent not being published when fetching the ships to merge
  failed retryably, which left ScenarioMeasurement with an open merge - the
  measurement this ticket is judged by.
  
  recalculation.merge-ship-threads=1 with max-concurrent-scenarios=1 reproduces
  the old sequential behaviour.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `25c5b8c6` **Darius Wattimena** (2026-08-24): Address review: start the tracker with the other background workers
  - The tracker no longer starts itself from @PostConstruct. ProcessingService
    starts and stops it alongside the other background workers, so a resumed
    scenario cannot be merged back before the ship and infra caches it reads are
    known to be valid.
  - It runs a plain named daemon Thread instead of a single-thread executor with
    a factory lambda, so the thread's settings are given directly. Shutdown
    joins it and reports what actually happened: the thread is never interrupted
    or killed, it finishes its pass and then sees the flag, so isAlive is the
    honest answer rather than a timed-out boolean.
  - ReventsTrackerSignal is no longer a bean. It belongs to the service that
    owns runningScenarios: signalling is what queueScenario does when that queue
    grows, and the tracker reads it off there, which is what kept the two out of
    a dependency cycle in the first place.
  - Companion objects moved to the top of the class, and the merge pools are
    built with apply rather than also. queueCapacity and threadNamePrefix keep
    their setter calls; Kotlin sees both as read-only properties.
  
  Fixes a race the review caught: runScenario queued the scenario for tracking
  before the caller had saved its RecalculationResult. Now that queueing wakes
  the tracker at once, a pass could reach an already-FINISHED scenario before
  its document existed, merge it, write the finished status into nothing
  (updateStatus does not upsert) and drop it from runningScenarios - after which
  the caller's save restored a stale unfinished status that was no longer being
  tracked. runScenario no longer queues; every caller does so after its save,
  which is what the merge-scenario paths already did.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `0f002594` **Darius Wattimena** (2026-08-25): Merge branch 'develop' into TCC-1180-parallel-scenario-merging
- `f04a302f` **Darius Wattimena** (2026-08-25): Merge branch 'develop' into TCC-1180-parallel-scenario-merging
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt
- `60643233` **Darius Wattimena** (2026-08-25): Repair the develop merge of the parallel merge-back
  The merge left the branch not compiling and, where it did resolve, undid two
  things this branch had changed.
  
   - mergeWindowsOfShip kept this branch's parameter list while its body was
     updated to develop's ShipMergeData/scenarioWindow shape, so the file did not
     compile. Signature and call site now pass both through.
  
   - mergeAndPersist (extracted on develop) came back with the merge-twice
     pattern: merge unlocked, and if the result touched the current ship status,
     take the ship lock and merge again. Its only caller now already holds that
     lock, and ShipLockService is backed by a non-reentrant StampedLock, so the
     nested executeBlocking deadlocked the merge thread against itself - wedging
     a pool thread for good, four such ships wedging the whole ship pool. It
     merges once again and derives refreshShipStatus from that single result.
  
   - EndMergeEvent was published both from the finally in fetchAndMergeDataV2 and
     from develop's line at the end of mergeShipsOfScenario, stamping the
     scenario measurement twice on the success path. Kept the finally.
  
  Also fixed the two parallel-merge tests develop's API changes broke
  (buildMergeEntries now returns ShipMergeData, setService takes properties
  first) and the stray indentation in setService.
  
  `should merge once when the merge touches the current ship status` covers the
  deadlock: it reaches mergeAndPersist with a status-touching result, so the
  unfixed code hung there rather than failing.
  
  ./gradlew test ktlintCheck: 2360 tests, 0 failures.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `398cceba` **Darius Wattimena** (2026-08-25): Hold the live ship lock per merge window, not across a ship's merge
  Merging a ship took ShipLockService for the whole ship: every merge window,
  plus the orphan-visit sweep with its per-port-area visit query and a
  time-window enlargement per orphan. Live AIS processing takes that same lock
  for every message, as do the events and ETA consumers, so a ship being merged
  back was stalled in real time for as long as its whole merge - seconds for a
  busy ship.
  
  Merge-back now locks on two levels, because the two things it excludes cost
  very differently:
  
   - ShipMergeLock is held for a ship's whole merge and only ever blocks another
     merge thread, which is what keeps two scenarios covering the same ship from
     interleaving their windows. Holding it long costs nothing that matters. It
     is a ReentrantLock, so nesting cannot deadlock a merge thread on itself the
     way the non-reentrant StampedLock did.
   - ShipLockService is now taken in exactly one place, mergeAndPersist, around
     a single merge-and-persist. The merge and the persist stay together under
     it: the merge reads the ship's stored entries, so a live message landing
     between the two would be silently overwritten.
  
  Replaying the scenario's events - the slowest part of a ship's merge - already
  ran before any lock was taken and still does.
  
  Covered by `takes the live ship lock per merge window instead of across the
  whole ship merge`, which pins both the per-window granularity and that the
  replay happens outside the lock.
  
  ./gradlew test ktlintCheck: 2361 tests, 0 failures.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `f8e9de69` **Darius Wattimena** (2026-08-25): Lock merge-back exactly per ship instead of on striped locks
  ShipMergeLock striped 4096 ReentrantLocks by shipId hash, copied from
  ShipLockService. That is correct - one ship always maps to one stripe, so two
  merges of it can never overlap - but two unrelated ships sharing a stripe block
  each other for no reason.
  
  Striping earns its place in ShipLockService, which every live AIS message
  contends on and where a map would be real overhead. Merge-back takes this lock
  a handful of times per scenario, so it can afford to be exact: a small map of
  the ships being merged right now, guarded by one mutex, with waiters parked on
  a condition. The map holds at most one entry per merge thread, so it does not
  grow with the number of ships seen.
  
  Kept non-reentrant, but a nested acquisition for the same ship now throws
  instead of hanging - the failure mode the non-reentrant StampedLock gave us.
  
  ShipMergeLockTest covers same-ship serialisation, ordering, release on failure
  and the fail-fast nesting. Its "does not block another ship" case deliberately
  uses two ids that DO collide under the old 4096-way striping (ship-a and
  ship-4168 both land on stripe 3824), so it fails if striping comes back;
  verified by temporarily restoring the striped version.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `53a53be7` **Darius Wattimena** (2026-08-25): Merge branch 'develop' into TCC-1180-parallel-scenario-merging
  Develop split the recalculation phases (PROGRESSING became RUNNING_REVENTS,
  with MERGING and POST_PROCESSING added) and started reporting merge progress,
  which lands squarely on this branch's parallel merge-back.
  
  Resolved:
  
   - the constructor and the test factory each gained a dependency on both sides:
     reventsMergeExecutor here, scenarioMeasurementDataSource on develop.
  
   - develop merged inline in checkScenarioProgress and then called
     enterPostProcessingOrFinish. Kept this branch's submit-to-the-pool, and moved
     develop's post-merge handling into mergeFinishedScenario, which now hands off
     to enterPostProcessingOrFinish instead of resolving the final phase itself.
     The retry branch reports MERGING rather than the old PROGRESSING.
  
   - develop counted merge progress as `index + 1` over a sequential loop. That
     means nothing once ships merge in parallel: they finish out of order, so a
     ship's position in the input is not how far the merge got. Added
     MergeProgressReporter, which hands each finishing ship the next count and
     serialises the persist so the stored value never goes backwards. It also
     moves the scenario into MERGING, since updatePhaseProgress sets the phase.
  
   - both sides had independently added a mockFinishedScenario test helper and
     git kept both, which does not compile. Kept develop's, the one its
     mockMergedScenario and mockPostProcessingScenario build on.
  
  Post-processing tracking composes with async merging as it stands: the
  POST_PROCESSING check sits at the top of the pass, so a scenario waiting on
  post-processing is never submitted for merging again, and a scenario still
  merging is refused by the executor's in-flight guard.
  
  ./gradlew test ktlintCheck: 2386 tests, 0 failures.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `b37c4624` **Darius Wattimena** (2026-08-25): Quiet the per-ship merge logging down to debug
  Merging a scenario logged three lines per ship and one per merge window at INFO,
  which was tolerable when ships merged one at a time and is not now that four
  merge threads interleave: a single scenario produces hundreds of lines that say
  nothing unless you are debugging a specific ship.
  
  Moved to debug, per the "don't log above DEBUG for statements expected to fire
  frequently" rule in CLAUDE.md:
   - "Replayed N event(s) into M entry(s)" - per ship AND per merge window;
   - "Building entries to be merged by replaying events" and "Built N merge
     entries" - per ship;
   - "Trying to get revents scenario with id X" and "Trying revents merge" - per
     scenario on every tracking pass, so once a minute for as long as a scenario
     runs, and now also on every pass a long merge is still in flight.
  
  Kept at INFO the lines that fire once per scenario or record an actual mutation:
  starting a merge, the eligible ship count, entering or skipping post-processing,
  scheduling a follow-up recalculation, and deleting an orphan port visit.
  
  Two of the kept lines did not name their scenario, which was fine on a single
  merge thread and is not when the pools interleave, so they do now.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `59e68427` **Darius Wattimena** (2026-08-25): Stop re-merging scenarios that already finished
  A port recalculation scheduled its automatic follow-up four times, because the
  scenario was merged back four times.
  
  Two things combined:
  
   - runningScenarios was a ConcurrentLinkedQueue. queueScenario adds
     unconditionally and Queue.remove() drops only ONE occurrence, so a scenario
     could sit in it more than once, and every leftover copy was another full
     merge. It is a Set now, so a scenario is tracked once and removing it removes
     it entirely.
  
   - a tracking pass only skipped scenarios in POST_PROCESSING. It never checked
     whether the scenario had already reached a final phase. Revents reports a
     scenario as FINISHED for as long as it exists, so anything still left in
     runningScenarios - a leftover copy, or a merge that threw after scheduling
     the follow-up but before writing the terminal status - was fetched, found
     FINISHED, and merged again on every pass. Each of those merges scheduled
     another follow-up. A pass now stops tracking a scenario whose own persisted
     phase is final.
  
  The second guard is what makes this safe rather than merely less likely: our own
  persisted phase is the only thing that can say the work is done, since revents
  cannot.
  
  Both regression tests were confirmed to fail against the previous code.
  
  TCC-1180
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `867c249b` **Darius Wattimena** (2026-08-25): Merge branch 'develop' into TCC-1180-parallel-scenario-merging

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-21)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F862%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-08-24)

_No comment._

### TeqJoostD — APPROVED (2026-08-27)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

I'm personally not really a fan of using PostConstruct annotations, is there no way to do this different?

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

Is having `false` here correct? If we stop the thread, doesn't that mean we still stopped it later, but just forced killed it?

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

We normally put companion objects at the top instead of at the bottom of the class

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

I believe we can directly provide the thread settings instead of having this lambda?

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsTrackerSignal.kt`

Does this need to be its own bean?

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ThreadPoolReventsMergeExecutor.kt`

Use `apply` instead of `also`? This way we can directly access those setters and fields?

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

Agreed, dropped it. `ProcessingService` now starts the tracker in `onStartProcessing()` next to `automaticRecalculationService`/`storyRepairService`, and already stopped it in `onStopBackgroundProcessing()`.

Side benefit: that is also the readiness fix augment asked for two lines up — `onStartProcessing()` only runs once the ship and infra caches are valid, so a scenario resumed on boot can no longer merge back against a half-loaded cache. `startup()` is guarded with an `AtomicBoolean` because a thread can only be started once.

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

Done — it is a plain named daemon `Thread` now instead of `Executors.newSingleThreadExecutor` with a factory lambda:

```kotlin
private val tracker = Thread(::trackLoop, THREAD_NAME).apply { isDaemon = true }
```

An executor was overkill for one long-lived loop, and this also made the shutdown semantics honest (see your other comment).

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

Good catch — the `false` was misleading, so it is gone.

Nothing force-kills the thread: `shutdown()` sets `shuttingDown`, signals so a waiting pass stops waiting, and the loop exits at the top of its next iteration. The old `awaitTermination` returning `false` on `InterruptedException` then logged "did not stop within 30 seconds", which was wrong — we had not waited 30 seconds, we just stopped waiting.

It now joins and reports what is actually true:

```kotlin
tracker.join(SHUTDOWN_TIMEOUT_MILLIS)
...
if (tracker.isAlive) {
    log.warn { "$THREAD_NAME is still finishing a pass, leaving it to run out as a daemon thread" }
}
```

So if a pass outlives the timeout we say so, and because the thread is a daemon it cannot hold up JVM exit.

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

Moved, in both `ReventsScenarioTracker` and `ThreadPoolReventsMergeExecutor`.

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsTrackerSignal.kt`

No, it does not — removed the `@Service`.

It only existed as a bean to dodge a cycle: `ReventsRecalculationService` signals, `ReventsScenarioTracker` waits, and the tracker already depends on the service. So the signal now just belongs to the service that owns `runningScenarios` — signalling is what `queueScenario` does when that queue grows — and the tracker reads it via `reventsRecalculationService.trackerSignal`. Same cycle-free wiring, one bean fewer.

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ThreadPoolReventsMergeExecutor.kt`

Done, both pools use `apply` now. Two of them had to stay setter calls — `setQueueCapacity` and `setThreadNamePrefix` do not resolve as assignable properties from Kotlin — but the rest is direct.

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

Confirmed and fixed. `updateStatus` is an `updateOneById` with no upsert, so the sequence you describe leaves the scenario stuck: the merge runs, its finished status is written into nothing, `runningScenarios.remove` drops it, and the caller's `save(result)` then restores the unfinished status of a scenario nobody is tracking any more.

`runScenario` no longer queues. Each caller queues after its `save`, which is what the merge-scenario paths (`mergeShipRecalculation`) and `trackScenario` already did — this just makes the recalculate paths consistent with them.

### Darius-Wattimena — 2026-08-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsScenarioTracker.kt`

Fixed, and the same change resolves a review comment asking to drop `@PostConstruct` anyway. `ProcessingService.onStartProcessing()` starts the tracker alongside the other background workers, so it only runs once `staticShipInfoService.isShipCacheValid()` and `infraService.isPomaDataValid()` hold.

## Comments
