# decision-intel Chat

A Next.js chat frontend for `decision-intel`, built against the REST API contract in the
"Agent Prompt" spec (job-based collection/pipeline triggers, `/search`, `/links`, `/docs`,
a streaming `/ask`). This is **separate from** the simpler `decision-intel serve` Flask+HTML
chat UI already in this repo — see [Two chat UIs, on purpose](#two-chat-uis-on-purpose) below
for which one to use when.

## What's here

- **Backend**: [`../src/decision_intel/api_server.py`](../src/decision_intel/api_server.py) — a
  new Flask app (run via `decision-intel api`) implementing the exact endpoint contract from the
  spec, on port 8000.
- **Frontend**: this directory — Next.js 14 (App Router), TypeScript, Tailwind, no UI component
  library, no state library. File structure matches what was requested:

  ```
  app/            layout.tsx, page.tsx, globals.css
  components/     ContextPanel, SourcesSection, CollectSection, PipelineSection,
                  ChatWindow, MessageBubble, JobStatus
  lib/            api.ts, useJob.ts, useLocalStorage.ts
  ```

## Running it

**1. Backend** (from the repo root, in the Python environment that already has this
project's dependencies installed):

```bash
decision-intel build   # if you haven't already — needs a vector index to answer questions
decision-intel api     # → http://127.0.0.1:8000
```

**2. Frontend** (from this directory):

```bash
npm install
cp .env.local.example .env.local   # NEXT_PUBLIC_API_URL=http://localhost:8000
npm run dev                        # → http://localhost:3000
```

`npm run build` has been run and passes cleanly (see [Verification](#verification) below) if you
want a production build instead: `npm run build && npm start`.

## Design decisions / where this fills in gaps in the spec

The spec is precise about almost everything, but a few implementation details weren't fully
pinned down and needed a concrete choice:

- **Backend framework**: the spec only fixes the API *contract* (`http://localhost:8000` +
  the listed routes), not the framework. I used **Flask**, matching the rest of this Python
  project (`webapp.py` already uses it) rather than introducing FastAPI as a second web
  framework dependency. Job execution is `threading.Thread` + an in-memory dict — correct for a
  hackathon demo, but **jobs and their results are lost on server restart** and there's no
  cross-process job visibility. A real deployment would want Celery/RQ backed by Redis.
- **Confluence / Notion collect buttons need an identifier to do anything** — `POST
  /collect/confluence` requires `space_keys[]`, `/collect/notion` needs `database_ids[]` or
  `page_ids[]`, but the spec's Collect section doesn't describe an input UI for these. I added a
  small inline text field (comma-separated) above each of those two buttons only; GitHub and JIRA
  need no such input (GitHub collects `all_repos: true`, JIRA runs with an empty JQL filter,
  matching the CLI's own defaults) and stayed single-click.
- **`/ask` empty-question heuristic** (spec: *"a 4xx (not 503) means the index exists"*):
  implemented literally — the backend checks index-existence **before** validating that a
  question was provided, returning `503` if the vector index is missing and `400` if it's
  present but the question is empty. This ordering is what makes the frontend's dummy-POST
  heuristic in `app/page.tsx` actually distinguish the two cases.
- **CORS**: manual headers on every response (`Access-Control-Allow-Origin: *`) rather than
  adding `flask-cors` as a dependency for three header lines — fine for this no-auth internal
  tool, not something to copy into anything handling real credentials.

## Verification

Node.js turned out to be installed on this machine but not on the shell's default `PATH`
(`C:\Program Files\nodejs`) — once that was sorted out:

- `npm install` — clean, no errors (386 packages).
- `npm run build` — **compiled and type-checked successfully, zero errors**, static pages
  generated for `/`.
- Ran `npm start` alongside the real `decision-intel api` backend (already populated from a real
  Jira/Confluence/GitHub collection) and drove it with a real browser: confirmed the sidebar
  collapse/expand rail, source status dots, per-source collect buttons (with the disabled state
  before Confluence/Notion have an input value), the Build button, and a full chat round-trip —
  user bubble → streaming assistant bubble → real backend response.
- The one thing that *didn't* work end-to-end in this environment: the actual AI answer, because
  the configured Anthropic account is out of API credit (`Your credit balance is too low...`).
  This is an account billing issue, not a bug — and it's a good sign in itself, since it proved
  the error path renders correctly in the red error-bubble style instead of hanging or crashing.

## Known follow-ups (not blocking, worth knowing about)

- **`next@14.2.5` has a disclosed security advisory** (`npm install` flags it). The spec pinned
  Next 14 explicitly, so I kept it, but you should bump to the latest patched 14.x release
  (`npm install next@14.2.x` for whatever the newest patch is) before this goes anywhere near the
  public internet — an internal hackathon demo behind no auth is a much lower-stakes place to run
  a vulnerable version than anywhere with real users.
- Real keyboards send Enter fine; only this session's own browser-automation tool had trouble
  synthesizing a native `keydown` event for testing — confirmed by dispatching one manually and
  watching the message send correctly.
- No tests, per the spec ("No tests required for the hackathon").

## Two chat UIs, on purpose

This repo now has two different chat frontends, and that's intentional rather than leftover
duplication:

| | `decision-intel serve` | This Next.js app |
|---|---|---|
| Stack | Flask + hand-written HTML/CSS/JS, no build step | Next.js/TypeScript/Tailwind |
| Backend | `webapp.py`, port 5000 | `api_server.py`, port 8000 |
| Collection/pipeline from the UI | No — CLI only | Yes — buttons + job polling |
| Best for | Quick local use, nothing to install | The richer contract this spec asked for |

Both point at the same underlying `DecisionAgent`/index/graph — pick whichever fits what you're
doing.
