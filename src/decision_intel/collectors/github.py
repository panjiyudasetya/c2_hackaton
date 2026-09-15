"""GitHub collector — fetches issues and PRs (with commits and reviews) as markdown."""

from __future__ import annotations

import os
import re
from pathlib import Path

from .base import BaseCollector


def _safe_filename(text: str) -> str:
    return re.sub(r"[^\w\-]", "_", text).strip("_")[:80]


class GitHubCollector(BaseCollector):
    """Collects GitHub issues and pull requests and writes them as markdown."""

    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "github")

    def is_configured(self) -> bool:
        return bool(os.environ.get("GITHUB_TOKEN"))

    def _client(self):
        from github import Github  # lazy import

        return Github(os.environ["GITHUB_TOKEN"])

    def collect(
        self,
        repos: list[str] | None = None,
        state: str = "all",
        max_issues: int = 30,
        max_prs: int = 30,
        **kwargs,
    ) -> list[Path]:
        """
        Fetch issues and PRs from the given repos and write one .md file each.

        Args:
            repos: List of ``owner/repo`` strings. Falls back to ``GITHUB_ORG`` env var
                   to list the org's repos (top 10 by last push).
            state: ``open``, ``closed``, or ``all``.
            max_issues: Max issues per repo.
            max_prs: Max pull requests per repo.
        """
        gh = self._client()

        if not repos:
            org_name = os.environ.get("GITHUB_ORG", "")
            if org_name:
                org = gh.get_organization(org_name)
                repos = [r.full_name for r in org.get_repos(sort="pushed")[:10]]
            else:
                raise ValueError(
                    "Provide repos=[...] or set GITHUB_ORG in your environment."
                )

        created: list[Path] = []
        for repo_name in repos:
            repo = gh.get_repo(repo_name)
            repo_dir = self.output_dir / _safe_filename(repo_name)
            repo_dir.mkdir(parents=True, exist_ok=True)

            for issue in repo.get_issues(state=state)[:max_issues]:
                if issue.pull_request:
                    continue  # PRs surface via get_issues; skip here
                path = self._write_issue(issue, repo_name, repo_dir)
                created.append(path)

            for pr in repo.get_pulls(state=state)[:max_prs]:
                path = self._write_pr(pr, repo_name, repo_dir)
                created.append(path)

        return created

    # ── issues ────────────────────────────────────────────────────────────────

    def _write_issue(self, issue, repo_name: str, out_dir: Path) -> Path:
        labels = [lb.name for lb in issue.labels]
        comments = list(issue.get_comments())

        lines: list[str] = [
            f"# Issue #{issue.number}: {issue.title}",
            "",
            f"**Repo:** {repo_name}  ",
            f"**URL:** {issue.html_url}  ",
            f"**State:** {issue.state}  ",
            f"**Author:** {issue.user.login if issue.user else 'unknown'}  ",
            f"**Created:** {str(issue.created_at)[:10]}  ",
        ]
        if issue.closed_at:
            lines.append(f"**Closed:** {str(issue.closed_at)[:10]}  ")
        if labels:
            lines.append(f"**Labels:** {', '.join(labels)}  ")

        lines += ["", "## Body", "", issue.body or "_No body._", ""]

        if comments:
            lines += ["## Comments", ""]
            for c in comments:
                lines += [
                    f"### {c.user.login if c.user else 'unknown'} — {str(c.created_at)[:10]}",
                    "",
                    c.body or "",
                    "",
                ]

        filename = f"issue_{issue.number}_{_safe_filename(issue.title)}.md"
        path = out_dir / filename
        path.write_text("\n".join(lines), encoding="utf-8")
        return path

    # ── pull requests ──────────────────────────────────────────────────────────

    def _write_pr(self, pr, repo_name: str, out_dir: Path) -> Path:
        labels = [lb.name for lb in pr.labels]
        commits = list(pr.get_commits())
        reviews = list(pr.get_reviews())
        comments = list(pr.get_issue_comments())

        lines: list[str] = [
            f"# PR #{pr.number}: {pr.title}",
            "",
            f"**Repo:** {repo_name}  ",
            f"**URL:** {pr.html_url}  ",
            f"**State:** {pr.state}  ",
            f"**Author:** {pr.user.login if pr.user else 'unknown'}  ",
            f"**Base → Head:** `{pr.base.ref}` ← `{pr.head.ref}`  ",
            f"**Created:** {str(pr.created_at)[:10]}  ",
        ]
        if pr.merged_at:
            lines.append(f"**Merged:** {str(pr.merged_at)[:10]}  ")
        if labels:
            lines.append(f"**Labels:** {', '.join(labels)}  ")

        lines += ["", "## Description", "", pr.body or "_No description._", ""]

        if commits:
            lines += ["## Commits", ""]
            for c in commits:
                sha = c.sha[:8]
                msg = (c.commit.message or "").split("\n")[0]
                author = c.commit.author.name if c.commit.author else "unknown"
                date = str(c.commit.author.date)[:10] if c.commit.author else ""
                lines.append(f"- `{sha}` **{author}** ({date}): {msg}")
            lines.append("")

        if reviews:
            lines += ["## Reviews", ""]
            for r in reviews:
                reviewer = r.user.login if r.user else "unknown"
                state = r.state
                submitted = str(r.submitted_at)[:10] if r.submitted_at else ""
                body = (r.body or "").strip()
                lines += [f"### {reviewer} — {state} ({submitted})", "", body or "_No comment._", ""]

        if comments:
            lines += ["## Comments", ""]
            for c in comments:
                lines += [
                    f"### {c.user.login if c.user else 'unknown'} — {str(c.created_at)[:10]}",
                    "",
                    c.body or "",
                    "",
                ]

        filename = f"pr_{pr.number}_{_safe_filename(pr.title)}.md"
        path = out_dir / filename
        path.write_text("\n".join(lines), encoding="utf-8")
        return path
