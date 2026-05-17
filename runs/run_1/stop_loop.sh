#!/usr/bin/env bash
# Pause the cycle loop.
#
# Creates a .stop sentinel that /cycle checks at the top of each run.
# While .stop exists, /cycle exits immediately without doing anything.
#
# To FULLY halt the /loop (so it stops firing every 10 min), you also
# need to press Esc in the Claude Code window where the loop is running.
# This script alone makes each fire a no-op, but the loop itself keeps
# firing on schedule.

set -euo pipefail
cd "$(dirname "$0")"
touch .stop
echo ".stop created. /cycle will skip every fire until you remove it."
echo "Resume:  ./start_loop.sh   (or: rm .stop)"
echo "Halt the /loop entirely:   press Esc in the Claude Code session."
