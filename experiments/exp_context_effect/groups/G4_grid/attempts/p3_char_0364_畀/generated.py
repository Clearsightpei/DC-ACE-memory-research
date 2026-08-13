# 畀 (bì) — Phase 3 char 0364, 8 strokes
# Structure: 田 (5 strokes: left shu + 横折 + inner heng + spine + bottom heng)
#            + wide 一 below (s6) + 丿 left leg (s7) + 竖 right leg (s8).
# Split: 畀 ≈ 田 + 丌 stack.
# Layout borrowed conceptually from mastered 甲 (0157) / 申 (0159) / 由 (0204)
# for the 田-frame + spine pattern; 丌 base inlined fresh with MMH anchors.
# Anchors follow MMH-derived expectations verbatim (per v9 lesson: MMH-verbatim
# beats hand-tuned when composition is failing).
#
# Reading-order log:
#  1. drawer_memory.md — no dedicated primitive for 田 or 丌; fresh inline OK.
#  2. INDEX.md grep 畀 — no mastered entry (0161 甴 is a related 田-frame char).
#  3. errata.md grep 畀 — not present.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 stroke primitives (s2 = 2 segments for 横折)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all P joints welded (s3⇆s4 mid-cross); N joints hold small natural gaps
    'overall_pass': True,
    'notes': '畀: 8 strokes. 田-frame on top, wide heng below, then 丿+丨 legs.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code")

from _anchor import anchor_to_xy, fat_line

WIDTH = 8

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 田 frame (strokes 1-5) ----

# s1 — left shu of 田
#      head TL(0.803, 0.873) → tail C(0.055, 0.693)
p1_head = anchor_to_xy(('TL', 0.803, 0.873))
p1_tail = anchor_to_xy(('C',  0.055, 0.693))
fat_line(draw, p1_head, p1_tail, WIDTH)

# s2 — 横折 (top bar + right wall). Split into two segments at the corner.
#      head TL(0.967, 0.885) → tail C(0.808, 0.603)
p2_head   = anchor_to_xy(('TL', 0.967, 0.885))
p2_tail   = anchor_to_xy(('C',  0.808, 0.603))
p2_corner = (p2_tail[0], p2_head[1])  # right-and-down: bend at (tail.x, head.y)
fat_line(draw, p2_head,   p2_corner, WIDTH)
fat_line(draw, p2_corner, p2_tail,   WIDTH)

# s3 — inner middle heng of 田 (welded across spine at C-mid)
#      head C(0.198, 0.254) → tail C(0.755, 0.181)
p3_head = anchor_to_xy(('C', 0.198, 0.254))
p3_tail = anchor_to_xy(('C', 0.755, 0.181))
fat_line(draw, p3_head, p3_tail, WIDTH)

# s4 — middle spine of 田
#      head TC(0.386, 0.914) → tail C(0.421, 0.518)
p4_head = anchor_to_xy(('TC', 0.386, 0.914))
p4_tail = anchor_to_xy(('C',  0.421, 0.518))
fat_line(draw, p4_head, p4_tail, WIDTH)

# s5 — bottom heng closing the 田 frame
#      head C(0.107, 0.649) → tail C(0.796, 0.521)
p5_head = anchor_to_xy(('C', 0.107, 0.649))
p5_tail = anchor_to_xy(('C', 0.796, 0.521))
fat_line(draw, p5_head, p5_tail, WIDTH)

# ---- 丌 base (strokes 6-8) ----

# s6 — long wide heng under 田
#      head BL(0.431, 0.001) → tail MR(0.634, 0.901)
p6_head = anchor_to_xy(('BL', 0.431, 0.001))
p6_tail = anchor_to_xy(('MR', 0.634, 0.901))
fat_line(draw, p6_head, p6_tail, WIDTH)

# s7 — 丿 left leg
#      head BL(0.996, 0.039) → tail BL(0.621, 0.924)
p7_head = anchor_to_xy(('BL', 0.996, 0.039))
p7_tail = anchor_to_xy(('BL', 0.621, 0.924))
fat_line(draw, p7_head, p7_tail, WIDTH)

# s8 — 竖 right leg (slightly rightward slant)
#      head C(0.737, 0.957) → tail BC(0.837, 1.044) — tail clipped at canvas edge
p8_head = anchor_to_xy(('C',  0.737, 0.957))
p8_tail = anchor_to_xy(('BC', 0.837, 1.044))
fat_line(draw, p8_head, p8_tail, WIDTH)

OUT = os.path.join(_HERE, '01_畀.png')
img.save(OUT)
print("Saved", OUT)
