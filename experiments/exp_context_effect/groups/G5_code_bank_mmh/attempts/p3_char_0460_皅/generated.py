# BANK_DEVIATION
# skipped: bai_white.py
# reason: bai_white native footprint is ~150 wide x 140 tall (aspect 1.07), but
#   in 皅 the left 白 is compressed into ML/BL columns only — MMH anchors give
#   box top-left (54.8, 191.0) to bottom-right (103.1, 288.9), i.e. ~48 wide x
#   ~98 tall (aspect 0.49). Native/target aspect ratio = 1.07 / 0.49 = 2.18x
#   mismatch on x/y — a pure uniform-scale call cannot deliver the narrow
#   tall left-radical 白 form. Per P-A-009 (quantitative BANK_DEVIATION),
#   inline all 5 白 strokes at MMH anchors with a stroke-primitive layer
#   (P-A-006).
# fresh_component: bai_left_narrow_for_皅
#
# P-A-006 note: bai_left + 巴 (no bank primitive for 巴) — inline all 9
# strokes at MMH anchors verbatim; use stroke primitives (pie/shu/heng/
# heng_zhe_box/shu_wan_gou) as the render layer.
#
# P-A-007-v2 hard-check: bai_white DOES exist for 白 but this is left-radical
# 白, not standalone 白 — anchor footprint verifies mismatch (see aspect calc
# above); skip is justified. No 巴 bank primitive exists so nothing to check
# there.

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu_wan_gou import draw_shu_wan_gou


# --- MMH anchors resolved to 300x300 pixel space (100x100 cells, y grows down)
# Cell origins: ML=(0,100) BL=(0,200) BC=(100,200) C=(100,100) MR=(200,100) BR=(200,200)
# 白 (strokes 1-5, left radical, compressed)
S1_HEAD = (79.7, 136.8);  S1_TAIL = (58.3, 186.6)   # 撇 pie
S2_HEAD = (41.0, 186.3);  S2_TAIL = (58.9, 281.0)   # 竖 shu (left of box)
S3_HEAD = (54.8, 191.0);  S3_TAIL = (103.1, 288.9)  # 横折 box (top+right)
S4_HEAD = (62.7, 232.6);  S4_TAIL = (87.9, 227.6)   # middle heng
S5_HEAD = (63.3, 274.8);  S5_TAIL = (95.2, 266.0)   # bottom heng (closes box)

# 巴 (strokes 6-9, right radical)
S6_HEAD = (147.7, 162.0); S6_TAIL = (210.1, 192.5)  # top heng-zhe (top+right of upper box)
S7_HEAD = (175.2, 166.4); S7_TAIL = (173.1, 198.9)  # short shu (right side of upper box)
S8_HEAD = (145.6, 215.6); S8_TAIL = (227.6, 204.2)  # middle heng
S9_HEAD = (133.3, 159.4); S9_TAIL = (262.5, 230.0)  # 竖弯钩 shu-wan-gou (long wrap)


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- 白 left radical ---
# s1: 撇 pie — top slash, thin taper
draw_pie(draw, S1_HEAD, S1_TAIL, bow_perp=5, w_head=5, w_tail=2, steps=60)
# s2: left 竖 shu
draw_shu(draw, S2_HEAD, S2_TAIL, width=5)
# s3: 横折 box (top+right of 白 box)
draw_heng_zhe_box(draw, S3_HEAD, S3_TAIL, width=5)
# s4: middle heng (thinner, short)
draw_heng(draw, S4_HEAD, S4_TAIL, width_head=4, width_tail=5)
# s5: bottom heng (closes box)
draw_heng(draw, S5_HEAD, S5_TAIL, width_head=4, width_tail=5)

# --- 巴 right radical ---
# s6: top heng-zhe (top + short right drop). Use heng_zhe_box with
#     top-left = s6 head, bottom-right = s6 tail. Yields the horizontal
#     top of 巴's upper compartment plus a short right vertical.
draw_heng_zhe_box(draw, S6_HEAD, S6_TAIL, width=6)
# s7: short 竖 shu — left vertical of the upper box (finishing the
#     compartment; joins s6 mid on top and s8 mid on bottom).
draw_shu(draw, S7_HEAD, S7_TAIL, width=6)
# s8: middle heng — crosses the middle of 巴, slight rise toward right.
draw_heng(draw, S8_HEAD, S8_TAIL, width_head=6, width_tail=7)
# s9: 竖弯钩 — long wrap. Descends from top (~133,159), curves along
#     bottom rightward, and hooks up-right ending at (262, 230).
#     Reduce bottom_extra so the curve's bottom sits ~y=270 (matches
#     GT footprint) rather than the default ~y=290. Slightly larger
#     knee_ratio so the horizontal shoulder sits further right, giving
#     the 巴 body room to close.
draw_shu_wan_gou(draw, S9_HEAD, S9_TAIL, width=6,
                 bottom_extra=42, knee_ratio=0.82)


out = Path(__file__).parent / '01_皅.png'
img.save(out)


SELF_CHECK = {
    'visual_ok': None,             # set after render + GT compare
    'stroke_count_ok': True,       # 9 primitive calls (5 白 + 4 巴)
    'endpoint_mismatches': [],     # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # all 12 expected joints are class N; each
                                   # is drawn as a natural small gap (no
                                   # explicit welding, no forced piercing)
    'overall_pass': None,
    'notes': ('BANK_DEVIATION on bai_white due to 2.18x aspect mismatch — '
              'inline 白 at MMH anchors per P-A-006 + P-A-009. 巴 has no '
              'bank primitive; inline all 4 strokes with stroke-primitive '
              'layer.'),
}
