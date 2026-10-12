#!/usr/bin/env python3
"""make_reliability_sample.py — frozen, blinded sample for a second-judge
inter-rater reliability study.

Draws 150 first-attempt renders from the common four-tier window (B9-B13,
curriculum positions 419-668), 30 per group, and emits a judge-facing
package that leaks nothing about group, source path, or original verdict.

Design
------
* Item-disjoint by default: 150 DISTINCT characters, 30 assigned to each
  group, so the second judge never sees the same reference image twice.
  Independent per-group sampling (--allow-repeats) draws ~118 distinct
  characters for 150 slots; the ~32 repeats let a judge anchor on their
  own earlier verdict for the same target, which weakens independence.
* Every image is COPIED into the package under an opaque token. Nothing
  in the judge-facing tree encodes group, item id, batch, or verdict.
* The token -> (group, item, original verdict) mapping is written to a
  separate ANSWER_KEY.json that the second judge must not open.
* Presentation order is shuffled with the recorded seed.

Outputs (under --out, default: reliability_study/)
    manifest.json      judge-facing; feed to judge_blind.py
    images/            blinded PNG copies (<token>.png, <token>_gt.png)
    RUBRIC.md          verbatim four-tier rubric
    README.md          instructions for the second judge
    ANSWER_KEY.json    SEALED — do not open before judging
    SAMPLE_SPEC.json   seed, parameters, checksum of the selection

Usage
    python3 tools/make_reliability_sample.py --seed 20261006
    # then, as the second judge:
    python3 tools/judge_blind.py --batch reliability_study/manifest.json
"""
import argparse, csv, hashlib, json, os, random, re, shutil, sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
EXPORT = os.path.join(ROOT, "export", "item_grades.csv")
GT_DIR = os.path.join(ROOT, "gt", "phase3")

GDIR = {"G1": "G1_no_memory", "G2": "G2_free_form", "G3": "G3_coords",
        "G4": "G4_grid", "G5": "G5_code_bank_mmh"}
GROUPS = ["G1", "G2", "G3", "G4", "G5"]

RAD = re.compile(r"^p2_radical_(\d+)_(.*)$")
CHR = re.compile(r"^p3_char_(\d+)_(.*)$")

RUBRIC = """# Verdict rubric — four tiers

You are grading a program-generated rendering of a Chinese character
against its reference. Judge the rendering only. Press one key per item.

  a = A (Perfect)  — calligraphic reference quality; structure,
                     proportion, and brush feel all correct.
  p = PASS         — correct and recognizable; a fluent reader
                     identifies it and nothing is structurally wrong.
                     May still look mechanical or uniform-width.
  c = C (Close)    — close but not exact; one localized error (one
                     stroke off, one component mis-positioned). Counts
                     as a failure for success rate, recorded separately.
  f = FAIL         — not recognizable, or structurally wrong.

  s = SKIP    b = BACK    q = QUIT (auto-saves)

Notes
-----
* Perfect is stringent. Correct strokes rendered with uniform-width
  crudeness earn PASS, not Perfect.
* "Success" in the downstream analysis means A or PASS. C and FAIL are
  both failures; they are kept apart only to separate a near miss from
  a total wreck.
* Grade each item on its own. Do not try to be consistent with how you
  think an earlier item was graded, and do not ration the tiers.
"""

README = """# Second-judge reliability study

## What this is

150 renderings sampled from one experiment. Your job is to grade each
one against its reference using the rubric in `RUBRIC.md`.

## What you are NOT told, deliberately

Which experimental condition produced each image, what the original
judge said about it, and what the study's hypotheses are. The sample is
frozen and the answer key is sealed in `ANSWER_KEY.json` — **do not open
it before you finish judging.**

## How to run

    python3 tools/judge_blind.py --batch reliability_study/manifest.json

Labels save after every keypress to `reliability_study/labels.json`.
The tool is resumable: quit with `q` and rerun to pick up where you
stopped. Judging 150 items takes roughly 45-70 minutes; splitting it
across sittings is fine.

## Please do not

* Look at the answer key, the repository, or the paper before finishing.
* Go back to revise earlier verdicts to make them consistent. First
  reaction is the measurement.
"""


def parse_item(item_id):
    """-> (abs_position, retry_n); retry_n = 0 for a first attempt."""
    m = RAD.match(item_id)
    if m:
        base, suffix = int(m.group(1)), m.group(2)
    else:
        m = CHR.match(item_id)
        if not m:
            return None, None
        base, suffix = int(m.group(1)) + 135, m.group(2)
    rm = re.search(r"__retry_(\d+)", suffix)
    return base, (int(rm.group(1)) if rm else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20261006,
                    help="recorded in SAMPLE_SPEC.json; changing it changes the sample")
    ap.add_argument("--per-group", type=int, default=30)
    ap.add_argument("--out", default=os.path.join(ROOT, "reliability_study"))
    ap.add_argument("--allow-repeats", action="store_true",
                    help="sample each group independently; a character may recur")
    args = ap.parse_args()

    rng = random.Random(args.seed)

    # ---- load first attempts in the four-tier window -------------------
    rows = list(csv.DictReader(open(EXPORT, encoding="utf-8")))
    pool = {}                                     # group -> {abs: row}
    for r in rows:
        a, rn = parse_item(r["item_id"])
        if a is None or rn != 0:
            continue
        if not (419 <= a <= 668):                 # B9-B13 common window
            continue
        pool.setdefault(r["group"], {})[a] = r
    for g in GROUPS:
        if len(pool.get(g, {})) != 250:
            sys.exit(f"ERROR: {g} has {len(pool.get(g, {}))} window items, expected 250")

    # ---- select --------------------------------------------------------
    picks = []                                    # (group, abs, row)
    if args.allow_repeats:
        for g in GROUPS:
            for a in rng.sample(sorted(pool[g]), args.per_group):
                picks.append((g, a, pool[g][a]))
    else:
        need = args.per_group * len(GROUPS)
        chosen = rng.sample(sorted(pool["G1"]), need)   # window is identical across groups
        rng.shuffle(chosen)
        for i, g in enumerate(GROUPS):
            for a in chosen[i * args.per_group:(i + 1) * args.per_group]:
                picks.append((g, a, pool[g][a]))

    rng.shuffle(picks)                            # presentation order

    # ---- build the package --------------------------------------------
    out = args.out
    img_dir = os.path.join(out, "images")
    os.makedirs(img_dir, exist_ok=True)

    items, key, missing = [], {}, []
    for n, (g, a, r) in enumerate(picks, start=1):
        token = f"R{n:04d}"
        char = r["char"]
        src = os.path.join(ROOT, "groups", GDIR[g], "attempts",
                           r["item_id"], f"01_{char}.png")
        gt = os.path.join(GT_DIR, f"{char}.png")
        if not os.path.exists(src) or not os.path.exists(gt):
            missing.append((token, g, r["item_id"], os.path.exists(src), os.path.exists(gt)))
            continue
        dst = os.path.join(img_dir, f"{token}.png")
        dgt = os.path.join(img_dir, f"{token}_gt.png")
        shutil.copyfile(src, dst)
        shutil.copyfile(gt, dgt)
        items.append({
            "id": token,
            "phase": "character",
            "target_label": char,
            "target_description": None,
            "target_png": os.path.abspath(dgt),
            "attempts": [{"group": "BLINDED", "path": os.path.abspath(dst)}],
        })
        key[token] = {"group": g, "item_id": r["item_id"], "abs": a,
                      "char": char, "batch": r["batch"],
                      "original_verdict": r["verdict"]}

    if missing:
        print(f"WARNING: {len(missing)} picks skipped (missing image):")
        for m in missing[:10]:
            print("   ", m)

    manifest = {"batch_id": "reliability_study", "shuffle_seed": args.seed,
                "items": items}
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w",
                             encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump(key, open(os.path.join(out, "ANSWER_KEY.json"), "w",
                        encoding="utf-8"), ensure_ascii=False, indent=2)
    open(os.path.join(out, "RUBRIC.md"), "w", encoding="utf-8").write(RUBRIC)
    open(os.path.join(out, "README.md"), "w", encoding="utf-8").write(README)

    digest = hashlib.sha256(
        json.dumps(sorted((v["group"], v["abs"]) for v in key.values())).encode()
    ).hexdigest()
    spec = {
        "created": datetime.now().isoformat(timespec="seconds"),
        "seed": args.seed,
        "per_group": args.per_group,
        "n_selected": len(items),
        "window": "B9-B13, curriculum positions 419-668 (250 items per group)",
        "sampling": "independent per group (repeats possible)" if args.allow_repeats
                    else "item-disjoint: 150 distinct characters, 30 per group",
        "selection_sha256": digest,
        "source": "export/item_grades.csv, first attempts only",
        "note": "Sample frozen at creation. Re-running with the same seed and "
                "the same item_grades.csv reproduces it exactly.",
    }
    json.dump(spec, open(os.path.join(out, "SAMPLE_SPEC.json"), "w"), indent=2)

    dist = {}
    for v in key.values():
        dist[v["group"]] = dist.get(v["group"], 0) + 1
    print(f"\nwrote {len(items)} blinded items to {out}")
    print(f"  seed              : {args.seed}")
    print(f"  sampling          : {spec['sampling']}")
    print(f"  per group         : {dist}")
    print(f"  distinct chars    : {len({v['char'] for v in key.values()})}")
    print(f"  selection sha256  : {digest[:16]}...")
    print(f"\n  second judge runs:")
    print(f"    python3 tools/judge_blind.py --batch {os.path.join(out, 'manifest.json')}")


if __name__ == "__main__":
    main()
