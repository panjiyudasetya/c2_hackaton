"""Small helpers shared by the Phase 1 (frontmatter-tagged) collectors."""
from __future__ import annotations

import os
import re


def safe_filename(text: str) -> str:
    """Turn arbitrary titles into a filesystem-safe filename fragment."""
    cleaned = re.sub(r"[^\w\-]", "_", text or "").strip("_")[:80]
    return cleaned or "untitled"


def require_env(name: str) -> str:
    """Fetch a required environment variable or fail with a clear message
    pointing at .env.example, instead of a bare KeyError."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            "Set it in your .env file (copy .env.example to .env and fill it in)."
        )
    return value
