"""CLI: print the drawer prompt for (group, item_id) to stdout.

Usage:
  python3 tools/print_drawer_prompt.py --group G4 --item p2_radical_019_匚
  python3 tools/print_drawer_prompt.py --group G4 --item p2_radical_011_匕 --retry 1
"""
import argparse, sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from dispatcher import build_drawer_prompt
from teacher import Teacher

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", required=True, choices=["G1","G2","G3","G4","G5"])
    ap.add_argument("--item", required=True, help="item_id, e.g. p2_radical_019_匚")
    ap.add_argument("--retry", type=int, default=0, help="retry_n; 0=main attempt")
    ap.add_argument("--rerun", action="store_true",
                    help="Rerun mode: prior = existing __retry_{retry} dir, output = __retry_{retry}__rerun. "
                         "Used to test prompt/protocol changes on the same failed attempts.")
    args = ap.parse_args()

    t = Teacher()
    match = [it for it in t.all_items if it["id"] == args.item]
    if not match:
        print(f"ERROR: item_id {args.item} not found", file=sys.stderr)
        sys.exit(1)
    item = dict(match[0])  # copy

    gdirs = {'G1':'G1_no_memory','G2':'G2_free_form','G3':'G3_coords','G4':'G4_grid','G5':'G5_code_bank_mmh'}
    EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if args.retry > 0:
        orig_id = item["id"]
        if args.rerun:
            # Rerun mode: don't overwrite the failed attempt; land in a fresh dir
            item["id"] = f"{orig_id}__retry_{args.retry}__rerun"
        else:
            item["id"] = f"{orig_id}__retry_{args.retry}"
    prompt = build_drawer_prompt(args.group, item)
    if args.retry > 0:
        # Collect ALL prior attempts (main + every existing __retry_K for K < N, plus
        # any __rerun variants). v10: drawer sees full trajectory — passes too, not just fails.
        char = item.get('character_or_shape') or match[0]['target_label']
        gt_png = item.get('target_png') or f"gt/phase{'2' if item['phase']=='radical' else '3'}/{char}.png"
        base_id = match[0]['id']
        attempts_root = os.path.join(EXP, "groups", gdirs[args.group], "attempts")

        prior_attempts = []  # list of (label, png_path, verdict_or_None)

        # Load verdicts across all judged batches so we can annotate each prior attempt
        judged_verdicts = {}  # attempt_key -> verdict
        judgments_dir = os.path.join(EXP, "judgments")
        if os.path.isdir(judgments_dir):
            for batch in os.listdir(judgments_dir):
                lp = os.path.join(judgments_dir, batch, "labels.json")
                if not os.path.isfile(lp):
                    continue
                try:
                    labs = json.load(open(lp, encoding="utf-8"))
                except Exception:
                    continue
                for aid, meta in labs.items():
                    if meta.get("actual_group") != args.group:
                        continue
                    iid = meta.get("item_id", "")
                    if iid.startswith(base_id):
                        # normalize the retry dir this refers to
                        # attempt_key format: <item_id>__att<N> — but item_id itself may
                        # already have __retry_K suffix from manifest builder.
                        judged_verdicts.setdefault(iid, meta.get("verdict"))

        def _add(dir_name, label):
            path = os.path.join(attempts_root, dir_name)
            png = os.path.join(path, f"01_{char}.png")
            if os.path.isfile(png):
                # translate absolute to project-relative for display
                rel = os.path.relpath(png, EXP)
                # find verdict
                if dir_name == base_id:
                    lookup = base_id
                else:
                    # try common forms curator/dispatcher use
                    suffix = dir_name[len(base_id):]  # e.g. "__retry_3"
                    lookup_candidates = [
                        f"{base_id}{suffix}__{args.group}",
                        f"{base_id}{suffix}",
                    ]
                    lookup = next((c for c in lookup_candidates if c in judged_verdicts), None)
                v = judged_verdicts.get(lookup) if lookup else None
                prior_attempts.append((label, rel, v))

        if args.rerun:
            # Rerun mode: include everything up to and including retry_N
            _add(base_id, "main")
            for k in range(1, args.retry + 1):
                _add(f"{base_id}__retry_{k}", f"retry {k}")
        else:
            _add(base_id, "main")
            for k in range(1, args.retry):
                _add(f"{base_id}__retry_{k}", f"retry {k}")

        # Build display list with verdict annotation
        if prior_attempts:
            trajectory_lines = []
            for label, rel, v in prior_attempts:
                verdict_str = f" — verdict: {v}" if v else " — verdict: (not yet judged)"
                trajectory_lines.append(f"- **{label}** — `{rel}`{verdict_str}")
            trajectory_block = "\n".join(trajectory_lines)
        else:
            trajectory_block = "*(no prior attempts on disk — this is unusual for a retry; proceed with GT-only analysis)*"

        prompt += f"""

## RETRY CONTEXT — READ THIS FIRST

This is retry #{args.retry} of {base_id}. Everything you had for the main attempt is still available: memory files, banks, principles, errata — plus one new resource: **your own past attempts on this item**, INCLUDING any that PASSED (so you can see what worked, not just what failed).

### Full attempt trajectory for {base_id}

{trajectory_block}

### MANDATORY STEP 0 — inspect the trajectory before writing any code

Before opening errata.md or any bank file:

1. Use the Read tool on the **ground truth PNG**: `{gt_png}`
2. Use the Read tool on **every prior attempt PNG listed above**. Look at each side-by-side with GT. Note which ones PASSED (if any) and which FAILED.
3. Write a "TRAJECTORY DIFF" block at the top of `generated.py` covering:
   - What the FAILED attempts got wrong (≥2 concrete visual gaps per fail: WHAT is off, WHERE, by how much).
   - What any PASSED attempts got right (if there are passes — copy their approach; don't reinvent).
   - Which fixes you plan to apply this attempt.

Do NOT skip this step; do NOT paraphrase errata — the trajectory diff must come from what you SEE in the PNGs.

### Then

- Read your errata.md entry — treat it as *one hypothesis*, not ground truth. Your visual trajectory diff overrides it if they conflict.
- Apply your best fix. Write to `attempts/{item['id']}/generated.py` and its PNG (a fresh dir — prior attempts untouched).
- After rendering, if you have budget for one revision, open your new PNG and compare to GT one more time. Revise once if you spot a fixable regression.
"""
    sys.stdout.write(prompt)

if __name__ == "__main__":
    main()
