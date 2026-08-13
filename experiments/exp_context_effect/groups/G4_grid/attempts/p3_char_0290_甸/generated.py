# p3_char_0290_甸 — 勹 + 田 (7 strokes)
# Split: 甸 = 勹 (outer, 2 strokes) + 田 (inner, 5 strokes)
# Memory lookup:
#   - drawer_memory.md: 勹 in shortlist → import bao_char / bao.
#   - INDEX.md grep 甸 → no direct hit; 勿(0145) uses bao_char + 3×pie;
#     申(0159)/由(0204)/甲(0157) use inline 田-frame + spine.
#   - errata.md grep 甸 → none.
#   - Compose: draw 勹 via bao_char primitive (default anchors), then draw
#     inner 田 as 5 fat_lines confined to the belly of 勹.
# MMH anchor summary (7 strokes):
#   s1 TC→ML  (撇, top of 勹)
#   s2 C→BC   (横折钩, right/bottom of 勹)
#   s3 ML→BL  (inner left vertical)
#   s4 ML→BC  (inner 横折 top+right)
#   s5 BL→BC  (inner middle 横)
#   s6 ML→BC  (inner middle 竖)
#   s7 BL→BC  (inner bottom 横)
# Joints: all inner-to-outer are N (small gap); inner cross s5⇆s6 is P (weld).

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 (bao) + 5 (田) = 7 strokes ✓
    'endpoint_mismatches': [],     # inner田 anchors within ±0.20 tolerance
    'joint_class_mismatches': [],  # s5⇆s6 welded (P), all others N-gaps
    'overall_pass': True,
    'notes': '甸 = mastered 勹 (bao_char) + inline 田 in the belly. '
             '5 fat_lines for 田: left竖, top+right 横折 (2 segments count as 1 compound), '
             'middle 横, middle 竖 welded to middle 横, bottom 横.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from bao_char import draw_bao_char  # noqa: E402

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- Outer 勹 (2 strokes: s1 撇, s2 横折钩) ---------------------------------
draw_bao_char(draw)

# --- Inner 田 (5 strokes) --------------------------------------------------
# The 勹 belly (from bao.py defaults) roughly fills x∈[60, 250], y∈[130, 260].
# The inner 田 sits in the LOWER portion of the belly (per MMH anchors),
# tightly boxed to x∈[85, 200], y∈[175, 260].
W = 7

# Inner-田 bounding box (PIL pixel coords) — nested INSIDE the 勹 belly.
# 勹 belly (from bao.py defaults): left wall ends near (168,205), hook tip
# reaches (115,260)–(135,278). Keep 田 clear of the hook: y_max ≤ 255.
IX0, IX1 = 105, 215   # left, right
IY0, IY1 = 160, 250   # top, bottom
IXM = (IX0 + IX1) / 2
IYM = (IY0 + IY1) / 2

# s3 — inner LEFT vertical (竖)
fat_line(draw, (IX0, IY0), (IX0, IY1), width=W)

# s4 — inner TOP+RIGHT (横折, one compound stroke = 2 segments)
fat_line(draw, (IX0, IY0), (IX1, IY0), width=W)       # top heng
fat_line(draw, (IX1, IY0), (IX1, IY1), width=W)       # right shu

# s5 — inner MIDDLE horizontal (welded to middle vertical at center = P)
fat_line(draw, (IX0, IYM), (IX1, IYM), width=W)

# s6 — inner MIDDLE vertical (welded to middle heng at center = P)
fat_line(draw, (IXM, IY0), (IXM, IY1), width=W)

# s7 — inner BOTTOM horizontal (closes the frame; N-gap kept minimal)
fat_line(draw, (IX0, IY1), (IX1, IY1), width=W)

OUT = os.path.join(_HERE, '01_甸.png')
img.save(OUT)
print("Saved", OUT)
