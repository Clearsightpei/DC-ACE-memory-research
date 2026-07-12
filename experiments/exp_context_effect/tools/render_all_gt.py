"""Bulk-render all Phase 3 GT PNGs at 300×300.

Iterates over curriculum/chars_1000.json and calls make_gt_300 render()
for each character. Writes to gt/phase3/<char>.png.

Skips characters already rendered. Reports failures (chars not in
graphics.txt).
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)

CHARS_JSON = os.path.join(EXP, "curriculum", "chars_1000.json")
OUT_DIR = os.path.join(EXP, "gt", "phase3")
MAKE_GT = os.path.join(HERE, "make_gt_300.py")
os.makedirs(OUT_DIR, exist_ok=True)


def main():
    with open(CHARS_JSON, "r", encoding="utf-8") as f:
        chars = json.load(f)

    rendered = 0
    skipped = 0
    failed = []

    for i, entry in enumerate(chars, 1):
        ch = entry["character"]
        out = os.path.join(OUT_DIR, f"{ch}.png")
        if os.path.exists(out):
            skipped += 1
            continue
        # Use subprocess to isolate turtle state per char — sharing Screen()
        # across many calls in one process leaks resources and causes
        # spurious failures after ~500 renders.
        r = subprocess.run(
            ["python3", MAKE_GT, "--char", ch, "--out", out],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and os.path.exists(out):
            rendered += 1
            if rendered % 50 == 0:
                print(f"  ... {i}/{len(chars)} done ({rendered} rendered)")
        else:
            failed.append(ch)

    print(f"\nDone. Rendered {rendered}, skipped {skipped}, failed {len(failed)}.")
    if failed:
        print(f"Failed sample: {''.join(failed[:60])}"
              + (f"  ... +{len(failed) - 60} more" if len(failed) > 60 else ""))
        with open(os.path.join(EXP, "gt", "phase3_failed.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(failed))
        print(f"Full list at gt/phase3_failed.txt")


if __name__ == "__main__":
    main()
