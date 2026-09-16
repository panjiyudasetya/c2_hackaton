"""
Flask backend for the decision-intel chat UI.

Wraps ``DecisionAgent.ask_stream()`` behind a small HTTP API so a browser
can chat with the local RAG pipeline (vector index + metadata graph) that
``decision-intel build`` produces. The frontend lives in ``web/static/`` and
is served directly by this same app -- no separate frontend server needed.

Run it with:

    python -m decision_intel.webapp
    # or, equivalently:
    decision-intel serve
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from flask import Flask, Response, jsonify, request, send_from_directory

_STATIC_DIR = Path(__file__).parent / "web" / "static"


def create_app(output_dir: str | Path = "output") -> Flask:
    """Build the Flask app. ``output_dir`` must match the one collection/
    build was run against (the default ``output`` matches the CLI's own
    default -- see ``--output-dir`` on ``decision-intel``)."""
    output_dir = Path(output_dir)
    app = Flask(__name__, static_folder=None)

    # Created lazily on first request rather than at import time, so the
    # module can be imported (e.g. for tests) without ANTHROPIC_API_KEY set.
    _agent_holder: dict = {}

    def _get_agent():
        if "agent" not in _agent_holder:
            from .agent import DecisionAgent
            _agent_holder["agent"] = DecisionAgent(output_dir)
        return _agent_holder["agent"]

    @app.get("/")
    def index():
        return send_from_directory(_STATIC_DIR, "index.html")

    @app.get("/<path:filename>")
    def static_files(filename):
        return send_from_directory(_STATIC_DIR, filename)

    @app.get("/api/status")
    def status():
        """Lets the frontend show a clear setup message instead of a silent failure."""
        return jsonify({
            "index_ready": (output_dir / ".chromadb").exists(),
            "graph_ready": (output_dir / ".graph.db").exists(),
            "output_dir": str(output_dir),
        })

    @app.post("/api/ask")
    def ask():
        data = request.get_json(silent=True) or {}
        question = (data.get("question") or "").strip()
        if not question:
            return jsonify({"error": "question is required"}), 400
        if not (output_dir / ".chromadb").exists():
            return jsonify({
                "error": "Vector index not found. Run `decision-intel build` after collecting data."
            }), 409

        def generate():
            try:
                for chunk in _get_agent().ask_stream(question):
                    yield f"data: {json.dumps({'text': chunk})}\n\n"
            except Exception as exc:  # noqa: BLE001 -- surface to the chat UI, don't 500 mid-stream
                yield f"data: {json.dumps({'error': str(exc)})}\n\n"
            finally:
                yield f"data: {json.dumps({'done': True})}\n\n"

        return Response(
            generate(),
            mimetype="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    return app


def main() -> None:
    from dotenv import load_dotenv
    load_dotenv()

    output_dir = os.environ.get("DECISION_INTEL_OUTPUT_DIR", "output")
    host = os.environ.get("DECISION_INTEL_HOST", "127.0.0.1")
    port = int(os.environ.get("DECISION_INTEL_PORT", "5000"))

    app = create_app(output_dir)
    print(f"decision-intel chat running at http://{host}:{port}  (output dir: {output_dir})")
    app.run(host=host, port=port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
