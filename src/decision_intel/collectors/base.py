"""Abstract base collector."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


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
