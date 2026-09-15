from __future__ import annotations

import os
import re
from pathlib import Path

# Asumsi BaseCollector ada di .base
from .base import BaseCollector 

def _safe_filename(text: str) -> str:
    return re.sub(r"[^\w\-]", "_", text).strip("_")[:80]

def _md_escape(text: str | None) -> str:
    return (text or "").replace("|", "\\|")

class JiraCollector(BaseCollector):
    """Collects JIRA issues hierarchically and writes them as markdown."""

    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "jira")

    def is_configured(self) -> bool:
        return all(
            os.environ.get(k) for k in ("JIRA_URL", "JIRA_USER", "JIRA_API_TOKEN")
        )

    def _client(self):
        from atlassian import Jira  # lazy import
        return Jira(
            url=os.environ["JIRA_URL"],
            username=os.environ["JIRA_USER"],
            password=os.environ["JIRA_API_TOKEN"],
            cloud=True,
        )

    # ==========================================
    # 1. FUNGSI TARIK SEMUA BOARD
    # ==========================================
    def get_all_boards(self) -> list[dict]:
        """Fetch all Agile boards."""
        jira = self._client()
        boards = []
        start_at = 0
        
        while True:
            # Menggunakan API Agile langsung dari client atlassian
            response = jira.get(f"rest/agile/1.0/board?startAt={start_at}&maxResults=50")
            page_boards = response.get("values", [])
            
            if not page_boards:
                break
                
            boards.extend(page_boards)
            start_at += 50
            
        return boards

    # ==========================================
    # 2. FUNGSI TARIK BOARD DAN CARDS (Tanpa Subtask)
    # ==========================================
    def get_board_cards(self, board_id: int | str) -> list[dict]:
        """Fetch all parent issues (cards) for a specific board."""
        jira = self._client()
        issues = []
        start_at = 0
        
        while True:
            response = jira.get(f"rest/agile/1.0/board/{board_id}/issue?startAt={start_at}&maxResults=50")
            page_issues = response.get("issues", [])
            
            if not page_issues:
                break
                
            # Filter hanya parent card (bukan subtask)
            for issue in page_issues:
                is_subtask = issue.get("fields", {}).get("issuetype", {}).get("subtask", False)
                if not is_subtask:
                    issues.append(issue)
                    
            start_at += 50
            
        return issues

    # ==========================================
    # 3. FUNGSI TARIK BOARD, CARDS, DAN SUBTASKS
    # ==========================================
    def get_board_cards_and_subtasks(self, board_id: int | str) -> list[dict]:
        """Fetch parent cards and embed their full subtask details."""
        jira = self._client()
        # Pakai fungsi nomor 2 untuk dapat parent card
        parent_cards = self.get_board_cards(board_id)
        
        for card in parent_cards:
            subtasks_refs = card.get("fields", {}).get("subtasks", [])
            full_subtasks = []
            
            for sub_ref in subtasks_refs:
                sub_key = sub_ref.get("key")
                if sub_key:
                    # Ambil detail lengkap subtask pakai endpoint issue standard
                    sub_detail = jira.issue(sub_key)
                    full_subtasks.append(sub_detail)
            
            # Embed data subtask lengkap ke dalam object card utama
            card["full_subtasks_data"] = full_subtasks
            
        return parent_cards

    # ==========================================
    # GENERATOR MARKDOWN (Menulis ke File)
    # ==========================================
    def collect_and_write_hierarchy(self, board_id: int | str) -> Path:
        """Contoh cara mengeksekusi fungsi di atas dan menulisnya ke .md"""
        # Ambil data terstruktur (Board > Card > Subtask)
        cards = self.get_board_cards_and_subtasks(board_id)
        
        lines: list[str] = [f"# Data Board {board_id}", ""]
        
        for card in cards:
            key = card["key"]
            summary = card.get("fields", {}).get("summary", "")
            lines.append(f"## 🎫 Card: [{key}] {summary}")
            
            subtasks = card.get("full_subtasks_data", [])
            if not subtasks:
                lines.append("- *(Tidak ada subtask)*")
            else:
                lines.append("- **Subtasks:**")
                for sub in subtasks:
                    sub_key = sub["key"]
                    sub_summary = sub.get("fields", {}).get("summary", "")
                    sub_status = sub.get("fields", {}).get("status", {}).get("name", "")
                    lines.append(f"  - 📝 [{sub_key}] {sub_summary} (Status: {sub_status})")
            
            lines.append("\n---\n")
            
        filename = f"board_{board_id}_hierarchy.md"
        return self._write(filename, "\n".join(lines))