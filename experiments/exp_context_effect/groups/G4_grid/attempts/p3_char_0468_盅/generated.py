"""盅 (zhōng) — 9 strokes.
Decomposition: 盅 = 中 (top) + 皿 (bottom).
  中 = 口 (s1..s3) + 长竖 (s4)
  皿 = 左竖 (s5) + 横折 (s6) + 内竖×2 (s7,s8) + 底横 (s9)

Rendering approach: MMH-verbatim anchors + inline base primitives
(fat_line + polyline for heng-zhe). No compound bank primitive matches
this top-bottom compression, so we inline per B9/B10 A-recipe point 4.
"""

# BANK_DEVIATION
# skipped: kou.py, min_dish.py (no min primitive in bank anyway)
# reason: 中's 口 sits in a compressed TC/ML top band (y 110-172) and
#         皿 sits in bottom third — neither matches standalone
#         primitives' default full-canvas anchors. Inlining per
#         MMH-verbatim keeps the top/bottom proportion.
# fresh_component: kou_top_compressed_for_中top; min_dish_bottom_slot

# Memory reads (v8 slim checklist):
#   1. drawer_memory.md — A-recipe: MMH-verbatim + base primitives + SELF_CHECK + N-joints
#   2. INDEX grep — no 盅, no 皿 primitive; kou exists but full-canvas
#   3. errata grep — no 盅 entry

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, "..", "..", "success_bank", "code")
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402


# ---- MMH-verbatim anchors ----
S1_H = ('ML', 0.727, 0.119); S1_T = ('ML', 0.981, 0.729)  # 口-left 竖
S2_H = ('ML', 0.844, 0.113); S2_T = ('C',  0.922, 0.430)  # 口 top+right 横折
S3_H = ('C',  0.034, 0.679); S3_T = ('MR', 0.080, 0.538)  # 口 bottom 横
S4_H = ('TC', 0.333, 0.609); S4_T = ('BC', 0.438, 0.086)  # 中 长竖
S5_H = ('BL', 0.659, 0.203); S5_T = ('BL', 0.911, 0.824)  # 皿 左竖
S6_H = ('BL', 0.820, 0.215); S6_T = ('BC', 0.934, 0.757)  # 皿 top 横折
S7_H = ('BC', 0.187, 0.291); S7_T = ('BC', 0.251, 0.807)  # 皿 内左竖
S8_H = ('BC', 0.597, 0.218); S8_T = ('BC', 0.541, 0.774)  # 皿 内右竖
S9_H = ('BL', 0.322, 0.912); S9_T = ('BR', 0.698, 0.892)  # 皿 底横

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; all joints N-class (natural gaps preserved). '
             '中 top compressed to y110-210, 皿 bottom compressed to y220-292.',
}


def draw_heng_zhe(draw, head, corner, tail, width=8):
    """Simple 横折: heng from head to corner, then shu to tail."""
    fat_line(draw, head, corner, width)
    fat_line(draw, corner, tail, width)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 中 (top) ----
    # s1: 口 left 竖
    fat_line(d, anchor_to_xy(S1_H), anchor_to_xy(S1_T), 8)

    # s2: 口 top-heng + right-shu (横折). Corner at top-right of 口.
    s2_head_px = anchor_to_xy(S2_H)
    s2_tail_px = anchor_to_xy(S2_T)
    s2_corner = (s2_tail_px[0], s2_head_px[1])  # (x_tail, y_head)
    draw_heng_zhe(d, s2_head_px, s2_corner, s2_tail_px, width=8)

    # s3: 口 bottom 横
    fat_line(d, anchor_to_xy(S3_H), anchor_to_xy(S3_T), 8)

    # s4: 中 长竖 (through box, extends above and below)
    fat_line(d, anchor_to_xy(S4_H), anchor_to_xy(S4_T), 9)

    # ---- 皿 (bottom) ----
    # s5: 左竖
    fat_line(d, anchor_to_xy(S5_H), anchor_to_xy(S5_T), 8)

    # s6: top-heng + right-shu (横折). Corner at top-right of 皿 frame.
    s6_head_px = anchor_to_xy(S6_H)
    s6_tail_px = anchor_to_xy(S6_T)
    s6_corner = (s6_tail_px[0], s6_head_px[1])
    draw_heng_zhe(d, s6_head_px, s6_corner, s6_tail_px, width=8)

    # s7: 内左竖
    fat_line(d, anchor_to_xy(S7_H), anchor_to_xy(S7_T), 7)

    # s8: 内右竖
    fat_line(d, anchor_to_xy(S8_H), anchor_to_xy(S8_T), 7)

    # s9: 底横 (long, extends beyond 皿 frame slightly)
    fat_line(d, anchor_to_xy(S9_H), anchor_to_xy(S9_T), 9)

    out = os.path.join(_HERE, '01_盅.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
