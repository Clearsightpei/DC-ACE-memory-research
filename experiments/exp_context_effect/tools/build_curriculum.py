"""Build the 1000-character curriculum for Phase 3.

Design:
- Target 1000 chars, ordered by stroke count 1 → 19.
- Per-bucket targets shaped for smooth difficulty progression, capped by
  bucket availability.
- **50/50 common/rare mix within each stroke bucket** (per user design
  decision — tests both compositional-memory-payoff and OOD-transfer):
    common = chars in `frequency_seed.SEED_SET`
    rare   = chars in graphics.txt at that stroke count but NOT in seed
- When the common half is short (high stroke counts have few common chars),
  we take all available common chars and top up the deficit from rare.
- Within-bucket ordering: interleave common and rare so the group's
  memory sees a mix as it progresses through the bucket, not a block of
  all-common-then-all-rare.

Output: curriculum/chars_1000.json
Schema:
  [
    {"idx": 1, "character": "一", "strokes": 1, "tier": "common", "rank": 2},
    {"idx": 2, "character": "丨", "strokes": 1, "tier": "rare",   "rank": null},
    ...
  ]
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from frequency_seed import SEED_SET, SEED_RANK  # noqa: E402

EXP = os.path.dirname(HERE)
LIST_CHARS = os.path.join(EXP, "..", "..", "runs", "run_6", "tools", "list_chars.py")
OUT = os.path.join(EXP, "curriculum", "chars_1000.json")

TARGETS = {
    1: 8,   2: 30,  3: 55,  4: 60,  5: 65,
    6: 70,  7: 70,  8: 70,  9: 70,  10: 70,
    11: 70, 12: 65, 13: 60, 14: 55, 15: 50,
    16: 45, 17: 40, 18: 30, 19: 17,
}


def enumerate_by_sc(sc):
    """Return list of {character, strokes, rank(seed-index)} at stroke count sc.

    Sorted by (in-seed-first, then codepoint).
    """
    r = subprocess.run(
        ['python3', LIST_CHARS, '--min', str(sc), '--max', str(sc),
         '--all', '--format', 'json'],
        capture_output=True, text=True, check=True,
    )
    return json.loads(r.stdout)


def interleave(common, rare):
    """Interleave two lists so the merged order alternates as much as
    possible. Whichever list is longer fills the tail."""
    out = []
    i = j = 0
    while i < len(common) and j < len(rare):
        out.append(common[i]); i += 1
        out.append(rare[j]);   j += 1
    out.extend(common[i:])
    out.extend(rare[j:])
    return out


def main():
    curriculum = []
    idx = 1
    summary = []
    for sc in range(1, 20):
        target = TARGETS[sc]
        target_common = target // 2
        target_rare = target - target_common

        pool = enumerate_by_sc(sc)
        common_pool = [c for c in pool if c['character'] in SEED_SET]
        rare_pool = [c for c in pool if c['character'] not in SEED_SET]

        # Sort common by seed rank (most frequent first)
        common_pool.sort(key=lambda x: SEED_RANK.get(x['character'], 1_000_000))

        # Actual picks (top-up when common short)
        picked_common = common_pool[:target_common]
        deficit_common = target_common - len(picked_common)
        picked_rare = rare_pool[:target_rare + deficit_common]

        actual = len(picked_common) + len(picked_rare)
        if actual < target:
            print(f"  sc={sc}: bucket exhausted, wanted {target} got {actual}")

        # Tag and interleave
        common_tagged = [{**c, "tier": "common", "seed_rank": SEED_RANK.get(c['character'])}
                         for c in picked_common]
        rare_tagged = [{**c, "tier": "rare", "seed_rank": None}
                       for c in picked_rare]
        merged = interleave(common_tagged, rare_tagged)

        for entry in merged:
            curriculum.append({
                "idx": idx,
                "character": entry["character"],
                "strokes": entry["strokes"],
                "tier": entry["tier"],
                "seed_rank": entry["seed_rank"],
            })
            idx += 1

        summary.append((sc, target, len(picked_common), len(picked_rare)))

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(curriculum)} chars to {OUT}")
    print(f"\nDistribution:")
    print(f"  {'sc':>3} {'target':>7} {'common':>7} {'rare':>6}")
    total_c = total_r = 0
    for sc, target, nc, nr in summary:
        print(f"  {sc:>3} {target:>7} {nc:>7} {nr:>6}")
        total_c += nc; total_r += nr
    print(f"  {'-'*3} {'-'*7} {'-'*7} {'-'*6}")
    print(f"  {'TOTAL':>3} {total_c+total_r:>7} {total_c:>7} {total_r:>6}")
    print(f"\nCommon:Rare ratio = {total_c}:{total_r} = {100*total_c/(total_c+total_r):.0f}%:{100*total_r/(total_c+total_r):.0f}%")


if __name__ == "__main__":
    main()
