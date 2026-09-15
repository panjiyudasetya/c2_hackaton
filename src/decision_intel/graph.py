"""
Phase 4 — Metadata graph: cross-source link adjacency in SQLite.

Builds an adjacency table from frontmatter ``explicit_links`` fields and
augments it with heuristic edges based on temporal and author proximity.
"""

from __future__ import annotations

import sqlite3
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from .collectors.base import parse_frontmatter

_SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    id        TEXT PRIMARY KEY,
    source    TEXT,
    type      TEXT,
    title     TEXT,
    date      TEXT,
    author    TEXT,
    file_path TEXT
);

CREATE TABLE IF NOT EXISTS edges (
    from_id    TEXT,
    to_id      TEXT,
    link_type  TEXT,    -- explicit | temporal | author
    confidence REAL,
    PRIMARY KEY (from_id, to_id)
);
"""

# ── helpers ───────────────────────────────────────────────────────────────────

def _open_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript(_SCHEMA)
    conn.commit()
    return conn


def _parse_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


# ── build from frontmatter ─────────────────────────────────────────────────────

def build_graph(output_dir: Path, db_path: Path | None = None) -> int:
    """
    Walk all ``.md`` files under *output_dir*, read frontmatter, and populate
    the SQLite graph with explicit edges from ``explicit_links``.

    Returns the total number of explicit edges inserted.
    """
    if db_path is None:
        db_path = output_dir / ".graph.db"

    conn = _open_db(db_path)
    edge_count = 0

    for md_file in sorted(output_dir.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        if not meta:
            continue

        doc_id = meta.get("id")
        if not doc_id:
            continue

        conn.execute(
            """INSERT OR REPLACE INTO documents (id, source, type, title, date, author, file_path)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                doc_id,
                meta.get("source", ""),
                meta.get("type", ""),
                str(meta.get("title", "")),
                str(meta.get("date", "")),
                str(meta.get("author", "")),
                str(md_file),
            ),
        )

        for linked_id in (meta.get("explicit_links") or []):
            conn.execute(
                """INSERT OR REPLACE INTO edges (from_id, to_id, link_type, confidence)
                   VALUES (?, ?, 'explicit', 1.0)""",
                (doc_id, linked_id),
            )
            # Bidirectional
            conn.execute(
                """INSERT OR REPLACE INTO edges (from_id, to_id, link_type, confidence)
                   VALUES (?, ?, 'explicit', 1.0)""",
                (linked_id, doc_id),
            )
            edge_count += 1

    conn.commit()
    conn.close()
    return edge_count


# ── heuristic edges ────────────────────────────────────────────────────────────

def add_heuristic_edges(output_dir: Path, db_path: Path | None = None) -> int:
    """
    Add low-confidence edges based on temporal and author proximity.

    - Same author within 14 days → confidence based on date gap
    - Same author (regardless of date) → confidence 0.3

    Returns number of heuristic edges added.
    """
    if db_path is None:
        db_path = output_dir / ".graph.db"

    conn = _open_db(db_path)

    rows = conn.execute(
        "SELECT id, date, author FROM documents WHERE author != '' ORDER BY date"
    ).fetchall()

    docs: list[dict[str, Any]] = [dict(r) for r in rows]
    added = 0

    for i, doc_a in enumerate(docs):
        for doc_b in docs[i + 1 :]:
            if doc_a["id"] == doc_b["id"]:
                continue

            same_author = (
                doc_a["author"]
                and doc_b["author"]
                and doc_a["author"] == doc_b["author"]
            )
            date_a = _parse_date(doc_a["date"])
            date_b = _parse_date(doc_b["date"])

            confidence: float = 0.0

            if same_author and date_a and date_b:
                gap = abs((date_a - date_b).days)
                if gap <= 14:
                    # Linear decay: gap 0 → confidence 1.0, gap 14 → confidence 0.0
                    confidence = max(0.1, 1.0 - gap / 14)
                    link_type = "temporal"
                else:
                    confidence = 0.3
                    link_type = "author"
            elif same_author:
                confidence = 0.3
                link_type = "author"

            if confidence <= 0:
                continue

            # Only insert if no explicit edge already exists
            for from_id, to_id in [(doc_a["id"], doc_b["id"]), (doc_b["id"], doc_a["id"])]:
                existing = conn.execute(
                    "SELECT confidence FROM edges WHERE from_id=? AND to_id=?",
                    (from_id, to_id),
                ).fetchone()
                if not existing:
                    conn.execute(
                        """INSERT OR IGNORE INTO edges (from_id, to_id, link_type, confidence)
                           VALUES (?, ?, ?, ?)""",
                        (from_id, to_id, link_type, confidence),
                    )
                    added += 1

    conn.commit()
    conn.close()
    return added


# ── document lookup ───────────────────────────────────────────────────────────

def get_document_file_path(doc_id: str, output_dir: Path, db_path: Path | None = None) -> str | None:
    """Return the on-disk file_path for *doc_id*, or None if not found."""
    if db_path is None:
        db_path = output_dir / ".graph.db"
    if not db_path.exists():
        return None
    conn = _open_db(db_path)
    row = conn.execute("SELECT file_path FROM documents WHERE id = ?", (doc_id,)).fetchone()
    conn.close()
    return row["file_path"] if row else None


# ── query ──────────────────────────────────────────────────────────────────────

class LinkedDocument:
    __slots__ = ("doc_id", "link_type", "confidence", "hops")

    def __init__(self, doc_id: str, link_type: str, confidence: float, hops: int) -> None:
        self.doc_id     = doc_id
        self.link_type  = link_type
        self.confidence = confidence
        self.hops       = hops

    def to_dict(self) -> dict[str, Any]:
        return {
            "doc_id":     self.doc_id,
            "link_type":  self.link_type,
            "confidence": round(self.confidence, 3),
            "hops":       self.hops,
        }


def get_linked_documents(
    doc_id: str,
    output_dir: Path,
    db_path: Path | None = None,
    min_confidence: float = 0.5,
    depth: int = 2,
) -> list[LinkedDocument]:
    """
    BFS traversal of the graph from *doc_id* up to *depth* hops.

    Returns documents reachable within *depth* hops with confidence
    >= *min_confidence*, ordered by confidence descending.
    """
    if db_path is None:
        db_path = output_dir / ".graph.db"

    if not db_path.exists():
        return []

    conn = _open_db(db_path)

    visited: dict[str, LinkedDocument] = {}
    frontier = {doc_id}

    for hop in range(1, depth + 1):
        if not frontier:
            break
        next_frontier: set[str] = set()
        for fid in frontier:
            rows = conn.execute(
                """SELECT to_id, link_type, confidence FROM edges
                   WHERE from_id = ? AND confidence >= ?
                   ORDER BY confidence DESC""",
                (fid, min_confidence),
            ).fetchall()
            for row in rows:
                to_id = row["to_id"]
                if to_id == doc_id or to_id in visited:
                    continue
                visited[to_id] = LinkedDocument(
                    doc_id=to_id,
                    link_type=row["link_type"],
                    confidence=row["confidence"],
                    hops=hop,
                )
                next_frontier.add(to_id)
        frontier = next_frontier

    conn.close()
    return sorted(visited.values(), key=lambda d: (-d.confidence, d.hops))
