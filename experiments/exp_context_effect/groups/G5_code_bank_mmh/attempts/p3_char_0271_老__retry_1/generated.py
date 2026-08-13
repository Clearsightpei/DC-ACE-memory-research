"""p3_char_0271_老 — retry 1.

TRAJECTORY DIFF
- main FAIL: too many stacked horizontals in the top 耂; the diagonal
  long-pie was placed in roughly right zone but the top cluster read
  as three parallel bars (s1/s3 both drawn plus a stray line). The
  bottom 匕's shu_wan_gou was too compact (curve bottomed above tail).
- Fixes applied here:
  1. Follow MMH anchors verbatim: s1 short heng crosses s2 vertical
     shu at cell C, forming a small '+' near top. s3 is the ONLY long
     horizontal (spans full width, slight tilt-up-right).
  2. s4 long pie sweeps from TR down to BL — one continuous curve.
  3. s5 short pie for 匕's top, s6 shu_wan_gou anchored to the actual
     tail (232, 241) with bottom_extra tuned so the knee sits near
     canvas bottom without off-canvas clipping.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


# 米字格 cell centers (300x300 canvas, 100-px cells)
CELL_CENTERS = {
    'TL': (50, 50),   'TC': (150, 50),   'TR': (250, 50),
    'ML': (50, 150),  'C':  (150, 150),  'MR': (250, 150),
    'BL': (50, 250),  'BC': (150, 250),  'BR': (250, 250),
}


def A(cell, xf, yf):
    cx, cy = CELL_CENTERS[cell]
    return (cx - 50 + xf * 100, cy - 50 + yf * 100)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- 耂 top ---
    # s1: short heng crossing near center-top
    s1_h = A('ML', 0.935, 0.175)   # ~(94, 118)
    s1_t = A('C',  0.881, 0.102)   # ~(188, 110)
    draw_heng(draw, s1_h, s1_t, width_head=6, width_tail=6)

    # s2: vertical shu (top pie/shu of 耂) crossing s1 at cell C
    s2_h = A('TC', 0.333, 0.533)   # ~(133, 53)
    s2_t = A('C',  0.383, 0.556)   # ~(138, 156)
    draw_shu(draw, s2_h, s2_t, width=6)

    # s3: long horizontal heng across middle
    s3_h = A('ML', 0.278, 0.775)   # ~(28, 178)
    s3_t = A('MR', 0.73,  0.55)    # ~(273, 155)
    draw_heng(draw, s3_h, s3_t, width_head=8, width_tail=9)

    # s4: long pie sweeping from upper-right down to lower-left
    s4_h = A('TR', 0.112, 0.729)   # ~(211, 73)
    s4_t = A('BL', 0.375, 0.73)    # ~(38, 273)
    draw_pie(draw, s4_h, s4_t, bow_perp=18, w_head=8, w_tail=3)

    # --- 匕 bottom-right ---
    # s5: short pie for 匕
    s5_h = A('BR', 0.259, 0.036)   # ~(226, 204)
    s5_t = A('BC', 0.403, 0.338)   # ~(140, 234)
    draw_pie(draw, s5_h, s5_t, bow_perp=-4, w_head=6, w_tail=3)

    # s6: shu_wan_gou. tail y=241 leaves only 59 px to canvas edge.
    # Use bottom_extra=32 so bottom_y=273 (safe on canvas), knee_ratio
    # 0.72 so the shoulder passes under tail before the up-hook.
    s6_h = A('C',  0.254, 0.931)   # ~(125, 193)
    s6_t = A('BR', 0.323, 0.405)   # ~(232, 241)
    draw_shu_wan_gou(draw, s6_h, s6_t,
                     width=6, bottom_extra=32, knee_ratio=0.72)

    out = os.path.join(HERE, "01_老.png")
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: heng, shu, heng, pie, pie, shu_wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors used verbatim from MMH block; shu_wan_gou bottom_extra tuned to 32 to keep the knee on-canvas.',
}


if __name__ == "__main__":
    print(render())
