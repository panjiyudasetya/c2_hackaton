# decision-intel

A local RAG pipeline that collects engineering artefacts from GitHub, JIRA, Notion, and Confluence, indexes them into a semantic vector store and a cross-source metadata graph, then answers "why was this decision made?" questions using Claude — with no separate Anthropic API key required.

---

## How it works

```
collect → enrich → index → graph → ask
```

| Phase | Command | What it does |
|-------|---------|--------------|
| 1 | `github` / `jira` / `confluence` / `notion` | Fetches issues, PRs, and pages; writes one Markdown file each with YAML frontmatter |
| 2 | `enrich` | Scans every `.md` file for cross-source link patterns (`PTO-123`, `Closes #42`, etc.) and writes them into each file's `explicit_links` frontmatter field |
| 3 | `index` | Chunks and embeds all Markdown files into a local ChromaDB vector store (`all-MiniLM-L6-v2`, ~90 MB download on first run) |
| 4 | `graph` | Builds a SQLite metadata graph from explicit links plus temporal/author-proximity heuristics |
| 5 | `ask` | Searches the vector store and graph locally, then sends the collected evidence to Claude in a single prompt — no tool-call round-trips |

All data is local. The only outbound calls are to GitHub/JIRA/Confluence/Notion APIs during collection and to Claude during `ask`.

---

## Requirements

- Python 3.11+
- [Claude Code](https://claude.ai/code) installed and signed in (`claude auth login`)
- Credentials for whichever sources you want to collect (see `.env.example`) — e.g. a GitHub personal access token for GitHub collection, an Atlassian API token for JIRA/Confluence

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=ghp_...
JIRA_URL=https://yourorg.atlassian.net
JIRA_USER=you@yourorg.com
JIRA_API_TOKEN=...
CONFLUENCE_URL=https://yourorg.atlassian.net
CONFLUENCE_USER=you@yourorg.com
CONFLUENCE_API_TOKEN=...     # can reuse JIRA_API_TOKEN — same Atlassian Cloud auth
NOTION_TOKEN=secret_...
```

---

## Quick start

```bash
# 1. Collect GitHub data (interactive repo picker)
decision-intel github

# 2. Build the index and graph in one step
decision-intel build

# 3. Ask a question
decision-intel ask "Why was chunk-processing added to the fact_bunkering query?"
```

`build` is a convenience alias for `enrich` + `index` + `graph` run in sequence.

---

## Sample question and answer

**Question**

```
decision-intel ask "Why was chunk-processing added to the fact_bunkering query, and what was slow about the original approach?"
```

**Answer** (abbreviated)

> ### Summary
> Chunk-processing *logging* was added in PR #730 as a diagnostic side-effect of fixing a slow `fact_bunkering` query. The primary fix addressed a missing `deleted_timestamp IS null` predicate that prevented index usage; the logging was added so future "stuck" DAG runs could be distinguished from genuinely slow queries.
>
> ### Decisions made
> - **Add `deleted_timestamp IS null` to joins in `proceed.sql`** → without it, Postgres couldn't use partial indexes, forcing full sequential scans (~27 s scanning 1.3 M+ rows for a 459-row result).
> - **Apply the identical predicate fix to `bunkering_components.sql`** → keeps the QC query in sync with the fact-table logic it validates.
> - **Add logging in `process_data_in_chunks`** → a previous "stuck" DAG run was actually a slow query stalled inside `fetchmany()`, not a hang; without visibility the two cases looked identical.
>
> ### Supporting evidence
> - `github:teqplay/dataflow_dag_core:pr:730` — Main PR with the predicate fix and chunk-processing logs.
> - `github:teqplay/dataflow_dag_core:pr:731` — Release PR 1.54.1 changelog confirming the rationale.
>
> ### Gaps
> - No JIRA ticket content for PTO-2866 was in the collected data; incident business context is missing.
> - The actual diff for `process_data_in_chunks` was not retrieved, so chunk size and prior chunking history are unclear.

Answers are saved automatically to `output/answers/`.

---

## All commands

```
decision-intel --help
```

| Command | Description |
|---------|-------------|
| `github` | Collect GitHub issues and PRs |
| `jira` | Collect JIRA issues |
| `confluence` | Collect Confluence pages |
| `notion` | Collect Notion pages |
| `enrich` | Scan collected files for cross-source links |
| `index` | Embed chunks into ChromaDB vector store |
| `graph` | Build SQLite cross-source metadata graph |
| `build` | Run enrich + index + graph in sequence |
| `ask "QUESTION"` | Ask the AI agent a decision question |
| `search "QUERY"` | Raw semantic search (JSON output, for scripting) |
| `links "DOC_ID"` | Follow graph links from a document (JSON output) |
| `read-doc "PATH"` | Print full content of a collected Markdown file |

### Useful flags

```bash
# Collect specific repos instead of the interactive picker
decision-intel github --repo owner/repo1 --repo owner/repo2

# Collect only recent items
decision-intel github --since 2026-01-01 --max-prs 100

# Collect JIRA issues matching a JQL query
decision-intel jira --jql "project = PTO AND updated >= -30d"

# Collect one or more Confluence spaces
decision-intel confluence --space TC --space PTO

# Skip heuristic graph edges (author/date proximity)
decision-intel graph --no-heuristics

# Don't save the answer to disk
decision-intel ask "..." --no-save

# Use a custom output directory
decision-intel --output-dir /path/to/output ask "..."
```

---

## Output layout

```
output/
  github/
    owner_repo/
      issues/     issue_N_title.md
      prs/        pr_N_title.md
  jira/
    PROJ/         PROJ-123.md
  confluence/
    SPACE/        pageid_title.md
  notion/
    database_id/  page-title.md
  answers/        20260915_124620_question_slug.md
  .chromadb/      (vector store — managed by ChromaDB)
  .graph.db       (SQLite metadata graph)
```

Each collected `.md` file has a YAML frontmatter block with at least `id`, `source`, `type`, `title`, `url`, and `explicit_links`, plus source-specific fields (e.g. `repo`/`labels` for GitHub, `project`/`issuetype` for JIRA, `space` for Confluence, `database_id` for Notion).

---

## Authentication

The agent uses your existing **Claude Code** session — the same credentials used by the `claude` CLI. No separate `ANTHROPIC_API_KEY` is needed. If you have one set in `.env` it is temporarily removed before the agent call and restored afterwards.

To sign in: `claude auth login`

---

## Good questions to ask

Questions that work well are ones where the answer lives across multiple PRs, issues, or tickets:

- *"Why was X library/framework chosen over alternatives?"*
- *"What was the incident that caused Y to be rewritten?"*
- *"Who decided to deprecate Z, and what was the stated reason?"*
- *"Why does the DAG retry N times — was that a deliberate choice?"*
- *"What problem was the chunking approach in fact_bunkering solving?"*

Questions that return thin answers typically lack collected source data — run `decision-intel search "topic"` first to check what's in the index.
