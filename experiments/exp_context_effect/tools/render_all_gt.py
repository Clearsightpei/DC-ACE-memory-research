"""Bulk-render all Phase 3 GT PNGs at 300x300.

In-process loop using the PIL renderer in make_gt_300. Deterministic
(same input always produces byte-identical output). No subprocess
isolation needed because pure PIL has no shared state.

Behavior:
  - Iterates curriculum/chars_1000.json.
  - Rewrites every PNG unconditionally (default). This guarantees
    a clean regeneration and prevents stale bad GTs from lingering.
    Pass --skip-existing for incremental behavior.
  - Reports failures (chars not in graphics.txt).

Usage:
    python3 render_all_gt.py
    python3 render_all_gt.py --skip-existing        # only render missing
    python3 render_all_gt.py --only 一,人,十        # render specific chars
    python3 render_all_gt.py --phase2               # render Phase-2 radicals
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from make_gt_300 import render, CharNotFound  # noqa: E402

CHARS_JSON = os.path.join(EXP, "curriculum", "chars_1000.json")
OUT_DIR_P3 = os.path.join(EXP, "gt", "phase3")


def _phase2_chars():
    from teacher import load_curriculum
    _, radicals, _ = load_curriculum()
    return [r["character_or_shape"] for r in radicals]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--skip-existing", action="store_true",
                   help="Skip chars whose PNG already exists (default: overwrite).")
    p.add_argument("--only", default=None,
                   help="Comma-separated list of chars to render (defaults to all).")
    p.add_argument("--phase2", action="store_true",
                   help="Render Phase-2 radicals instead of Phase-3 characters.")
    args = p.parse_args()

    if args.phase2:
        chars = _phase2_chars()
        out_dir = os.path.join(EXP, "gt", "phase2")
    else:
        with open(CHARS_JSON, "r", encoding="utf-8") as f:
            entries = json.load(f)
        chars = [e["character"] for e in entries]
        out_dir = OUT_DIR_P3

    if args.only:
        wanted = set(args.only.split(","))
        chars = [c for c in chars if c in wanted]

    os.makedirs(out_dir, exist_ok=True)

    rendered = 0
    skipped = 0
    failed = []
    for i, ch in enumerate(chars, 1):
        out = os.path.join(out_dir, f"{ch}.png")
        if args.skip_existing and os.path.exists(out):
            skipped += 1
            continue
        try:
            render(ch, out)
            rendered += 1
            if rendered % 100 == 0:
                print(f"  ... {rendered}/{len(chars) - skipped}", flush=True)
        except CharNotFound:
            failed.append(ch)

    print(f"\nDone. Rendered {rendered}, skipped {skipped}, failed {len(failed)}.")
    if failed:
        print(f"Failed sample: {''.join(failed[:60])}"
              + (f"  ... +{len(failed) - 60} more" if len(failed) > 60 else ""))
        outname = "phase2_failed.txt" if args.phase2 else "phase3_failed.txt"
        with open(os.path.join(EXP, "gt", outname), "w", encoding="utf-8") as f:
            f.write("\n".join(failed))


if __name__ == "__main__":
    main()
