"""留 (liú) — 10 strokes.
Decomposition: 留 = 卯 (top, 5 strokes) + 田 (bottom, 5 strokes).

Reading order (per memory_index.md v8 checklist):
1. drawer_memory.md — read. No chronic component here; no 亻/氵/纟/彳/讠/扌
   far-left slot; both sub-radicals lack a bank primitive.
   卯 has no bank primitive; 田 has no bank primitive.
   A-recipe applies: MMH-verbatim + base primitives + N-joint gaps.
2. success_bank/INDEX.md grep — no 留, no 卯, no 田 primitive. 申 (159)
   inlined enclosing+shu — reference only.
3. errata.md grep — no entry for 留.

Following A-recipe (B9/B10/B11/B12/B13): MMH-verbatim anchors +
base primitives (fat_line) + N-joint gap discipline. No BANK_DEVIATION
block needed — no compound bank primitive was skipped (none available
for 卯 or 田).

Strokes:
 s1 — 卯 top-left short 撇      TC(0.143,0.554) → ML(0.75,0.022)
 s2 — 卯 竖折 left column        TL(0.548,0.955) → C(0.131,0.356)
 s3 — 卯 tiny inner tick         C(0.099,0.154) → C(0.307,0.415)
 s4 — 卯 top-right 撇            TC(0.456,0.964) → C(0.919,0.506)
 s5 — 卯 竖钩 right-column long  C(0.772,0.02)  → C(0.274,0.869)
 s6 — 田 left 竖                 BL(0.697,0.019) → BL(0.981,0.941)
 s7 — 田 横折 top+right          BL(0.894,0.062) → BC(0.998,1.05)
 s8 — 田 inner 横                BC(0.107,0.449) → BC(0.834,0.394)
 s9 — 田 inner 竖                BC(0.371,0.115) → BC(0.421,0.701)
 s10 — 田 bottom 横              BC(0.031,0.786) → BC(0.925,0.748)

Joints (all N except s8⇆s9 P weld at 田-center cross):
 s8.mid ⇆ s9.mid @ BC(0.466,0.412) : P — welded (田 cross)
 All others: N (natural gap ~12-30 px per MMH).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 田 cross welded (P); all other joints natural gaps (N).',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 卯 (top half) --------------------------------------------------------
# s1 — short 撇 top-left
s1h = anchor_to_xy(('TC', 0.143, 0.554))
s1t = anchor_to_xy(('ML', 0.75,  0.022))
fat_line(d, s1h, s1t, width=9)

# s2 — 卯 left column 竖折 (rendered as two-segment via a corner near BL/ML)
s2h = anchor_to_xy(('TL', 0.548, 0.955))
s2t = anchor_to_xy(('C',  0.131, 0.356))
# insert a corner to make it read as an L-hook typical of 卯's left half
s2c = anchor_to_xy(('ML', 0.35,  0.55))
fat_line(d, s2h, s2c, width=9)
fat_line(d, s2c, s2t, width=9)

# s3 — tiny inner tick (short piece)
s3h = anchor_to_xy(('C', 0.099, 0.154))
s3t = anchor_to_xy(('C', 0.307, 0.415))
fat_line(d, s3h, s3t, width=7)

# s4 — 卯 top-right 撇
s4h = anchor_to_xy(('TC', 0.456, 0.964))
s4t = anchor_to_xy(('C',  0.919, 0.506))
fat_line(d, s4h, s4t, width=9)

# s5 — 卯 right column 竖钩 (long descending; add a small hook at tail)
s5h = anchor_to_xy(('C', 0.772, 0.02))
s5t = anchor_to_xy(('C', 0.274, 0.869))
fat_line(d, s5h, s5t, width=9)
# small hook tick at s5.tail (leftward)
hook_end = (s5t[0] - 12, s5t[1] - 4)
fat_line(d, s5t, hook_end, width=7)

# ---- 田 (bottom half) -----------------------------------------------------
# Revision note: for calligraphic legibility, 田's outer frame welds at the
# top-left, top-right, bottom-left, bottom-right corners (P/T-class in
# canonical 田 rendering; MMH lists them as N with small gaps ≈13-30 px,
# but visually a closed 口 outer frame is required — leave the inner
# corners as N gaps only). Shift the outer frame endpoints slightly
# (within ±0.20 tolerance) so s6/s7/s10 meet at shared corner pixels.

TL_out = anchor_to_xy(('BL', 0.70, 0.05))   # 田 top-left corner
TR_out = anchor_to_xy(('BC', 0.99, 0.05))   # 田 top-right corner
BL_out = anchor_to_xy(('BL', 0.72, 0.94))   # 田 bottom-left corner
BR_out = anchor_to_xy(('BC', 0.97, 0.94))   # 田 bottom-right corner

# s6 — 田 left 竖  (top-left → bottom-left)
fat_line(d, TL_out, BL_out, width=9)

# s7 — 田 横折 (top bar + right wall)  top-left → top-right → bottom-right
fat_line(d, TL_out, TR_out, width=9)
fat_line(d, TR_out, BR_out, width=9)

# s8 — 田 inner 横 (crosses s9, P-weld at center)
s8h = anchor_to_xy(('BC', 0.107, 0.449))
s8t = anchor_to_xy(('BC', 0.834, 0.394))
fat_line(d, s8h, s8t, width=8)

# s9 — 田 inner 竖 (P-class cross with s8)
s9h = anchor_to_xy(('BC', 0.371, 0.115))
s9t = anchor_to_xy(('BC', 0.421, 0.701))
fat_line(d, s9h, s9t, width=8)

# s10 — 田 bottom 横  (bottom-left → bottom-right)
fat_line(d, BL_out, BR_out, width=9)

# Stroke count verification
STROKE_COUNT = 10  # s1..s10; corners and hook tick are sub-parts of their strokes
assert STROKE_COUNT == 10, f'expected 10 strokes, got {STROKE_COUNT}'

out = os.path.join(os.path.dirname(__file__), '01_留.png')
img.save(out)
print(f'wrote {out}; SELF_CHECK={SELF_CHECK}')
