"""
REST API backend for the decision-intel Next.js chat frontend (see
``frontend/``). Runs on port 8000 by default.

This is a separate, richer surface from ``webapp.py``'s minimal Flask+HTML
chat UI: collection and pipeline steps are triggered as background jobs
(poll ``GET /jobs/{id}`` for status) instead of blocking the request, and
there are extra query endpoints (``/search``, ``/links``, ``/docs``) for a
frontend that wants to do more than just ask questions.

No authentication -- this is an internal tool, matching the frontend spec.
"""

from __future__ import annotations

import json
import threading
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from flask import Flask, Response, jsonify, request

# ── background job registry ───────────────────────────────────────────────────
# In-memory only -- jobs (and their results) don't survive a server restart.
# That's fine for a hackathon tool; a real deployment would want a persistent
# queue (Celery/RQ) instead.

_JOBS_LOCK = threading.Lock()
_JOBS: dict[str, "Job"] = {}


@dataclass
class Job:
    id: str
    status: str = "running"  # "running" | "done" | "failed"
    result: Any = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {"job_id": self.id, "status": self.status, "result": self.result, "error": self.error}


def _run_job(fn: Callable[[], Any]) -> str:
    """Run *fn* on a background thread, tracked under a new job id."""
    job = Job(id=uuid.uuid4().hex)
    with _JOBS_LOCK:
        _JOBS[job.id] = job

    def target() -> None:
        try:
            job.result = fn()
            job.status = "done"
        except Exception as exc:  # noqa: BLE001 -- surface to the job's `error` field, not a 500
            job.error = str(exc)
            job.status = "failed"

    threading.Thread(target=target, daemon=True).start()
    return job.id


def create_api_app(output_dir: str | Path = "output") -> Flask:
    output_dir = Path(output_dir)
    app = Flask(__name__)

    # ── CORS ──────────────────────────────────────────────────────────────────
    # The Next.js frontend runs on a different origin/port (typically
    # localhost:3000) than this API (localhost:8000), so every response needs
    # CORS headers. No credentials are used, so a wildcard origin is fine for
    # this internal tool.
    @app.after_request
    def _add_cors_headers(resp):
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        return resp

    @app.route("/", defaults={"_path": ""}, methods=["OPTIONS"])
    @app.route("/<path:_path>", methods=["OPTIONS"])
    def _preflight(_path):
        return ("", 204)

    # ── meta ──────────────────────────────────────────────────────────────────

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/sources/status")
    def sources_status():
        from .collectors import ConfluenceCollector, GitHubCollector, JiraCollector, NotionCollector

        return jsonify({
            "github": {"configured": GitHubCollector(output_dir).is_configured()},
            "jira": {"configured": JiraCollector(output_dir).is_configured()},
            "confluence": {"configured": ConfluenceCollector(output_dir).is_configured()},
            "notion": {"configured": NotionCollector(output_dir).is_configured()},
        })

    # ── picker lists (for the frontend's repo/board checklists) ────────────────

    @app.get("/sources/github/repos")
    def github_repos():
        from .collectors import GitHubCollector

        collector = GitHubCollector(output_dir)
        if not collector.is_configured():
            return jsonify({"error": "GitHub not configured"}), 503
        repos = collector.list_all_repos()
        return jsonify([{"full_name": name, "pushed_at": pushed, "description": desc} for name, pushed, desc in repos])

    @app.get("/sources/jira/boards")
    def jira_boards():
        from .collectors import JiraCollector

        collector = JiraCollector(output_dir)
        if not collector.is_configured():
            return jsonify({"error": "JIRA not configured"}), 503
        return jsonify(collector.list_all_boards())

    # ── collection ──────────────────────────────────────────────────────────────

    @app.post("/collect/github")
    def collect_github():
        from .collectors import GitHubCollector

        body = request.get_json(silent=True) or {}
        collector = GitHubCollector(output_dir)

        def run():
            repos = body.get("repos") or None
            if body.get("all_repos"):
                repos = [name for name, _, _ in collector.list_all_repos()]
            if not repos:
                raise ValueError("Provide repos[] or set all_repos=true")
            return [str(p) for p in collector.collect(
                repos=repos,
                state=body.get("state", "all"),
                max_issues=body.get("max_issues", 1000),
                max_prs=body.get("max_prs", 1000),
                max_commits=body.get("max_commits", 50),
                since=body.get("since"),
            )]

        return jsonify({"job_id": _run_job(run)})

    @app.post("/collect/jira")
    def collect_jira():
        from .collectors import JiraCollector

        body = request.get_json(silent=True) or {}
        collector = JiraCollector(output_dir)
        boards = body.get("boards") or []

        def run():
            if boards:
                return [str(p) for p in collector.collect_boards(
                    boards, max_results_per_board=body.get("max_results", 1000)
                )]
            return [str(p) for p in collector.collect(
                jql=body.get("jql", ""),
                max_results=body.get("max_results", 50),
            )]

        return jsonify({"job_id": _run_job(run)})

    @app.post("/collect/confluence")
    def collect_confluence():
        from .collectors import ConfluenceCollector

        body = request.get_json(silent=True) or {}
        collector = ConfluenceCollector(output_dir)

        def run():
            space_keys = body.get("space_keys") or []
            if not space_keys:
                raise ValueError("space_keys[] is required")
            return [str(p) for p in collector.collect(
                space_keys=space_keys,
                max_pages=body.get("max_pages", 100),
            )]

        return jsonify({"job_id": _run_job(run)})

    @app.post("/collect/notion")
    def collect_notion():
        from .collectors import NotionCollector

        body = request.get_json(silent=True) or {}
        collector = NotionCollector(output_dir)

        def run():
            database_ids = body.get("database_ids") or []
            page_ids = body.get("page_ids") or []
            if not database_ids and not page_ids:
                raise ValueError("Provide database_ids[] or page_ids[]")
            return [str(p) for p in collector.collect(
                database_ids=database_ids,
                page_ids=page_ids,
                max_pages=body.get("max_pages", 50),
            )]

        return jsonify({"job_id": _run_job(run)})

    # ── pipeline ────────────────────────────────────────────────────────────────

    @app.post("/pipeline/enrich")
    def pipeline_enrich():
        from .enricher import enrich_all

        return jsonify({"job_id": _run_job(lambda: enrich_all(output_dir))})

    @app.post("/pipeline/index")
    def pipeline_index():
        from .indexer import build_index

        return jsonify({"job_id": _run_job(lambda: build_index(output_dir))})

    @app.post("/pipeline/graph")
    def pipeline_graph():
        from .graph import add_heuristic_edges, build_graph

        body = request.get_json(silent=True) or {}
        no_heuristics = bool(body.get("no_heuristics"))

        def run():
            explicit = build_graph(output_dir)
            heuristic = 0 if no_heuristics else add_heuristic_edges(output_dir)
            return {"explicit_edges": explicit, "heuristic_edges": heuristic}

        return jsonify({"job_id": _run_job(run)})

    @app.post("/pipeline/build")
    def pipeline_build():
        from .enricher import enrich_all
        from .graph import add_heuristic_edges, build_graph
        from .indexer import build_index

        def run():
            enrich_result = enrich_all(output_dir)
            indexed_chunks = build_index(output_dir)
            explicit = build_graph(output_dir)
            heuristic = add_heuristic_edges(output_dir)
            return {
                "enrich": enrich_result,
                "indexed_chunks": indexed_chunks,
                "explicit_edges": explicit,
                "heuristic_edges": heuristic,
            }

        return jsonify({"job_id": _run_job(run)})

    # ── jobs ──────────────────────────────────────────────────────────────────

    @app.get("/jobs/<job_id>")
    def get_job(job_id: str):
        job = _JOBS.get(job_id)
        if not job:
            return jsonify({"error": "job not found"}), 404
        return jsonify(job.to_dict())

    @app.get("/jobs")
    def list_jobs():
        return jsonify([j.to_dict() for j in _JOBS.values()])

    # ── query ─────────────────────────────────────────────────────────────────

    @app.get("/search")
    def search():
        from .indexer import search_documents

        q = request.args.get("q", "")
        if not q:
            return jsonify({"error": "q is required"}), 400
        top_k = int(request.args.get("top_k", 10))
        source = request.args.get("source") or None
        since = request.args.get("since") or None
        results = search_documents(query=q, output_dir=output_dir, top_k=top_k, source=source, since=since)
        return jsonify([r.to_dict() for r in results])

    @app.get("/links/<path:doc_id>")
    def links(doc_id: str):
        from .graph import get_linked_documents

        min_confidence = float(request.args.get("min_confidence", 0.5))
        depth = int(request.args.get("depth", 2))
        results = get_linked_documents(
            doc_id=doc_id, output_dir=output_dir, min_confidence=min_confidence, depth=depth
        )
        return jsonify([r.to_dict() for r in results])

    @app.get("/docs")
    def docs():
        raw_path = request.args.get("path", "")
        if not raw_path:
            return jsonify({"error": "path is required"}), 400

        p = Path(raw_path)
        try:
            # Reject anything outside output_dir -- this endpoint takes an
            # arbitrary path from the client, so path traversal must be blocked.
            p.resolve().relative_to(output_dir.resolve())
        except ValueError:
            return jsonify({"error": "path must be within the output directory"}), 400

        if not p.is_file():
            return jsonify({"error": "file not found"}), 404
        return jsonify({"path": str(p), "content": p.read_text(encoding="utf-8")})

    # ── agent ─────────────────────────────────────────────────────────────────

    @app.post("/ask")
    def ask():
        from .agent import DecisionAgent

        body = request.get_json(silent=True) or {}
        question = (body.get("question") or "").strip()
        save = body.get("save", True)

        # Order matters here: the frontend's "is the index ready?" check is a
        # dummy POST with an empty question, expecting 503 (index missing) vs.
        # a 4xx like this 400 (index present, just a bad request) -- see
        # frontend/lib/api.ts / app/page.tsx.
        if not (output_dir / ".chromadb").exists():
            return jsonify({"error": "Vector index not found. Run the pipeline first."}), 503
        if not question:
            return jsonify({"error": "question is required"}), 400

        agent = DecisionAgent(output_dir)

        def generate():
            chunks: list[str] = []
            try:
                for chunk in agent.ask_stream(question):
                    chunks.append(chunk)
                    yield f"data: {json.dumps({'token': chunk})}\n\n"
            except Exception as exc:  # noqa: BLE001 -- surface to the chat UI, don't 500 mid-stream
                yield f"data: {json.dumps({'error': str(exc)})}\n\n"
                return

            answer = "".join(chunks)
            saved_to = None
            if save:
                answers_dir = output_dir / "answers"
                answers_dir.mkdir(parents=True, exist_ok=True)
                slug = "".join(c if c.isalnum() else "_" for c in question.lower())[:60]
                ts = time.strftime("%Y%m%d_%H%M%S")
                out = answers_dir / f"{ts}_{slug}.md"
                out.write_text(f"# {question}\n\n{answer}", encoding="utf-8")
                saved_to = str(out)

            yield f"data: {json.dumps({'answer': answer, 'saved_to': saved_to})}\n\n"

        return Response(
            generate(),
            mimetype="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    @app.post("/jira/readiness")
    def jira_readiness():
        from .agent import TicketReadinessReviewer
        from .agent.readiness_reviewer import save_and_diff

        body = request.get_json(silent=True) or {}
        issue_key = (body.get("issue_key") or "").strip()
        if not issue_key:
            return jsonify({"error": "issue_key is required"}), 400

        reviewer = TicketReadinessReviewer(output_dir)

        def generate():
            chunks: list[str] = []
            try:
                for chunk in reviewer.review_stream(issue_key):
                    chunks.append(chunk)
                    yield f"data: {json.dumps({'token': chunk})}\n\n"
            except Exception as exc:  # noqa: BLE001 -- surface to the chat UI, don't 500 mid-stream
                yield f"data: {json.dumps({'error': str(exc)})}\n\n"
                return

            report = "".join(chunks)
            diff = save_and_diff(output_dir, issue_key, report)
            yield f"data: {json.dumps({'history': diff})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"

        return Response(
            generate(),
            mimetype="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    @app.post("/jira/comment")
    def jira_comment():
        from .collectors import JiraCollector

        body = request.get_json(silent=True) or {}
        issue_key = (body.get("issue_key") or "").strip()
        comment = (body.get("comment") or "").strip()
        if not issue_key or not comment:
            return jsonify({"error": "issue_key and comment are required"}), 400

        collector = JiraCollector(output_dir)
        if not collector.is_configured():
            return jsonify({"error": "JIRA not configured"}), 503

        try:
            url = collector.post_comment(issue_key, comment)
        except Exception as exc:  # noqa: BLE001
            return jsonify({"error": str(exc)}), 502

        return jsonify({"posted": True, "url": url})

    return app


def main() -> None:
    import os

    from dotenv import load_dotenv

    load_dotenv()
    output_dir = os.environ.get("DECISION_INTEL_OUTPUT_DIR", "output")
    host = os.environ.get("DECISION_INTEL_API_HOST", "127.0.0.1")
    port = int(os.environ.get("DECISION_INTEL_API_PORT", "8000"))

    app = create_api_app(output_dir)
    print(f"decision-intel API running at http://{host}:{port}  (output dir: {output_dir})")
    app.run(host=host, port=port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
