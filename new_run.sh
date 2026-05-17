#!/usr/bin/env bash
# new_run.sh — create a fresh DC-ACE run directory from the template.
#
# Usage:
#   ./new_run.sh <run_name>
#   ./new_run.sh run_3
#
# Creates:
#   runs/<run_name>/                  ← clone of dc_ace_template/
#
# Runs are PLAIN FOLDERS inside the one project repo
# (github.com/Clearsightpei/DC-ACE-memory-research). There is no
# per-run git repo and no per-run GitHub remote — every run's
# cycle-by-cycle history is committed to (and pushed from) the single
# project repo by the /cycle skill. This keeps GitHub to one clean
# repo with many commits, not many repos.
#
# Does NOT modify active_run.txt — switch the active run yourself with:
#   echo runs/<run_name> > active_run.txt

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <run_name>" >&2
    echo "  e.g.: $0 run_3" >&2
    exit 2
fi

RUN_NAME="$1"
PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE_DIR="$PROJECT_ROOT/dc_ace_template"
DEST_DIR="$PROJECT_ROOT/runs/$RUN_NAME"

if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "Template directory not found: $TEMPLATE_DIR" >&2
    exit 1
fi

if [ -e "$DEST_DIR" ]; then
    echo "Destination already exists: $DEST_DIR" >&2
    echo "Pick a different run name, or rm -rf the existing one first." >&2
    exit 1
fi

mkdir -p "$PROJECT_ROOT/runs"
cp -r "$TEMPLATE_DIR" "$DEST_DIR"
chmod +x "$DEST_DIR/start_loop.sh" "$DEST_DIR/stop_loop.sh"

# Restore the empty dirs that cp may flatten depending on the tree state.
mkdir -p "$DEST_DIR"/{ground_truths,attempts,judge_results,task_briefs}

# Strip any .git that slipped in from the template copy — runs are
# plain folders in the one project repo, never their own repo.
rm -rf "$DEST_DIR/.git"

# Record the run's creation in the SINGLE project repo.
cd "$PROJECT_ROOT"
git add "runs/$RUN_NAME"
git commit -m "cycle 0 init: fresh run '$RUN_NAME' from template" >/dev/null 2>&1 \
    || echo "(nothing to commit — check 'git status')"

echo "Created run: $DEST_DIR  (tracked in the project repo)"
echo
echo "To activate this run:"
echo "    echo runs/$RUN_NAME > $PROJECT_ROOT/active_run.txt"
echo
echo "History & GitHub: handled by the one project repo. /cycle commits"
echo "each phase and pushes to origin (DC-ACE-memory-research). Nothing"
echo "else to set up."
echo
echo "To start the loop:"
echo "    (in Claude Code from $PROJECT_ROOT)"
echo "    /loop 10m /cycle"
