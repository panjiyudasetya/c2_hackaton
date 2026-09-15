"""CLI entry point — run collectors and write markdown output."""

from __future__ import annotations

from pathlib import Path

import click
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()
console = Console()


@click.group()
@click.option(
    "--output-dir",
    "-o",
    default="output",
    show_default=True,
    help="Root directory for generated markdown files.",
)
@click.pass_context
def cli(ctx: click.Context, output_dir: str) -> None:
    """decision-intel: collect JIRA, GitHub, and Notion data as markdown files."""
    ctx.ensure_object(dict)
    ctx.obj["output_dir"] = Path(output_dir)


# ── JIRA ──────────────────────────────────────────────────────────────────────

@cli.command()
@click.option("--jql", default="", help="JQL query string. Default: all issues, newest first.")
@click.option("--max", "max_results", default=50, show_default=True, help="Max issues to fetch.")
@click.pass_context
def jira(ctx: click.Context, jql: str, max_results: int) -> None:
    """Fetch JIRA issues and write one markdown file per issue."""
    from .collectors import JiraCollector

    collector = JiraCollector(ctx.obj["output_dir"])
    if not collector.is_configured():
        console.print("[red]JIRA not configured.[/red] Set JIRA_URL, JIRA_USER, JIRA_API_TOKEN.")
        raise SystemExit(1)

    with console.status("Fetching JIRA issues…"):
        paths = collector.collect(jql=jql, max_results=max_results)

    _print_results("JIRA", paths)


# ── Confluence & JIRA, frontmatter-tagged (Phase 1) ─────────────────────────────
# These write one .md file per page/issue with a YAML "tag" frontmatter block
# (id/source/type/.../explicit_links), matching the convention already used
# for GitHub docs — see decision_intel/frontmatter_utils.py.

@cli.command("collect-confluence")
@click.option("--space", "space_key", required=True, help="Confluence space key, e.g. TC.")
@click.option("--out", "out_dir", default=None, help="Output dir. Default: <output-dir>/confluence.")
@click.pass_context
def collect_confluence(ctx: click.Context, space_key: str, out_dir: str | None) -> None:
    """Fetch every page in a Confluence space as frontmatter-tagged markdown."""
    from .collectors import confluence

    target = out_dir or str(ctx.obj["output_dir"] / "confluence")
    try:
        with console.status(f"Fetching Confluence space {space_key}…"):
            paths = confluence.collect(space_key, target)
    except RuntimeError as exc:
        console.print(f"[red]Confluence not configured:[/red] {exc}")
        raise SystemExit(1)

    _print_results("Confluence", [Path(p) for p in paths])


@cli.command("collect-jira")
@click.option("--boards", "board_names", multiple=True, required=True, help="Board name (substring match). Repeatable.")
@click.option("--out", "out_dir", default=None, help="Output dir. Default: <output-dir>/jira.")
@click.pass_context
def collect_jira(ctx: click.Context, board_names: tuple[str, ...], out_dir: str | None) -> None:
    """Fetch every card (and subtasks) from the given JIRA boards as
    frontmatter-tagged markdown, one file per issue."""
    from .collectors import jira as jira_tagged

    target = out_dir or str(ctx.obj["output_dir"] / "jira")
    try:
        with console.status(f"Fetching JIRA boards {list(board_names)}…"):
            paths = jira_tagged.collect(list(board_names), target)
    except RuntimeError as exc:
        console.print(f"[red]JIRA not configured:[/red] {exc}")
        raise SystemExit(1)

    _print_results("JIRA (tagged)", [Path(p) for p in paths])


# ── GitHub ────────────────────────────────────────────────────────────────────

@cli.command()
@click.option(
    "--repo",
    "repos",
    multiple=True,
    help="owner/repo to collect from. Can be repeated. Defaults to GITHUB_ORG repos.",
)
@click.option(
    "--state",
    default="all",
    type=click.Choice(["open", "closed", "all"]),
    show_default=True,
)
@click.option("--max-issues", default=30, show_default=True)
@click.option("--max-prs", default=30, show_default=True)
@click.pass_context
def github(
    ctx: click.Context,
    repos: tuple[str, ...],
    state: str,
    max_issues: int,
    max_prs: int,
) -> None:
    """Fetch GitHub issues and pull requests and write one markdown file each."""
    from .collectors import GitHubCollector

    collector = GitHubCollector(ctx.obj["output_dir"])
    if not collector.is_configured():
        console.print("[red]GitHub not configured.[/red] Set GITHUB_TOKEN.")
        raise SystemExit(1)

    with console.status("Fetching GitHub issues and PRs…"):
        paths = collector.collect(
            repos=list(repos) or None,
            state=state,
            max_issues=max_issues,
            max_prs=max_prs,
        )

    _print_results("GitHub", paths)


# ── Notion ────────────────────────────────────────────────────────────────────

@cli.command()
@click.option(
    "--database",
    "database_ids",
    multiple=True,
    help="Notion database ID. Can be repeated.",
)
@click.option(
    "--page",
    "page_ids",
    multiple=True,
    help="Notion page ID to fetch directly. Can be repeated.",
)
@click.option("--max-pages", default=50, show_default=True)
@click.pass_context
def notion(
    ctx: click.Context,
    database_ids: tuple[str, ...],
    page_ids: tuple[str, ...],
    max_pages: int,
) -> None:
    """Fetch Notion pages from databases or by ID and write one markdown file each."""
    from .collectors import NotionCollector

    if not database_ids and not page_ids:
        console.print("[yellow]Provide at least one --database or --page ID.[/yellow]")
        raise SystemExit(1)

    collector = NotionCollector(ctx.obj["output_dir"])
    if not collector.is_configured():
        console.print("[red]Notion not configured.[/red] Set NOTION_TOKEN.")
        raise SystemExit(1)

    with console.status("Fetching Notion pages…"):
        paths = collector.collect(
            database_ids=list(database_ids),
            page_ids=list(page_ids),
            max_pages=max_pages,
        )

    _print_results("Notion", paths)


# ── all ───────────────────────────────────────────────────────────────────────

@cli.command("all")
@click.option("--jql", default="", help="JQL for JIRA.")
@click.option("--repo", "repos", multiple=True, help="owner/repo for GitHub.")
@click.option("--database", "database_ids", multiple=True, help="Notion database ID.")
@click.option("--page", "page_ids", multiple=True, help="Notion page ID.")
@click.pass_context
def collect_all(
    ctx: click.Context,
    jql: str,
    repos: tuple[str, ...],
    database_ids: tuple[str, ...],
    page_ids: tuple[str, ...],
) -> None:
    """Run all configured collectors in sequence."""
    ctx.invoke(jira, jql=jql, max_results=50)
    ctx.invoke(github, repos=repos, state="all", max_issues=30, max_prs=30)
    if database_ids or page_ids:
        ctx.invoke(notion, database_ids=database_ids, page_ids=page_ids, max_pages=50)


# ── helpers ───────────────────────────────────────────────────────────────────

def _print_results(source: str, paths: list[Path]) -> None:
    table = Table(title=f"{source} — {len(paths)} file(s) written", show_lines=False)
    table.add_column("File", style="cyan", no_wrap=False)
    for p in paths:
        table.add_row(str(p))
    console.print(table)


if __name__ == "__main__":
    # Required for `python -m decision_intel.cli ...` to actually dispatch
    # into the Click group — without this, running the module just defines
    # the commands and exits with no output and no error (which is exactly
    # what was happening before this line existed).
    cli()
