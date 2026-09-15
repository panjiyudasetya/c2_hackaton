"""
GitHub collector — issues, PRs, and commit messages with YAML frontmatter.
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path

from .base import BaseCollector, render_frontmatter


def _safe(text: str) -> str:
    return re.sub(r"[^\w\-]", "_", text).strip("_")[:60]


def _is_bot(login: str | None) -> bool:
    return bool(login and login.endswith("[bot]"))


class GitHubCollector(BaseCollector):
    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "github")

    def is_configured(self) -> bool:
        return bool(os.environ.get("GITHUB_TOKEN"))

    def _client(self):
        from github import Github
        return Github(os.environ["GITHUB_TOKEN"])

    # ── repo listing (used by CLI picker) ─────────────────────────────────────

    def list_all_repos(self, max_repos: int = 200) -> list[tuple[str, str]]:
        """Return (full_name, last_pushed_date) for every accessible repo."""
        gh = self._client()
        results: list[tuple[str, str]] = []
        for repo in gh.get_user().get_repos(sort="pushed", direction="desc"):
            pushed = str(repo.pushed_at.date()) if repo.pushed_at else ""
            results.append((repo.full_name, pushed))
            if len(results) >= max_repos:
                break
        return results

    # ── main entry point ───────────────────────────────────────────────────────

    def collect(
        self,
        repos: list[str],
        state: str = "all",
        max_issues: int = 50,
        max_prs: int = 50,
        max_commits: int = 50,
        since: str | None = None,
        **kwargs,
    ) -> list[Path]:
        """
        Collect issues and PRs from the given repos and write one .md file each.

        Args:
            repos:       List of ``owner/repo`` strings.
            state:       ``open``, ``closed``, or ``all``.
            max_issues:  Max issues per repo.
            max_prs:     Max pull requests per repo.
            max_commits: Max commits listed per PR (messages only, no diffs).
            since:       Only include items updated after this date (``YYYY-MM-DD``).
        """
        since_dt = datetime.strptime(since, "%Y-%m-%d") if since else None
        gh = self._client()

        created: list[Path] = []
        for repo_name in repos:
            repo = gh.get_repo(repo_name)
            repo_dir = self.output_dir / _safe(repo_name)
            (repo_dir / "issues").mkdir(parents=True, exist_ok=True)
            (repo_dir / "prs").mkdir(parents=True, exist_ok=True)

            # Issues (skip PRs and bot authors)
            issue_kwargs: dict = {"state": state}
            if since_dt:
                issue_kwargs["since"] = since_dt
            count = 0
            for issue in repo.get_issues(**issue_kwargs):
                if count >= max_issues:
                    break
                if issue.pull_request or _is_bot(issue.user.login if issue.user else None):
                    continue
                created.append(self._write_issue(issue, repo_name, repo_dir / "issues"))
                count += 1

            # Pull requests
            pr_kwargs: dict = {"state": state}
            count = 0
            for pr in repo.get_pulls(**pr_kwargs):
                if count >= max_prs:
                    break
                if _is_bot(pr.user.login if pr.user else None):
                    continue
                if since_dt and pr.updated_at and pr.updated_at < since_dt:
                    break
                created.append(self._write_pr(pr, repo_name, repo_dir / "prs", max_commits))
                count += 1

        return created

    # ── issue ──────────────────────────────────────────────────────────────────

    def _write_issue(self, issue, repo_name: str, out_dir: Path) -> Path:
        author = issue.user.login if issue.user else "unknown"
        labels = [lb.name for lb in issue.labels]
        date = str(issue.created_at)[:10] if issue.created_at else ""

        meta = {
            "id":             f"github:{repo_name}:issue:{issue.number}",
            "source":         "github",
            "type":           "issue",
            "repo":           repo_name,
            "number":         issue.number,
            "title":          issue.title,
            "author":         author,
            "state":          issue.state,
            "date":           date,
            "url":            issue.html_url,
            "labels":         labels,
            "explicit_links": [],  # populated by enricher (Phase 2)
        }

        body_lines: list[str] = [
            f"# Issue #{issue.number}: {issue.title}",
            "",
            f"**Repo:** {repo_name}  ",
            f"**URL:** {issue.html_url}  ",
            f"**State:** {issue.state} | **Author:** {author}  ",
            f"**Created:** {date}  ",
        ]
        if issue.closed_at:
            body_lines.append(f"**Closed:** {str(issue.closed_at)[:10]}  ")
        if labels:
            body_lines.append(f"**Labels:** {', '.join(labels)}  ")

        body_lines += ["", "## Body", "", issue.body or "_No body._", ""]

        comments = list(issue.get_comments())
        if comments:
            body_lines += ["## Comments", ""]
            for c in comments:
                if _is_bot(c.user.login if c.user else None):
                    continue
                body_lines += [
                    f"### {c.user.login if c.user else 'unknown'} — {str(c.created_at)[:10]}",
                    "",
                    c.body or "",
                    "",
                ]

        filename = f"issue_{issue.number}_{_safe(issue.title)}.md"
        path = out_dir / filename
        path.write_text(render_frontmatter(meta, "\n".join(body_lines)), encoding="utf-8")
        return path

    # ── pull request ───────────────────────────────────────────────────────────

    def _write_pr(self, pr, repo_name: str, out_dir: Path, max_commits: int) -> Path:
        author = pr.user.login if pr.user else "unknown"
        labels = [lb.name for lb in pr.labels]
        date = str(pr.created_at)[:10] if pr.created_at else ""
        merged = str(pr.merged_at)[:10] if pr.merged_at else None

        # Pre-populate linked issues from body (Closes #N / Fixes #N patterns)
        linked_issues = [
            f"github:{repo_name}:issue:{n}"
            for n in re.findall(r"(?:closes?|fixes?|resolves?)\s+#(\d+)", pr.body or "", re.I)
        ]

        meta = {
            "id":             f"github:{repo_name}:pr:{pr.number}",
            "source":         "github",
            "type":           "pull_request",
            "repo":           repo_name,
            "number":         pr.number,
            "title":          pr.title,
            "author":         author,
            "state":          pr.state,
            "date":           date,
            "merged_at":      merged,
            "base_branch":    pr.base.ref if pr.base else None,
            "head_branch":    pr.head.ref if pr.head else None,
            "url":            pr.html_url,
            "labels":         labels,
            "linked_issues":  linked_issues,
            "explicit_links": linked_issues[:],  # seeded with linked issues
        }

        body_lines: list[str] = [
            f"# PR #{pr.number}: {pr.title}",
            "",
            f"**Repo:** {repo_name}  ",
            f"**URL:** {pr.html_url}  ",
            f"**State:** {pr.state} | **Author:** {author}  ",
            f"**Base ← Head:** `{pr.base.ref if pr.base else '?'}` ← `{pr.head.ref if pr.head else '?'}`  ",
            f"**Created:** {date}  ",
        ]
        if merged:
            body_lines.append(f"**Merged:** {merged}  ")
        if labels:
            body_lines.append(f"**Labels:** {', '.join(labels)}  ")

        body_lines += ["", "## Description", "", pr.body or "_No description._", ""]

        # Commits — full messages (subject + body), no diffs
        commits = list(pr.get_commits())
        shown = commits[:max_commits]
        if shown:
            body_lines += ["## Commits", ""]
            for c in shown:
                sha = c.sha[:8]
                full_msg = (c.commit.message or "").strip()
                subject, _, body = full_msg.partition("\n")
                c_author = c.commit.author.name if c.commit.author else "unknown"
                c_date = str(c.commit.author.date)[:10] if c.commit.author else ""
                body_lines.append(f"- `{sha}` **{c_author}** ({c_date}): {subject}")
                if body.strip():
                    for line in body.strip().splitlines():
                        body_lines.append(f"  {line}")
            if len(commits) > max_commits:
                body_lines.append(f"- _… {len(commits) - max_commits} more commits not shown_")
            body_lines.append("")

        # Reviews (summary-level — APPROVED / CHANGES_REQUESTED with top-level comment)
        reviews = list(pr.get_reviews())
        if reviews:
            body_lines += ["## Reviews", ""]
            for r in reviews:
                reviewer = r.user.login if r.user else "unknown"
                submitted = str(r.submitted_at)[:10] if r.submitted_at else ""
                body_lines += [
                    f"### {reviewer} — {r.state} ({submitted})",
                    "",
                    (r.body or "").strip() or "_No comment._",
                    "",
                ]

        # Inline review comments (per-line code threads — most technical discussion lives here)
        review_comments = list(pr.get_review_comments())
        if review_comments:
            body_lines += ["## Review Comments", ""]
            for rc in review_comments:
                if _is_bot(rc.user.login if rc.user else None):
                    continue
                path_hint = f" on `{rc.path}`" if rc.path else ""
                body_lines += [
                    f"### {rc.user.login if rc.user else 'unknown'} — {str(rc.created_at)[:10]}{path_hint}",
                    "",
                    rc.body or "",
                    "",
                ]

        # General PR comments (non-review thread comments)
        comments = list(pr.get_issue_comments())
        if comments:
            body_lines += ["## Comments", ""]
            for c in comments:
                if _is_bot(c.user.login if c.user else None):
                    continue
                body_lines += [
                    f"### {c.user.login if c.user else 'unknown'} — {str(c.created_at)[:10]}",
                    "",
                    c.body or "",
                    "",
                ]

        filename = f"pr_{pr.number}_{_safe(pr.title)}.md"
        path = out_dir / filename
        path.write_text(render_frontmatter(meta, "\n".join(body_lines)), encoding="utf-8")
        return path
