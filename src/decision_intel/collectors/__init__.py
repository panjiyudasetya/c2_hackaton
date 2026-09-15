"""Collector package.

Two collector styles live here:

- Class-based (`BaseCollector` subclasses), each with a `.collect()` that
  returns `list[Path]`: `GitHubCollector`, the legacy board-hierarchy
  `JiraCollector` (in `jira_collector.py`), and `NotionCollector`.
- Function-based "Phase 1" collectors that write frontmatter-tagged
  markdown via `frontmatter_utils.write_document`: `confluence.collect()`
  and `jira.collect()` (module-level, not classes — import the submodule
  itself, e.g. `from .collectors import confluence`).

Note: `jira_collector.JiraCollector` (legacy) and `jira.collect` (tagged)
are two different things that happen to both talk to Jira — the former
predates the frontmatter-tagging convention and is kept only for the
existing board-hierarchy dump; new work should use `jira.collect`.
"""
from .github import GitHubCollector
from .jira_collector import JiraCollector
from .notion import NotionCollector

__all__ = ["GitHubCollector", "JiraCollector", "NotionCollector"]
