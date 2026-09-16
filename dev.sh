#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

# ── load .env so decision-intel api can see credentials ───────────────────────
if [[ -f "$ROOT/.env" ]]; then
  set -o allexport
  # shellcheck disable=SC1091
  source "$ROOT/.env"
  set +o allexport
fi

# ── ensure frontend deps are installed ────────────────────────────────────────
if [[ ! -d "$ROOT/frontend/node_modules" ]]; then
  echo "Installing frontend dependencies..."
  npm --prefix "$ROOT/frontend" install
fi

# ── start backend ─────────────────────────────────────────────────────────────
echo "Starting decision-intel API on http://127.0.0.1:8000 ..."
decision-intel api &
BACKEND_PID=$!

# ── start frontend ────────────────────────────────────────────────────────────
echo "Starting Next.js dev server on http://localhost:3000 ..."
npm --prefix "$ROOT/frontend" run dev &
FRONTEND_PID=$!

# ── clean up both on exit ─────────────────────────────────────────────────────
cleanup() {
  echo ""
  echo "Shutting down..."
  kill "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null || true
  wait "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null || true
}
trap cleanup INT TERM EXIT

echo ""
echo "  Backend:  http://127.0.0.1:8000"
echo "  Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl-C to stop."
wait
