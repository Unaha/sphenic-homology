#!/usr/bin/env bash
# One-command verification: enumeration replay + independent certificate replay on all bundles.
set -e
cd "$(dirname "$0")"
echo "== 1/2 independent enumeration replay (stdlib only) =="
python3 scripts/enum_replay.py
echo "== 2/2 independent certificate replay (all bundle sets) =="
for d in certificates/N*; do python3 scripts/lg_replay_check.py "$d"; done
echo "ALL VERIFICATION PASSES COMPLETE"
