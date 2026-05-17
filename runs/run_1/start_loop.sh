#!/usr/bin/env bash
# Resume the cycle loop.
#
# Removes the .stop sentinel so /cycle will run on its next fire.
# Does NOT start /loop itself — you start that in Claude Code with:
#
#     /loop 10m /cycle
#
# This script just clears the pause flag.

set -euo pipefail
cd "$(dirname "$0")"
rm -f .stop
echo ".stop removed."
echo "If /loop is already running in Claude Code, the next fire will do real work."
echo "If /loop is NOT running yet, start it with:  /loop 10m /cycle"
