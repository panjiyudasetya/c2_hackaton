"""
Abstract base collector with shared frontmatter helpers.
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import yaml

_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Return (metadata_dict, body_text). Body excludes the frontmatter block."""
    m = _FM_RE.match(content)
    if m:
        return yaml.safe_load(m.group(1)) or {}, content[m.end():]
    return {}, content


def render_frontmatter(meta: dict[str, Any], body: str) -> str:
    """Serialize metadata as YAML frontmatter and prepend to body."""
    fm = yaml.dump(meta, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{fm}---\n{body}"


class BaseCollector(ABC):
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def is_configured(self) -> bool:
        """Return True if required credentials are present."""

    @abstractmethod
    def collect(self, **kwargs) -> list[Path]:
        """Fetch data, write markdown files, return list of created file paths."""

    def _write(self, filename: str, content: str) -> Path:
        path = self.output_dir / filename
        path.write_text(content, encoding="utf-8")
        return path
