"""CLI: print the drawer prompt for (group, item_id) to stdout.

Usage:
  python3 tools/print_drawer_prompt.py --group G4 --item p2_radical_019_匚
  python3 tools/print_drawer_prompt.py --group G4 --item p2_radical_011_匕 --retry 1
"""
import argparse, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from dispatcher import build_drawer_prompt
from teacher import Teacher

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", required=True, choices=["G1","G2","G3","G4"])
    ap.add_argument("--item", required=True, help="item_id, e.g. p2_radical_019_匚")
    ap.add_argument("--retry", type=int, default=0, help="retry_n; 0=main attempt")
    args = ap.parse_args()

    t = Teacher()
    match = [it for it in t.all_items if it["id"] == args.item]
    if not match:
        print(f"ERROR: item_id {args.item} not found", file=sys.stderr)
        sys.exit(1)
    item = dict(match[0])  # copy

    if args.retry > 0:
        # rewrite id + attempt path so retries land in a distinct dir
        orig_id = item["id"]
        item["id"] = f"{orig_id}__retry_{args.retry}"
    prompt = build_drawer_prompt(args.group, item)
    if args.retry > 0:
        prompt += f"\n\n## RETRY CONTEXT\n\nThis is retry #{args.retry} of {match[0]['id']}. Prior attempt saved at `groups/{ {'G1':'G1_no_memory','G2':'G2_free_form','G3':'G3_coords','G4':'G4_grid'}[args.group] }/attempts/{match[0]['id']}/`. Read your errata.md entry for this item, apply the fix idea, save to `attempts/{item['id']}/` (a fresh dir).\n"
    sys.stdout.write(prompt)

if __name__ == "__main__":
    main()
