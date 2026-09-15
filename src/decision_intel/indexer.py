"""
Phase 3 — Chunking, embedding, and vector search via ChromaDB.

Documents are split at ``##`` section headings, embedded with a local
sentence-transformers model, and stored in a persistent ChromaDB collection.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .collectors.base import parse_frontmatter

_CHROMA_COLLECTION = "decision_intel"
_EMBED_MODEL = "all-MiniLM-L6-v2"
_MIN_CHUNK_CHARS = 120
_MAX_CHUNK_CHARS = 6000  # ChromaDB document size limit


# ── chunking ──────────────────────────────────────────────────────────────────

def chunk_document(path: Path) -> list[dict[str, Any]]:
    """
    Split a markdown file at ``##`` headings.

    Returns a list of::

        {
            "id":       str,            # "<doc_id>::chunk-N"
            "text":     str,            # chunk content
            "metadata": dict,           # frontmatter fields + chunk_index
        }
    """
    content = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)

    doc_id: str = meta.get("id") or f"file:{path.stem}"

    # Split on lines that start a level-2 heading
    raw_sections = re.split(r"\n(?=## )", body)

    chunks: list[dict[str, Any]] = []
    for i, section in enumerate(raw_sections):
        text = section.strip()
        if len(text) < _MIN_CHUNK_CHARS:
            continue

        chunk_meta: dict[str, Any] = {
            "doc_id":         doc_id,
            "source":         meta.get("source", "unknown"),
            "type":           meta.get("type", "unknown"),
            "title":          str(meta.get("title", "")),
            "author":         str(meta.get("author", "")),
            "date":           str(meta.get("date", "")),
            "url":            str(meta.get("url", "")),
            "file_path":      str(path),
            "explicit_links": ",".join(meta.get("explicit_links") or []),
            "chunk_index":    i,
        }

        chunks.append({
            "id":       f"{doc_id}::chunk-{i}",
            "text":     text[:_MAX_CHUNK_CHARS],
            "metadata": chunk_meta,
        })

    return chunks


# ── chroma factory ────────────────────────────────────────────────────────────

def _get_chroma_collection(chroma_dir: Path):
    """Return (or create) the persistent ChromaDB collection."""
    import chromadb
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

    ef = SentenceTransformerEmbeddingFunction(model_name=_EMBED_MODEL)
    client = chromadb.PersistentClient(path=str(chroma_dir))
    return client.get_or_create_collection(
        name=_CHROMA_COLLECTION,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"},
    )


# ── indexing ──────────────────────────────────────────────────────────────────

def build_index(output_dir: Path, chroma_dir: Path | None = None) -> int:
    """
    Walk all ``.md`` files under *output_dir*, chunk them, embed them,
    and upsert into ChromaDB.

    Returns total number of chunks indexed.
    """
    if chroma_dir is None:
        chroma_dir = output_dir / ".chromadb"

    collection = _get_chroma_collection(chroma_dir)

    all_chunks: list[dict[str, Any]] = []
    for md_file in sorted(output_dir.rglob("*.md")):
        all_chunks.extend(chunk_document(md_file))

    if not all_chunks:
        return 0

    # Upsert in batches of 64 to avoid memory spikes
    batch_size = 64
    for start in range(0, len(all_chunks), batch_size):
        batch = all_chunks[start : start + batch_size]
        collection.upsert(
            ids=[c["id"] for c in batch],
            documents=[c["text"] for c in batch],
            metadatas=[c["metadata"] for c in batch],
        )

    return len(all_chunks)


# ── search ────────────────────────────────────────────────────────────────────

class SearchResult:
    __slots__ = ("chunk_id", "doc_id", "text", "score", "metadata")

    def __init__(
        self,
        chunk_id: str,
        doc_id: str,
        text: str,
        score: float,
        metadata: dict[str, Any],
    ) -> None:
        self.chunk_id = chunk_id
        self.doc_id   = doc_id
        self.text     = text
        self.score    = score
        self.metadata = metadata

    def to_dict(self) -> dict[str, Any]:
        return {
            "chunk_id": self.chunk_id,
            "doc_id":   self.doc_id,
            "text":     self.text,
            "score":    round(self.score, 4),
            **{k: v for k, v in self.metadata.items() if k != "doc_id"},
        }


def search_documents(
    query: str,
    output_dir: Path,
    chroma_dir: Path | None = None,
    top_k: int = 10,
    source: str | None = None,
    since: str | None = None,
) -> list[SearchResult]:
    """
    Semantic search over the ChromaDB collection.

    Args:
        query:      Natural-language question.
        output_dir: Root output directory (used to locate chroma_dir).
        chroma_dir: Explicit path to ChromaDB data; defaults to output_dir/.chromadb.
        top_k:      Number of results to return.
        source:     Filter by source (``github``, ``jira``, ``notion``, ``confluence``).
        since:      Filter to documents with date >= this string (``YYYY-MM-DD``).
    """
    if chroma_dir is None:
        chroma_dir = output_dir / ".chromadb"

    collection = _get_chroma_collection(chroma_dir)

    where_clauses: list[dict] = []
    if source:
        where_clauses.append({"source": source})
    if since:
        where_clauses.append({"date": {"$gte": since}})

    where: dict | None = None
    if len(where_clauses) == 1:
        where = where_clauses[0]
    elif len(where_clauses) > 1:
        where = {"$and": where_clauses}

    kwargs: dict[str, Any] = {"query_texts": [query], "n_results": top_k}
    if where:
        kwargs["where"] = where

    results = collection.query(**kwargs)

    output: list[SearchResult] = []
    ids       = results["ids"][0]
    documents = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    for chunk_id, text, distance, meta in zip(ids, documents, distances, metadatas):
        score = 1.0 - distance  # cosine: distance 0 = identical, convert to similarity
        output.append(
            SearchResult(
                chunk_id=chunk_id,
                doc_id=meta.get("doc_id", ""),
                text=text,
                score=score,
                metadata=meta,
            )
        )

    return output
