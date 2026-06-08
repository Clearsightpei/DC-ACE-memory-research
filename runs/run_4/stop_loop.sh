#!/usr/bin/env bash
# Pause the cycle loop for this run.
#
# Creates a .stop sentinel that /cycle checks at the top of each run.
# While .stop exists, /cycle exits immediately without doing anything
# (per the cycle skill's preflight step).

set -euo pipefail
cd "$(dirname "$0")"
touch .stop
echo ".stop created in $(pwd). /cycle will skip every fire until you remove it."
echo "Resume:  ./start_loop.sh   (or: rm .stop)"
echo "Halt /loop entirely:       press Esc in the Claude Code session."
