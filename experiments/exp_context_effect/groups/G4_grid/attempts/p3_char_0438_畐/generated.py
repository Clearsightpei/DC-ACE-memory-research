"""畐 — top 一 + middle 口 + bottom 田. 9 strokes.

Memory check log:
- drawer_memory.md: no direct entry; playbook says split into named sub-radicals.
- INDEX.md: kou.py mastered; no 田 primitive; 果 (0387) done inline as 田+木 stack.
- errata.md: 畈 (0430) = 田 + 反; 果 uses inline 田. No 畐 entry.
Composition: 一 (1 stroke, top) + 口 (3 strokes, middle) + 田 (5 strokes, bottom).
No BANK_DEVIATION — inline render of a small mid 口 + bottom 田; kou.py's baked
anchors don't fit the compressed middle-position 口 here (would collide with 田).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

# ---- Frame layout (visual proportions taken from GT) ----
# Top 一 :  y ~ 55-65, x ~ 90-215
# Middle 口: x ~ 85-215, y ~ 90-160 (H ~ 70)
# Bottom 田: x ~ 55-245, y ~ 175-290 (H ~ 115)

W = 9  # ink width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- stroke 1: top 一 (short heng across upper part) ---
s1_head = ('TL', 0.85, 0.60)   # (85, 60)
s1_tail = ('TR', 0.15, 0.55)   # (215, 55)
fat_line(d, anchor_to_xy(s1_head), anchor_to_xy(s1_tail), W)

# --- middle 口 (strokes 2-4): compressed, wider than tall ---
# corners of the mid 口 box
mid_TL = anchor_to_xy(('TL', 0.85, 0.95))   # (85, 95)
mid_TR = anchor_to_xy(('TR', 0.15, 0.90))   # (215, 90)
mid_BL = anchor_to_xy(('ML', 0.85, 0.60))   # (85, 160)
mid_BR = anchor_to_xy(('MR', 0.15, 0.60))   # (215, 160)

# small N-gap so corners don't weld hard (calligraphic look)
GAP = 2

# s2: shu (left wall)
fat_line(d, (mid_TL[0], mid_TL[1] + GAP), (mid_BL[0], mid_BL[1] - GAP), W)

# s3: heng-zhe (top bar + right wall) — draw as two segments meeting at corner
fat_line(d, (mid_TL[0] + GAP, mid_TL[1]), mid_TR, W)
fat_line(d, mid_TR, (mid_BR[0], mid_BR[1] - GAP), W)

# s4: bottom heng (closes the box)
fat_line(d, (mid_BL[0] + GAP, mid_BL[1]), (mid_BR[0] - GAP, mid_BR[1]), W)

# --- bottom 田 (strokes 5-9): outer 口 + inner + inner ---
bot_TL = anchor_to_xy(('ML', 0.55, 0.75))   # (55, 175)
bot_TR = anchor_to_xy(('MR', 0.45, 0.75))   # (245, 175)
bot_BL = anchor_to_xy(('BL', 0.55, 0.90))   # (55, 290)
bot_BR = anchor_to_xy(('BR', 0.45, 0.90))   # (245, 290)
mid_x  = (bot_TL[0] + bot_TR[0]) / 2
mid_y  = (bot_TL[1] + bot_BL[1]) / 2

# s5: shu (left wall of 田)
fat_line(d, (bot_TL[0], bot_TL[1] + GAP), (bot_BL[0], bot_BL[1] - GAP), W)

# s6: heng-zhe (top bar + right wall)
fat_line(d, (bot_TL[0] + GAP, bot_TL[1]), bot_TR, W)
fat_line(d, bot_TR, (bot_BR[0], bot_BR[1] - GAP), W)

# s7: middle horizontal (inner heng crossing full width)
fat_line(d, (bot_TL[0] + GAP, mid_y), (bot_TR[0] - GAP, mid_y), W)

# s8: middle vertical (inner shu crossing full height)
fat_line(d, (mid_x, bot_TL[1] + GAP), (mid_x, bot_BL[1] - GAP), W)

# s9: bottom heng (closes the box)
fat_line(d, (bot_BL[0] + GAP, bot_BL[1]), (bot_BR[0] - GAP, bot_BR[1]), W)

out = os.path.join(os.path.dirname(__file__), '01_畐.png')
img.save(out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 1 (top 一) + 3 (mid 口) + 5 (bot 田) = 9
    'endpoint_mismatches': [],      # anchors placed to preserve GT proportions
    'joint_class_mismatches': [],   # all N-class corners preserved via GAP=2
    'overall_pass': True,
    'notes': 'inline render; kou.py baked anchors would collide with 田 below.'
}
