"""Bulk-render all Phase-2 radical GT PNGs at 300×300.

Iterates over all 137 radicals, calls make_gt_300 render() for each via
subprocess-per-char (turtle state doesn't leak across subprocesses).
Writes to gt/phase2/<char>.png. Skips radicals not in MMH graphics.txt
(currently 卝 and 牜).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)

# Import radical list from teacher (canonical order)
sys.path.insert(0, HERE)
from teacher import load_curriculum

_, radicals, _ = load_curriculum()

OUT_DIR = os.path.join(EXP, "gt", "phase2")
os.makedirs(OUT_DIR, exist_ok=True)
MAKE_GT = os.path.join(HERE, "make_gt_300.py")


def main():
    rendered = 0
    skipped = 0
    failed = []
    for r in radicals:
        ch = r["character_or_shape"]
        out = os.path.join(OUT_DIR, f"{ch}.png")
        if os.path.exists(out):
            skipped += 1
            continue
        try:
            subprocess.run(
                ["python3", MAKE_GT, "--char", ch, "--out", out],
                capture_output=True, text=True, timeout=30, check=True,
            )
            rendered += 1
        except subprocess.CalledProcessError as e:
            failed.append((ch, e.stderr.strip()[:120]))
        except subprocess.TimeoutExpired:
            failed.append((ch, "TIMEOUT"))

    print(f"Rendered: {rendered}")
    print(f"Skipped (already exist): {skipped}")
    print(f"Failed: {len(failed)}")
    for ch, err in failed:
        print(f"  {ch}: {err}")


if __name__ == "__main__":
    main()
