#!/usr/bin/env python3
"""list_chars.py — curriculum enumerator over MakeMeAHanzi graphics.txt.

The Teacher uses this to design a simple→complex character curriculum.
`make_char_gt.py` only renders ONE character; this is the missing
enumeration piece. Read-only: it never renders or writes anything.

A character's stroke count is len(entry["strokes"]) from graphics.txt.

Filters (AND-combined):
  1. CJK-unified only: a single codepoint in U+4E00..U+9FFF
     (drops radicals like ⺀ and compatibility blocks).
  2. Stroke-count band: --min / --max  (default 1..20, so the
     33-stroke monsters never surface).
  3. Common-frequency seed: by default the result is intersected with
     an embedded ~320-character high-frequency seed list, so "simple"
     means *common-and-simple*, not "first obscure glyph in file
     order". --all bypasses the seed (full graphics.txt within band).

Output is sorted by (stroke_count, frequency_rank); seed chars sort by
their frequency rank, non-seed chars (only present with --all) sort
after seed chars within the same stroke count.

Usage:
  python tools/list_chars.py [--min N] [--max N] [--all] [--limit K]
                             [--format plain|json] [--graphics PATH]

  plain (default):  one per line  "人\t2\trank=12"
  json:             [{"character":"人","strokes":2,"rank":12}, ...]
"""

import argparse
import json
import os
import sys

# ── graphics.txt resolution (same logic as make_char_gt.py) ───────────

def _find_default_graphics():
    """Walk up from this file looking for draw_character/graphics.txt."""
    here = os.path.dirname(os.path.abspath(__file__))
    for depth in range(6):
        candidate = os.path.join(here, *([".."] * depth), "draw_character", "graphics.txt")
        if os.path.exists(candidate):
            return os.path.abspath(candidate)
    return os.path.abspath(os.path.join(here, "..", "..", "draw_character", "graphics.txt"))


DEFAULT_GRAPHICS = os.environ.get("GRAPHICS_TXT") or _find_default_graphics()

# ── Embedded common-frequency seed ────────────────────────────────────
# Modern simplified Chinese, ordered by usage frequency (most common
# first). Embedded as a literal (not a data file) for self-containment
# and reproducibility — the curriculum pool must be fixed for the paper.
# rank = 1-based position in this string.
_SEED = (
    "的一是不了人我在有他这为之大来以个中上们"
    "到说国和地也子时道出而要于就下得可你年生"
    "自会那后能对着事其里所去行过家十用发天如"
    "然作方成者多日都三小军二无同么经法当起与"
    "好看学进种将还分此心前面又定见只主没公从"
    "想气五理点文长太两高些三本月定真切平问回"
    "信美再外第打正业本她身边物名果加西月话合"
    "回特代内信表化老给世位次度门任常先海通教"
    "儿原东声提立及比员解水名真听实把相市望次"
    "形几色金量及思九水山术状识候带亲反验运区"
    "做空数被设由神往传师光取选打白教听更结风"
    "色更便条决干部总城北队向力管新四级思口程"
    "白话权门常题书数处听步引太军许更别飞张文"
    "由放识候候内每风极元社决西被干做必战先回"
    "则任取据处队南给色光门即保治北造百规热领"
    "七海口东导器压志世金增争济阶油思术极交受"
    "联什认六共权收证改清美再采转更单风切打白"
    "教速值留团知步反处记将千找争领或师结块跑"
    "谁草越字加脚紧爱等习阵怎花苦惊孩"
)
# Build rank map; first occurrence wins (dedupe while keeping order).
_SEED_RANK = {}
for _i, _c in enumerate(_SEED):
    if _c not in _SEED_RANK:
        _SEED_RANK[_c] = len(_SEED_RANK) + 1


def _is_cjk_unified(ch: str) -> bool:
    return len(ch) == 1 and 0x4E00 <= ord(ch) <= 0x9FFF


def enumerate_chars(graphics_path, lo, hi, seeded):
    """Yield (character, stroke_count, rank) passing the filters."""
    out = []
    with open(graphics_path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            ch = item.get("character", "")
            strokes = item.get("strokes")
            if not ch or not isinstance(strokes, list):
                continue
            if not _is_cjk_unified(ch):
                continue
            sc = len(strokes)
            if sc < lo or sc > hi:
                continue
            rank = _SEED_RANK.get(ch)
            if seeded and rank is None:
                continue
            # non-seed chars (only with --all) sort after seed chars
            sort_rank = rank if rank is not None else 10_000 + ord(ch) % 10_000
            out.append((ch, sc, rank, sort_rank))
    out.sort(key=lambda r: (r[1], r[3]))
    return out


def main():
    p = argparse.ArgumentParser(description="Enumerate graphics.txt characters by stroke count for curriculum design.")
    p.add_argument("--min", type=int, default=1, help="min stroke count (default 1)")
    p.add_argument("--max", type=int, default=20, help="max stroke count (default 20)")
    p.add_argument("--all", action="store_true", help="bypass the common-frequency seed (full graphics.txt within band)")
    p.add_argument("--limit", type=int, default=None, help="cap the number of results")
    p.add_argument("--format", choices=["plain", "json"], default="plain")
    p.add_argument("--graphics", default=None, help="path to graphics.txt (overrides $GRAPHICS_TXT / default)")
    args = p.parse_args()

    gp = args.graphics or DEFAULT_GRAPHICS
    if not os.path.exists(gp):
        print(f"graphics.txt not found: {gp}", file=sys.stderr)
        sys.exit(1)

    rows = enumerate_chars(gp, args.min, args.max, seeded=not args.all)
    if args.limit is not None:
        rows = rows[: args.limit]

    print(f"# {len(rows)} chars  strokes {args.min}-{args.max}  "
          f"{'seeded' if not args.all else 'ALL'}  src={gp}", file=sys.stderr)

    if args.format == "json":
        print(json.dumps(
            [{"character": c, "strokes": s, "rank": r} for (c, s, r, _sr) in rows],
            ensure_ascii=False))
    else:
        for (c, s, r, _sr) in rows:
            print(f"{c}\t{s}\trank={r if r is not None else '-'}")


if __name__ == "__main__":
    main()
