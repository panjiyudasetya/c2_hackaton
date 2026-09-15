"""
Collector package.

All collectors are `BaseCollector` subclasses with a `.collect()` that
returns `list[Path]`, and write frontmatter-tagged markdown via
`base.render_frontmatter` (id/source/type/.../explicit_links) so Phase 2/3/4
(enrich/index/graph) can build the link graph and vector index on top of
them.
"""
from decision_intel.collectors.confluence import ConfluenceCollector
from decision_intel.collectors.github import GitHubCollector
from decision_intel.collectors.jira import JiraCollector
from decision_intel.collectors.notion import NotionCollector

__all__ = ["ConfluenceCollector", "GitHubCollector", "JiraCollector", "NotionCollector"]
