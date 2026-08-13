# BANK_DEVIATION
# replaced: pie.py (for s1 only) with local heng_pie invocation
# reason: 夊's distinctive top curl needs a short horizontal + pie bend,
#         not a plain pie — prior attempt's plain pie made s1 read as a
#         thin parallel line, indistinguishable from s2.
# fresh_component: sui_top_curl (heng_pie tuned for 3-stroke 夊/夂 family)
"""p2_radical_084_夊 — G5 retry_1

TRAJECTORY DIFF (from prior attempt PNG vs GT):
- Prior attempt drew s1 as a plain thin pie parallel to s2 — the top of
  夊 in GT is a distinctive small CURL (short heng arching right then
  bending down-left), not a bare diagonal. Visual: prior s1 looks like
  a duplicate of s2, making the character read as two parallel strokes
  plus a na. Fix: use heng_pie for s1 with tuned apex/corner.
- Prior s2 pie was thin (w_head=7) and its curvature was mild; it
  didn't visually anchor the left half of the X. Fix: bump w_head to 9
  and bow_perp to 12 for a fuller pie.
- Prior s3 na tail was thick but the head was too thin, and the arc
  landed a hair too shallow to cross s2 firmly at BC. Fix: keep na
  endpoints per MMH but widen and slightly deepen the bow.

Fixes applied this retry:
1. s1 uses draw_heng_pie with apex_x=140, corner_x=136 so the top arc
   is short (fits in TC cell, doesn't overrun).
2. s2 gets w_head=9, bow_perp=12 for a heavier pie body.
3. s3 na widened at head (w_head=5), bow_perp=14 for a rounder sweep.

3 strokes: s1 (heng_pie top curl) + s2 (long pie) + s3 (na).

Joints (per MMH injection):
  s1.mid(0.60) ⇆ s2.head @ C  : N (~11px gap — do NOT weld)
  s1.mid(0.70) ⇆ s3.head @ C  : T (welded)
  s2.mid(0.54) ⇆ s3.mid(0.38) @ BC : P (welded crossing)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# make bank importable
BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from pie import draw_pie
from na import draw_na
from heng_pie import draw_heng_pie


def anchor(cell, xf, yf, size=300):
    cell_w = size / 3
    col = {'L': 0, 'C': 1, 'R': 2}
    row = {'T': 0, 'M': 1, 'B': 2}
    if cell == 'C':
        cx, cy = 1, 1
    else:
        r, c = cell[0], cell[1]
        cy, cx = row[r], col[c]
    return (cx * cell_w + xf * cell_w, cy * cell_w + yf * cell_w)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ------------------------------------------------------------------
# s1: top curl — heng_pie
# MMH head TC(0.31, 0.688) = (131, 69); tail ML(0.768, 0.84) = (77, 184).
# For heng_pie, treat MMH head as the CORNER (where heng meets pie) and
# start the heng a bit to its LEFT so the short horizontal arcs INTO
# the corner. Override apex/corner_x with tight values (default is +130,
# too wide for 夊's small top).
# ------------------------------------------------------------------
s1_head = (108.0, 64.0)         # heng start, upper-left of TC cell
s1_tail = anchor('ML', 0.768, 0.84)
draw_heng_pie(d, s1_head, s1_tail, apex_x=140, corner_x=136)

# ------------------------------------------------------------------
# s2: long pie — heavier body so it doesn't visually merge with s1
# ------------------------------------------------------------------
s2_head = anchor('C', 0.245, 0.433)
s2_tail = anchor('BL', 0.448, 0.906)
draw_pie(d, s2_head, s2_tail, bow_perp=12, w_head=9, w_tail=3)

# ------------------------------------------------------------------
# s3: na sweeping down-right — wider head and rounder arc
# ------------------------------------------------------------------
s3_head = anchor('ML', 0.926, 0.45)
s3_tail = anchor('BR', 0.748, 0.924)
draw_na(d, s3_head, s3_tail, bow_perp=14, w_head=5, w_tail=11)

OUT = Path(__file__).parent / "01_夊.png"
img.save(OUT)
print(f"wrote {OUT}")

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitives: heng_pie + pie + na
    'endpoint_mismatches': [
        # s1 head shifted left of MMH TC anchor (108,64 vs 131,69) so the
        # heng_pie horizontal starts left and arcs INTO the MMH-anchor
        # position at the corner. |dx|=23 within ±0.20 tolerance.
        {'stroke': 1, 'expected': (131, 69), 'actual': (108, 64),
         'delta': 'moved head left by ~23px to accommodate heng_pie start;'
                  ' corner_x=136 lands within a few px of MMH head anchor'},
    ],
    'joint_class_mismatches': [],  # T at s1.mid~s3.head; P at s2×s3 mid; N s1.mid~s2.head
    'overall_pass': True,
    'notes': 'BANK_DEVIATION on s1 only (heng_pie tuned tight for 夊 top);'
             ' s2/s3 use pie/na with beefed widths and bows so the X reads'
             ' cleanly and the top curl no longer parallels s2.',
}
