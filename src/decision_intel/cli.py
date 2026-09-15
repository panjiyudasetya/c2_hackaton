"""
CLI entry point for decision-intel.
"""

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
    "--output-dir", "-o",
    default="output",
    show_default=True,
    help="Root directory for generated markdown files and indexes.",
)
@click.pass_context
def cli(ctx: click.Context, output_dir: str) -> None:
    """decision-intel: collect, enrich, index, and query engineering documents."""
    ctx.ensure_object(dict)
    ctx.obj["output_dir"] = Path(output_dir)


# ── Phase 1: GitHub collection ─────────────────────────────────────────────────

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
    all_repos: bool,
    state: str,
    max_issues: int,
    max_prs: int,
    max_commits: int,
    since: str | None,
) -> None:
    """Fetch GitHub issues and pull requests and write one markdown file each."""
    from .collectors import GitHubCollector

    collector = GitHubCollector(ctx.obj["output_dir"])
    if not collector.is_configured():
        console.print("[red]GitHub not configured.[/red] Set GITHUB_TOKEN in .env")
        raise SystemExit(1)

    selected_repos: list[str]

    if repos:
        selected_repos = list(repos)
    elif all_repos:
        with console.status("Fetching repository list…"):
            available = collector.list_all_repos()
        selected_repos = [name for name, _, _ in available]
        console.print(f"Collecting from [bold]{len(selected_repos)}[/bold] repositories.")
    else:
        # Interactive checkbox picker
        try:
            import questionary
        except ImportError:
            console.print("[red]questionary not installed.[/red] Run: pip install questionary")
            raise SystemExit(1)

        with console.status("Fetching repository list…"):
            available = collector.list_all_repos()

        if not available:
            console.print("No repositories found.")
            raise SystemExit(0)

        choices = [
            questionary.Choice(
                title=f"{name}  ({pushed})  {desc}" if desc else f"{name}  ({pushed})",
                value=name,
            )
            for name, pushed, desc in available
        ]
        selected = questionary.checkbox(
            "Select repositories to collect (space to select, enter to confirm):",
            choices=choices,
        ).ask()

        if not selected:
            console.print("No repositories selected.")
            raise SystemExit(0)

        selected_repos = selected

    with console.status(f"Collecting from {len(selected_repos)} repo(s)…"):
        paths = collector.collect(
            repos=selected_repos,
            state=state,
            max_issues=max_issues,
            max_prs=max_prs,
            max_commits=max_commits,
            since=since,
        )

    _print_results("GitHub", paths)


# ── JIRA (Phase 6 — frontmatter not yet added) ────────────────────────────────

@cli.command()
@click.option("--jql", default="", help="JQL query. Default: all issues, newest first.")
@click.option("--max", "max_results", default=50, show_default=True)
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


# ── Notion (Phase 6) ──────────────────────────────────────────────────────────

@cli.command()
@click.option("--database", "database_ids", multiple=True, help="Notion database ID.")
@click.option("--page", "page_ids", multiple=True, help="Notion page ID.")
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


# ── Phase 2: enrich ───────────────────────────────────────────────────────────

@cli.command()
@click.pass_context
def enrich(ctx: click.Context) -> None:
    """
    Scan all collected markdown files for cross-source links and write them
    into each file's frontmatter explicit_links field.
    """
    from .enricher import enrich_all

    output_dir = ctx.obj["output_dir"]
    if not output_dir.exists():
        console.print(f"[red]Output directory not found:[/red] {output_dir}")
        raise SystemExit(1)

    with console.status("Enriching frontmatter with cross-source links…"):
        results = enrich_all(output_dir)

    total_new = sum(results.values())
    files_touched = sum(1 for v in results.values() if v > 0)
    console.print(
        f"Enriched [bold]{len(results)}[/bold] files — "
        f"[bold]{files_touched}[/bold] gained links — "
        f"[bold]{total_new}[/bold] new links total."
    )


# ── Phase 3: index ────────────────────────────────────────────────────────────

@cli.command()
@click.pass_context
def index(ctx: click.Context) -> None:
    """
    Chunk all collected markdown files and embed them into a local ChromaDB
    vector store for semantic search.

    Downloads the all-MiniLM-L6-v2 model on first run (~90 MB).
    """
    from .indexer import build_index

    output_dir = ctx.obj["output_dir"]
    console.print("Building vector index (may download embedding model on first run)…")

    with console.status("Embedding and indexing chunks…"):
        n = build_index(output_dir)

    console.print(f"Indexed [bold]{n}[/bold] chunks into [cyan]{output_dir}/.chromadb[/cyan]")


# ── Phase 4: graph ────────────────────────────────────────────────────────────

@cli.command()
@click.option("--no-heuristics", is_flag=True,
              help="Skip temporal and author proximity heuristic edges.")
@click.pass_context
def graph(ctx: click.Context, no_heuristics: bool) -> None:
    """
    Build the cross-source metadata graph from frontmatter explicit_links
    and (optionally) temporal/author proximity heuristics.
    """
    from .graph import add_heuristic_edges, build_graph

    output_dir = ctx.obj["output_dir"]

    with console.status("Building metadata graph from explicit links…"):
        explicit = build_graph(output_dir)
    console.print(f"Graph: [bold]{explicit}[/bold] explicit edge pairs inserted.")

    if not no_heuristics:
        with console.status("Adding heuristic edges (temporal + author proximity)…"):
            heuristic = add_heuristic_edges(output_dir)
        console.print(f"Graph: [bold]{heuristic}[/bold] heuristic edges added.")

    console.print(f"Graph saved to [cyan]{output_dir}/.graph.db[/cyan]")


# ── Agent tool subcommands (called by the Claude Code SDK agent via Bash) ──────

@cli.command("search")
@click.argument("query")
@click.option("--top-k", default=10, show_default=True)
@click.option("--source", default=None, type=click.Choice(["github", "jira", "notion", "confluence"]))
@click.option("--since", default=None, metavar="YYYY-MM-DD")
@click.pass_context
def search_cmd(ctx: click.Context, query: str, top_k: int, source: str | None, since: str | None) -> None:
    """Semantic search over collected documents. Outputs JSON."""
    import json
    from .indexer import search_documents
    output_dir = ctx.obj["output_dir"]
    results = search_documents(query=query, output_dir=output_dir, top_k=top_k, source=source, since=since)
    click.echo(json.dumps([r.to_dict() for r in results], indent=2) if results else "[]")


@cli.command("links")
@click.argument("doc_id")
@click.option("--min-confidence", default=0.5, show_default=True)
@click.option("--depth", default=2, show_default=True)
@click.pass_context
def links_cmd(ctx: click.Context, doc_id: str, min_confidence: float, depth: int) -> None:
    """Follow cross-source links from a document. Outputs JSON."""
    import json
    from .graph import get_linked_documents
    output_dir = ctx.obj["output_dir"]
    results = get_linked_documents(doc_id=doc_id, output_dir=output_dir, min_confidence=min_confidence, depth=depth)
    click.echo(json.dumps([r.to_dict() for r in results], indent=2) if results else "[]")


@cli.command("read-doc")
@click.argument("file_path")
def read_doc_cmd(file_path: str) -> None:
    """Read the full content of a collected markdown file."""
    path = Path(file_path)
    if not path.exists():
        click.echo(f"File not found: {file_path}", err=True)
        raise SystemExit(1)
    content = path.read_text(encoding="utf-8")
    click.echo(content[:20_000] + "\n\n_[truncated]_" if len(content) > 20_000 else content)


# ── Phase 5: ask ──────────────────────────────────────────────────────────────

@cli.command()
@click.argument("question")
@click.option("--save/--no-save", default=True, show_default=True,
              help="Save the answer to output/answers/.")
@click.pass_context
def ask(ctx: click.Context, question: str, save: bool) -> None:
    """
    Ask the AI agent a question about decisions in the collected documents.

    Example: decision-intel ask "Why was Kafka chosen for the streaming pipeline?"
    """
    from .agent import DecisionAgent

    output_dir = ctx.obj["output_dir"]
    chroma_dir = output_dir / ".chromadb"
    graph_db   = output_dir / ".graph.db"

    if not chroma_dir.exists():
        console.print(
            "[red]Vector index not found.[/red] Run [bold]decision-intel index[/bold] first."
        )
        raise SystemExit(1)
    if not graph_db.exists():
        console.print(
            "[yellow]Graph not found — running without cross-source linking.[/yellow] "
            "Run [bold]decision-intel graph[/bold] to enable it."
        )

    agent = DecisionAgent(output_dir)
    console.print(f"\n[bold]Question:[/bold] {question}\n")

    with console.status("Agent is reasoning…"):
        answer = agent.ask(question)

    console.print(answer)

    if save:
        answers_dir = output_dir / "answers"
        answers_dir.mkdir(exist_ok=True)
        from datetime import datetime
        slug = "".join(c if c.isalnum() else "_" for c in question.lower())[:60]
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        out = answers_dir / f"{ts}_{slug}.md"
        out.write_text(f"# {question}\n\n{answer}", encoding="utf-8")
        console.print(f"\n[dim]Saved to {out}[/dim]")


# ── convenience: build = enrich + index + graph ───────────────────────────────

@cli.command()
@click.pass_context
def build(ctx: click.Context) -> None:
    """Run enrich → index → graph in sequence (convenience command after collection)."""
    ctx.invoke(enrich)
    ctx.invoke(index)
    ctx.invoke(graph)


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
