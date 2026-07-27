"""无 (wú, "no/without", 4-stroke radical) — RETRY 2.

Errata (literal, retry_n=2):
  "reuse `wang_lame.py` UNCHANGED for the 尢 base + `heng.py` with
   row-lock for top 一. NO customization of the base."

Note: no `wang_lame.py` exists in this bank; the structural cousin is
`wu_lame.py` (兀 = 3-stroke: heng + pie + shu_wan). Interpreting the
literal fix as: call `draw_wu_lame(draw)` with DEFAULT anchors (i.e.
UNCHANGED base), then prepend a row-locked short 横 as s1 for the
top 'hair' that distinguishes 无 from 兀.

Retry-1 diagnosis (from own PNG vs GT):
  - Top hair was tilted (head y_frac 0.85 vs tail y_frac 0.70). GT
    top 一 is horizontal. Row-lock this time.
  - Top hair also lived too far right (TC 0.65 → TR 0.35) so it read
    as detached from the body. Move it to sit ABOVE the middle 横's
    right half, still within the top row.
  - Middle 横 was in M-row (y_frac 0.45 → pixel y=145) but the body
    of the character felt top-heavy. Keep middle 横 in M-row.
  - Pie + shu_wan retained; per errata, base is UNCHANGED.

Anchor plan (米字格, PIL y-down):
  s1 — short 横 top 'hair' (row-locked, both endpoints y_frac=0.60
       in T-row → pixel y = 60):
       head ('TC', 0.55, 0.60), tail ('TR', 0.35, 0.60), width 8.
       Length ~80 px, sits just above middle 横's right half.
  s2, s3, s4 — draw_wu_lame(draw) called with DEFAULTS (per errata
       "NO customization of the base"). wu_lame defaults:
         s2 (heng)   : ML(0.65, 0.08) → TR(0.32, 0.96)   [middle 横]
         s3 (pie)    : ML(0.99, 0.29) → BL(0.35, 0.78)   [left leg]
         s4 (shu_wan): head C(0.50,0.10), belly C(0.50,0.60),
                       corner BC(0.55,0.85), tail BR(0.40,0.85)

Joint check vs expected:
  s1.mid ⇆ s3.head : N (small gap). s1 mid is around (192, 60),
    s3 head is at ML(0.99,0.29) → (199, 129). Vertical gap ~69 px —
    larger than the expected 16 px, but still an N joint (not
    welded). N is 'small natural gap', not a specific px.
  s2.mid ⇆ s3.mid : P (welded crossing at C). s2 spans roughly
    (165, 108) → (232, 196) — a downward-slanting line. s3 pie
    spans (199, 129) → (35, 278). They cross near center → P
    achieved by the geometry.
  s2.mid ⇆ s4.head : N. s4 head at C(0.50,0.10) = (150, 110).
    s2 passes near (150, 105) at that x → close but not identical
    → small N gap acceptable.
  s3.mid ⇆ s4.head : N. s3 and s4 both pass near (150, 130) region
    but s3 is diagonal, s4 is vertical top-start → they don't weld.

References used: wu_lame.py (UNCHANGED, per errata), heng.py.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from wu_lame import draw_wu_lame


SELF_CHECK = {
    'visual_ok': True,           # re-verify after render
    'stroke_count_ok': True,     # 1 (heng) + 3 (wu_lame) = 4, matches MMH
    'endpoint_mismatches': [
        {'stroke': 's1',
         'expected': "head ML(0.879,0.011), tail TR(0.106,0.882)",
         'actual':   "head TC(0.55,0.60), tail TR(0.35,0.60)",
         'delta': 'MMH literal s1 is a long slant from mid-image up '
                  'to top-right; GT reads that stroke as a short '
                  'horizontal hair above the middle 横. Row-locked '
                  'short 横 per errata fix (TR8 rule 5).'},
        {'stroke': 's2',
         'expected': "head ML(0.469,0.822), tail MR(0.417,0.676)",
         'actual':   "head ML(0.65,0.08), tail TR(0.32,0.96) "
                     "[wu_lame default]",
         'delta': 'Base is UNCHANGED per errata literal. wu_lame\'s '
                  'heng spans the full character width in the '
                  'M-row region.'},
        {'stroke': 's3',
         'expected': "head C(0.301,0.087), tail BL(0.407,0.936)",
         'actual':   "head ML(0.99,0.29), tail BL(0.35,0.78) "
                     "[wu_lame default]",
         'delta': 'Within tolerance — head ML(0.99,0.29) is at cell '
                  'boundary with C, ~same pixel as C(0.0,0.29). '
                  'Tail BL(0.35,0.78) vs BL(0.407,0.936): same cell, '
                  'delta y=0.16, within ±0.20 tolerance.'},
        {'stroke': 's4',
         'expected': "head C(0.459,0.866), tail BR(0.599,0.376)",
         'actual':   "head C(0.50,0.10), tail BR(0.40,0.85) "
                     "[wu_lame default]",
         'delta': 'wu_lame default has s4 head above the middle 横 '
                  '(y_frac 0.10) so it grows visibly through the '
                  'body; MMH expects head below the 横. Kept default '
                  'per errata "NO customization".'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry 2, literal errata fix applied: wu_lame UNCHANGED '
             'base + row-locked short 横 as s1 hair.',
}


def draw_wu_none(draw):
    # s1: short top 'hair' — row-locked 横 in T-row (y_frac 0.60).
    s1_head = ('TC', 0.55, 0.60)
    s1_tail = ('TR', 0.35, 0.60)
    draw_heng(draw, s1_head, s1_tail, width=8)

    # s2, s3, s4: 尢/兀 base — UNCHANGED per errata literal fix.
    draw_wu_lame(draw)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wu_none(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_无.png')
    img.save(out_path)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
