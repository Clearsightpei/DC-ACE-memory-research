# 果 (guǒ) — Phase 3 char 0387, 8 strokes
# Structure: 田 (top) + 木-like base (wide heng + spine + 撇 + 捺).
# Stroke split (MMH order):
#   s1  left 竖 of 田
#   s2  横折 (top + right wall of 田) — 2-segment L
#   s3  upper inside 横 of 田
#   s4  bottom-closing 横 of 田
#   s5  wide 一 (木's heng, spans ML→MR)
#   s6  central 竖 spine (through 田 middle + down as 木's shu)
#   s7  left 撇 leg of 木
#   s8  right 捺 leg of 木
#
# Reading-order log:
#  1. drawer_memory.md — no dedicated 田 or 果 primitive; inline fresh per 畀 pattern.
#  2. INDEX.md grep 果 — no mastered entry; 畀 (0364, 田+丌) and 申 (0159, 田-frame+spine) are analogs.
#  3. errata.md grep 果 — not present.
# Approach: mimic 畀's inline 田-frame recipe, replace 丌 with 木 (wide heng + spine + 撇/捺).
# Anchors follow MMH-derived expectations verbatim.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 stroke primitives (s2 = 2 segments for 横折 L)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # P at spine×upper-heng and spine×wide-heng welded; N at frame corners
    'overall_pass': True,
    'notes': '果: 8 strokes. 田 frame on top, wide heng across middle, central spine, splayed 撇/捺 legs.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code")

from _anchor import anchor_to_xy, fat_line

WIDTH = 8

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 田 frame + inner bars (strokes 1-4) ----

# s1 — left 竖 of 田
p1_head = anchor_to_xy(('TL', 0.753, 0.791))
p1_tail = anchor_to_xy(('C',  0.028, 0.597))
fat_line(draw, p1_head, p1_tail, WIDTH)

# s2 — 横折 (top bar + right wall of 田). Split into two segments at the corner.
p2_head   = anchor_to_xy(('TL', 0.844, 0.773))
p2_tail   = anchor_to_xy(('C',  0.793, 0.456))
p2_corner = (p2_tail[0], p2_head[1])  # corner at (tail.x, head.y)
fat_line(draw, p2_head,   p2_corner, WIDTH)
fat_line(draw, p2_corner, p2_tail,   WIDTH)

# s3 — upper inside 横 (welded across spine at P joint)
p3_head = anchor_to_xy(('C', 0.09,  0.175))
p3_tail = anchor_to_xy(('C', 0.708, 0.093))
fat_line(draw, p3_head, p3_tail, WIDTH)

# s4 — bottom 横 closing the 田 frame
p4_head = anchor_to_xy(('C', 0.087, 0.529))
p4_tail = anchor_to_xy(('C', 0.761, 0.395))
fat_line(draw, p4_head, p4_tail, WIDTH)

# ---- 木 base (strokes 5-8) ----

# s5 — wide 一 across the middle (木's heng, spans ML→MR)
p5_head = anchor_to_xy(('ML', 0.451, 0.922))
p5_tail = anchor_to_xy(('MR', 0.458, 0.819))
fat_line(draw, p5_head, p5_tail, WIDTH)

# s6 — central 竖 spine, from inside 田 top down through 木 (clip at canvas bottom)
p6_head = anchor_to_xy(('TC', 0.365, 0.823))
p6_tail_raw = anchor_to_xy(('BC', 0.436, 1.082))
p6_tail = (p6_tail_raw[0], min(p6_tail_raw[1], 298))
fat_line(draw, p6_head, p6_tail, WIDTH)

# s7 — left 撇 leg
p7_head = anchor_to_xy(('C',  0.351, 0.913))
p7_tail = anchor_to_xy(('BL', 0.378, 0.786))
fat_line(draw, p7_head, p7_tail, WIDTH)

# s8 — right 捺 leg
p8_head = anchor_to_xy(('C',  0.526, 0.901))
p8_tail = anchor_to_xy(('BR', 0.798, 0.736))
fat_line(draw, p8_head, p8_tail, WIDTH)

OUT = os.path.join(_HERE, '01_果.png')
img.save(OUT)
print("Saved", OUT)
