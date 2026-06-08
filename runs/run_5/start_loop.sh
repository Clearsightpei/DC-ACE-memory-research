#!/usr/bin/env bash
# Resume the cycle loop for this run.
#
# Removes the .stop sentinel so /cycle will run on its next fire.
# Does NOT start /loop itself — you start that in Claude Code with:
#
#     /loop 10m /cycle
#
# This script just clears the pause flag for THIS run dir.

set -euo pipefail
cd "$(dirname "$0")"
rm -f .stop
echo ".stop removed in $(pwd)."
echo "If /loop is running in Claude Code, the next fire will do real work."
echo "If /loop is NOT running yet, start it with:  /loop 10m /cycle"
